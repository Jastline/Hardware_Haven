import os

# Инициализируем класс магазина
class HardwareHaven: # Класс магазина
    def __init__(self):
        self.products = [] # Список продуктов
        self.admins = [] # Список админов
        self.customers = [] # Список покупателей
        self.purchased_products = [] # Список купленных продуктов

    # Функция добавления товара
    def add_product(self, name, price, quantity):
        self.products.append({"name": name, "price": price, "quantity": quantity})

    # Функция удаления товара
    def remove_product(self, idx):
        # Если индекс товара будет больше 0 и меньше или равен количеству всех товаров
        if 0 < idx <= len(self.products):
            # Удалить продукт по индексу
            removed_product = self.products.pop(idx - 1)
            print(f"Товар '{removed_product['name']}' успешно удален.")
        else:
            print("Продукт с указанным индексом не найден.")

    # Функция вывода всех товаров
    def display_products(self):
        if self.products:
            print("\nСписок продуктов:")
            # В цикле будут выводится все значения из списка self.products
            for idx, product in enumerate(self.products, start=1):
                print(f"{idx}. {product['name']} - Цена: {product['price']} руб. - В наличии: {product['quantity']}")
        else:
            print("В магазине нет продуктов.")

    # Функция вывода всех купленных товаров
    def display_purchased_products(self):
        # Проверяем, есть ли купленные товары
        if self.purchased_products:
            # Если есть, выводим список купленных товаров
            print("\nСписок купленных товаров:")
            for product in self.purchased_products:
                print(f"{product['name']} - Цена: {product['price']} руб. - Количество: {product['quantity']}")
        else:
            # Если купленных товаров нет, выводим сообщение об этом
            print("Вы еще не совершали покупок за сегодняшнюю сессию")

    def display_active_customers(self):
        # Проверяем, есть ли активные покупатели в списке
        if self.customers:
            # Если есть, выводим заголовок
            print("Активные покупатели:")
            # Перебираем каждого покупателя и выводим его имя и логин
            for customer in self.customers:
                print(f"Имя: {customer['name']}, Логин: {customer['login']}")
        else:
            # Если список покупателей пуст, выводим сообщение об отсутствии активных покупателей
            print("Нет активных покупателей.")

    def display_active_admins(self):
        # Проверяем, есть ли активные администраторы в списке
        if self.admins:
            # Если есть, выводим заголовок
            print("Активные администраторы:")
            # Перебираем каждого администратора и выводим его имя и логин
            for admin in self.admins:
                print(f"Имя: {admin['name']}, Логин: {admin['login']}")
        else:
            # Если список администраторов пуст, выводим сообщение об отсутствии активных администраторов
            print("Нет активных администраторов.")

    # Функция покупки товара
    def buy_product(self, idx, quantity):
        # Если индекс будет больше 0 и меньше или равен длине товаров
        if 0 < idx <= len(self.products):
            # Получаем информацию о продукте по индексу
            product = self.products[idx - 1]
            # Проверяем, достаточно ли товара для покупки указанного количества
            if product['quantity'] >= quantity:
                # Выводим сообщение о покупке и вычитаем купленное количество из общего количества товара
                print(f"Вы купили {quantity} единиц товара '{product['name']}' за {product['price'] * quantity} руб.")
                product['quantity'] -= quantity
                # Добавляем купленный товар в список приобретенных товаров
                self.purchased_products.append(
                    {"name": product['name'], "price": product['price'], "quantity": quantity})
            else:
                # Если товара недостаточно, выводим сообщение об этом
                print("Недостаточно товара в наличии.")
        else:
            # Если указанный индекс продукта не найден, выводим сообщение об этом
            print("Продукт с указанным индексом не найден.")

    # Функция сохранения данных в файл product.txt
    def save_data_from_file(self, list_for_save, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                if list_for_save == self.products:
                    file.write("Список продуктов:\n")
                    for product in self.products:
                        file.write(f"    {product['name']} - {product['price']} - {product['quantity']}\n")
                    print("\nДанные о продуктах успешно сохранены в файл", filename)
                elif list_for_save == self.admins:
                    for admin in self.admins:
                        name = admin['name'].strip()  # Используем ключи словаря admin
                        login = admin['login'].strip()
                        password = admin['password'].strip()

                        name = name.replace(':', '', 1)

                        file.write(f"Админ {name}:\n"
                                   f"    Логин: {login}\n"
                                   f"    Пароль: {password}\n")
                    print("\nДанные об админах успешно сохранены в файл", filename)
                elif list_for_save == self.customers:
                    for customer in self.customers:
                        name = customer['name'].strip()
                        login = customer['login'].strip()
                        password = customer['password'].strip()

                        name = name.replace(':', '', 1)

                        file.write(f"Покупатель {name}:\n"
                                   f"    Логин: {login}\n"
                                   f"    Пароль: {password}\n")
                    print("\nДанные о покупателях успешно сохранены в файл", filename)
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    # Функция загрузки товаров из файла product.txt
    def load_data_from_file(self):
        # Загрузка файла product.txt
        try:
            # Открываем файл товаров в режиме чтения
            with open('Product.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()  # Строка = строка из файла
                products_start_idx = 0  # Начальный индекс товара

                # Проходим по каждой строке файла и присваиваем порядковый номер строки, а также саму строку
                for idx, line in enumerate(lines):
                    if line.startswith("Список продуктов:"):
                        products_start_idx = idx + 1
                        break

                # Проходим по каждой строке файла в поисках и присваиваем атрибуту товара значения из файла
                if products_start_idx:
                    self.products = []
                    for line in lines[products_start_idx:]:
                        parts = line.strip().split(" - ")
                        if len(parts) == 3:  # Проверяем, что есть все три части
                            name, price, quantity = parts
                            self.products.append({"name": name, "price": float(price), "quantity": int(quantity)})
                        else:
                            print(f"Неверный формат строки: {line}")

            print("\nДанные о продуктах успешно загружены из файла Product.txt")
        except FileNotFoundError:
            print("Ошибка: Файл 'Product.txt' не найден.")

        # Загрузка файла Admin.txt
        try:
            with open('Admin.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.admins = []
                idx = 0
                while idx < len(lines):
                    if lines[idx].startswith("Админ"):
                        parts = lines[idx].strip().split(" ")
                        if len(parts) == 2:
                            name = parts[1]
                        else:
                            name = "Unknown"
                        login = lines[idx + 1].strip().split(": ")[1]
                        password = lines[idx + 2].strip().split(": ")[1]
                        self.admins.append({"name": name, "login": login, "password": password})
                        idx += 3
                    else:
                        idx += 1

            print("Данные об администраторах успешно загружены из файла Admin.txt.")
        except FileNotFoundError:
            print("Ошибка: Файл 'Admin.txt' не найден.")

        # Загрузка файла Customer.txt
        try:
            with open('Customer.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.customers = []
                idx = 0
                while idx < len(lines):
                    if lines[idx].startswith("Покупатель"):
                        parts = lines[idx].strip().split(" ")
                        if len(parts) == 2:
                            name = parts[1]
                        else:
                            name = "Unknown"
                        login = lines[idx + 1].strip().split(": ")[1]
                        password = lines[idx + 2].strip().split(": ")[1]
                        self.customers.append({"name": name, "login": login, "password": password})
                        idx += 3
                    else:
                        idx += 1

            print("Данные о покупателях успешно загружены из файла Customer.txt.")
        except FileNotFoundError:
            print("Ошибка: Файл 'Customer.txt' не найден.")

    # Проверка наличия всех файлов
    def check_file(self):
        try:
            # Проверяем наличие файлов
            with open("Product.txt", "r", encoding='utf-8') as product_file:
                if product_file.read().strip():  # Проверяем, что файл не пустой
                    pass
                else:
                    return False
            with open("Admin.txt", "r", encoding='utf-8') as admin_file:
                if admin_file.read().strip():  # Проверяем, что файл не пустой
                    pass
                else:
                    return False
            with open("Customer.txt", "r", encoding='utf-8') as customer_file:
                if customer_file.read().strip():  # Проверяем, что файл не пустой
                    pass
                else:
                    return False
            return True
        except FileNotFoundError:
            return False

    def create_missing_files(self):
        # Проверка наличия файла с продуктами
        if not os.path.exists('Product.txt'):
            with open('Product.txt', 'w', encoding='utf-8') as file:
                file.write("")

        # Проверка наличия файла с админами
        if not os.path.exists('Admin.txt'):
            with open('Admin.txt', 'w', encoding='utf-8') as file:
                file.write("")

        # Проверка наличия файла с покупателями
        if not os.path.exists('Customer.txt'):
            with open('Customer.txt', 'w', encoding='utf-8') as file:
                file.write("")
    # Проверяем наличие файлов и создаем их при необходимости


# Инициализируем основные классы пользователей
class Person:
    def __init__(self):
        self.nickname = None
        self.login = None
        self.password = None
        self.admins = []
        self.customers = []
        self.products = []

class Admin(Person):
    def __init__(self):
        super().__init__()

    shop = HardwareHaven()

    def add_admin(self, nickname, login, password):
        self.nickname = nickname
        self.login = login

        self.password = password

class Customer(Person):
    def __init__(self):
        super().__init__()

    def add_customer(self, nickname, login, password):
        self.nickname = nickname
        self.login = login
        self.password = password

# Инициализируем основную функцию, которая будет выполнять основной код программы
def main():
    # Создаём объект класса магазина
    shop = HardwareHaven()

    # Инициализируем функцию инициализации пользователя
    def authentication():
        # Строчка ниже позволяет выполнять код, до тех пор, пока не выйдем из цикла
        while True:
            # Инициализируем переменные для корректной работы и избегания ошибок
            admin_login_file = ""
            admin_password_file = ""

            customer_login_file = ""
            customer_password_file = ""

            print("\nВыберите доступное действие:\n"
                  "1. Администратор\n"
                  "2. Покупатель\n"
                  "3. Зарегистрироваться\n"
                  "4. Выход\n")
            # Принимаем выбор пользователя
            choice = input("Выберите действие: ")

            if choice == '1': # Если Выбран Администратор
                # Принимаем значения введёных данных
                admin_name = input("Никнейм:")
                admin_login = input("Логин: ")
                admin_password = input("Пароль: ")
                admin_found = False # Это надо, чтобы грамотно работали функции переборки файлов
                try:
                    # Открываем файл админа
                    with open('Admin.txt', 'r', encoding='utf-8') as file:
                        # Повторяем цикл столько раз, сколько у нас строчек
                        for line in file:
                            # Перебираем пока не найдём нужного админа
                            if line.strip() == f'Админ {admin_name}:':
                                # Возвращаем true, чтобы удобно перейти к следующей стадии инициализации
                                admin_found = True
                            # Когда значение true начинает выполнятся этот код
                            elif admin_found:
                                # Если после очищения от всего в начале строки остаётся "Логин:", то выполняем
                                if line.strip().startswith('Логин:'):
                                    # Считываем логин админа из файла убирая всё ненужное
                                    admin_login_file = line.strip().split(':')[-1].strip()
                                # Аналогично для пароля
                                elif line.strip().startswith('Пароль:'):
                                    admin_password_file = line.strip().split(':')[-1].strip()
                                    break  # После получения пароля можно прекратить перебор
                    # Если логин и пароль совпадают с тем, что уже инициализированы в файле, то выполняем
                    if admin_login == admin_login_file and admin_password == admin_password_file:
                        print(f"\nДобро пожаловать божественное существо {admin_name}")
                        admin = Admin() # Объект класса Админ
                        admin.nickname = admin_name
                        admin.login = admin_login
                        admin.password = admin_password
                        return admin
                    # Если в файле такого пользователя ненашли
                    else:
                        print("Вы ввели неверно логин или пароль:\n"
                              f"{admin_login_file}, {admin_password_file}")
                    # Выход из цикла authentication
                    break
                # Функция для обработки ошибок
                except FileNotFoundError:
                    print("Ошибка: Файл 'Admin.txt' не найден.")
                    # Выход из цикла authentication
                    break

            elif choice == '2': # Если выбран Покупатель
                # Всё тоже самое, что и для админа
                customer_nickname = input("Никнейм:")
                customer_login = input("Логин: ")
                customer_password = input("Пароль: ")
                customer_found = False

                with open('Customer.txt', 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.strip() == f'Покупатель {customer_nickname}:':
                            customer_found = True
                        elif customer_found:
                            if line.strip().startswith('Логин:'):
                                customer_login_file = line.strip().split(':')[-1].strip()
                            elif line.strip().startswith('Пароль:'):
                                customer_password_file = line.strip().split(':')[-1].strip()
                                break  # После получения пароля можно прекратить перебор
                if customer_login == customer_login_file and customer_password == customer_password_file:
                    print(f"\nПриветствуем вас в нашем магазине: {customer_nickname}")
                    customer = Customer()
                    customer.nickname = customer_nickname
                    customer.login = customer_login
                    customer.password = customer_password
                    return customer
                else:
                    print("Вы ввели неверно логин или пароль:\n"
                          f"{customer_login_file}, {customer_password_file}")
                # Выход из цикла authentication
                break
            elif choice == '3': # Если пользователь хочет зарегистрироваться
                # Даём выбор
                choice_2 = input("\nКем вы хотите стать?"
                                 "\n1. Админ"
                                 "\n2. Покупатель"
                                 "\n\nВыберите действие: ")
                # Ставим ограничние на регистрацию, чтобы сторонний пользователь не зарегестрировался под видом админа
                if choice_2 == '1':
                    print("\nВы не можете добавить админа не авторизовавшись.\n"
                          "Чтобы зарегестрировать нового админа необходимо одному из действующих вас зарегестрировать")
                # Регистрируем покупателя
                elif choice_2 == '2':
                    customer = Customer() # Объект класса Покупатель
                    customer_name = input("Введите никнейм покупателя: ")
                    customer_login = input("Введите логин покупателя: ")
                    customer_password = input("Введите пароль покупателя: ")
                    customer_found = False  # Это надо, чтобы грамотно работали функции переборки файлов
                    if customer_found == False: # Если покупатель не найден, то пытаемся его найти при авторизации, чтобы проверить совпадения на уже существующих пользователей
                        # Открываем файл покупателя
                        with open('Customer.txt', 'r', encoding='utf-8') as file:
                            # Повторяем цикл столько раз, сколько у нас строчек
                            for line in file:
                                # Проверяем, существует ли покупатель с таким же именем или логином
                                if line.strip() == f'Покупатель {customer_name}:':
                                    print("\nТакое имя уже существует")
                                    customer_found = True
                                    break  # Прерываем цикл, так как уже найден существующий пользователь
                                elif line.strip() == f'Логин: {customer_login}':
                                    print("\nТакой логин уже существует")
                                    customer_found = True
                                    break  # Прерываем цикл, так как уже найден существующий пользователь
                        # Если пользователь не найден, регистрируем его и сохраняем данные
                        if customer_found == False:
                            customer.nickname = customer_name
                            customer.login = customer_login
                            customer.password = customer_password
                            # Преобразуем объект Customer в словарь перед сохранением
                            customer_dict = {
                                'name': customer.nickname,
                                'login': customer.login,
                                'password': customer.password
                            }
                            shop.customers.append(customer_dict)  # Добавляем покупателя в список
                            shop.save_data_from_file(shop.customers, 'Customer.txt')
                            print(
                                "\nВы успешно зарегистрировались, пройдите авторизацию снова, чтобы подтвердить ваши данные")
                        else:
                            print("\nПопробуйте зарегистрироваться заново, такой пользователь уже существует")

            elif choice == '4': # Если пользвоатель выходит из программы

                print("До свидания!")

                # Сначала сохраняем данные продуктов
                shop.save_data_from_file(shop.products, "Product.txt")

                # Затем сохраняем данные администраторов
                shop.save_data_from_file(shop.admins, "Admin.txt")

                # И в конце сохраняем данные покупателей
                shop.save_data_from_file(shop.customers, "Customer.txt")

                exit()

            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")
                return None

    def main_text():
        while True:
            User = authentication()
            while True:
                if isinstance(User, Admin):
                    print("\nМеню:\n"
                          "1. Посмотреть список товаров\n"
                          "2. Добавить продукт\n"
                          "3. Удалить продукт\n"
                          "4. Посмотреть список админов\n"
                          "5. Посмотреть список пользователей\n"
                          "6. Добавить нового админа\n"
                          "9. Выход\n")

                    choice = input("Выберите действие: ")
                    if choice == '1':
                        shop.display_products()
                    elif choice == '2':
                        name = input("Введите название продукта: ")
                        price = float(input("Введите цену продукта: "))
                        quantity = int(input("Введите количество продукта: "))
                        shop.add_product(name, price, quantity)
                    elif choice == '3':
                        idx = int(input("Введите индекс продукта для удаления: "))
                        shop.remove_product(idx)
                    elif choice == '4':
                        shop.display_active_admins()
                    elif choice == '5':
                        shop.display_active_customers()
                    elif choice == '6':
                        admin_name = input("Введите никнейм администратора: ")
                        admin_login = input("Введите логин администратора: ")
                        admin_password = input("Введите пароль администратора: ")
                        admin_found = False  # Флаг для проверки существующих администраторов
                        # Проверяем наличие администратора с таким же никнеймом или логином
                        with open('Admin.txt', 'r', encoding='utf-8') as file:
                            for line in file:
                                if f'Админ {admin_name}:' in line.strip():
                                    print("\nТакое имя уже существует")
                                    admin_found = True
                                    break
                                elif f'Логин: {admin_login}' in line.strip():
                                    print("\nТакой логин уже существует")
                                    admin_found = True
                                    break

                        # Если администратор не найден, регистрируем его
                        if not admin_found:
                            admin = Admin()
                            admin.name = admin_name
                            admin.login = admin_login
                            admin.password = admin_password

                            admin_dict = {
                                'nickname': admin.name,
                                'login': admin.login,
                                'password': admin.password
                            }
                            shop.admins.append(admin_dict)
                            shop.save_data_from_file(shop.admins, 'Admin.txt')
                            print(
                                "\nВы успешно зарегистрировались, пройдите авторизацию снова, чтобы подтвердить ваши данные")
                        else:
                            print("\nПопробуйте зарегистрироваться заново, такой администратор уже существует")
                    elif choice == '9':
                        print(f"Вы вышли из аккаунта админа")
                        break
                    else:
                        print("Неверный выбор. Пожалуйста, выберите снова.")
                elif isinstance(User, Customer):
                    print("\nМеню:\n"
                          "1. Посмотреть список товаров\n"
                          "2. Купить товары\n"
                          "3. Показать купленные товары\n"
                          "9. Выход\n")

                    choice = input("Выберите действие: ")
                    if choice == '1':
                        shop.display_products()
                    elif choice == '2':
                        shop.display_products()
                        idx = int(input("\nВведите номер товара, который хотите купить: "))
                        quantity = int(input("\nВведите количество товара: "
                                             "\nЕсли вы передумаете, то введите 0"))
                        shop.buy_product(idx, quantity)
                    elif choice == '3':
                        shop.display_purchased_products()
                    elif choice == '9':
                        print("Вы вышли из аккаунта покупателя")
                        break
                    else:
                        print("Неверный выбор. Пожалуйста, выберите снова.")
                else:
                    break
    # Проверка данных и возвращение булевого результата
    check = shop.check_file()

    # Проверка на наличие сохранения
    if check:
        # Загрузка данных из файла при запуске
        shop.load_data_from_file()
        main_text()
    else:
        # Если файлы отсутствуют, создаем их и пытаемся снова вызвать main
        shop.create_missing_files()
        main_text()  # Рекурсивный вызов функции main

# Выполняем основной код
if __name__ == "__main__":
    # Этот блок кода будет выполнен только если данный файл был запущен напрямую,
    # а не импортирован как модуль в другой программе.
    main()  # Вызываем функцию main(), которая является точкой входа в программу.
