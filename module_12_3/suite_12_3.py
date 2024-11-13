import unittest
import test_12_1
import test_12_2

test_12_1.RunnerTest.is_frozen = True
test_12_2.TournamentTest.is_frozen = True

runner_tournament = unittest.TestSuite()

runner_tournament.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
runner_tournament.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

TextTestRunner = unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(runner_tournament)
