
from datetime import datetime, timedelta


class student:

    def __init__(self, id, name, dob, year):
        self.studentID = id
        self.name = name
        self.date = dob
        self.year = year

    def calc_age(self):
        now = datetime.now()
        birthday = datetime.strptime(self.date, "%m-%d-%Y")
        difference = now - birthday
        self.date = difference.days // 365
        return self.date
    
    def get_registration(self):
        if self.year == 'Senior':
            return '4/1 to 4/3'
        elif self.year == 'Junior':
            return '4/4 to 4/6.'
        elif self.year == 'Sophomore':
            return '4/7 to 4/9.'
        elif self.year == 'Freshman':
            return '4/10 to 4/12'
        else:
            print('Invalid year. Please enter Senior, Junior, Sophomore, or Freshman.')


