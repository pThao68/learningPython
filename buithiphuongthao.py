# Đề bài
# - Đọc 1 file văn bản gồm nhiều dòng
# - Ghi ra màn hình theo thứ tự ngược lại của các dòng
# ví du: 
# Nam quốc sơn hà 
# Nam đế cư
# ==>
# Nam đế cư
# Nam quốc sơn hà
with open('abc.txt', 'r') as file:
    for line in reversed(list(file.readlines())):
        print(line.strip())