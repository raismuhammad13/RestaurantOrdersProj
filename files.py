import os 
import time 


def get_file(filepath):
    file_list = []
    for file in os.listdir(filepath):
        if file.endswith('.csv'):
            file_list.append(file)
    return file_list