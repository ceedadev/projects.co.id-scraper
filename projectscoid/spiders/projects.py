import scrapy
from scrapy import Selector

base_url = 'https://projects.co.id/public/browse_projects/listing?page='

class ProjectsSpider(scrapy.Spider):
    name = 'projects'
    allowed_domains = ['projects.co.id']
    start_urls = [base_url+str(page) for page in range(1,2)]
    
    def parse(self, response):
        projectList = response.xpath("//div[div[@class='col-md-10 align-left']]").getall()
        for project in projectList :
            sel = Selector(text=project)
            title:str = sel.css('h2').css('a::text').get()
            title = title.strip()
            url = sel.css('h2').css('a::attr(href)').get()
            tags = sel.xpath("//span[@class='tag label label-default']/a/text()").getall()
            description:str = sel.css('p::text').extract_first()
            description = description.strip().lower()
            projectOwnerUser = sel.xpath("//a[@class='short-username']/strong/text()").get()
            print(title)
            print(url)
            print(tags)
            print(description)
            print(projectOwnerUser)