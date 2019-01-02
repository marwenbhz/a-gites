# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from a_gites.items import AGitesItem


class AGitesspiderSpider(scrapy.Spider):
    name = 'a_gitesspider'
    allowed_domains = ['a-gites.com']
    start_urls = ['https://www.a-gites.com/locations-vacances-en-france.php']
    custom_settings = {
    'LOG_FILE': 'logs/a_gites.log',
    'LOG_LEVEL':'ERROR'
     }


    def __init__(self, *args, **kwargs):
        super(AGitesspiderSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        print('PROCESSING LOCATIONS...' + response.url)
	locations = response.css('div.bloc')
	for location in locations:
	    link_location = location.css('a.decouvrir::attr(href)').extract_first()
	    title = location.css('h3::text').extract_first()
	    yield Request(link_location, callback=self.parse_location, meta={'link_location': link_location})


    def parse_location(self, response):
	print('PROCESSING ANNONCES...' + response.url)
        link_location = response.url
	annonces = response.css('li.lp-ad-list-item')
	#for annonce in annonces:
	link_annonce = response.css('a.lp-ad-item-title-link::attr(href)').extract_first()
        yield Request(link_annonce, callback=self.parse_annonce, meta={'link_annonce': link_annonce, 'link_location': link_location})


	# Get relative next url with css selector.
	#relative_next_url = response.css('li.lp-pager-list-item > a::attr(href)').extract_first()
	#relative_next_url = response.xpath('//li[@class="lp-pager-list-item"]//a/@href').extract()
	#for i in range(0, len(relative_next_url)):
	#    yield Request(relative_next_url[i], callback=self.parse_location)



    '''
    def parse_annonce(self, response):
	print('PROCESSING ANNONCE DETAILS...' + response.url)

	item = AGitesItem()
	try:
	    item['TITLE_LOCATION'] = response.css('h1.gen-font-roboto-light::text').extract_first().strip()
	except:
	    print('ERROR PARSE TITLE LOCATION...' + response.url)
	try:
	    item['TITLE_ANNONCE'] = response.css('div.dpv3-title-block > h2::text').extract_first().strip()
	except:
	    print('ERROR PARSE TITLE ANNONCE...' + response.url)

	try:
	    price = response.css('p.gen-font-size-29 > a::text').extract()
	    comment = response.css('p.gen-font-size-14 > a::text').extract()
	    item['PRICE'] = price[0] + ' ' + comment[0] if len(price) == 1 else price[0] + ' ' + comment[0] + ' ' + price[1] + ' ' + comment[1]
	except:
	    print('ERROR PARSE PRICE...' + response.url)

	try:
	    item['LINK_ANNONCE'] = response.url
	except:
	    print('ERROR PARSE LINK ANNONCE...' + response.url)
	try:
	    item['LINK_ANNONCES'] = response.meta.get('link_annonces')
	except:
	    print('ERROR PASS LINK ANNONCES...' + response.url)
	try:
	    item['LINK_LOCATION'] = response.meta.get('link_location')
	except:
	    print('ERROR PASS LINK LOCATION...' + response.url)

	try:
	    item['OWNER'] = response.css('div.dpv3-owner-name::text').extract_first().strip()
	except:
	    print('ERROR PARSE OWNER...' + response.url)

	try:
	    item['DESCRIPTION'] = response.css('p.gen-disable-defaults::text').extract_first().strip()
	except:
	    print('ERROR PARSE DESCRIPTION...' + response.url)

	try:
	    adress = response.css('div.dpv3-location-title-block > h2::text').extract_first()[14:]
	    index_pos = adress.index(' ')
	    VILLE = adress[:index_pos-1]
	    CODE_POSTAL = adress[index_pos+1:]
	    print(VILLE)
	    print(CODE_POSTAL)
	except:
	    print('ERROR PARSE VILLE & CODE_POSTAL...' + response.url)

	try:
	    item['TYPE_LOGEMENT'] = response.css('span.gen-font-strong > strong::text').extract_first().strip()
	except:
	    print('ERROR TYPE_LOGEMENT PARSE...' + response.url)


	try:
	    item['CAPACITE'] = response.css('span.gen-font-strong').extract_first().strip()
	except:
	    print('ERROR CAPACITE  PARSE...' + response.url)

	try:
	    item[''] = response.css('span.').extract_first().strip()
	except:
	    print()

	yield item

	'''