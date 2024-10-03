'''
Arrange words in a string in the order of their length

Write a function that inputs a string. The function should return the string sorted in ascending order of the length of the words.

Example Test Case:
Input: "This is a cool sentence"
Output: "a is this cool sentence" 

Answer: 
'''

def asc():
    a=input("Enter a sentence: ")
    words=a.split()
    sort=sorted(words,key=len)
    end=' '.join(sort)
    print(end)
asc()

'''
Output:

Enter a sentence: Why so serious?
so Why serious?
'''
