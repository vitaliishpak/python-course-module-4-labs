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
