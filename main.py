import json


def write_json(type: str, file_dir: str, ascent: int, height: int, chars: str):
    with open('result.json', 'w', encoding='utf-8') as make_file:
        custom_font = dict()
        custom_font["type"] = type
        custom_font["file"] = file_dir
        custom_font["ascent"] = ascent
        custom_font["height"] = height
        custom_font["chars"] = chars
        json_data = custom_font

        json.dump(json_data, make_file, indent="\t", ensure_ascii=False)
    with open('result.json', 'r') as f:
        json_data = json.load(f)

    print(json.dumps(json_data, indent="\t"))


if __name__ == '__main__':
    index = 30000
    amount = 20

    c = "{}".format(hex(index))[2:]

    for i in range(amount):
        c = "{}".format(hex(index+i))[2:]
        unicode = rf"\u{c}"
        print(unicode)
        write_json("bitmap", "skill:font/assassin/blasting/1.png", 41, 160, unicode)