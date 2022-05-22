# -- coding: utf-8 --
"""
Created on Sun May 22 09:53:20 2022

@author: 
"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
driver_TOS = webdriver.Chrome(service=service)
while(True):
    print("""
          a. Retrieve data
          b. Create the graph
          c. Display the matrix
          d. Save to Excel file
          e. Exit
          """)
    option_TOS = input("Please select your option: \n")
    if(option_TOS == "a"): 
        driver_TOS.get("https://www.bedbathandbeyond.com/store/category/college/decor/10625?icid=hp_homepage_4acrs_slot2_bath")
        prod_names_TOS = []
        prod_prices_TOS = []
        time.sleep(5)
        shadow_host_TOS = driver_TOS.find_element("id", "wmHostPrimary")
        shadow_root = driver_TOS.execute_script('return arguments[0].shadowRoot', shadow_host_TOS)
        #shadow_root_TOS = shadow_host_TOS.shadowRoot
        products_TOS = shadow_root.find_elements("css selector", ".prodCardWrap")
        for product_TOS in products_TOS:
            product_container_TOS = product_TOS.find_element("class name", "prodCardR")
            product_name_TOS = product_container_TOS.find_element("class name", "prodTitle").get_element("innerText")
            prod_names_TOS.append(product_name_TOS)
        print(prod_names_TOS)