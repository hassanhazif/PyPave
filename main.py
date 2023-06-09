from math import sin
from math import pi

# INPUT
#-------------------

N = 3 #Number of layers
E = [80000,25000,25000] #Elastic Modulus of the layers


#TRAFFIC AND LOADING
#-------------------

#Standard parameters (Ref: TRL615)

SSWL = 40000 # N (Single Standard wheel load)
CA_radius = 0.151 # m (Contact Area radius)
CA = pi*CA_radius**2 # sqm (Contact Area)

# Defines the function for the tire contact pressure for oblong shaped contact area
# Ref: Huang (2004) p28
# TCA - Tire Contact Area

def TCA_oblong(L):
    
    x = pi*(0.3*L)**2 + (0.4*L)*(0.6*L)

    return(x)


print ("Run successfully finished!")