from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,winsound

driver = webdriver.PhantomJS()




def progerss_state(text):
    while "Report in progress" in text:
        print(text)
        time.sleep(5)
        progerss_state(get_page())
    else:
        winsound.PlaySound(r'C:\Windows\Media\Windows Notify Calendar.wav', winsound.SND_FILENAME)
        print(" ==== Done ====")
        print(text)

def get_page():


    # login or not
    try:
        login = driver.find_element_by_link_text("IT-647-X1362 Web Site Construction & Mgmt 16TW1")
    except:
        driver.get("https://bb.snhu.edu/webapps/login/")

        id_box = driver.find_element_by_id("user_id")
        pass_box = driver.find_element_by_id("password")
        submit_btn = driver.find_element_by_id("loginFormList").find_element_by_name("login")

    # Blackboard user name and password
        id_box.send_keys("YOUR BLACKBOARD ID")
        pass_box.send_keys("BLACKBOARD PASSWORD")
        submit_btn.click()
        print("Login Success")


    wait_list = [{"course_name":(By.LINK_TEXT, "IT-647-X1362 Web Site Construction & Mgmt 16TW1")},
                     {"learning_modules":(By.ID, "paletteItem:_2156234_1")},
                     {"module_one":(By.ID, "_13381958_1")},
                     {"short_paper_1_3":(By.ID, "_13381975_1")},
                     {"safe_assign":(By.ID, "safeassignHeader")}
                     ]


    for i in wait_list:
        if isPresent(list(i.values())[0]):
            if "safe_assign" not in i.keys():
                try:
                    driver.find_element(list(i.values())[0][0], list(i.values())[0][1]).find_element_by_tag_name("h3").find_element_by_tag_name('a').click()
                except:
                    if "learning_modules" in i.keys():
                        driver.find_element(list(i.values())[0][0], list(i.values())[0][1]).find_element_by_tag_name('a').click()
                    else:
                        driver.find_element(list(i.values())[0][0], list(i.values())[0][1]).click()
            else:
                state = driver.find_element(list(i.values())[0][0], list(i.values())[0][1]).find_element_by_class_name("metadata").text
                return state
        else:
            break
    return "Progress Error!"


def isPresent(locator):
    try:
        element =  WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(locator))
    except:
        print("No Item found!")
        with open("page.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)
        return False
    else:
        print(locator[1],"is found, next step:")
        return True


progerss_state(get_page())