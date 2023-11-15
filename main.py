import csv
import re
import os
from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
    "height": "^\\d\\.\\d{2}$",
    "snils": "^\\d{11}$",
    "passport": "^\\d{2}\\s\\d{2}\\s\\d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\\s-]+$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",
    "issn": "^\\d{4}-\\d{4}$",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "time": "^([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d)\\.(\\d{1,6})$"
}


def is_valid_row(row: list[str]) -> bool:
    """
    метод который проверяет соответствует ли каждое значение в строке
    шаблону в PATTERNS.
    :param row: list[str]
    :return: bool
    """
    flag = True
    for key, value in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[key], value):
            flag = False
            return flag
    return flag


def get_invalid_rows(path_to_csv_file: str) -> list[int]:
    """
    метод который возвращает список индексов строк CSV-файла, не соответствующих ожидаемым шаблонам.
    :param path_to_csv_file: str
    :return: list[int]
    """
    index_list = []
    data = []
    with open(path_to_csv_file, "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    for i, row in enumerate(data):
        if not is_valid_row(row):
            index_list.append(i)
    return index_list

if __name__ == "__main__":
    path_to_csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "59.csv")
    invalid_rows = get_invalid_rows(path_to_csv_file)
    serialize_result(59, calculate_checksum(invalid_rows))