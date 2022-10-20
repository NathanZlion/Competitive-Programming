def numberOfFlagstones(n, m, a):
    if n%a==0:
      xNum=n//a
    else:
      xNum=n//a +1
    if m%a==0:
      yNum=m//a
    else:
      yNum=m//a+1
    return xNum * yNum
