from os import path
class BookManagement:
    def __init__(self):
        pass
    def addBook(self,b):
        with open("BookData.txt","a") as fb:
            fb.write(str(b))
            fb.write("\n")
    def ShowAllBook(self):
        if(path.exists("BookData.txt")):
            with open("BookData.txt","r") as fb:
                print(fb.read())
        else:
            print("File does not exist")
    def searchBook(self,bid):
        if(path.exists("BookData.txt")):
            with open("BookData.txt","r") as fb:
                for line in fb:
                    if(str(bid) in line):
                    
                        print("Record is found")
                        print(line)
                        break
                else:
                    print("Record not found")
        else:
            print("File does not exist")
    def deleteBook(self,bid):
        if(path.exists("BookData.txt")):
            allBook = []  
            found = False
            with open("BookData.txt","r") as fb:
                for line in fb:
                    if(str(bid) not in line):
                        allBook.append(line)                       
                    else:
                        found=True
                print(" Book Record is successfully Deleted!")
            if(found):
                with open("BookData.txt","w") as fb:
                    for line in allBook:
                        fb.write(line)
        else:
            print("Record does not exist")
    def editBook(self,bid):
        if(path.exists("BookData.txt")):
            allBook = []
            found = False
            with open("BookData.txt","r") as fb:
                for line in fb:
                    if(str(bid) not in line):
                        allBook.append(line)
                    else:
                        Book = line.split(",")                        
                        ans = input("Do you wish to change the Book name?  ")
                        if(ans.lower() == "y" ):
                            bnm = input("Enter the new Book name: ")
                            Book[1] = bnm
                        ans = input("Do you wish to change the Book Author?  ")
                        if(ans.lower() == "y" ):
                            authr = input("Enter the new Book Author: ")
                            Book[2] = authr
                        ans = input("Do you wish to change Avaibility status?  ")
                        if(ans.lower() == "y" ):
                            avaibl = input("Enter the new Avaibility status: ")
                            Book[3] = avaibl
                        Book = ",".join(Book)     
                        allBook.append(Book)
                        found=True
            if(found):
                with open("BookData.txt","w") as fb:
                    for line in allBook:
                        fb.write(line)
        else:
            print("File does not exist")
