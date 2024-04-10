import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import subprocess
import time
#*MyFunc
import immobiliare, trovacasa


subprocess.call("cls", shell=True)

luogo = input("insersci comune o zona: ")

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #_options = Options()
        #_options.add_argument("--headless")
        #self.driver = webdriver.Firefox(options=_options)
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        immobiliare.Ricerca(driver, By, luogo, True)
        trovacasa.Ricerca(driver, By, luogo, True)
        


    def tearDown(self):
        self.driver.close()
        subprocess.call("start notepad reportIMMOBILIARE.txt", shell=True)
        subprocess.call("start notepad reportTROVACASA.txt", shell=True)
        

if __name__ == "__main__":
    unittest.main()