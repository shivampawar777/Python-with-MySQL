from dbConnect import Student

def main():
    stud = Student()
    
    while True:
        print("\n*****Eneter the choice*****")
        print("1.Insert the data")
        print("2.Update the data")
        print("3.Delete the data")
        print("4.Displat the data")
        print("5.Break")
        print("\n")

        try:
            ch = int(input())
            
            if(ch==1):
                print("Data added")
            elif(ch==2):
                print("Data updated")
            elif(ch==3):
                print("Data deleted")
            elif(ch==4):
                print("Data printed")
            elif(ch==5):
                break
            else:
                print("Please enter valid input")
        except Exception as e:
            print(e)        



if __name__ == "__main__":
    main()
