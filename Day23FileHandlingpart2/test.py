import csv
with open("dictcsv.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

with open("file.csv","w",newline="") as f:
    data = ["Col1","Col2","Col3"]
    writer = csv.DictWriter(f,fieldnames=data)
    writer.writeheader()
    writer.writerow({"Col1":"A","Col2":"B","Col3":"C"})
    writer.writerow({"Col1":"Aa","Col2":"Bb","Col3":"Cc"})

with open("student.csv","w",newline="") as f:
    heading = ["Id","Name","Marks"]
    writer = csv.DictWriter(f,heading)
    writer.writeheader()
    writer.writerows([
        {"Id":101,"Name":"Fathima","Marks":99},
        {"Id":102,"Name":"Tarannum","Marks":99},
        {"Id":103,"Name":"Nikath","Marks":99},

    ])
