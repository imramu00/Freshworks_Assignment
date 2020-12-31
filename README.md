# Freshworks_Assignment
## Initial Steps:
    Clone the repo in your PC.
    Execute the Main.Py File using command prompt or terminal.
      py Main.py
    You have the option to either Open an existing JSON file in the current path or create a new JSON file.

## After the selecting/creating a new JSON file,You can perform the following operations on the JSON object
    1.Create
    2.Read
    3.Delete
    4.Exit
  
## 1.Opening/Creating a File:
    The file could be opened only if it satisfies the condition:
      -If it is not being used by any other proceess.
      -If the given file doesn't exist a new file in the given name would be created.
    You would require to given a name to the new JSON file to be created and opened.
    If you create a new file , you have the option to set time to live for the entire JSON object in seconds.
## 2.Create:
    -You could create a new Key-Value pair only if the file is less than 1GB in size.
    -The length of both key and value should be less that 32char in length.
    -The size of the value should be less than 16KB in size.
## 3.Read
    -For the given key ,the key-value pair could be read only if it has not expired.
    
## 4.Delete
    -For the given key ,the key-value pair will be deleted only if it has not expired.
## 5.Exit
    -Once you press exit ,The JSON file would be updated and closed.
