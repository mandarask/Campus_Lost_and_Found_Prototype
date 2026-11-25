from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open Campus Lost and Found website
    driver.get(
        "http://127.0.0.1:5500/Campus_Lost_and_Found_Prototype/index.html"
    )

    # Fill the report form with test data
    Select(driver.find_element(By.ID, "type")).select_by_visible_text("Lost")

    driver.find_element(By.ID, "name").send_keys("Selenium Test Wallet")

    driver.find_element(By.ID, "location").send_keys("Central Library")

    driver.find_element(By.ID, "description").send_keys(
        "Black leather wallet used for Selenium testing"
    )

    driver.find_element(By.ID, "contact").send_keys(
        "test@college.edu"
    )

    # Submit the report
    driver.find_element(
        By.CSS_SELECTOR, "#itemForm button[type='submit']"
    ).click()

    print("Test item submitted successfully")

    # Search for the submitted item
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "searchInput"))
    )

    search_box.send_keys("Selenium Test Wallet")

    driver.find_element(By.ID, "searchButton").click()

    # Check search result
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "results"),
            "Selenium Test Wallet"
        )
    )

    print("PASS: Matching item found successfully")

    input("Press Enter to close the browser...")

finally:
    driver.quit()