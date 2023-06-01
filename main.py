from math import sin
from math import pi




SSWL = 40000 # N (Single Standard wheel load) Ref: TRL615
CA_radius = 0.151 # m (Contact Area radius) Ref: TRL615

# Defines the function for the tire contact pressure for oblong shaped contact area
# Ref: Huang (2004) p28
# Tire Contact Area (TCA)

def TCA_oblong(L):
    
    x = pi*(0.3*L)**2 + (0.4*L)*(0.6*L)

    return(x)

print(TCA_oblong(2))

