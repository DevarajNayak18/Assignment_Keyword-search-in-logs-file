import re    #importing RegExp re Library
file = open(r"logcat_5.txt","r") # Read the file
lst = [w for w in file if re.search(r'crash',w) or re.search(r'tombstone',w) or re.search(r'reboot',w)]
print(lst)
file.close()
with open(r'captured_log1.txt', 'w') as txt:  #created new file to write each lines in that file
    for line in lst: #reading each line by line


































































































































































































