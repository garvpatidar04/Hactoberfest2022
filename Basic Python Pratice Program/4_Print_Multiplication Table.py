# program for operator overloading 
def Table(n):
    print('\n')
    for i in range(1,11):
        print('\t',n,' * ',i,' =  ',i*n);
    print('\n')


num = int(input("Enter a number for table: "))
Table(num)
