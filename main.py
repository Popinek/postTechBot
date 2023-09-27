from os import environ
from dotenvy import load_env, read_file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from gpt import *


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


def tweet_posttech(driver, tweet_message, num_tweets=2):
    try:

        # Switch to the post.tech window
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(1))
        driver.switch_to.window(driver.window_handles[0])

        # Create X number of tweets
        for _ in range(num_tweets):

            # Locate create new tweet
            tweet_input = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="What\'s happening?"]'))
            )
            # Enter message
            tweet_input.send_keys(tweet_message)

            # Locate and click send button
            send_tweet_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.custom-button[type="submit"]'))
            )
            send_tweet_button.click()

            print("You tweeted:", tweet_message)

            # Go back to the home page to create next tweet
            driver.get("https://post.tech/home")

            # Wait to load web page
            time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    # You can add further actions or interactions with the webpage here.
    time.sleep(10000)
    # Close the browser when done
    driver.quit()


def reply_posttech(driver, reply_message, num_messages=2):
    try:

        # Switch to the post.tech window
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(1))
        driver.switch_to.window(driver.window_handles[0])
        # Go to Homepage
        WebDriverWait(driver, 60).until(EC.url_to_be("https://post.tech/home"))

        # Find and reply to the first 'num_messages' messages
        for _ in range(num_messages):

            # Locate the element by class name
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.whitespace-pre-line.break-words'))
                 )

            # Read the tweet
            read_tweet = element.text
            print("Message:", read_tweet)

            # Reply to the tweet

            # Locate and click message button
            locate_message_button = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/article/div/span/div/div[2]/div[2]/div/button[1]'))
            )
            locate_message_button.click()

            # Locate reply window
            locate_reply_window = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Post your reply"]'))
            )

            # Enter the reply message
            locate_reply_window.send_keys(reply_message)

            # Locate and click submit button
            send_reply_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/form/label/div/div[2]/div[2]/button'))
            )
            send_reply_button.click()
            print("Message:", reply_message)

            # Go back to the home page to reply to the next message
            driver.get("https://post.tech/home")

            # Wait to load web page
            time.sleep(10)

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
    #openai_api_key = environ.get("gpt")

    target_url = 'https://post.tech/'

    #tweet_message = gptTweet(openai_api_key)
    tweet_message = "Hey"
    reply_message = "I agree"
    driver = open_firefox_and_navigate(target_url)

    login(driver, hot_ultra_login, hot_ultra_pass)
    #reply_posttech(driver, reply_message)
    tweet_posttech(driver, tweet_message)
