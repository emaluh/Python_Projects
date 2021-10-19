n1=int(input('Введіть кількість навчальних предметів='))
a1=0
i=0
while i<n1:
    x=int(input(':'))
    a1+=x
    i+=1
print(a1/n1)





n = int(input())
a = []
for i in range (n):
 x = int(input())
 a.append(x)
print(sum(a)/len(a))
