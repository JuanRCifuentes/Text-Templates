from string import Template
import os

def clear_directory():
    os.system('rm -rf `find . -type d -name __pycache__`')
    return

def _createFolder(folder):
    # Check whether the specified path exists or not
    folder_exist = os.path.exists(folder)

    if not folder_exist:
        # Create a new directory because it does not exist 
        os.makedirs(folder)

def create(template, data, name, folder):
    os.system('clear')
    with open(template, 'r') as f:
        src = Template(f.read())
        result = src.substitute(data)

    _createFolder(folder)

    with open(f'{folder}/{name}', 'w') as output:
        output.write(result)

    clear_directory()

    print(f'Created file in path: {folder}/{name}')

if __name__ == '__main__':
    print('Hello World!')
