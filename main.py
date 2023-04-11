import unittest

from mail import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["adam.nowak@student.wat.edu.pl", True, True, "Adam", "Nowak"],
            ["magdalena.kowalska@wat.edu.pl", False, False, "Magdalena", "Kowalska"],
            ["michal.mazurek@student.wat.edu.pl", True, True, "Michal", "Mazurek"],
            ["ewa.szymczyk@wat.edu.pl", False, False, "Ewa", "Szymczyk"],
            ["jan.kaczmarek@student.wat.edu.pl", True, True, "Jan", "Kaczmarek"],
            ["krystyna.kowalczyk@wat.edu.pl", False, False, "Krystyna", "Kowalczyk"],
            ["pawel.krupa@student.wat.edu.pl", True, True, "Pawel", "Krupa"],
            ["anna.majewska@wat.edu.pl", False, False, "Anna", "Majewska"],
            ["bartosz.wojciechowski@student.wat.edu.pl", True, True, "Bartosz", "Wojciechowski"],
            ["elzbieta.janik@wat.edu.pl", False, False, "Elzbieta", "Janik"], ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_male = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_male, extractor.is_male())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())