fp=open("word.txt","w")
if fp:
    print("successfully opend")
    fp.write("i")
    fp.write("a")
    fp.write("")
    fp.close()