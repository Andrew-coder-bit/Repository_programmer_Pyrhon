import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total = sum(item['score'] * item['weight'] for item in data) #использование генератора
    return round(total, 3)


print(task())
