from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

try:
    for page_number in range(1, 6):  # Scraping from the next 5 pages
        # Open the website for the current page
        driver.get(f"https://scrapeme.live/shop/page/{page_number}/")

        # Find individual product elements
        product_items = driver.find_elements(By.CSS_SELECTOR, 'ul.products li')

        # Print the product names for the current page
        print(f"Page {page_number}:")
        for item in product_items:
            product_name = item.find_element(By.CSS_SELECTOR, 'h2').text
            print(product_name)

finally:
    driver.quit()
