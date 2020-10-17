from urllib.parse import urlsplit
import scrapy
from scrapy.crawler import CrawlerProcess
from typing import List, Dict


class CourseSpider(scrapy.Spider):
    name: str = "coursespider"


    def start_request(self):
        """This will scrape the list of Urls given."""
        urls: List[str] = ['https://catalog.unc.edu/courses/']
        for url in urls:
            yield scrapy.Request( url = url, callback = self.parse)
        

    def parse(self, response):
        """This will scrape the course catalog to get to each department."""
        links = response.css('/html/ul[1]//li/@href').extract()
        for link in links:
            course_dictionary['test'] = link
            # yield response.follow( url = link, callback = self.parse2)


    # def parse2(self, response):
    #     """This will get all the course names/numbers from each department."""
    #     department_name: str = response.xpath( 'h.page-title::text').extract()
    #     course_names: str = response.css('div.courseblock > p.courseblocktitle::text').extract()
    #     course_dictionary[department_name] = course_names

course_dictionary: Dict[str,List[str]] = {}

process = CrawlerProcess()
process.crawl(CourseSpider)
process.start()



