import os

print('Welcome to the Level-Up Corporation Data Extraction Tool')
print('----------------FOR AUTHORIZED INTERNAL USE ONLY!!----------------\n')

cwd = os.getcwd()

files = os.listdir(cwd)

file_list = []

for file in files:
    if os.path.isfile(os.path.join(cwd, file)):
        file_info = {
            'name': file,
            'size_bytes': os.path.getsize(os.path.join(cwd, file)),
            'absolute_path': os.path.abspath(os.path.join(cwd, file))
        }
        file_list.append(file_info)


print(file_list)
