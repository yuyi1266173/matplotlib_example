# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

import sys
sys.path.append('D:\Python3\workPlace\GitWorkPlace\matplotlib_example\matplotlib_example')

from items import MatplotlibExampleItem


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css = 'div.toctree-wrapper.compound', \
        	deny = '/index.html$')
        links = le.extract_links(response)
        print( len(links) )

        for link in links:
        	yield scrapy.Request(link.url, callback = self.parse_example)

    def parse_example(self, response):
    	href = response.css('a.reference.external::attr(href)').extract_first()
    	url = response.urljoin(href)

    	example = MatplotlibExampleItem()
    	example['file_urls'] = [url]

    	return example