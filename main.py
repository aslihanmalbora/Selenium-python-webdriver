from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

options.add_argument("--disable-gpu")

options.add_argument("--no-sandbox")

options.add_argument("enable-automation")

options.add_argument("--disable-infobars")

options.add_argument("--disable-dev-shm-usage")
chrome_driver_path = './chromedriver'
my_url = 'https://khedmatma.ir'
option = Options()
option.headless = False
option.executable_path = chrome_driver_path
driver = webdriver.Chrome(options=option)
driver.get(my_url)
driver.maximize_window()
