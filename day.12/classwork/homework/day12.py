print(int(5.7))       # 5, მრგვალდება ქვემოთ
print(int("42"))      # 42, სტრინგიდან მთელ რიცხვში გადაყვანა
print(int(True))      # 1, Boolean ტიპი True გადაყვანილია 1-ში
print(int(False))     # 0, Boolean ტიპი False გადაყვანილია 0-ში
print(int(-8.9))      # -8, მრგვალდება ქვემოთ
str (სტრინგში გადაყვანა)
python
Copy
Edit
print(str(123))       # '123', რიცხვი გადაყვანილია ტექსტში
print(str(5.7))       # '5.7', float გადაყვანილია ტექსტში
print(str(True))      # 'True', Boolean ტიპი გადაყვანილია ტექსტში
print(str(None))      # 'None', None ტიპი გადაყვანილია ტექსტში
print(str(-42))       # '-42', უარყოფითი რიცხვი გადაყვანილია ტექსტში
float (მცურავი წერტილით რიცხვში გადაყვანა)
python
Copy
Edit
print(float(5))       # 5.0, მთელ რიცხვი გადაყვანილია float-ში
print(float("3.14"))  # 3.14, ტექსტი გადაყვანილია float-ში
print(float(True))    # 1.0, Boolean True გადაყვანილია float-ში
print(float(False))   # 0.0, Boolean False გადაყვანილია float-ში
print(float("-2.5"))  # -2.5, სტრინგი გადაყვანილია float-ში
2) რა დროს გვჭირდება მონაცემთა ტიპის კონვერტაცია?
მონაცემთა ტიპის კონვერტაცია საჭიროა მაშინ, როდესაც:

განსხვავებული ტიპის მონაცემები უნდა ერთად გამოვიყენოთ (მაგ., სტრინგი და რიცხვი).
საჭირო ხდება მონაცემების შესატყვის ფორმატში გამოყენება (მაგ., ტექსტიდან რიცხვში გადაყვანა არითმეტიკული ოპერაციებისათვის).
ფუნქციები ითხოვენ სპეციფიკურ ტიპს (მაგ., int ტიპის მნიშვნელობა ლუპში ან float ტიპის მნიშვნელობა პროცენტების გამოთვლისთვის).
მონაცემები შეგვყავს მომხმარებლისგან (ტექსტი უნდა გადავიყვანოთ რიცხვში).
3) სამი ასაკის საშუალო არითმეტიკული
python
Copy
Edit
# ასაკების შეყვანა
age1 = int(input("შეიყვანეთ პირველი ადამიანის ასაკი: "))
age2 = int(input("შეიყვანეთ მეორე ადამიანის ასაკი: "))
age3 = int(input("შეიყვანეთ მესამე ადამიანის ასაკი: "))

# საშუალო არითმეტიკული
average_age = (age1 + age2 + age3) / 3
print(f"სამი ადამიანის ასაკის საშუალო არითმეტიკული არის: {average_age}")
4) მომხმარებლის ასაკი 20 წელში
python
Copy
Edit
# ასაკის შეყვანა
current_age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# ასაკი 20 წელში
age_in_20_years = current_age + 20
print(f"20 წელში თქვენ იქნებით: {age_in_20_years} წლის.")
5) 6 შედარების ოპერატორები ცვლადებით
> (მეტი ვიდრე)
python
Copy
Edit
a, b = 10, 5
print(a > b)   # True
print(b > a)   # False
print(a > 0)   # True
print(b > -1)  # True
print(0 > a)   # False
< (ნაკლები ვიდრე)
python
Copy
Edit
a, b = 10, 20
print(a < b)   # True
print(b < a)   # False
print(a < 30)  # True
print(15 < b)  # True
print(-5 < a)  # True
>= (მეტი ან ტოლი)
python
Copy
Edit
a, b = 10, 10
print(a >= b)   # True
print(b >= 5)   # True
print(a >= 15)  # False
print(10 >= a)  # True
print(8 >= b)   # False
<= (ნაკლები ან ტოლი)
python
Copy
Edit
a, b = 7, 10
print(a <= b)   # True
print(b <= 5)   # False
print(a <= 7)   # True
print(0 <= a)   # True
print(15 <= b)  # False
!= (არ არის ტოლი)
python
Copy
Edit
a, b = 5, 8
print(a != b)   # True
print(a != 5)   # False
print(b != 0)   # True
print(a != -5)  # True
print(8 != b)   # False
== (ტოლი)
python
Copy
Edit
a, b = 12, 12
print(a == b)   # True
print(a == 10)  # False
print(b == 12)  # True
print(0 == a)   # False
print(a == a)   # True