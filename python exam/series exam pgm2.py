file_obj=open("demofile.txt","r+")

condition=True
while condition:
    x = file_obj.readline()
    words=x.split(" ")
    if(len(words)>5):
        w=words[0]
        if(w[0].isupper()):
            print(x)
    if not x:
        condition = False
        print("End of the file")

