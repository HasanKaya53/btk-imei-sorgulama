from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from selenium.webdriver.common.by import By



imeiNumarasi = "imei no"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(executable_path = r'drivers/paonetdriverC.exe', options=chrome_options)
driver.get("https://www.turkiye.gov.tr/imei-sorgulama")


driver.find_element("xpath","/html/body/main/div/section/section[2]/form/fieldset/div/input").send_keys(imeiNumarasi)
driver.find_element("xpath","/html/body/main/div/section/section[2]/form/div/input[1]").click()
imeiNo = driver.find_element("xpath","/html/body/main/div/section/section[2]/div[1]/dl/dd[1]").text
Durum = driver.find_element("xpath","/html/body/main/div/section/section[2]/div[1]/dl/dd[2]").text
Kaynak = driver.find_element("xpath","/html/body/main/div/section/section[2]/div[1]/dl/dd[3]").text
SorguTarihi = driver.find_element("xpath","/html/body/main/div/section/section[2]/div[1]/dl/dd[4]").text
markaModel = driver.find_element("xpath","/html/body/main/div/section/section[2]/div[1]/dl/dd[5]").text

markaModelSplit = markaModel.split(",")



print("Tum Marka Model:"+markaModel)


datas = {"Marka":"","Model":"","IMEI":"","Durum":"","Kaynak":"","SorguTarihi":""}
for x in markaModelSplit:
    

uretici = markaModelSplit[0].split(":")[1]
pazarAdi = markaModelSplit[1].split(":")[1]
marka = markaModelSplit[2].split(":")[1]
modelBilgileri = markaModelSplit[3].split(":")[1]

print(modelBilgileri)





#866334046109316





