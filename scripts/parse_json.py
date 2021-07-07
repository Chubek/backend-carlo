import json


def parse_jsons(json_path):
    jsons = []


    with open(json_path, encoding="UTF-8") as jf:
        lines = jf.readlines()
        for line in lines:
            try:
                jsonobj = json.loads(line.strip().strip("\n"))
                jsons.append((line, jsonobj))
            except:
                continue

        jf.close()

    return jsons

def save_jsons(json_path, jsons):
    with open(json_path, encoding="UTF-8") as jf:
        lines = []
        for json in jsons:
            try:
                jsonobj = json.dumps(jsons)
                lines.append(jsonobj + "\t\n")
            except:
                continue

            jf.writelines(lines)

        jf.close()

    return True