"""
    Seymone Gugneja
    CSCI 3675
    Homework 1
"""

#import abstract base class and abstract method
from abc import ABC, abstractmethod

"""
    CONTACT CLASS
    * Initialize first name, last name, and telephone number
"""
class Contact:
    def __init__(self, fName, lName, telephone):
        self.fName = fName
        self.lName = lName
        self.telephone = telephone

"""
    EVENT ABSTRACT CLASS
    * Create abstract class event with 2 subclasses appointment and meeting
"""
class Event(ABC):

    @abstractmethod
    def appointment(Event): pass 

    @abstractmethod
    def meeting(Event): pass

    
