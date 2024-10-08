'''
Design your own Stack

The stack should have three functions: push(int), pop() and peek(). 
You are only allowed to use Arrays or Linked Lists.

Answer: 
'''

command=input("Enter command (Push/Pull/Pop): ")
class stack:
    exlist=[]
    def push(self,a):
        S.exlist.append(a)
    def pops(self):
        S.exlist.pop()
    def peek(self):
        print("The last value:",S.exlist[-1])
S=stack()
x="y"
while (x.lower()=="y"):
    if (command.lower()=="push"):
        a=int(input("Enter a value to add: "))
        S.push(a)
        print("List:",S.exlist)
    elif (command.lower()=="pop"):
        if len(S.exlist)>0:
            S.pops()
            print("List after popping:",S.exlist)
        else:
            print("Nothing there to delete")
    elif (command.lower()=="peek"):
        if len(S.exlist)>0:
            S.peek()
        else:
            print("Nothing there to see")
    x=input("Continue? (Y/N): ")
    if (x.lower()=="y"):
        command=input("Enter command (Push/Peek/Pop): ")
    else:
        break

'''
Output:

Enter command (Push/Pull/Pop): push
Enter a value to add: 1
List: [1]
Continue? (Y/N): y
Enter command (Push/Peek/Pop): push
Enter a value to add: 2
List: [1, 2]
Continue? (Y/N): y
Enter command (Push/Peek/Pop): peek
The last value: 2
Continue? (Y/N): y
Enter command (Push/Peek/Pop): pop
List after popping: [1]
Continue? (Y/N): y
Enter command (Push/Peek/Pop): pop
List after popping: []
Continue? (Y/N): y
Enter command (Push/Peek/Pop): peek
Nothing there to see
Continue? (Y/N): y
Enter command (Push/Peek/Pop): pop
Nothing there to delete
Continue? (Y/N):n
'''

