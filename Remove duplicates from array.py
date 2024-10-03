'''
Remove duplicates from array

Write a function that inputs an array. This function should return an array that 
has the elements in the same order,but with each element appearing only once.
Assume the input array is already sorted.

Example Test Case: 
Input: [2,3,4,4,6,7,7]
Output: [2,3,4,6,7]  

Answer:
''' 

def dupe():
    inlist=list(input("Enter values: ").split())
    outlist=[]
    for i in inlist:
        if int(i) not in outlist:
            outlist.append(int(i))
    print(outlist)
dupe()

'''
Output:

Enter values: 2 3 4 4 5
[2, 3, 4, 5]
'''