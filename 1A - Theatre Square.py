from math import ceil

def numberOfFlagstones(n, m, a):
	return ceil(n/a)*ceil(m/a)
