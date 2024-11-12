import runner_and_tournament
import unittest


def start_or_not(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', True):
            self.skipTest("Тесты заморожены в этом кейсе")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
         print(key, '. ', value)

    @start_or_not
    def setUp(self):
        self.runner_U = runner_and_tournament.Runner("Usain", 10)
        self.runner_A = runner_and_tournament.Runner("Andrey", 9)
        self.runner_N = runner_and_tournament.Runner("Nick", 3)

    @start_or_not
    def test_Tournament_1(self):
        tour = runner_and_tournament.Tournament(90, self.runner_U, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')

    @start_or_not
    def test_Tournament_2(self):
        tour = runner_and_tournament.Tournament(90, self.runner_A, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[max(list(TournamentTest.all_results.keys()))+1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')

    @start_or_not
    def test_Tournament_3(self):
        tour = runner_and_tournament.Tournament(90, self.runner_U, self.runner_A, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[max(list(TournamentTest.all_results.keys()))+1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')

    #проверка, что нет зависимости порядка участников и победителя
    #для этого беру дистанцию = наименьшей из скоростей из двух участников
    #запускаю тест дважды, меняя порядок участников
    #оба раза должен победить один и тот же
    @start_or_not
    def test_Tournament_4(self):
        distance = min(self.runner_N.speed,self.runner_U.speed)*1
        tour = runner_and_tournament.Tournament(distance, self.runner_U, self.runner_N)
        results = tour.start()
        tour_1 = runner_and_tournament.Tournament(distance, self.runner_N, self.runner_U)
        results_1 = tour_1.start()

        self.assertTrue(results[max(list(results.keys()))] == results_1[max(list(results_1.keys()))])


if __name__ == "__main__":
    unittest.main()