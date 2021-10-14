import copy
import re
import scrapy
from guaiben_redis.items import GuaibenItem, GuaibenItem2
import get_number
from get_number import output_id_data
from scrapy_redis.spiders import RedisSpider

class IndexSpider(RedisSpider):
    name = 'guaiben'
    redis_key = 'guaiben'

    def __init__(self, *args, **Kwargs):
        domain = Kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(IndexSpider, self).__init__(*args, **Kwargs)

    def parse(self, response):
        print(response.headers)
        if int(response.status) == 200:
            item = GuaibenItem()
            item['title_data'] = response.xpath('//div[@id="intro"]/p[1]/text()').extract_first()  # 小说标题
            item['name_data'] = response.xpath("//div[@id='info']/h1/text()").extract_first()  # 小说名字
            item['type_data'] = response.xpath("//div[@id='info']/p[1]/text()").extract_first()  # 小说类型
            panduan_data = response.xpath('//dl/dd[2]/a/text()').extract_first()
            if '章' in str(panduan_data):
                yield item
                item2 = GuaibenItem2()
                book_id = output_id_data.search_id(item['name_data'])  # 查询book_id
                ji_data = response.xpath('//dl/dd')
                for i in ji_data:
                    xs_data = i.xpath('./a/text()').extract_first()  # 章值
                    if '章' in str(xs_data):
                        item2['book_id'] = book_id
                        data = re.split(r'章', xs_data)[1]  # 获取章名字
                        zhang_name = data.replace(' ', '')
                        pattern = r"第.+章|^.+章"
                        zhang_data = re.findall(pattern, xs_data)[0]  # 章名字
                        patterns = r'\d+'
                        match = re.findall(patterns, zhang_data)  # 检测有无数字
                        if match:
                            zhang = match[0]  # 数字
                            rules = '第' + output_id_data.numbers(zhang) + '章'  # 第i章
                        else:
                            rules = zhang_data
                        item2['rules'] = rules
                        item2['zhang_name'] = zhang_name
                        page_data = i.xpath('./a/@href').extract_first()  # 章数地址
                        end_url = 'http://www.guaiben.com/' + page_data
                        yield scrapy.Request(end_url, callback=self.get_xs_data, meta={'item': copy.deepcopy(item2)},
                                             dont_filter=True)
                    else:
                        print('已过滤', xs_data)
                        pass
            else:
                pass
        else:
            pass

    def get_xs_data(self, response):
        item2 = response.meta['item']
        text = response.xpath('//*[@id="content"]/text()').extract()
        text_ends = ''
        for i in text:
            text_end = i + ' '
            text_ends += text_end
        content = text_ends
        item2['content'] = "".join(content.split())
        yield item2
