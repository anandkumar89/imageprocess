# Scrapy

	install scrapy using ``pip3 install scrapy``
---
### Troubleshooting while installation
> can't import service_identity(opentype)
> solved using ``pip3 install -U pyasn1`` https://github.com/scrapy/scrapy/issues/783
> 
> meanwhile I also checked proper installation of module service_identity, cryptography. But upgrading/installing pyasn1 solved the issue.
---
url can be downloaded as html file format using ``fetch(url)`` command.
``response`` can be viewed in browser as ``view(reponse)``. Particular element can be selected using css selectors and later can be extracted as:
```{python}
response.css('css selector::text').extract() / .extract_first()
```

Available commands for scrapy:

``bench       ``  Run quick benchmark test
``check       ``  Check spider contracts
``crawl       ``  Run a spider
``edit        ``  Edit spider
``fetch       ``  Fetch a URL using the Scrapy downloader
``genspider   ``  Generate new spider using pre-defined templates
``list        ``  List available spiders
``parse       ``  Parse URL (using its spider) and print the results
``runspider   ``  Run a self-contained spider (without creating a project)
``settings    ``  Get settings values
``shell       ``  Interactive scraping console
``startproject``  Create new project
``version     ``  Print Scrapy version
``view        ``  Open URL in browser, as seen by Scrapy

### Create a project
> $ scrapy startproject project_name
> $ cd project_name
> $ scrapy genspider spider_name www.example.com/

Now, go edit parse function for spider in spider directory to extract desired data from response and yeild a generator as desired.

``custom_settings = {FEED_FORMAT:"csv/json/xml", FEED_URI:"file_name"}`` can be set.


---
##### Refrences
- https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
- https://doc.scrapy.org/en/latest/intro/tutorial.html#extracting-data-in-our-spider
