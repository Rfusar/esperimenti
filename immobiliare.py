import time

def Ricerca(driver, By, luogo, primaPagina=None):
    if primaPagina:
        driver.get("https://www.immobiliare.it/")
        time.sleep(4)
        try: 
            cookie0 = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div[2]/svg')
            cookie0.click()
        except:...
        #*cookie
        cookie1 = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')  
        cookie1.click()  
            
        #*Luogo
        search_luogo = driver.find_element(By.XPATH, '//*[@id="sale"]/div[1]/nd-geography-search/input[1]')
        search_luogo.send_keys(luogo)
        time.sleep(3)
    
        parent_element = driver.find_element(By.CLASS_NAME, 'nd-autocomplete__list.is-open')
        parent_element.click()
        cerca = driver.find_element(By.XPATH, '//*[@id="sale"]/div[4]/button')
        cerca.click()
        time.sleep(1)
        try: 
            cookie2 = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div[2]/svg')
            cookie2.click()
        except:...
        try:
            cookie3 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/button')
            cookie3.click()
        except:...

        #*Filtri
        btn_filtri = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/button')
        btn_filtri.click()
        time.sleep(1)
        btn_superficie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[3]/div/div')
        btn_superficie.click()
        time.sleep(1)

        metriQuadrati = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[3]/div/div[2]/div[1]/input[1]')
        metriQuadrati.send_keys('110')
        time.sleep(1)

        pulisci0 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[4]')
        pulisci0.click()
        time.sleep(1)

        btn_locali = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[4]/div/div[1]')
        btn_locali.click()
        time.sleep(1)

        locali = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[4]/div/div[2]/div[1]/input[1]')
        locali.send_keys("4")
        time.sleep(1)

        pulisci0.click()
        time.sleep(1)

        btn_invia = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/button[2]')
        btn_invia.click()
        time.sleep(1)

    
    prezzi = driver.find_elements(By.CLASS_NAME, "in-reListCardPrice")
    links = driver.find_elements(By.CLASS_NAME, "in-reListCard__title")
    dettagli = driver.find_elements(By.CLASS_NAME, "in-reListCardFeatureList")

    dati = []
    for i, p in enumerate(prezzi):
        dato = {}
        span = p.find_element(By.TAG_NAME, 'span')
        dato["prezzo"] = span.text
        dati.append(dato)

    for i, l in enumerate(links):
        href = l.get_attribute('href')
        luogo = l.text
        dati[i]["href"] = href
        dati[i]["luogo"] = luogo

    for i, d in enumerate(dettagli):
        dati[i]['dettagli'] = {}
        divs = d.find_elements(By.CLASS_NAME, 'in-reListCardFeatureList__item')
        for k, d0 in enumerate(divs):
            span = d0.find_element(By.TAG_NAME, 'span')
            dati[i]['dettagli'][f'dettaglio{k}'] = span.text

    
    print("Ho iniziato a scrivere...IMMOBILIARE")
    with open("reportIMMOBILIARE.txt", "a+", encoding="utf-8")as f: 
        for d in dati:
            f.write(f"luogo ---> {d['luogo']}\n")
            f.write(f"prezzo ---> {d['prezzo']}\n")
            f.write(f"link ---> {d['href']}\n")
            for k, v in d['dettagli'].items():
                f.write(f"\t{k} ---> {v}\n")
            f.write("\n\n")

    time.sleep(2)
    def nextPage():
        try:
            btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/div/div[3]/div[3]/a[1]')
            if btn:
                btn.click()
                Ricerca(driver, By, luogo)
            else: return
        except: return

    nextPage()