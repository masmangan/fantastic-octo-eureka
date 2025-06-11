from login import test_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def mostLiked():
  driver = test_login("Admin", "admin123")
  driver.implicitly_wait(5)
  driver.find_element(By.XPATH, "//a[@href='/web/index.php/buzz/viewBuzz']").click()
 
  time.sleep(5)
  wait = WebDriverWait(driver, 10)
  #Pega os botoes de mais curtido e clicka nele!
  most_liked = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Most Liked Posts')]")))
  most_liked.click()

  time.sleep(3)

  return driver
  

  



if __name__ == "__main__":
  try:
    driver = mostLiked()
    print("View Most Liked Posts test passed.")
    driver.quit()
  except TimeoutException:
    print("Login test failed: Timeout while waiting for elements.")
  except NoSuchElementException as e:
    print(f"Login test failed: Element not found - {e}")
  finally:
    print("Ending Process...")

