from os import environ
from dotenvy import load_env, read_file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_firefox_and_navigate(url):
    # Create a Firefox WebDriver instance
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--start-maximized')  # Maximize the browser window on start (optional)
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the specified URL
    driver.get(url)

    return driver


def login(driver, hot_ultra_login, hot_ultra_pass):
    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/button[2]"))
        )

        # Click the element to open the new window
        element.click()

        # Switch to the new window
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        # Wait for the login and password fields to be visible and ready to accept input
        username_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="username_or_email"]'))
        )
        password_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )

        # Enter the username and password
        username_input.send_keys(hot_ultra_login)
        password_input.send_keys(hot_ultra_pass)

        # Locate and click the login button
        login_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]'))
        )
        login_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")


def tweet(driver, tweet_message):
    try:
        # Switch to the post.tech window
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(1))
        driver.switch_to.window(driver.window_handles[0])

        # Locate create new tweet
        tweet_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id=":r8:"]'))
        )
        # Enter message
        tweet_input.send_keys(tweet_message)

        # Locate and click send button
        send_tweet_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/main/form/label/div/div[2]/div[2]/button'))
        )
        send_tweet_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")

    # You can add further actions or interactions with the webpage here.
    time.sleep(10000)
    # Close the browser when done
    driver.quit()


# Example usage:
if __name__ == "__main__":
    load_env(read_file('.env'))
    hot_ultra_login = environ.get("hot_ultra_login")
    hot_ultra_pass = environ.get("hot_ultra_pass")

    target_url = 'https://post.tech/'

    tweet_message = 'Hello, world!'
    driver = open_firefox_and_navigate(target_url)

    login(driver, hot_ultra_login, hot_ultra_pass)
    tweet(driver, tweet_message)
