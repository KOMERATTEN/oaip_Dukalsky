from random import randint
random_num = randint(1, 100)

user_num = int(input("Введите чило от 1 до 100: "))

while random_num != user_num:
    if user_num > random_num:
        print("Меньше")  
    elif user_num < random_num:
        print("Больше")

    user_num = int(input("Введите число от 1 до 100: "))
            
print("Угадал!")

