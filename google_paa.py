from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv, time
import datetime
# import xlsxwriter

def returnChromeDriver(pathToChromeDriver):
    print('in return chrome driver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chromedriver = pathToChromeDriver
    userAgent = "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver, chrome_options = chrome_options)
    return driver

def returnSearchUrl(question):
    print('return search url')
    baseGoogleQuery = "https://www.google.com/search?q="
    searchUrl = baseGoogleQuery + question.lower().replace(" ", "+").replace("?", "%3F").replace("'", "%27")
    return searchUrl



def extractQuestionData(soup):
    print('extract qeustions data')
    questionList = []
    #  find all paa
    for question in soup.findAll("div", class_="related-question-pair"):
    # find first paa
    # question = soup.find("div", class_="related-question-pair")

        questionDict = {}
        questionDict['relatedQuestion'] = question.find("g-accordion-expander").find("div").text

        if question.find("h3"):
            questionDict['titleTag'] = question.find("h3").text
            questionDict['titleTagLength'] = len(questionDict['titleTag'])
        else:
            questionDict['titleTag'] = "N/A - ERROR?"
            questionDict['titleTagLength'] = "N/A - ERROR?"

        if question.find("div", {"role":"heading"}):
            questionDict['answer'] = question.find("div", {"role":"heading"}).text
            questionDict['answerLength'] = len(questionDict['answer'])
        else:
            try:
                questionDict['answer'] = question.find("g-accordion-expander").findAll("div")[2].text
                questionDict['answerLength'] = len(questionDict['answer'])
            except:
                questionDict['answer'] = "N/A"
                questionDict['answerLength'] = "N/A"


        questionList.append(questionDict)
    return questionList

def writeCsvFile(allExtractedDataList):
    # date = datetime.datetime.now()
    with open("data1.csv",'a', newline='', encoding="utf-8") as csv_file:
        filewriter = csv.writer(csv_file)

        for questionData in allExtractedDataList:
            for relatedQuestion in questionData['relatedQuestionData']:
                filewriter.writerow([relatedQuestion['relatedQuestion'], relatedQuestion['answer']])

questions = ['main care for ','how to care of ','how to water ', 'how often to water','how much watar need ', 'how much sun need','how much light need',
             'can i eat ', 'Are the fruits edible of ','It grows indoors ', ' it grow in low light ', 'can grow in pot',
             'how to maintein ', 'how to check the soil','how to grow in garden ', 'grow outdoor ', 'When does it bloom'  ]

plants = ['roses']
for plant in plants:
    for q in questions:
        question = q+plant
        pathToChromeDriver = "C:/Users/dorms/Desktop/old/backup/flask_chatbot-master - v2/chromedriver.exe"
        driver = returnChromeDriver(pathToChromeDriver)
        searchUrl = returnSearchUrl(question)
        driver.get(searchUrl)
        time.sleep(1)

        allExtractedDataList = []

        if driver.find_elements_by_css_selector('div.related-question-pair'):
            soup = BeautifulSoup(driver.page_source, "lxml")
            extractedData = extractQuestionData(soup)
            currentQuestionDict = {'initialQuestion':question, 'relatedQuestionData':extractedData}
            allExtractedDataList.append(currentQuestionDict)

        else:
            print ("No Questions Found For: " + question)

        driver.quit()

        writeCsvFile(allExtractedDataList)