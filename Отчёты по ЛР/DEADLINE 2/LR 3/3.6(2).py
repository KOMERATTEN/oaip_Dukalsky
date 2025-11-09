from random import randint

# Инициализация данных
counter = {}
store = {}
price = {}
money = 1000  # начальный капитал
days = 0
name = input("Введите имя вашего ларька: ")

print(f"CRM система Ларька {name}")

def add_fruit():
    fruit = input("Введите название фрукта: ")
    max_counter = int(input("Максимальное количество на прилавке: "))
    max_store = int(input("Максимальное количество за прилавком: "))
    purchase = int(input("Цена покупки: "))
    sale = int(input("Цена продажи: "))
    
    counter[fruit] = {'max': max_counter, 'current': 0}
    store[fruit] = {'max': max_store, 'current': 0}
    price[fruit] = {'sale_price': sale, 'purchase_price': purchase}

def move_to_counter():
    fruit = input("Какой фрукт переместить? ")
    if fruit in store and fruit in counter:
        amount = int(input("Сколько переместить? "))
        if store[fruit]['current'] >= amount:
            available_space = counter[fruit]['max'] - counter[fruit]['current']
            if amount > available_space:
                amount = available_space
            store[fruit]['current'] -= amount
            counter[fruit]['current'] += amount
            print(f"Перемещено {amount} {fruit}")
        else:
            print("Недостаточно фруктов за прилавком")
    else:
        print("Фрукт не найден")

def buy_fruit():
    global money
    fruit = input("Какой фрукт закупить? ")
    if fruit in price:
        amount = int(input("Сколько закупить? "))
        cost = amount * price[fruit]['purchase_price']
        if money >= cost:
            available_space = store[fruit]['max'] - store[fruit]['current']
            if amount > available_space:
                amount = available_space
            store[fruit]['current'] += amount
            money -= cost
            print(f"Закуплено {amount} {fruit} за {cost}")
        else:
            print("Недостаточно денег")
    else:
        print("Фрукт не найден")

def simulate_day():
    global money, days
    days += 1
    print(f"\n--- День {days} ---")
    
    # Продажа фруктов
    for fruit in counter:
        if counter[fruit]['current'] > 0:
            sold = randint(0, counter[fruit]['current'])
            counter[fruit]['current'] -= sold
            money += sold * price[fruit]['sale_price']
            print(f"Продано {sold} {fruit}")
    
    # Кража Ашота
    if randint(1, 100) <= 20:
        stolen_fruit = list(counter.keys())[randint(0, len(counter)-1)]
        stolen_amount = int(counter[stolen_fruit]['current'] * randint(50, 100) / 100)
        counter[stolen_fruit]['current'] -= stolen_amount
        print(f"Ашот украл {stolen_amount} {stolen_fruit}!")
    
    # Изменение цен
    for fruit in price:
        change = randint(-5, 5)
        price[fruit]['sale_price'] += change
        price[fruit]['purchase_price'] += change
        if change > 0:
            print(f"Цена на {fruit} выросла")
        elif change < 0:
            print(f"Цена на {fruit} упала")
    
    print(f"Баланс: {money}")
    
    if money <= 0:
        print("Вы банкрот! Возвращайтесь на арбузные плантации.")
        exit()
    
    if days >= 10:
        print("Поздравляем! Ашота поймали! Вы победили!")
        exit()

def show_status():
    print("\n--- Статус ---")
    print(f"Деньги: {money}")
    print("Прилавок:")
    for fruit, data in counter.items():
        print(f"  {fruit}: {data['current']}/{data['max']}")
    print("Запас:")
    for fruit, data in store.items():
        print(f"  {fruit}: {data['current']}/{data['max']}")
    print("Цены:")
    for fruit, data in price.items():
        print(f"  {fruit}: покупка {data['purchase_price']}, продажа {data['sale_price']}")

# Основной цикл
while True:
    print("\n1 - Добавить фрукт")
    print("2 - Переместить на прилавок")
    print("3 - Закупить фрукты")
    print("4 - Статус")
    print("5 - Завершить день")
    print("6 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        add_fruit()
    elif choice == "2":
        move_to_counter()
    elif choice == "3":
        buy_fruit()
    elif choice == "4":
        show_status()
    elif choice == "5":
        simulate_day()
    elif choice == "6":
        break
    else:
        print("Неверный выбор")