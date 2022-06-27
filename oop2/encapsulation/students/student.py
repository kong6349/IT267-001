class Student:
    def __init__(self,stuid,name,major) -> None:
        self._stuid = stuid
        self._name = name
        self._major = major

    def _displayNameAndMajor(self):
        print(f'name: {self._name}')
        print(f'major: {self._major}')