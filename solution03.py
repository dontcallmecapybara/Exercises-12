class Date:
    '''
    Class of date.

    Attributes
    ----------
    months (dict): The dictionary with number of month (key) and its name (value).
    days_31 (list): The list with number of months which have 31 days.
    days_30 (list): The list with number of months which have 30 days.

    Parameters
    ----------
    date (str): Date entered by user.

    Prints
    ------
    Date if it is correct or None if it is not correct.
    '''


    months = {
        '01': 'янв',
        '02': 'фев',
        '03': 'мар',
        '04': 'апр',
        '05': 'май',
        '06': 'июн',
        '07': 'июл',
        '08': 'авг',
        '09': 'сен',
        '10': 'окт',
        '11': 'ноя',
        '12': 'дек'
    }

    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    def __init__(self, date):
        if self.check_date(date):
            self.__date = date
        else:
            self.__date = None
            print('ошибка')
            
    date = property()

    @date.getter
    def date(self):
        '''
        The 'date' property getter.

        Returns
        -------
            str: A string representation of the date in the format 'day month year' if the date is set.
            None: If the date is not set.
        '''


        return f'{int(self.__date[:2])} {Date.months[self.__date[3:5]]} {self.__date[6:]} г.' if self.__date != None else None

    @date.setter
    def date(self, new_date):
        '''
        The 'date' property setter.

        Parameters
        ----------
        new_date (str): The new date.

        Modifies
        --------
        If 'new_date' is valid, it is assigned to 'self.__date'.

        Prints
        ------
        If 'new_date' is not valid, prints 'ошибка'.
        '''


        if self.check_date(new_date):
            self.__date = new_date
        else:
            self.__date = None
            print('ошибка')
    
    def is_leap_year(self, year_str):
        '''
        Checks for leap year.

        Parameters
        ----------
        year_str (str): The year to be checked.

        Returns
        -------
            True: if 'year_str' is a leap year.
            False: If 'year_str; is not a leap year.
        '''


        year = int(year_str)
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            if year % 100 != 0:
                return True
            else:
                return False
        else:
            return False


    def check_date(self, date):
        '''
        Checks the date for correctness.

        Parameters
        ----------
        date (str): The date to be checked.

        Returns
        -------
            True: If date is correct.
            False: If date is not correct.
        '''


        if isinstance(date, str):
            if date[3:5] == '02':
                if self.is_leap_year(date[6:]):
                    if 0 < int(date[:2]) <= 29:
                        return True
                    else:
                        return False
                else:
                    if 0 < int(date[:2]) <= 28:
                        return True
                    else:
                        return False
            elif int(date[3:5]) in Date.days_31:
                if 0 < int(date[:2]) <= 31:
                    return True
                else:
                    return False
            elif int(date[3:5]) in Date.days_30:
                if 0 < int(date[:2]) <= 30:
                    return True
                else:
                    return False
    
    def to_timestamp(self):
        '''
        Calculates amount of seconds from '01.01.1970' to current date.

        Returns
        -------
        result (int): Amount of seconds from '01.01.1970' to current date.
        '''


        result = 0
        for year in range(1970, int(self.__date[6:])):
            if self.is_leap_year(year):
                result += 86400 * 366
            else:
                result += 86400 * 365

        for month in range(1, int(self.__date[3:5])):
            if month == 2:
                if self.is_leap_year(self.__date[6:]):
                    result += 86400 * 29
                else:
                    result += 86400 * 28
            elif month in Date.days_31:
                result += 86400 * 31
            elif month in Date.days_30:
                result += 86400 * 30
            
        for day in range(1, int(self.__date[:2])):
            result += 86400
        
        return result
    
    def __eq__(self, other):
        return self.to_timestamp() == other.to_timestamp()
    
    def __ne__(self, other):
        return self.to_timestamp() != other.to_timestamp()
    
    def __lt__(self, other):
        return self.to_timestamp() < other.to_timestamp()
    
    def __le__(self, other):
        return self.to_timestamp() <= other.to_timestamp()
    
    def __gt__(self, other):
        return self.to_timestamp() > other.to_timestamp()
    
    def __ge__(self, other):
        return self.to_timestamp() >= other.to_timestamp()

    def __str__(self):
        return self.date if self.__date != None else 'None'


class Load:
    '''
    Class of loading files.
    '''
    

    def write(file_1, file_2, file_3):
        '''
        Reads 3 files and uploading data from it.
        '''


        with open(file_1, 'r', encoding='UTF-8') as f:
            for line in [line.strip() for line in f.readlines()][1:]:
                id, date, title = line.split(';')[:-1]
                Meeting.lst_meeting.append(Meeting(int(id), Date(date), title))

        with open(file_2, 'r', encoding='UTF-8') as f:
            for line in [line.strip() for line in f.readlines()][1:]:
                id, nick_name, first_name, last_name, middle_name, gender = line.split(';')[:-1]
                User.lst_users.append(User(int(id), nick_name, first_name, last_name, middle_name, gender))

        with open(file_3, 'r', encoding='UTF-8') as f:
            for line in [line.strip() for line in f.readlines()][1:]:
                id_meet, id_pers = line.split(';')[:-1]
                for meet in Meeting.lst_meeting:
                    if meet.id == int(id_meet):
                        for user in User.lst_users:
                            if user.id == int(id_pers):
                                meet.employees.append(user)


class User:
    '''
    Class of users.

    Attributes
    ----------
    lst_users (list): List of users.
    '''


    lst_users = []

    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


class Meeting:
    '''
    Class of Meeting.

    Attributes
    ----------
    lst_meeting (list): List of meetings.

    Parameters
    ----------
    id (str): Meetings id.
    date (str): Meetings date.
    title (str): Meetings title.

    Prints
    ------
    Information about meetings in special form.
    '''


    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id
        self.date = date
        self.title = title
        self.employees = []
    
    def add_person(self, person):
        '''
        Adds a person to list of employees for meeting.
        '''


        self.employees.append(person)

    def count(self):
        '''
        Returns number of employees on meeting.
        '''


        return len(self.employees)

    @staticmethod
    def count_meeting(date):
        '''
        Returns number of meetings.
        '''


        count = 0
        for meet in Meeting.lst_meeting:
            if meet.date == date:
                count += 1
        
        return count

    @staticmethod
    def total():
        '''
        Returns number of all employees.
        '''


        count = 0
        for meet in Meeting.lst_meeting:
            count += len(meet.employees)

        return count

    def __repr__(self):
        result = ''

        result += f'Рабочая встреча {Meeting.lst_meeting.index(self) + 1}\n'
        result += f'{self.date} {self.title}\n'

        for employee in self.employees:
            if employee.gender:
                employee_str = (f'ID: {employee.id} '
                                f'LOGIN: {employee.nick_name} '
                                f'NAME: {employee.first_name} {employee.middle_name} {employee.last_name} '
                                f'GENDER: {employee.gender}')
            else:
                employee_str = (f'ID: {employee.id} '
                                f'LOGIN: {employee.nick_name} '
                                f'NAME: {employee.first_name} {employee.middle_name} {employee.last_name}')

            employee_str = ' '.join(employee_str.split())
            employee_str += '\n'
            result += employee_str

        return result
