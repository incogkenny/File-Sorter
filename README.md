# Download Folder Organizer

This script is a simple tool designed to organize files within a download folder into specific directories based on their file extension. It's particularly useful for users who frequently download various types of files and need a streamlined way to manage them.

## How it Works

The script utilizes Python's built-in `os` and `shutil` modules to interact with the file system and move files accordingly. It operates within a specified download folder, which can be modified as needed. The script iterates through each file in the folder and categorizes them based on their file extension into respective directories.

## Supported File Types and Directories

- **Documents**:
  - PowerPoint presentations (`.ppt`, `.pptx`)
  - Word documents (`.doc`, `.docx`, `.rtf`)
  - PDF files (`.pdf`)
  - Excel spreadsheets (`.xls`, `.xlsx`, `.xlsm`, `.xlsb`)
  - XML files (`.xml`)
  
- **Images**:
  - PNG images (`.png`)
  - JPEG images (`.jpg`, `.jpeg`)
  - WebP images (`.webp`)
  - SVG images (`.svg`)
  
- **Zips and Other Compressed Files**:
  - Zip archives (`.zip`)
  - 7z archives (`.7z`)
  - RAR archives (`.rar`)
  
- **Executables**:
  - Executable files (`.exe`)
  
- **Other**:
  - Files that do not match any of the above categories are moved to an "Other" directory.

## How to Use

1. Modify the `path` variable to specify the location of your download folder.
2. Run the script. It will automatically organize the files within the specified folder into respective directories based on their file extensions.
3. **Optional** add the script to Windows Task Scheduler to configure it to run on a schedule. [Here's a guide how to do that.](https://community.esri.com/t5/python-documents/schedule-a-python-script-using-windows-task/ta-p/915861)

## Note

- Ensure that you have Python installed on your system.
- This script is designed for Windows operating systems. If you're using a different operating system, you may need to adjust the file path format accordingly.

## Disclaimer

Please use this script responsibly and make sure to review the changes it will make to your file system before running it. The script moves files, which could potentially lead to unintended consequences if used incorrectly.
