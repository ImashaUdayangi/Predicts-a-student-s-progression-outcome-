# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221357,w1956115
# Date: 14/12/2022


#Creating Variables
p = 0
r = 0
s = 0
t = 0

#Creating list
input_data = []

#Creating text file
text = open("textfile.txt" , "w")


#Checking whether student or staff 
option = None
while True :
    try:
        option = int(input("Enter 1 for student and 2 for staff: "))
    except:
        print("Invalid option")
        continue
    if option == 1 or option == 2:
        break
    else:
        print("Invalid option")
        continue


while True:
    while True:
        try:
            crt_pass = int(input("\nPlease enter your credits at pass:"))
            if crt_pass not in range(0,121,20):
               print("Out of range")
               continue
        except ValueError:
            print("Integer required")
            continue
        break

    while True:
        try:
            crt_defer = int(input("Please enter your credits at defer:"))
            if crt_defer not in range(0,121,20):
               print("Out of range")
               continue
        except ValueError:
            print("Integer required")
            continue
        break
        

    while True:
        try:
            crt_fail = int(input("Please enter your credits at fail:"))
            if crt_fail not in range(0,121,20):
               print("Out of range")
               continue
        except ValueError:
            print("Integer required")
            continue
        break
 
    total = crt_pass + crt_defer + crt_fail #Checking the total
    if total != 120:
        print('Total incorrect')
        continue
    else:
        if crt_pass == 120:
            p += 1
            progression = "Progress"
        elif crt_pass == 100:
            r += 1
            progression = "Progress(module trailer)"
        elif crt_pass <= 80 and crt_defer <= 120 and crt_fail <=60:
            s += 1
            progression = "module retriever"
        elif crt_pass <= 40 and crt_defer <= 40 and crt_fail <= 120:
            t += 1
            progression = "Exclude"

    print(progression)
    if option == 1:
        break
    results = (f"{progression} - {crt_pass} , {crt_defer} , {crt_fail}")
    input_data.append(results)
    text.write(f"{results}\n")


    #Checking the user input     
    repeat = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    if repeat.lower() == "y":
        continue
    elif repeat.lower() == "q":
        #Histogram
        print("-"*75)
        print("Histogram")
        print("Progress" , p , " :" , "*"*p , end='')
        print()
        print("Trailer" , r , "  :" , "*"*r , end='')
        print()
        print("Retriever" , s , ":" , "*"*s , end='')
        print()
        print("Excluded" , t , " :" , "*"*t , end='')
        print()
        print()
        print((p + r + s + t) ,"outcomes in total")
        print("-"*75)
        break
    else:
        print("\nInavalid Input")
        print("Please enter only 'y' and 'q'")
        repeat = str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"))
        continue

for i in input_data:
    print(i)

text.close() #closing text file
