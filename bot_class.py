from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class CookieClickerBot:
    def __init__(self) -> None:

        self.setup()
        self.browser.implicitly_wait(10) # Espera 5 segundos

        self.basic_elements()
        
        self.actions = ActionChains(self.browser)
        while True:
            self.controller()
    
    def setup(self):
        #Brave Browser - Windows
        driver_path = "C:/Program Files (x86)/chromedriver.exe"
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

        self.option = webdriver.ChromeOptions()
        self.option.binary_location = brave_path
        self.browser = webdriver.Chrome(executable_path=driver_path, chrome_options=self.option)
        self.browser.get("https://orteil.dashnet.org/cookieclicker/")

    def basic_elements(self):
        self.cookie = self.browser.find_element_by_id("bigCookie") #Objeto cookie
        self.cookie_count = self.browser.find_element_by_id("cookies")
        self.cookies_ps_id = self.browser.find_element_by_id("compactCookies")

        self.farms = [self.browser.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]
        self.upgrade = self.browser.find_element_by_id("upgrades")

        self.productOwned_farm = "1" 

    def buy_farm(self, farm):
        upgrade_actions = ActionChains(self.browser)
        upgrade_actions.move_to_element(farm)
        upgrade_actions.click(farm)
        upgrade_actions.perform()

    
    def check_unlock_next_farm(self):
        owned_qtd_html = self.browser.find_element_by_id("productOwned" + self.productOwned_farm)
        if owned_qtd_html.text == "1":
            self.productOwned_farm = str(int(self.productOwned_farm)+1)
            self.farms = [self.browser.find_element_by_id("productPrice" + str(i)) for i in range(int(self.productOwned_farm),-1,-1)]
        
    def controller(self):
        self.actions.click(self.cookie)
        self.actions.perform() 

        self.check_unlock_next_farm()

        count_str = self.cookie_count.text.split(" ")[0]
        count = int(count_str.replace(',', ''))


        len_farms = len(self.farms)


        for i in range(len_farms):
            value_farm_str = self.farms[i].text
            value_farm = int(value_farm_str.replace(',', ''))

            if i > 0:
                value_next_farm_str = self.farms[i-1].text
                value_next_farm = int(value_next_farm_str.replace(',', ''))

                if value_farm * 5 < value_next_farm: 
                    if value_farm <= count: 
                        self.buy_farm(self.farms[i])
            else:
                if value_farm <= count: 
                    self.buy_farm(self.farms[i])
                

bot = CookieClickerBot()
bot()