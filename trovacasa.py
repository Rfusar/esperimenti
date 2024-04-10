import time
def Ricerca(driver, By, luogo, primapagina=None):
    if primapagina:
        driver.get("https://www.trovacasa.it/")
        time.sleep(1)

        try: 
            cookie = driver.find_element(By.XPATH, '/html/div/div/button')
            cookie.click()
        except:...

        #*Luogo
        search_text = driver.find_element(By.XPATH, '//*[@id="TestoRicercaLuogo"]')
        search_text.send_keys(luogo)

        #*Superficie
        superficie = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/div[3]/div[2]')
        superficie.click()
        time.sleep(1)
        searchSuperficie = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/div[3]/div[2]/div/span/input')
        searchSuperficie.send_keys("110")

        #*Locali
        locali = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/div[3]/div[3]')
        locali.click()
        time.sleep(1)
        searchLocali = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/div[3]/div[3]/div/div[1]/div[2]/div/div/div/div[5]/input')
        searchLocali.click()
        time.sleep(1)

        btn_search = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/div[2]/div[4]')
        btn_search.click()
        time.sleep(2)

    dati = []
    containers = driver.find_elements(By.CLASS_NAME, 'card__elementsContainer')
    for c in containers:
        dato = {}
        link = c.find_element(By.TAG_NAME, 'a')
        dato['href'] = link.get_attribute('href')
        dato['luogo'] = link.text

        description = c.find_element(By.TAG_NAME, 'p')
        dato['descrizione'] = description.text

        dettagli = c.find_elements(By.CLASS_NAME, 'card__infoContainer')
        for d in dettagli:
            prezzo = d.find_element(By.CLASS_NAME, 'card__price')
            dato['prezzo'] = prezzo.text
            dettagli0 = d.find_elements(By.CLASS_NAME, 'card__info')
            dato['dettagli'] = {}
            for i, d0 in enumerate(dettagli0):
                dato['dettagli'][f'A_dettaglio{i}'] = d0.text

        dettagli1 = c.find_elements(By.CLASS_NAME, 'card__tagContainer')
        for d1 in dettagli1:
            dettagli2 = d1.find_elements(By.CLASS_NAME, 'annuncioTag')
            for i, d2 in enumerate(dettagli2):
                dato['dettagli'][f'B_dettaglio{i}'] = d2.text

        dati.append(dato)

    print("Ho iniziato a scrivere...TROVACASA")
    with open("reportTROVACASA.txt", "a+", encoding="utf-8") as f:
        for d in dati:
            f.write(f"luogo ---> {d['luogo']}\n")
            f.write(f"prezzo ---> {d['prezzo']}\n")
            f.write(f"link ---> {d['href']}\n")
            for v in d['dettagli'].values():
                f.write(f"\tdettaglio ---> {v}\n")
            f.write(f"descrizione ---> {d['descrizione']}\n")
            f.write("\n\n")

    time.sleep(2)
    def nextPage():
        try:
            btn = driver.find_element(By.CSS_SELECTOR, '.pager__link.big.next')
            if btn:
                btn.click()
                Ricerca(driver, By, luogo)
            else: return
        except: return

    nextPage()