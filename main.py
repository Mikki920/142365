import requests
from bs4 import BeautifulSoup
# import lxml


url = "https://hard.rozetka.com.ua/computers/c80095/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"user-agent": user}
""
session = requests.Session()


for j in range(1,68):
    print (f"Page - {j}")
    url = f"https://hard.rozetka.com.ua/computers/c80095/page={j}/"
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        products = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")

        for prod in products:
            if prod.find('div', class_="goods-tile__price--old price--gray ng-star-inserted"):
                price = prod.find("span", class_="goods-tile__price-value")
                title = prod.find('span', class_="goods-tile__title")
                price_prod = price.text.replace(" ", " ")
                title_prod = title.text
                with open("catalog.txt", "a", encoding="utf-8") as file:
                    file.write(f"{price_prod} {title_prod}\n")




