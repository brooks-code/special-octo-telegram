# A script to test Selenium in headless mode

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

options = Options()
#options.add_argument("--headless")
driver = Firefox(options=options)

print("Firefox headless browser invoked.")
driver.get('https://www.deepl.com/en/translator')

# Print the first 300 characters of the page above.
print(driver.page_source[:300])

driver.quit()
