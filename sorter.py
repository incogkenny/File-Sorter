import os
import shutil

path = 'C:/Users/josh0/Downloads'
list_ = os.listdir(path)


for file_ in list_:
    name, ext = os.path.splitext(file_)

    ext = ext[1:]

    if ext == '':
        continue

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
    elif ext.lower() == 'png' or ext.lower() == 'jpg' or ext.lower() == 'jpeg' or ext.lower() == 'webp' or ext.lower() \
            == 'svg':
        shutil.move(path + '/' + file_, path + '/Images/' + file_)

    # Zips and other compressed files
    elif ext.lower() == 'zip' or ext.lower() == '7z' or ext.lower() == 'rar':
        shutil.move(path + '/' + file_, path + '/Zips-RARs/' + file_)

    elif ext.lower() == 'exe':
        shutil.move(path+'/'+file_, path+'/.exe/' + file_)

    else:
        shutil.move(path + '/' + file_, path + '/Other/' + file_)
