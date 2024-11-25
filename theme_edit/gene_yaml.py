import csv
import os
import yaml

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录：{current_dir}")


def gene_keys(src: str, key: str, res_type: str):
    pk_dict = {}
    pk_list = []
    with open(src, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            new_row = {}
            for _k, _v in row.items():
                if _k != key and _k != "分类" and _v != "":
                    new_row[_k] = _v
                    print(_v)
            if res_type == "dict":
                pk_dict[row[key]] = new_row
            elif res_type == "list":
                pk_list.append(new_row)
    if len(pk_dict) <= 0 and len(pk_list) >= 1:
        yaml_date = pk_list
    elif len(pk_dict) >= 1 and len(pk_list) <= 0:
        yaml_date = pk_dict
    else:
        yaml_date = ""
    with open(src.replace("csv", "yaml"), "w", encoding="utf-8") as f:
        f.write(
            yaml.dump(
                yaml_date,
                default_flow_style=True,
                allow_unicode=True,
                width=float("inf"),
            )
        )


gene_keys("./perset_keys.csv", key="name", res_type="dict")
# gene_keys("./default-44-keyboard.csv", key="name", res_type="list")
