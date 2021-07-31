#  so we have based class called Musician 
# and we have class called Guitarist  , Drummers , Bass
from abc import ABC , abstractmethod, abstractstaticmethod
# Band, Musician, Guitarist, Bassist, Drummer


class Musician(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):

    def __init__(self, name):
        self.name = name
    
     
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
     
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return "face melting guitar solo"    


class Drummer(Musician):

    def __init__(self, name):
        self.name = name
    
    
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return "rattle boom crash"    


class Bassist(Musician):

    def __init__(self, name):
        self.name = name
    
    
    def __str__(self):
        return f"My name is {self.name} and I play bass"
     
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return "bom bom buh bom"


# //////////////////
class Band(Musician):
    instances = []
 
    def __init__(self, name , members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)

    
    def __str__(self):
        return f"our band name : {self.name}"
    
    def __repr__(self):
        return f"Band instance. Name = {self.name}."

    def play_solos(self):
        string_list =[]
        for instance in self.members:
            string_list.append(instance.play_solo())
        return string_list

    @classmethod
    def to_list(cls):
        return cls.instances

    def get_instrument():
        pass

    def play_solo(self):
        pass