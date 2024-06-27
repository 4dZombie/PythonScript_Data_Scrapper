import requests
from bs4 import BeautifulSoup
import json
import time

def get_products_from_category(category_url):
    print(f"Scraping category: {category_url}")
    response = requests.get(category_url)
    if response.status_code != 200:
        print(f"Failed to retrieve {category_url}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []
    seen_products = set()  # To track unique product names
    
    product_elements = soup.find_all('div', class_='product-small')
    if not product_elements:
        print("No product elements found.")
    
    for product in product_elements:
        try:
            name = product.find('p', class_='name').text.strip()
            price = product.find('span', class_='woocommerce-Price-amount').text.strip()
            
            if name not in seen_products:
                products.append({'name': name, 'price': price})
                seen_products.add(name)
                print(f"Found product: {name} - {price}")
            else:
                print(f"Duplicate product skipped: {name}")
        except AttributeError as e:
            print(f"Error processing product: {e}")
        time.sleep(10)  # Delay of request took it from robots.txt file
    
    return products

def save_products(products, filename='products.json'):
    with open(filename, 'w') as f:
        json.dump(products, f, indent=4)

if __name__ == '__main__':
    categories = [
        'https://beck-mathys.ch/shop/broetli-gipfeli/',
        'https://beck-mathys.ch/shop/suesse-gebaecke/',
        'https://beck-mathys.ch/shop/stueckli/',
        'https://beck-mathys.ch/shop/brunch/',
        'https://beck-mathys.ch/shop/take-away-und-apero/',
        'https://beck-mathys.ch/shop/normalbrot/',
        'https://beck-mathys.ch/shop/spezialbrot/',
        'https://beck-mathys.ch/shop/zopf/',
        'https://beck-mathys.ch/shop/schokolade/',
        'https://beck-mathys.ch/shop/konfekt/',
        'https://beck-mathys.ch/shop/take-away-und-apero/waehen/',
        'https://beck-mathys.ch/shop/desserts/',
        'https://beck-mathys.ch/shop/aktulles/',
        'https://beck-mathys.ch/shop/torten/',
    ]
    
    all_products = []
    for category_url in categories:
        category_products = get_products_from_category(category_url)
        all_products.extend(category_products)
    
    save_products(all_products)
    print('Products saved to products.json')
