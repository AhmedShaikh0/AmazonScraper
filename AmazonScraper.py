from bs4 import BeautifulSoup
import requests
from colorama import Fore

url1 = "https://www.amazon.com/dp/"
url2 = input("Enter Product ID: ")

def ScrapAmazon():
    url =  requests.get(url1+url2)
    soup = BeautifulSoup(url.text, "html.parser")
    about = soup.find('h1', attrs= {'class':'a-size-base-plus a-text-bold'})
    product = soup.find('span', attrs= {'id':'productTitle'})
    symbol = soup.find('span', attrs= {'class':'a-price-symbol'})
    productprice = soup.find('span', attrs= {'class':'a-price-whole'})
    details = soup.findAll('li', attrs= {'class':'a-spacing-mini'})

    
    print(Fore.GREEN,"\nTitle:", product.text.strip())
    print(Fore.GREEN,"\nPrice:", symbol.text.strip(),productprice.text.strip(),"Exluding Shipping Fees\n")
    print(Fore.WHITE,about.text.strip(),"\n")

    for details in details:
        print(Fore.YELLOW,details.text,"\n")
        
ScrapAmazon()