from datetime import datetime

class student:

    def __init__(self, name, dob, credits):
        self.name = name
        self.dob = dob
        self.credits = credits
        
    def get_age(self):
        age = (datetime.now() - self.dob).days // 365
        return age

    def get_credits(self):
        return self.credits
    
    def topper(self):
        return max(student,lambda student:student.get_credits()) 
    
    