from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from IPython.display import display, HTML
import time

class indeed():
    def __init__(self,keywords,maxPages,location):
        self.headers ={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        self.keywords = str(keywords)
        self.maxPages = int(maxPages)
        self.location = str(location)
        self.df= pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Description"])




    def DFappend(self, Title, Location, Company, Salary, Sponsored, Description):
        self.df = self.df.append({'Title':Title,'Location':Location,"Company":Company,"Salary":Salary,"Sponsored":Sponsored,
                                  "Description": Description},ignore_index=True)


        print("Got objects", self.df.shape)
        # display(self.df)




    def toCSV(self):
        name=self.keywords
        locaton=self.location

        self.df.to_csv(name+"_"+locaton+".csv", index=False)

    def Translate(self):
        k=self.keywords
        loc=self.location
        url='https://www.indeed.ca/jobs?q='+k+"&l="+loc+"&start="
        print(url)
        return url
    def getWork(self):
        driver = webdriver.Chrome()
        max=self.maxPages*10

        for i in range(0, max, 10):
            driver.get(self.Translate() + str(i))
            title=""
            location=""
            company=""
            salary=""
            Description=""
            driver.implicitly_wait(4)

            for job in driver.find_elements_by_class_name('result'):

                soup = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')

                try:
                    title = soup.find("a", class_="jobtitle").text.replace("\n", "").strip()

                except:
                    title = 'None'

                try:
                    location = soup.find(class_="location").text
                except:
                    location = 'None'

                try:
                    company = soup.find(class_="company").text.replace("\n", "").strip()
                except:
                    company = 'None'

                try:
                    salary = soup.find(class_="salary").text.replace("\n", "").strip()
                except:
                    salary = 'None'

                try:
                    sponsored = soup.find(class_="sponsoredGray").text
                    sponsored = "Sponsored"
                except:
                    sponsored = "No sponsored"

                sum_div = job.find_element_by_class_name('summary')
                try:
                    sum_div.click()
                except:
                    time.sleep(0.1)
                    print(driver.find_elements_by_class_name('popover-x-button-close'))
                    close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]

                    close_button.click()
                    sum_div.click()
                try:
                    Description = driver.find_element_by_id('vjs-desc').text
                except:
                    Description='None'
                try:
                    self.DFappend(title,location,company,salary,sponsored,Description)
                except:
                    print("err")


def main():
    keywords=input("type in searching key words: ")
    pages= input("type in max scraping page: ")
    location= input("type in location: ")
    n =indeed(keywords,int(pages),location)
    n.getWork()
    n.toCSV()

if __name__ == '__main__':
    main()
