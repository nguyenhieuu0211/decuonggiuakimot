#input: nhập vào ba cạnh của một tam giác
#output: chu vi và diện tích của tam giác đó
a=int(input('Mời bạn nhập cạnh a: '))
b=int(input('Mời bạn nhập cạnh b: '))
c=int(input('Mời bạn nhập cạnh c: '))
#a,b,c =map(int,input('Mời bạn nhập ba cạnh của tam giác:').split())
if a<=0 or b<=0 or c<=0:
    print(a,b,c,'không phải là cạnh của một tam giác')
if a+b<=c or a+c<=b or a+b<=c:
    print(a,b,c,'không phải là cạnh của một tam giác')
if a+b>c or a+c>b or b+c>a and a>0 and b>0 and c>0:
    cv= a+b+c
    p=cv/2
    s=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print('chu vi của tam giác là: ',cv)
    print('diện tích của tam giác là: ',s)
#end