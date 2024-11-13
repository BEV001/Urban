import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = bool

    @unittest.skipIf(is_frozen, "Тесты заморожены в этом кейсе")
    def test_walk(self):
        tester = runner.Runner("walking")
        for i in range(0, 10):
            runner.Runner.walk(tester)
        self.assertEqual(tester.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты заморожены в этом кейсе")
    def test_run(self):
        tester = runner.Runner("running")
        for i in range(0, 10):
            runner.Runner.run(tester)
        self.assertEqual(tester.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты заморожены в этом кейсе")
    def test_challenge(self):
        tester_walk = runner.Runner("walking 1")
        tester_run = runner.Runner("running 1")
        for i in range(0, 10):
            runner.Runner.walk(tester_walk)
            runner.Runner.run(tester_run)
        self.assertNotEqual(tester_walk.distance, tester_run.distance)


if __name__ == "__main__":
    unittest.main()
