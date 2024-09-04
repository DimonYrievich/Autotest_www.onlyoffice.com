
import os
import csv
import unittest
from Script import script


class TestScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Удаляем файл "test_script.csv", если он существует, чтобы начать тестирование с "0"
        if os.path.exists("test_script.csv"):
            os.remove("test_script.csv")
        # Задаем путь к выходному файлу для тестов
        cls.output_file = "/Users/dimon/PycharmProjects/PROJECTS/Тестовые_задания/Autotest_www.onlyoffice.com/test_script.csv"

    # Проверяем, что скрипт выполняется:
    def test_script_execution(self):
        script(self.output_file)                # Запускаем основной скрипт

        self.assertTrue(os.path.exists(self.output_file), "Файл с результатами не был создан.") # Проверяем, что файл создан

        with open(self.output_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)
            self.assertGreater(len(rows), 1, "Файл с результатами пустой.")              # Проверяем, что файл не пустой
            self.assertEqual(rows[0], ["Country", "CompanyName", "FullAddress"], "Заголовки файла не соответствуют ожидаемым.")

    # Проверяем корректность данных, записанных в файл:
    def test_data_content(self):
        script(self.output_file)

        with open(self.output_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)[1:]       # Пропускаем заголовок, т.к. его уже проверили

            for row in rows:
                country, company_name, full_address = row

                # Проверка на наличие данных в Country
                self.assertTrue(country, "Поле Country не должно быть пустым.")

                # Проверка на наличие данных в CompanyName
                self.assertTrue(company_name, "Поле CompanyName не должно быть пустым.")
                if company_name == "Название компании не найдено":
                    self.assertEqual(company_name, "Название компании не найдено", "Некорректное значение в поле CompanyName.")

                # Проверка на наличие данных в FullAddress
                self.assertTrue(full_address, "Поле FullAddress не должно быть пустым.")

    # Проверяем на отсутствие названия компании:
    def test_handling_missing_company_name(self):
        script(self.output_file)

        with open(self.output_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)[1:]  # Пропускаем заголовок

            for row in rows:
                company_name = row[1]
                if not company_name:
                    self.assertEqual(company_name, "Название компании не найдено", "Программа не обработала корректно отсутствие названия компании.")


if __name__ == "__main__":
    unittest.main()