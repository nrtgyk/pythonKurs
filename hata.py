#a= int("asdfg1234")
#print(a)
"""
try:
    a=int("1234")
    print("program burada")
except:
    print("bir hata oluştu")
print("bloklar sona erdi")"""

try:
    a=int(input("sayı 1: "))
    b=int(input("sayı 2: "))
    print(a/b)
except ValueError:
    print("lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("bir sayı 0'a bölünemez")
finally:
    print("burası çalştı")
print("bloklar sona erdi.")