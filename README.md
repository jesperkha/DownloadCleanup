# DownloadCleanup

### **Installation**

Either use git fork or download the zip file of the repository.

<br>

### **How to use**

_You need to have python installed on your computer_

- Open a terminal window and navigate to the folder with the `main.py` file in it.
- Run the command `python main.py` to run the default cleanup process.
- Additional arguments can be given, such as the flags below.

<br>

### **Flags**

`-r` | Automatically rename files to date of download / edit.

`-c` | Will request an input for new name of each file. Leaving the input empty will just keep the current filename.

`-d` | Delete all `.exe` files. This is usually done to remove installers. Will run default process as well.

`-D` | Delete **every** file in downloads folder.

<br>

### **Adding new directories**

To add new directories for sorting other filetypes you can do so by adding the path in the `ext.py` file.

The file is formatted like this:

```python
[
    [ [list of file extentions], path ],

    # Example:
    [ ["png", "jpg"], "/Pictures" ]
    # The full path becomes:
    # C:/Users/yourlogin/Pictures/_Downloads/

    # The _Downloads directory is added automatically and can be changed in config.json
]
```
