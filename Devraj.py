
#search for keywords and pull out  entire lines and print them
list=["crash", "reboot","tombstone"] #created list
f=open("logcat_5.txt",'r')#open log file
lines_list=f.readlines() #assign line by line data to line_list variable
for i in lines_list:  #read each line
    for j in list:  #read each word
        if j in i: #if that word in read line print it
            new=open("devaraj_new.txt","a")
            new.writelines(i)#write in new file
            new.close()
            print(i)
f.close()