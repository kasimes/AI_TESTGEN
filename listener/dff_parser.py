import json

# diff.json dosyasını aç
with open("diff.json", "r", encoding="utf-8") as f:
    diff_data = json.load(f)

# Değişen dosyaların isimlerini al
changed_files = [file["filename"] for file in diff_data.get("files", [])]

# Sadece dosya isimlerini içeren sade JSON oluştur
with open("changed_files.json", "w", encoding="utf-8") as f:
    json.dump({"files": changed_files}, f, indent=2)

print("Değişen dosyalar:", changed_files)

