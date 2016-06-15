# -*- coding: utf-8 -*-
# MDLog.py

import os

def main():
    print u"开始 \n"
    print get_cur_pwd()
    print u"成功！\n"

# 获取当前路径
def get_cur_pwd():
    return os.getcwd()

# 获取路径中的所有文件
def get_recursive_file_list(path):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        if os.path.isdir(full_file_name):
            next_level_files = get_recursive_file_list(full_file_name)
            all_files.extend(next_level_files)
        else:
            all_files.append(full_file_name)
    return all_files

# 获取所有读取文件的头信息
def get_file_head_content(path):
    fo = open(path,"rw+")
    print u"正在读取->"+fo.name
    head = ""
    line = fo.readline()
    while line!=null:
        if(line=="------\n"):
            break
        head += line
        line = fo.readline()  
    fo.close()  
    return head

# 处理头内容加入路径
def insert_other_data_into_head(head,path):
    idx = head.rfind("}")
    head = head[:-idx]+",\n\"url\":\"" + path.replace("\\","/") + "\""+"}"
    return head;

# 获取所有文件的Json
def get_file_josn(all_files):
    print "";

# 写入文件（files.json）文件 
def write_file(content,path):
    fo = open(path, "w")
    fo.write(content)
    fo.close()
    print "success get all files!";

if __name__ == "__main__":
    main()




