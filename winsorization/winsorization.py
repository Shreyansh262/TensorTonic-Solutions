import math

def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    low = ((len(values)) - 1)*lower_pct/100
    high = ((len(values)) - 1)*upper_pct/100
    val_low = values[math.floor(low)] + (low-math.floor(low))*(values[math.ceil(low)] - values[math.floor(low)])
    val_high = values[math.floor(high)] + (high-math.floor(high))*(values[math.ceil(high)] - values[math.floor(high)])
    for i in range(len(values)):
        if values[i] < val_low:
            values[i] = val_low
        elif values[i] > val_high:
            values[i] = val_high
    return values