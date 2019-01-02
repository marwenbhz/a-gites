from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from a_gites.spiders.a_gitesspider.py import AGitesspiderSpider


process = CrawlerProcess(get_project_settings())
process.crawl(AGitesspiderSpider)
process.start()
