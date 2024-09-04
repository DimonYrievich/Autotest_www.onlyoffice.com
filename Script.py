
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import csv
import time


def script(path_to_output_file):
    webdriver_path = "/Users/dimon/PycharmProjects/PROJECTS/Тестовые_задания/Autotest_www.onlyoffice.com/geckodriver.exe"
    service = Service(executable_path = webdriver_path)     # Настройка сервиса (создаем объект Service для GeckoDriver)
    driver = webdriver.Firefox(service=service)             # Инициализация веб-драйвера

    try:
        # 1. Запуск браузера и переход на страницу www.onlyoffice.com
        driver.get("https://www.onlyoffice.com")
        time.sleep(3)

        # 2. Переход по ссылке в шапке About -> Contacts
        driver.get("https://www.onlyoffice.com/contacts.aspx")
        time.sleep(3)

        # 3. Парсинг данных об офисах
        offices = driver.find_elements(By.CLASS_NAME, "companydata")
        office_data = []
        # Ищем нужные элементы и добавляем их в список office_data
        for office in offices:
            country = office.find_element(By.CLASS_NAME, "region").text.strip()
            # company_name = office.find_element(By.CSS_SELECTOR, "span > b").text.strip()               # Не находит!!!
            # company_name = office.find_element(By.XPATH, ".//span/b").text.strip()                     # Не находит!!!
            try:
                company_name = office.find_element(By.XPATH, ".//span/b").text.strip()
            except Exception:
                company_name = "Имя компании не найдено"

            full_address_elements = office.find_elements(By.XPATH, ".//span[@itemprop='streetAddress'] | "
                                                                   ".//span[@itemprop='addressCountry'] | "
                                                                   ".//span[@itemprop='postalCode'] | "
                                                                   ".//span[@itemprop='telephone']")
            full_address = []
            for element in full_address_elements:
                text = element.text.strip()
                if text:
                    full_address.append(text)
            full_address = " ".join(full_address)
            office_data.append([country, company_name, full_address])

        # 4. Запись данных в CSV файл
        with open(path_to_output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Country", "CompanyName", "FullAddress"])
            writer.writerows(office_data)

        print(f"Данные сохранены в {path_to_output_file}")

    finally:
        # Закрытие браузера
        driver.quit()


# Вызов функции с указанием пути к выходному файлу
path_to_output_file = "/Users/dimon/PycharmProjects/PROJECTS/Тестовые_задания/Autotest_www.onlyoffice.com/output_file.csv"
script(path_to_output_file)

# Вызов функции с прямым указанием выходного файла
# script("output_file.csv")