print("Name:Lata.S.B",
       "USN:1AY24AI060",
       "Section:'O'")
import os
import shutil

def selective_copy(source_folder, dest_folder, file_ext):
    os.makedirs(dest_folder, exist_ok=True)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_ext.lower()):
                source_path = os.path.join(foldername, filename)
                dest_path = os.path.join(dest_folder, filename)
                print(f"Copying: {source_path} -> {dest_path}")
                shutil.copy2(source_path, dest_path)

source = input("Enter the source folder path: ")
destination = input("Enter the destination folder path: ")
extension = input("Enter the file extension (e.g., .pdf, .jpg): ")

selective_copy(source, destination, extension)
import os

def find_large_files(folder, size_limit_mb=100):
    size_limit = size_limit_mb * 1024 * 1024 

    print(f"Scanning '{folder}' for files larger than {size_limit_mb} MB...\n")

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                filesize = os.path.getsize(filepath)
                if filesize > size_limit:
                    print(f"{os.path.abspath(filepath)} - {filesize / (1024 * 1024):.2f} MB")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Cannot access {filepath}: {e}")

if __name__ == "__main__":
    folder_to_search = input("Enter the path to the folder to scan: ")
    find_large_files(folder_to_search)


import os
import re

def close_gaps(folder, prefix):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    numbered_files = []
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    numbered_files.sort()

    expected_number = 1
    for current_number, filename in numbered_files:
        if current_number != expected_number:
            new_name = f"{prefix}{str(expected_number).zfill(3)}.txt"
            print(f"Renaming {filename} -> {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        expected_number += 1

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter file prefix (e.g., 'spam'): ")
    close_gaps(folder, prefix)
import os
import re

def insert_gap(folder, prefix, insert_at):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    numbered_files = []
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    numbered_files.sort(reverse=True)  

    for number, filename in numbered_files:
        if number >= insert_at:
            new_number = number + 1
            new_name = f"{prefix}{str(new_number).zfill(3)}.txt"
            print(f"Renaming {filename} -> {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter file prefix (e.g., 'spam'): ")
    insert_at = int(input("Insert gap at number: "))
    insert_gap(folder, prefix, insert_at)