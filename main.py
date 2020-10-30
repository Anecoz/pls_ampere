import os
import time
import threading
import requests
import discord
from dotenv import load_dotenv
from html.parser import HTMLParser

def ITS_HAPPENING(store, gpu_name):
  #await channel.send(f"OMG IT'S HAPPENING! Store {store} has a GPU named {gpu_name}")
  print(f"OMG IT'S HAPPENING! Store {store} has a GPU named {gpu_name}")

class NetOnNetHTMLParser(HTMLParser):
  result = ""

  def handle_starttag(self, tag, attrs):
    if tag == "input":
      if ('name', 'ProductName') in attrs:
        for attr in attrs:
          if 'value' in attr:
            name = attr[1]
            if "3080" in name or "3090" in name:
              self.result = name
              #ITS_HAPPENING("NetOnNet", name)

class InetHTMLParser(HTMLParser):
  result = ""

  def handle_starttag(self, tag, attrs):
    if tag == "a" and len(attrs) == 2:
      if 'href' in attrs[0] and 'aria-label' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          self.result = name
          #ITS_HAPPENING("Inet", name)

class KomplettHTMLParser(HTMLParser):
  result = ""

  def handle_starttag(self, tag, attrs):
    if tag == "a" and len(attrs) == 4:
      if 'class' in attrs[0] and 'title' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          self.result = name
          #ITS_HAPPENING("Komplett", name)

class ElgigantenHTMLParser(HTMLParser):
  result = ""

  def handle_starttag(self, tag, attrs):
    if tag == "a" and len(attrs) == 4:
      if 'class' in attrs[0] and 'title' in attrs[1]:
        name = attrs[1][1]
        if "3080" in name or "3090" in name:
          self.result = name
          #ITS_HAPPENING("Elgiganten", name)

def do_netonnet():
  print("Searching NetOnNet...")
  r = requests.get("https://www.netonnet.se/art/fyndvaror/fyndvaror-datorkomponenter/grafikkort")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = NetOnNetHTMLParser()
  parser.feed(r.text)

  print("NetOnNet done.")
  return parser.result

def do_inet():
  print("Searching Inet...")
  r = requests.get("https://www.inet.se/fyndhornan?filters=%7B%22-11%22%3A%7B%22type%22%3A%22Template%22%2C%22any%22%3A%5B17%5D%7D%7D")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = InetHTMLParser()
  parser.feed(r.text)

  print("Inet done.")
  return parser.result

def do_komplett():
  print("Searching Komplett...")
  r = requests.get("https://www.komplett.se/category/10072/demovaror/datorutrustning/demo-grafikkort")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = KomplettHTMLParser()
  parser.feed(r.text)

  print("Komplett done.")
  return parser.result

def do_elgiganten():
  print("Searching Elgiganten...")
  r = requests.get("https://www.elgiganten.se/catalog/outlet/outlet-datorer-tillbehor/datorer-tillbehor-fyndvaror?SearchParameter=%26%40QueryTerm%3D*%26ContextCategoryUUID%3DZS.sGQV9kRYAAAFs_dQnwfF6%26discontinued%3D0%26online%3D1%26Produkttyp%3DGrafikkort%26%40Sort.ViewCount%3D1%26%40Sort.ProductListPrice%3D0&PageSize=12&ProductElementCount=&searchResultTab=Products&CategoryName=outlet-datorer-tillbehor&CategoryDomainName=store-elgigantenSE-ProductCatalog#filter-sidebar")

  if r.status_code != 200:
    print("Status code not 200, exiting")
    exit()

  parser = ElgigantenHTMLParser()
  parser.feed(r.text)

  print("Elgiganten done.")
  return parser.result

stop_thread = False
async def check_loop_thread():
  print("Starting thread loop...")
  counter = 0

  while not stop_thread:
    if counter != 0 and counter % 50 == 0:
      await channel.send(f"I've looked for cards {counter} times... Sadge")

    result = do_netonnet()
    if result != "":
      await channel.send(f"OMG IT'S HAPPENING! Store NetOnNet has a GPU named {result}!")

    result = do_inet()
    if result != "":
      await channel.send(f"OMG IT'S HAPPENING! Store Inet has a GPU named {result}!")

    result = do_komplett()
    if result != "":
      await channel.send(f"OMG IT'S HAPPENING! Store Komplett has a GPU named {result}!")

    result = do_elgiganten()
    if result != "":
      await channel.send(f"OMG IT'S HAPPENING! Store Elgiganten has a GPU named {result}!")

    time.sleep(20)
    counter = counter + 1


if __name__ == "__main__":
  # start up discord bot stuff
  load_dotenv()
  TOKEN = os.getenv('DISCORD_TOKEN')
  GUILD = os.getenv('DISCORD_GUILD')

  client = discord.Client()

  @client.event
  async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{guild.name}')

    global channel
    channel = discord.utils.get(guild.channels, name='general')
    if channel:
      client.loop.create_task(check_loop_thread())

  client.run(TOKEN)

  stop_thread = True


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