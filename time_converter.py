from datetime import datetime

time = input("Enter time your want to convert: ")

def time_parser(self, time):
    start_period = time.split('T')[0]
    start_period_obj = datetime.strptime(start_period, "%Y-%m-%d")
    # line 9 is set to output the format DD-MMM-YY you can adjust this to suit your desired output
    new_format = start_period_obj.strftime("%d-%b-%y")
    print('The converted date is')
    print(new_format)
    # return new_format

time_parser(time,time)    