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

productOwned_farm = "1" 
actions = ActionChains(browser)
#http://www.koalastothemax.com/


def buy_farm(farm):
    upgrade_actions = ActionChains(browser)
    upgrade_actions.move_to_element(farm)
    upgrade_actions.click(farm)
    upgrade_actions.perform()

def check_unlock_next_farm(productOwned_farm):
    owned_qtd_html = browser.find_element_by_id("productOwned" + productOwned_farm)
    if owned_qtd_html.text == "1":
        productOwned_farm = str(int(productOwned_farm)+1)
        farms = [browser.find_element_by_id("productPrice" + str(i)) for i in range(productOwned_farm,-1,-1)]
    pass


for i in range(5000): 
    actions.click(cookie)
    actions.perform() 

    check_unlock_next_farm(productOwned_farm)

    count = int(cookie_count.text.split(" ")[0])
    len_farms = len(farms)


    for i in range(len_farms):
        value_farm = int(farms[i].text) 
        if i > 0:
            value_next_farm = int(farms[i-1].text) 
            if value_farm * 4 < value_next_farm: 
                if value_farm <= count: 
                    buy_farm(farms[i])
        else:
            if value_farm <= count: 
                buy_farm(farms[i])
                


    
