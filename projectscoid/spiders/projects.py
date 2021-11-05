from itemloaders.processors import TakeFirst
import scrapy
from scrapy import Selector
from scrapy.loader import ItemLoader
from ..items import ProjectsItem
from datetime import datetime as dt

base_url = 'https://projects.co.id/public/browse_projects/listing?page='

def budgetSplit(value:str):
    value = value.strip('Rp ').replace(',','')
    value = value.split(' - ')
    minBudget = int(value[0]) 
    maxBudget = int(value[1])
    return minBudget, maxBudget

class ProjectsSpider(scrapy.Spider):
    name = 'projects'
    allowed_domains = ['projects.co.id']
    start_urls = [base_url+str(page) for page in range(1,26)]
    
    def parse(self, response):
        projectList = response.xpath("//div[div[@class='col-md-10 align-left']]").getall()
        for project in projectList :
            sel = Selector(text=project)
            title:str = sel.css('h2').css('a::text').get()
            title = title.strip()
            title = title.title()
            url = sel.css('h2').css('a::attr(href)').get()
            tags = sel.xpath("//span[@class='tag label label-default']/a/text()").getall()
            description:str = sel.css('p::text').extract_first()
            description = description.strip().lower().replace('\n','').replace('\u00a0',' ').replace('\u0144',' ').replace('\uf0b7', '-').replace('\u2022', '-').replace('\u2013', '').replace(';', ':')
            projectOwnerUser:str = sel.xpath("//a[@class='short-username']/strong/text()").get()
            projectOwnerUser = projectOwnerUser.strip()
            # Details Column
            # Left Column
            leftColumnDetails:list = sel.xpath("//div[@class='col-md-6 align-left'][1]/text()").getall()
            # result = ['\n ', '\nRp 1,500,000 - 1,700,000', ' ', '\n04/11/2021 18:48:19 WIB', ' ', '\n04/12/2021 18:48:19 WIB', ' ', '\n14', ' ']
            publishedBudget:str = leftColumnDetails[1]
            publishedBudget = publishedBudget.strip()
            
            publishedBudgetMin, publishedBudgetMax = budgetSplit(publishedBudget)
            publishedDate:str = leftColumnDetails[3]
            publishedDate = publishedDate.strip()
            selectDeadline:str = leftColumnDetails[5]
            selectDeadline = selectDeadline.strip()

            finishDays:str = leftColumnDetails[7]
            finishDays = finishDays.strip()
            # Right Column
            rightColumnDetails = sel.xpath("//div[@class='col-md-6 align-left'][2]/text()").getall()
            # result =  ['\n', '\n', ' ', '\n0', ' ', '\n', ' ']
            bidCount:str = rightColumnDetails[3]
            bidCount = bidCount.strip()
            projectStatus = sel.xpath("//div[@class='col-md-6 align-left'][2]/span/text()").get()
            needWeeklyReportXpath = sel.xpath("//div[@class='col-md-6 align-left'][2]/i/@class").get()
            if ('fa-check' in needWeeklyReportXpath):
                needWeeklyReport = True
            else:
                needWeeklyReport = False
            #Project Owner Info Column
            projectOwnerIsOnlineXpath = sel.xpath("//i/@class").get()
            if('online' in projectOwnerIsOnlineXpath):
                projectOwnerIsOnline = True
            else:
                projectOwnerIsOnline = False
            projectOwnerColumn = sel.xpath("//div[@class='col-md-2 align-left']/text()").getall()
            # result = ['\n', ' ', ' Kab. Grobogan', ' ', '\xa0', '\xa0', '\xa0', '\xa0', ' 10.00/10.00', ' 4 projects', ' 250 Point', ' #1,887 dari 340,505 ']
            projectOwnerLocation:str = projectOwnerColumn[2]
            projectOwnerLocation = projectOwnerLocation.strip()
            if (projectOwnerLocation == ''):
                projectOwnerLocation = 'Unspecified'
            projectOwnerScore = projectOwnerColumn[-4]
            projectOwnerScore = projectOwnerScore.strip()
            projectOwnerScore:list = projectOwnerScore.split(sep='/')
            projectOwnerScore = projectOwnerScore.pop(0)
            projectOwnerNoProjects:str = projectOwnerColumn[-3]
            projectOwnerNoProjects = projectOwnerNoProjects.strip()
            projectOwnerPoint:str = projectOwnerColumn[-2]
            projectOwnerPoint = projectOwnerPoint.strip()
            projectOwnerRanking:str = projectOwnerColumn[-1]
            projectOwnerRanking = projectOwnerRanking.strip()
            
            #BEGIN ITEMLOADER
            l = ItemLoader(item=ProjectsItem())
            l.add_value('title',title)
            l.add_value('url', url)
            l.add_value('description', description)
            l.add_value('tags', tags)
            l.add_value('publishedBudgetMin', publishedBudgetMin)
            l.add_value('publishedBudgetMax', publishedBudgetMax)
            l.add_value('publishedDate', publishedDate)
            l.add_value('selectDeadline', selectDeadline)
            l.add_value('finishDays', finishDays)
            l.add_value('projectStatus', projectStatus)
            l.add_value('bidCount', bidCount)
            l.add_value('needWeeklyReport', needWeeklyReport)
            l.add_value('projectOwnerIsOnline', projectOwnerIsOnline)
            l.add_value('projectOwnerUser', projectOwnerUser)
            l.add_value('projectOwnerLocation', projectOwnerLocation)
            l.add_value('projectOwnerScore', projectOwnerScore)
            l.add_value('projectOwnerNoProjects', projectOwnerNoProjects)
            l.add_value('projectOwnerPoint', projectOwnerPoint)
            l.add_value('projectOwnerRanking', projectOwnerRanking)
            yield l.load_item()