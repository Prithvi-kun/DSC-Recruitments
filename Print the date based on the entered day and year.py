'''
Print the date based on the entered day and year

Write a function that inputs two integers: the day number and the year. This function should 
generate a string that has the entire date with the date, month and year mentioned. Ensure that
the function also considers leap years.

Example Test Case:
Inputs:  256, 2021
Output: “13 September, 2021”

Answer:
'''

def calendar():
    year=int(input("Enter the year: "))
    day=int(input("Enter day: "))
    if (year%4==0):
        feb_days=29
    else:
        feb_days=28
    m_days=[31,feb_days,31,30,31,30,31,31,30,31,30,31]
    m= ["January","February","March","April","May","June","July","August","September","October","November","December"]
    xday=day
    for i in range(12):
        if xday<=m_days[i]:
            print(xday,m[i],year)
            break
        xday-=m_days[i]
calendar()

'''
Output:

Enter the year: 2024
Enter day: 60
29 February 2024
'''