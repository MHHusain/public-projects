from selenium import webdriver


def reboot_router(driver_path, gateway, user_name, _password):
    driver = webdriver.Chrome(driver_path)
    driver.get(gateway)
    username = driver.find_element_by_id("userName")
    password = driver.find_element_by_id("pcPassword")
    username.send_keys(user_name)
    password.send_keys(_password)
    login = driver.find_element_by_id("loginBtn")
    login.click()
    system = driver.find_element_by_id("a43")
    system.click()
    reboot_link = driver.find_element_by_id("a49")
    reboot_link.click()
    reboot = driver.find_element_by_id("reboot")
    reboot.click()


reboot_router(r"C:\Users\NS\Desktop\Projects\python project\selenium\chromedriver_win32\chromedriver.exe", "http://192.168.0.1", "admin", "admin")
