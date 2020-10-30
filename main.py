# NETONNET grafikkort fyndvaror
# https://www.netonnet.se/art/fyndvaror/fyndvaror-datorkomponenter/grafikkort

import requests
from html.parser import HTMLParser

def ITS_HAPPENING(store, gpu_name):
  print("OMG IT'S HAPPENING! Store", store, "has a GPU named", gpu_name)

class NetOnNetHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    if tag == "input":
      # Check if this is a "product entry" type of attribute, they come in pairs like ('name', 'ProductName'), ('value', 'Gigabyte 1660')
      if ('name', 'ProductName') in attrs:
        for attr in attrs:
          if 'value' in attr:
            # Now check if there is a 3080 or 3090 in here...
            name = attr[1]
            #print("Name of GPU: ", name)
            if "3080" in name or "3090" in name:
              ITS_HAPPENING("NetOnNet", name)

  def handle_endtag(self, tag):
    pass

  def handle_data(self, data):
    pass

class InetHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    #print("Start tag: ", tag)
    if tag == "a" and len(attrs) == 2:
      if 'href' in attrs[0] and 'aria-label' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          ITS_HAPPENING("Inet", name)

  def handle_endtag(self, tag):
    #print("end tag: ", tag)
    pass

  def handle_data(self, data):
    #print("Data: ", data)
    pass

class KomplettHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    #print("Start tag: ", tag)
    if tag == "a" and len(attrs) == 4:
      if 'class' in attrs[0] and 'title' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          ITS_HAPPENING("Komplett", name)

  def handle_endtag(self, tag):
    #print("end tag: ", tag)
    pass

  def handle_data(self, data):
    #print("Data: ", data)
    pass

class ElgigantenHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    #print("Start tag: ", tag)
    if tag == "a" and len(attrs) == 4:
      if 'class' in attrs[0] and 'title' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          ITS_HAPPENING("Elgiganten", name)

  def handle_endtag(self, tag):
    #print("end tag: ", tag)
    pass

  def handle_data(self, data):
    #print("Data: ", data)
    pass

def do_netonnet():
  print("Searching NetOnNet...")
  r = requests.get("https://www.netonnet.se/art/fyndvaror/fyndvaror-datorkomponenter/grafikkort")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = NetOnNetHTMLParser()
  parser.feed(r.text)

  print("NetOnNet done.")

def do_inet():
  print("Searching Inet...")
  r = requests.get("https://www.inet.se/fyndhornan?filters=%7B%22-11%22%3A%7B%22type%22%3A%22Template%22%2C%22any%22%3A%5B17%5D%7D%7D")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = InetHTMLParser()
  parser.feed(r.text)

  print("Inet done.")

def do_komplett():
  print("Searching Komplett...")
  r = requests.get("https://www.komplett.se/category/10072/demovaror/datorutrustning/demo-grafikkort")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = KomplettHTMLParser()
  parser.feed(r.text)

  print("Komplett done.")

def do_elgiganten():
  print("Searching Elgiganten...")
  r = requests.get("https://www.elgiganten.se/catalog/outlet/outlet-datorer-tillbehor/datorer-tillbehor-fyndvaror?SearchParameter=%26%40QueryTerm%3D*%26ContextCategoryUUID%3DZS.sGQV9kRYAAAFs_dQnwfF6%26discontinued%3D0%26online%3D1%26Produkttyp%3DGrafikkort%26%40Sort.ViewCount%3D1%26%40Sort.ProductListPrice%3D0&PageSize=12&ProductElementCount=&searchResultTab=Products&CategoryName=outlet-datorer-tillbehor&CategoryDomainName=store-elgigantenSE-ProductCatalog#filter-sidebar")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = ElgigantenHTMLParser()
  parser.feed(r.text)

  print("Elgiganten done.")

if __name__ == "__main__":
  do_netonnet()
  do_inet()
  do_komplett()
  do_elgiganten()



#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

#def do_webhallen():
#  print("Searching Webhallen...")

#  chrome_opts = Options()
#  chrome_opts.add_argument("--headless")
#  chrome_opts.add_argument("--disable-gpu")
#  browser = webdriver.Chrome(options=chrome_opts)
#  browser.get("https://www.webhallen.com/se/category/4818-Grafikkort")

#  html = browser.page_source
#  parser = WebhallenHTMLParser()
#  parser.feed(html)

#  browser.quit()
#  print("Webhallen done.")

#class WebhallenHTMLParser(HTMLParser):
#  def handle_starttag(self, tag, attrs):
#    print("Tag: ", tag)

#  def handle_endtag(self, tag):
#    print("End tag: ", tag)

#  def handle_data(self, data):
#    print("Data: ", data)