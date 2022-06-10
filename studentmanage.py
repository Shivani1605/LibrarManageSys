from os import path
from datetime import datetime, timedelta
from book import Book
class StudentManagement:
    def __init__(self):
        pass
    def ShowAllBook(self):
        if(path.exists("BookData.txt")):
                with open("BookData.txt","r") as fb:
                    print(fb.read())  
        else:
            print("File does not exist")   


    def searchBook(self,option):
        if(path.exists("BookData.txt")):
            with open("BookData.txt","r") as fb:
                for line in fb:
                    if(str(option)in line):
                        print("Record is found")
                        print(line)
                        break
                else:
                    print("Record not found")
        else:
            print("File does not exist")

    
    def IssueBook(self,bid,Fname,date_issue):
        Issue=False
        with open("BookData.txt","r") as fb:
            for line in fb:
                Book=line.split(",")
                if(Book[0]==str(bid) and Book[3]=="True\n"):
                    with open("BookIssuedData.txt","a") as fb:
                        fb.write(str(bid))
                        fb.write(",")
                        fb.write(Fname)
                        fb.write(",")
                        fb.write(str(date_issue))
                        fb.write("\n")     
                        Issue=True
                        break
            else:
                print("Book is not available!")
        if(Issue):
            a=[]
            found=False
            with open("BookData.txt","r") as fb:
                for line in fb:
                    if(str(bid) not in line):
                        a.append(line)
                    else:
                        book=line.split(",")
                        book[3]="False\n"
                        book=",".join(book)
                        a.append(book)
                        found=True
            if(found):
                with open("BookData.txt","w") as fb:
                    for line in a:
                        fb.write(line)
                    print("Successfully Issued!!!")
    
    def ReturnBook(self,bid,Fname,date_return):
        if(path.exists("BookIssuedData.txt")):
            with open("BookIssuedData.txt","r") as fb:
                Return=False
                for  line in fb:
                    if((str(bid) in line) and (Fname in line)) :
                        Return=True
                        print("*****************************************************")
                        book=line.split(",")
                        book_i=book[2].split(("-"))
                        year=int(book_i[0])
                        month=int(book_i[1])
                        day=int(book_i[2])
                        D_issue=datetime(year,month,day)
                        print("Date of Book Issue: ",D_issue)
                        book_r=date_return.split(("-"))
                        year=int(book_r[0])
                        month=int(book_r[1])
                        day=int(book_r[2])
                        D_return=datetime(year,month,day)
                        print("Date of Book Return: ",D_return)
                        #difference
                        diff=(D_return-D_issue)
                        diff=diff.days
                        print("Total days you have book with you: ",diff)
                        day=5
                        if(diff>5):
                            extra_days=diff-5
                            due=extra_days*10
                            
                            print("please pay the due for late submission of",extra_days ,"days is:",due,"Rupee")
                            print("Thank you !!!")
                        else:
                            print("Thank you !!!")
                            
            if(Return):
                Book=[]
                found=False
                with open("BookIssuedData.txt","r") as fb:
                    for line in fb:
                        bid=str(bid)
                        try:
                            line.index(bid,0,3)
                            found=True
                        except:
                            Book.append(line)
            
            
                        found=True
                if(found):
                    with open("BookIssuedData.txt","w") as fb:
                        for line in Book:
                            fb.write(line)
                    
        else:
            print("Please issue your book!")
