#!/usr/bin/env python
# coding: utf-8

# # Scrape the website of Global Salmon Initiative
# 
# https://globalsalmoninitiative.org/en/sustainability-report/sustainability-indicators/
# 
# 

# In[124]:


import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[159]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[145]:


# driver.find_elements(By.CLASS_NAME, "countryBlock")
#countries = driver.find_elements(By.CLASS_NAME, "countryBlock")
#countries[0].click()


# In[160]:


driver.get("https://globalsalmoninitiative.org/en/sustainability-report/sustainability-indicators/")


# In[161]:


countries = driver.find_elements(By.CLASS_NAME, "countryBlock")


# In[162]:


country_ids = ['companyCount_australia','companyCount_canada', 'companyCount_chile', 'companyCount_faroes', 'companyCount_new-zealand', 'companyCount_norway', 'companyCount_scotland']


# In[173]:


driver.get('https://globalsalmoninitiative.org/en/sustainability-report/sustainability-indicators/#aquachile')


# In[174]:


for country_id in country_ids[:1]:
    driver.find_element(By.ID, country_id).click()
    time.sleep(10)
    companyTitles = driver.find_elements(By.CLASS_NAME, "companyTitle")
    for company in companyTitles:
        if company.is_displayed() and company.is_enabled():
            company.click()
            time.sleep(5)
            # TODO: add code to scrape table data of this company
            fishEscapes = driver.find_element(By.ID, "fish-escapes")
            #print(fishEscapes.text)
            EscapesTable = fishEscapes.find_elements(By.CLASS_NAME, 'table-bordered')
            for table in EscapesTable:
                year = table.find_elements(By.TAG_NAME, "h3")
                if len(year)>0:
                    print(year[0].text)
                print("****")
            
            ## end of code that gets data for a specific company
            
            driver.find_element(By.ID, "companies-reset").click()
            time.sleep(5)
    
    driver.get("https://globalsalmoninitiative.org/en/sustainability-report/sustainability-indicators/")
    time.sleep(10)


# In[85]:





# In[ ]:





# In[126]:


driver.get("https://globalsalmoninitiative.org/en/sustainability-report/sustainability-indicators/")


# In[127]:


companyTitles = driver.find_elements(By.CLASS_NAME, "companyTitle")
    


# In[128]:


from selenium.webdriver.common.action_chains import ActionChains

for company in companyTitles:
    print(company.is_enabled())
    #company.click()
    ActionChains(driver).move_to_element(company).perform()
    #.click(company).perform()
    time.sleep(5)


# In[ ]:




