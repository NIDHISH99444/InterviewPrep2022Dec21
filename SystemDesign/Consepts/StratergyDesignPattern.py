from abc import ABC,abstractmethod
from typing import List

class SupportTickets :
    customer : str
    issue : str

    def __init__(self,customer,issue):
        self.customer=customer
        self.issue=issue


class TicketOrderingStratergy(ABC):
    @abstractmethod
    def createOrdering(self,list : List[SupportTickets]) -> List[SupportTickets]:
        pass


class FIFOStratergy(TicketOrderingStratergy):
    def createOrdering(self, list: List[SupportTickets]) -> List[SupportTickets]:
        return list.copy()

class FILOStratergy(TicketOrderingStratergy):
    def createOrdering(self, list: List[SupportTickets]) -> List[SupportTickets]:
        list_copy=list.copy()
        list_copy.reverse()
        return list_copy


class CustomerSupport:
    tickets : List[SupportTickets] = []

    def create_ticket(self,customer,issue):
        self.tickets.append(SupportTickets(customer,issue))

    def process_ticket(self,processingStratergy :TicketOrderingStratergy ):
        #create list
        ticketList=processingStratergy.createOrdering(self.tickets)
        for ticket in ticketList:
            self.print_ticket(ticket)

    def print_ticket(self,ticket : SupportTickets):
        print(ticket.customer,"->",ticket.issue)

app=CustomerSupport()
app.create_ticket("nidhish","laptop not working")
app.create_ticket("niharika","keyboard not working")
app.process_ticket(FILOStratergy())


