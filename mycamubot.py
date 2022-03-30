import schedule
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")

driver = None
URL = "https://www.mycamu.co.in/"


def start_browser():
    global driver
    driver = webdriver.Chrome(options=opt, service_log_path='NUL')

    driver.get(URL)

    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))


def login():
    global driver
    print("browser opened")
    print("went to site")
    time.sleep(5)
    # search_box = driver.find_element(By.XPATH, '//*[@id="proceed_id"]')
    # search_box.click()
    time.sleep(5)
    print("proceed clicked")
    user = driver.find_element(By.XPATH, '//*[@id="username"]')
    user.send_keys("your gmail here")
    print("username")
    passw = driver.find_element(By.XPATH, '//*[@id="password"]')
    passw.send_keys("your password here" + Keys.RETURN)
    print("password")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,130)")
    time.sleep(2)
    print("scrolled down ")
    driver.find_element(By.XPATH,
                        '// *[ @ id = "Timetable"] / a').click()
    print("timetable clicked")
    time.sleep(2)


def class11():
    global driver
    driver.find_element(By.XPATH, '//*[@id="tdy_schdl"]/div[1]/div[4]/div[2]/a').click() or driver.find_element(
        By.XPATH, '//*[@id="tdy_schdl"]/div[1]/div[5]/div[2]/a').click() or driver.find_elements(
            By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[2]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="attendanceConfirmModal"]/div/div/div[3]/button[2]').click()
    print("clicked yes")
    time.sleep(2)
    print("class 1 attend")


def class22():
    driver.find_element(By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[4]/div[2]/a').click() or driver.find_element(
        By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[2]/a').click() or driver.find_elements(
        By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[2]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="attendanceConfirmModal"]/div/div/div[3]/button[2]').click()
    print("clicked yes")
    print("class 2 attend")


def class33():
    driver.find_element(By.XPATH, '//*[@id="tdy_schdl"]/div[3]/div[4]/div[2]/a').click() or driver.find_element(
        By.XPATH, '//*[@id="tdy_schdl"]/div[3]/div[5]/div[2]/a').click() or driver.find_elements(
            By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[3]/a').click()
    print("sa")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="attendanceConfirmModal"]/div/div/div[3]/button[2]').click()
    print("clicked yes")


def class44():
    driver.find_element(By.XPATH, '//*[@id="tdy_schdl"]/div[4]/div[4]/div[2]/a').click() or driver.find_element(
        By.XPATH, '//*[@id="tdy_schdl"]/div[5]/div[4]/div[2]/a').click() or driver.find_element(
            By.XPATH, '//*[@id="tdy_schdl"]/div[4]/div[5]/div[2]/a').click() or driver.find_elements(
                By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[4]/a').click() or driver.find_elements(
                    By.XPATH, '//*[@id="tdy_schdl"]/div[4]/div[4]/div[2]/a').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="attendanceConfirmModal"]/div/div/div[3]/button[2]').click()
    print("clicked yes")
    time.sleep(3)
    print("attending class 4")


def class55():
    driver.find_element(By.XPATH, '//*[@id="tdy_schdl"]/div[5]/div[5]/div[2]/a').click() or driver.find_element(
        By.XPATH, '//*[@id="tdy_schdl"]/div[5]/div[5]/div[2]/a').click() or driver.find_elements(
            By.XPATH, '//*[@id="tdy_schdl"]/div[2]/div[5]/div[5]/a').click()
    print("1s")
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="attendanceConfirmModal"]/div/div/div[3]/button[2]').click()

    print("clicked yes")
    time.sleep(3)
    print("attending class 5")

def class1():
    global driver
    start_browser()
    login()
    time.sleep(2)
    k = 1
    while k <= 5:
        driver.refresh()
        time.sleep(2)
        try:
            class11()
            break
        except:
            time.sleep(60)
            k += 1

    driver.close()
    driver.quit()


def class2():
    global driver
    start_browser()
    login()
    time.sleep(2)
    k = 1
    while k <= 5:
        driver.refresh()
        time.sleep(2)
        try:
            class22()
            break
        except:
            time.sleep(60)
            k += 1
    driver.close()
    driver.quit()


def class3():
    global driver
    start_browser()
    login()
    time.sleep(2)
    k = 1
    while k <= 5:
        driver.refresh()
        time.sleep(2)
        try:
            class33()
            break
        except:
            time.sleep(60)
            k += 1
    driver.close()
    driver.quit()


def class4():
    global driver
    start_browser()
    login()
    time.sleep(2)
    k = 1
    while k <= 5:
        driver.refresh()
        time.sleep(2)
        try:
            class44()
            break
        except:
            time.sleep(60)
            k += 1
    driver.close()
    driver.quit()


def class5():
    global driver
    start_browser()
    login()
    time.sleep(2)
    k = 1
    while k <= 5:
        driver.refresh()
        time.sleep(2)
        try:
            class55()
            break
        except:
            time.sleep(60)
            k += 1
    driver.close()
    driver.quit()


schedule.every().monday.at("09:10").do(class1)
schedule.every().monday.at("10:00").do(class2)
schedule.every().monday.at("10:48").do(class3)
schedule.every().monday.at("11:40").do(class4)
schedule.every().monday.at("12:25").do(class5)

schedule.every().tuesday.at("09:10").do(class1)
schedule.every().tuesday.at("10:00").do(class2)
schedule.every().tuesday.at("10:48").do(class3)
schedule.every().tuesday.at("11:40").do(class4)
schedule.every().tuesday.at("12:25").do(class5)

schedule.every().wednesday.at("09:10").do(class1)
schedule.every().wednesday.at("10:00").do(class2)
schedule.every().wednesday.at("10:48").do(class3)
schedule.every().wednesday.at("11:40").do(class4)
schedule.every().wednesday.at("12:25").do(class5)

schedule.every().thursday.at("09:10").do(class1)
schedule.every().thursday.at("10:00").do(class2)
schedule.every().thursday.at("10:48").do(class3)
schedule.every().thursday.at("11:28").do(class4)
schedule.every().thursday.at("12:25").do(class5)

schedule.every().friday.at("09:10").do(class1)
schedule.every().friday.at("10:00").do(class2)
schedule.every().friday.at("10:48").do(class3)
schedule.every().friday.at("11:40").do(class4)
schedule.every().friday.at("12:25").do(class5)

schedule.every().saturday.at("09:10").do(class1)
schedule.every().saturday.at("10:00").do(class2)
schedule.every().saturday.at("10:48").do(class3)
schedule.every().saturday.at("11:40").do(class4)
schedule.every().saturday.at("12:25").do(class5)


while True:
    schedule.run_pending()
    time.sleep(1)
