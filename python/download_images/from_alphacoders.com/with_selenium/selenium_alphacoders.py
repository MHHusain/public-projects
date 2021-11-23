import os
import requests
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


class search_and_url(BaseException):
    pass


class both_none(BaseException):
    pass


class Download:
    FOLDER_INDEX = 0
    FOLDER_ID = random.randint(1, 1000)

    def __init__(self, chrome_web_driver, directory=""):
        self.directory = directory
        self.chrome_web_driver = chrome_web_driver
        self.searches_folder = os.path.join(f"{self.directory}", f'text_folder{Download.FOLDER_ID}')

    def download_links(self, search=None, url=None, pages=1000):
        Download.FOLDER_INDEX += 1
        driver = webdriver.Chrome(self.chrome_web_driver)
        if search and url:
            raise search_and_url("you have to use search or url parameter")
        elif url:
            driver.get(url)
            bais_directory = f'{self.searches_folder}/{url}{Download.FOLDER_INDEX}'
            os.makedirs(bais_directory)
        elif search:
            search_string = search.replace(" ", "+")
            driver.get(f"https://wall.alphacoders.com/search.php?search={search_string}")
            bais_directory = f'{self.searches_folder}/{search}{Download.FOLDER_INDEX}'
            os.makedirs(bais_directory)
        else:
            raise both_none("search and url cannot be both none")
        next_link = ""
        index = 1
        while next_link != '#' and index <= pages:
            current_url = driver.current_url
            driver.implicitly_wait(5)
            container_imageslinks = driver.find_elements(By.XPATH, "//div[@class='boxgrid']")
            list_of_imageslinks = []
            for i in container_imageslinks:
                imageslinks = i.find_element(By.TAG_NAME, "a")
                list_of_imageslinks.append(imageslinks.get_attribute("href"))
            links = []
            for e in list_of_imageslinks:
                driver.get(e)
                image = driver.find_element(By.CLASS_NAME, "main-content")
                links.append(image.get_attribute("src"))
            with open(f"{bais_directory}/{index}.txt", 'a') as links_file:
                for i in links:
                    links_file.write(i)
                    links_file.write("\n")
            driver.get(current_url)
            try:
                page_div = driver.find_element(By.CLASS_NAME, "visible-sm")
            except selenium.common.exceptions.NoSuchElementException:
                print("number of pages is 1")
                break
            ul = page_div.find_element(By.CLASS_NAME, 'pagination')
            next_button = ul.find_element(By.CLASS_NAME, "next-container")
            next_link = next_button.get_attribute("href")
            if next_link != "#":
                driver.get(next_link)
            index += 1
        driver.quit()
        return True

    def preform_instalation(self, text_folder_dir=None):
        if not text_folder_dir:
            images_folder = os.path.join(f"{self.directory}", f'images_of text_folder{Download.FOLDER_ID}')
            pass_ = 0
            for current_path, dir_folders, file_names in os.walk(self.searches_folder):
                if pass_ != 0:
                    search_folder = f'{images_folder}/{os.path.split(current_path)[-1]}'
                    os.makedirs(search_folder)
                    for each_file_name in file_names:
                        with open(f"{current_path}/{each_file_name}.txt") as text:
                            links = text.read().split('\n')
                            for each_link in links:
                                try:
                                    image = requests.get(each_link)
                                    with open(
                                            f'{search_folder}/page{each_file_name.split(".")[0]}_{random.randint(1, 1000000000)}.jpg',
                                            'wb') as image_file:
                                        image_file.write(image.content)
                                except requests.exceptions.MissingSchema:
                                    pass
                pass_ = 1
        else:
            spliting_dir = os.path.split(text_folder_dir)
            images_folder = os.path.join(spliting_dir[0], f'images_of {spliting_dir[-1]}')
            pass_ = 0
            for current_path, dir_folders, file_names in os.walk(text_folder_dir):
                if pass_ != 0:
                    search_folder = f'{images_folder}/{os.path.split(current_path)[-1]}'
                    os.makedirs(search_folder)
                    for each_file_name in file_names:
                        with open(f"{current_path}/{each_file_name}") as text:
                            links = text.read().split('\n')
                            for each_link in links:
                                try:
                                    image = requests.get(each_link)
                                    with open(
                                            f'{search_folder}/page{each_file_name.split(".")[0]}_{random.randint(1, 1000000000)}.jpg',
                                            'wb') as image_file:
                                        image_file.write(image.content)
                                except requests.exceptions.MissingSchema:
                                    pass
                pass_ = 1


if __name__ == '__main__':
    download_obj = Download(r"C:\Users\NS\Desktop\random stuff\python folder\86\chromedriver.exe")
    download_obj.download_links("Re Zero")
    download_obj.preform_instalation()
