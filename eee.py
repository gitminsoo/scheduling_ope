import json
import json_parse

with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)

print(process)