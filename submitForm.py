from selenium import webdriver 
import time
import random
def openChrome():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options= options)
    return driver
def operationAuth(driver):
    url = "https://www.wjx.cn/m/28777538.aspx"
    driver.get(url)
    for i in range(1,7,1):
        try:
            time.sleep(2)
            #   /div[@id="div{i}"]/div[@class="ui-controlgroup"]/a[@class="jqradio"]
            # //*[@id="div12"]/ul/li[1]

            elem = driver.find_elements_by_xpath(f'//*[@id="div{i}"]/div[@class="ui-controlgroup"]//a[@class="jqradio"]')
            print(elem)
            print(f'第{i}次')
            pos = random.randint(0,len(elem)-1)
            elem[pos].click()
        except:
            pass
    for j in range(0,12,1):
        try:
            checks = driver.find_elements_by_xpath(f'//*[@id="div{j}"]/div[@class="ui-controlgroup"]//a[@class="jqcheck"]')
            print(checks)
            for item in range(0,len(checks)-1):
                checks[item].click()
        except:
            pass
    checks = driver.find_elements_by_xpath('//*[@id="div12"]/ul/li')
    print(len(checks))
    for item in range(0,len(checks)):
                time.sleep(1)
                checks[item].click()
    print('操作完毕')
 
    text1=driver.find_element_by_xpath('//*[@id="q13"]')
    text2=driver.find_element_by_xpath('//*[@id="q14"]')
    text1.send_keys("来自班长的恶搞")
    text2.send_keys("来自班长的恶搞")
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
if __name__=="__main__":
    driver = openChrome()
    operationAuth(driver)
