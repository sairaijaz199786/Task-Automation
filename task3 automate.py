import os
import shutil
print("=" * 50)
print("📂 Automatic File Organizer")
print("=" * 50)
# Folder path
folder_path = input("Enter the folder path: ").strip()
if not os.path.exists(folder_path):
    print("❌ Folder not found!")
    exit()
# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Python Files": [".py"]
}
moved_files = 0
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)
        for folder_name, extensions in file_types.items():
            if extension.lower() in extensions:
                destination_folder = os.path.join(folder_path, folder_name)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(file_path, os.path.join(destination_folder, file))
                print(f"✅ {file} → {folder_name}")
                moved_files += 1
                break
print("\n" + "=" * 50)
print(f"🎉 File organization completed!")
print(f"📦 Total files moved: {moved_files}")
print("=" * 50)