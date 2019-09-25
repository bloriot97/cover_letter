import os
import sys
import json
import subprocess
import datetime
from shutil import copyfile

def read_file(file_path):
    content = ""
    with open(file_path) as file:
        content = file.read()
    return content

def read_json(file_path):
    data = {}
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

if __name__ == "__main__":
    cover_letter_name = sys.argv[1]
    global_data = read_json('info.json')
    local_data = read_json(f'./cover_letters/{cover_letter_name}/info.json')
    content = read_file(f'./cover_letters/{cover_letter_name}/content.md')
    data = global_data.copy()
    if "date" not in local_data:
        now = datetime.datetime.now()
        local_data["date"] = now.strftime("%B %d, %Y")
    data["cl_data"] = local_data

    copyfile(f'./cover_letters/{cover_letter_name}/content.md', 'template/tmp/content.md')

    subprocess.run(["relaxed", "template/cover_letter.pug", f"./cover_letters/{cover_letter_name}/cover_letter.pdf", "--temp", "template/tmp/", "--build-once", "--locals", json.dumps(data)])
