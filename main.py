import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Input Data
#------------

T = 100 ## Traffic Level in msa
F = 3 ## Foundation class (1,2,3,4)
Mat = 1
# 1-Asphalt 40/60 
# 2-EME2 
# 3-HBGM-A 
# 4-HBGM-B 
# 5-HBGM-C 
# 6-HBGM-D

# Materials data Import
#-----------------------

AC = pd.read_csv("CSV\AC.csv",header=None)
EME2 = pd.read_csv("CSV\EME2.csv",header=None)
HBGM_A = pd.read_csv("CSV\HBGM_A.csv",header=None)
HBGM_B = pd.read_csv("CSV\HBGM_B.csv",header=None)
HBGM_C = pd.read_csv("CSV\HBGM_C.csv",header=None)
HBGM_D = pd.read_csv("CSV\HBGM_D.csv",header=None)

# Foundation Class and Traffic data Import
#-----------------------------------------

T1F1 = pd.read_csv("CSV\T1F1.csv",header=None)
T1F2 = pd.read_csv("CSV\T1F2.csv",header=None)
T1F3 = pd.read_csv("CSV\T1F3.csv",header=None)
T1F4 = pd.read_csv("CSV\T1F4.csv",header=None)
T2F2 = pd.read_csv("CSV\T2F2.csv",header=None)
T2F3 = pd.read_csv("CSV\T2F3.csv",header=None)
T2F4 = pd.read_csv("CSV\T2F4.csv",header=None)

print ("data import complete!")

# Traffic Data Logic
#-------------

if T <= 20:
    if F==1:
        print("Using T1F1")
        T_dat = T1F1
    elif F==2:
        print("Using T1F2")
        T_dat = T1F2
    elif F==3:
        print("Using T1F3")
        T_dat = T1F3
    elif F==4:
        print("Using T1F4")
        T_dat = T1F4
    else:
        print("invalid foundation class")

else:
    if F==1:
        print("Traffic class above 20msa cannot be supported by this foundation class!")
    elif F==2:
        print("Using T2F2")
        T_dat = T2F2
    elif F==3:
        print("Using T2F3")
        T_dat = T2F3
    elif F==4:
        print("Using T2F4")
        T_dat = T2F4
    else:
        print("invalid foundation class")

## Material Data Logic
##---------------------

if Mat == 1:
    print ("Using AC material")
    Mat_dat = AC
elif Mat == 2:
    print ("Using EME 2 Material")
    Mat_dat = EME2
elif Mat == 3:
    print ("Using HBGM A")
    Mat_dat = HBGM_A
elif Mat == 4:
    print ("Using HBGM B")
    Mat_dat = HBGM_B
elif Mat == 5:
    print ("Using HBGM C")
    Mat_dat = HBGM_C
elif Mat == 6:
    print ("Using HBGM D")
    Mat_dat = HBGM_D
else:
    print ("Invalid material class!")

## Interpolation
## -------------

df_T = pd.DataFrame(T_dat)
df_M = pd.DataFrame(Mat_dat)

#print(df_T)

I1=interp1d(df_T[1],df_T[0],kind='linear')
Y=I1(T)

I2=interp1d(df_M[0],df_M[1])

Thk = I2(Y)

print(Thk)

print ("Run Complete!")