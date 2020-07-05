import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class CoinLangSwitch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_switching(self):
        driver = self.driver
        driver.get("https://coinmarketcap.com")

        def get_langbar():
            lang_trigger = driver.find_element_by_class_name(
                'cmc-popover__trigger')
            current_lang = lang_trigger.text
            lang_trigger.click()

            lang_dropdown = driver.find_element_by_class_name(
                'cmc-popover__dropdown')

            langs = lang_dropdown.find_elements_by_class_name(
                'cmc-language-picker__option')

            return current_lang, langs

        current_lang, langs = get_langbar()
        iterations = len(langs)
        iterations = 3 #for short test, comment the string for full test
        counter = 0
        succ_switches = 0

        while counter < iterations:
            next_lang = langs[counter]
            next_lang_name = next_lang.text
            next_lang_link = next_lang.get_attribute('href')
            link_lang = next_lang_link.split('/')[-2] #lang abbr in link
            if link_lang == 'coinmarketcap.com':
                link_lang = 'en' #wish it was more elegant)

            next_lang.click()
            print('switching lang to', next_lang_name, 'with', link_lang, 'link')
            counter+=1
            current_lang, langs = get_langbar()
            # is lang switched?
            print ('lang after switching:', current_lang)
            print ('lang assumed to be switched', link_lang)
            same =  current_lang.lower().strip()==link_lang
            print ('Are they the same (case-insensitive?', same)
            if same: succ_switches+=1
        print ('==Total==')
        print (succ_switches, 'successfull switches of', iterations)
  

    def tearDown(self):
        pass
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
