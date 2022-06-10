from bookManagement import BookManagement
from studentmanage import StudentManagement
from book import Book
choice=0
bM=BookManagement()
sM=StudentManagement()
a=input("Are you an Student? (y or n)")
print("********************Welcome to in Library********************")
#*****************
#student section
#*****************

if (a=="y" or a=="Y"):       
    while(choice!=4):
        print("*****************************")
        print("--------STUDENT MENU---------")
        print("*****************************")
        print('''\t1.Show Book List
        2.Search Book 
        3.Issue Book
        4.Return Book
        5.Exit''')
        print("*****************************")

        try:
            choice = int(input("Enter your choice from 1-5: "))
            
            if(choice==1):#Show all books
                sM.ShowAllBook()

            elif(choice ==2):#Search book
                op=int(input("Enter option 1(bid search)or 2(bname search) or 3(author search) "))
                if(op==1):# Search book by ID
                    bid=int(input("Enter ID no of book which you want to search:"))
                    option=bid
                    sM.searchBook(option)
                elif(op==2):# Search book by Book Name
                    bname=input("Enter Book Name of book which you want to search:") 
                    option=bname
                    sM.searchBook(option)
                        
                elif(op==3):# Search book by Author Name
                    author=input("Enter author Name of book which you want to search:")
                    option=author
                    sM.searchBook(option)
                else:
                    print("Please Enter valide option")
            
                
            elif(choice==3):#Issue book
                bid=int(input("Enter Id of book which you want to issue: "))
                Fname=input("Enter your Full Name: ")
                date_issue=input("Enetr the date of book issue(yy-mm-dd): ")
                sM.IssueBook(bid,Fname,date_issue)
                
            elif(choice==4):#Return book
                bid=int(input("Enter Id no of book which you submit:"))
                Fname=input("Enter your Full Name: ")
                date_return=input("Enetr the date of book return(yy-mm-dd): ")
                sM.ReturnBook(bid,Fname,date_return)
            
            elif(choice ==5 ):            
                print("Thank you for visiting Library")
                break
            else:
                print("Please enter a valid choice from 1-5")            
        except ValueError:
            print("Please enter input as suggested.")
            

#***********************            
#Admin section
#***********************

else:    
    count=2    
    for i in range(0,count+1):
        u=input("Enter User Name: ")
        p=input("Enter Password: ")
        User_id="Library"
        password="Library@123"
        if (u==User_id and p==password):
            while(choice!=6):
                print("****************************************")
                print("----------------ADMIN MENU--------------")
                print("****************************************")
                print('''\t\t1.Add Book
                2.Show all Book
                3.Search Book          
                4.Edit Book
                5.Delete Book
                6.Exit ''')
                print("****************************************")
                try:
                    choice = int(input("Enter your choice from 1-6: "))
                    if(choice == 1):#Add book
                        bid = int(input("Enter Book ID: "))
                        bname = input("Enter Book Name: ")
                        author = input("Enter Book Author Name: ")            
                        avlbl= input("Enter Book is Available or Not: ")
                        b1 = Book(bid,bname,author,avlbl)   
                        bM.addBook(b1)
                        
                    elif(choice == 2):#Show all book
                        bM.ShowAllBook()
                        
                    elif(choice == 3):#search book
                        bid = int(input("Enter the id you want to search: "))
                        bM.searchBook(bid)
                        
                    elif(choice == 4):#Edit book
                        bid = int(input("Enter the id you want to edit: "))
                        bM.editBook(bid)
                        
                    elif(choice == 5):#Delete book 
                        bid = int(input("Enter the id you want to delete: "))
                        bM.deleteBook(bid)
                        
                    elif(choice == 6):
                        print("Thank you for using library management system")
                        break
                    else:
                        print("Please enter a valid choice from 1-6")
                except ValueError:
                    print("Please input as suggested.")
        else:
            i+=1
            print("Please enter valid ID and Pass")
        
