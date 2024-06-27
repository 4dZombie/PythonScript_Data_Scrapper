import json

def convert_special_chars(json_data):
    return json.loads(json.dumps(json_data).encode().decode('unicode_escape'))

with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

products_converted = convert_special_chars(products)

with open('products_converted.json', 'w', encoding='utf-8') as f:
    json.dump(products_converted, f, ensure_ascii=False, indent=4)

print('Special characters converted and saved to products_converted.json')
