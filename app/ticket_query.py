from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.globals import BookingService,TheatreService, MovieService
from app.globals import State
import json

Movie_AllBookings = './data/bookings.json'
with open(Movie_AllBookings, 'r') as f:
    my_list = json.load(f)
    print(my_list)

class TicketQueryScreen(TitledScreen):
    def __init__(self):
        super().__init__("Ticket")

    def start(self):
        super().start()
        print('Select an option or 0 to return home:')
        print('1.Query Ticket')
        print('2.Cancel Ticket')
        print('3.Go back')
        ticket_activity = int(input())

        print('Enter your ticket ID or 99 to return to previous page')
        ticketID_no = int(input())
        ticket_info = BookingService.get(ticketID_no)
        print('Your ticket details will be displayed below:')
        print('Here is ticket #' + str(ticketID_no) + ' :' )

        def TicketQuery(ticketID_no):
            print('hi')

        def TicketCancellation(ticketID_no):
            for idx, obj in enumerate(my_list):
                if obj['id'] == ticketID_no:
                    my_list.pop(idx)

        def Ticket_GoBack():
            return self.navigate(Test())


        if ticket_activity == 1:
            return TicketQuery

        elif ticket_activity == 2:
            print('confirm ticket cancellation (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Ticket #' + str(ticketID_no) + ' has been cancelled')
                print('Thank You.')
                return TicketCancellation

            elif answer == 'no':
                return Ticket_GoBack()

        else:
            return Ticket_GoBack()


        return self.navigate(Test())











