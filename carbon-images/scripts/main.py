import numpy as np

def chapman_richards(age:float, b0:float, b1:float, b2:float):
    return (b0 * (1 - np.exp(-b1*age))) ** b2



# se_asia(age:100, hecters:100)
# -> obj w name, hectors, biomass