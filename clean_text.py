
import os
import re
from sys import argv


def Open_file(filename):
    
    with open(filename, 'r', encoding='UTF-8') as file:
        file_string = file.read()
    file.close()
    return file_string

def Save_into_file(raw_data, save_path, new_file_name=''):

    full_save_path = os.path.join(save_path, new_file_name)
    file = open(full_save_path, mode='w', encoding='utf8')
    file.write(raw_data)
    file.close()

def Not_full_English(text):

    not_full_english = re.search(r'[^\x00-\x7F]+', text) # not an ASCII chae
    if not_full_english != None:
        return 1
    return 0

def Name_start_with_dot(file_name):

    name_strat_with_dot = re.search(r"^\.", file_name)
    if name_strat_with_dot != None:
        return 1
    else:
        return 0

def Text_treatment(file_string):

    raw_text = ""
    #saving only the data that is under the <text> </text> tab
    start_index = file_string.find("<text")
    if start_index != -1:
        close_first_text_tab_index = file_string[start_index:].find(">")
        end_index = file_string[start_index + close_first_text_tab_index:].find("</text>")
        raw_text = file_string[start_index + close_first_text_tab_index + 1 : start_index + close_first_text_tab_index + end_index]
    #treating the headers - deleting the == ... == and at the end of each header I added a '.'
    raw_text = re.sub(r"=+ ", "", raw_text)
    raw_text = re.sub(r" =+", ".", raw_text)
    #delete the [[ ]] that symbolyze links
    raw_text = re.sub(r"[\[\[\]\]]", "", raw_text)
    #delete all images descriptions
    raw_text = re.sub(r"File:[ -~]+px[ -~]+.", "", raw_text)


    return raw_text


if __name__ == "__main__":

    dirty_files_path = argv[1]
    clean_files_path = argv[2]

    dirty_files_list = os.listdir(dirty_files_path) #files names inclding the ".txt" extention
    
    for dirty_file in dirty_files_list:
        dirty_file_path = os.path.join(dirty_files_path, dirty_file)
        if (Not_full_English(dirty_file)) or (Name_start_with_dot(dirty_file)):
            os.remove(dirty_file_path) # remove the non full english file from the directory
        else:
            file_string = Open_file(dirty_file_path)
            raw_text = Text_treatment(file_string)
            Save_into_file(raw_text, clean_files_path, dirty_file)
