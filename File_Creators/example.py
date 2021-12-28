from file_from_template import create

def example():
    folder = 'Created_Files/Test_Template'
    name = 'test_file.txt'

    data = {
        'Title': 'Test File',
        'Name': 'File Tester 1',
        'Amount': '5'
    }

    template = 'Templates/test_template.txt'

    create(template, data, name, folder)

if __name__ == '__main__':
    example()
    