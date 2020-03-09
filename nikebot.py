from selenium import webdriver
from time import sleep

class NikeBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.nike.com/cn/t/react-vision-%E7%94%B7%E5%AD%90%E8%BF%90%E5%8A%A8%E9%9E%8B-H3Wpwv/CD4373-002')
        sleep(1)
        try:
            close_btn = self.driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header"]/header/aside/div/button/i')
            close_btn.click()

        #option_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')

        #option_btn.click()


        except:
        #Find button & click
            login_btn = self.driver.find_element_by_xpath(
                     '//*[@id="AccountNavigationContainer"]/button')
            login_btn.click()

            #Select window to handle
            text_area = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/header/div[2]/div/div[1]/div/div[6]/form/div[2]/div[3]/input')
            text_area.send_keys('15655240958')

            pwd_area = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/header/div[2]/div/div[1]/div/div[6]/form/div[3]/input')
            pwd_area.send_keys('Haozihaoya123')

            login_btn2 = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/header/div[2]/div/div[1]/div/div[6]/form/div[7]/input')
            login_btn2.click()



            size_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/fieldset/div/div[7]/label')

            add_to_cart_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[2]/button[1]')
            add_to_cart_btn.click()
        # base_window = self.driver.window_handles[0]
        # popup_window = self.driver.window_handles[1]
        # self.driver.switch_to_window(popup_window)
        #
        # #Fill in text
        # email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        # email_in.send_keys('411518343@qq.com')
        #
        # pwd_in =self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pwd_in.send_keys('Haozihaoya123')
        #
        # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        # login_btn.click()
        #
        # self.driver.switch_to_window(base_window)
        #
        # pop1_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # pop1_btn.click()

       # pop2_btn = self.driver.find_element_by_xpath('')


bot = NikeBot()
bot.login()

