from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.binary_location = "/usr/lib/firefox/firefox"

driver = webdriver.Firefox(options=options)
driver.get("http://localhost:8000")
print(driver.title)
assert "Congratulations!" in driver.title
print("OK")

