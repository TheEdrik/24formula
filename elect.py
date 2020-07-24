#!/usr/bin/python3

# Riddler Township voting, 2020-07-24
# fivethirtyeight.com/features/are-you-a-pinball-wizard/

# elect.py | sort -k +3n
#
# filter out lost elections: "grep -v ^-"

##----------------------------------------------------------------------------
## Oneshire    11   3
## Twoshire    21   4
## Threeshire  31   5
## Fourshire   41   6
## Fiveshire   51   7
## Sixshire    61   8
## Sevenshire  71   9
## Eightshire  81   10
## Nineshire   91   11
## Tenshire    101  12

ELECTORS = [
	[  11,  3, ],
	[  21,  4, ],
	[  31,  5, ],
	[  41,  6, ],
	[  51,  7, ],
	[  61,  8, ],
	[  71,  9, ],
	[  81, 10, ],
	[  91, 11, ],
	[ 101, 12, ],
]


##--------------------------------------
## searching for minimal number of citizen votes with majority
## electoral votes: assume 0/majority received in each shire
## (any additional citizen votes are considered lost/overkill here)
##
## search for the minimal number of 
##   1) achieve local majority---and nothing more---with each shire to win
##   2) safe to ignore any other shire with 0 citizen votes, since
##      those electors are already lost
##   3) filter shire-won combinations where electors are sufficient to win
##   4) sort combinations in increasing order of citizen votes
##
def election():
	majority = list((e[0] +1) //2  for e in ELECTORS)   ## for each shire
	voters   = sum(e[0] for e in ELECTORS)              ## nr. of citizens
	elmjr    = (sum(e[1] for e in ELECTORS) +1) //2     ## elector majority

				## enumerate shires with majority won; bitmask
				## bit #N on if won majority in shire #N
				##
	for won in range(1 << len(ELECTORS)):
		wbm = list(won & (1 << e)  for e in range(len(ELECTORS)))
				## bitmask -> unpacked bit array

				## citizen+electoral votes, per-shire
				## 0 if did not win that shire

		civ = list(majority[b]     if wbm[b]  else 0
		           for b in range(len(ELECTORS)))

		elv = list(ELECTORS[b][1]  if wbm[b]  else 0
		           for b in range(len(ELECTORS)))

		if (sum(elv) < elmjr):
			print("-", end='')            ## mark lost-election row

				## nr. of electoral votes, nr. of citizen votes,
				## percentage, list of per-shire citizen votes,
				## nr. of winning-party electors
				##
		print(f"{sum(elv)} {sum(civ)} " +
		      f"{100.0 * sum(civ) /voters:.02f}% "
		      f"votes={civ} electors={elv}")

election()

