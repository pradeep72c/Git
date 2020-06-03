from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = False
driver=webdriver.Firefox(capabilities=caps)

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False
#
# driver = webdriver.Firefox(capabilities=cap,executable_path=r'C:\Users\Admin\Desktop\Angularjs\Python\Drivers\geckodriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
driver.quit()
