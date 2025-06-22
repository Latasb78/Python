print("Name:Lata.S.B",
       "USN:1AY24AI060",
       "Section:'O'")
import os
import shutil

def selective_copy(source_folder, dest_folder, file_ext):
    # Ensure destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_ext.lower()):
                source_path = os.path.join(foldername, filename)
                dest_path = os.path.join(dest_folder, filename)
                print(f"Copying: {source_path} -> {dest_path}")
                shutil.copy2(source_path, dest_path)

# User input
source = input("Enter the source folder path: ")
destination = input("Enter the destination folder path: ")
extension = input("Enter the file extension (e.g., .pdf, .jpg): ")

# Call the function
selective_copy(source, destination, extension)
#deleting unneeded files
import os

def find_large_files(folder, size_limit_mb=100):
    size_limit = size_limit_mb * 1024 * 1024  # Convert MB to bytes

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

# Example usage
if __name__ == "__main__":
    folder_to_search = input("Enter the path to the folder to scan: ")
    find_large_files(folder_to_search)
