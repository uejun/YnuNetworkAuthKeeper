# -*- coding: utf-8 -*-
import json
import os
import time
from selenium import webdriver


def main():
    print(os.path.abspath(__file__))
    abs_dirpath = os.path.dirname(os.path.abspath(__file__))
    auth_filepath = os.path.join(abs_dirpath, "auth.json")

    try:
        while True:
            # YNUネットワーク認証IDとPasswordを認証jsonファイルより取得
            with open(auth_filepath, 'r') as f:
                auth_data = json.load(f)
                ynu_id = auth_data["id"]
                password = auth_data["password"]

                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs", prefs)

                # Chrome起動
                driver = webdriver.Chrome(chrome_options=chrome_options)
                driver.implicitly_wait(10)
                driver.set_page_load_timeout(30)

                # YNUネットワーク認証
                url = "https://na.ynu.ac.jp/"
                driver.get(url)
                time.sleep(1.5)

                print(driver.current_url)
                if driver.current_url == "https://na.ynu.ac.jp/www/login-success-page.html":
                    driver.close()
                else:
                    driver.find_element_by_name("name").send_keys(ynu_id)
                    driver.find_element_by_name("pass").send_keys(password)
                    time.sleep(1)
                    driver.find_element_by_xpath('//input[@value="login"]').submit()
                    time.sleep(1)

                    # ブラウザを終了
                    driver.close()

            time.sleep(11*60*60)
    except KeyboardInterrupt:
            try:
                driver.close()
            except:
                pass


if __name__ == '__main__':
    main()
