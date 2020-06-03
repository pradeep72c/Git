from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Desktop\Angularjs\Python\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
signin = driver.find_element_by_id('signin_button')
signin.click()
assert 'Zero - Log in' == driver.title
driver.find_element_by_id('user_login').send_keys('username')
driver.find_element_by_id('user_password').send_keys('password')
driver.find_element_by_name('submit').click()
driver.find_element_by_xpath('//*[@id="transfer_funds_tab"]/a').click()
frmaccele = driver.find_element_by_css_selector('#tf_fromAccountId')
frmacc = Select(frmaccele)
# frmacc.select_by_index(3)
# frmacc.select_by_value("2")
frmacc.select_by_visible_text('Loan(Avail. balance = $ 780)')
toaccele = driver.find_element_by_css_selector('#tf_toAccountId')
toacc = Select(toaccele)
toacc.select_by_visible_text('Brokerage(Avail. balance = $ 197)')
driver.find_element_by_xpath('//*[@id="tf_amount"]').send_keys('900')
driver.find_element_by_css_selector('#tf_description').send_keys('Money Transfer')
driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
assert False == driver.find_element_by_css_selector('#tf_fromAccountId').is_enabled()
assert False == driver.find_element_by_xpath('//*[@id="tf_toAccountId"]').is_enabled()
assert False == driver.find_element_by_xpath('//*[@id="tf_amount"]').is_enabled()
assert False == driver.find_element_by_xpath('//*[@id="tf_description"]').is_enabled()
driver.find_element_by_css_selector('#btn_submit').click()
msg = driver.find_element_by_xpath('//*[@id="transfer_funds_content"]/div/div/div[1]').text
assert 'You successfully submitted your transaction.' == msg
# driver.quit()