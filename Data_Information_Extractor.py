import os
from typing import List, Dict, Optional
from tabulate import tabulate
from datetime import datetime

print("-----This is an Data Extraction Tool for Level Up Corporation-----")
print("-----Use of this tool is subject to Approval by Management"
      " and is intended for internal use only.-----")

def get_file_info(path: Optional[str] = ".") -> List[Dict[str, str]]:
    """
    Recursively scans the given directory and returns a list of dictionaries,
    each containing file information.

    Args:
        path (str, optional): Path to the directory to scan. Defaults to current directory.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing file metadata.
    """
    file_info_list = []

    for root, _, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            stats = os.stat(full_path)

            file_info = {
                "File Name": file_name,
                "Path": os.path.relpath(full_path, path),
                "Size (KB)": f"{stats.st_size / 1024:.2f}",
                "Modified Time": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
            file_info_list.append(file_info)

    return file_info_list

if __name__ == "__main__":
    files = get_file_info()  # You can pass a path like get_file_info("/your/path")
    print(tabulate(files, headers="keys", tablefmt="grid"))
