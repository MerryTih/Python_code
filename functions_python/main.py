######### 1 ##########

# def print_alphabet(case):
#     if case.islower():
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     elif case.isupper():
#         alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     else:
#         print("Incorrect data entry. Please enter a lowercase or uppercase letter")
#         return
#     print(', '.join(alphabet))

# user_input = input("Type an uppercase letter to output uppercase letters or a lowercase letter to output lowercase letters:")
# print_alphabet(user_input)

######### 2 ###########

# def print_alphabet(case):
#     if case.islower():
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     elif case.isupper():
#         alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     else:
#         print("Incorrect data entry. Please enter a lowercase or uppercase letter")
#         return
#     print(', '.join(alphabet[alphabet.index(case):]))

# user_input = input("Type an uppercase letter to print uppercase letters or a lowercase letter to print lowercase letters:")
# print_alphabet(user_input)

######### 3 ##########

# def count_words(sentence):
#     space_count = sentence.count(' ')
#     word_count = space_count + 1
#     return word_count

# user_input = input("Введіть рядок із слів, розділених пробілами: ")

# word_count = count_words(user_input)
# print("Кількість слів в рядку:", word_count)

# def count_words(sentence):
#     words = sentence.split()
#     return len(words)

# text = "Еней був парубок моторний.    І хлопець хоч куди козак"

# word_count = count_words(text)
# print("Кількість слів в рядку:", word_count)

########## 4 #########

# def extract_domain(email):
#     username, domain = email.split('@')
#     return domain

# user_email = input("Введіть адресу електронної пошти: ")

# domain = extract_domain(user_email)
# print("Доменне ім'я сервера:", domain)

######## 5 #########
# якщо всі дані були введені з малої букви - перетворити перші літери слів на великі

# def format_name(surname, name, patronymic):
#     formatted_surname = surname.capitalize()
#     formatted_name = name.capitalize()
#     formatted_patronymic = patronymic.capitalize()
#     return formatted_surname, formatted_name, formatted_patronymic

# surname = input("Введіть ваше прізвище: ")
# name = input("Введіть ваше ім'я: ")
# patronymic = input("Введіть ваше по-батькові: ")

# formatted_surname, formatted_name, formatted_patronymic = format_name(surname, name, patronymic)
# print("Відформатовані дані:")
# print("Прізвище:", formatted_surname)
# print("Ім'я:", formatted_name)
# print("По-батькові:", formatted_patronymic)

######## 6 ########
# перетворення Сидоров Іван Миколайович на Сидоров І.М.

# def format_initials(surname, name, patronymic):
#     initials = surname.title() + ' ' + name[0].upper() + '. ' + patronymic[0].upper() + '.'
#     return initials

# surname = input("Введіть ваше прізвище: ")
# name = input("Введіть ваше ім'я: ")
# patronymic = input("Введіть ваше по-батькові: ")

# initials = format_initials(surname, name, patronymic)
# print("Відформатовані ініціали:", initials)

