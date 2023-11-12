import csv
import json
# TODO импортировать необходимые молули

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    result = []
    with open(INPUT_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
    ...  # TODO считать содержимое csv файла

    json_data = json.dumps(result, indent=4)
    print(json_data)
    ...  # TODO Сериализовать в файл с отступами равными 4

    # with open(OUTPUT_FILENAME, 'w') as json_file:
    #     json.dump(result, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()
    #
    # with open(OUTPUT_FILENAME) as output_f:
    #     for line in output_f:
    #         print(line, end="")



