from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # after importing this keyboard keys to perform task

driver_path = r"C:\Users\mrspm\PycharmProjects\Wiki_mainPageScrapping_Selenium\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count_data = driver.find_element_by_css_selector("#articlecount a")
# count_data.click()
all_portals = driver.find_element_by_link_text("All portals")  # finding throuhgh link text on website page
search = driver.find_element_by_name("search")
search.send_keys("Python") ### writing anything after holding the point where you want to write
search.send_keys(Keys.ENTER) # similar to clicking Enter on keyboard.










