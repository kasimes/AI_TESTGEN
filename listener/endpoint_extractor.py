import json
import re 
import os 


# burada dosya okunacak 

with open("changed_files.json", "r", encoding="utf-8") as f:
    changed_data = json.load(f)

files = changed_data.get("files", [])    



# endpointleri tutacak liste
endpoints = []

# Reges desenleri

regex_patterns = [
   # FastAPI / Flask/Flask-RESTful
    r'@(?:app|router)\.(?:get|post|put|delete|patch)\(["\'](.*?)["\']',
    r'@app\.route\(["\'](.*?)["\'],\s*methods\s*=\s*\[.*?\]\)',
    r'@api\.resource\(["\'](.*?)["\']\)',

    # Django
    r'path\(["\'](.*?)["\'],\s*.*?\)',
    r're_path\(["\'](.*?)["\'],\s*.*?\)',

    # Spring Boot
    r'@(?:GetMapping|PostMapping|PutMapping|DeleteMapping|RequestMapping)\(["\'](.*?)["\']'
]


# Dosyaları işle
for file_path in files:
    if not file_path.endswith(('.py', '.java')):
        continue  # Sadece Python ve Java dosyalarını işle
    if not os.path.exists(file_path):
        print(f"Dosya bulunamadı: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

        routes = []

        for pattern in regex_patterns:
            matches = re.findall(pattern, content)
            if matches:
                routes.extend(matches)
        if routes:
            endpoints.append({
                "file": file_path,
                "endpoints": routes
            })
                     

with open("extracted_endpoints.json", "w", encoding="utf-8") as f:
    json.dump({"endpoints": endpoints}, f, indent=2)

print("Extracted endpoints:", endpoints)    