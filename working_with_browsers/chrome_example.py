from  selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Desktop\Angularjs\Python\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
driver.quit()