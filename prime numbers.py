#Take the input from the user:   
lower = 1  
upper = int(input("Enter upper range: "))  #code to enter till which number we want to find prime no.'s'
a= "abcd"
for i in a:
    print("*")
for x in range(lower,upper + 1):  #loop to read all no.'s till the entered no.
   if x > 1:   
       for i in range(2,x): #loop to divide all the no.'s till the entered no. by the no.'s before it  
           if (x % i) == 0: #if the remainder of the divison is 0 in any case when the no. is divided by the no.'s before it break this loop as it will not be a prime no. 
               break  
       else:  
           print(x) #if the remainder is non-zero in all case  then print that no. as it will be a prime no.
