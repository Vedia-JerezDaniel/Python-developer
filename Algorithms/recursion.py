# Recursion, which originates from the Latin verb, “recurrere” means to “run back”...
# and this is what the program we’re going to write together is going to do- run back to itself,
# over and over, as many times as it needs to until the program terminates.

# ____________________________________________________EXAMPLES__________________________________________________________

# FACTORIALS

def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print(iterative_factorial(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        return temp * n

print(recur_factorial(5))


# Two-line recursive program to calculate factorial
def recur_factorial(n):
    if n == 1: 
        return n
    else: 
        return n * recur_factorial(n - 1)

print(recur_factorial(5))


# PERMUTATIONS

# ITERATIVE PROGRAM FOR PERMUTATIONS

from math import factorial


def permutations(str):
    for _ in range(factorial(len(str))):
        print(' '.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp

s = 'limes'
s = list(s)
permutations(s)


# RECURSIVE PROGRAM FOR PERMUTATIONS

def permute(string, pocket=" "):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range((len(string))):
            letter = string[i]
            front = string[:i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)
            
print(permute("LIMES", " "))


# NO PROGRAM WAS DISCUSSED FOR N-QUEENS PROBLEM

forvalues j=1/2 {
	forvalues i=1/6 {
		foreach c in boom slump {
		
	* the dummy for the U.S. is dropped to avoid collinearity with the constant
	
	* (a) Uniform effect of d.CAPB changes
	reg ly`i'   fAA ///
		hply dml0dly dml1dly dmdumiso1-dmdumiso16  ${fe`j'} ///
		if `c'==1 & year>=1980 & year<=2007, cluster(iso)
	eststo `c'`i'`j'
	if `i'==6 & "`c'"=="Hi" & `j'==2 {
		gen s_ols = e(sample)
		}
	}
}



forvalues j=1/2 {
	forvalues i=1/6 {
		foreach c in boom slump {
		
	* the dummy for the U.S. is dropped to avoid collinearity with the constant
	
	* (a) Uniform effect of d.CAPB changes
	reg ly`i'   fAA ///
		# hply dml0dly dml1dly dmdumiso1-dmdumiso16  ${fe`j'} ///
		if `c'==1 & year>=1980 & year<=2007, cluster(iso)
	eststo `c'`i'`j'
	

	}
}

	forvalues i=1/6 {
		foreach c in boom slump {
	
	* (a) Uniform effect of d.CAPB changes
	reg ly`i'   fAA ///
		hply dml0dly dml1dly dmdumiso1-dmdumiso16 ${fe`j'} ///
		if `c'==1 & year>=1980 & year<=2007, cluster(iso) 
	eststo `c'`i'`j'
	if `i'==6 & "`c'"=="Hi" & `j'==2 {
		gen s_ols = e(sample)
		}
	
	* (b) Separate effects of d.CAPB for Large( >1.5%) and Small (<= 1.5%) changes
	reg ly`i'   smfAA lgfAA ///
		hply dml0dly dml1dly dmdumiso1-dmdumiso16 ${fe`j'} ///
		if `c'==1 & year>=1980 & year<=2007, cluster(iso) 
	eststo `c'`i'lgsm`j'
	}
}

label var fAA "Fisc multiplier, y = boom"

esttab boom1`j' boom2`j' boom3`j' boom4`j' boom5`j' boom6`j' ///
	using ../tables/Table`t`j''.tex , f replace keep(fAA) ///
	b(2) se(2) sfmt(2) obslast se label star(* 0.10 ** 0.05 *** 0.01)

label var fAA "Fisc multiplier, y = slump"

esttab slump1`j' slump2`j' slump3`j' slump4`j' slump5`j' slump6`j' ///
	using ../tables/Table`t`j''.tex , f a keep(fAA) ///
	b(2) se(2) sfmt(2) obslast se label star(* 0.10 ** 0.05 *** 0.01)  nomtitles nonum



label var lgfAA "Fiscal multiplier, large change, y = boom"
label var smfAA "Fiscal multiplier, small change, y = boom"

esttab boom1lgsm`j' boom2lgsm`j' boom3lgsm`j' boom4lgsm`j' boom5lgsm`j' boom6lgsm`j' ///
	using ../tables/Table`t`j''.tex , f a keep(lgfAA smfAA) order(lgfAA smfAA) ///
	b(2) se(2) sfmt(2) obslast se label star(* 0.10 ** 0.05 *** 0.01)  nomtitles nonum

label var lgfAA "Fiscal multiplier, large change, y = slump"
label var smfAA "Fiscal multiplier, small change, y = slump"

esttab slump1lgsm`j' slump2lgsm`j' slump3lgsm`j' slump4lgsm`j' slump5lgsm`j' slump6lgsm`j' ///
	using ../tables/Table`t`j''.tex , f a keep(lgfAA smfAA) order(lgfAA smfAA) ///
	b(2) se(2) sfmt(2) obslast se label star(* 0.10 ** 0.05 *** 0.01)  nomtitles nonum

	
}