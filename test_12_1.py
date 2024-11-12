import runner
import unittest

def start_or_not(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', True):
            self.skipTest("Тесты заморожены в этом кейсе")
        else:
            return func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @start_or_not
    def test_walk(self):
        tester = runner.Runner("walking")
        for i in range(0, 10):
            runner.Runner.walk(tester)
        self.assertEqual(tester.distance, 50)

    @start_or_not
    def test_run(self):
        tester = runner.Runner("running")
        for i in range(0, 10):
            runner.Runner.run(tester)
        self.assertEqual(tester.distance, 100)

    @start_or_not
    def test_challenge(self):
        tester_walk = runner.Runner("walking 1")
        tester_run = runner.Runner("running 1")
        for i in range(0, 10):
            runner.Runner.walk(tester_walk)
            runner.Runner.run(tester_run)
        self.assertNotEqual(tester_walk.distance, tester_run.distance)



if __name__ == "__main__":
    unittest.main()
