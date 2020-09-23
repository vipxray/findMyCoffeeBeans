# Created by Haorui Chen
# Updated by 05/15/2020

import time
import json
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By    # find by name, id, ..
from selenium.webdriver.support import expected_conditions as EC

def get_peets_coffee():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\vipxr\OneDrive\Coding\find_ur_coffee\data_crawling\chromedriver.exe')
    product_data = {}

    # peet's coffee
    # date: 05/21/2020
    url_peet = 'https://www.peets.com/coffee/drip-brewing'
    driver.get(url_peet)
    for t in range(3):
        time.sleep(random.randint(2, 3))
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    product = driver.find_elements_by_class_name("product-link")
    product_links = [p.get_attribute('href') for p in product]
    # print('product_links:', len(product_links), '\n', product_links)

    product_data['peets coffee'] = []
    for p_link in product_links:
        time.sleep(random.randint(2, 5))
        cur_product = driver.get(p_link)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "product_addtocart_form"))
        )
        driver.get(p_link)
        # [name, bio, price, rating, flvr_note, flvr_ctgy, roast_lv, origin]
        name = driver.find_element_by_class_name('product-name').text
        short_description = driver.find_element_by_class_name('std').text
        price = driver.find_element_by_class_name('price').text
        rating = driver.find_element_by_xpath('//*[@id="BVRRSummaryContainer"]/div/div/div/div/div/div/dl/dd[1]/div/a/span').text
        flavor_note = driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[3]/div[1]/div').text
        flavor_category = driver.find_element_by_class_name('flavor').text
        roast_lv = driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[3]/div[3]/div/div').text
        product_data['peets coffee'].append({
            'name': name,
            'short_description': short_description,
            'price': price,
            'rating': rating,
            'flavor_note': flavor_note,
            'flavor_category': flavor_category,
            'roast_lv': roast_lv
        })
    with open('coffee_product_data.json', 'w') as outfile:
        json.dump(product_data, outfile)
        
    driver.close()


# TODO: def get_starbucks_coffee():
