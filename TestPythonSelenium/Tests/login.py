from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
import time


def test_login(username, password):

  driver = webdriver.Chrome()
  driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
  driver.maximize_window()
  input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]')))
  input_field.clear()
  input_field.send_keys(username)
  input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]')))
  input_field.clear()
  input_field.send_keys(password)
  driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
  time.sleep(20)
  driver.implicitly_wait(20)
  return driver


if __name__ == "__main__":
  try:
    driver = test_login("Admin", "admin123")
    print("Login test passed.")
  except TimeoutException:
    print("Login test failed: Timeout while waiting for elements.")
  except NoSuchElementException as e:
    print(f"Login test failed: Element not found - {e}")
  finally:
    driver.quit()