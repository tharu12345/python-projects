num = int (input("Enter Your Marks: "))
if 200 >= num >= 0:
    if num >= 175:
        print ("a")
    elif num >= 150:
        print("b")
    elif num >= 100:
        print("c")
    else:
        print("Fail")

else:
    print("Invalid Marks")
