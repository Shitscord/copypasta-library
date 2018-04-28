import os, time

print("Finding text files")
namelist=[]
for file in os.listdir("lib"):
    if file.endswith(".txt"):
        item = (file[:-4])
        print("Found: ", item)
        namelist.append(item)
        time.sleep(.05)
namelist.sort
print("CP List: ", namelist)


towrite="cplibrary = ["
x=0
while x<len(namelist):
    towrite=(towrite+"'"+str(namelist[x])+"'")
    if x==len(namelist)-1:
        towrite=(towrite+"]")
    else:
        towrite=(towrite+", ")
    x=x+1

print(towrite)

writefile = open("index.py","w")
writefile.write(towrite)
writefile.close()

input("Done!")