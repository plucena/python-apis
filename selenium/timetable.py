from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

#setup
#url = "https://ibm.biz/HRJustificativaHoras"
url= "https://docs.google.com/forms/d/1bnbH5z-qV_LCsg5I_mdkd1T5kK0L3UF5T3MFbwXaCYs/viewform?edit_requested=true#"
today = datetime.datetime.now()
str_today = str(today.day).zfill(2) + "/" + str(today.month).zfill(2) + "/" + str(today.year)
start_hour  = "09:00"
number_hours = "9"


def submit_hours(user, password):
	if(today.weekday()<6):
		driver = webdriver.Chrome()
		driver.get(url)
		element = driver.find_element_by_id("entry_444885743")
		element.send_keys(str_today)
		element = driver.find_element_by_id("entry_645594624")
		element.send_keys(start_hour)
		element = driver.find_element_by_id("entry_235408508")
		element.send_keys(number_hours)
		elem = driver.find_element_by_id("ss-submit")
		elem.send_keys(Keys.RETURN)
		driver.close()
		print("Enviado")

# loop to read from database
submit_hours("plucena@br.ibm,com", "")