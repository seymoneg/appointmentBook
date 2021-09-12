"""
    Seymone Gugneja
    CSCI 3675
    Homework 1
"""

#import abc for abstract methods
from datetime import datetime, timedelta


class Contact:
    
    """
    CONTACT CLASS
    * Initialize first name, last name, and telephone number
    * get_name returns name
    * get_phone returns phone number
    * toString() returns the information as a string
    """
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def toString(self):
        return self.get_name() + '' + str(self.get_phone())
    
class Event():
    """
    EVENT ABSTRACT CLASS
    * Create abstract class event with 2 subclasses appointment and meeting
    * toString() returns the information as a string
    """

    #an event has an attribute for contact and starting date and time for the event
    def __init__(self, contact, mtgDateTime):
        super().__init__()
        self.contact = contact
        self.mtgDateTime = mtgDateTime
  
    def toString(self):
        return self.contact.toString() + '' + self.mtgDateTime.toString()
    
class Appointment(Event):
    """
    APPOINTMENT SUBCLASS
    * Create subclass for appointment that specifies the type of appointment
    * get_type returns the type of appointment
    * toString() returns the information as a string
    """
    
    def __init__(self, contact, mtgDate, mtgTime, apptType): 
        super().__init__(contact, mtgDate, mtgTime)
        self.apptType = apptType
            
    def get_type(self):
        return self.apptType
    
    def toString(self):
        return super().toString() + '' + self.get_type()

class Meeting(Event):
    """
    MEETING SUBCLASS
    * Create subclass for meeting that maintains the name of attendees
    * provide toString() method, addAttendee method, and get_attendees method
    * addAttendee method adds given name to meeting's list of attendees
    * get_attendees returns list of attendee names
    * toString() returns the information as a string
    """
    
    def __init__(self, contact, mtgDate, mtgTime, apptType, attendeeNames): 
        super().__init__(contact, mtgDate, mtgTime, apptType)
        self.attendeeNames = attendeeNames
        
    def addAttendee(self, person):
        self.attendeeNames.append(person)
    
    def get_attendees(self):
        return self.attendeeNames
    
    def toString(self):
        return super().toString() + '' + self.get_attendees()
    
class AppointmentBook:
    
    """
    APPOINTMENT BOOK
    * Maintain attribute that stores the list of events
    * add_event adds given event to appointment book
    * get_events_for_date returns a list of events for a given date
    """
    
    def __init__(self, eventList): 
        self.eventList = eventList
        
    def add_event(self, newEvent): 
        eventOnDate = self.get_events_for_date(newEvent.mtgDateTime)
        for i in eventOnDate:
            if newEvent.mtgDateTime == i.mtgDateTime:
                return
            
        self.eventList.append(newEvent)
    
    def get_events_for_date(self, date): 
        return [j for j in self.eventList if date.date() == j.mtgDateTime.date()]
    
def main():
    contact = Contact("Ashley Berry", 921-347-4480)
    
