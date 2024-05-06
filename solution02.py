class AirTicket:
    '''
    Class of AirTickets.

    Parameters
    ----------
    passenger_name (str): Name of passenger.
    _from (str): The country of departure.
    to (str): The country of arrival.
    date_time (str): Date and time.
    flight (str): Number of flight.
    seat (str): Seat of passenger.
    _class (str): Passengers class.
    gate (str): Number of gate.

    Returns
    -------
    (str): Info about each passengers.
    '''


    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate


    def __str__(self):
        len_pas = 16 - len(self.passenger_name)
        len_from = 4 - len(self._from)
        len_to = 3 - len(self.to)
        len_date = 16 - len(self.date_time)
        len_flight = 20 - len(self.flight)
        len_seat = 4 - len(self.seat)
        len_class = 3 - len(self._class)
        len_gate = 4 - len(self.gate)

        return '|' + self.passenger_name + ' ' * len_pas + '|' + self._from + ' '\
        * len_from + '|' + self.to + ' ' * len_to + '|' + self.date_time + ' '\
        * len_date + '|' + self.flight + ' ' * len_flight + '|' + self.seat\
        + ' ' * len_seat + '|' + self._class + ' ' * len_class + '|'\
        + self.gate + ' ' * len_gate + '|'
    
class Load:
    '''
    Class of loading tickeckets.

    Attributes
    ----------
    data (list): List of instances of the AirTicket class.
    '''
    data = []

    def write(file):
        '''
        Reads file then make instances of the AirTicket class and add it to "Load.data".
        '''


        with open(file, 'r', encoding='utf-8') as file:
            attributes = file.readline().strip().split(';')
            all_tickets = file.readlines()[1:]
        
        attributes.pop()
        all_tickets = [s.replace('\n', '') for s in all_tickets]
        all_tickets = [s.split(';') for s in all_tickets]
        for item in all_tickets:
            item.pop()

        for ticket in all_tickets:
            tckt_dt = AirTicket(*ticket)
            Load.data.append(tckt_dt)
