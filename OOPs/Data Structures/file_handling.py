import os
#create file
def create_file(file_name):
    with open(file_name,"w") as file_handle:
        file_handle.close()

#add content
def append_content(file_name,content):
    with open(file_name,"a") as file_handle:
        file_handle.write(content)
        file_handle.write(content)
        file_handle.write(content)
        file_handle.close()

#read and print content
def read_print_content(file_name):
    with open(file_name,"r") as file_handle:
        content = file_handle.read()
        print(content)
        file_handle.close()

#delete file
def delete_file(file_name):
    if os.path.exists("file_name"):
        os.remove(file_name)
        print(f"File {file_name} got deleted")

    else:
        print("File does not exixt")


file_name = "my_notes.txt "
content = "Namaskara Karnataka \n"
create_file(file_name)

append_content(file_name,content)

read_print_content(file_name)

delete_file(file_name)