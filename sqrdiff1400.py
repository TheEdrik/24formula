#!/usr/bin/python3

# fivethirtyeight.com and other puzzles: side-solution stubs

##--------------------------------------
## diff-of-squares solution for 1400
##
##     a^2 - b^2 = (a + b) (a - b) = 1400 = 2^3 * 5^2 * 7
## enumerate suitable (a+b), (a-b) pairs for 1400
##
## observation: a+b and a-b must be both even, since (1) they differ
## with 2b for integer b, therefore they are both odd or even
## while (2) their product is even.
##
## for some integer K divisor of 350,
##       a + b = 2 * K
##       a - b = 2 * (350 / K)
## possible K divisors: 1, 2, 5, 7, 10, 14, 25, 35, 50, 70, 175, 350
##
## a+b > a-b restricts valid values to K > 350/K; sqrt(350) =~ 18.7 so only
## 25, 35, 50, 70, 175, 350 are possible.  these choices of K generate the
## following solutions:
##     a=39, b=11
##                 a+b=50, a-b=28, K=25
##     a=45, b=25
##                 a+b=70, a-b=20, K=35
##     a=57, b=43
##                 a+b=100, a-b=14, K=50
##     a=75, b=65
##                 a+b=140, a-b=10, K=70
##     a=177, b=173
##                 a+b=350, a-b=4, K=175
##     a=351, b=349
##                 a+b=700, a-b=2, K=350
##
def sqrdiff1400():
##	ks = (1, 2, 5, 7, 10, 14, 25, 35, 50, 70, 175, 350)
	ks = list(k  for k in range(1, 350+1)  if ((350 % k) == 0))

	for K in ks:
		apb, amb = 2* K, 2* 350 // K            ## a+b, a-b
		if amb >= apb:
			continue

		a = (amb +apb) // 2
		b = apb -a

		print(f'a={ a }, b={ b }')
		print(f'            a+b={ apb }, a-b={ amb }, K={ K }')
		print()
		assert(1400 == a*a - b*b)


sqrdiff1400()

