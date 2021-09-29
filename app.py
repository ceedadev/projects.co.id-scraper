from bs4 import BeautifulSoup
import urllib3
import datetime
import csv

http = urllib3.PoolManager()
url_prefix = "https://projects.co.id/public/browse_projects/listing?page="

project_title = []
project_url = []
project_min_budget = []
project_max_budget = []
project_publish_datetime = []
project_deadline_datetime = []
project_finish_days = []

def striptime(string, datetimeformat = True):
    pass

for i in range(1,25): #looping for every page
    site = url_prefix + str(i)
    r = http.request('GET', site)
    #Fetch message
    if r.status == 200:
        print('Page ' + str(i) + ' fetch Success..')
    else:
        print('Page ' + str(i) + ' fetch Failed..')
    #begin beautiful soup parse
    soup = BeautifulSoup(r.data, 'html.parser')
    #looping for every project h2 attribute
    for title in soup.find_all('h2'): #h2 tag to get title and url
        project:str = title.get_text(strip=" ")
        project = project.replace(',','')
        url = title.a.get('href')
        #append to list
        project_title.append(project)
        project_url.append(url)
    #left_columns contains important detail of the project
    left_columns = soup.find_all(class_="col-md-6 align-left")[::2]
    #begin column
    for column in left_columns:
        detail = column.get_text("|", strip=" ")
        list_detail = detail.split('|')
        # first we clean the budget string
        budget = list_detail[1]
        budget = budget.strip("Rp ")
        budget = budget.replace(",","")
        min_budget,max_budget = budget.split(" - ") #min max budget cleaned
        project_min_budget.append(int(min_budget))
        project_max_budget.append(int(max_budget)) #budgets done!
        #pub date convert to python datetime format
        pub_datetime = list_detail[3]
        pub_datetime = pub_datetime.strip(" WIB") #29/12/2020 19:29:45
        # pub_datetime = datetime.strptime(pub_datetime, "%d/%m/%Y %H:%M:%S") #uncomment to use python format
        project_publish_datetime.append(pub_datetime) #publish datetime done!
        #deadline date convert to python datetime format, method same as above
        dl_datetime = list_detail[5]
        dl_datetime = dl_datetime.strip(" WIB")
        # dl_datetime = datetime.strptime(dl_datetime, "%d/%m/%Y %H:%M:%S") #uncomment to use python format
        project_deadline_datetime.append(dl_datetime) #deadline done!
        #expected finish days
        finish_days = int(list_detail[7])
        project_finish_days.append(finish_days)

#zipped to tuple 
zipped = zip(project_title, project_url, project_min_budget, project_max_budget, project_publish_datetime, project_deadline_datetime, project_finish_days)
data_header = ['title','url','minBudget','maxBudget','published','deadline','finishDays']
data = list(zipped)

dt = datetime.datetime.now()

now = dt.strftime("%d%m%Y%H%M")

#begin csv write
with open("projects" + now + ".csv", "w+") as f:
    writer=csv.writer(f, delimiter=',')
    writer.writerow(data_header)
    writer.writerows(data)
