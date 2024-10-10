"""Day 05 MODULES AND LIBRARIES """

# Write a Python function file_system_operations() -> dict that performs the following operations using the os module and returns a dictionary with:
# The current working directory.
# A list of files in the current directory.
# A confirmation message after creating a new directory called 'new_folder'.


import os

def file_system_opeartions()->dict:
    result={}

    current_directory=os.getcwd()

    files=os.listdir(current_directory) 

    new_directory='new_folder'
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    result['current_directory']=current_directory
    result['files']=files
    result['new_directory']='new_folder created'

    return result
