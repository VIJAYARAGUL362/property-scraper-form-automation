from bs4 import BeautifulSoup
import os,time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
CHROME_DRIVER_PATH = "C:/Users/Hi/Downloads/chromedriver-win64/chromedriver-win64"

# loading the environment variable
load_dotenv()

# links
WEBSITE_URL = os.getenv('ZILLOW_CLONE_URL')
GOOGLE_FORMS_URL = os.getenv('GOOGLE_FORM_URL')

# getting the website
response = requests.get(WEBSITE_URL)
zillow_text = response.text

# initializing the soup object
soup = BeautifulSoup(zillow_text,'html.parser')
print(soup.title.text)

# GETTING THE LINKS OF THE PROPERTY
links_soup = soup.select("a[data-test = 'property-card-link']")

links = [link.attrs['href']  for link in links_soup]

# GETTING THE ADDRESS OF THE PROPERTY
address_soup = soup.select("address[data-test = 'property-card-addr']")

addresses = [" ".join(address.text.split()) for address in address_soup]

# GETTING THE PRICE
prices_soup = soup.select("span[data-test = 'property-card-price']")

prices = [price.text.split('+')[0] for price in prices_soup] # removed the + symbol

for i in range(len(prices)): # removing the '\mo' from the prices
    if prices[i].endswith('/mo'):
        prices[i] = prices[i][:-3]
    if prices[i].startswith('$'): # removing the '$' symbol from the prices
        prices[i] = prices[i][1:]


class FormFillerBot:
    """
    This class fetches the form and fill the price,address and link to the property.
    """
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
    def get_form(self):
        """
        Fetches the form
        :return:
        """
        self.driver.get(GOOGLE_FORMS_URL)

    def fill_details(self,address:str,price:str,link:str):
        """
        fill the details in the fetched form
        :param address: address of the property
        :param price: price of the property
        :param link: link to the property
        :return:
        """
        inputs = self.driver.find_elements(By.CLASS_NAME,'whsOnd')

        # ADDRESS OF THE PROPERTY
        address_input_box = inputs[0]
        address_input_box.clear()
        address_input_box.send_keys(address)

        # PRICE OF THE PROPERTY
        price_input_box = inputs[1]
        price_input_box.clear()
        price_input_box.send_keys(price)

        # LINK TO THE PROPERTY
        link_input_box = inputs[2]
        link_input_box.clear()
        link_input_box.send_keys(link)

    def press_submit(self):
        """
        presses the submit button of the form.
        :return:
        """
        submit_button = self.driver.find_element(By.CLASS_NAME,'uArJ5e')
        submit_button.click()


# INSTANCE OF THE FormFillerBot
bot = FormFillerBot()

for address,price,link in zip(addresses,prices,links):
    bot.get_form()
    time.sleep(1) # waiting for the webpage to load
    bot.fill_details(address,price,link)
    bot.press_submit()
    time.sleep(1) # waiting for the webpage to move to submit page




