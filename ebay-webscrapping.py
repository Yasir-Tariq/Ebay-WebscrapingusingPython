from urllib.request import urlopen as ureq #module for getting html data
from bs4 import BeautifulSoup as b #module for parsing html data
import re #module for regular expression
import math #module for mathematical expression


base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
request = input('Enter keyword to search:  ')
url_separator = "&LH_TitleDesc=0&_pgn="
page_num = input('Enter page number: ')

url = base_url + request + url_separator + page_num

html = ureq(url)
soup = b(html, "html.parser")

#----------    FOR FILE HANDLING
filename = "dataaa.csv"
f = open(filename, "w")
headers = "Name, Price , Shipping\n"
f.write(headers)
#----------




#function to get data by scrapping
def getdata():

    for post in soup.findAll("li", {"class" : "s-item"}):
        title = ""
        sample = "0"
        reship = "0"

        for j in post.findAll("h3", {"class" : "s-item__title"}):
            title = j.text
            print("Name of the product: " + title)
        for k in post.findAll("span", {"class" : "s-item__price"}):
            price = k.text.strip()
            sample = re.sub(r'[$|+|Tap item to see current priceSee Price|See Price]',r'',price)
            dollar = "$"
            msg = f'Price of the product: {dollar} {sample}'
            print(msg)
            # print("Price of the product: " + "$" + sample)
        for l in post.findAll("span", {"class" : "s-item__shipping s-item__logisticsCost"}):
            if l.text == "Free International Shipping":
                l = "0"
                print("Shipping: " + "$" + l)
            else:
                ship = l.text.strip()
                reship = re.sub(r'[$|+|shipping]',r'',ship)
                # newship = float(reship)
                dollarr = "$"
                msgg = f'Shipping:  {dollarr} {reship}'
                print(msgg)
                # print("Shipping: " + "$" + reship)
                f.write(title.replace(",", "|") + "," + sample + "," + reship +  "\n")
    f.close()
# def compare():
#     budget = 900


#Calling the function in the main body
if __name__ == "__main__":
    getdata()
