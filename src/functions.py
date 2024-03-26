import json
# Функция должна представлять собой загрузку файла .json


def load_json_file():
    with open("product.json", "rt", encoding="utf-8") as file_operation:
        return json.loads(file_operation.read())
