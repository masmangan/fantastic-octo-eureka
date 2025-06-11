from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from login import test_login

def time_at_work(noteIn, noteOut):
    driver = test_login("Admin", "admin123")
    
    driver.find_element(By.CSS_SELECTOR, ".oxd-icon-button.oxd-icon-button--solid-main.orangehrm-attendance-card-action").click()
    time.sleep(5)

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical'))
    )
    textarea_field.clear()
    textarea_field.send_keys(noteIn)

    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time in recorded successfully.")
    time.sleep(10)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-icon.bi-clock.oxd-time-input--clock'))).click()

    for i in range(3):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.oxd-icon.bi-chevron-down.oxd-icon-button__icon.oxd-time-hour-input-down'))
        ).click()

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical'))
    )
    textarea_field.clear()
    textarea_field.send_keys(noteOut)

    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time out recorded successfully.")

    time.sleep(10)

    return driver

if __name__ == "__main__":
    driver = None
    try:
        driver = time_at_work("Start of work", "End of work")
        print("Time at work test passed.")
    except TimeoutException:
        print("Time at work test failed: Timeout while waiting for elements.")
    except NoSuchElementException as e:
        print(f"Time at work test failed: Element not found - {e}")
    finally:
        if driver:
            driver.quit()
