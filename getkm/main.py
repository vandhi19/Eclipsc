import requests
import time
from linkedlist import SingleLinkedList
from linkedlist import InitNode
from linkedlist import Addnode
from linkedlist import sort
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def findbusroute(data,SingleList):
    init = 0
    index = data.find(" km")
    while index != -1:
        adjust = index + 4
        newcontent = data[adjust:(data.__len__()-adjust)]
        km = data[(index - 4):(index)]
        if '"' in km:
            km = km[1:km.__len__()]
            if '.' in km:
                kmindex = km.find('.')
                km = km[:(kmindex)]            

        if init == 0:
            InitNode(SingleList, km)
            init = 1
        else:
            Addnode(SingleList, km)

        data = newcontent
        index = data.find(" km")
    printdata(SingleList)
    sort(SingleList)
    
def printdata(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next

chromedriver = "E:\Python36-32\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://maps.google.com")
elem = driver.find_element_by_name("q")
time.sleep(.500)
elem.clear()
elem.send_keys("chennai to madurai")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source or "There is no Internet connection" not in driver.page_source
time.sleep(2)
link = driver.current_url
linkfile = requests.get(link)
content = linkfile.text
index = content.find(" km")
buscontent = content
SingleList = SingleLinkedList()
findbusroute(buscontent,SingleList)
printdata(SingleList)


driver.close()
driver.quit()
print("Finished")
    