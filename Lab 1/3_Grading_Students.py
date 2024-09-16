m1=int(input("Enter your marks "))
m2=int(input("Enter your marks "))
m3=int(input("Enter your marks "))
m4=int(input("Enter your marks "))
m5=int(input("Enter your marks "))
tp=(100*((m1+m2+m3+m4+m5)/500))
if(tp>=90 and tp<=100):
    print("Ex")
elif(tp>=80 and tp<=90):
    print("A")
elif(tp>=70 and tp<=80):
    print("B")  
elif(tp>=60 and tp<=50):
    print("C")  
elif(tp<=50):
    print("F")       