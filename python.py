# PYTHON GİRİŞ DERSİ 1

###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

# tek satırlık yorum
''' 3 tirnak arasina istenilen uzunlukta yorum yazilir''' 

# print()
print("Hello, World!")

print('Hello World!')

print("Hello, World!",
      "I love programming",
      "Python")

print("Hello, World!", "I love programming", "Python")

print("Hello, World!\nI love programming python")


# Değişkenler 
name = "Python"
print(name)

# Sayılar: integer
number = 35
print(number)


print(type(name))  #veri tipini yazdırma
print(len(name)) #veri uzunluğunu yazdırma
 
# Sayılar: float
pi = 3.14
type(pi)


t, f = True, False
print(type(t))


# Matematiksel İşlemler

5**2
     
35+67

print(2 + 5)

"35"+"67"
     
"35" + 67 
     
"35"*3
     
"hello"*4
     

x = 10

print(x+2)
print(x-2)
print(x*2) # üssü
print(x**2) # karesi
print(x/2)
print(x//2) #bölümü verir
print(x%2) #bölümden kalanı verir

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 // 2 =", 5//2)
print("5 ** 2 =", 5**2)
print("5 % 2 =", 5%2)
     
     
y = 13
print(y//2)
print(y%2)
     

x = 5 # equivalent to x = 5
x += 5 # equivalent to x = x + 5
x -= 5 # equivalent to x = x - 5
x *= 5 # equivalent to x = x * 5
x /= 5 # equivalent to x = x / 5
x %= 5 # equivalent to x = x % 5
x //= 5 # equivalent to x = x // 5
x **= 5 # equivalent to x = x ** 5

z = 5
z+=1 # z= z+1 demek , z'nin eski değeri 5 iken yeni değeri 6 oldu.
z
     
# Sayılar (Numbers): int, float, complex

a = 5
b = 10.5

int(b) # Tipleri değiştirmek
float(a)

int(a * b / 10)

c = a * b / 10

int(c)



# mantıksal operatörler 
num1 = 10
num2 = 5

print(num1, ">", num2, "=", num1 > num2)
print(num1, ">=", num2, "=", num1 >= num2)
print(num1, "<", num2, "=", num1 < num2)
print(num1, "<=", num2, "=", num1 <= num2)
print(num1, "==", num2, "=", num1 == num2)
print(num1, "!=", num2, "=", num1 != num2)


# input()
y = input("Please enter a city name: ")  #input her zaman string alır
print("Hello", y)

number2 =int(input("Please enter a number: "))
print("This number is ", number2)


long_str = """artificial intelligence, machine learning, deep learning, computer, python"""
long_str[0]  #Karakter Dizilerinin Elemanlarına Erişmek
long_str[3]


long_str[0:3]   # Karakter Dizilerinde Slice İşlemi

"veri" in long_str  # String İçerisinde Karakter Sorgulamak



"python".upper()  # upper() & lower(): küçük-büyük dönüşümleri
"PYTHON".lower()



hi = "Hello AI Era"       # replace: karakter değiştirir
hi.replace("l", "p")


"Hello AI Era".split()   # split: böler

"python".capitalize()   # capitalize: ilk harfi büyütür


hello = "world"
hello[2:4]  # [x:y] --> x ten y. karaktere kadar al ama y. karakteri alma.


city = "istanbul"
city[0:6:2]  # [başlangıç:bitiş:step_sayısı]



# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.


my_list = ["python", "course", "hello", 3, 5, 6, 7]
my_list.append('computer')  # append() ile liste sonuna elemanlar ekleyebiliriz.
my_list.pop()  # pop() listenin son elemanını atar.
my_list.remove("course")
type(my_list)
print(my_list)



# Sözlük (Dictonary)

# Değiştirilebilir.
# Sırasız. (3.7 sonra sıralı.)
# Kapsayıcı.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"][1]



dictionary["REG"]   # Key'e Göre Value'ya Erişmek
dictionary.get("REG")


dictionary["REG"] = ["YSA", 10]  # Value Değiştirmek

dictionary.keys()  # Tüm Key'lere Erişmek

dictionary.values() # Tüm Value'lara Erişmek


dictionary.items()  # Tüm Çiftleri Tuple Halinde Listeye Çevirme

dictionary.update({"REG": 11})  # Key-Value Değerini Güncellemek

dictionary.update({"RF": 10})  # Yeni Key-Value Eklemek


# Demet (Tuple)

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)


# Set

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1