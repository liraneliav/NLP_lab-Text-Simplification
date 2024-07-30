
import os
import re
from sys import argv

def Open_file(filename):
    
    with open(filename, 'r', encoding='UTF-8') as file:
        file_string = file.read()

    file.close()
    
    return file_string

def Spilt_into_texts(full_file_str):
    
    texts = full_file_str.split("<page>")

    return texts

def Save_texts(texts, texts_dic_full_path):

    for text in texts:
        start_index = text.find("<title>")
        if start_index != -1:
            end_index = text.find("</title>")
            text_title = text[start_index+len("<title>"):end_index]
            text_title = re.sub(r'\@|\$|\%|\&|\\|/|\:|\*|\?|\"|\'|\<|\>|\||\~|\`|\#|\^|\+|\=|\{|\}|\[|\]|\;|\!', " ", text_title)
            if (len(text_title) < 100):
                new_text_path = os.path.join(texts_dic_full_path, text_title + ".txt")
                file = open(new_text_path, mode='w', encoding='utf8')
                file.write(text)
                file.close()


if __name__ == "__main__":

    filename = argv[1]
    texts_dic_path = argv[2]

    file_string = Open_file(filename)
    texts_array = Spilt_into_texts(file_string)
    Save_texts(texts_array, texts_dic_path)
    