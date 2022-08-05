"""
#These codes can be wrong
import requests 

from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"

response=requests.get(url)

html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")

titles=soup.find_all("td",{"class":"titleColumn"})
ratings=soup.find_all("td",{"class":"ratingColumn imdbRating"})
"""
for titles,ratings in zip(titles,ratings):
    print("Title:",titles.text)
    print("Rating:",ratings.text)
"""
for titles,ratings in zip(titles,ratings):
    titles=titles.text
    ratings=ratings.text
    titles=titles.strip()
    titles=titles.replace("\n","")

    ratings=ratings.strip()
    ratings=ratings.replace("\n","")

    print("Title:",titles)
    print("Rating:",ratings)

#print(response)
"""