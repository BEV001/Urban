import time


class UrTube():

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def add(self, *args):
        """
        добавление видео в реестр ситемы YouTube
        :param args: видео
        :return:
        """
        for item in args:
            if item.title not in self.videos.keys():
                self.videos[item.title] = {'duration': item.duration,
                                           'time now': item.time_now,
                                           'adult mode': item.adult_mode}
            else:
                self.videos[item.title]['time now'] = item.time_now

    def get_videos(self, key_word):
        """
        поиск видео по ключевому слову
        :param key_word: клюевое слово
        :return: список найденных видео
        """
        list_= []
        for title in self.videos.keys():
            if key_word.lower() in title.lower():
                list_.append(title)
            else:
                continue
        return list_

    def watch_video(self, title):
        """"
        просмотр видео
        """
        if self.current_user != None:             #  проверка на вход пользоваетеля
            if title in self.videos.keys():     # проверка наличия видео
                if self.videos[title]['adult mode'] == True and self.users[self.current_user]['age'] < 18:  #проверка на возврасное ограничение и возраст пользователя
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for sec in range(self.videos[title]['time now'], self.videos[title]['duration']+1, 1):
                        print (sec, end=" ")
                        time.sleep(1)
                    print ("Конец видео")
            else:
                print('Такого видео нет в YouTube')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


    def register_user(self, nickname, password, age):
        """
        регистрирует пользователя в системе и сохраняет его данные
        :param nickname: имя пользователя
        :param password: пароль пользователя в хешированном виде
        :param age:  возраст пользователя
        :return:
        """
        if nickname not in self.users.keys():
            user = User(nickname, password, age)
            self.users[user.nickname] = {'password': user.password,
                              'age': user.age}
            self.current_user = user.nickname
            print(f"Пользователь {nickname} зарегистрирован! \nДобро пожаловать в YouTube, {nickname}")
        else:
            return print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        """
        Вход в сиcтему YouTube
        :param nickname:
        :param password:
        :return:
        """
        print()
        if nickname in self.users.keys():   # проверка регистрации  пользователя
            if hash(password) == self.users[nickname]['password']:
                print(f"Добро пожаловать в YouTube, {nickname}")
                self.current_user = nickname
                return self.current_user
            else:
                print("Введен неверный пароль")
        else:
            print("Пользователь не найден, требуется регистрация")
            choice = int (input("Для регистрации нажмите - 1,\nдля выхода - 2,\nОтвет: "))
            if choice == 1:
                user = User(nickname, password, int(input("Введите ваш возраст: ")))
                self.register_user(user.nickname, user.password, user.age)
                self.log_out()
                self.current_user = user.nickname
                return self.current_user
            elif choice == 2:
                self.log_out()

    def log_out(self):
        """
        Выход из системы
        :return:
        """
        self.current_user = None
        return self.current_user


class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video():
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)




if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register_user('vasya_pupkin', 'lolkekcheburek',13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register_user('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')