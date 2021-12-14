from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = "C:/Program Files (x86)/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"



option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://orteil.dashnet.org/cookieclicker/")

browser.implicitly_wait(5) # Espera 5 segundos

cookie = browser.find_element_by_id("bigCookie") #Objeto cookie
cookie_count = browser.find_element_by_id("cookies")
cookies_ps_id = browser.find_element_by_id("compactCookies")


farms = [browser.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]
upgrade = browser.find_element_by_id("upgrades")

productOwned_num = "1" 
actions = ActionChains(browser)
recalc = False
#http://www.koalastothemax.com/


for i in range(500000): 

    owned = browser.find_element_by_id("productOwned" + productOwned_num)
    if owned.text == "1":
        productOwned_num = str(int(productOwned_num)+1)

        farms = [browser.find_element_by_id("productPrice" + str(i)) for i in range(productOwned_num,-1,-1)]
    

    if recalc == True:  

        farms = [browser.find_element_by_id("productPrice" + str(i)) for i in range(1,17,-1)]
        upgrade = browser.find_element_by_id("upgrades")

    actions.click(cookie)
    actions.perform() 
    count = int(cookie_count.text.split(" ")[0])
    
    len_farm = len(farm)
    for farm in farms: 
        value_farm = int(farm.text) 
        if value_farm <= count: 
            upgrade_actions = ActionChains(browser)
            upgrade_actions.move_to_element(farm)
            upgrade_actions.click(farm)
            upgrade_actions.perform()