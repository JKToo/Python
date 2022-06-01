#Name: Justin K Too
#Email: justin.too27@myhunter.cuny.edu
#This program takes user input and turns it into a pyramid

s = input("Enter a string ")
ls = len(s)
for i in range(0, ls-1):
    print(s[0:i])

for i in range(0, ls-1):
    print(s[i:ls])

print("Thank you for using my program!")
