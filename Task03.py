#Task03

#01 -Write a Python program to sum up all the items in a list.
x=[1,2,3,4,5,6]
i=0
sum=0
while i<len(x):
    print(x[i])
    sum+=x[i]
    i+=1
    print(f"Total :{sum}")


#02 - Write a Python program to get the largest number from a list.
x=[2,4,6,8,10]
i=0
max=0
while i<len(x):
    if max<x[i]:
     max=x[i]
    i+=1
print(f"max:{max}")


#03-Write a Python program to Count occurrences of an element in a list
x=[3,2,3,4,3,5,3]
i=0
num=3
count=0
while i<len(x):
    if num==x[i]:
        count+=1
    i+=1
print(f"count of {num} is {count}")



#04 -Write a Python program to Sum the number of digits in a list.
x=[123,456,789,12,34]
i=0
total_sum=0
while i<len(x):
    num=x[i]
    while num>0:
        total_sum+=num % 10
        num=num//10
        i+=1
print(f"sum of digits:{total_sum}")


#05 -Write a Python program to count Even and Odd numbers in a list.
x=[1,6,4,3,17,9,15]
even_count=0
odd_count=0
i=0
while i<len(x):
    if x[i]%2 == 0:
        even_count+=1
    else:
         odd_count+=1
    i+=1     
print(f"count of even number:{even_count}")
print(f"count of odd number:{odd_count}")



#06 -Write a Python program to print positive numbers in a list.

number=[1,-2,3,-4,5,-7,8,6]
i=0
while i<len(number):
    if number[i]>0:
        print(number[i])
    i+=1 

    
#07-Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Sample List : [ 'abc', 'xyz', 'aba', '1221' ] Expected Result: 2
sample_list=['abc','xyz','aba','1221']
count=0
i=0
while i < len(sample_list):
    s=sample_list[i]
    if len(s)>=2 and s[0] == s[-1]:
        count+=1
    i+=1
print("Numbers of string where the first and last characters are the same:",count)
    



#08-Write a Python program to remove duplicates from a list.
numbers=[1,2,4,3,7,2,3,8,9,10]
sample_set=set(numbers)
new_numbers=list(sample_set)
print(new_numbers)

#09 Write a Python program to print the numbers of a specified list after removing even numbers from it.
x=[1,2,3,4,5,6]
i=0
c=[]
l=[]
while(i<len(x)):
    if (x[i]%2==0):
        c.append(x[i])
    else:
        l.append(x[i])
    i+=1
print(f"{c}\n{l}")


