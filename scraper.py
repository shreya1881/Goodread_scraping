import requests
import openpyxl
from bs4 import BeautifulSoup
import html5lib 

goodread = openpyxl.Workbook()
sheet = goodread.active
sheet.title='Most Popular Books of 2021'

sheet.append(['Title','Author','Image URL','Total Number of Ratings','Average Rating'])

url = "https://www.goodreads.com/book/popular_by_date/2021"

try:
  req = requests.get(url)
  req.raise_for_status()
  soup = BeautifulSoup(req.text,"html.parser")

  books = soup.find('div', class_="RankedBookList").find_all('article')

  for book in books:

    name = book.find('strong').a.text
  

    author = book.find('span',class_="ContributorLink__name").text
  

    image = book.find('img',class_="ResponsiveImage").get('src')
 

    avg_rating = book.find('span',class_="Text Text__body3 Text__semibold Text__body-standard").text
    

    num_ratings = book.find('span',class_="Text Text__body3 Text__subdued").text.strip('k ratings')
    
    
    print(name,author,image,avg_rating,num_ratings)
    sheet.append([name,author,image,num_ratings,avg_rating])
    
except Exception as e:
  print(e)

goodread.save('Most Popular Books of 2021.xlsx')