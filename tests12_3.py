import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        maks = runner.Runner('Макс')
        for i in range(10):
            maks.walk()
        self.assertEqual(maks.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        denis = runner.Runner('Денис')
        for i in range(10):
            denis.run()
        self.assertEqual(denis.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        ivan = runner.Runner('Иван')
        sasha = runner.Runner('Саша')
        for i in range(10):
            ivan.run()
            sasha.walk()
        self.assertNotEqual(ivan.distance, sasha.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.first_runner = runner_and_tournament.Runner('Усэйн', 10)
        self.second_runner = runner_and_tournament.Runner('Андрей', 9)
        self.third_runner = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        race = runner_and_tournament.Tournament(90, self.first_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        race = runner_and_tournament.Tournament(90, self.second_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        race = runner_and_tournament.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
