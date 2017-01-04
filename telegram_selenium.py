from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
import time


def main():
    binary_path = '/usr/local/Caskroom/firefox/46.0.1/Firefox.app/Contents/MacOS/firefox'
    profile_path = '/Users/sardor/Library/Application Support/Firefox/Profiles/ipwnti5p.default'
    profile = webdriver.FirefoxProfile(profile_path)
    binary = FirefoxBinary(binary_path)
    driver = webdriver.Firefox(firefox_binary=binary)
    # driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)
    driver.get('https://web.telegram.org')
    time.sleep(5)
    phone_number_input = driver.find_element_by_name('phone_number')
    phone_number_from_twilio = '3751237654'
    phone_number_input.clear()
    phone_number_input.send_keys(phone_number_from_twilio)
    phone_number_input.send_keys(Keys.RETURN)
    time.sleep(2)
    modal_window_ok_button = driver.find_element_by_css_selector("button[ng-switch='type']").click()
    print(modal_window_ok_button)
    driver.quit()


if __name__ == '__main__':
    main()
