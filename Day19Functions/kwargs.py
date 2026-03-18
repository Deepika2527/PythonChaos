def demo(**kwargs):
    print(kwargs)
demo(name="abc", clas = "python")


def std(**st):
    for k,v in st.items():
        print(k, "-" , v)
std(id='101',id1 = "102", id3= '103')




print("Exmaple with pos,args,heywordargs,kwargs")

def institute(name,*course,cnt_no,**price):
    print("Institution Name : ", name)
    print("Course avaiable are :", course)
    print("ContactNo  : ", cnt_no)
    print("Prices : ", price)
institute("AIT",'Pfs','Jfs','Mern',cnt_no="9090909090",pfs=40000,jfs=40000,mern =4000)