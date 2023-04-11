import re

class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.regex = r'((?P<name>[a-z]+)\.(?P<surname>[a-z]+)[0-9]*@(?P<is_student>(student\.)?)(wat\.edu\.pl))'

    def is_student(self) -> bool:
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        return bool(res and res[0][3])

    def get_name(self) -> str:
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        return res[0][1].capitalize() if res else None

    def get_surname(self) -> str:
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        return res[0][2].capitalize() if res else None

    def is_male(self) -> bool:
        name = self.get_name()
        return name and not name.endswith('a')