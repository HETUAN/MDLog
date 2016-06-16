# -*- coding: utf-8 -*-
# MDLog.py

import os
base = ""
def main():
    print u"start"
    files = get_recursive_file_list(get_cur_pwd())
    write_file(get_file_josn(files),os.path.join(base,"Data\\files.json"))
    print u"success!"

# 获取当前路径 使用时要注意路径
def get_cur_pwd():
    global base 
    base = os.path.split(os.path.split(os.getcwd())[0])[0]
    return os.path.join(base,"md")

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
    print "success get all files!";
    return all_files

# 获取所有读取文件的头信息
def get_file_head_content(path):
    fo = open(path,"r")
    # print u"正在读取->"+fo.name
    print u"on reading ->"+fo.name
    head = ""
    line = fo.readline()
    while line!=None:
        if(line=="------\n"):
            break
        head += line
        line = fo.readline()  
    fo.close()  
    return head

# 处理头内容加入路径
def insert_other_data_into_head(head,path):
    # print head
    # print "------"
    # print path
    # print base
    # print path.replace(base,"")
    idx = head.rfind("}")
    head = head[:idx-1]+",\n\"url\":\"" + path.replace(base+"\\","").replace("\\","/") + "\""+"}"
    return head;

# 获取所有文件的Json
def get_file_josn(all_files):
    fjson = "{\"files\":["
    for file in all_files:
        fjson += insert_other_data_into_head(get_file_head_content(file),file)+","
    fjson = fjson[:-1]
    fjson += "]}"
    print "success get josn menu data!";
    return fjson

# 写入文件（files.json）文件 
def write_file(content,path):
    fo = open(path, "w")
    fo.write(content)
    fo.close()
    print "success write into files.josn!";

if __name__ == "__main__":
    main()




