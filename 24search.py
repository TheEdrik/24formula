#!/usr/bin/python3

## https://fivethirtyeight.com/features/can-you-make-24/

import itertools, re

##--------------------------------------
## operations: add, subtract, multiply, divide, exponentiate (+ - * / ^)
##
## 1) three operations, between four numbers 
## 2) enumerate all operations
## 3) combine all possible four numbers
##    note: itertools.combinations() allows repetition ('3' twice), must filter
## 4) enumerate all possible parenthesis-pair combinations
## 5) evaluate generated formula, tolerating division-by-zero exceptions
##   5.1) report values matching 24
##
## encode parenthesis-pairs as bitmask (10 possible positions, 512..1):
##      (A .  B). C  . D    p =      256          +32
##      (A .  B . C) . D    p =      256                  +8
##     ((A .  B). C) . D    p = 512 +256          +32     +8
##      (A . (B . C)). D    p =      256      +64         +8 +4
##       A .  B .(C  . D)   p =                        16       +2
##       A . (B . C  . D)   p =                64               +2
##       A . (B .(C  . D))  p =                64     +16       +2 +1
##       A .((B . C) . D)   p =           128 +64         +8    +2
##      (A .  B).(C  . D)   p =      256          +32 +16       +2
##     ^^   ^^ ^ ^ ^^   ^^  --- possible paren positions  512,256, ... 2,1
##     512  128  16     2
##      256  64    8     1
##             32   4
##
## other parentheses positions are invalid or redundant,
## f.ex. "(A . (B . C) . D)" contains redundant external, parentheses;
## "(A . B .(C . D" is invalid.  Other equivalent combinations are not
## listed.
##
## final formula:
##    (    A   .    (    B   )    .    (    C    )   .    D   )
##    p0?  n0  op0  p1?  n1  p2?  op1  p3?  n2  p4?  op2  n3  p5?
##
def total24():
	OPS = '+-*/^'                                ## python3: ^ -> ** (expn)
	nrs = set(itertools.permutations('2334', 4))
					## permutation does not deduplicate 3's
	ops = list(itertools.product(OPS, OPS, OPS))
	prs = (256 +32, 256 +8, 512 +256 +32 +8, 256 +64 +8 +4, 16 +2, 64 +2,
	       64 +16 +2 +1, 128 +64 +8 +2, 256 +32 +16 +2)

	for n, o, p in itertools.product(nrs, ops, prs):
		if (o[0] +o[1] +o[2] == '^^^'):
			continue
				## cascade exponentiation, always >>24
				## evaluation may be slow, so early-terminate

						## construct expression string
		form = [
		         '('  if (p & 512)  else None,
		         '('  if (p & 256)  else None,

		         n[0], o[0],                          ## A .
		         '('  if (p & 128)  else None,
		         '('  if (p &  64)  else None,

		         n[1],                                ## B
		         ')'  if (p &  32)  else None,

		         o[1],                                ## .
		         '('  if (p &  16)  else None,

		         n[2],                                ## C
		         ')'  if (p &   8)  else None,
		         ')'  if (p &   4)  else None,

		         o[2], n[3],                          ## . D
		         ')'  if (p &   2)  else None,
		         ')'  if (p &   1)  else None,
		]

		fp = ' '.join(f  for f in form  if (f != None))
							## formula, printable

			## replace single-char mnemonics with python operators

		fe = re.sub('\^', '**', fp)
							## formula, eval-ready

		try:
			v = eval(fe)
				##
				## -X ^ (...fractional Y...) -> complex
				##
			if isinstance(v, complex) or not (23.995 <= v <= 24.005):
				print('## ', end='')

			print(f'{v} = {fp}')

		except ZeroDivisionError:
			print('## DIV0: ', fp)
		except SyntaxError:
			print('## INVD: ', fp)


##----------------------------------------------------------------------------
if __name__ == '__main__':
	total24()

