# Coin Flip

### Challenge
> Keith has been very bored with his job as an industrial couponer lately, and so he has decided to spend his time flipping coins. The results of his coin flips are [in this file](data.txt). Keith now wants to know how many runs of flips he found. A run is any consecutive sequence of the same flip. For example, the flips 001111101011 have three runs of length one, two runs of length two, and one run of length five. Can you help Keith count runs? The flag is the number of runs of length one, the number of runs of length two, the number of runs of length three, etc. up to the longest run in the sequence, each separated by a comma and a space. 


### Solution

My idea is to split up the string every end of consecutive characters.
	
	001111101011 -> {00, 11111, 0, 1, 0, 11}

Afterwhich, we count the lengths of each item in the list and keep track of it in a dictionary.
Finally, we join the lengths in order with ', ' as the delimiter.

_(See [analyse.py](analyse.py) on how it is done)_

Now, run it on `data.txt` and we get this output flag

	249369, 124813, 62558, 31389, 15475, 7891, 3975, 1982, 943, 486, 270, 107, 64, 33, 15, 8, 4, 1, 1, 1