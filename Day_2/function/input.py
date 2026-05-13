import aritmatika as f


berat = float (input("Masukkan berat badan : "))
tinggi = float (input ("Masukkan tinggi badan : "))

#print("berat", berat)
#print("tinggi saya", tinggi)


bmi = f.bmi(berat, tinggi)
print("BMI Anda adalah:", bmi)

bmi_check = f.bmi_check(bmi)