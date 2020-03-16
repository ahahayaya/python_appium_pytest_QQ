from selenium.webdriver.support.wait import WebDriverWait
# from comm.init_driver import get_driver
class comm:
    def __init__(self,driver):
        self.driver = driver
    def search_element(self,loc):
        return WebDriverWait(self.driver,25,1).until(lambda x:x.find_element(*loc))
    def click_element(self,loc):
        self.search_element(loc).click()
    def input_element(self,loc,text):
        self.search_element(loc).clear()
        self.search_element(loc).send_keys(text)



