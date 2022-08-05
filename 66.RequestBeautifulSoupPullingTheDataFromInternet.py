#These codes can be wrong
#I didn't complete here 
#After 65 these codes can be wrong
"""
import requests
from bs4 import BeautifulSoup
url="https://www..net/"
response=requests.get(url)

html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")
#print(soup.prettify())
#print(response)

#print(soup.find_all("a"))
#for i in soup.find_all("a"):
    #print(i.text)
    #print("********************")
print(soup.find_all("div",{"class":"item uzman"}))
"""



