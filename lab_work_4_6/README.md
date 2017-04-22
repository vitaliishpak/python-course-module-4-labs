##Laboratory Work 4.6

####Description:

1. Create list with 5 elements of string data
2. Create empty config.data file
3. Create function “writeConfig” that will do:
    a. Take two arguments (file object and string data)
    b. Read data from file and if in config.data lines
        - “Configuration file! Do not modify!”, skip step else write above line.
    c. Write second argument (string data) from new line, ex. 
        - “string_data;”
4. Create simple python decorator were:
    a. Created file object with path – “config.data” and mode “r+”
    b. writeConfig function called
    c. close file object
5. Use for loop for write each item from list created before
6. Use breakpoint after every iteration and check config.data file content

####Here is its solution code:

*solution_4_6.py*
```python
def file_content_decorator(func):
    def wrapper(item):
        data_file = open("lw_4_6_package/config.data", "r+")
        func(data_file, item)
        data_file.close()
    return wrapper


@file_content_decorator
def write_config(file, line):   # Define function in step 3
    if "Configuration file! Do not modify!" in file.read():
        file.write("%s;\n" % (line))
    else:
        file.write("Configuration file! Do not modify!\n"+\
                   "%s;\n"%(line))


data_lst = ["index.php", "main.py", "__init__.py", "core.py", "data.bin"]

config_data = open("lw_4_6_package/config.data", 'w')
config_data.write('')
config_data.close()

for item in data_lst:
    write_config(item)
```