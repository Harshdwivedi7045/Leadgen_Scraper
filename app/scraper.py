from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scrape_google_maps(location):
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/maps')

    time.sleep(2)
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.clear()
    search_box.send_keys(location)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    results = []
    try:
        listings = driver.find_elements(By.CLASS_NAME, 'Nv2PK')
        for listing in listings:
            try:
                name = listing.find_element(By.CLASS_NAME, 'qBF1Pd').text
            except:
                name = 'N/A'
            try:
                address = listing.find_element(By.CLASS_NAME, 'rllt__details').text
            except:
                address = 'N/A'
            try:
                phone = listing.find_element(By.CLASS_NAME, 'UsdlK').text
            except:
                phone = 'N/A'
            results.append({
                'name': name,
                'address': address,
                'phone': phone
            })
    except Exception as e:
        print("Error extracting listings:", e)

    driver.quit()
    return results
