import re 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import argparse

parser = argparse.ArgumentParser(description='Enter Company Name To Query. i.e verzion, gamestop,facebook ')
parser.add_argument("-d")

args = parser.parse_args()
d = args.d

driver = webdriver.Chrome()
url = "https://www.crunchbase.com/organization/{0}/company_financials".format(d)
driver.get(url) 
get_url = driver.current_url 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
pattern="acquired by"
for string in soup.strings:
 x = repr(string)
 if re.search(pattern, x):
  y = x.split("'")[1]  
  z = y.lstrip(' ')
  if re.search(r'Auto-generated', z) is None:
   print(z)

driver.close()
driver.quit()

