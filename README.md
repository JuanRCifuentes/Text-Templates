# Text Templates

This repo was created to facilitate the use of text-file templates to create new text files. It is based in [`Template` from library `string`](https://docs.python.org/3/library/string.html#string.Template). Does not require any pip installation as this library is native in python.

The main folders ('Created_Files', 'File_Creators' and 'Templates') are not being tracked by git, so anything written on those is gonna be only locally saved.

> Text files are not only `.txt`. There are a huge number of extensions that use text files, such as '.py', '.js', '.xml', etc.

## Usage
To use this repo, the only thing you have to keep in mind is importing the file 'File_Creators/file_from_template.py' and using the function `create()`. This funciton takes 4 parameters:
    - template: A string with the path to the template.
    - data: A dictionary with the keys being the placeholders in the template, and the values the text to substitute.
    - name: A string with the name (including the extension) of the new file.
    - folder: A string denoting the path for the new file.
It creates a new file using the template passed and the dictionary to fill the values. The new file is saved with a designated name and in a designated folder. The folder is created if it didn't exist at the moment of the execution.

The file 'File_Creators/example.py' shows how to implement all this while keeping the repository organized.

## Organization
To keep things organized, you can store your templates in the 'Templates' folder, create new scripts (based on the 'File_Creators/example.py' file) on the 'File_Creators' folder and save the new files in the 'Created_Files' folder.