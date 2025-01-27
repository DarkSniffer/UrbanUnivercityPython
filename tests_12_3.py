import unittest
from runner2 import Runner, Tournament

def skip_if_frozen(cls_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if getattr(globals().get(cls_name), 'is_frozen', False):
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen('RunnerTest')
    def test_walk(self):
        runner = Runner("TestWalk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen('RunnerTest')
    def test_run(self):
        runner = Runner("TestRun")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen('RunnerTest')
    def test_challenge(self):
        runner1 = Runner("TestChallenge1")
        runner2 = Runner("TestChallenge2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
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

    @skip_if_frozen('TournamentTest')
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.__class__.all_results['test_race_usain_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_usain_nick'][max(self.__class__.all_results['test_race_usain_nick'].keys())] == "Ник")

    @skip_if_frozen('TournamentTest')
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.__class__.all_results['test_race_andrey_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_andrey_nick'][max(self.__class__.all_results['test_race_andrey_nick'].keys())] == "Ник")

    @skip_if_frozen('TournamentTest')
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.__class__.all_results['test_race_usain_andrey_nick'] = tournament.start()
        self.assertTrue(self.__class__.all_results['test_race_usain_andrey_nick'][max(self.__class__.all_results['test_race_usain_andrey_nick'].keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()