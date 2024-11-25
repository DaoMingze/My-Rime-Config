import yaml
import html
from pprint import pprint

# 读取YAML配置文件
with open("theme/trime/wendao.trime.yaml", "r", encoding="utf-8") as file:
    try:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    except yaml.YAMLError as e:
        print(e)
        config = {}

default_config = config.get("preset_keyboards", {}).get("default", {})

keyboard_list = []
for i in range(len(default_config["keys"])):
    value = default_config["keys"][i]
    if "click" not in value:
        keyboard_list.append(" " * value["width"])
    else:
        keyboard_list.append(value["click"])

### name、width、


output = "\n".join(
    "\t".join(map(str, keyboard_list[i : i + 10]))
    for i in range(0, len(keyboard_list), 10)
)

print(output)

# 创建HTML内容
html_content = "<html><body>"
html_content += "<h1>Preset Default Keys</h1>"
html_content += "<ul>"

# 遍历default_config中的键值对，并添加到HTML内容中
for key, value in default_config.items():
    html_content += f"<li><b>{html.escape(key)}</b>: {html.escape(str(value))}</li>"

html_content += "</ul></body></html>"

# 将HTML内容写入到一个HTML文件中
with open("show.html", "w") as html_file:
    html_file.write(html_content)

print("HTML文件已生成，包含了YAML配置中的default键值对。")
