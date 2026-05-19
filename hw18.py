#1. Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

    #2. Largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

    #3. Reverse a string
string = input("Enter a string: ")
reversed_string = string[::-1]  
print("Reversed string:", reversed_string)

# 4.Count vowels in a string
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'   
count = 0
for char in string:
    if char in vowels:
        count += 1  
print("Number of vowels in the string:", count)

# 5.Multiplication table (up to 10)
num = int(input("Enter a number: "))
print("Multiplication Table of", num)   
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    # 6.Fibonacci sequence (n terms)
n = int(input("Enter the number of terms: "))
a, b = 0, 1 
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

    # 7.Palindrome check
string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome") 
else:    print("Not a palindrome")

    # 8.Word frequency in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()    
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1  
    else:
        frequency[word] = 1
print("Word Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

    # 9.Prime numbers in a range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))    
print("Prime numbers in the range:")
for num in range(start, end + 1):   
    if num > 1:  
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

    #10. To-Do List (console app)
tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")

    elif choice == "3":
        print("Tasks:")
        for t in tasks:
            print("-", t)

    elif choice == "4":
        break

    else:
        print("Invalid choice")







