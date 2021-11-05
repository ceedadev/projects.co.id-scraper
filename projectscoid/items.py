# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import MapCompose, TakeFirst
from scrapy.item import Item, Field
from datetime import datetime as dt

def dateTimeSerializer (value):
    # 04/11/2021 16:15:58 WIB
    dateTime = dt.strptime(value,"%d/%m/%Y %H:%M:%S WIB")
    return dateTime

class ProjectsItem(Item):
    # define the fields for your item here like:
    title = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())
    description = Field(output_processor=TakeFirst())
    tags = Field()
    publishedBudgetMin = Field(output_processor=TakeFirst())
    publishedBudgetMax = Field(output_processor=TakeFirst())
    publishedDate = Field(input_processor=MapCompose(dateTimeSerializer), output_processor=TakeFirst())
    selectDeadline = Field(input_processor=MapCompose(dateTimeSerializer), output_processor=TakeFirst())
    finishDays = Field(output_processor=TakeFirst())
    projectStatus = Field(output_processor=TakeFirst())
    bidCount = Field(output_processor=TakeFirst())
    needWeeklyReport = Field(output_processor=TakeFirst())
    projectOwnerIsOnline = Field(output_processor=TakeFirst())
    projectOwnerUser = Field(output_processor=TakeFirst())
    projectOwnerLocation = Field(output_processor=TakeFirst())
    projectOwnerScore = Field(output_processor=TakeFirst())
    projectOwnerNoProjects = Field(output_processor=TakeFirst())
    projectOwnerPoint = Field(output_processor=TakeFirst())
    projectOwnerRanking = Field(output_processor=TakeFirst())
