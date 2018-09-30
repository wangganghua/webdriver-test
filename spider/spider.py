# -*- encoding:utf-8 -*-

from selenium import webdriver
# from selenium.webdriver import ActionChains
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(sys.path)

# pip install  selenium (3.14.1)
# 安装火狐  v57 64位
# 下载geckodriver-v0.19.1-win64.zip 、火狐驱动包 .exe ，放在 安装的python 目录


def test():
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    driver.find_element_by_name("wd").send_keys("python")
    driver.find_element_by_id("su").click()
    # driver.refresh()
    print driver.title
    # print driver.current_url
    time.sleep(30*6)
    driver.quit()
test()