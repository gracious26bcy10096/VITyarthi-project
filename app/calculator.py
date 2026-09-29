def convert(amt, value1, value2):
    amt = float(amt)
    step1 = amt / value1
    step2 = step1 * value2
    return round(step2, 2)
