num = int(input('Enter number: '))
n = int(input('Enter multiple of: '))

def RoundNumToNearestMultiple(num, n):
    x = 0              #x is the number of multiples of n
    L_N_M = 0
    x = num // n       #L_N_M is lower nearest multiple
    L_N_M = x * n
    H_N_M = L_N_M + n  #H_N_M is higher nearest multiple
    LM_diff = num - L_N_M
    HM_diff = H_N_M - num
    if HM_diff > LM_diff:
        rounding = L_N_M
    if LM_diff > HM_diff:
        rounding = H_N_M
    if LM_diff == HM_diff:
        rounding = H_N_M
    return rounding

print(RoundNumToNearestMultiple(num, n))
