from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#[CODE 1]
def Goobne_store(result):
    wd = webdriver.Chrome('./WebDriver/chromedriver')
    for i in range(-1,1129):
        wd.get("https://www.goobne.co.kr/store/search_store.asp")
        time.sleep(1)
        try:
            wd.execute_script("chgSido('선택')")
            wd.execute_script("goSearch('N')")
            time.sleep(1)
            GNhtml = wd.page_source
            soupGN = BeautifulSoup(GNhtml, 'html.parser')

            store_GN = soupGN.find_all('div', attrs={'class':'desc'})
            store_GN = store_GN[5:]
            # print(store_GN[i])
            store_name_dl = store_GN[i].select("dl>dt.name")
            store_name = store_name_dl[0].string
            print(store_name)
            store_address_list = store_GN[i].select("dl>dd.local")
            store_address = store_address_list[0].string
            # print(store_address)
            store_phone_list = store_GN[i].select("dl>dd.num")
            store_phone = store_phone_list[0].string
            # print(store_phone)
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
        # print(len(store_GN))
    return

def main():
    result = []
    print('Goobne sotre crawling>>>>>>>>>>')
    Goobne_store(result)
    GN_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    GN_tbl.to_csv('./Goobne.csv', encoding = 'utf-8', mode = 'w', index = True)


if __name__ == '__main__':
    main()