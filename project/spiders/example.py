# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from datetime import datetime

from selenium.webdriver.common.keys import Keys
from project.selenium import browser

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/']

    def __init__(self, *args, **kwargs):
        self.browser = browser

    def parse(self, response):
        self.browser.get(self.start_urls[0])  # init request
        sleep(5)
         # find and fill user and password fields
        searchInput = self.browser.find_elements_by_css_selector('input.gLFyf')
        searchInput[0].send_keys('Wikipedia')
        searchInput[0].send_keys(Keys.ENTER) # simulate key ENTER
        sleep(3)
        self.browser.close()
