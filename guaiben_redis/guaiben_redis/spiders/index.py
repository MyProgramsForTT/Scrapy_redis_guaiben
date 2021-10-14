import scrapy
from guaiben_redis.items import GuaibenItem
from urllib.parse import parse_qs
from scrapy_redis.spiders import RedisSpider


class IndexSpider(RedisSpider):
    name = 'index'
    #allowed_domains = ['search.jd.com']
    #start_urls = ['https://search.jd.com/Search?keyword=%E4%B9%A6&wq=%E4%B9%A6&pvid=6263ebbb3cf1443295fe83781685cc74&page=3&s=56&click=0']
    redis_key = 'JD'
    def __init__(self,*args,**Kwargs):
        domain = Kwargs.pop('domain','')
        self.allowed_domains = list(filter(None,domain.split(',')))
        super(IndexSpider,self).__init__(*args,**Kwargs)
    def parse(self, response):
        items = JdScrapyItem()
        books_msgs = response.xpath("//div[@id='J_goodsList']")
        books_msg = books_msgs.xpath("./ul/li")
        for i in books_msg:
            items['goods_url'] = 'https:' +i.xpath(".//div[@class='p-img']/a/@href").extract_first()
            items['price'] = i.xpath(".//i/text()").extract_first()
            items['name'] = ' '.join(i.xpath(".//div[@class='p-name']/a/em/text()").extract())
            items['store'] = i.xpath(".//div[@class='p-shopnum']/a/@title").extract_first()
            yield items

        next_url = str(response.url)
        zd = dict([(k, v[0]) for k, v in parse_qs(next_url.split('?', 1)[1]).items()])
        page_data = int(zd['page'])+2
        if page_data<200:
            next_url = 'https://search.jd.com/Search?keyword=书&wq=书&pvid=6263ebbb3cf1443295fe83781685cc74&page={}'.format(page_data)
            yield scrapy.Request(next_url,callback=self.parse)
        else:
            print('SUCCESS TO THE END PAGE!')
