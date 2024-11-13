############################  Working with variables
# greeting = "Hello world"
# print(greeting)
# message = "You shouldn't give up"
# print(message)
# message = "Try to study hard"
# print(message)
# subject = "Artificial Intelligence"
# print(subject)
#
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

############################  Working with string
# street = "Baraka"
# district = "Marshal"
# region = "Andijan"
# print(f"{street} street, {district} district, {region} region")
# street = input("Enter your street\n")
# district = input("Enter your district\n")
# region = input("Enter your region\n")
# print(f"My street is {street}\n my district is {district}\n my region is {region}")

############################## Working with numbers
# num = int(input("Enter any number "))
# num1 = num**2
# num2 = num**3
# print(f"{num} ning kvadarti {num1} ga teng,\n{num} ning kubi {num2} ga teng")

# age = int(input("How old are you? "))
# birth_year = 2024 - age
# print(f" You are {birth_year} ")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print(f"{num1} + {num2} = {num1+num2} \n{num1} - {num2} = {num1-num2} \n{num1} * {num2} ={num1*num2} \n{num1} / {num2} {num1/num2}")

######################Working with lists

# names = ['Manzura', 'Ziyoda', 'Munisa']
# print("Salom", names[1], "what do your plan for today? ")
# print("Salom", names[0], "Would you like to learn coding?")
# print("Salom", names[2], "What kind of books do you like?")

# numbers = [3, 5, 7, 12, -34]
# print(numbers)
# numbers[3] = numbers[1] + numbers[3]
# numbers[0] = numbers[3] + numbers[4]
# print(numbers)
#
# historic_persons = ['Amir Temur', "Alisher Nvoiy", "Bobur"]
# modern_persons  = ["Ilon Mask", "Bill Geyts"]
# print("I wanna talk to from historic people", historic_persons.pop(1), "and from modern people", modern_persons.pop(1))
#
# friends = []
# friends.append('Sarvinoz')
# friends.append('Dilnoza')
# friends.append('Gulnoza')
# friends.append('Mushtariy')
# print(friends)
# friends.remove('Gulnoza')
# friends.remove('Mushtariy')
# print(friends)
# friends.append("Durdona")
# friends.insert(2, "Kumush")
# friends.insert(0, "Diyora")
# print(friends)
#
# guests = []
# guests.append(friends.pop(2))
# guests.append(friends.pop(0))
# print(f"Guests are{guests}")


########################### Tuples


# country = ['USA', 'UK', 'Canada', 'Germany', 'Uzbekistan']
# print(len(country))
# print(sorted(country))
# print(sorted(country, reverse=True))
# country.reverse()
# print(country)
# country.sort()
# print(country)
# country.sort(reverse=True)

# country1 = country #(bu nusxa olish emas shuunchaki bitta dataga 2ta nom berib qo'ydik
# print(country)
# print(country1)
# country1.remove('Germany')
# print(country1)
#
# country1 = country[:] #bu nusxa olish

########################### for tsikl

# guests = ['John', 'Lily', 'Lucy', 'Maria', 'Steysi']
#
# for guest in guests:
#     print('Welcome', guest)

# meals = []
# print('What is your 5 meals do you like? ')
# for i in range(5):
#     meals.append(input(f"Enter your {i+1} - meals : "))
# print(meals)


# hobbies = []
# print('What is your 5 hobbies do you like? ')
# for hobby in range(3):
#     hobbies.append(input(f"Enter your {hobby+1} - hobbies do you like most: "))
# print(hobbies)

########################### if-elsee

# universities = ['Turin', 'Cambridge', 'Oxford', 'Harward', 'Idu']
# for university in universities:
#     if university == 'Idu':
#         print(university.upper())
#     else:
#         print(university.title())

# login = input('Enter a new login: ')
# if len(login) <= 4:
#     print("Login must be 4 letter")

#
# employees = {
#     'durdona': 'logist',
#     'mahliyo': 'operator',
#     'shodiya' : 'manager',
#     'gulbahor': 'hr'
# }
#
# for key, value in employees.items():
#     print(f"{key.title()} work as a {value.title}")

# book_list = {
#     'november': 'bir olima qiz bor edi',
#     'december': 'yashamoq',
#     'january': 'marketing'
# }
# for key, value in book_list.items():
#     print(f"I wanna read { value.capitalize()} in {key.title()} ")

# employees = {
#     'durdona': 'logist',
#     'mahliyo': 'operator',
#     'shodiya': 'manager',
#     'gulbahor': 'hr',
#     'diyora': 'logist',
#     'ruxshona' : 'operator'
# }
# for employee in set(employees.values()):
#     print(employee.title())

# item0 = {
#     'item': 'pen',
#     'color': 'black',
#     'price': 10000
# }
#
# item1 = {
#     'item': 'notebook',
#     'color': 'pink',
#     'price': 50000
# }
#
# item2 = {
#     'item': 'jewelry',
#     'color': 'gold',
#     'price': 65000
# }
#
# item3 = {
#     'item': 'bag',
#     'color': 'brown',
#     'price': 250000
# }

# items = [item0, item1, item2, item3]
# for item in items:
#     print(f"This: {item['item'].title()}, "
#           f"color: {item['color']}, "
#           f"price: {item['price']} ")

###########################input() va while

# names = []
# n = 1
# while True:
#     question = f"Enter your {n} - brother: "
#     name = input(question)
#     names.append(name)
#     question1 = input("Would you like to add? yes/no ")
#     n+=1
#     if question1 != 'yes':
#         break
# print("Your brothers: ")
# for name in names:
#     print(name.title())


# items = []
# n = 1
# while True:
#     question = f"Enter {n} the important thing: "
#     item = input(question)
#     items.append(item)
#     question1 = input("Would you like to add? yes/no ")
#     if question1 != 'yes':
#         break
#     n+=1
#
# print("Your important things: ")
# for item in items:
#     print(item.title())

# subjects = []
# n=1
# while True:
#     question = f"Enter your {n} subject: "
#     subject = input(question)
#     subjects.append(subject)
#     n+=1
#     question1 = input("Do you want to add more subjects? yes/no ")
#     if question1 != 'yes':
#         break
#
# print("Your subjects are: ")
# for subject in subjects:
#     print(subject.title())


# subjects = {}
# while True:
#     name = input(f"Enter your subject's name: ")
#     grade = int(input(f"Enter {name.title()} 's grade"))
#     subjects[name] = grade
#
#     question = input("Do you want to add more subjects? yes/no ")
#     if question != 'yes':
#         break
# for name, grade in subjects.items():
#     print(f"You got {grade} from {name}")
#
# students = ["Sanjar", "Mirjalol", "Lutfullo", "Asilbek"]
# paid_students = {}
# while students:
#     student = students.pop()
#     paid = input(f"{student}, have you paid the fees? (yes/no): ").lower()
#     if paid == 'yes':
#         print(f"{student.title()} paid")
#     else:
#         print(f"{student.title()} not paid")
# print(paid_students)


############Function

# def greeting(name):
#     print(f"Hello, Welcome to our event {name.title()}")
#
# greeting('Bargida')


# def calculate_two_number(num1, num2):
#     print(f"Result of two numbers {num1 +num2}")
#
# calculate_two_number(3, 5)
#
# def full_name(name, surname = 'Tilyakova'):
#     print(f"Your name is {name}  \n"
#           f"Your surname is {surname}")
#
# full_name('Bargida')

# def age_of_your(year, this_year=2024):
#     print(f"Your are {this_year - year}")
#
# age_of_your(1997)
# age_of_your(1989)

# def item_info(product, price, color):
#     item = { 'product': product,
#              'price': price,
#              'color': color
#     }
#     return item
#
# print(f"We're gonna make some product's list")
#
# items = []
# while True:
#     product = input("Enter product : ")
#     price = int(input("Enter product's price: "))
#     color = input("Enter product's color: ")
#     items.append(item_info(product, price, color))
#
#     question = input("Would you like to add something?  yes/no: ")
#     if question == 'no':
#         break
# for item in items:
#     if item['price']:
#         price = int(item['price'])
#     else:
#         price = ''
#     print(f"{item['color'].title()} Narhi : {price} ")

############ Funksiyaga ro'yxat uzatish

# def bahola(names):
#     grades = {}
#     while names:
#         name = names.pop()
#         grade = int(input(f"Enter {name.title()}'s grade : "))
#         grades[name] = grade
#     return grades
#
# students = ["John", "Lucy", "Lily", "Steysi"]
# grades = bahola(students)
# print(grades)

# def colleagues_age(names):
#     ages = {}
#     while names:
#         name = names.pop()
#         age = int(input(f"Enter colleagues's {name.title()}: "))
#         ages[name] = age
#     return ages
#
#
# colleagues = ["Sam", "John", "Lucy"]
# ages = colleagues_age(colleagues)
# print(ages)

