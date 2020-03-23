x = int(input("Inserire un numero "))
if x % 2 == 0:
    print("il numero che hai inserito è pari")
else:
    ("il numero che hai inserito è dispari")
print(x*2, " questo è il doppio del numero che hai inserito")
print(x/2, " questa è la metà del numero che hai inserito")
f = 1
for e in range(1, x+1):
    f*= e
print("{} è il fattoriale di {}".format(f, x))
