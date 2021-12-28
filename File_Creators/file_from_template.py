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

def create(template: str, data: dict, name: str, folder: str):
    '''
    Creates a new file using the template passed and the dictionary keys to fill the values. 
    The new file is saved with a designated name and in a designated folder. 
    The folder is created if it didn't exist at the moment of the execution.

    Parameters: 
    - template: A string with the path to the template.
    - data: A dictionary with the keys being the placeholders in the template, and the values the text to substitute.
    - name: A string with the name (including the extension) of the new file.
    - folder: A string denoting the path for the new file.

    Returns: The path of the new file relative to the execution folder.
    '''

    os.system('clear')
    with open(template, 'r') as f:
        src = Template(f.read())
        result = src.substitute(data)

    _createFolder(folder)

    with open(f'{folder}/{name}', 'w') as output:
        output.write(result)

    clear_directory()

    print(f'Created file in path: {folder}/{name}')
    return f'{folder}/{name}'

if __name__ == '__main__':
    print('Hello World!')
