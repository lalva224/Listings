
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException


def getLinks(website_url):
    driver.get(website_url)


    wait = WebDriverWait(driver, 1000)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiButtonBase-root ")))

    urls = []
    listing_links = driver.find_elements(By.CLASS_NAME,"MuiLink-root")


    for link in listing_links:
        url = link.get_attribute("href")
        if url is not None and "niche.com/k12/" in url:
            niche_url = url

        if niche_url is not None:
            urls.append(niche_url)

    unique_urls = list(set(urls))

    return unique_urls


#myrhmamVTjorkhs
PATH = "C:\\Program Files (x86)\\chromedriver_win32\\chromedriver.exe"
driver = uc.Chrome(executable_path=PATH)
URL = "https://www.niche.com/k12/search/montessori-schools/"
driver.get(URL)



   

school_names = []
addresses = []
states = []
cities = []
zips = []
websites = []
phone_numbers = []

page = 70


while(page<104):
    if(page>1):
        URL = f"https://www.niche.com/k12/search/montessori-schools/?page={page}"
    page+=1
    try: 
        unique_urls = getLinks(URL)

        for unique_url in unique_urls:
            driver.get(unique_url)
            
            try:
                wait = WebDriverWait(driver, 2)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME,"profile__address--compact")))
        
                address_full = driver.find_element(By.CLASS_NAME,"profile__address--compact")
                
                
                address_parts = address_full.text.strip().split("\n")

                if(len(address_parts)>1):
                    city_state_zip = address_parts[1].strip().split(",")
                    state_zip = city_state_zip[1].strip().split(" ")     

                address = address_parts[0]
                city = city_state_zip[0]
                state = state_zip[0]
                zip = state_zip[1]

                addresses.append(address)
                cities.append(city)
                states.append(state)
                zips.append(zip)

            except TimeoutException:
                try:
                    time.sleep(2)
                    driver.find_element(By.CLASS_NAME,"px-captcha-message")
                    wait = WebDriverWait(driver, 10000)
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"footer-logo")))
                    continue   
                except NoSuchElementException:    
                    continue
            except NoSuchElementException:
                addresses.append("NA")
                cities.append("NA")
                states.append("NA")
                zips.append("NA")
            except IndexError:
                print(address_full)
                addresses.append("NA")
                cities.append("NA")
                states.append("NA")
                zips.append("NA")


            
            try:
                school_name = driver.find_element(By.CLASS_NAME,"postcard__title")
                school_names.append(school_name.text)
            except NoSuchElementException:
                school_names.append("NA")
                
            try:
                website = driver.find_element(By.CLASS_NAME,"profile__website__link")
                websites.append(website.text)
            except NoSuchElementException:
                websites.append("NA")
                
            try:    
                phone_number = driver.find_element(By.CLASS_NAME,"profile__telephone__link")
                phone_numbers.append(phone_number.text)
            except NoSuchElementException:
                phone_numbers.append("NA")

    except NoSuchWindowException:
            break


            
   

   

        
    

data = {
    "School Name" : school_names,
    "Address" :addresses,
    "City" : cities,
    "State" : states,
    "Zip" : zips,
    "Website" : websites,
    "Phone Number" : phone_numbers,
    

}


print(page)
dataframe = pd.DataFrame(data)
dataframe.to_csv("new_listings.csv", mode = 'a',encoding="utf-8",index=False, header=False)

   
    



## very manual, time consuming -- 3 hrs with no errors.

# listings = driver.find_elements(By.XPATH, "//h2[contains(@class, 'MuiLink-root')]")
# size = len(listings)

# for i in range(size):
#     listing = listings[i]
#     driver.execute_script("arguments[0].click();",listing)
#     time.sleep(2)
#     print(driver.title)
#     driver.back()
#     time.sleep(2)

# for listing in listings:
#    listing.click()
#    wait = WebDriverWait(driver, 5)
#    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content")))

#    print(driver.title)

#    driver.back()
#    wait = WebDriverWait(driver, 5)
#    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiLink-underlineHover")))



# print("School names", len(school_names))
# print("Cities", len(cities))
# print("States", len(states))
# print("Zips", len(zips))
# print("Websites",len(websites))
# print("Phone Numbers", len(phone_numbers))



# wait = WebDriverWait(driver,3)
# wait.until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))
# time.sleep(10)
# button = driver.find_element(By.CSS_SELECTOR,css)
# ActionChains(driver).click_and_hold(button).perform()



# ActionChains(driver).release(button).perform


    





    





