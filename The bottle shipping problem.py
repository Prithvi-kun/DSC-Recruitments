'''
The bottle shipping problem

A company manufactures packing cartons in four sizes: small, medium, large and xl. 
These cartons can hold 6 bottles, 12 bottles, 24 bottles and 48 bottles respectively.
Write a function that inputs the number of bottles to be shipped by the company. 
The function should print the break-up of the number of cartons used in descending order of capacity.

Example Test Case:
Input: 140
Output: 2 xl, 1 large, 1 medium, 1 small

Answer:
'''

def carton():
    bottles=int(input("Enter number of bottles: "))
    s,m,l,xl=6,12,24,48
    no_xl=no_l=no_m=no_s=0
    while bottles>=s:
        if (bottles>=xl):
            no_xl=bottles//xl
            bottles-=(no_xl*xl)
        elif (bottles>=l):
            no_l=bottles//l
            bottles-=(no_l*l)
        elif (bottles>=m):
            no_m=bottles//m
            bottles-=(no_m*m)
        elif (bottles>=s):
            no_s=bottles//s
            bottles-=(no_s*s)
            if (bottles==0):
                pass
            elif (bottles>0):
                no_s+=1
        else:
            break
    print(no_xl,"xl,",no_l,"large,",no_m,"medium and",no_s,"small")
carton()

'''
Output:

Enter number of bottles: 69
1 xl, 0 large, 1 medium and 1 small
'''
