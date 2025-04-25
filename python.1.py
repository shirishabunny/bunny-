#python program to print the fibonacci sequence using while loop
n_terms =int(input("enter the n_terms of fibonaci terms to display:"))
#first two terms
a,b=0,1
count=0
#check if the number of terms is vaild
if n_terms<=0:
   print ("please enter a positive integer.")
elif n_terms==1:
   print("fibonaci sequence:")
   print(a)
else:
   print ("fibonacci sequence:")
while count <n_terms:
   print(a,end="")
   #update values
   a,b=b,a+b
   count+=1


           
