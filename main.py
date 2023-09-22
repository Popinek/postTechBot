from selenium import webdriver
import time

def open_firefox_and_navigate(url, driver_path):
    # Create a Firefox WebDriver instance
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--start-maximized')  # Maximize the browser window on start (optional)
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the specified URL
    driver.get(url)

    # You can add further actions or interactions with the webpage here.
    time.sleep(1000)
    # Close the browser when done
    driver.quit()

# Example usage:
if __name__ == "__main__":
    target_url = 'https://post.tech/'
    driver_path = r'C:\Users\lukas\Desktop\python\geckodriver.exe'  # Replace with the actual path to the GeckoDriver executable
    open_firefox_and_navigate(target_url, driver_path)
