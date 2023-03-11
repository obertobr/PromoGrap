import time
from selenium import webdriver

web = webdriver.Chrome(r"/chromedriver.exe")
web.get("https://campaign.aliexpress.com/wow/gcp/sd-g-2022/index?spm=a2g0o.home.01002.4.31c81c913GLz9u")

#web.find_element("xpath", "/html/body/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div/div/div[2]/div").click()

time.sleep(1)

web.refresh()

for i in range(3):
    time.sleep(1)
    web.find_element("xpath", "/html/body").send_keys(webdriver.Keys.PAGE_DOWN)
    #web.execute_script("window.scrollTo(0, document.body.scrollHeight);")

textos = web.find_elements("xpath", "//*[starts-with(@id, '3307188110')]/div/div/div[*]/div/div[2]/div[1]")
precos = web.find_elements("xpath", "//*[starts-with(@id, '3307188110')]/div/div/div[*]/div/div[2]/div[3]/span[1]")


for i in range(1,len(textos)):
    texto = textos[i].get_attribute("innerHTML")
    preco = precos[i-1].get_attribute("innerHTML")
    if(texto[:1] == "<"):
        texto = texto.split(">")[1]
    print("Preço: ", preco, " nome:", texto)

input()