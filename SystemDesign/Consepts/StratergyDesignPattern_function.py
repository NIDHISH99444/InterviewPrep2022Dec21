from abc import ABC,abstractmethod
from typing import List

class SupportTickets :
    # id : str
    customer : str
    issue : str

    # def __init__(self,id,customer,issue):
    def __init__(self,customer,issue):
        # self.id=id
        self.customer=customer
        self.issue=issue

def filocreateOrdering(list: List[SupportTickets]) -> List[SupportTickets]:
    return list.copy()

def filocreateOrdering( list: List[SupportTickets]) -> List[SupportTickets]:
    list_copy=list.copy()
    list_copy.reverse()
    return list_copy

class CustomerSupport:
    tickets : List[SupportTickets] = []

    def create_ticket(self,customer,issue):
        self.tickets.append(SupportTickets(customer,issue))

    def process_ticket(self,processingStratergy_func ):
        #create list
        ticketList=processingStratergy_func(self.tickets)
        for ticket in ticketList:
            self.print_ticket(ticket)

    def print_ticket(self,ticket : SupportTickets):
        print(ticket.customer,"->",ticket.issue)

app=CustomerSupport()
app.create_ticket("nidhish","laptop not working")
app.create_ticket("niharika","keyboard not working")
app.process_ticket(filocreateOrdering)

