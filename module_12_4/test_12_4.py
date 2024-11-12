import rt_with_exceptions
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                    encoding="UTF-8", format='%(asctime)s || %(levelname)s || %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            tester = rt_with_exceptions.Runner("walking", speed=-5)
            logging.info(f'"test_walk" выполнен успешно')
            for i in range(0, 10):
                rt_with_exceptions.Runner.walk(tester)
            self.assertEqual(tester.distance, 50)
        except ValueError as negative_number:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            tester = rt_with_exceptions.Runner(10, 6)
            logging.info(f'"test_run" выполнен успешно')
            for i in range(0, 10):
                rt_with_exceptions.Runner.run(tester)
            self.assertEqual(tester.distance, 100)
        except TypeError as type_name:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        tester_walk = rt_with_exceptions.Runner("walking 1")
        tester_run = rt_with_exceptions.Runner("running 1")
        for i in range(0, 10):
            rt_with_exceptions.Runner.walk(tester_walk)
            rt_with_exceptions.Runner.run(tester_run)
        self.assertNotEqual(tester_walk.distance, tester_run.distance)



class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
         print(key, '. ', value)


    def setUp(self):
        self.runner_U = rt_with_exceptions.Runner("Usain", 10)
        self.runner_A = rt_with_exceptions.Runner("Andrey", 9)
        self.runner_N = rt_with_exceptions.Runner("Nick", 3)


    def test_Tournament_1(self):
        tour = rt_with_exceptions.Tournament(90, self.runner_U, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')


    def test_Tournament_2(self):
        tour = rt_with_exceptions.Tournament(90, self.runner_A, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[max(list(TournamentTest.all_results.keys()))+1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')


    def test_Tournament_3(self):
        tour = rt_with_exceptions.Tournament(90, self.runner_U, self.runner_A, self.runner_N)
        results = tour.start()
        TournamentTest.all_results[max(list(TournamentTest.all_results.keys()))+1] = results
        self.assertTrue(results[max(list(results.keys()))] == 'Nick')



if __name__ == "__main__":

    unittest.main()