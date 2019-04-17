#We're going to code a while loop that implements a very basic control system for an inverted pendulum. 
#If there's an offset from standing perfectly straight, the while loop will incrementally fix this offset.

_____

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
    
_____

#The while loop that corrects the offset is a good start, but what if offset is negative? 
#You can try to run the sample code on the right where offset is initialized to -6, but your sessions will be disconnected. The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.
#Fix things by putting an if-else statement inside the while loop.

_____

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset < 0:
        offset = offset + 1
    else:
        offset = offset - 1
    print(offset)
    
