"""
RECURSION LAB
You need to design an iterative and a recursive function called replicate_iter
and replicate_recur respectively which will receive two arguments: times which
is the number of times to repeat and data which is the number or string to be repeated.

The function should return an array containing repetitions of the data argument.
For instance, replicate_recur(3, 5) or replicate_iter(3,5) should return [5,5,5].
If the times argument is negative or zero, return an empty array. If the argument
is invalid, raise a ValueError.
"""

def replicate_iter(times, data):
        if((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
                raise ValueError("Invalid arguments")
        elif(times <= 0):
                return []
        else:
                array = []
                for x in range(times):
                        array.append(data)
                return array

	
def replicate_recur(times, data):
        if((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
                raise ValueError("Invalid arguments")
        elif(times <= 0):
                return []
        else:
                return ([data] + replicate_recur((times - 1), data))        
