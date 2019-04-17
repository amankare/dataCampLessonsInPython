#Random float
#Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

#All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, you'll be using two functions from this package:

#seed(): sets the random seed, so that your results are the reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
#rand(): if you don't specify any arguments, it generates a random float between zero and one.

_____

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

_____

#Roll the dice
#In the previous exercise, you used rand(), that generates a random float between 0 and 1.

#As Filip explained in the video you can just as well use randint(), also a function of the random package, to generate integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.

import numpy as np
np.random.randint(4, 8)
#Numpy has already been imported as np and a seed has been set. Can you roll some dice?

_____

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
a = np.random.randint(1,7)
print(a)

# Use randint() again
print(np.random.randint(1,7))



