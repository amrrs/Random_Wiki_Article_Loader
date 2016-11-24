#load webdriver function from selenium
from selenium import webdriver
from time import sleep

#Setting up Chrome webdriver Options
chrome_options = webdriver.ChromeOptions()

#setting  up local path of chrome binary file 
chrome_options.binary_location = "C:\\Users\\SA31\\Downloads\\dt\\Win_337026_chrome-win32\\chrome-win32\\chrome.exe"

#creating Chrome webdriver instance with the set chrome_options
driver = webdriver.Chrome(chrome_options=chrome_options)


#driver = webdriver.Chrome()

#loading 5 random wikipedia articles 
for i in range(1,6):
    #opening the url in the created browser instance
    driver.get("https://en.wikipedia.org/wiki/Special:Random")
    #getting the article title using id
    print(str(i)+'. '+driver.find_element_by_id('firstHeading').text)
    sleep(2)
    #scrolling the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
    sleep(1)
    #scrolling till the end of the page
    driver.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight)")

driver.close()
    
