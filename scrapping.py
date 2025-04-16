from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Path chromedriver
chrome_driver_path = r"C:\Users\lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Setup WebDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)


def scrape_trustpilot_reviews(base_url, start_page=1, end_page=3, output_file="aardy_reviews_clean.csv"):
    scraped_data = []

    for page in range(start_page, end_page + 1):
        url = f"{base_url}?page={page}"
        print(f"Mengakses: {url}")
        try:
            driver.get(url)
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "styles_reviewContentwrapper__K2aRu"))
            )
            blocks = driver.find_elements(By.CLASS_NAME, "styles_reviewContentwrapper__K2aRu")

            for review in blocks:
                try:
                    title = review.find_element(By.TAG_NAME, "h2").text.strip()
                except:
                    title = ""

                try:
                    content = review.find_element(By.CSS_SELECTOR,
                                                  'p[data-service-review-text-typography="true"]').text.strip()
                except:
                    content = ""

                if title or content:
                    scraped_data.append({
                        "title": title,
                        "content": content
                    })
        except Exception as e:
            print(f"Error saat load halaman {page}: {e}")

        time.sleep(2)

    df = pd.DataFrame(scraped_data)
    df.to_csv(output_file, index=False)
    print(f"Selesai. Data disimpan di '{output_file}'.")


# Run scraper
scrape_trustpilot_reviews("https://www.trustpilot.com/review/aardy.com", start_page=1, end_page=1000) # 1000 pages

# Close browser
driver.quit()
