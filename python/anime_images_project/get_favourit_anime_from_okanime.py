from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/NS/Desktop/random stuff/python folder/86/chromedriver.exe")
driver.get('https://okanime.tv/library/favorites')


def log_in():
    email = driver.find_element_by_id("login-email")
    email.send_keys("username")
    password = driver.find_element_by_id("login-password")
    password.send_keys("password")
    login = driver.find_element_by_name("commit")
    login.click()


log_in()


driver.get('https://okanime.tv/library/favorites')

container = driver.find_element_by_id("Favorites")
link_containers = container.find_elements_by_class_name("batnie-image")

list_of_links = []
for link_container in link_containers:
    link = link_container.find_element_by_tag_name("a")
    list_of_links.append(link.get_attribute("href"))


name_year_dict = dict()
for a in list_of_links:
    driver.get(a)
    container_of_name = driver.find_element(By.CLASS_NAME, "col-md-9")
    container_of_name2 = container_of_name.find_element(By.CLASS_NAME, "author-info-title")
    messy_name = container_of_name2.find_element(By.TAG_NAME, "h6").text

    try:
        year = int(messy_name[-1:-5:-1][::-1])
        name = messy_name[3:-4]
    except ValueError:
        name = messy_name[3:]
        year = None
    rating = messy_name[0:3]
    name_year_dict[name] = [year, rating]
    print(f"{name},{year},{rating}")
