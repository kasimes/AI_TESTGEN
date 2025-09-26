import json
import os

# # diff.json dosyasını aç
# with open("diff.json", "r", encoding="utf-8") as f:
#     diff_data = json.load(f)

# # Değişen dosyaların isimlerini al
# changed_files = [file["filename"] for file in diff_data.get("files", [])]

# # Sadece dosya isimlerini içeren sade JSON oluştur
# with open("changed_files.json", "w", encoding="utf-8") as f:
#     json.dump({"files": changed_files}, f, indent=2)

# print("Değişen dosyalar:", changed_files)


def extract_changed_files(diff_file="diff.json", valid_extensions=None):
    if valid_extensions is None:
        valid_extensions = {'.py', '.java'}
    if not os.path.exists(diff_file):
        print(f"Dosya bulunamadı: {diff_file}")
        return []
    with open(diff_file, "r", encoding="utf-8") as f:
        try:
            diff_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"JSON okuma hatası: {e}")
            return []
        #değişen dosyaların isimlerini al
    files_info = diff_data.get("files",[])
    changed_files = []
    
    for file_entry in files_info:
        file_name = file_entry.get("filename")
        if not file_name:
            continue
        if not any(file_name.endswith(ext) for ext in valid_extensions):
            continue
        if not os.path.exists(file_name):
            print(f"Uyarı: Dosya bulunamadı {file_name}, atlanıyor...")
            continue
        changed_files.append(file_name)   

    return changed_files

def save_changed_files(changed_files, output_file="changed_files.json"):

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump({"files": changed_files}, f, indent=2)

    print(f"Değişen dosyalar {output_file} dosyasına kaydedildi.")
    print ("Değişen dosyalar:", changed_files)

if __name__ == "__main__":
    changed_files = extract_changed_files()
    if changed_files:
      save_changed_files(changed_files)  
    else:
      print("Değişen dosya bulunamadı veya tüm dosyalar filtrelendi .")  