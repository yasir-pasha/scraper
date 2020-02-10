#Web Scraper - Python

Introduction
===========

Web scraper written in `Python`. Scrape 300 plus products from [Smallable](https://en.smallable.com/fashion/teen).

Dependencies
============
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
* [json](https://docs.python.org/3/library/json.html)

Installation and Usage
====================

First of all install `Python 3.8`. Copy all the files to your directory. Install `BeautifullSoup` by running this `pip3 install beautifulsoup4`
After successfully installation run `py collect-data.py`. It will take 3 to 5 min to scrape data and save it in `result.json` file.
When scraping successfully completed run `py analysis.py` Data Analysis. It will return this type of data.

```
{
  "products": [
    {
      "name": "Le Vrai Claude K-way 3.0 Midnight blue",
      "url": "https://en.smallable.com//le-vrai-claude-k-way-3-0-midnight-blue-k-way-82533.html",
      "brand": "K-way",
      "full_price": "\u20ac65",
      "price": 65.0,
      "previous_price": "",
      "image_urls": [
        "//static.smallable.com/1022297-324x324q80/le-vrai-claude-k-way-30.jpg",
        "//static.smallable.com/1022296-324x324q80/le-vrai-claude-k-way-30.jpg"
      ],
      "sizes": [
        "4Y",
        "6Y",
        "8Y",
        "10Y",
        "12Y",
        "14Y"
      ],
      "description": [
        "Fabrics : Nylon Canvas",
        "Details : with Hood, Long sleeves, Side pockets, Zip, Waterproof, Windbreaker, Thermosealed seams, Breathable",
        "Sizing for this item runs large.",
        "Composition : 100% Nylon"
      ]
    }
}
``` 