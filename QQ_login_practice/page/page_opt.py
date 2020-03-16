from time import sleep
import allure
from comm.comm import comm
import page
class page_opt(comm):
    def __init(self,driver):
        comm.__init__(self,driver)
    @allure.step(title="点击同意和登录")
    def click_login_btn(self):
        sleep(40)
        self.click_element(page.agree)
        self.click_element(page.click_login)
    @allure.step(title='输入用户名和密码')
    def login_opt(self,uid,pwd,except_result):
        self.input_element(page.uid,uid)
        self.input_element(page.pwd,pwd)
        self.click_element(page.login)
        try:
            sleep(2)
            self.click_element(page.head)
            sleep(2)
            self.click_element(page.setting)
            sleep(2)
            self.click_element(page.user_manager)
            sleep(2)
            self.click_element(page.logout_user)
            sleep(2)
            self.click_element(page.makesure_logout)
            sleep(2)
            assert except_result == 'pass'
        except Exception as e:
            self.click_element(page.fail_login)
            assert except_result == 'fail'

