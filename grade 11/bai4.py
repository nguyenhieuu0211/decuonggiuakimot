#input: nhập vào hai số nguyên dương m và n
#output: kiểm tra m có chia hết cho n không
m=int(input('Mời bạn nhập m: '))
n=int(input('Mời bạn nhập n: '))
if m%n==0:
    print('YES')
if m%n!=0:
    print('NO')
#end