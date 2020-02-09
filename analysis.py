import collections
import json

# Get data from file
with open('result.json') as f:
    data = json.load(f)

products_by_brands = collections.defaultdict(list)

brands = set()
for product in data['products']:
    brands.add(product['brand'])
    products_by_brands[product['brand']].append(product)

for brand in brands:
    brand_products = products_by_brands[brand]
    max_price = max(brand_products, key=lambda x: x['price'])
    min_price = min(brand_products, key=lambda x: x['price'])
    # avg_price = sum(brand_products, key=lambda x: x['price'])
    total_price = sum(item['price'] for item in brand_products)

    on_sale_products = list(filter(lambda elem: elem['previous_price'] != '', brand_products))
    products_count = len(brand_products)
    avg_price = total_price / products_count

    print(brand)
    print('Total Products:' + str(products_count))
    print("Maximum Price of " + brand + ": [Product Name:" + max_price['name'] + ", Price:" + str(
        max_price['price']) + "]")
    print("Minimum Price of " + brand + ": [Product Name:" + min_price['name'] + ", Price:" + str(
        min_price['price']) + "]")
    print("Average Price of " + brand + ": " + str('{0:.2f}'.format(avg_price)))
    print("Total products on sale of " + brand + ": " + str(len(on_sale_products)))
    print('===================================================')
    print('')

# print(products_by_brands['Jott'])
