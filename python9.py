a=int(input("Δώσε εναν αριθμό:"))
a=a*3+1
digits=[int(x) for x in str(a)]
for i in range (len(digits)-1):
    a=sum(digits)
    digits=[int(x) for x in str(a)]
print (a)
