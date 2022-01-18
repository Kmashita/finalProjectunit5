#start time 9:40 
#solution to problem 1 

sum = 0

for i in range(1000):
    if i % 5 == 0 or i % 3 == 0: #modulus to see if the number is divisible by 5 or 3. 
        sum = sum + i
print(sum)

#solution to problem 2 (work in progress)

a = 1 
b = 2
c = 0 
sum = 0
result = 0
even = 0

while sum < 4000000: #the sum should always remain lower than 4 million as instructed. 
    sum = a+c 
    result = a+even 
    c = a+b
    if c % 2 == 0: #the number will always be even if the remainder is 0 after being divided by 2. 
        even = c
    else:
        even = 0
    a = b 
    b = c
    
print(result)

#end time is 10:30. Total: 50 minutes
