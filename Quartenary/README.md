# Quartenary

### Challenge
> What is the flag?

> 1310122012111303121113131233130212101303120113021211130013111310122012111302121113101233121212211230123013031300120112031211023211101220122113031303121112321310121112321203121112211232131012111232131012211233123212011230123013211230121112121310120212301201123212230232131012201211121212301201121312211303032213131220132112101233121113031232123312331232121113111303121112021201130312111212123313111302
Hint: If you think you are close but it is not working, try adding a leading zero. 

### Solution

From the name of the challenge, and from close inspection, we can see it is in base-4 (digits 0, 1, 2, 3).
I'm guessing it is a base-4 ASCII string.

Now with this, since an ASCII character is 8-bits or 2 hex-pairs, it is 4 digits of base-4.
We first split the provided string into a list of 4 digits each
	
	 re.findall('....', input)

After which, we need some background knowledge of base-4:

	  33 base-4 = 0x0F
	3333 base-4 = 0xFF
	  10 base-4 = 4 decimal
	 100 base-4 = 16 decimal

Knowing this, we can form our own base-4 calculation and then convert it into ASCII
_(See [base4-to-ascii.py](base4-to-ascii.py))_

Input the given number and we get this sentence

	thesewordsareputheretofillspace.Thissentenceintentionallyleftblank.theflagis:whydoesnooneusebasefour

And the flag is `whydoesnooneusebasefour`
