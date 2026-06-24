import json

filepath ="C:\\python playwright\\June2026_batch2_playwright_APITesting\\product\\python_files\\test_data.json"

with open(filepath,"r") as file:  data = json.load(file)  print(data['base_url'])  print(data["resource"])  data["token"]="qaclick123"  with open(filepath, "w") as file:     json.dump(data,file,indent = 4)