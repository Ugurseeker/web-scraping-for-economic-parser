

import time
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome tarayıcısını başlatma
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tarayıcı penceresi olmadan çalışmasını sağlar
driver = webdriver.Chrome(options=chrome_options)

# Excel dosyasının adını belirleyin
excel_file = 'financial_data.xlsx'

# Günlük hedef zamanları ayarlayan fonksiyon
def get_daily_target_times():
    today = datetime.now().date()  # Bugünün tarihi
    target_times = [
        datetime.combine(today, datetime.strptime("9:00:00", "%H:%M:%S").time()),
        datetime.combine(today, datetime.strptime("12:00:00", "%H:%M:%S").time()),
        datetime.combine(today, datetime.strptime("15:00:00", "%H:%M:%S").time()),
        datetime.combine(today, datetime.strptime("18:00:00", "%H:%M:%S").time())
    ]
    return target_times

# Veri çekme ve DataFrame oluşturma döngüsü
def run_bot():
    try:
        while True:
            current_time = datetime.now()
            start_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
            end_time = current_time.replace(hour=18, minute=0, second=0, microsecond=0)

            if start_time <= current_time <= end_time:
                target_times = get_daily_target_times()
                # Her gün için hedef zamanlar güncellenir
                #Amaç: Mevcut zamanın çalışma saatleri içinde olup olmadığını kontrol etmek.
                #Eğer çalışma saatleri içindeyse, veri çekme işlemi için belirlenen zamanları almak.

                # Hedef zamana kadar bekleme
                for target_time in target_times:
                    if current_time < target_time:
                        wait_time = (target_time - current_time).total_seconds()
                        hours, remainder = divmod(wait_time, 3600)
                        minutes, _ = divmod(remainder, 60)
                        print(f"{target_time} için bekleniyor, {int(hours)} saat {int(minutes)} dakika uyuma")
                        time.sleep(wait_time)
                        break
#Amaç: Hedef zamanlardan birine kadar beklemek. Her hedef zaman için  mevcut zamanla karşılaştırma yapılır
#ve eğer mevcut zaman bu hedef zamanlardan önceyse, aradaki süre kadar beklenir.

                # Web sayfalarına gidin ve verileri çekin
                try:
                    wait = WebDriverWait(driver, 10)

                    # USD/TRY verisini çek
                    driver.get("https://tr.tradingview.com/symbols/USDTRY/")
                    usdtry = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # GAUTRY verisini çek
                    driver.get("https://tr.tradingview.com/symbols/XAUTRYG/")
                    gautry = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # EUR/TRY verisini çek
                    driver.get("https://tr.tradingview.com/symbols/EURTRY/")
                    eurtry = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # ETH/USD verisini çek
                    driver.get("https://tr.tradingview.com/symbols/ETHUSD/")
                    ethusd = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # BTC/USDT verisini çek
                    driver.get("https://tr.tradingview.com/symbols/BTCUSDT/")
                    btcusdt = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # XAG/TRY verisini çek
                    driver.get("https://tr.tradingview.com/symbols/XAGTRYG/")
                    xagtry = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]/span'))).text

                    # BIST-100 verisini çek
                    driver.get("https://tr.tradingview.com/symbols/BIST-XU100/")
                    bist100 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # UKOIL verisini çek
                    driver.get("https://tr.tradingview.com/symbols/UKOIL/")
                    ukoil = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                         '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # NASDAQ-100 verisini çek
                    driver.get("https://tr.tradingview.com/symbols/NASDAQ-NDX/")
                    nasdaq_ndx = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]'))).text

                    # Türkiye 5 yıl vadeli CDS verisini çek
                    driver.get("https://www.worldgovernmentbonds.com/cds-historical-data/turkey/5-years/")
                    turkey_cds = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//*[@id="post-33"]/div/div[3]/div/div[3]'))).text

                    # Zaman damgasını al
                    timestamp = pd.Timestamp.now()
                    # isteğe bağlı değiştirilebilir.

                    # Yeni veriyi içeren DataFrame oluştur
                    new_data = pd.DataFrame([[timestamp, usdtry, gautry, eurtry, ethusd, btcusdt, xagtry, bist100, ukoil, nasdaq_ndx, turkey_cds]],
                                            columns=['Timestamp', 'USD/TRY', 'GAUTRY', 'EUR/TRY', 'ETH/USD', 'BTC/USDT', 'XAG/TRY', 'BIST-100', 'UKOIL', 'NASDAQ-100', 'Turkey CDS (5Y)'])

                    # Eğer dosya mevcutsa eski verileri oku ve yeni verilerle birleştir
                    try:
                        df = pd.read_excel(excel_file)
                        df = pd.concat([df, new_data], ignore_index=True)
                    except FileNotFoundError:
                        df = new_data

                    # Veriyi Excel dosyasına yazdır
                    df.to_excel(excel_file, index=False)

                    # DataFrame'i ekrana yazdır
                    print("\033c", end="")  # Konsolu temizler
                    print(df)

                except Exception as e:
                    print(f"Bir hata oluştu: {e}")


            else:
                # Çalışma saatleri dışındaysa ertesi güne kadar bekle
                time_until_next_start = (start_time + timedelta(days=1) - current_time).total_seconds()
                hours, remainder = divmod(time_until_next_start, 3600)
                minutes, _ = divmod(remainder, 60)
                print(f"Çalışma saatleri sona erdi. {int(hours)} saat {int(minutes)} dakika uykuya geçiliyor.")
                time.sleep(time_until_next_start)

    finally:
        driver.quit()
        print("Program sona erdi.")

# Botu başlat
run_bot()
