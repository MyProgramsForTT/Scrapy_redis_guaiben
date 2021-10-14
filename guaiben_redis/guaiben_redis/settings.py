SPIDER_MODULES = ['guaiben_redis.spiders']
NEWSPIDER_MODULE = 'guaiben_redis.spiders'
ROBOTSTXT_OBEY=False

#USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'guaiben_redis.pipelines.MysqlPipeline3': 300,
}

#LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 0
#REDIS_URL = 'redis://root:5555@127.0.0.1:6379'
REDIS_URL = 'redis://root:5555@192.168.10.106:6379'

