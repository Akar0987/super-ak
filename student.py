import csv
fh=open("student.csv","w")
stwriter=csv.writer(fh)
stwriter.writerow(['roll no.','name','marks'])
for i in range (5):
    print("student record",(i+1))
    rollno=int(input("enter roll no"))
    name =input("enter name")
    marks=int(input("enter marks"))
    sturec=[rollno,name ,marks]   #creATE SEQENCE OF USER DATA
    stwriter.writerow(sturec)
fh.close()
          #close file
          
    
