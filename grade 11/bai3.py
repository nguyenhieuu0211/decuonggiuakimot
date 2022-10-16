#intput: nhập hai số a và b
#output: nghiệm của phương trình bậc hai
print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
'''if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:''' 
delta = (b**2)-(4*a*c)
if delta >0:
    x1=(-b - (delta)**(1/2))/(2*a)
    x2=(-b + (delta)**(1/2))/(2*a)
    print('phương trình có hai nghiệm: ',x1,'và',x2)
if delta==0:
    x3=(-b)/(2*a)
    print('phương trình có nghiệm kép là:', x3)
if delta <0:
    print('phương trình vô nghiệm')
#end



