import sys,os,pytest
from time import sleep
sys.path.append(os.getcwd())
from page.page_opt import page_opt
from comm.init_driver import get_driver
from comm.init_data import  get_data
import page

class Test_login:
    def setup_class(self):
        self.page_obj = page_opt(get_driver())
        self.page_obj.click_login_btn()
    def teardown_class(self):
        sleep(3)
        self.page_obj.driver.quit()
    @pytest.mark.parametrize("caseid,uid,pwd,except_result",get_data())
    def test_login(self,caseid,uid,pwd,except_result):
        self.page_obj.login_opt(uid,pwd,except_result)


