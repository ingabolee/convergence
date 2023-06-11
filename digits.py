

def product_of_digits(n):
    prod = 1
    for i in str(n):
        if i == '0' or i == '1':
            pass
        else:
            prod *= int(i)
    if len(str(prod)) == 1:
        return prod
    else:
        return product_of_digits(prod)

count1 = 0; count2 = 0; count3 = 0; count4 = 0; count5 = 0; count6 = 0; count7 = 0; count8 = 0; count9 = 0  
for i in range(1,100000000):
    #print(i, " converges to: ", product_of_digits(i))
    if product_of_digits(i) == 1:
        count1+=1
    elif product_of_digits(i) == 2:
        count2+=1
    elif product_of_digits(i) == 3:
        count3+=1
    elif product_of_digits(i) == 4:
        count4+=1
    elif product_of_digits(i) == 5:
        count5+=1
    elif product_of_digits(i) == 6:
        count6+=1
    elif product_of_digits(i) == 7:
        count7+=1
    elif product_of_digits(i) == 8:
        count8+=1
    elif product_of_digits(i) == 9:
        count9+=1

print(
    "1: ", count1, 
    "\n2: ", count2, 
    "\n3: ", count3, 
    "\n4: ", count4, 
    "\n5: ", count5, 
    "\n6: ", count6, 
    "\n7: ", count7, 
    "\n8: ", count8, 
    "\n9: ", count9, 
)
