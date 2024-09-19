import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver

def scrape_website_with_scaperapi(api_key, website):
    # Set up Chrome driver
    chrome_driver_path = './chromedriver'
    options = Options()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled') 
    options.add_argument('--disable-infobars')

    proxy_options = {
    'proxy': {
        'http': f'http://scraperapi:{api_key}@proxy-server.scraperapi.com:8001',
        'https': f'http://scraperapi:{api_key}@proxy-server.scraperapi.com:8001',
        'no_proxy': 'localhost,127.0.0.1'
    }
    }


    driver = webdriver.Chrome(
        service=Service(chrome_driver_path),
        options=options,
        seleniumwire_options=proxy_options
    )
    
    # Navigate to the website
    driver.get(website)
    print("Page loaded into Selenium ...")
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


    page_source = driver.page_source

    driver.quit()
    return page_source


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        #remove script and style tags
        script_or_style.extract()

    #separate with new line
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
        
    return cleaned_content

#create batches of the data 
def split_dom_content(dom_content, max_length=6000):
    return [
        #grabs first 6000 characers
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]