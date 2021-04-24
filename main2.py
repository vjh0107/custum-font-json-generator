import json


if __name__ == '__main__':
    index = "00ef"
    amount = 20

    for i in range(amount):
        print(f"  - setname{{name={chr(int(index, 16)+i)}; delay=0}} @self ~onSpawn")
