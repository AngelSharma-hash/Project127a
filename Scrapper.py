import pandas as pd
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

Page_Url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:\\Users\\Angel Sharma\\Desktop\\PythonProjects\\Project127")
browser.get(Page_Url)

time.sleep(10)

def Scrape():
    headers = ["Apparent Magnitude", "Proper Name", "Bayer Designation", "Distance", "Spectral Class", "Mass", "Radius", "Luminosity"]
    Star_data = []
    for i in range(0,200):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index!=1:
                    try:
                        temp_list.append(td_tag.contents[-1].strip())
                    except :
                        temp_list.append("")
                else:
                    try:
                        temp_list.append(td_tag.find_all("a")[0].contents[0])
                    except:
                        temp_list.append("")
            Star_data.append(temp_list)
    with open ("Scrapper.csv", "w",encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(Star_data)

Scrape()