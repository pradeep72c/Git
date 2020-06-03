from  selenium import webdriver

driver = webdriver.Ie(executable_path=r'C:\Users\Admin\Desktop\Angularjs\Python\Drivers\IEDriverServer.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
driver.quit()