class Flight:
    total_num_of_pass = 0
    total_num_of_fligt = 0

    def __init__(self, airline, num_of_pass) -> None:
        self.airline = airline
        self.num_of_pass = num_of_pass
        Flight.total_num_of_pass += num_of_pass
        Flight.total_num_of_fligt += 1
    
    def print_num_of_pass(self):
        print('Number of passengers of',
            self.airline, ':', self.num_of_pass)
    
    @classmethod
    def print_total_num(cls):
        print('Total number of passengers',
            cls.total_num_of_pass)
    
    @classmethod
    def print_avg_num_pass(cls):
        print('Average number of passengers: ',
            cls.total_num_of_pass/cls.total_num_of_fligt)

flight1 = Flight('SAS', 300)
flight2 = Flight('KLM', 200)
flight3 = Flight('Swiss', 100)

Flight.print_avg_num_pass()