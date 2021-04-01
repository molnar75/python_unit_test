class Employee:
    
    def __init__(self, first, last, pay, birth_year):
        self.first = first
        self.last = last
        self.pay = pay
        self.birth_year = birth_year
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def age(self):
        if self.birth_year != None:
            return 2021 - self.birth_year
        else:
            return None
    
    @age.deleter
    def age(self):
        self.birth_year = None
