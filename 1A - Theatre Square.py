from math import ceil

def numberOfFlagstones(n, m, a):
	x=ceil(n/a)
	y=ceil(m/a)
	return x*y
