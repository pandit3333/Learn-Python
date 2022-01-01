#cost of shipping
charge = True

#Entering the total amount
totalAmount = int(input("Enter the amount of your total purchase \n$"))

if totalAmount >= 100 :
    charge = False
    print("Your shipping is free.")

else :
    charge = 10
    print("$10 is added in your purchase for shipping.")

#Calculating total amount adding shipping charge
Amount = str(totalAmount + charge)
print("The total cost you need to pay is $" + Amount) 