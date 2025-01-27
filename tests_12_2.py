import unittest
from runner2 import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.__class__.all_results['test_race_usain_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_usain_nick'][max(self.__class__.all_results['test_race_usain_nick'].keys())] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.__class__.all_results['test_race_andrey_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_andrey_nick'][max(self.__class__.all_results['test_race_andrey_nick'].keys())] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.__class__.all_results['test_race_usain_andrey_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_usain_andrey_nick'][max(self.__class__.all_results['test_race_usain_andrey_nick'].keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()