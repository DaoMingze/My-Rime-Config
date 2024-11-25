a = {
    "X4": {
        "command": "",
        "commit": "",
        "functional": "",
        "label": "四字",
        "name": "X4",
        "option": "",
        "preview": "",
        "repeatable": "",
        "select": "",
        "send": "",
        "shift_lock": "",
        "states": "",
        "text": "{Home}{Right}{Right}{Right}{Right}}{Right}{Right}{Right}{Right}",
        "toggle": "",
        "分类": "编辑",
        "注释": "",
    }
}

for k, v in a.items():
    # print(type(v))
    new_value = {}
    for _key, _value in v.items():
        if _key != "name" and _value != "":
            new_value[_key] = _value
    a[k] = new_value

print(a)
