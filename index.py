from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import constants

req = Request(constants.BASE_URL + 'fashion/teen?_infinite=300&_scroll=4', headers=constants.HEADERS)
result = urlopen(req).read()

soup = BeautifulSoup(result, "html.parser")
products = soup.find_all('div', class_='product-item')
all_products = {'products': []}


def getProductDetail(product_url):
    """
    Get the product details.
    :parameter product_url: Product URL whose detail to be fetched
    """
    request = Request(product_url, headers=constants.HEADERS)
    result = urlopen(request).read()
    parser = BeautifulSoup(result, "html.parser")

    # Find the description and create list form it
    description_element = parser.find('div', class_='p-description').find_all('li')
    description = []
    for item in description_element:
        description.append(item.text)

    # Find the sizes and create list from it
    sizes_element = parser.find('select', id='form_size_select').find_all('option')
    sizes = []
    for item in sizes_element[1:]:
        if item != 'None':
            sizes.append(item.get('data-size'))

    return {'description': description, 'sizes': sizes}


# Loop the products to get required information
for product in products:
    title_elem = product.find('div', class_='p-name')
    product_brand = product.find('div', class_='p-brand')
    product_full_price = product.find('span', class_='full-price')
    product_price = product.find('meta', {'itemprop': 'price'})
    sale_price_element = product.find('span', class_='sale-price')
    product_images = product.find_all('img')
    sizes = product.find_all('li', class_='fake-btn')
    url = product.find('a', class_='product-click')

    images = []
    for product_image in product_images:
        images.append(product_image.get('data-src'))

    sale_price = ''
    if sale_price_element is not None:
        sale_price = sale_price_element.text
    product_url = constants.BASE_URL + url.get('href')
    product_detail = getProductDetail(product_url)

    all_products['products'].append({
        'name': title_elem.text,
        'url': product_url,
        'brand': product_brand.text,
        'full_price': product_full_price.text,
        'price': float(product_price.get('content')),
        'previous_price': sale_price,
        'image_urls': images,
        'sizes': product_detail['sizes'],
        'description': product_detail['description'],
    })
# Write the data into json file
with open('result.json', 'w') as fp:
    json.dump(all_products, fp)

print('Result is saved in result.json file')
