# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from datetime import datetime as dt

def dateTimeSerializer (value:str):
    # 04/11/2021 16:15:58 WIB
    dateTime = dt.strptime(date_string=value, format="%d/%m/%Y %H:%M:%S WIB")
    return dateTime

class ProjectsItem(Item):
    # define the fields for your item here like:
    title = Field()
    description = Field()
    tags = Field()
    publishedBudget = Field()
    publishedDate = Field(serializer=dateTimeSerializer)
    selectDeadline = Field(serializer=dateTimeSerializer)
    finishDays = Field()
    projectStatus = Field()
    bidCount = Field()
    needWeeklyReport = Field()
    projectOwnerUser = Field()
    projectOwnerLocation = Field()
    projectOwnerStars = Field()
    projectOwnerScore = Field()
    projectOwnerNoProjects = Field()
    projectOwnerPoint = Field()
    projectOwnerRanking = Field()
