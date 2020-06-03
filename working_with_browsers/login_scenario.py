from  selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Desktop\Angularjs\Python\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
signin = driver.find_element_by_id('signin_button')
signin.click()
assert 'Zero - Log in' == driver.title
driver.find_element_by_id('user_login').send_keys('username')
driver.find_element_by_id('user_password').send_keys('password')
driver.find_element_by_name('submit').click()
driver.quit()