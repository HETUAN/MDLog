hello = '''{
    "name":"zhangsanm",
    "age":12,
    "sex":"man"
}'''
idx = hello.rfind("}")
print hello[:idx]