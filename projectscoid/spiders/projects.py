import scrapy


class ProjectsSpider(scrapy.Spider):
    name = 'projects'
    allowed_domains = ['project.co.id']
    start_urls = ['http://project.co.id/']

    def parse(self, response):
        pass
