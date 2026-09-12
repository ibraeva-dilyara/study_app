import random
import re
import time


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cards = []


class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class LearningApp:
    def __init__(self):
        self.users = {}
        self.current_user = None


    def register(self):
        username = input("Введите имя пользователя: ")

        if username in self.users:
            print("Пользователь уже существует.")
            return

        password = input("Введите пароль: ")

        if len(password) < 5:
            print("Пароль должен быть не короче 5 символов.")
            return

        if not re.fullmatch(r"[A-Za-z0-9]+", password):
            print("Пароль должен содержать только латинские буквы и цифры.")
            return

        self.users[username] = User(username, password)
        print("Регистрация успешна.")

    def login(self):
        username = input("Имя пользователя: ")
        password = input("Пароль: ")

        user = self.users.get(username)

        if user and user.password == password:
            self.current_user = user
            print(f"Добро пожаловать, {username}")
        else:
            print("Неверное имя пользователя или пароль.")




    def add_card(self):
        if not self.current_user:
            print("Сначала войдите в систему.")
            return

        question = input("Введите вопрос: ")
        answer = input("Введите ответ: ")

        self.current_user.cards.append(Card(question, answer))
        print("Карточка добавлена.")

    def random_card(self):
        if not self.current_user:
            print("Сначала войдите в систему.")
            return

        if not self.current_user.cards:
            print("У вас нет карточек.")
            return

        card = random.choice(self.current_user.cards)

        print("\nВопрос:")
        print(card.question)

        input("Нажмите Enter, чтобы увидеть ответ: ")

        print("Ответ:")
        print(card.answer)




    def quiz(self):
        if not self.current_user:
            print("Сначала войдите в систему.")
            return

        cards = self.current_user.cards

        if not cards:
            print("Нет карточек для викторины.")
            return

        score = 0

        questions = cards.copy()
        random.shuffle(questions)

        print("\nВикторина началась")
        print("На каждый вопрос даётся 30 секунд.\n")

        for card in questions:
            print(f"Вопрос: {card.question}")

            start_time = time.time()
            answer = input("Ваш ответ: ")
            elapsed = time.time() - start_time

            if elapsed > 30:
                print("Время вышло")
                continue

            if answer.strip().lower() == card.answer.strip().lower():
                print("Верно")
                score += 1
            else:
                print(f"Неверно. Правильный ответ: {card.answer}")

            print()

        print(f"Результат: {score}/{len(questions)}")



    def run(self):
        while True:
            print("\nМеню")
            print("1 Регистрация")
            print("2 Вход")
            print("3 Добавить карточку")
            print("4 Случайная карточка")
            print("5 Начать викторину")
            print("0 Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.add_card()
            elif choice == "4":
                self.random_card()
            elif choice == "5":
                self.quiz()
            elif choice == "0":
                print("До свидания!")
                break
            else:
                print("Неверный пункт меню.")


if __name__ == "__main__":
    app = LearningApp()
    app.run()