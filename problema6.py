n=2398
x=n%10
y=(n%100)//10
z=(n%1000)//100
q=n//1000
w=1000*x+100*y+10*z+q
print(x,"ultima cifră a numărului n")
print(y,"penultima cifră a numarului n")
print(n//9,"cîtul împărțirii la 9")
print(n%9,"restul împărțirii la 9")
print(x+y+z+q,"suma cifrelor numărului n")
print(w,"răsturnatul numărului")