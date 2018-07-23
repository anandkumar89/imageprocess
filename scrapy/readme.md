# Scrapy

install scrapy using ``pip3 install scrapy``
---
# Troubleshooting while installation
>> can't import service_identity(opentype)
solved using ``pip3 install -U pyasn1`` https://github.com/scrapy/scrapy/issues/783

meanwhile I also checked proper installation of module service_identity, cryptography. But upgrading/installing pyasn1 solved the issue.
---
url can be downloaded as html file format using ``fetch(url)`` command.
``response`` can be viewed in browser as ``view(reponse)``. Particular element can be selected using css selectors and later can be extracted as:
```{python}
response.css('css selector::text').extract() / .extract_first()
```


