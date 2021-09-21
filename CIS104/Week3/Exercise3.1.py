hr = input("Enter Hours:")
rt = input("Enter Rate:")
Fhr = float(hr)
Frt = float(rt)
if Fhr > 40 :
    Rpay = Fhr * Frt
    Opay = (Fhr - 40.0) * (Frt * 0.5)
    pay = Rpay + Opay
else:
    pay = Fhr * Frt
print("Pay:", pay)
