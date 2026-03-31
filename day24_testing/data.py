import csv
f = open("notes.csv","r")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

with open("notes.csv","r") as file:
    reader = csv.reader(file)
    for f in reader:
        print(f)

# using dict redaer
print("using dict reader...")
with open("notes.csv","r") as r:
    reader = csv.DictReader(r)
    # for row in reader:
    #     print(row)
    for row in reader:
        print("---- Student ----")
        for  k,v in row.items():
            print(k, ":", v)

print("Using writer method")

file = open("data.csv","w",newline="")
write = csv.writer(file)
write.writerow(['name','course','mode'])
write.writerow(["deepika","pfs","online"])
write.writerows([
    ["std1","jfs","onile"],
    ["test2","mern","offline"],
    ])

with open("dummy.csv","a",newline="") as file:
    write = csv.writer(file)
    write.writerows([
        ["name","quantity","price","paymentmode"],
        ["mobile","2",30000,"online"],
        ["laptop",1,45000,"cash"]])
    
with open("file.csv","a",newline="") as f:
    data = ["name","role","mode"]
    write = csv.DictWriter(f,fieldnames=data)
    write.writeheader()
    write.writerow({"name":"std1","role":"developer","mode":3000})




