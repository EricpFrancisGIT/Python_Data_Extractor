import os

print('Welcome to the Level-Up Corporation Data Extraction Tool')
print('----------------FOR AUTHORIZED INTERNAL USE ONLY!!----------------\n')

cwd = os.getcwd()

files = os.listdir('.')

file_info_list = []

for file in files:
    if os.path.isfile(file):
        file_info = {
            'name': file,
            'size_bytes': os.path.getsize(file),
            'absolute_path': os.path.abspath(file)
        }
        file_info_list.append(file_info)

print(file_info_list)
