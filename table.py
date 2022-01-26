number = int(input("Enter your Number # "))
result = 1
if number % 2==0:
    with open("table.txt","w") as file:
        for i in range(1,11):
            result = number * i        
            file.write("{}*{}={}\n".format(number , i , result))
    file.close()