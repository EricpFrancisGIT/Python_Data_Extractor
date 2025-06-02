import os
from typing import List, Dict, Optional
from tabulate import tabulate


print("-----This is an Data Extraction Tool for Level Up Corporation-----")
print("-----Use of this tool is subject to Approval by Management"
      " and is intended for internal use only.-----")

def get_file_info(path: Optional[str] = ".") -> List[Dict[str, str]]:
 
    file_info_list = []

    for root, _, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            stats = os.stat(full_path)

            file_info = {
                "File Name": file_name,
                "File Location Path": os.path.relpath(full_path, path),
                "Size (KB)": f"{stats.st_size / 1024:.2f}"
            }
            file_info_list.append(file_info)

    return file_info_list

if __name__ == "__main__":
    files = get_file_info()
    print(tabulate(files, headers="keys", tablefmt="grid"))

print("-----Extraction Completed-----")
print("-----Thank you for using the Level Up Corporation Data Extraction Tool-----")


