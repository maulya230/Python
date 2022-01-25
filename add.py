#Write python code to add the entered digits of a specific number using function

def sum(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    print(sum)

n=int(input("Enter the number: "))
sum(n)
