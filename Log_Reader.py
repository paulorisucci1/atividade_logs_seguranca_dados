
class Log_Reader:

    def __init__(self):
        self.__desired_log = None
        self.__start_line = None
        self.__finish_line = None
        self.__log_archives = {
            'system': '/var/log/syslog',
            'auth': '/var/log/auth.log',
            'boot': '/var/log/boot.log',
            'kernel': '/var/log/kern.log',
            'drivers': '/var/log/dmesg',
            'fail_log': '/var/log/faillog',
        }

    def read_file(self):
        self.__refresh_entries()

        try:
            self.__read_user_input()

            file = open(self.__log_archives[self.__desired_log])
            self.__print_lines(file)

            file.close()
        except Exception as e:
            print(e)

    def __print_lines(self, file):
        amount_of_lines = self.__start_line + self.__finish_line
        if self.__start_line is not None and self.__finish_line is not None:
            for line in file.readlines()[self.__start_line:amount_of_lines]:
                print(f'{line}')
        elif self.__start_line is not None:
            for line in file.readlines()[self.__start_line:]:
                print(f'{line}')
        else:
            for line in file.readlines():
                print(f'{line}')

    def __read_user_input(self):
        user_input = input('Type the chosen option, the start line and the amount of lines\nExample: auth 0 10\n')\
            .lower().split(' ')

        self.__validate_input(user_input)
        self.__desired_log = user_input[0]
        if len(user_input) > 1:
            self.__start_line = int(user_input[1])
        if len(user_input) > 2:
            self.__finish_line = int(user_input[2])


    def __validate_input(self, user_input):
        if user_input[0] not in self.__log_archives:
            raise Exception("The given input does not match any valid option")

        if len(user_input) == 2 and not(user_input[1].isnumeric()):
            raise Exception("The start line is invalid")

        if len(user_input) == 3 and (not(user_input[1].isnumeric()) or not(user_input[2].isnumeric())):
            raise Exception("The start line or the amount of lines are invalid")

    def __refresh_entries(self):
        self.__desired_log = None
        self.__start_line = None
        self.__finish_line = None
