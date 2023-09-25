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
        if not os.path.isdir(path + '/' + '/Docs/Powerpoint/'):
            os.mkdir(path + '/Docs/Powerpoint/')
        shutil.move(path + '/' + file_, path + '/Docs/Powerpoint/' + file_)

    elif ext.lower() == 'doc' or ext.lower() == 'docx' or ext.lower() == 'rtf':
        if not os.path.isdir(path + '/' + '/Docs/Word/'):
            os.mkdir(path + '/Docs/Word/')
        shutil.move(path + '/' + file_, path + '/Docs/Word/' + file_)

    elif ext.lower() == 'pdf':
        if not os.path.isdir(path + '/' + '/Docs/Pdf/'):
            os.mkdir(path + '/Docs/Pdf/')
        shutil.move(path + '/' + file_, path + '/Docs/Pdf/' + file_)

    elif ext.lower() == 'xls' or ext.lower() == 'xlsx' or ext.lower() == 'xlsm' or ext.lower() == 'xlsb':
        if not os.path.isdir(path + '/' + '/Docs/Excel/'):
            os.mkdir(path + '/Docs/Excel/')
        shutil.move(path + '/' + file_, path + '/Docs/Excel/' + file_)

    elif ext.lower() == 'xml':
        if not os.path.isdir(path + '/' + '/Docs/Xml/'):
            os.mkdir(path + '/Docs/Xml/')
        shutil.move(path + '/' + file_, path + '/Docs/Xml/' + file_)

    # Images
    elif ext.lower() == 'png' or ext.lower() == 'jpg' or ext.lower() == 'jpeg' or ext.lower() == 'webp' or ext.lower() \
            == 'svg':
        if not os.path.isdir(path + '/' + '/Images/'):
            os.mkdir(path + '/Images/')
        shutil.move(path + '/' + file_, path + '/Images/' + file_)

    # Zips and other compressed files
    elif ext.lower() == 'zip' or ext.lower() == '7z' or ext.lower() == 'rar':
        if not os.path.isdir(path + '/' + '/Zips-RARs/'):
            os.mkdir(path + '/Zips-RARs/')
        shutil.move(path + '/' + file_, path + '/Zips-RARs/' + file_)

    elif ext.lower() == 'exe':
        if not os.path.isdir(path + '/' + '/Apps-Setups/'):
            os.mkdir(path + '/Apps-Setups/')
        shutil.move(path + '/' + file_, path + '/Apps-Setups/' + file_)

    else:
        if not os.path.isdir(path + '/' + '/Other/'):
            os.mkdir(path + '/Other/')
        shutil.move(path + '/' + file_, path + '/Other/' + file_)
