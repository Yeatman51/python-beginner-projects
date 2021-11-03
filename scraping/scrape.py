from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.apartments.com/apartments/asheville-nc/1-bedrooms/?bb=gr6p7g7n-Hsh39hjK"
page = requests.get(url)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="placards placardsv2")
print("help")
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Address','Bedrooms','Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('span', class_="js-placardTitle title").text.replace('\n', '')
        address = list.find('div', class_="property-address").text.replace('\n', '')
        bedrooms = list.find('p', class_="property-beds").text.replace('\n', '')
        price = list.find('p', class_="property-pricing").text.replace('\n', '')
        
        info = [title, address, bedrooms, price]
        thewriter.writerow(info)
