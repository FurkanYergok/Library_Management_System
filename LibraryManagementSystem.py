class Library:
    def __init__(self):
        self.txtfile=open("books.txt","a+",encoding="utf-8")
        #This is the constructer method which we use for creating and changing the file.
    def __del__(self):
        self.txtfile.close()
        #This method is used for closing the created file, so it is a destructor.
    def list_books(self):
        self.txtfile.seek(0)#By using this line, we start at the end of the file.
        reader = self.txtfile.readlines() #We read the file lines
        #print(reader) We used those lines for testing.
        datalist=list()
        #We've created an empty list above to hold the information
        for i in reader:
            temp=i.splitlines()
            for j in temp:
                datalist.append(j.split(","))
            #The code above first creates a list from the strings in a list, and after that in those list splits the elements by using split() if there is a "," between those elements.
            #We used .splitlines() because it was asked for us to use it.
        ct=1#This is the counter to print the book number
        for i in datalist:
            print(f"Book number: {ct}")
            print("Book Title: ",i[0])
            print("Author: ",i[1])
            print("Release date: ", i[2])
            print("Page count: ",i[3])
            print("\n")
            ct+=1
            
    def add_book(self):
        title = input("Enter the title of the book:\n")
        author = input("Enter the author of the book:\n")
        release_date = input("Enter the first release year:\n")
        pages = input("Enter the number of pages in that book:\n")
        #After getting the info we create a string to write to the file.
        wholestring = title+","+author+","+release_date+","+pages+"\n"
        self.txtfile.write(wholestring)
        
    def remove_book(self):
        self.txtfile.seek(0)
        title = input("Enter the title of the book which you want to remove:\n")
        reader = self.txtfile.readlines()
        booklist=list()
        #First we ask for the title, and read the file.
        for i in reader:
            temp=i.strip("\n")
            booklist.append(temp.split(","))#Same thing we did in the list_books() section but We used a different method; because, it felt easier to use
        counter=0#This variable is used for getting the index of the title in the nested list which we've created
        status = 0#We used this variable to check that if the searched title is in the list.
        for i in booklist:
            if title in i:
                status = 1
                a = i.index(title)#We found the index of the book first
                booklist[counter].pop(a)#After that we removed the title of the book first and after that the whole information about the book was removed.
                print(f"index of the given book is: booklist[{counter}][{a}](it is in a nested list)")
                booklist.pop(counter)
                break
            counter+=1
        #At below, we inform the user if the book is not found in the list.
        if status ==0:
            print("\nThe book has not found.\n")
        self.txtfile.truncate(0)
        for i in booklist:
            newstring=""
            #An empty string which we use for writing to the file
            ct=0
            #In this section we've used a counter variable to check if the iteration is made for 4 times. Because all the books have the same type of info. Title,Author,Date,Page.
            for j in i:
               newstring+=j 
               ct+=1
               if ct!=4:
                   #If the counter is not 4 that means all the infos are not completed for a book. Therefore we seperate them by using ,
                   newstring+=","
               if ct==4:
                   #When the counter variable becomes 4, we use \n to create a new line. By using that we can hold the information more readable.
                   newstring+="\n"
                   self.txtfile.write(newstring)
                   newstring
                   
        
lib = Library()
#In the last section We created an user interface to do some operations, which are listing the books, adding a new book, removing a book by using the title of the book and exiting the interface by using q which was requested from us by our mentors.
while True:
    print("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\nEnter q to terminate the program(enter it in lowercase)\n")
    operation=str(input("Enter the number of the operation you want to do:\n"))
    if operation=="1":
        lib.list_books()
    elif operation=="2":
        lib.add_book()
    elif operation=="3":
        lib.remove_book()
    elif operation == "q":
        print("Program successfully terminated.")
        #By entering q, we break the while loop by using break and ending the app.
        break
    else:
        #If the user enters something invalid, we inform the user to try again
        print("This was an invalid operation. Enter numbers between 1 and 3(both are included) or enter q to terminate the program.\n")
           
            
        