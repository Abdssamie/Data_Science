from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Edge()

driver.get("https://watersgeo.epa.gov/iwtt/guided-search")

title = driver.title

driver.implicitly_wait(0.5)

search_button = driver.find_element(by=By.CSS_SELECTOR,
                                    value="#root > div > div > section > section > div.tw-my-4 > button:nth-child(1)")
search_button.click()


try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ""))
    )
    print("Industries specific queries are visible, proceeding...")
except TimeoutError:
    print("Timeout waiting for the element")


main_table = driver.find_element(by=By.CSS_SELECTOR,
                                 value="#root > div > div > section > section > section > table")

rows = main_table.find_elements(By.TAG_NAME, "tr")

column_index = 4

data = []

for i, row in enumerate(rows):
    cells = row.find_elements(By.TAG_NAME, "td")

    if len(cells) > column_index:
        try:
            target_cell = cells[column_index]

            table_button = target_cell.find_element(by=By.TAG_NAME, value="button")
            table_button.click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ""))
            )
            print("Industries specific query table is visible, proceeding...")

        except TimeoutError:
            print("Timeout waiting for the industry based table")

        except Exception:
            print(f"Button not found in row {i+1} and cell {column_index}")


        try:
            popup_data = driver.find_element(By.CSS_SELECTOR, "[data-id='iwtt-modal-contents']")

            table_to_scrape = popup_data.find_element(By.TAG_NAME, "table")
            table_rows = table_to_scrape.find_elements(By.TAG_NAME, "tr")

            for table_row in table_rows:
                table_cells = table_row.find_elements(By.TAG_NAME, "td")

                data.append([cell.text for cell in table_cells])

        except Exception:
            print('Something went wrong while scraping the table')


df = pd.DataFrame(data)

df.to_csv('out.csv', index=False)
