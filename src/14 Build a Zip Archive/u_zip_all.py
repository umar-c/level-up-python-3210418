import zipfile
from zipfile import ZipFile
import os
 
def zip_all(path, filetypes, zip_file='default.zip'):
    if path is None or "".__eq__(path.strip()):
        print("No file path has been provided! Exiting...")
        return
    
    with ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as myzip:
        for root, _, files in os.walk(path):
           for file in files:
                if '.'+file.split('.')[1] in filetypes:
                    full_filename = os.path.join(root, file)
                    print(f'Adding {full_filename} to {zip_file}...')
                    myzip.write(full_filename)

    print(f'\nLisiting the contents of {zip_file}...')
    with ZipFile(zip_file, 'r') as myzip:
        myzip.printdir()

# commands used in solution video for reference
if __name__ == '__main__':
    zip_all('./my_stuff', ['.jpg','.txt'], 'my_stuff.zip')
