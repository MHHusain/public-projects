from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r"C:\Users\NS\Desktop\random stuff\python folder\chromedriver_win32---------88\chromedriver.exe")
driver.get("https://onma.me/manga/pandora-hearts")
links = driver.find_element(By.XPATH, "//a[@class='download']")
print(links.get_attribute("href"))