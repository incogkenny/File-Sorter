import os
import shutil

# Define the path to the download folder
path = 'C:/Users/josh0/Downloads'

# Get a list of files in the download folder
list_ = os.listdir(path)

# Iterate through each file in the list
for file_ in list_:
    # Split the file name and extension
    name, ext = os.path.splitext(file_)
    
    # Remove the leading dot from the extension
    ext = ext[1:]
    
    # If the extension is empty, skip the file
    if ext == '':
        continue
    
    # Skip directories/folders
    if ext.lower() == 'dir':
        continue
    
    # Documents
    elif ext.lower() == 'ppt' or ext.lower() == 'pptx':
        shutil.move(path + '/' + file_, path + '/Docs/Powerpoint/' + file_)
    elif ext.lower() == 'doc' or ext.lower() == 'docx' or ext.lower() == 'rtf':
        shutil.move(path + '/' + file_, path + '/Docs/Word/' + file_)
    elif ext.lower() == 'pdf':
        shutil.move(path + '/' + file_, path + '/Docs/Pdf/' + file_)
    elif ext.lower() == 'xls' or ext.lower() == 'xlsx' or ext.lower() == 'xlsm' or ext.lower() == 'xlsb':
        shutil.move(path + '/' + file_, path + '/Docs/Excel/' + file_)
    elif ext.lower() == 'xml':
        shutil.move(path + '/' + file_, path + '/Docs/Xml/' + file_)
    
    # Images
    elif ext.lower() == 'png' or ext.lower() == 'jpg' or ext.lower() == 'jpeg' or ext.lower() == 'webp' or ext.lower() == 'svg':
        shutil.move(path + '/' + file_, path + '/Images/' + file_)
    
    # Zips and other compressed files
    elif ext.lower() == 'zip' or ext.lower() == '7z' or ext.lower() == 'rar':
        shutil.move(path + '/' + file_, path + '/Zips-RARs/' + file_)
    
    # Executables
    elif ext.lower() == 'exe':
        shutil.move(path+'/'+file_, path+'/.exe/' + file_)
    
    # Move other files to the "Other" directory
    else:
        shutil.move(path + '/' + file_, path + '/Other/' + file_)

        shutil.move(path + '/' + file_, path + '/Other/' + file_)
