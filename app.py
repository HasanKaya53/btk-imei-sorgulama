from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium


imeiNumarasi = input("Sorgulanacak IMEI Numarası: ")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=%s" % "1920,1080")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.turkiye.gov.tr/imei-sorgulama")


driver.find_element(By.ID, "txtImei").click()
driver.find_element(By.ID, "txtImei").send_keys(imeiNumarasi)
driver.find_element(By.ID, "txtImei").send_keys(Keys.ENTER)
imeiNo = driver.find_element(By.CSS_SELECTOR, "dd:nth-child(2)").text
durum = driver.find_element(By.CSS_SELECTOR, "dd:nth-child(4)").text
kaynak = driver.find_element(By.CSS_SELECTOR, "dd:nth-child(6)").text
sorguTarihi = driver.find_element(By.CSS_SELECTOR, "dd:nth-child(8)").text
markaModel = driver.find_element(By.CSS_SELECTOR, "dd:nth-child(10)").text

markaModelSplit = markaModel.split(",")

for x in markaModelSplit:
    uretici = markaModelSplit[0].split(":")[1]
    pazarAdi = markaModelSplit[1].split(":")[1]
    marka = markaModelSplit[2].split(":")[1]
    model = markaModelSplit[3].split(":")[1]
    

#datas = {"Marka":marka,"Model":model,"IMEI":imeiNo,"Durum":durum,"Kaynak":kaynak,"SorguTarihi":sorguTarihi}

print("Marka: "+marka)
print("Model: "+model)
print("IMEI: "+imeiNo)
print("Durum: "+durum)
print("Kaynak: "+kaynak)
print("Sorgu Tarihi: "+sorguTarihi)