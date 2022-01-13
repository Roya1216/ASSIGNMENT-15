n = int(input("Please write how many numbers are in your array? "))

arr = []

for i in range(0,n) :

    txt = "Enter #"+str(i)+"  :  "

    arr.append(int(input(txt)))

arr2 = arr[::-1]

if arr2 == arr :

    print ("Positive")

else :

    print("Negative")