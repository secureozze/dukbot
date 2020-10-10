from selenium import webdriver
import db_functions as db


def get_schedule(input_month):
    chromedriver = "C:/Users/home/Desktop/ChatBot_수업/telegram_flask/chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(
        "options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    driver = webdriver.Chrome(chromedriver, options=options)

    new_url = "https://twice.jype.com/schedule.asp?od={}/1/2019".format(input_month)
    driver.get(new_url)
    schedule_list = driver.find_element_by_id("sche-list")

    result = ""
    if schedule_list.text:
        result = schedule_list.text

    driver.quit()

    return result



if __name__ =="__main__":

    text = get_schedule(1)