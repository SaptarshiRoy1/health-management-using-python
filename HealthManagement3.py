import datetime
r=str(datetime.datetime.now())


print("Health Management System")
dict1={1:"harry",2:"rohann",3:"rohit"}
dict2={1:"food",2:"exercise"}
dict3={1:"log",2:"retrive"}


for i,j in dict1.items():
    print("press-",i,"for-",j)
a=int(input())

for u,v in dict2.items():
    print("press-",u,"for-",v)
b=int(input())

for m,n in dict3.items():
    print("press-",m,"for-",n)
c=int(input())

if c ==1:
    k=1
    while k==1:
        s = input("Enter\n")

        with open(dict1[a]+dict2[b]+".txt","a") as f:
            f.write("["+r+"]-"+s+"\n")
            print("Successfully Written")
        k=int(input("1-add more\n2-exit\n"))

elif c==2:
    with open(dict1[a]+dict2[b]+".txt","r") as f:
        print(f.read())
else:
    print("Wrong Input")
