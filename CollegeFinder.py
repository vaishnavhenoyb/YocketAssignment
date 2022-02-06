from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

cap = {'binary_location': r"C:\Users\Vaishnav\Downloads\chromedriver_win32\chromedriver"}
driver = webdriver.Chrome(desired_capabilities=cap,
                          executable_path=r"C:\Users\Vaishnav\Downloads\chromedriver_win32\chromedriver")
action = ActionChains(driver)

# maximize the window size
driver.maximize_window()

url = "https://yocket.com/"

# navigate to the url
driver.get(url)

# Click on the College Finder
collegeFinder = driver.find_element_by_xpath('//*[@id="college-finder"]')
collegeFinder.click()
time.sleep(1)

# Click on the Masters
mastersButton = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/a[2]/button')
mastersButton.click()
time.sleep(7)

##After 7 seconds, the Yocket Assistant Chat window will popup automatically. We need to manually close
# that Window to proceed further

# Where do you want to study ?
countryName = driver.find_element_by_xpath('//*[@id="vs1__combobox"]/div[1]/input')  # Click on the Country field
countryName.click()
time.sleep(1)
countryName.send_keys("United States")  # Enter the Country Name
time.sleep(2)
countryName = driver.find_element_by_xpath('//*[@id="vs1__listbox"]')
countryName.click()
time.sleep(3)

# What are you planning to study?
subjectName = driver.find_element_by_xpath('//*[@id="vs2__combobox"]/div[1]/input')  # Click on the Subject field
subjectName.click()
time.sleep(1)
subjectName = driver.find_element_by_xpath('//*[@id="vs2__combobox"]/div[1]/input')
subjectName.click()
subjectName.send_keys("Computer Science")  # Type the Subject name
time.sleep(2)
subjectName.send_keys(Keys.ENTER)  # Click on the Subject
time.sleep(2)

# Click on Next
activeOption = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div/span/form/div[2]/div[2]/button')
activeOption.click()
time.sleep(2)

# TELL US ALL ABOUT YOUR UNDERGRAD
# What was your undergraduate college name?
undergraduateCollegeName = driver.find_element_by_xpath('//input[@placeholder = "Select College"]')
undergraduateCollegeName.click()
time.sleep(1)
undergraduateCollegeName.send_keys("Sahyadri College Of Engineering and Management")
time.sleep(2)
undergraduateCollegeName.send_keys(Keys.ENTER)
time.sleep(2)

# Which course did you major in?
courseMajor = driver.find_element_by_xpath('//input[@placeholder = "Select Major"]')
courseMajor.click()
time.sleep(1)
courseMajor.send_keys("Computer Science")
time.sleep(2)
courseMajor.send_keys(Keys.ENTER)
time.sleep(2)

# What is your score/expected score?
scoreDetails = driver.find_element_by_xpath('//*[@id="marks"]')
scoreDetails.click()
time.sleep(1)
scoreDetails.send_keys("6.82")
time.sleep(2)

# Click on Next
loginButton = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div/span/form/div[2]/div[2]/button')
loginButton.click()

# Which English test did you take?
englishTest = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div/div/span/form/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div')
englishTest.click()
englishScore = driver.find_element_by_xpath('//*[@id="toefl_overall_score"]')
englishScore.click()
time.sleep(1)
englishScore.send_keys("116")

# Which aptitude test did you take?
aptitudeTest = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div/div/span/form/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div')
aptitudeTest.click()
aptitudeScore = driver.find_element_by_xpath('//*[@id="total_gmat_score"]')
aptitudeScore.click()
time.sleep(1)
aptitudeScore.send_keys("780")

# Click on Next
loginButton = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div/span/form/div[2]/div[2]/button')
loginButton.click()

# How much relevant work experience do you have?
workExperience = driver.find_element_by_xpath('//*[@id="work_exp"]')
workExperience.click()
time.sleep(1)
workExperience.send_keys("43")

# Have you published any relevant research papers?
researchPapers = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div/div/span/form/div[1]/div[2]/div[2]/div/div[1]/div/div')
researchPapers.click()
time.sleep(1)

# How many relevant projects have you done?
projects = driver.find_element_by_xpath('//*[@id="project"]')
projects.click()
time.sleep(1)
projects.send_keys("4")

# Click on Next
loginButton = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div/span/form/div[2]/div[2]/button')
loginButton.click()
