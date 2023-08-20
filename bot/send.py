from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge import service
import os
os.system("cls") #clear screen from previous sessions
import time
import sqlite3
from datetime import datetime, timedelta

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
my_service=service.Service(r'msedgedriver.exe')
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage') # uses disk instead of RAM, may be slow

s = 10 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(service=my_service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)

username = "admin"
password = "admin"
login_page = "https://moodle.rea.perm.ru/login/index.php"
base_url = "https://moodle.rea.perm.ru/user/profile.php?id="
text_file = open("moodle-message.txt", "r")
message = text_file.read()
text_file.close()

# Create table to store Moodle pages urls and dates of sending a message
def create_table():
    conn = sqlite3.connect('recepients-and-dates.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        moodle_page_url TEXT PRIMARY KEY,
        date_sent TEXT
    )
    """)
    conn.commit()
    conn.close()
create_table()

def send_a_message():
    name = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@class="h2"]'))).get_attribute('innerHTML')
    personalized_message = "Dear " + name + "!\n\n" + message
    
    try:
        add_contact = driver.find_element(By.XPATH, '//a[@id="toggle-contact-button" and contains(., "Добавить в список контактов")]')
        action.move_to_element(add_contact).perform()
        action.click(add_contact).perform()
        time.sleep(3)
    except:
        pass
    
    message_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="message-user-button"]')))
    action.click(message_button).perform() 
    time.sleep(5)
    
    try:
        text_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@data-region="send-message-txt"]')))
        driver.execute_script('arguments[0].innerHTML = arguments[1]', text_area, personalized_message)
        time.sleep(3)
        
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="send-message"]')))
        action.move_to_element(send_button).perform()
        action.click(send_button).perform()
        time.sleep(5)
        return 0
    except:
        return 1 

def check_and_send_message(recepient_url):
    moodle_page_url = recepient_url
    conn = sqlite3.connect('recepients-and-dates.db')
    cursor = conn.cursor()

    # Query for the user by moodle_page_url
    cursor.execute("SELECT date_sent FROM messages WHERE moodle_page_url = ?", (moodle_page_url,))
    result = cursor.fetchone()

    if result:
        date_sent_str = result[0]
        if date_sent_str:
            date_sent = datetime.strptime(date_sent_str, '%Y-%m-%d')
            if datetime.now() - date_sent > timedelta(days=365):
                if send_a_message() == 0: # if sending messages is allowed
                    update_date_sent(moodle_page_url)
        else:
            if send_a_message() == 0: # if sending messages is allowed
                update_date_sent(moodle_page_url)
    else:
        if send_a_message() == 0: # if sending messages is allowed
            insert_user(moodle_page_url)

    conn.close()

def insert_user(moodle_page_url):
    conn = sqlite3.connect('recepients-and-dates.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (moodle_page_url, date_sent) VALUES (?, ?)", (moodle_page_url, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def update_date_sent(moodle_page_url):
    conn = sqlite3.connect('recepients-and-dates.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE messages SET date_sent = ? WHERE moodle_page_url = ?", (datetime.now().strftime('%Y-%m-%d'), moodle_page_url))
    conn.commit()
    conn.close()

def login():
    driver.get(login_page)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys(password)
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="loginbtn"]')))).perform()
              
def main():
    login()
    time.sleep(3)
    
    for i in range(4917,5200):
        recepient = base_url + str(i)
        driver.get(recepient)
        time.sleep(2)
        
        try:
            error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-danger')))
            if error: continue
        except:
            pass
        
        check_and_send_message(recepient)
        
        

    os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
    print("All the messages on this website are sent, and the IDs of the recepients have been stored in the local database!!! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    
    # Close the only tab, will also close the browser.
    driver.close()
    driver.quit()
main()