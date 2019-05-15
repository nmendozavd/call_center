import datetime
import time

"""
class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS

        Call.NUM_CALLS += 1

    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(new_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()
"""

class Call(object):
    num_calls = 1
    def __init__(self, caller_name, caller_number, reason):
        self.unique_id = Call.num_calls
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = datetime.datetime.now()
        self.reason = reason
        Call.num_calls += 1

    def display_info(self):
        print "ID: " + str(self.unique_id)
        print "Caller Name: " + str(self.caller_name)
        print "Caller Phone Number: " + str(self.caller_number)
        print "Time of Call: " + str(self.time_of_call)
        print "Reason for Call: " + str(self.reason)

class CallCenter(object):
    def __init__(self, *calls):
        self.calls = []
        self.queue_size = len(calls)
        for i in calls:
           self.calls.append(i)
    
    def add(self, call):
        self.calls.append(call)
        return self
    
    def remove(self):
        del self.calls[0]
        return self   

    def info(self):
        for i in range(len(self.calls)):
            print "Caller Name : " + self.calls[i].caller_name
            print "Caller Phone Number : " + self.calls[i].caller_number
            print "Queue size: "+ str(len(self.calls))
        return self
    
c1 = Call("Noel", "323-204-8567", "Refund Status")
c2 = Call("Kevin", "323-774-7759", "To Complain")
c3 = Call("Isabeth", "323-772-8357", "Defective Product")
#c3.display_info()

newCall = CallCenter(c1)
newCall.add(c1).add(c2).add(c3).remove()
newCall.info()

