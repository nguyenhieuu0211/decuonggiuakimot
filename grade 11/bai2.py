#input: nhập hai số a và b trong pt ax+b=0
#output: nghiệm của phương trình ax+b=0
print('giải phương trình bậc nhất: ax+b=0')
a=int(input('Mời bạn nhập a: '))
b=int(input('Mời bạn nhập b: '))
if a==0 and b==0:
    print('Phương trình vô số nghiệm')
if a==0 and b!=0:
    print('Phương trình vô nghiệm')
if a!=0:
    x=(-b)/a
    print('Nghiệm của phương trình là:', x)