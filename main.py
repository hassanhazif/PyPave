from math import sin
from math import pi


# Defines the function for the tire contact pressure for oblong shaped contact area
# Huang (2004) p28
# Tire Contact Area (TCA)

def TCA_oblong(L):
    
    x = pi*(0.3*L)**2 + (0.4*L)*(0.6*L)

    return(x)

print(TCA_oblong(2))

