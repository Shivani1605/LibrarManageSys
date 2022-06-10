class Book():
    
    def __init__(self,bid=1,bname=" ",author=" ",avlbl=" "):
        self.bid = bid
        self.bname = bname
        self.author = author
        self.avlbl=avlbl

        
    def displayBook(self):
        print("Book ID :",self.bid)
        print("Book Name :",self.bname)
        print("Book Author :",self.author)
        print("Book Availablity: ",self.avlbl)

        
    def __str__(self):
        data=str(self.bid)+","+str(self.bname)+","+str(self.author)+","+str(self.avlbl)
        return data
