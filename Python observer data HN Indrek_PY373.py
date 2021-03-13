# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:50:09 2019 run in Python 3.7.3

@author: Eelke Snoeren

THIS PYTHON SCRIPT WILL CREATE A RESULT EXCEL-FILE
FROM RAW DATA FROM OBSERVER. IT IS DEVELOPED ON HN002, THE PROSOCIAL BEHAVIOR DATA.

TO DO BEFOREHAND
1) CHANGE THE PATH OF PYTHON TO YOUR DATA FOLDER 
2) CHANGE THE PATH AND FILENAME TO THE RIGHT RESULTS DOCUMENT
3) FILL IN TREATMENT GROUPS (if your have more than 6, the program needs adjustments)
6) MATCH X-AX SCALE TO NUMBER OF TREATMENT GROUPS
7) CHECK WHETHER THE COLUMNS ARE THE SAME AS MENTIONED
8) FILL IN THE BEHAVIORS YOU SCORE FROM BA-BZ
9) FILL OUT YOUR OBSERVATION NAMES AS THEY WERE IN OA-OZ
10) FILL OUT YOUR RATCODE IN EF/EM
11) CHECK WHETHER ALL RATS EXIST; OTHERWISE CHANGE YOUR EXCEL FILE


haal tijd fight eraf
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from itertools import chain
sns.set()
from PIL import Image
import glob
import os
from matplotlib.backends.backend_pdf import PdfPages
import multiprocessing as mp

# Define the directory in which you stored the data (use / instead of \)
directory= "C:/Users/esn001/Documents/python/Python 3.8/Data projects/HN Indrek"

# Define the directory from which the files should come
os.chdir(directory)

# Define output file names
out_path1 = "%s/Output/HN002_results.xlsx" % directory
out_path2 = "%s/Output/HN002_resultspermin.xlsx" % directory
out_path3 = "%s/Output/HN002_resultsmod.xlsx" % directory
out_path4 = "%s/Output/HN002_resultsmodtreat.xlsx" % directory
out_path5 = "%s/Output/HN002_statistics.xlsx" % directory
out_path6 = "%s/Output/HN002_testresults.xlsx" % directory



# Load all excel files in the folder into one DataFrame and clean up
dataraw = pd.DataFrame()
for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f)
    dataraw = dataraw.append(df,ignore_index=True,sort=False)

dataraw = dataraw.dropna(axis=0, how='all')
dataraw = dataraw.reset_index()

# Take a look at your data
#dataraw.shape
#dataraw.head()
#dataraw.tail()

## now save the data frame to excel
#writer4 = pd.ExcelWriter(out_path4, engine='xlsxwriter')
#data.to_excel(writer4, sheet_name='data')
#writer4.save()
#writer4.close()

# Fill out your short column names behind the definition a-z
#AA='nix'
A='Index'
B='Index'
C='Unimportant'
D='Unimportant'
E='Unimportant'
F='Unimportant'
G='Time_hmsf'
H='Time_hms'
I='Unimportant'
J='Time'
K='Unimportant'
L='Observation'
M='Event_log'
N='Subject_raw'
O='Behavior'
P='Modifier1'
Q='Modifier2' 
R='Modifier3'
S='Modifier4'
T='Modifier5'
U='Modifier6'
V='Modifier7'
W='Modifier8'
X='Modifier9'
Y='Modifier10'
Z='Modifier11'
XA='Modifier12'
XB='Modifier13'
XC='Event_type' 
XD='Comment'
XE='Modifier14'
XF='RatID'
XG='ModID'
XH='Treatment'
XI='Treatment_mod'
XJ='Sex_mod'
XK='Treat_mod'
XL='Mod_loc'
XM='Mod_winner'
XN='RatID_witness'
XO='RatID_witness_plus'

# Fill out your treatment/stimulus behind definition SA-SZ
SA='CTR-females'
SB='FLX-females'
SC='CTR-males'
SD='FLX-males'
SE='Stimulus4'
SF='Stimulus5' 

Stimuli_values= (SA,SB,SC,SD)

# Fill out your ratcode for each Experimental Female or Male 
# (e.g. EF21 is female 1 in experiment 2, EM32 is male 2 in experiment 3)
EF11='FF2'
EF12='FF1'
EF13='FC1'
EF14='FC2'
EF21='FF3'
EF22='FC3'
EF23='FF4'
EF24='FC4'
EF31='FC6'
EF32='FF6'
EF33='FC5'
EF34='FF5'
EF41='FC8'
EF42='FC7'
EF43='FF7'
EF44='FF8'
EF51='FF9'
EF52='FC10'
EF53='FC9'
EF54='FF10'
EM11='MC2'
EM12='MF1'
EM13='MC1'
EM14='MF2'
EM21='MC3'
EM22='MF3'
EM23='MC4'
EM24='MF4'
EM31='MC5'
EM32='MF6'
EM33='MC6'
EM34='MF5'
EM41='MF7'
EM42='MC8'
EM43='MC7'
EM44='MF8'
EM51='MF10'
EM52='MC9'
EM53='MC10'
EM54='MF9'

ratcodes=(EM11,EM12,EM13,EM14,EM31,EM32,EM33,EM34,EM41,EM42,EM43,EM44,EM51,EM52,
          EM53,EM54,EF11,EF12,EF13,EF14,EF31,EF32,EF33,EF34,EF41,EF42,EF43,EF44,
          EF51,EF52,EF53,EF54)

# Fill out your behavioral observations behind definition BA-BZ
BA='Resting/immobile'
BB='Walking'
BC='Sniffing anogenitally'
BD='Sniffing others'
BE='Self grooming'
BF='Self grooming near others'
BG='Grooming others'
BH='Walk over/under others'
BI='Resting with others'
BJ='Rearing' #not used
BK='Running' #not used
BL='non-social exploration'
BM='Nose-off'
BN='Fighting with other'
BO='Boxing'
BP='Kicking'
BQ='wrestling'
BR='Flee'
BS='Chasing (after fight)'
BT='Rattling the tail' #not used
BU='Defensive stance'
BV='In opening facing open field'
BW='In opening facing burrow'
BX='Drinking'
BY='Freezing' #not used
BZ='Freezing with others' #not used
BBA='Approach'
BBB='Pursuing/chasing' #not used
BBC='Rejection' #not used
BBD='Food transport' #not used
BBE='Digging/moving bedding/nesting material/wood'
BBF='Carrying nesting materials/wood'
BBG='Chewing wood' #not used
BBH='Eating'
BBI='Hiding' 
BBJ='Hiding with others'
BBK='irrelevant' #not used

# Fill in your extra behavioral calculations behind definition EA-EZ
EA='Active social behavior' # Grooming others + Sniffing others + Sniffing anogenitally
EB='Passive social behavior' # resting with others, hiding with others
EC='Social context' # Active social behavior + passive social behavior + self grooming near others
ED='General active' # Walking + walking over + non-social exploration
EE='General passive' # Resting + resting near others + hiding + hiding near others
EF='Conflict behavior' # Nose-off + fighting + boxing + kicking + wrestling + defensive posture + fleeing + chasing 
EG='Selfgrooming' # selfgrooming alone and with others

# Make a list of the standard behaviors and the to be calculated behaviors
list_behaviors=list((BA,BB,BC,BD,BE,BF,BG,BH,BI,BL,BM,BN,BO,BP,BQ,BR,BS,BU,BV,BW,BX,BBA,BBE,BBF,BBH,BBI,BBJ))
list_behaviors_social =list((BC,BD,BF,BG,BI,BM,BN,BO,BP,BQ,BR,BS,BU,BBA,BBJ))
list_behaviors_extra=list((EA,EB,EC,ED,EE,EF,EG))
list_results=list((EA,EB,EC,ED,EE,EF,EG,BA,BB,BC,BD,BE,BF,BG,BH,BI,BL,BM,BN,BO,BP,BQ,BR,BS,BU,BV,BW,BX,BBA,BBE,BBF,BBH,BBI,BBJ))
list_results_social=list((EA,EB,EC,EF,BC,BD,BF,BG,BI,BM,BN,BO,BP,BQ,BR,BS,BU,BBA,BBJ))

# Fill out your observation names, so that they can be splitted in the right experiment
#OA= 
# Rename columns (add or remove letters according to number of columns)
dataraw.columns = [B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,XA,XB,XC,XD,XE]

# Make a new datafile with selected columns
data=dataraw[[J,L,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,XA,XB,XC,XE]]

## now save the data frame to excel
#writer4 = pd.ExcelWriter(out_path4, engine='xlsxwriter')
#data.to_excel(writer4, sheet_name='data')
#writer4.save()
#writer4.close()

## Check whether all behaviors are in the final document, if not relevant remove from above lists
#behaviors_in=list(data.Behavior.unique())
#def returnNotMatches(a, b):
#    return ((x for x in b if x not in a))
#
#missing= list(returnNotMatches(behaviors_in,list_behaviors))
#for i in missing:
#    print(i)

# Make a column for the experiment number
data=data.assign(Fight =lambda x: data.Observation.str.split('\s+').str[-1])
data=data.assign(Cohort_pre1 =lambda x: data.Observation.str.split('\s+').str[0])
data=data.assign(Cohort_pre2 =lambda x: data.Cohort_pre1.str.split('extra-').str[-1])
data=data.assign(Cohort_pre3 =lambda x: data.Cohort_pre1.str.split('-').str[0])
data['Extra']=np.where(data['Cohort_pre3']=='extra',2,1)
data=data.assign(Cohort =lambda x: data.Cohort_pre2.str.split("").str[4])
data=data.assign(Day =lambda x: data.Cohort_pre2.str.split("").str[6])

# Create fake fight where there is data missing per rat
data.loc[data['Fight'].isnull(),'Fight'] = "nodata"

# Create dataframes for RATID for the RATS subject based on experiments 
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='F1'),EF11, "")
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='F2'),EF12, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='F3'),EF13, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='F4'),EF14, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='M1'),EM11, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='M2'),EM12, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='M3'),EM13, data[XF])
data[XF]=np.where((data['Cohort']=='1')&(data[N]=='M4'),EM14, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='F1'),EF31, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='F2'),EF32, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='F3'),EF33, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='F4'),EF34, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='M1'),EM31, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='M2'),EM32, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='M3'),EM33, data[XF])
data[XF]=np.where((data['Cohort']=='3')&(data[N]=='M4'),EM34, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='F1'),EF41, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='F2'),EF42, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='F3'),EF43, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='F4'),EF44, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='M1'),EM41, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='M2'),EM42, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='M3'),EM43, data[XF])
data[XF]=np.where((data['Cohort']=='4')&(data[N]=='M4'),EM44, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='F1'),EF51, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='F2'),EF52, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='F3'),EF53, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='F4'),EF54, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='M1'),EM51, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='M2'),EM52, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='M3'),EM53, data[XF])
data[XF]=np.where((data['Cohort']=='5')&(data[N]=='M4'),EM54, data[XF])

# Create dataframes for MODID for the MODIFIER subject based on experiments 
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='F1')|(data[Q]=='F1')|
        (data[R]=='F1')|(data[S]=='F1')|(data[T]=='F1')|(data[U]=='F1')|(data[V]=='F1')|
        (data[W]=='F1')|(data[X]=='F1')|(data[Y]=='F1')|(data[Z]=='F1')|(data[XA]=='F1')|
        (data[XB]=='F1')|(data[XE]=='F1')),EF11, "")
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='F2')|(data[Q]=='F2')|
        (data[R]=='F2')|(data[S]=='F2')|(data[T]=='F2')|(data[U]=='F2')|(data[V]=='F2')|
        (data[W]=='F2')|(data[X]=='F2')|(data[Y]=='F2')|(data[Z]=='F2')|(data[XA]=='F2')|
        (data[XB]=='F2')|(data[XE]=='F2')),EF12, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='F3')|(data[Q]=='F3')|
        (data[R]=='F3')|(data[S]=='F3')|(data[T]=='F3')|(data[U]=='F3')|(data[V]=='F3')|
        (data[W]=='F3')|(data[X]=='F3')|(data[Y]=='F3')|(data[Z]=='F3')|(data[XA]=='F3')|
        (data[XB]=='F3')|(data[XE]=='F3')),EF13, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='F4')|(data[Q]=='F4')|
        (data[R]=='F1')|(data[S]=='F4')|(data[T]=='F4')|(data[U]=='F4')|(data[V]=='F4')|
        (data[W]=='F1')|(data[X]=='F4')|(data[Y]=='F4')|(data[Z]=='F4')|(data[XA]=='F4')|
        (data[XB]=='F1')|(data[XE]=='F4')),EF14, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='M1')|(data[Q]=='M1')|
        (data[R]=='M1')|(data[S]=='M1')|(data[T]=='M1')|(data[U]=='M1')|(data[V]=='M1')|
        (data[W]=='M1')|(data[X]=='M1')|(data[Y]=='M1')|(data[Z]=='M1')|(data[XA]=='M1')|
        (data[XB]=='M1')|(data[XE]=='M1')),EM11, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='M2')|(data[Q]=='M2')|
        (data[R]=='M2')|(data[S]=='M2')|(data[T]=='M2')|(data[U]=='M2')|(data[V]=='M2')|
        (data[W]=='M2')|(data[X]=='M2')|(data[Y]=='M2')|(data[Z]=='M2')|(data[XA]=='M2')|
        (data[XB]=='M2')|(data[XE]=='M2')),EM12, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='M3')|(data[Q]=='M3')|
        (data[R]=='M3')|(data[S]=='M3')|(data[T]=='M3')|(data[U]=='M3')|(data[V]=='M3')|
        (data[W]=='M3')|(data[X]=='M3')|(data[Y]=='M3')|(data[Z]=='M3')|(data[XA]=='M3')|
        (data[XB]=='M3')|(data[XE]=='M3')),EM13, data[XG])
data[XG]=np.where((data['Cohort']=='1')&((data[P]=='M4')|(data[Q]=='M4')|
        (data[R]=='M1')|(data[S]=='M4')|(data[T]=='M4')|(data[U]=='M4')|(data[V]=='M4')|
        (data[W]=='M1')|(data[X]=='M4')|(data[Y]=='M4')|(data[Z]=='M4')|(data[XA]=='M4')|
        (data[XB]=='M1')|(data[XE]=='M4')),EM14, data[XG])

data[XG]=np.where((data['Cohort']=='3')&((data[P]=='F1')|(data[Q]=='F1')|
        (data[R]=='F1')|(data[S]=='F1')|(data[T]=='F1')|(data[U]=='F1')|(data[V]=='F1')|
        (data[W]=='F1')|(data[X]=='F1')|(data[Y]=='F1')|(data[Z]=='F1')|(data[XA]=='F1')|
        (data[XB]=='F1')|(data[XE]=='F1')),EF31, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='F2')|(data[Q]=='F2')|
        (data[R]=='F2')|(data[S]=='F2')|(data[T]=='F2')|(data[U]=='F2')|(data[V]=='F2')|
        (data[W]=='F2')|(data[X]=='F2')|(data[Y]=='F2')|(data[Z]=='F2')|(data[XA]=='F2')|
        (data[XB]=='F2')|(data[XE]=='F2')),EF32, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='F3')|(data[Q]=='F3')|
        (data[R]=='F3')|(data[S]=='F3')|(data[T]=='F1')|(data[U]=='F3')|(data[V]=='F3')|
        (data[W]=='F3')|(data[X]=='F3')|(data[Y]=='F1')|(data[Z]=='F3')|(data[XA]=='F3')|
        (data[XB]=='F3')|(data[XE]=='F3')),EF33,data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='F4')|(data[Q]=='F4')|
        (data[R]=='F1')|(data[S]=='F4')|(data[T]=='F4')|(data[U]=='F4')|(data[V]=='F4')|
        (data[W]=='F1')|(data[X]=='F4')|(data[Y]=='F4')|(data[Z]=='F4')|(data[XA]=='F4')|
        (data[XB]=='F1')|(data[XE]=='F4')),EF34, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='M1')|(data[Q]=='M1')|
        (data[R]=='M1')|(data[S]=='M1')|(data[T]=='M1')|(data[U]=='M1')|(data[V]=='M1')|
        (data[W]=='M1')|(data[X]=='M1')|(data[Y]=='M1')|(data[Z]=='M1')|(data[XA]=='M1')|
        (data[XB]=='M1')|(data[XE]=='M1')),EM31, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='M2')|(data[Q]=='M2')|
        (data[R]=='M2')|(data[S]=='M2')|(data[T]=='M2')|(data[U]=='M2')|(data[V]=='M2')|
        (data[W]=='M2')|(data[X]=='M2')|(data[Y]=='M2')|(data[Z]=='M2')|(data[XA]=='M2')|
        (data[XB]=='M2')|(data[XE]=='M2')),EM32, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='M3')|(data[Q]=='M3')|
        (data[R]=='M3')|(data[S]=='M3')|(data[T]=='M1')|(data[U]=='M3')|(data[V]=='M3')|
        (data[W]=='M3')|(data[X]=='M3')|(data[Y]=='M1')|(data[Z]=='M3')|(data[XA]=='M3')|
        (data[XB]=='M3')|(data[XE]=='M3')),EM33, data[XG])
data[XG]=np.where((data['Cohort']=='3')&((data[P]=='M4')|(data[Q]=='M4')|
        (data[R]=='M1')|(data[S]=='M4')|(data[T]=='M4')|(data[U]=='M4')|(data[V]=='M4')|
        (data[W]=='M1')|(data[X]=='M4')|(data[Y]=='M4')|(data[Z]=='M4')|(data[XA]=='M4')|
        (data[XB]=='M1')|(data[XE]=='M4')),EM34, data[XG])

data[XG]=np.where((data['Cohort']=='4')&((data[P]=='F1')|(data[Q]=='F1')|
        (data[R]=='F1')|(data[S]=='F1')|(data[T]=='F1')|(data[U]=='F1')|(data[V]=='F1')|
        (data[W]=='F1')|(data[X]=='F1')|(data[Y]=='F1')|(data[Z]=='F1')|(data[XA]=='F1')|
        (data[XB]=='F1')|(data[XE]=='F1')),EF41, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='F2')|(data[Q]=='F2')|
        (data[R]=='F2')|(data[S]=='F2')|(data[T]=='F2')|(data[U]=='F2')|(data[V]=='F2')|
        (data[W]=='F2')|(data[X]=='F2')|(data[Y]=='F2')|(data[Z]=='F2')|(data[XA]=='F2')|
        (data[XB]=='F2')|(data[XE]=='F2')),EF42, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='F3')|(data[Q]=='F3')|
        (data[R]=='F3')|(data[S]=='F3')|(data[T]=='F1')|(data[U]=='F3')|(data[V]=='F3')|
        (data[W]=='F3')|(data[X]=='F3')|(data[Y]=='F1')|(data[Z]=='F3')|(data[XA]=='F3')|
        (data[XB]=='F3')|(data[XE]=='F3')),EF43, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='F4')|(data[Q]=='F4')|
        (data[R]=='F1')|(data[S]=='F4')|(data[T]=='F4')|(data[U]=='F4')|(data[V]=='F4')|
        (data[W]=='F1')|(data[X]=='F4')|(data[Y]=='F4')|(data[Z]=='F4')|(data[XA]=='F4')|
        (data[XB]=='F1')|(data[XE]=='F4')),EF44, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='M1')|(data[Q]=='M1')|
        (data[R]=='M1')|(data[S]=='M1')|(data[T]=='M1')|(data[U]=='M1')|(data[V]=='M1')|
        (data[W]=='M1')|(data[X]=='M1')|(data[Y]=='M1')|(data[Z]=='M1')|(data[XA]=='M1')|
        (data[XB]=='M1')|(data[XE]=='M1')),EM41, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='M2')|(data[Q]=='M2')|
        (data[R]=='M2')|(data[S]=='M2')|(data[T]=='M2')|(data[U]=='M2')|(data[V]=='M2')|
        (data[W]=='M2')|(data[X]=='M2')|(data[Y]=='M2')|(data[Z]=='M2')|(data[XA]=='M2')|
        (data[XB]=='M2')|(data[XE]=='M2')),EM42, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='M3')|(data[Q]=='M3')|
        (data[R]=='M3')|(data[S]=='M3')|(data[T]=='M1')|(data[U]=='M3')|(data[V]=='M3')|
        (data[W]=='M3')|(data[X]=='M3')|(data[Y]=='M1')|(data[Z]=='M3')|(data[XA]=='M3')|
        (data[XB]=='M3')|(data[XE]=='M3')),EM43, data[XG])
data[XG]=np.where((data['Cohort']=='4')&((data[P]=='M4')|(data[Q]=='M4')|
        (data[R]=='M1')|(data[S]=='M4')|(data[T]=='M4')|(data[U]=='M4')|(data[V]=='M4')|
        (data[W]=='M1')|(data[X]=='M4')|(data[Y]=='M4')|(data[Z]=='M4')|(data[XA]=='M4')|
        (data[XB]=='M1')|(data[XE]=='M4')),EM44, data[XG])

data[XG]=np.where((data['Cohort']=='5')&((data[P]=='F1')|(data[Q]=='F1')|
        (data[R]=='F1')|(data[S]=='F1')|(data[T]=='F1')|(data[U]=='F1')|(data[V]=='F1')|
        (data[W]=='F1')|(data[X]=='F1')|(data[Y]=='F1')|(data[Z]=='F1')|(data[XA]=='F1')|
        (data[XB]=='F1')|(data[XE]=='F1')),EF51, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='F2')|(data[Q]=='F2')|
        (data[R]=='F2')|(data[S]=='F2')|(data[T]=='F2')|(data[U]=='F2')|(data[V]=='F2')|
        (data[W]=='F2')|(data[X]=='F2')|(data[Y]=='F2')|(data[Z]=='F2')|(data[XA]=='F2')|
        (data[XB]=='F2')|(data[XE]=='F2')),EF52, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='F3')|(data[Q]=='F3')|
        (data[R]=='F3')|(data[S]=='F3')|(data[T]=='F1')|(data[U]=='F3')|(data[V]=='F3')|
        (data[W]=='F3')|(data[X]=='F3')|(data[Y]=='F1')|(data[Z]=='F3')|(data[XA]=='F3')|
        (data[XB]=='F3')|(data[XE]=='F3')),EF53, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='F4')|(data[Q]=='F4')|
        (data[R]=='F1')|(data[S]=='F4')|(data[T]=='F4')|(data[U]=='F4')|(data[V]=='F4')|
        (data[W]=='F1')|(data[X]=='F4')|(data[Y]=='F4')|(data[Z]=='F4')|(data[XA]=='F4')|
        (data[XB]=='F1')|(data[XE]=='F4')),EF54, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='M1')|(data[Q]=='M1')|
        (data[R]=='M1')|(data[S]=='M1')|(data[T]=='M1')|(data[U]=='M1')|(data[V]=='M1')|
        (data[W]=='M1')|(data[X]=='M1')|(data[Y]=='M1')|(data[Z]=='M1')|(data[XA]=='M1')|
        (data[XB]=='M1')|(data[XE]=='M1')),EM51, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='M2')|(data[Q]=='M2')|
        (data[R]=='M2')|(data[S]=='M2')|(data[T]=='M2')|(data[U]=='M2')|(data[V]=='M2')|
        (data[W]=='M2')|(data[X]=='M2')|(data[Y]=='M2')|(data[Z]=='M2')|(data[XA]=='M2')|
        (data[XB]=='M2')|(data[XE]=='M2')),EM52, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='M3')|(data[Q]=='M3')|
        (data[R]=='M3')|(data[S]=='M3')|(data[T]=='M1')|(data[U]=='M3')|(data[V]=='M3')|
        (data[W]=='M3')|(data[X]=='M3')|(data[Y]=='M1')|(data[Z]=='M3')|(data[XA]=='M3')|
        (data[XB]=='M3')|(data[XE]=='M3')),EM53, data[XG])
data[XG]=np.where((data['Cohort']=='5')&((data[P]=='M4')|(data[Q]=='M4')|
        (data[R]=='M1')|(data[S]=='M4')|(data[T]=='M4')|(data[U]=='M4')|(data[V]=='M4')|
        (data[W]=='M1')|(data[X]=='M4')|(data[Y]=='M4')|(data[Z]=='M4')|(data[XA]=='M4')|
        (data[XB]=='M1')|(data[XE]=='M4')),EM54, data[XG])

# Make a column with the treatments per rat
data[XH]=np.where(((data[XF]=='FC1')|(data[XF]=='FC2')|(data[XF]=='FC3')|(data[XF]=='FC4')|
        (data[XF]=='FC5')|(data[XF]=='FC6')|(data[XF]=='FC7')|(data[XF]=='FC8')|(data[XF]=='FC9')|
        (data[XF]=='FC10')),SA, "")
data[XH]=np.where(((data[XF]=='FF1')|(data[XF]=='FF2')|(data[XF]=='FF3')|(data[XF]=='FF4')|
        (data[XF]=='FF5')|(data[XF]=='FF6')|(data[XF]=='FF7')|(data[XF]=='FF8')|(data[XF]=='FF9')|
        (data[XF]=='FF10')),SB, data[XH])
data[XH]=np.where(((data[XF]=='MC1')|(data[XF]=='MC2')|(data[XF]=='MC3')|(data[XF]=='MC4')|
        (data[XF]=='MC5')|(data[XF]=='MC6')|(data[XF]=='MC7')|(data[XF]=='MC8')|(data[XF]=='MC9')|
        (data[XF]=='MC10')),SC, data[XH])
data[XH]=np.where(((data[XF]=='MF1')|(data[XF]=='MF2')|(data[XF]=='MF3')|(data[XF]=='MF4')|
        (data[XF]=='MF5')|(data[XF]=='MF6')|(data[XF]=='MF7')|(data[XF]=='MF8')|(data[XF]=='MF9')|
        (data[XF]=='MF10')),SD, data[XH])

# Make a column with the treatments per modifier
data[XI]=np.where(((data[XG]=='FC1')|(data[XG]=='FC2')|(data[XG]=='FC3')|(data[XG]=='FC4')|
        (data[XG]=='FC5')|(data[XG]=='FC6')|(data[XG]=='FC7')|(data[XG]=='FC8')|(data[XG]=='FC9')|
        (data[XG]=='FC10')),SA, "")
data[XI]=np.where(((data[XG]=='FF1')|(data[XG]=='FF2')|(data[XG]=='FF3')|(data[XG]=='FF4')|
        (data[XG]=='FF5')|(data[XG]=='FF6')|(data[XG]=='FF7')|(data[XG]=='FF8')|(data[XG]=='FF9')|
        (data[XG]=='FF10')),SB, data[XI])
data[XI]=np.where(((data[XG]=='MC1')|(data[XG]=='MC2')|(data[XG]=='MC3')|(data[XG]=='MC4')|
        (data[XG]=='MC5')|(data[XG]=='MC6')|(data[XG]=='MC7')|(data[XG]=='MC8')|(data[XG]=='MC9')|
        (data[XG]=='MC10')),SC, data[XI])
data[XI]=np.where(((data[XG]=='MF1')|(data[XG]=='MF2')|(data[XG]=='MF3')|(data[XG]=='MF4')|
        (data[XG]=='MF5')|(data[XG]=='MF6')|(data[XG]=='MF7')|(data[XG]=='MF8')|(data[XG]=='MF9')|
        (data[XG]=='MF10')),SD, data[XI])

# Make a column with sex per modifier
data[XJ]=np.where((data[XI]==SA)|(data[XI]==SB),'female','male')
data[XJ]=np.where(data[XG]=="","",data[XJ])

# Make a column with treatmentgroup per modifier
data[XK]=np.where((data[XI]==SA)|(data[XI]==SC),'CTR','FLX')
data[XK]=np.where(data[XG]=="","",data[XK])

# Make a column with modifier location
data[XL]=np.where((data[XA]=='OA'),'Open field',"")
data[XL]=np.where(((data[XA]=='Tunnels')|(data[XA]=='Nest Box Right')|(data[XA]=='Nest Box Left')|
        (data[XA]=='Nest Box Mid Right')|(data[XA]=='Nest Box Mid Left')),'Burrow',data[XL])

# Make a column with modifier winner loser or other
data[XM]=np.where((data[X]=='winner'),'Winner',"")
data[XM]=np.where((data[Y]=='loser'),'Loser',data[XM])
data[XM]=np.where((data[Z]=='other (not winner/loser)'),'Other',data[XM])

# Make column with RatID winner, loser, witness or not
data['Rat_role']=np.where((data[O]=='won a fight'),1,np.NaN)
data['Rat_role']=np.where((data[O]=='lost a fight'),2,data['Rat_role'])
data['Rat_role']=np.where((data[O]=='Is Close during fight'),3,data['Rat_role'])
data['Rat_role']=np.where((data[O]=='in Not Close during fight'),4,data['Rat_role'])

data= data.sort_values(by=['RatID','Fight','Time'])
data['Rat_role'].fillna(method = "ffill", inplace=True)
data[XN]=np.where((data['Rat_role']==1),'Winner',"")
data[XN]=np.where((data['Rat_role']==2),'Loser',data[XN])
data[XN]=np.where((data['Rat_role']==3),'Witness',data[XN])
data[XN]=np.where((data['Rat_role']==4),'NotWitness',data[XN])

data[XO]=np.where((data[XN]=='NotWitness'),'NotWitness','Witness')

# Determine the end of fight and delete the behaviors before this
data= data.sort_values(by=['Fight','Time'])

# Mark beginning/end per fight
data['obsnum'] = data.groupby('Fight')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['endfight']=np.where((data[O]=='won a fight'),data['Time'],np.NaN)
data['endfight']= np.where((data['obsnum']==1), 99999,data['endfight'])
data['endfight'].fillna(method = "ffill", inplace=True)
data['endfight']=np.where(data['endfight']==99999, np.NaN, data['endfight'])
data['endfight'].fillna(method = "backfill", inplace=True)

# Delete columns with time smaller than the end of fight
data['duringfight']=np.where((data['Time'])<(data['endfight']),'delete',"")
        
data= data.sort_values(by=['RatID','Fight','Time'])
# Delete the rows that "end" a behavior
# Drop a row by condition
data=data[data.Event_type != 'State stop']
data=data[data.duringfight != 'delete']
# Delete the rows that do not contain a behavior or ratID
data=data[data.Subject_raw != ""]
data=data[data.RatID != ""]
data=data[data.Subject_raw != 'MrX']
data=data[data.Behavior != ""]
data=data[data.Behavior != "Irrelevant"]

# Calculate the durations of each behavior
data['time_diff'] = data['Time'].diff()
data.loc[data.RatID != data.RatID.shift(), 'time_diff'] = None

# Now put the time differences to the right behavior in column 'durations'
data['durations'] = data.time_diff.shift(-1)
data= data.dropna(axis=0, subset=['durations'])

# Create unique code per Fight per rat-> all the following calculations will be unique per Fight
data['ratID_Fight'] = data[XF].map(str) + data['Fight']

# Create unique code per Rat-role per fight
data['ratID_Fight_role'] = data[XN].map(str) + data['ratID_Fight']

# Create unique code per Rat-role per fight with winner loser as witness
data['ratID_Fight_roleplus'] = data[XO].map(str) + data['ratID_Fight']

# Create unique code per behavior per rat
data['ratID_beh'] = data[O].map(str) + data['ratID_Fight']
data['ratID_beh_role'] = data[O].map(str) + data['ratID_Fight_role']
data['ratID_beh_roleplus'] = data[O].map(str) + data['ratID_Fight_roleplus']

# Create unique code per behavior per rat per location
data['ratID_beh_loc'] = data[Q].map(str) + data['ratID_beh']
data['ratID_beh_loc_role'] = data[Q].map(str) + data['ratID_beh_role']
data['ratID_beh_loc_roleplus'] = data[Q].map(str) + data['ratID_beh_roleplus']

# Create unique code per behavior per rat per sex
data['ratID_beh_sex'] = data['ratID_beh'].map(str) + data[XJ]
data['ratID_beh_sex_role'] = data['ratID_beh_role'].map(str) + data[XJ]
data['ratID_beh_sex_roleplus'] = data['ratID_beh_roleplus'].map(str) + data[XJ]

# Create unique code per behavior per rat per treatment group
data['ratID_beh_treat'] = data['ratID_beh'].map(str) + data[XI]
data['ratID_beh_treat_role'] = data['ratID_beh_role'].map(str) + data[XI]
data['ratID_beh_treat_roleplus'] = data['ratID_beh_roleplus'].map(str) + data[XI]

# Create unique code per behavior per rat per treatment group
data['ratID_beh_loc_treat'] = data['ratID_beh_loc'].map(str) + data[XI]
data['ratID_beh_loc_treat_role'] = data['ratID_beh_loc_role'].map(str) + data[XI]
data['ratID_beh_loc_treat_roleplus'] = data['ratID_beh_loc_roleplus'].map(str) + data[XI]

# Create unique code per behavior per rat per ModID
data['ratID_beh_modsub'] = data[XG].map(str)+data['ratID_beh'] 
data['ratID_beh_modsub_role'] = data[XG].map(str)+data['ratID_beh_role'] 
data['ratID_beh_modsub_roleplus'] = data[XG].map(str)+data['ratID_beh_roleplus'] 

# Create unique code per behavior per rat per ModID_winner
data['ratID_beh_modwinner'] = data[XM].map(str)+data['ratID_beh'] 
data['ratID_beh_loc_modwinner'] = data[XM].map(str)+data['ratID_beh_loc'] 
data['ratID_beh_modwinner_role'] = data[XM].map(str)+data['ratID_beh_role'] 
data['ratID_beh_loc_modwinner_role'] = data[XM].map(str)+data['ratID_beh_loc_role'] 
data['ratID_beh_modwinner_roleplus'] = data[XM].map(str)+data['ratID_beh_roleplus']
data['ratID_beh_loc_modwinner_roleplus'] = data[XM].map(str)+data['ratID_beh_loc_roleplus']

# Mark beginning per rat
data['obs_num'] = data.groupby('ratID_Fight')[O].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data['obs_beh_num'] = data.groupby('ratID_beh')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_role_num'] = data.groupby('ratID_beh_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_roleplus_num'] = data.groupby('ratID_beh_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_num'] = data.groupby('ratID_beh_loc')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_num'] = data.groupby('ratID_beh_sex')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_num'] = data.groupby('ratID_beh_treat')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_num'] = data.groupby('ratID_beh_loc_treat')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_num'] = data.groupby('ratID_beh_loc_modwinner')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_num'] = data.groupby('ratID_beh_modsub')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_num'] = data.groupby('ratID_beh_modwinner')[O].transform(lambda x: np.arange(1, len(x) + 1))

data['obs_beh_loc_role_num'] = data.groupby('ratID_beh_loc_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_role_num'] = data.groupby('ratID_beh_sex_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_role_num'] = data.groupby('ratID_beh_treat_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_role_num'] = data.groupby('ratID_beh_loc_treat_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_role_num'] = data.groupby('ratID_beh_loc_modwinner_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_role_num'] = data.groupby('ratID_beh_modsub_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_role_num'] = data.groupby('ratID_beh_modwinner_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_roleplus_num'] = data.groupby('ratID_beh_loc_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_roleplus_num'] = data.groupby('ratID_beh_sex_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_roleplus_num'] = data.groupby('ratID_beh_treat_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_roleplus_num'] = data.groupby('ratID_beh_loc_treat_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_roleplus_num'] = data.groupby('ratID_beh_loc_modwinner_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_roleplus_num'] = data.groupby('ratID_beh_modsub_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_roleplus_num'] = data.groupby('ratID_beh_modwinner_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))


# Number the behaviors backwards and end per rat
data = data.sort_values(by=['ratID_beh','Time'], ascending = False)
data['obs_beh_num_back'] = data.groupby('ratID_beh')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_num_back'] = data.groupby('ratID_beh_loc')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_num_back'] = data.groupby('ratID_beh_sex')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_num_back'] = data.groupby('ratID_beh_treat')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_num_back'] = data.groupby('ratID_beh_loc_treat')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_num_back'] = data.groupby('ratID_beh_loc_modwinner')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_num_back'] = data.groupby('ratID_beh_modsub')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_num_back'] = data.groupby('ratID_beh_modwinner')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_role_num_back'] = data.groupby('ratID_beh_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_role_num_back'] = data.groupby('ratID_beh_loc_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_role_num_back'] = data.groupby('ratID_beh_sex_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_role_num_back'] = data.groupby('ratID_beh_treat_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_role_num_back'] = data.groupby('ratID_beh_loc_treat_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_role_num_back'] = data.groupby('ratID_beh_loc_modwinner_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_role_num_back'] = data.groupby('ratID_beh_modsub_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_role_num_back'] = data.groupby('ratID_beh_modwinner_role')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_roleplus_num_back'] = data.groupby('ratID_beh_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_roleplus_num_back'] = data.groupby('ratID_beh_loc_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_sex_roleplus_num_back'] = data.groupby('ratID_beh_sex_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_treat_roleplus_num_back'] = data.groupby('ratID_beh_treat_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_treat_roleplus_num_back'] = data.groupby('ratID_beh_loc_treat_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_loc_modwinner_roleplus_num_back'] = data.groupby('ratID_beh_loc_modwinner_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modsub_roleplus_num_back'] = data.groupby('ratID_beh_modsub_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))
data['obs_beh_modwinner_roleplus_num_back'] = data.groupby('ratID_beh_modwinner_roleplus')[O].transform(lambda x: np.arange(1, len(x) + 1))

data = data.sort_values(by=['ratID_Fight','Time'], ascending = False)
data['obs_num_back'] = data.groupby('ratID_Fight')[O].transform(lambda x: np.arange(1, len(x) + 1))
data = data.sort_values(by=['ratID_Fight','Time'])

# Sum up the durations on occurance
data['obs_beh_sumdur']=data.groupby('ratID_beh')['durations'].cumsum()
data['obs_beh_loc_sumdur']=data.groupby('ratID_beh_loc')['durations'].cumsum()
data['obs_beh_treat_sumdur']=data.groupby('ratID_beh_treat')['durations'].cumsum()
data['obs_beh_loc_treat_sumdur']=data.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data['obs_beh_loc_modwinner_sumdur']=data.groupby('ratID_beh_loc_modwinner')['durations'].cumsum()
data['obs_beh_modsub_sumdur']=data.groupby('ratID_beh_modsub')['durations'].cumsum()
data['obs_beh_modwinner_sumdur']=data.groupby('ratID_beh_modwinner')['durations'].cumsum()

data['obs_beh_role_sumdur']=data.groupby('ratID_beh_role')['durations'].cumsum()
data['obs_beh_loc_role_sumdur']=data.groupby('ratID_beh_loc_role')['durations'].cumsum()
data['obs_beh_treat_role_sumdur']=data.groupby('ratID_beh_treat_role')['durations'].cumsum()
data['obs_beh_loc_treat_role_sumdur']=data.groupby('ratID_beh_loc_treat_role')['durations'].cumsum()
data['obs_beh_loc_modwinner_role_sumdur']=data.groupby('ratID_beh_loc_modwinner_role')['durations'].cumsum()
data['obs_beh_modsub_role_sumdur']=data.groupby('ratID_beh_modsub_role')['durations'].cumsum()
data['obs_beh_modwinner_role_sumdur']=data.groupby('ratID_beh_modwinner_role')['durations'].cumsum()

data['obs_beh_roleplus_sumdur']=data.groupby('ratID_beh_roleplus')['durations'].cumsum()
data['obs_beh_loc_roleplus_sumdur']=data.groupby('ratID_beh_loc_roleplus')['durations'].cumsum()
data['obs_beh_treat_roleplus_sumdur']=data.groupby('ratID_beh_treat_roleplus')['durations'].cumsum()
data['obs_beh_loc_treat_roleplus_sumdur']=data.groupby('ratID_beh_loc_treat_roleplus')['durations'].cumsum()
data['obs_beh_loc_modwinner_roleplus_sumdur']=data.groupby('ratID_beh_loc_modwinner_roleplus')['durations'].cumsum()
data['obs_beh_modsub_roleplus_sumdur']=data.groupby('ratID_beh_modsub_roleplus')['durations'].cumsum()
data['obs_beh_modwinner_roleplus_sumdur']=data.groupby('ratID_beh_modwinner_roleplus')['durations'].cumsum()
 
# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TN_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_num'], np.NaN)
        data['TN_%s'% col_name]= np.where(data['TN_%s'% col_name]==1,data['obs_beh_num_back'], np.NaN)
        data['TN_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TN_%s'% col_name])
        data['TN_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TN_%s'% col_name])
        data['TN_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TN_%s'% col_name]=np.where(data['TN_%s'% col_name]==99999, np.NaN, data['TN_%s'% col_name])
        data['TN_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TN_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TN_%s'% col_name]==88888),
            0,data['TN_%s'% col_name])
        data['TN_%s'% col_name]=np.where(data['TN_%s'% col_name]==88888, np.NaN, data['TN_%s'% col_name])
        data['TN_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BN_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_num'], np.NaN)
        data['BN_%s'% col_name]= np.where(data['BN_%s'% col_name]==1,data['obs_beh_loc_num_back'], np.NaN)
        data['BN_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BN_%s'% col_name])
        data['BN_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BN_%s'% col_name])
        data['BN_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BN_%s'% col_name])
        data['BN_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BN_%s'% col_name])
        data['BN_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BN_%s'% col_name]=np.where(data['BN_%s'% col_name]==99999, np.NaN, data['BN_%s'% col_name])
        data['BN_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BN_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BN_%s'% col_name]==88888), 
            0,data['BN_%s'% col_name])
        data['BN_%s'% col_name]=np.where(data['BN_%s'% col_name]==88888, np.NaN, data['BN_%s'% col_name])
        data['BN_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['ON_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_num'], np.NaN)
        data['ON_%s'% col_name]= np.where(data['ON_%s'% col_name]==1,data['obs_beh_loc_num_back'], np.NaN)
        data['ON_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['ON_%s'% col_name])
        data['ON_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['ON_%s'% col_name])
        data['ON_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['ON_%s'% col_name])
        data['ON_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['ON_%s'% col_name])
        data['ON_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ON_%s'% col_name]=np.where(data['ON_%s'% col_name]==99999, np.NaN, data['ON_%s'% col_name])
        data['ON_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ON_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ON_%s'% col_name]==88888), 
            0,data['ON_%s'% col_name])
        data['ON_%s'% col_name]=np.where(data['ON_%s'% col_name]==88888, np.NaN, data['ON_%s'% col_name])
        data['ON_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additional behaviors for total environment, burrow, and open field    
data['TN_%s'% EA]=(data['TN_%s'% BG]+data['TN_%s'% BD]+data['TN_%s'% BC])
data['TN_%s'% EB]=(data['TN_%s'% BI]+data['TN_%s'% BBJ])
data['TN_%s'% EC]=(data['TN_%s'% BG]+data['TN_%s'% BD]+data['TN_%s'% BC]+data['TN_%s'% BF]+data['TN_%s'% BI]+data['TN_%s'% BBJ])
data['TN_%s'% ED]=(data['TN_%s'% BB]+data['TN_%s'% BH]+data['TN_%s'% BL])
data['TN_%s'% EE]=(data['TN_%s'% BA]+data['TN_%s'% BI]+data['TN_%s'% BBI]+data['TN_%s'% BBJ])
data['TN_%s'% EF]=(data['TN_%s'% BM]+data['TN_%s'% BN]+data['TN_%s'% BO]+data['TN_%s'% BP]+data['TN_%s'% BQ]+data['TN_%s'% BU]+data['TN_%s'% BS]+data['TN_%s'% BR])
data['TN_%s'% EG]=(data['TN_%s'% BE]+data['TN_%s'% BF])

data['BN_%s'% EA]=(data['BN_%s'% BG]+data['BN_%s'% BD]+data['BN_%s'% BC])
data['BN_%s'% EB]=(data['BN_%s'% BI]+data['BN_%s'% BBJ])
data['BN_%s'% EC]=(data['BN_%s'% BG]+data['BN_%s'% BD]+data['BN_%s'% BC]+data['BN_%s'% BF]+data['BN_%s'% BI]+data['BN_%s'% BBJ])
data['BN_%s'% ED]=(data['BN_%s'% BB]+data['BN_%s'% BH]+data['BN_%s'% BL])
data['BN_%s'% EE]=(data['BN_%s'% BA]+data['BN_%s'% BI]+data['BN_%s'% BBI]+data['BN_%s'% BBJ])
data['BN_%s'% EF]=(data['BN_%s'% BM]+data['BN_%s'% BN]+data['BN_%s'% BO]+data['BN_%s'% BP]+data['BN_%s'% BQ]+data['BN_%s'% BU]+data['BN_%s'% BS]+data['BN_%s'% BR])
data['BN_%s'% EG]=(data['BN_%s'% BE]+data['BN_%s'% BF])

data['ON_%s'% EA]=(data['ON_%s'% BG]+data['ON_%s'% BD]+data['ON_%s'% BC])
data['ON_%s'% EB]=(data['ON_%s'% BI]+data['ON_%s'% BBJ])
data['ON_%s'% EC]=(data['ON_%s'% BG]+data['ON_%s'% BD]+data['ON_%s'% BC]+data['ON_%s'% BF]+data['ON_%s'% BI]+data['ON_%s'% BBJ])
data['ON_%s'% ED]=(data['ON_%s'% BB]+data['ON_%s'% BH]+data['ON_%s'% BL])
data['ON_%s'% EE]=(data['ON_%s'% BA]+data['ON_%s'% BI]+data['ON_%s'% BBI]+data['ON_%s'% BBJ])
data['ON_%s'% EF]=(data['ON_%s'% BM]+data['ON_%s'% BN]+data['ON_%s'% BO]+data['ON_%s'% BP]+data['ON_%s'% BQ]+data['ON_%s'% BU]+data['ON_%s'% BS]+data['ON_%s'% BR])
data['ON_%s'% EG]=(data['ON_%s'% BE]+data['ON_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_num'], np.NaN)
    data['TNFF_%s'% col_name]= np.where(data['TNFF_%s'% col_name]==1,data['obs_beh_treat_num_back'], np.NaN)
    data['TNFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFF_%s'% col_name]=np.where(data['TNFF_%s'% col_name]==99999, np.NaN, data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFF_%s'% col_name]==88888), 
        0,data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name]=np.where(data['TNFF_%s'% col_name]==88888, np.NaN, data['TNFF_%s'% col_name])
    data['TNFF_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total environment
    data['TNCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_num'], np.NaN)
    data['TNCF_%s'% col_name]= np.where(data['TNCF_%s'% col_name]==1,data['obs_beh_treat_num_back'], np.NaN)
    data['TNCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCF_%s'% col_name]=np.where(data['TNCF_%s'% col_name]==99999, np.NaN, data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCF_%s'% col_name]==88888), 
        0,data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name]=np.where(data['TNCF_%s'% col_name]==88888, np.NaN, data['TNCF_%s'% col_name])
    data['TNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total environment
    data['TNFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_num'], np.NaN)
    data['TNFM_%s'% col_name]= np.where(data['TNFM_%s'% col_name]==1,data['obs_beh_treat_num_back'], np.NaN)
    data['TNFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFM_%s'% col_name]=np.where(data['TNFM_%s'% col_name]==99999, np.NaN, data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFM_%s'% col_name]==88888), 
        0,data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name]=np.where(data['TNFM_%s'% col_name]==88888, np.NaN, data['TNFM_%s'% col_name])
    data['TNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total environment
    data['TNCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_num'], np.NaN)
    data['TNCM_%s'% col_name]= np.where(data['TNCM_%s'% col_name]==1,data['obs_beh_treat_num_back'], np.NaN)
    data['TNCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCM_%s'% col_name]=np.where(data['TNCM_%s'% col_name]==99999, np.NaN, data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCM_%s'% col_name]==88888), 
        0,data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name]=np.where(data['TNCM_%s'% col_name]==88888, np.NaN, data['TNCM_%s'% col_name])
    data['TNCM_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TNW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_num'], np.NaN)
    data['TNW_%s'% col_name]= np.where(data['TNW_%s'% col_name]==1,data['obs_beh_modwinner_num_back'], np.NaN)
    data['TNW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNW_%s'% col_name])
    data['TNW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TNW_%s'% col_name])
    data['TNW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNW_%s'% col_name])
    data['TNW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TNW_%s'% col_name])
    data['TNW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNW_%s'% col_name]=np.where(data['TNW_%s'% col_name]==99999, np.NaN, data['TNW_%s'% col_name])
    data['TNW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNW_%s'% col_name]==88888), 
        0,data['TNW_%s'% col_name])
    data['TNW_%s'% col_name]=np.where(data['TNW_%s'% col_name]==88888, np.NaN, data['TNW_%s'% col_name])
    data['TNW_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TNL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_num'], np.NaN)
    data['TNL_%s'% col_name]= np.where(data['TNL_%s'% col_name]==1,data['obs_beh_modwinner_num_back'], np.NaN)
    data['TNL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNL_%s'% col_name])
    data['TNL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TNL_%s'% col_name])
    data['TNL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNL_%s'% col_name])
    data['TNL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TNL_%s'% col_name])
    data['TNL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNL_%s'% col_name]=np.where(data['TNL_%s'% col_name]==99999, np.NaN, data['TNL_%s'% col_name])
    data['TNL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNL_%s'% col_name]==88888), 
        0,data['TNL_%s'% col_name])
    data['TNL_%s'% col_name]=np.where(data['TNL_%s'% col_name]==88888, np.NaN, data['TNL_%s'% col_name])
    data['TNL_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TNO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Others')),data['obs_beh_modwinner_num'], np.NaN)
    data['TNO_%s'% col_name]= np.where(data['TNO_%s'% col_name]==1,data['obs_beh_modwinner_num_back'], np.NaN)
    data['TNO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNO_%s'% col_name])
    data['TNO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TNO_%s'% col_name])
    data['TNO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNO_%s'% col_name])
    data['TNO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TNO_%s'% col_name])
    data['TNO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNO_%s'% col_name]=np.where(data['TNO_%s'% col_name]==99999, np.NaN, data['TNO_%s'% col_name])
    data['TNO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNO_%s'% col_name]==88888), 
        0,data['TNO_%s'% col_name])
    data['TNO_%s'% col_name]=np.where(data['TNO_%s'% col_name]==88888, np.NaN, data['TNO_%s'% col_name])
    data['TNO_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BNFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BNFF_%s'% col_name]= np.where(data['BNFF_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['BNFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_%s'% col_name]=np.where(data['BNFF_%s'% col_name]==99999, np.NaN, data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFF_%s'% col_name]==88888), 
        0,data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name]=np.where(data['BNFF_%s'% col_name]==88888, np.NaN, data['BNFF_%s'% col_name])
    data['BNFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_%s'% col_name]=np.where(data['BNFF_%s'% col_name]==np.NaN,0, data['BNFF_%s'% col_name])

    data['BNCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BNCF_%s'% col_name]= np.where(data['BNCF_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['BNCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_%s'% col_name]=np.where(data['BNCF_%s'% col_name]==99999, np.NaN, data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCF_%s'% col_name]==88888), 
        0,data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name]=np.where(data['BNCF_%s'% col_name]==88888, np.NaN, data['BNCF_%s'% col_name])
    data['BNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_%s'% col_name]=np.where(data['BNCF_%s'% col_name]== np.NaN,0, data['BNCF_%s'% col_name])

    data['BNFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BNFM_%s'% col_name]= np.where(data['BNFM_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['BNFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_%s'% col_name]=np.where(data['BNFM_%s'% col_name]==99999, np.NaN, data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFM_%s'% col_name]==88888), 
        0,data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name]=np.where(data['BNFM_%s'% col_name]==88888, np.NaN, data['BNFM_%s'% col_name])
    data['BNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_%s'% col_name]=np.where(data['BNFM_%s'% col_name]==np.NaN,0, data['BNFM_%s'% col_name])
 
    data['BNCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BNCM_%s'% col_name]= np.where(data['BNCM_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['BNCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_%s'% col_name]=np.where(data['BNCM_%s'% col_name]==99999, np.NaN, data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCM_%s'% col_name]==88888), 
        0,data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name]=np.where(data['BNCM_%s'% col_name]==88888, np.NaN, data['BNCM_%s'% col_name])
    data['BNCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_%s'% col_name]=np.where(data['BNCM_%s'% col_name]== np.NaN,0, data['BNCM_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ONFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ONFF_%s'% col_name]= np.where(data['ONFF_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['ONFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_%s'% col_name]=np.where(data['ONFF_%s'% col_name]==99999, np.NaN, data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFF_%s'% col_name]==88888), 
        0,data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name]=np.where(data['ONFF_%s'% col_name]==88888, np.NaN, data['ONFF_%s'% col_name])
    data['ONFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_%s'% col_name]=np.where(data['ONFF_%s'% col_name]== np.NaN,0, data['ONFF_%s'% col_name])

    data['ONCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ONCF_%s'% col_name]= np.where(data['ONCF_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['ONCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_%s'% col_name]=np.where(data['ONCF_%s'% col_name]==99999, np.NaN, data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCF_%s'% col_name]==88888), 
        0,data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name]=np.where(data['ONCF_%s'% col_name]==88888, np.NaN, data['ONCF_%s'% col_name])
    data['ONCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_%s'% col_name]=np.where(data['ONCF_%s'% col_name]== np.NaN,0, data['ONCF_%s'% col_name])
    
    data['ONFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ONFM_%s'% col_name]= np.where(data['ONFM_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['ONFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_%s'% col_name]=np.where(data['ONFM_%s'% col_name]==99999, np.NaN, data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFM_%s'% col_name]==88888), 
        0,data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name]=np.where(data['ONFM_%s'% col_name]==88888, np.NaN, data['ONFM_%s'% col_name])
    data['ONFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_%s'% col_name]=np.where(data['ONFM_%s'% col_name]== np.NaN,0, data['ONFM_%s'% col_name])

    data['ONCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ONCM_%s'% col_name]= np.where(data['ONCM_%s'% col_name]==1,data['obs_beh_loc_treat_num_back'], np.NaN)
    data['ONCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_%s'% col_name]=np.where(data['ONCM_%s'% col_name]==99999, np.NaN, data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCM_%s'% col_name]==88888), 
        0,data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name]=np.where(data['ONCM_%s'% col_name]==88888, np.NaN, data['ONCM_%s'% col_name])
    data['ONCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_%s'% col_name]=np.where(data['ONCM_%s'% col_name]== np.NaN,0, data['ONCM_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BNW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BNW_%s'% col_name]= np.where(data['BNW_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['BNW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_%s'% col_name]=np.where(data['BNW_%s'% col_name]==99999, np.NaN, data['BNW_%s'% col_name])
    data['BNW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNW_%s'% col_name]==88888), 
        0,data['BNW_%s'% col_name])
    data['BNW_%s'% col_name]=np.where(data['BNW_%s'% col_name]==88888, np.NaN, data['BNW_%s'% col_name])
    data['BNW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_%s'% col_name]=np.where(data['BNW_%s'% col_name]== np.NaN,0, data['BNW_%s'% col_name])

    data['BNL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BNL_%s'% col_name]= np.where(data['BNL_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['BNL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_%s'% col_name]=np.where(data['BNL_%s'% col_name]==99999, np.NaN, data['BNL_%s'% col_name])
    data['BNL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNL_%s'% col_name]==88888), 
        0,data['BNL_%s'% col_name])
    data['BNL_%s'% col_name]=np.where(data['BNL_%s'% col_name]==88888, np.NaN, data['BNL_%s'% col_name])
    data['BNL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_%s'% col_name]=np.where(data['BNL_%s'% col_name]== np.NaN,0, data['BNL_%s'% col_name])

    data['BNO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BNO_%s'% col_name]= np.where(data['BNO_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['BNO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_%s'% col_name]=np.where(data['BNO_%s'% col_name]==99999, np.NaN, data['BNO_%s'% col_name])
    data['BNO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNO_%s'% col_name]==88888), 
        0,data['BNO_%s'% col_name])
    data['BNO_%s'% col_name]=np.where(data['BNO_%s'% col_name]==88888, np.NaN, data['BNO_%s'% col_name])
    data['BNO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_%s'% col_name]=np.where(data['BNO_%s'% col_name]== np.NaN,0, data['BNO_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ONW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ONW_%s'% col_name]= np.where(data['ONW_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['ONW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_%s'% col_name]=np.where(data['ONW_%s'% col_name]==99999, np.NaN, data['ONW_%s'% col_name])
    data['ONW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONW_%s'% col_name]==88888), 
        0,data['ONW_%s'% col_name])
    data['ONW_%s'% col_name]=np.where(data['ONW_%s'% col_name]==88888, np.NaN, data['ONW_%s'% col_name])
    data['ONW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_%s'% col_name]=np.where(data['ONW_%s'% col_name]== np.NaN,0, data['ONW_%s'% col_name])

    data['ONL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ONL_%s'% col_name]= np.where(data['ONL_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['ONL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_%s'% col_name]=np.where(data['ONL_%s'% col_name]==99999, np.NaN, data['ONL_%s'% col_name])
    data['ONL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONL_%s'% col_name]==88888), 
        0,data['ONL_%s'% col_name])
    data['ONL_%s'% col_name]=np.where(data['ONL_%s'% col_name]==88888, np.NaN, data['ONL_%s'% col_name])
    data['ONL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_%s'% col_name]=np.where(data['ONL_%s'% col_name]== np.NaN,0, data['ONL_%s'% col_name])

    data['ONO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ONO_%s'% col_name]= np.where(data['ONO_%s'% col_name]==1,data['obs_beh_loc_modwinner_num_back'], np.NaN)
    data['ONO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_%s'% col_name]=np.where(data['ONO_%s'% col_name]==99999, np.NaN, data['ONO_%s'% col_name])
    data['ONO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONO_%s'% col_name]==88888), 
        0,data['ONO_%s'% col_name])
    data['ONO_%s'% col_name]=np.where(data['ONO_%s'% col_name]==88888, np.NaN, data['ONO_%s'% col_name])
    data['ONO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_%s'% col_name]=np.where(data['ONO_%s'% col_name]== np.NaN,0, data['ONO_%s'% col_name])


# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TNFF_%s'% EA]=(data['TNFF_%s'% BG]+data['TNFF_%s'% BD]+data['TNFF_%s'% BC])
data['TNFF_%s'% EB]=(data['TNFF_%s'% BI]+data['TNFF_%s'% BBJ])
data['TNFF_%s'% EC]=(data['TNFF_%s'% BG]+data['TNFF_%s'% BD]+data['TNFF_%s'% BC]+data['TNFF_%s'% BF]+data['TNFF_%s'% BI]+data['TNFF_%s'% BBJ])
data['TNFF_%s'% EF]=(data['TNFF_%s'% BM]+data['TNFF_%s'% BN]+data['TNFF_%s'% BO]+data['TNFF_%s'% BP]+data['TNFF_%s'% BQ]+data['TNFF_%s'% BU]+data['TNFF_%s'% BS]+data['TNFF_%s'% BR])

data['BNFF_%s'% EA]=(data['BNFF_%s'% BG]+data['BNFF_%s'% BD]+data['BNFF_%s'% BC])
data['BNFF_%s'% EB]=(data['BNFF_%s'% BI]+data['BNFF_%s'% BBJ])
data['BNFF_%s'% EC]=(data['BNFF_%s'% BG]+data['BNFF_%s'% BD]+data['BNFF_%s'% BC]+data['BNFF_%s'% BF]+data['BNFF_%s'% BI]+data['BNFF_%s'% BBJ])
data['BNFF_%s'% EF]=(data['BNFF_%s'% BM]+data['BNFF_%s'% BN]+data['BNFF_%s'% BO]+data['BNFF_%s'% BP]+data['BNFF_%s'% BQ]+data['BNFF_%s'% BU]+data['BNFF_%s'% BS]+data['BNFF_%s'% BR])

data['ONFF_%s'% EA]=(data['ONFF_%s'% BG]+data['ONFF_%s'% BD]+data['ONFF_%s'% BC])
data['ONFF_%s'% EB]=(data['ONFF_%s'% BI]+data['ONFF_%s'% BBJ])
data['ONFF_%s'% EC]=(data['ONFF_%s'% BG]+data['ONFF_%s'% BD]+data['ONFF_%s'% BC]+data['ONFF_%s'% BF]+data['ONFF_%s'% BI]+data['ONFF_%s'% BBJ])
data['ONFF_%s'% EF]=(data['ONFF_%s'% BM]+data['ONFF_%s'% BN]+data['ONFF_%s'% BO]+data['ONFF_%s'% BP]+data['ONFF_%s'% BQ]+data['ONFF_%s'% BU]+data['ONFF_%s'% BS]+data['ONFF_%s'% BR])

data['TNCF_%s'% EA]=(data['TNCF_%s'% BG]+data['TNCF_%s'% BD]+data['TNCF_%s'% BC])
data['TNCF_%s'% EB]=(data['TNCF_%s'% BI]+data['TNCF_%s'% BBJ])
data['TNCF_%s'% EC]=(data['TNCF_%s'% BG]+data['TNCF_%s'% BD]+data['TNCF_%s'% BC]+data['TNCF_%s'% BF]+data['TNCF_%s'% BI]+data['TNCF_%s'% BBJ])
data['TNCF_%s'% EF]=(data['TNCF_%s'% BM]+data['TNCF_%s'% BN]+data['TNCF_%s'% BO]+data['TNCF_%s'% BP]+data['TNCF_%s'% BQ]+data['TNCF_%s'% BU]+data['TNCF_%s'% BS]+data['TNCF_%s'% BR])

data['BNCF_%s'% EA]=(data['BNCF_%s'% BG]+data['BNCF_%s'% BD]+data['BNCF_%s'% BC])
data['BNCF_%s'% EB]=(data['BNCF_%s'% BI]+data['BNCF_%s'% BBJ])
data['BNCF_%s'% EC]=(data['BNCF_%s'% BG]+data['BNCF_%s'% BD]+data['BNCF_%s'% BC]+data['BNCF_%s'% BF]+data['BNCF_%s'% BI]+data['BNCF_%s'% BBJ])
data['BNCF_%s'% EF]=(data['BNCF_%s'% BM]+data['BNCF_%s'% BN]+data['BNCF_%s'% BO]+data['BNCF_%s'% BP]+data['BNCF_%s'% BQ]+data['BNCF_%s'% BU]+data['BNCF_%s'% BS]+data['BNCF_%s'% BR])

data['ONCF_%s'% EA]=(data['ONCF_%s'% BG]+data['ONCF_%s'% BD]+data['ONCF_%s'% BC])
data['ONCF_%s'% EB]=(data['ONCF_%s'% BI]+data['ONCF_%s'% BBJ])
data['ONCF_%s'% EC]=(data['ONCF_%s'% BG]+data['ONCF_%s'% BD]+data['ONCF_%s'% BC]+data['ONCF_%s'% BF]+data['ONCF_%s'% BI]+data['ONCF_%s'% BBJ])
data['ONCF_%s'% EF]=(data['ONCF_%s'% BM]+data['ONCF_%s'% BN]+data['ONCF_%s'% BO]+data['ONCF_%s'% BP]+data['ONCF_%s'% BQ]+data['ONCF_%s'% BU]+data['ONCF_%s'% BS]+data['ONCF_%s'% BR])

data['TNFM_%s'% EA]=(data['TNFM_%s'% BG]+data['TNFM_%s'% BD]+data['TNFM_%s'% BC])
data['TNFM_%s'% EB]=(data['TNFM_%s'% BI]+data['TNFM_%s'% BBJ])
data['TNFM_%s'% EC]=(data['TNFM_%s'% BG]+data['TNFM_%s'% BD]+data['TNFM_%s'% BC]+data['TNFM_%s'% BF]+data['TNFM_%s'% BI]+data['TNFM_%s'% BBJ])
data['TNFM_%s'% EF]=(data['TNFM_%s'% BM]+data['TNFM_%s'% BN]+data['TNFM_%s'% BO]+data['TNFM_%s'% BP]+data['TNFM_%s'% BQ]+data['TNFM_%s'% BU]+data['TNFM_%s'% BS]+data['TNFM_%s'% BR])

data['BNFM_%s'% EA]=(data['BNFM_%s'% BG]+data['BNFM_%s'% BD]+data['BNFM_%s'% BC])
data['BNFM_%s'% EB]=(data['BNFM_%s'% BI]+data['BNFM_%s'% BBJ])
data['BNFM_%s'% EC]=(data['BNFM_%s'% BG]+data['BNFM_%s'% BD]+data['BNFM_%s'% BC]+data['BNFM_%s'% BF]+data['BNFM_%s'% BI]+data['BNFM_%s'% BBJ])
data['BNFM_%s'% EF]=(data['BNFM_%s'% BM]+data['BNFM_%s'% BN]+data['BNFM_%s'% BO]+data['BNFM_%s'% BP]+data['BNFM_%s'% BQ]+data['BNFM_%s'% BU]+data['BNFM_%s'% BS]+data['BNFM_%s'% BR])

data['ONFM_%s'% EA]=(data['ONFM_%s'% BG]+data['ONFM_%s'% BD]+data['ONFM_%s'% BC])
data['ONFM_%s'% EB]=(data['ONFM_%s'% BI]+data['ONFM_%s'% BBJ])
data['ONFM_%s'% EC]=(data['ONFM_%s'% BG]+data['ONFM_%s'% BD]+data['ONFM_%s'% BC]+data['ONFM_%s'% BF]+data['ONFM_%s'% BI]+data['ONFM_%s'% BBJ])
data['ONFM_%s'% EF]=(data['ONFM_%s'% BM]+data['ONFM_%s'% BN]+data['ONFM_%s'% BO]+data['ONFM_%s'% BP]+data['ONFM_%s'% BQ]+data['ONFM_%s'% BU]+data['ONFM_%s'% BS]+data['ONFM_%s'% BR])

data['TNCM_%s'% EA]=(data['TNCM_%s'% BG]+data['TNCM_%s'% BD]+data['TNCM_%s'% BC])
data['TNCM_%s'% EB]=(data['TNCM_%s'% BI]+data['TNCM_%s'% BBJ])
data['TNCM_%s'% EC]=(data['TNCM_%s'% BG]+data['TNCM_%s'% BD]+data['TNCM_%s'% BC]+data['TNCM_%s'% BF]+data['TNCM_%s'% BI]+data['TNCM_%s'% BBJ])
data['TNCM_%s'% EF]=(data['TNCM_%s'% BM]+data['TNCM_%s'% BN]+data['TNCM_%s'% BO]+data['TNCM_%s'% BP]+data['TNCM_%s'% BQ]+data['TNCM_%s'% BU]+data['TNCM_%s'% BS]+data['TNCM_%s'% BR])

data['BNCM_%s'% EA]=(data['BNCM_%s'% BG]+data['BNCM_%s'% BD]+data['BNCM_%s'% BC])
data['BNCM_%s'% EB]=(data['BNCM_%s'% BI]+data['BNCM_%s'% BBJ])
data['BNCM_%s'% EC]=(data['BNCM_%s'% BG]+data['BNCM_%s'% BD]+data['BNCM_%s'% BC]+data['BNCM_%s'% BF]+data['BNCM_%s'% BI]+data['BNCM_%s'% BBJ])
data['BNCM_%s'% EF]=(data['BNCM_%s'% BM]+data['BNCM_%s'% BN]+data['BNCM_%s'% BO]+data['BNCM_%s'% BP]+data['BNCM_%s'% BQ]+data['BNCM_%s'% BU]+data['BNCM_%s'% BS]+data['BNCM_%s'% BR])

data['ONCM_%s'% EA]=(data['ONCM_%s'% BG]+data['ONCM_%s'% BD]+data['ONCM_%s'% BC])
data['ONCM_%s'% EB]=(data['ONCM_%s'% BI]+data['ONCM_%s'% BBJ])
data['ONCM_%s'% EC]=(data['ONCM_%s'% BG]+data['ONCM_%s'% BD]+data['ONCM_%s'% BC]+data['ONCM_%s'% BF]+data['ONCM_%s'% BI]+data['ONCM_%s'% BBJ])
data['ONCM_%s'% EF]=(data['ONCM_%s'% BM]+data['ONCM_%s'% BN]+data['ONCM_%s'% BO]+data['ONCM_%s'% BP]+data['ONCM_%s'% BQ]+data['ONCM_%s'% BU]+data['ONCM_%s'% BS]+data['ONCM_%s'% BR])

data['TNW_%s'% EA]=(data['TNW_%s'% BG]+data['TNW_%s'% BD]+data['TNW_%s'% BC])
data['TNW_%s'% EB]=(data['TNW_%s'% BI]+data['TNW_%s'% BBJ])
data['TNW_%s'% EC]=(data['TNW_%s'% BG]+data['TNW_%s'% BD]+data['TNW_%s'% BC]+data['TNW_%s'% BF]+data['TNW_%s'% BI]+data['TNW_%s'% BBJ])
data['TNW_%s'% EF]=(data['TNW_%s'% BM]+data['TNW_%s'% BN]+data['TNW_%s'% BO]+data['TNW_%s'% BP]+data['TNW_%s'% BQ]+data['TNW_%s'% BU]+data['TNW_%s'% BS]+data['TNW_%s'% BR])

data['BNW_%s'% EA]=(data['BNW_%s'% BG]+data['BNW_%s'% BD]+data['BNW_%s'% BC])
data['BNW_%s'% EB]=(data['BNW_%s'% BI]+data['BNW_%s'% BBJ])
data['BNW_%s'% EC]=(data['BNW_%s'% BG]+data['BNW_%s'% BD]+data['BNW_%s'% BC]+data['BNW_%s'% BF]+data['BNW_%s'% BI]+data['BNW_%s'% BBJ])
data['BNW_%s'% EF]=(data['BNW_%s'% BM]+data['BNW_%s'% BN]+data['BNW_%s'% BO]+data['BNW_%s'% BP]+data['BNW_%s'% BQ]+data['BNW_%s'% BU]+data['BNW_%s'% BS]+data['BNW_%s'% BR])

data['ONW_%s'% EA]=(data['ONW_%s'% BG]+data['ONW_%s'% BD]+data['ONW_%s'% BC])
data['ONW_%s'% EB]=(data['ONW_%s'% BI]+data['ONW_%s'% BBJ])
data['ONW_%s'% EC]=(data['ONW_%s'% BG]+data['ONW_%s'% BD]+data['ONW_%s'% BC]+data['ONW_%s'% BF]+data['ONW_%s'% BI]+data['ONW_%s'% BBJ])
data['ONW_%s'% EF]=(data['ONW_%s'% BM]+data['ONW_%s'% BN]+data['ONW_%s'% BO]+data['ONW_%s'% BP]+data['ONW_%s'% BQ]+data['ONW_%s'% BU]+data['ONW_%s'% BS]+data['ONW_%s'% BR])

data['TNL_%s'% EA]=(data['TNL_%s'% BG]+data['TNL_%s'% BD]+data['TNL_%s'% BC])
data['TNL_%s'% EB]=(data['TNL_%s'% BI]+data['TNL_%s'% BBJ])
data['TNL_%s'% EC]=(data['TNL_%s'% BG]+data['TNL_%s'% BD]+data['TNL_%s'% BC]+data['TNL_%s'% BF]+data['TNL_%s'% BI]+data['TNL_%s'% BBJ])
data['TNL_%s'% EF]=(data['TNL_%s'% BM]+data['TNL_%s'% BN]+data['TNL_%s'% BO]+data['TNL_%s'% BP]+data['TNL_%s'% BQ]+data['TNL_%s'% BU]+data['TNL_%s'% BS]+data['TNL_%s'% BR])

data['BNL_%s'% EA]=(data['BNL_%s'% BG]+data['BNL_%s'% BD]+data['BNL_%s'% BC])
data['BNL_%s'% EB]=(data['BNL_%s'% BI]+data['BNL_%s'% BBJ])
data['BNL_%s'% EC]=(data['BNL_%s'% BG]+data['BNL_%s'% BD]+data['BNL_%s'% BC]+data['BNL_%s'% BF]+data['BNL_%s'% BI]+data['BNL_%s'% BBJ])
data['BNL_%s'% EF]=(data['BNL_%s'% BM]+data['BNL_%s'% BN]+data['BNL_%s'% BO]+data['BNL_%s'% BP]+data['BNL_%s'% BQ]+data['BNL_%s'% BU]+data['BNL_%s'% BS]+data['BNL_%s'% BR])

data['ONL_%s'% EA]=(data['ONL_%s'% BG]+data['ONL_%s'% BD]+data['ONL_%s'% BC])
data['ONL_%s'% EB]=(data['ONL_%s'% BI]+data['ONL_%s'% BBJ])
data['ONL_%s'% EC]=(data['ONL_%s'% BG]+data['ONL_%s'% BD]+data['ONL_%s'% BC]+data['ONL_%s'% BF]+data['ONL_%s'% BI]+data['ONL_%s'% BBJ])
data['ONL_%s'% EF]=(data['ONL_%s'% BM]+data['ONL_%s'% BN]+data['ONL_%s'% BO]+data['ONL_%s'% BP]+data['ONL_%s'% BQ]+data['ONL_%s'% BU]+data['ONL_%s'% BS]+data['ONL_%s'% BR])

data['TNO_%s'% EA]=(data['TNO_%s'% BG]+data['TNO_%s'% BD]+data['TNO_%s'% BC])
data['TNO_%s'% EB]=(data['TNO_%s'% BI]+data['TNO_%s'% BBJ])
data['TNO_%s'% EC]=(data['TNO_%s'% BG]+data['TNO_%s'% BD]+data['TNO_%s'% BC]+data['TNO_%s'% BF]+data['TNO_%s'% BI]+data['TNO_%s'% BBJ])
data['TNO_%s'% EF]=(data['TNO_%s'% BM]+data['TNO_%s'% BN]+data['TNO_%s'% BO]+data['TNO_%s'% BP]+data['TNO_%s'% BQ]+data['TNO_%s'% BU]+data['TNO_%s'% BS]+data['TNO_%s'% BR])

data['BNO_%s'% EA]=(data['BNO_%s'% BG]+data['BNO_%s'% BD]+data['BNO_%s'% BC])
data['BNO_%s'% EB]=(data['BNO_%s'% BI]+data['BNO_%s'% BBJ])
data['BNO_%s'% EC]=(data['BNO_%s'% BG]+data['BNO_%s'% BD]+data['BNO_%s'% BC]+data['BNO_%s'% BF]+data['BNO_%s'% BI]+data['BNO_%s'% BBJ])
data['BNO_%s'% EF]=(data['BNO_%s'% BM]+data['BNO_%s'% BN]+data['BNO_%s'% BO]+data['BNO_%s'% BP]+data['BNO_%s'% BQ]+data['BNO_%s'% BU]+data['BNO_%s'% BS]+data['BNO_%s'% BR])

data['ONO_%s'% EA]=(data['ONO_%s'% BG]+data['ONO_%s'% BD]+data['ONO_%s'% BC])
data['ONO_%s'% EB]=(data['ONO_%s'% BI]+data['ONO_%s'% BBJ])
data['ONO_%s'% EC]=(data['ONO_%s'% BG]+data['ONO_%s'% BD]+data['ONO_%s'% BC]+data['ONO_%s'% BF]+data['ONO_%s'% BI]+data['ONO_%s'% BBJ])
data['ONO_%s'% EF]=(data['ONO_%s'% BM]+data['ONO_%s'% BN]+data['ONO_%s'% BO]+data['ONO_%s'% BP]+data['ONO_%s'% BQ]+data['ONO_%s'% BU]+data['ONO_%s'% BS]+data['ONO_%s'% BR])

  
# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNCR_%s'% col_name]=(data['TNCF_%s'% col_name]+data['TNCM_%s'% col_name])
    data['TNFR_%s'% col_name]=(data['TNFF_%s'% col_name]+data['TNFM_%s'% col_name])

data['TNCR_%s'% EA]=(data['TNCF_%s'% EA]+data['TNCM_%s'% EA])
data['TNFR_%s'% EA]=(data['TNFF_%s'% EA]+data['TNFM_%s'% EA])
data['TNCR_%s'% EB]=(data['TNCF_%s'% EB]+data['TNCM_%s'% EB])
data['TNFR_%s'% EB]=(data['TNFF_%s'% EB]+data['TNFM_%s'% EB])
data['TNCR_%s'% EC]=(data['TNCF_%s'% EC]+data['TNCM_%s'% EC])
data['TNFR_%s'% EC]=(data['TNFF_%s'% EC]+data['TNFM_%s'% EC])
data['TNCR_%s'% EF]=(data['TNCF_%s'% EF]+data['TNCM_%s'% EF])
data['TNFR_%s'% EF]=(data['TNFF_%s'% EF]+data['TNFM_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNM_%s'% col_name]=(data['TNCM_%s'% col_name]+data['TNFM_%s'% col_name])
    data['TNF_%s'% col_name]=(data['TNFF_%s'% col_name]+data['TNCF_%s'% col_name])

data['TNM_%s'% EA]=(data['TNCM_%s'% EA]+data['TNFM_%s'% EA])
data['TNF_%s'% EA]=(data['TNFF_%s'% EA]+data['TNCF_%s'% EA])
data['TNM_%s'% EB]=(data['TNCM_%s'% EB]+data['TNFM_%s'% EB])
data['TNF_%s'% EB]=(data['TNFF_%s'% EB]+data['TNCF_%s'% EB])
data['TNM_%s'% EC]=(data['TNCM_%s'% EC]+data['TNFM_%s'% EC])
data['TNF_%s'% EC]=(data['TNFF_%s'% EC]+data['TNCF_%s'% EC])
data['TNM_%s'% EF]=(data['TNCM_%s'% EF]+data['TNFM_%s'% EF])
data['TNF_%s'% EF]=(data['TNFF_%s'% EF]+data['TNCF_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BNCR_%s'% col_name]=(data['BNCF_%s'% col_name]+data['BNCM_%s'% col_name])
    data['BNFR_%s'% col_name]=(data['BNFF_%s'% col_name]+data['BNFM_%s'% col_name])

data['BNCR_%s'% EA]=(data['BNCF_%s'% EA]+data['BNCM_%s'% EA])
data['BNFR_%s'% EA]=(data['BNFF_%s'% EA]+data['BNFM_%s'% EA])
data['BNCR_%s'% EB]=(data['BNCF_%s'% EB]+data['BNCM_%s'% EB])
data['BNFR_%s'% EB]=(data['BNFF_%s'% EB]+data['BNFM_%s'% EB])
data['BNCR_%s'% EC]=(data['BNCF_%s'% EC]+data['BNCM_%s'% EC])
data['BNFR_%s'% EC]=(data['BNFF_%s'% EC]+data['BNFM_%s'% EC])
data['BNCR_%s'% EF]=(data['BNCF_%s'% EF]+data['BNCM_%s'% EF])
data['BNFR_%s'% EF]=(data['BNFF_%s'% EF]+data['BNFM_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BNM_%s'% col_name]=(data['BNCM_%s'% col_name]+data['BNFM_%s'% col_name])
    data['BNF_%s'% col_name]=(data['BNFF_%s'% col_name]+data['BNCF_%s'% col_name])

data['BNM_%s'% EA]=(data['BNCM_%s'% EA]+data['BNFM_%s'% EA])
data['BNF_%s'% EA]=(data['BNFF_%s'% EA]+data['BNCF_%s'% EA])
data['BNM_%s'% EB]=(data['BNCM_%s'% EB]+data['BNFM_%s'% EB])
data['BNF_%s'% EB]=(data['BNFF_%s'% EB]+data['BNCF_%s'% EB])
data['BNM_%s'% EC]=(data['BNCM_%s'% EC]+data['BNFM_%s'% EC])
data['BNF_%s'% EC]=(data['BNFF_%s'% EC]+data['BNCF_%s'% EC])
data['BNM_%s'% EF]=(data['BNCM_%s'% EF]+data['BNFM_%s'% EF])
data['BNF_%s'% EF]=(data['BNFF_%s'% EF]+data['BNCF_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONCR_%s'% col_name]=(data['ONCF_%s'% col_name]+data['ONCM_%s'% col_name])
    data['ONFR_%s'% col_name]=(data['ONFF_%s'% col_name]+data['ONFM_%s'% col_name])

data['ONCR_%s'% EA]=(data['ONCF_%s'% EA]+data['ONCM_%s'% EA])
data['ONFR_%s'% EA]=(data['ONFF_%s'% EA]+data['ONFM_%s'% EA])
data['ONCR_%s'% EB]=(data['ONCF_%s'% EB]+data['ONCM_%s'% EB])
data['ONFR_%s'% EB]=(data['ONFF_%s'% EB]+data['ONFM_%s'% EB])
data['ONCR_%s'% EC]=(data['ONCF_%s'% EC]+data['ONCM_%s'% EC])
data['ONFR_%s'% EC]=(data['ONFF_%s'% EC]+data['ONFM_%s'% EC])
data['ONCR_%s'% EF]=(data['ONCF_%s'% EF]+data['ONCM_%s'% EF])
data['ONFR_%s'% EF]=(data['ONFF_%s'% EF]+data['ONFM_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONM_%s'% col_name]=(data['ONCM_%s'% col_name]+data['ONFM_%s'% col_name])
    data['ONF_%s'% col_name]=(data['ONFF_%s'% col_name]+data['ONCF_%s'% col_name])

data['ONM_%s'% EA]=(data['ONCM_%s'% EA]+data['ONFM_%s'% EA])
data['ONF_%s'% EA]=(data['ONFF_%s'% EA]+data['ONCF_%s'% EA])
data['ONM_%s'% EB]=(data['ONCM_%s'% EB]+data['ONFM_%s'% EB])
data['ONF_%s'% EB]=(data['ONFF_%s'% EB]+data['ONCF_%s'% EB])
data['ONM_%s'% EC]=(data['ONCM_%s'% EC]+data['ONFM_%s'% EC])
data['ONF_%s'% EC]=(data['ONFF_%s'% EC]+data['ONCF_%s'% EC])
data['ONM_%s'% EF]=(data['ONCM_%s'% EF]+data['ONFM_%s'% EF])
data['ONF_%s'% EF]=(data['ONFF_%s'% EF]+data['ONCF_%s'% EF])

# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TD_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_num'], np.NaN)
        data['TD_%s'% col_name]= np.where(data['TD_%s'% col_name]==1,data['obs_beh_sumdur'], np.NaN)
        data['TD_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TD_%s'% col_name])
        data['TD_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TD_%s'% col_name])
        data['TD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TD_%s'% col_name]=np.where(data['TD_%s'% col_name]==99999, np.NaN, data['TD_%s'% col_name])
        data['TD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TD_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TD_%s'% col_name]==88888),
            0,data['TD_%s'% col_name])
        data['TD_%s'% col_name]=np.where(data['TD_%s'% col_name]==88888, np.NaN, data['TD_%s'% col_name])
        data['TD_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BD_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_num'], np.NaN)
        data['BD_%s'% col_name]= np.where(data['BD_%s'% col_name]==1,data['obs_beh_loc_sumdur'], np.NaN)
        data['BD_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BD_%s'% col_name])
        data['BD_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BD_%s'% col_name])
        data['BD_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BD_%s'% col_name])
        data['BD_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BD_%s'% col_name])
        data['BD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BD_%s'% col_name]=np.where(data['BD_%s'% col_name]==99999, np.NaN, data['BD_%s'% col_name])
        data['BD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BD_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BD_%s'% col_name]==88888), 
            0,data['BD_%s'% col_name])
        data['BD_%s'% col_name]=np.where(data['BD_%s'% col_name]==88888, np.NaN, data['BD_%s'% col_name])
        data['BD_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['OD_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_num'], np.NaN)
        data['OD_%s'% col_name]= np.where(data['OD_%s'% col_name]==1,data['obs_beh_loc_sumdur'], np.NaN)
        data['OD_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['OD_%s'% col_name])
        data['OD_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['OD_%s'% col_name])
        data['OD_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['OD_%s'% col_name])
        data['OD_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['OD_%s'% col_name])
        data['OD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['OD_%s'% col_name]=np.where(data['OD_%s'% col_name]==99999, np.NaN, data['OD_%s'% col_name])
        data['OD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['OD_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['OD_%s'% col_name]==88888), 
            0,data['OD_%s'% col_name])
        data['OD_%s'% col_name]=np.where(data['OD_%s'% col_name]==88888, np.NaN, data['OD_%s'% col_name])
        data['OD_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additiODal behaviors for total envirODment, burrow, and open field    
data['TD_%s'% EA]=(data['TD_%s'% BG]+data['TD_%s'% BD]+data['TD_%s'% BC])
data['TD_%s'% EB]=(data['TD_%s'% BI]+data['TD_%s'% BBJ])
data['TD_%s'% EC]=(data['TD_%s'% BG]+data['TD_%s'% BD]+data['TD_%s'% BC]+data['TD_%s'% BF]+data['TD_%s'% BI]+data['TD_%s'% BBJ])
data['TD_%s'% ED]=(data['TD_%s'% BB]+data['TD_%s'% BH]+data['TD_%s'% BL])
data['TD_%s'% EE]=(data['TD_%s'% BA]+data['TD_%s'% BI]+data['TD_%s'% BBI]+data['TD_%s'% BBJ])
data['TD_%s'% EF]=(data['TD_%s'% BM]+data['TD_%s'% BD]+data['TD_%s'% BO]+data['TD_%s'% BP]+data['TD_%s'% BQ]+data['TD_%s'% BU]+data['TD_%s'% BS]+data['TD_%s'% BR])
data['TD_%s'% EG]=(data['TD_%s'% BE]+data['TD_%s'% BF])

data['BD_%s'% EA]=(data['BD_%s'% BG]+data['BD_%s'% BD]+data['BD_%s'% BC])
data['BD_%s'% EB]=(data['BD_%s'% BI]+data['BD_%s'% BBJ])
data['BD_%s'% EC]=(data['BD_%s'% BG]+data['BD_%s'% BD]+data['BD_%s'% BC]+data['BD_%s'% BF]+data['BD_%s'% BI]+data['BD_%s'% BBJ])
data['BD_%s'% ED]=(data['BD_%s'% BB]+data['BD_%s'% BH]+data['BD_%s'% BL])
data['BD_%s'% EE]=(data['BD_%s'% BA]+data['BD_%s'% BI]+data['BD_%s'% BBI]+data['BD_%s'% BBJ])
data['BD_%s'% EF]=(data['BD_%s'% BM]+data['BD_%s'% BD]+data['BD_%s'% BO]+data['BD_%s'% BP]+data['BD_%s'% BQ]+data['BD_%s'% BU]+data['BD_%s'% BS]+data['BD_%s'% BR])
data['BD_%s'% EG]=(data['BD_%s'% BE]+data['BD_%s'% BF])

data['OD_%s'% EA]=(data['OD_%s'% BG]+data['OD_%s'% BD]+data['OD_%s'% BC])
data['OD_%s'% EB]=(data['OD_%s'% BI]+data['OD_%s'% BBJ])
data['OD_%s'% EC]=(data['OD_%s'% BG]+data['OD_%s'% BD]+data['OD_%s'% BC]+data['OD_%s'% BF]+data['OD_%s'% BI]+data['OD_%s'% BBJ])
data['OD_%s'% ED]=(data['OD_%s'% BB]+data['OD_%s'% BH]+data['OD_%s'% BL])
data['OD_%s'% EE]=(data['OD_%s'% BA]+data['OD_%s'% BI]+data['OD_%s'% BBI]+data['OD_%s'% BBJ])
data['OD_%s'% EF]=(data['OD_%s'% BM]+data['OD_%s'% BD]+data['OD_%s'% BO]+data['OD_%s'% BP]+data['OD_%s'% BQ]+data['OD_%s'% BU]+data['OD_%s'% BS]+data['OD_%s'% BR])
data['OD_%s'% EG]=(data['OD_%s'% BE]+data['OD_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_num'], np.NaN)
    data['TDFF_%s'% col_name]= np.where(data['TDFF_%s'% col_name]==1,data['obs_beh_treat_sumdur'], np.NaN)
    data['TDFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFF_%s'% col_name]=np.where(data['TDFF_%s'% col_name]==99999, np.NaN, data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFF_%s'% col_name]==88888), 
        0,data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name]=np.where(data['TDFF_%s'% col_name]==88888, np.NaN, data['TDFF_%s'% col_name])
    data['TDFF_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total envirODment
    data['TDCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_num'], np.NaN)
    data['TDCF_%s'% col_name]= np.where(data['TDCF_%s'% col_name]==1,data['obs_beh_treat_sumdur'], np.NaN)
    data['TDCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCF_%s'% col_name]=np.where(data['TDCF_%s'% col_name]==99999, np.NaN, data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCF_%s'% col_name]==88888), 
        0,data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name]=np.where(data['TDCF_%s'% col_name]==88888, np.NaN, data['TDCF_%s'% col_name])
    data['TDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total envirODment
    data['TDFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_num'], np.NaN)
    data['TDFM_%s'% col_name]= np.where(data['TDFM_%s'% col_name]==1,data['obs_beh_treat_sumdur'], np.NaN)
    data['TDFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFM_%s'% col_name]=np.where(data['TDFM_%s'% col_name]==99999, np.NaN, data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFM_%s'% col_name]==88888), 
        0,data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name]=np.where(data['TDFM_%s'% col_name]==88888, np.NaN, data['TDFM_%s'% col_name])
    data['TDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total envirODment
    data['TDCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_num'], np.NaN)
    data['TDCM_%s'% col_name]= np.where(data['TDCM_%s'% col_name]==1,data['obs_beh_treat_sumdur'], np.NaN)
    data['TDCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCM_%s'% col_name]=np.where(data['TDCM_%s'% col_name]==99999, np.NaN, data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCM_%s'% col_name]==88888), 
        0,data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name]=np.where(data['TDCM_%s'% col_name]==88888, np.NaN, data['TDCM_%s'% col_name])
    data['TDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BDFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BDFF_%s'% col_name]= np.where(data['BDFF_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['BDFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_%s'% col_name]=np.where(data['BDFF_%s'% col_name]==99999, np.NaN, data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFF_%s'% col_name]==88888), 
        0,data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name]=np.where(data['BDFF_%s'% col_name]==88888, np.NaN, data['BDFF_%s'% col_name])
    data['BDFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_%s'% col_name]=np.where(data['BDFF_%s'% col_name]==np.NaN,0, data['BDFF_%s'% col_name])

    data['BDCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BDCF_%s'% col_name]= np.where(data['BDCF_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['BDCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_%s'% col_name]=np.where(data['BDCF_%s'% col_name]==99999, np.NaN, data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCF_%s'% col_name]==88888), 
        0,data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name]=np.where(data['BDCF_%s'% col_name]==88888, np.NaN, data['BDCF_%s'% col_name])
    data['BDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_%s'% col_name]=np.where(data['BDCF_%s'% col_name]== np.NaN,0, data['BDCF_%s'% col_name])

    data['BDFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BDFM_%s'% col_name]= np.where(data['BDFM_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['BDFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_%s'% col_name]=np.where(data['BDFM_%s'% col_name]==99999, np.NaN, data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFM_%s'% col_name]==88888), 
        0,data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name]=np.where(data['BDFM_%s'% col_name]==88888, np.NaN, data['BDFM_%s'% col_name])
    data['BDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_%s'% col_name]=np.where(data['BDFM_%s'% col_name]==np.NaN,0, data['BDFM_%s'% col_name])
 
    data['BDCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['BDCM_%s'% col_name]= np.where(data['BDCM_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['BDCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_%s'% col_name]=np.where(data['BDCM_%s'% col_name]==99999, np.NaN, data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCM_%s'% col_name]==88888), 
        0,data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name]=np.where(data['BDCM_%s'% col_name]==88888, np.NaN, data['BDCM_%s'% col_name])
    data['BDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_%s'% col_name]=np.where(data['BDCM_%s'% col_name]== np.NaN,0, data['BDCM_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ODFF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ODFF_%s'% col_name]= np.where(data['ODFF_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['ODFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_%s'% col_name]=np.where(data['ODFF_%s'% col_name]==99999, np.NaN, data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFF_%s'% col_name]==88888), 
        0,data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name]=np.where(data['ODFF_%s'% col_name]==88888, np.NaN, data['ODFF_%s'% col_name])
    data['ODFF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_%s'% col_name]=np.where(data['ODFF_%s'% col_name]== np.NaN,0, data['ODFF_%s'% col_name])

    data['ODCF_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ODCF_%s'% col_name]= np.where(data['ODCF_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['ODCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_%s'% col_name]=np.where(data['ODCF_%s'% col_name]==99999, np.NaN, data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCF_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCF_%s'% col_name]==88888), 
        0,data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name]=np.where(data['ODCF_%s'% col_name]==88888, np.NaN, data['ODCF_%s'% col_name])
    data['ODCF_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_%s'% col_name]=np.where(data['ODCF_%s'% col_name]== np.NaN,0, data['ODCF_%s'% col_name])
    
    data['ODFM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ODFM_%s'% col_name]= np.where(data['ODFM_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['ODFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_%s'% col_name]=np.where(data['ODFM_%s'% col_name]==99999, np.NaN, data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFM_%s'% col_name]==88888), 
        0,data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name]=np.where(data['ODFM_%s'% col_name]==88888, np.NaN, data['ODFM_%s'% col_name])
    data['ODFM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_%s'% col_name]=np.where(data['ODFM_%s'% col_name]== np.NaN,0, data['ODFM_%s'% col_name])

    data['ODCM_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_num'], np.NaN)
    data['ODCM_%s'% col_name]= np.where(data['ODCM_%s'% col_name]==1,data['obs_beh_loc_treat_sumdur'], np.NaN)
    data['ODCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_%s'% col_name]=np.where(data['ODCM_%s'% col_name]==99999, np.NaN, data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCM_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCM_%s'% col_name]==88888), 
        0,data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name]=np.where(data['ODCM_%s'% col_name]==88888, np.NaN, data['ODCM_%s'% col_name])
    data['ODCM_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_%s'% col_name]=np.where(data['ODCM_%s'% col_name]== np.NaN,0, data['ODCM_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TDW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_num'], np.NaN)
    data['TDW_%s'% col_name]= np.where(data['TDW_%s'% col_name]==1,data['obs_beh_modwinner_sumdur'], np.NaN)
    data['TDW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDW_%s'% col_name])
    data['TDW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TDW_%s'% col_name])
    data['TDW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDW_%s'% col_name])
    data['TDW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TDW_%s'% col_name])
    data['TDW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDW_%s'% col_name]=np.where(data['TDW_%s'% col_name]==99999, np.NaN, data['TDW_%s'% col_name])
    data['TDW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDW_%s'% col_name]==88888), 
        0,data['TDW_%s'% col_name])
    data['TDW_%s'% col_name]=np.where(data['TDW_%s'% col_name]==88888, np.NaN, data['TDW_%s'% col_name])
    data['TDW_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TDL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_num'], np.NaN)
    data['TDL_%s'% col_name]= np.where(data['TDL_%s'% col_name]==1,data['obs_beh_modwinner_sumdur'], np.NaN)
    data['TDL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDL_%s'% col_name])
    data['TDL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TDL_%s'% col_name])
    data['TDL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDL_%s'% col_name])
    data['TDL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TDL_%s'% col_name])
    data['TDL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDL_%s'% col_name]=np.where(data['TDL_%s'% col_name]==99999, np.NaN, data['TDL_%s'% col_name])
    data['TDL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDL_%s'% col_name]==88888), 
        0,data['TDL_%s'% col_name])
    data['TDL_%s'% col_name]=np.where(data['TDL_%s'% col_name]==88888, np.NaN, data['TDL_%s'% col_name])
    data['TDL_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TDO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')),data['obs_beh_modwinner_num'], np.NaN)
    data['TDO_%s'% col_name]= np.where(data['TDO_%s'% col_name]==1,data['obs_beh_modwinner_sumdur'], np.NaN)
    data['TDO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDO_%s'% col_name])
    data['TDO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TDO_%s'% col_name])
    data['TDO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDO_%s'% col_name])
    data['TDO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TDO_%s'% col_name])
    data['TDO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDO_%s'% col_name]=np.where(data['TDO_%s'% col_name]==99999, np.NaN, data['TDO_%s'% col_name])
    data['TDO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDO_%s'% col_name]==88888), 
        0,data['TDO_%s'% col_name])
    data['TDO_%s'% col_name]=np.where(data['TDO_%s'% col_name]==88888, np.NaN, data['TDO_%s'% col_name])
    data['TDO_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BDW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BDW_%s'% col_name]= np.where(data['BDW_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['BDW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_%s'% col_name]=np.where(data['BDW_%s'% col_name]==99999, np.NaN, data['BDW_%s'% col_name])
    data['BDW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDW_%s'% col_name]==88888), 
        0,data['BDW_%s'% col_name])
    data['BDW_%s'% col_name]=np.where(data['BDW_%s'% col_name]==88888, np.NaN, data['BDW_%s'% col_name])
    data['BDW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_%s'% col_name]=np.where(data['BDW_%s'% col_name]== np.NaN,0, data['BDW_%s'% col_name])

    data['BDL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BDL_%s'% col_name]= np.where(data['BDL_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['BDL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_%s'% col_name]=np.where(data['BDL_%s'% col_name]==99999, np.NaN, data['BDL_%s'% col_name])
    data['BDL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDL_%s'% col_name]==88888), 
        0,data['BDL_%s'% col_name])
    data['BDL_%s'% col_name]=np.where(data['BDL_%s'% col_name]==88888, np.NaN, data['BDL_%s'% col_name])
    data['BDL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_%s'% col_name]=np.where(data['BDL_%s'% col_name]== np.NaN,0, data['BDL_%s'% col_name])

    data['BDO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['BDO_%s'% col_name]= np.where(data['BDO_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['BDO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_%s'% col_name]=np.where(data['BDO_%s'% col_name]==99999, np.NaN, data['BDO_%s'% col_name])
    data['BDO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDO_%s'% col_name]==88888), 
        0,data['BDO_%s'% col_name])
    data['BDO_%s'% col_name]=np.where(data['BDO_%s'% col_name]==88888, np.NaN, data['BDO_%s'% col_name])
    data['BDO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_%s'% col_name]=np.where(data['BDO_%s'% col_name]== np.NaN,0, data['BDO_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ODW_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ODW_%s'% col_name]= np.where(data['ODW_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['ODW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_%s'% col_name]=np.where(data['ODW_%s'% col_name]==99999, np.NaN, data['ODW_%s'% col_name])
    data['ODW_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODW_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODW_%s'% col_name]==88888), 
        0,data['ODW_%s'% col_name])
    data['ODW_%s'% col_name]=np.where(data['ODW_%s'% col_name]==88888, np.NaN, data['ODW_%s'% col_name])
    data['ODW_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_%s'% col_name]=np.where(data['ODW_%s'% col_name]== np.NaN,0, data['ODW_%s'% col_name])

    data['ODL_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ODL_%s'% col_name]= np.where(data['ODL_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['ODL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_%s'% col_name]=np.where(data['ODL_%s'% col_name]==99999, np.NaN, data['ODL_%s'% col_name])
    data['ODL_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODL_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODL_%s'% col_name]==88888), 
        0,data['ODL_%s'% col_name])
    data['ODL_%s'% col_name]=np.where(data['ODL_%s'% col_name]==88888, np.NaN, data['ODL_%s'% col_name])
    data['ODL_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_%s'% col_name]=np.where(data['ODL_%s'% col_name]== np.NaN,0, data['ODL_%s'% col_name])

    data['ODO_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_num'], np.NaN)
    data['ODO_%s'% col_name]= np.where(data['ODO_%s'% col_name]==1,data['obs_beh_loc_modwinner_sumdur'], np.NaN)
    data['ODO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_%s'% col_name]=np.where(data['ODO_%s'% col_name]==99999, np.NaN, data['ODO_%s'% col_name])
    data['ODO_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODO_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODO_%s'% col_name]==88888), 
        0,data['ODO_%s'% col_name])
    data['ODO_%s'% col_name]=np.where(data['ODO_%s'% col_name]==88888, np.NaN, data['ODO_%s'% col_name])
    data['ODO_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_%s'% col_name]=np.where(data['ODO_%s'% col_name]== np.NaN,0, data['ODO_%s'% col_name])

# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TDFF_%s'% EA]=(data['TDFF_%s'% BG]+data['TDFF_%s'% BD]+data['TDFF_%s'% BC])
data['TDFF_%s'% EB]=(data['TDFF_%s'% BI]+data['TDFF_%s'% BBJ])
data['TDFF_%s'% EC]=(data['TDFF_%s'% BG]+data['TDFF_%s'% BD]+data['TDFF_%s'% BC]+data['TDFF_%s'% BF]+data['TDFF_%s'% BI]+data['TDFF_%s'% BBJ])
data['TDFF_%s'% EF]=(data['TDFF_%s'% BM]+data['TDFF_%s'% BN]+data['TDFF_%s'% BO]+data['TDFF_%s'% BP]+data['TDFF_%s'% BQ]+data['TDFF_%s'% BU]+data['TDFF_%s'% BS]+data['TDFF_%s'% BR])

data['BDFF_%s'% EA]=(data['BDFF_%s'% BG]+data['BDFF_%s'% BD]+data['BDFF_%s'% BC])
data['BDFF_%s'% EB]=(data['BDFF_%s'% BI]+data['BDFF_%s'% BBJ])
data['BDFF_%s'% EC]=(data['BDFF_%s'% BG]+data['BDFF_%s'% BD]+data['BDFF_%s'% BC]+data['BDFF_%s'% BF]+data['BDFF_%s'% BI]+data['BDFF_%s'% BBJ])
data['BDFF_%s'% EF]=(data['BDFF_%s'% BM]+data['BDFF_%s'% BN]+data['BDFF_%s'% BO]+data['BDFF_%s'% BP]+data['BDFF_%s'% BQ]+data['BDFF_%s'% BU]+data['BDFF_%s'% BS]+data['BDFF_%s'% BR])

data['ODFF_%s'% EA]=(data['ODFF_%s'% BG]+data['ODFF_%s'% BD]+data['ODFF_%s'% BC])
data['ODFF_%s'% EB]=(data['ODFF_%s'% BI]+data['ODFF_%s'% BBJ])
data['ODFF_%s'% EC]=(data['ODFF_%s'% BG]+data['ODFF_%s'% BD]+data['ODFF_%s'% BC]+data['ODFF_%s'% BF]+data['ODFF_%s'% BI]+data['ODFF_%s'% BBJ])
data['ODFF_%s'% EF]=(data['ODFF_%s'% BM]+data['ODFF_%s'% BN]+data['ODFF_%s'% BO]+data['ODFF_%s'% BP]+data['ODFF_%s'% BQ]+data['ODFF_%s'% BU]+data['ODFF_%s'% BS]+data['ODFF_%s'% BR])

data['TDCF_%s'% EA]=(data['TDCF_%s'% BG]+data['TDCF_%s'% BD]+data['TDCF_%s'% BC])
data['TDCF_%s'% EB]=(data['TDCF_%s'% BI]+data['TDCF_%s'% BBJ])
data['TDCF_%s'% EC]=(data['TDCF_%s'% BG]+data['TDCF_%s'% BD]+data['TDCF_%s'% BC]+data['TDCF_%s'% BF]+data['TDCF_%s'% BI]+data['TDCF_%s'% BBJ])
data['TDCF_%s'% EF]=(data['TDCF_%s'% BM]+data['TDCF_%s'% BN]+data['TDCF_%s'% BO]+data['TDCF_%s'% BP]+data['TDCF_%s'% BQ]+data['TDCF_%s'% BU]+data['TDCF_%s'% BS]+data['TDCF_%s'% BR])

data['BDCF_%s'% EA]=(data['BDCF_%s'% BG]+data['BDCF_%s'% BD]+data['BDCF_%s'% BC])
data['BDCF_%s'% EB]=(data['BDCF_%s'% BI]+data['BDCF_%s'% BBJ])
data['BDCF_%s'% EC]=(data['BDCF_%s'% BG]+data['BDCF_%s'% BD]+data['BDCF_%s'% BC]+data['BDCF_%s'% BF]+data['BDCF_%s'% BI]+data['BDCF_%s'% BBJ])
data['BDCF_%s'% EF]=(data['BDCF_%s'% BM]+data['BDCF_%s'% BN]+data['BDCF_%s'% BO]+data['BDCF_%s'% BP]+data['BDCF_%s'% BQ]+data['BDCF_%s'% BU]+data['BDCF_%s'% BS]+data['BDCF_%s'% BR])

data['ODCF_%s'% EA]=(data['ODCF_%s'% BG]+data['ODCF_%s'% BD]+data['ODCF_%s'% BC])
data['ODCF_%s'% EB]=(data['ODCF_%s'% BI]+data['ODCF_%s'% BBJ])
data['ODCF_%s'% EC]=(data['ODCF_%s'% BG]+data['ODCF_%s'% BD]+data['ODCF_%s'% BC]+data['ODCF_%s'% BF]+data['ODCF_%s'% BI]+data['ODCF_%s'% BBJ])
data['ODCF_%s'% EF]=(data['ODCF_%s'% BM]+data['ODCF_%s'% BN]+data['ODCF_%s'% BO]+data['ODCF_%s'% BP]+data['ODCF_%s'% BQ]+data['ODCF_%s'% BU]+data['ODCF_%s'% BS]+data['ODCF_%s'% BR])

data['TDFM_%s'% EA]=(data['TDFM_%s'% BG]+data['TDFM_%s'% BD]+data['TDFM_%s'% BC])
data['TDFM_%s'% EB]=(data['TDFM_%s'% BI]+data['TDFM_%s'% BBJ])
data['TDFM_%s'% EC]=(data['TDFM_%s'% BG]+data['TDFM_%s'% BD]+data['TDFM_%s'% BC]+data['TDFM_%s'% BF]+data['TDFM_%s'% BI]+data['TDFM_%s'% BBJ])
data['TDFM_%s'% EF]=(data['TDFM_%s'% BM]+data['TDFM_%s'% BN]+data['TDFM_%s'% BO]+data['TDFM_%s'% BP]+data['TDFM_%s'% BQ]+data['TDFM_%s'% BU]+data['TDFM_%s'% BS]+data['TDFM_%s'% BR])

data['BDFM_%s'% EA]=(data['BDFM_%s'% BG]+data['BDFM_%s'% BD]+data['BDFM_%s'% BC])
data['BDFM_%s'% EB]=(data['BDFM_%s'% BI]+data['BDFM_%s'% BBJ])
data['BDFM_%s'% EC]=(data['BDFM_%s'% BG]+data['BDFM_%s'% BD]+data['BDFM_%s'% BC]+data['BDFM_%s'% BF]+data['BDFM_%s'% BI]+data['BDFM_%s'% BBJ])
data['BDFM_%s'% EF]=(data['BDFM_%s'% BM]+data['BDFM_%s'% BN]+data['BDFM_%s'% BO]+data['BDFM_%s'% BP]+data['BDFM_%s'% BQ]+data['BDFM_%s'% BU]+data['BDFM_%s'% BS]+data['BDFM_%s'% BR])

data['ODFM_%s'% EA]=(data['ODFM_%s'% BG]+data['ODFM_%s'% BD]+data['ODFM_%s'% BC])
data['ODFM_%s'% EB]=(data['ODFM_%s'% BI]+data['ODFM_%s'% BBJ])
data['ODFM_%s'% EC]=(data['ODFM_%s'% BG]+data['ODFM_%s'% BD]+data['ODFM_%s'% BC]+data['ODFM_%s'% BF]+data['ODFM_%s'% BI]+data['ODFM_%s'% BBJ])
data['ODFM_%s'% EF]=(data['ODFM_%s'% BM]+data['ODFM_%s'% BN]+data['ODFM_%s'% BO]+data['ODFM_%s'% BP]+data['ODFM_%s'% BQ]+data['ODFM_%s'% BU]+data['ODFM_%s'% BS]+data['ODFM_%s'% BR])

data['TDCM_%s'% EA]=(data['TDCM_%s'% BG]+data['TDCM_%s'% BD]+data['TDCM_%s'% BC])
data['TDCM_%s'% EB]=(data['TDCM_%s'% BI]+data['TDCM_%s'% BBJ])
data['TDCM_%s'% EC]=(data['TDCM_%s'% BG]+data['TDCM_%s'% BD]+data['TDCM_%s'% BC]+data['TDCM_%s'% BF]+data['TDCM_%s'% BI]+data['TDCM_%s'% BBJ])
data['TDCM_%s'% EF]=(data['TDCM_%s'% BM]+data['TDCM_%s'% BN]+data['TDCM_%s'% BO]+data['TDCM_%s'% BP]+data['TDCM_%s'% BQ]+data['TDCM_%s'% BU]+data['TDCM_%s'% BS]+data['TDCM_%s'% BR])

data['BDCM_%s'% EA]=(data['BDCM_%s'% BG]+data['BDCM_%s'% BD]+data['BDCM_%s'% BC])
data['BDCM_%s'% EB]=(data['BDCM_%s'% BI]+data['BDCM_%s'% BBJ])
data['BDCM_%s'% EC]=(data['BDCM_%s'% BG]+data['BDCM_%s'% BD]+data['BDCM_%s'% BC]+data['BDCM_%s'% BF]+data['BDCM_%s'% BI]+data['BDCM_%s'% BBJ])
data['BDCM_%s'% EF]=(data['BDCM_%s'% BM]+data['BDCM_%s'% BN]+data['BDCM_%s'% BO]+data['BDCM_%s'% BP]+data['BDCM_%s'% BQ]+data['BDCM_%s'% BU]+data['BDCM_%s'% BS]+data['BDCM_%s'% BR])

data['ODCM_%s'% EA]=(data['ODCM_%s'% BG]+data['ODCM_%s'% BD]+data['ODCM_%s'% BC])
data['ODCM_%s'% EB]=(data['ODCM_%s'% BI]+data['ODCM_%s'% BBJ])
data['ODCM_%s'% EC]=(data['ODCM_%s'% BG]+data['ODCM_%s'% BD]+data['ODCM_%s'% BC]+data['ODCM_%s'% BF]+data['ODCM_%s'% BI]+data['ODCM_%s'% BBJ])
data['ODCM_%s'% EF]=(data['ODCM_%s'% BM]+data['ODCM_%s'% BN]+data['ODCM_%s'% BO]+data['ODCM_%s'% BP]+data['ODCM_%s'% BQ]+data['ODCM_%s'% BU]+data['ODCM_%s'% BS]+data['ODCM_%s'% BR])
   
data['TDW_%s'% EA]=(data['TDW_%s'% BG]+data['TDW_%s'% BD]+data['TDW_%s'% BC])
data['TDW_%s'% EB]=(data['TDW_%s'% BI]+data['TDW_%s'% BBJ])
data['TDW_%s'% EC]=(data['TDW_%s'% BG]+data['TDW_%s'% BD]+data['TDW_%s'% BC]+data['TDW_%s'% BF]+data['TDW_%s'% BI]+data['TDW_%s'% BBJ])
data['TDW_%s'% EF]=(data['TDW_%s'% BM]+data['TDW_%s'% BN]+data['TDW_%s'% BO]+data['TDW_%s'% BP]+data['TDW_%s'% BQ]+data['TDW_%s'% BU]+data['TDW_%s'% BS]+data['TDW_%s'% BR])

data['BDW_%s'% EA]=(data['BDW_%s'% BG]+data['BDW_%s'% BD]+data['BDW_%s'% BC])
data['BDW_%s'% EB]=(data['BDW_%s'% BI]+data['BDW_%s'% BBJ])
data['BDW_%s'% EC]=(data['BDW_%s'% BG]+data['BDW_%s'% BD]+data['BDW_%s'% BC]+data['BDW_%s'% BF]+data['BDW_%s'% BI]+data['BDW_%s'% BBJ])
data['BDW_%s'% EF]=(data['BDW_%s'% BM]+data['BDW_%s'% BN]+data['BDW_%s'% BO]+data['BDW_%s'% BP]+data['BDW_%s'% BQ]+data['BDW_%s'% BU]+data['BDW_%s'% BS]+data['BDW_%s'% BR])

data['ODW_%s'% EA]=(data['ODW_%s'% BG]+data['ODW_%s'% BD]+data['ODW_%s'% BC])
data['ODW_%s'% EB]=(data['ODW_%s'% BI]+data['ODW_%s'% BBJ])
data['ODW_%s'% EC]=(data['ODW_%s'% BG]+data['ODW_%s'% BD]+data['ODW_%s'% BC]+data['ODW_%s'% BF]+data['ODW_%s'% BI]+data['ODW_%s'% BBJ])
data['ODW_%s'% EF]=(data['ODW_%s'% BM]+data['ODW_%s'% BN]+data['ODW_%s'% BO]+data['ODW_%s'% BP]+data['ODW_%s'% BQ]+data['ODW_%s'% BU]+data['ODW_%s'% BS]+data['ODW_%s'% BR])

data['TDL_%s'% EA]=(data['TDL_%s'% BG]+data['TDL_%s'% BD]+data['TDL_%s'% BC])
data['TDL_%s'% EB]=(data['TDL_%s'% BI]+data['TDL_%s'% BBJ])
data['TDL_%s'% EC]=(data['TDL_%s'% BG]+data['TDL_%s'% BD]+data['TDL_%s'% BC]+data['TDL_%s'% BF]+data['TDL_%s'% BI]+data['TDL_%s'% BBJ])
data['TDL_%s'% EF]=(data['TDL_%s'% BM]+data['TDL_%s'% BN]+data['TDL_%s'% BO]+data['TDL_%s'% BP]+data['TDL_%s'% BQ]+data['TDL_%s'% BU]+data['TDL_%s'% BS]+data['TDL_%s'% BR])

data['BDL_%s'% EA]=(data['BDL_%s'% BG]+data['BDL_%s'% BD]+data['BDL_%s'% BC])
data['BDL_%s'% EB]=(data['BDL_%s'% BI]+data['BDL_%s'% BBJ])
data['BDL_%s'% EC]=(data['BDL_%s'% BG]+data['BDL_%s'% BD]+data['BDL_%s'% BC]+data['BDL_%s'% BF]+data['BDL_%s'% BI]+data['BDL_%s'% BBJ])
data['BDL_%s'% EF]=(data['BDL_%s'% BM]+data['BDL_%s'% BN]+data['BDL_%s'% BO]+data['BDL_%s'% BP]+data['BDL_%s'% BQ]+data['BDL_%s'% BU]+data['BDL_%s'% BS]+data['BDL_%s'% BR])

data['ODL_%s'% EA]=(data['ODL_%s'% BG]+data['ODL_%s'% BD]+data['ODL_%s'% BC])
data['ODL_%s'% EB]=(data['ODL_%s'% BI]+data['ODL_%s'% BBJ])
data['ODL_%s'% EC]=(data['ODL_%s'% BG]+data['ODL_%s'% BD]+data['ODL_%s'% BC]+data['ODL_%s'% BF]+data['ODL_%s'% BI]+data['ODL_%s'% BBJ])
data['ODL_%s'% EF]=(data['ODL_%s'% BM]+data['ODL_%s'% BN]+data['ODL_%s'% BO]+data['ODL_%s'% BP]+data['ODL_%s'% BQ]+data['ODL_%s'% BU]+data['ODL_%s'% BS]+data['ODL_%s'% BR])

data['TDO_%s'% EA]=(data['TDO_%s'% BG]+data['TDO_%s'% BD]+data['TDO_%s'% BC])
data['TDO_%s'% EB]=(data['TDO_%s'% BI]+data['TDO_%s'% BBJ])
data['TDO_%s'% EC]=(data['TDO_%s'% BG]+data['TDO_%s'% BD]+data['TDO_%s'% BC]+data['TDO_%s'% BF]+data['TDO_%s'% BI]+data['TDO_%s'% BBJ])
data['TDO_%s'% EF]=(data['TDO_%s'% BM]+data['TDO_%s'% BN]+data['TDO_%s'% BO]+data['TDO_%s'% BP]+data['TDO_%s'% BQ]+data['TDO_%s'% BU]+data['TDO_%s'% BS]+data['TDO_%s'% BR])

data['BDO_%s'% EA]=(data['BDO_%s'% BG]+data['BDO_%s'% BD]+data['BDO_%s'% BC])
data['BDO_%s'% EB]=(data['BDO_%s'% BI]+data['BDO_%s'% BBJ])
data['BDO_%s'% EC]=(data['BDO_%s'% BG]+data['BDO_%s'% BD]+data['BDO_%s'% BC]+data['BDO_%s'% BF]+data['BDO_%s'% BI]+data['BDO_%s'% BBJ])
data['BDO_%s'% EF]=(data['BDO_%s'% BM]+data['BDO_%s'% BN]+data['BDO_%s'% BO]+data['BDO_%s'% BP]+data['BDO_%s'% BQ]+data['BDO_%s'% BU]+data['BDO_%s'% BS]+data['BDO_%s'% BR])

data['ODO_%s'% EA]=(data['ODO_%s'% BG]+data['ODO_%s'% BD]+data['ODO_%s'% BC])
data['ODO_%s'% EB]=(data['ODO_%s'% BI]+data['ODO_%s'% BBJ])
data['ODO_%s'% EC]=(data['ODO_%s'% BG]+data['ODO_%s'% BD]+data['ODO_%s'% BC]+data['ODO_%s'% BF]+data['ODO_%s'% BI]+data['ODO_%s'% BBJ])
data['ODO_%s'% EF]=(data['ODO_%s'% BM]+data['ODO_%s'% BN]+data['ODO_%s'% BO]+data['ODO_%s'% BP]+data['ODO_%s'% BQ]+data['ODO_%s'% BU]+data['ODO_%s'% BS]+data['ODO_%s'% BR])


# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDCR_%s'% col_name]=(data['TDCF_%s'% col_name]+data['TDCM_%s'% col_name])
    data['TDFR_%s'% col_name]=(data['TDFF_%s'% col_name]+data['TDFM_%s'% col_name])

data['TDCR_%s'% EA]=(data['TDCF_%s'% EA]+data['TDCM_%s'% EA])
data['TDFR_%s'% EA]=(data['TDFF_%s'% EA]+data['TDFM_%s'% EA])
data['TDCR_%s'% EB]=(data['TDCF_%s'% EB]+data['TDCM_%s'% EB])
data['TDFR_%s'% EB]=(data['TDFF_%s'% EB]+data['TDFM_%s'% EB])
data['TDCR_%s'% EC]=(data['TDCF_%s'% EC]+data['TDCM_%s'% EC])
data['TDFR_%s'% EC]=(data['TDFF_%s'% EC]+data['TDFM_%s'% EC])
data['TDCR_%s'% EF]=(data['TDCF_%s'% EF]+data['TDCM_%s'% EF])
data['TDFR_%s'% EF]=(data['TDFF_%s'% EF]+data['TDFM_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDM_%s'% col_name]=(data['TDCM_%s'% col_name]+data['TDFM_%s'% col_name])
    data['TDF_%s'% col_name]=(data['TDFF_%s'% col_name]+data['TDCF_%s'% col_name])

data['TDM_%s'% EA]=(data['TDCM_%s'% EA]+data['TDFM_%s'% EA])
data['TDF_%s'% EA]=(data['TDFF_%s'% EA]+data['TDCF_%s'% EA])
data['TDM_%s'% EB]=(data['TDCM_%s'% EB]+data['TDFM_%s'% EB])
data['TDF_%s'% EB]=(data['TDFF_%s'% EB]+data['TDCF_%s'% EB])
data['TDM_%s'% EC]=(data['TDCM_%s'% EC]+data['TDFM_%s'% EC])
data['TDF_%s'% EC]=(data['TDFF_%s'% EC]+data['TDCF_%s'% EC])
data['TDM_%s'% EF]=(data['TDCM_%s'% EF]+data['TDFM_%s'% EF])
data['TDF_%s'% EF]=(data['TDFF_%s'% EF]+data['TDCF_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BDCR_%s'% col_name]=(data['BDCF_%s'% col_name]+data['BDCM_%s'% col_name])
    data['BDFR_%s'% col_name]=(data['BDFF_%s'% col_name]+data['BDFM_%s'% col_name])

data['BDCR_%s'% EA]=(data['BDCF_%s'% EA]+data['BDCM_%s'% EA])
data['BDFR_%s'% EA]=(data['BDFF_%s'% EA]+data['BDFM_%s'% EA])
data['BDCR_%s'% EB]=(data['BDCF_%s'% EB]+data['BDCM_%s'% EB])
data['BDFR_%s'% EB]=(data['BDFF_%s'% EB]+data['BDFM_%s'% EB])
data['BDCR_%s'% EC]=(data['BDCF_%s'% EC]+data['BDCM_%s'% EC])
data['BDFR_%s'% EC]=(data['BDFF_%s'% EC]+data['BDFM_%s'% EC])
data['BDCR_%s'% EF]=(data['BDCF_%s'% EF]+data['BDCM_%s'% EF])
data['BDFR_%s'% EF]=(data['BDFF_%s'% EF]+data['BDFM_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BDM_%s'% col_name]=(data['BDCM_%s'% col_name]+data['BDFM_%s'% col_name])
    data['BDF_%s'% col_name]=(data['BDFF_%s'% col_name]+data['BDCF_%s'% col_name])

data['BDM_%s'% EA]=(data['BDCM_%s'% EA]+data['BDFM_%s'% EA])
data['BDF_%s'% EA]=(data['BDFF_%s'% EA]+data['BDCF_%s'% EA])
data['BDM_%s'% EB]=(data['BDCM_%s'% EB]+data['BDFM_%s'% EB])
data['BDF_%s'% EB]=(data['BDFF_%s'% EB]+data['BDCF_%s'% EB])
data['BDM_%s'% EC]=(data['BDCM_%s'% EC]+data['BDFM_%s'% EC])
data['BDF_%s'% EC]=(data['BDFF_%s'% EC]+data['BDCF_%s'% EC])
data['BDM_%s'% EF]=(data['BDCM_%s'% EF]+data['BDFM_%s'% EF])
data['BDF_%s'% EF]=(data['BDFF_%s'% EF]+data['BDCF_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODCR_%s'% col_name]=(data['ODCF_%s'% col_name]+data['ODCM_%s'% col_name])
    data['ODFR_%s'% col_name]=(data['ODFF_%s'% col_name]+data['ODFM_%s'% col_name])

data['ODCR_%s'% EA]=(data['ODCF_%s'% EA]+data['ODCM_%s'% EA])
data['ODFR_%s'% EA]=(data['ODFF_%s'% EA]+data['ODFM_%s'% EA])
data['ODCR_%s'% EB]=(data['ODCF_%s'% EB]+data['ODCM_%s'% EB])
data['ODFR_%s'% EB]=(data['ODFF_%s'% EB]+data['ODFM_%s'% EB])
data['ODCR_%s'% EC]=(data['ODCF_%s'% EC]+data['ODCM_%s'% EC])
data['ODFR_%s'% EC]=(data['ODFF_%s'% EC]+data['ODFM_%s'% EC])
data['ODCR_%s'% EF]=(data['ODCF_%s'% EF]+data['ODCM_%s'% EF])
data['ODFR_%s'% EF]=(data['ODFF_%s'% EF]+data['ODFM_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODM_%s'% col_name]=(data['ODCM_%s'% col_name]+data['ODFM_%s'% col_name])
    data['ODF_%s'% col_name]=(data['ODFF_%s'% col_name]+data['ODCF_%s'% col_name])

data['ODM_%s'% EA]=(data['ODCM_%s'% EA]+data['ODFM_%s'% EA])
data['ODF_%s'% EA]=(data['ODFF_%s'% EA]+data['ODCF_%s'% EA])
data['ODM_%s'% EB]=(data['ODCM_%s'% EB]+data['ODFM_%s'% EB])
data['ODF_%s'% EB]=(data['ODFF_%s'% EB]+data['ODCF_%s'% EB])
data['ODM_%s'% EC]=(data['ODCM_%s'% EC]+data['ODFM_%s'% EC])
data['ODF_%s'% EC]=(data['ODFF_%s'% EC]+data['ODCF_%s'% EC])
data['ODM_%s'% EF]=(data['ODCM_%s'% EF]+data['ODFM_%s'% EF])
data['ODF_%s'% EF]=(data['ODFF_%s'% EF]+data['ODCF_%s'% EF])
   
#NOW FOR THE ROLE OF EACH RAT
# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TN_role_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_role_num'], np.NaN)
        data['TN_role_%s'% col_name]= np.where(data['TN_role_%s'% col_name]==1,data['obs_beh_role_num_back'], np.NaN)
        data['TN_role_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TN_role_%s'% col_name])
        data['TN_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TN_role_%s'% col_name])
        data['TN_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TN_role_%s'% col_name]=np.where(data['TN_role_%s'% col_name]==99999, np.NaN, data['TN_role_%s'% col_name])
        data['TN_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TN_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TN_role_%s'% col_name]==88888),
            0,data['TN_role_%s'% col_name])
        data['TN_role_%s'% col_name]=np.where(data['TN_role_%s'% col_name]==88888, np.NaN, data['TN_role_%s'% col_name])
        data['TN_role_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BN_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_role_num'], np.NaN)
        data['BN_role_%s'% col_name]= np.where(data['BN_role_%s'% col_name]==1,data['obs_beh_loc_role_num_back'], np.NaN)
        data['BN_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BN_role_%s'% col_name]=np.where(data['BN_role_%s'% col_name]==99999, np.NaN, data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BN_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BN_role_%s'% col_name]==88888), 
            0,data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name]=np.where(data['BN_role_%s'% col_name]==88888, np.NaN, data['BN_role_%s'% col_name])
        data['BN_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['ON_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_role_num'], np.NaN)
        data['ON_role_%s'% col_name]= np.where(data['ON_role_%s'% col_name]==1,data['obs_beh_loc_role_num_back'], np.NaN)
        data['ON_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ON_role_%s'% col_name]=np.where(data['ON_role_%s'% col_name]==99999, np.NaN, data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ON_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ON_role_%s'% col_name]==88888), 
            0,data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name]=np.where(data['ON_role_%s'% col_name]==88888, np.NaN, data['ON_role_%s'% col_name])
        data['ON_role_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additional behaviors for total environment, burrow, and open field    
data['TN_role_%s'% EA]=(data['TN_role_%s'% BG]+data['TN_role_%s'% BD]+data['TN_role_%s'% BC])
data['TN_role_%s'% EB]=(data['TN_role_%s'% BI]+data['TN_role_%s'% BBJ])
data['TN_role_%s'% EC]=(data['TN_role_%s'% BG]+data['TN_role_%s'% BD]+data['TN_role_%s'% BC]+data['TN_role_%s'% BF]+data['TN_role_%s'% BI]+data['TN_role_%s'% BBJ])
data['TN_role_%s'% ED]=(data['TN_role_%s'% BB]+data['TN_role_%s'% BH]+data['TN_role_%s'% BL])
data['TN_role_%s'% EE]=(data['TN_role_%s'% BA]+data['TN_role_%s'% BI]+data['TN_role_%s'% BBI]+data['TN_role_%s'% BBJ])
data['TN_role_%s'% EF]=(data['TN_role_%s'% BM]+data['TN_role_%s'% BN]+data['TN_role_%s'% BO]+data['TN_role_%s'% BP]+data['TN_role_%s'% BQ]+data['TN_role_%s'% BU]+data['TN_role_%s'% BS]+data['TN_role_%s'% BR])
data['TN_role_%s'% EG]=(data['TN_role_%s'% BE]+data['TN_role_%s'% BF])

data['BN_role_%s'% EA]=(data['BN_role_%s'% BG]+data['BN_role_%s'% BD]+data['BN_role_%s'% BC])
data['BN_role_%s'% EB]=(data['BN_role_%s'% BI]+data['BN_role_%s'% BBJ])
data['BN_role_%s'% EC]=(data['BN_role_%s'% BG]+data['BN_role_%s'% BD]+data['BN_role_%s'% BC]+data['BN_role_%s'% BF]+data['BN_role_%s'% BI]+data['BN_role_%s'% BBJ])
data['BN_role_%s'% ED]=(data['BN_role_%s'% BB]+data['BN_role_%s'% BH]+data['BN_role_%s'% BL])
data['BN_role_%s'% EE]=(data['BN_role_%s'% BA]+data['BN_role_%s'% BI]+data['BN_role_%s'% BBI]+data['BN_role_%s'% BBJ])
data['BN_role_%s'% EF]=(data['BN_role_%s'% BM]+data['BN_role_%s'% BN]+data['BN_role_%s'% BO]+data['BN_role_%s'% BP]+data['BN_role_%s'% BQ]+data['BN_role_%s'% BU]+data['BN_role_%s'% BS]+data['BN_role_%s'% BR])
data['BN_role_%s'% EG]=(data['BN_role_%s'% BE]+data['BN_role_%s'% BF])

data['ON_role_%s'% EA]=(data['ON_role_%s'% BG]+data['ON_role_%s'% BD]+data['ON_role_%s'% BC])
data['ON_role_%s'% EB]=(data['ON_role_%s'% BI]+data['ON_role_%s'% BBJ])
data['ON_role_%s'% EC]=(data['ON_role_%s'% BG]+data['ON_role_%s'% BD]+data['ON_role_%s'% BC]+data['ON_role_%s'% BF]+data['ON_role_%s'% BI]+data['ON_role_%s'% BBJ])
data['ON_role_%s'% ED]=(data['ON_role_%s'% BB]+data['ON_role_%s'% BH]+data['ON_role_%s'% BL])
data['ON_role_%s'% EE]=(data['ON_role_%s'% BA]+data['ON_role_%s'% BI]+data['ON_role_%s'% BBI]+data['ON_role_%s'% BBJ])
data['ON_role_%s'% EF]=(data['ON_role_%s'% BM]+data['ON_role_%s'% BN]+data['ON_role_%s'% BO]+data['ON_role_%s'% BP]+data['ON_role_%s'% BQ]+data['ON_role_%s'% BU]+data['ON_role_%s'% BS]+data['ON_role_%s'% BR])
data['ON_role_%s'% EG]=(data['ON_role_%s'% BE]+data['ON_role_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_role_num'], np.NaN)
    data['TNFF_role_%s'% col_name]= np.where(data['TNFF_role_%s'% col_name]==1,data['obs_beh_treat_role_num_back'], np.NaN)
    data['TNFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFF_role_%s'% col_name]=np.where(data['TNFF_role_%s'% col_name]==99999, np.NaN, data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFF_role_%s'% col_name]==88888), 
        0,data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name]=np.where(data['TNFF_role_%s'% col_name]==88888, np.NaN, data['TNFF_role_%s'% col_name])
    data['TNFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total environment
    data['TNCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_role_num'], np.NaN)
    data['TNCF_role_%s'% col_name]= np.where(data['TNCF_role_%s'% col_name]==1,data['obs_beh_treat_role_num_back'], np.NaN)
    data['TNCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCF_role_%s'% col_name]=np.where(data['TNCF_role_%s'% col_name]==99999, np.NaN, data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCF_role_%s'% col_name]==88888), 
        0,data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name]=np.where(data['TNCF_role_%s'% col_name]==88888, np.NaN, data['TNCF_role_%s'% col_name])
    data['TNCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total environment
    data['TNFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_role_num'], np.NaN)
    data['TNFM_role_%s'% col_name]= np.where(data['TNFM_role_%s'% col_name]==1,data['obs_beh_treat_role_num_back'], np.NaN)
    data['TNFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFM_role_%s'% col_name]=np.where(data['TNFM_role_%s'% col_name]==99999, np.NaN, data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFM_role_%s'% col_name]==88888), 
        0,data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name]=np.where(data['TNFM_role_%s'% col_name]==88888, np.NaN, data['TNFM_role_%s'% col_name])
    data['TNFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total environment
    data['TNCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_role_num'], np.NaN)
    data['TNCM_role_%s'% col_name]= np.where(data['TNCM_role_%s'% col_name]==1,data['obs_beh_treat_role_num_back'], np.NaN)
    data['TNCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCM_role_%s'% col_name]=np.where(data['TNCM_role_%s'% col_name]==99999, np.NaN, data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCM_role_%s'% col_name]==88888), 
        0,data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name]=np.where(data['TNCM_role_%s'% col_name]==88888, np.NaN, data['TNCM_role_%s'% col_name])
    data['TNCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TNW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TNW_role_%s'% col_name]= np.where(data['TNW_role_%s'% col_name]==1,data['obs_beh_modwinner_role_num_back'], np.NaN)
    data['TNW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNW_role_%s'% col_name]=np.where(data['TNW_role_%s'% col_name]==99999, np.NaN, data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNW_role_%s'% col_name]==88888), 
        0,data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name]=np.where(data['TNW_role_%s'% col_name]==88888, np.NaN, data['TNW_role_%s'% col_name])
    data['TNW_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TNL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TNL_role_%s'% col_name]= np.where(data['TNL_role_%s'% col_name]==1,data['obs_beh_modwinner_role_num_back'], np.NaN)
    data['TNL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNL_role_%s'% col_name]=np.where(data['TNL_role_%s'% col_name]==99999, np.NaN, data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNL_role_%s'% col_name]==88888), 
        0,data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name]=np.where(data['TNL_role_%s'% col_name]==88888, np.NaN, data['TNL_role_%s'% col_name])
    data['TNL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TNO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Others')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TNO_role_%s'% col_name]= np.where(data['TNO_role_%s'% col_name]==1,data['obs_beh_modwinner_role_num_back'], np.NaN)
    data['TNO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNO_role_%s'% col_name]=np.where(data['TNO_role_%s'% col_name]==99999, np.NaN, data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNO_role_%s'% col_name]==88888), 
        0,data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name]=np.where(data['TNO_role_%s'% col_name]==88888, np.NaN, data['TNO_role_%s'% col_name])
    data['TNO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BNFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BNFF_role_%s'% col_name]= np.where(data['BNFF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_role_%s'% col_name]=np.where(data['BNFF_role_%s'% col_name]==99999, np.NaN, data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFF_role_%s'% col_name]==88888), 
        0,data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name]=np.where(data['BNFF_role_%s'% col_name]==88888, np.NaN, data['BNFF_role_%s'% col_name])
    data['BNFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_role_%s'% col_name]=np.where(data['BNFF_role_%s'% col_name]==np.NaN,0, data['BNFF_role_%s'% col_name])

    data['BNCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BNCF_role_%s'% col_name]= np.where(data['BNCF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_role_%s'% col_name]=np.where(data['BNCF_role_%s'% col_name]==99999, np.NaN, data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCF_role_%s'% col_name]==88888), 
        0,data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name]=np.where(data['BNCF_role_%s'% col_name]==88888, np.NaN, data['BNCF_role_%s'% col_name])
    data['BNCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_role_%s'% col_name]=np.where(data['BNCF_role_%s'% col_name]== np.NaN,0, data['BNCF_role_%s'% col_name])

    data['BNFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BNFM_role_%s'% col_name]= np.where(data['BNFM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_role_%s'% col_name]=np.where(data['BNFM_role_%s'% col_name]==99999, np.NaN, data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFM_role_%s'% col_name]==88888), 
        0,data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name]=np.where(data['BNFM_role_%s'% col_name]==88888, np.NaN, data['BNFM_role_%s'% col_name])
    data['BNFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_role_%s'% col_name]=np.where(data['BNFM_role_%s'% col_name]==np.NaN,0, data['BNFM_role_%s'% col_name])
 
    data['BNCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BNCM_role_%s'% col_name]= np.where(data['BNCM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_role_%s'% col_name]=np.where(data['BNCM_role_%s'% col_name]==99999, np.NaN, data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCM_role_%s'% col_name]==88888), 
        0,data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name]=np.where(data['BNCM_role_%s'% col_name]==88888, np.NaN, data['BNCM_role_%s'% col_name])
    data['BNCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_role_%s'% col_name]=np.where(data['BNCM_role_%s'% col_name]== np.NaN,0, data['BNCM_role_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ONFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ONFF_role_%s'% col_name]= np.where(data['ONFF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_role_%s'% col_name]=np.where(data['ONFF_role_%s'% col_name]==99999, np.NaN, data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFF_role_%s'% col_name]==88888), 
        0,data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name]=np.where(data['ONFF_role_%s'% col_name]==88888, np.NaN, data['ONFF_role_%s'% col_name])
    data['ONFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_role_%s'% col_name]=np.where(data['ONFF_role_%s'% col_name]== np.NaN,0, data['ONFF_role_%s'% col_name])

    data['ONCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ONCF_role_%s'% col_name]= np.where(data['ONCF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_role_%s'% col_name]=np.where(data['ONCF_role_%s'% col_name]==99999, np.NaN, data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCF_role_%s'% col_name]==88888), 
        0,data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name]=np.where(data['ONCF_role_%s'% col_name]==88888, np.NaN, data['ONCF_role_%s'% col_name])
    data['ONCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_role_%s'% col_name]=np.where(data['ONCF_role_%s'% col_name]== np.NaN,0, data['ONCF_role_%s'% col_name])
    
    data['ONFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ONFM_role_%s'% col_name]= np.where(data['ONFM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_role_%s'% col_name]=np.where(data['ONFM_role_%s'% col_name]==99999, np.NaN, data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFM_role_%s'% col_name]==88888), 
        0,data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name]=np.where(data['ONFM_role_%s'% col_name]==88888, np.NaN, data['ONFM_role_%s'% col_name])
    data['ONFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_role_%s'% col_name]=np.where(data['ONFM_role_%s'% col_name]== np.NaN,0, data['ONFM_role_%s'% col_name])

    data['ONCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ONCM_role_%s'% col_name]= np.where(data['ONCM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_num_back'], np.NaN)
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_role_%s'% col_name]=np.where(data['ONCM_role_%s'% col_name]==99999, np.NaN, data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCM_role_%s'% col_name]==88888), 
        0,data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name]=np.where(data['ONCM_role_%s'% col_name]==88888, np.NaN, data['ONCM_role_%s'% col_name])
    data['ONCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_role_%s'% col_name]=np.where(data['ONCM_role_%s'% col_name]== np.NaN,0, data['ONCM_role_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BNW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BNW_role_%s'% col_name]= np.where(data['BNW_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_role_%s'% col_name]=np.where(data['BNW_role_%s'% col_name]==99999, np.NaN, data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNW_role_%s'% col_name]==88888), 
        0,data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name]=np.where(data['BNW_role_%s'% col_name]==88888, np.NaN, data['BNW_role_%s'% col_name])
    data['BNW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_role_%s'% col_name]=np.where(data['BNW_role_%s'% col_name]== np.NaN,0, data['BNW_role_%s'% col_name])

    data['BNL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BNL_role_%s'% col_name]= np.where(data['BNL_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_role_%s'% col_name]=np.where(data['BNL_role_%s'% col_name]==99999, np.NaN, data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNL_role_%s'% col_name]==88888), 
        0,data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name]=np.where(data['BNL_role_%s'% col_name]==88888, np.NaN, data['BNL_role_%s'% col_name])
    data['BNL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_role_%s'% col_name]=np.where(data['BNL_role_%s'% col_name]== np.NaN,0, data['BNL_role_%s'% col_name])

    data['BNO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BNO_role_%s'% col_name]= np.where(data['BNO_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_role_%s'% col_name]=np.where(data['BNO_role_%s'% col_name]==99999, np.NaN, data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNO_role_%s'% col_name]==88888), 
        0,data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name]=np.where(data['BNO_role_%s'% col_name]==88888, np.NaN, data['BNO_role_%s'% col_name])
    data['BNO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_role_%s'% col_name]=np.where(data['BNO_role_%s'% col_name]== np.NaN,0, data['BNO_role_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ONW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ONW_role_%s'% col_name]= np.where(data['ONW_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_role_%s'% col_name]=np.where(data['ONW_role_%s'% col_name]==99999, np.NaN, data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONW_role_%s'% col_name]==88888), 
        0,data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name]=np.where(data['ONW_role_%s'% col_name]==88888, np.NaN, data['ONW_role_%s'% col_name])
    data['ONW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_role_%s'% col_name]=np.where(data['ONW_role_%s'% col_name]== np.NaN,0, data['ONW_role_%s'% col_name])

    data['ONL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ONL_role_%s'% col_name]= np.where(data['ONL_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_role_%s'% col_name]=np.where(data['ONL_role_%s'% col_name]==99999, np.NaN, data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONL_role_%s'% col_name]==88888), 
        0,data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name]=np.where(data['ONL_role_%s'% col_name]==88888, np.NaN, data['ONL_role_%s'% col_name])
    data['ONL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_role_%s'% col_name]=np.where(data['ONL_role_%s'% col_name]== np.NaN,0, data['ONL_role_%s'% col_name])

    data['ONO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ONO_role_%s'% col_name]= np.where(data['ONO_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_num_back'], np.NaN)
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_role_%s'% col_name]=np.where(data['ONO_role_%s'% col_name]==99999, np.NaN, data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONO_role_%s'% col_name]==88888), 
        0,data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name]=np.where(data['ONO_role_%s'% col_name]==88888, np.NaN, data['ONO_role_%s'% col_name])
    data['ONO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_role_%s'% col_name]=np.where(data['ONO_role_%s'% col_name]== np.NaN,0, data['ONO_role_%s'% col_name])


# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TNFF_role_%s'% EA]=(data['TNFF_role_%s'% BG]+data['TNFF_role_%s'% BD]+data['TNFF_role_%s'% BC])
data['TNFF_role_%s'% EB]=(data['TNFF_role_%s'% BI]+data['TNFF_role_%s'% BBJ])
data['TNFF_role_%s'% EC]=(data['TNFF_role_%s'% BG]+data['TNFF_role_%s'% BD]+data['TNFF_role_%s'% BC]+data['TNFF_role_%s'% BF]+data['TNFF_role_%s'% BI]+data['TNFF_role_%s'% BBJ])
data['TNFF_role_%s'% EF]=(data['TNFF_role_%s'% BM]+data['TNFF_role_%s'% BN]+data['TNFF_role_%s'% BO]+data['TNFF_role_%s'% BP]+data['TNFF_role_%s'% BQ]+data['TNFF_role_%s'% BU]+data['TNFF_role_%s'% BS]+data['TNFF_role_%s'% BR])

data['BNFF_role_%s'% EA]=(data['BNFF_role_%s'% BG]+data['BNFF_role_%s'% BD]+data['BNFF_role_%s'% BC])
data['BNFF_role_%s'% EB]=(data['BNFF_role_%s'% BI]+data['BNFF_role_%s'% BBJ])
data['BNFF_role_%s'% EC]=(data['BNFF_role_%s'% BG]+data['BNFF_role_%s'% BD]+data['BNFF_role_%s'% BC]+data['BNFF_role_%s'% BF]+data['BNFF_role_%s'% BI]+data['BNFF_role_%s'% BBJ])
data['BNFF_role_%s'% EF]=(data['BNFF_role_%s'% BM]+data['BNFF_role_%s'% BN]+data['BNFF_role_%s'% BO]+data['BNFF_role_%s'% BP]+data['BNFF_role_%s'% BQ]+data['BNFF_role_%s'% BU]+data['BNFF_role_%s'% BS]+data['BNFF_role_%s'% BR])

data['ONFF_role_%s'% EA]=(data['ONFF_role_%s'% BG]+data['ONFF_role_%s'% BD]+data['ONFF_role_%s'% BC])
data['ONFF_role_%s'% EB]=(data['ONFF_role_%s'% BI]+data['ONFF_role_%s'% BBJ])
data['ONFF_role_%s'% EC]=(data['ONFF_role_%s'% BG]+data['ONFF_role_%s'% BD]+data['ONFF_role_%s'% BC]+data['ONFF_role_%s'% BF]+data['ONFF_role_%s'% BI]+data['ONFF_role_%s'% BBJ])
data['ONFF_role_%s'% EF]=(data['ONFF_role_%s'% BM]+data['ONFF_role_%s'% BN]+data['ONFF_role_%s'% BO]+data['ONFF_role_%s'% BP]+data['ONFF_role_%s'% BQ]+data['ONFF_role_%s'% BU]+data['ONFF_role_%s'% BS]+data['ONFF_role_%s'% BR])

data['TNCF_role_%s'% EA]=(data['TNCF_role_%s'% BG]+data['TNCF_role_%s'% BD]+data['TNCF_role_%s'% BC])
data['TNCF_role_%s'% EB]=(data['TNCF_role_%s'% BI]+data['TNCF_role_%s'% BBJ])
data['TNCF_role_%s'% EC]=(data['TNCF_role_%s'% BG]+data['TNCF_role_%s'% BD]+data['TNCF_role_%s'% BC]+data['TNCF_role_%s'% BF]+data['TNCF_role_%s'% BI]+data['TNCF_role_%s'% BBJ])
data['TNCF_role_%s'% EF]=(data['TNCF_role_%s'% BM]+data['TNCF_role_%s'% BN]+data['TNCF_role_%s'% BO]+data['TNCF_role_%s'% BP]+data['TNCF_role_%s'% BQ]+data['TNCF_role_%s'% BU]+data['TNCF_role_%s'% BS]+data['TNCF_role_%s'% BR])

data['BNCF_role_%s'% EA]=(data['BNCF_role_%s'% BG]+data['BNCF_role_%s'% BD]+data['BNCF_role_%s'% BC])
data['BNCF_role_%s'% EB]=(data['BNCF_role_%s'% BI]+data['BNCF_role_%s'% BBJ])
data['BNCF_role_%s'% EC]=(data['BNCF_role_%s'% BG]+data['BNCF_role_%s'% BD]+data['BNCF_role_%s'% BC]+data['BNCF_role_%s'% BF]+data['BNCF_role_%s'% BI]+data['BNCF_role_%s'% BBJ])
data['BNCF_role_%s'% EF]=(data['BNCF_role_%s'% BM]+data['BNCF_role_%s'% BN]+data['BNCF_role_%s'% BO]+data['BNCF_role_%s'% BP]+data['BNCF_role_%s'% BQ]+data['BNCF_role_%s'% BU]+data['BNCF_role_%s'% BS]+data['BNCF_role_%s'% BR])

data['ONCF_role_%s'% EA]=(data['ONCF_role_%s'% BG]+data['ONCF_role_%s'% BD]+data['ONCF_role_%s'% BC])
data['ONCF_role_%s'% EB]=(data['ONCF_role_%s'% BI]+data['ONCF_role_%s'% BBJ])
data['ONCF_role_%s'% EC]=(data['ONCF_role_%s'% BG]+data['ONCF_role_%s'% BD]+data['ONCF_role_%s'% BC]+data['ONCF_role_%s'% BF]+data['ONCF_role_%s'% BI]+data['ONCF_role_%s'% BBJ])
data['ONCF_role_%s'% EF]=(data['ONCF_role_%s'% BM]+data['ONCF_role_%s'% BN]+data['ONCF_role_%s'% BO]+data['ONCF_role_%s'% BP]+data['ONCF_role_%s'% BQ]+data['ONCF_role_%s'% BU]+data['ONCF_role_%s'% BS]+data['ONCF_role_%s'% BR])

data['TNFM_role_%s'% EA]=(data['TNFM_role_%s'% BG]+data['TNFM_role_%s'% BD]+data['TNFM_role_%s'% BC])
data['TNFM_role_%s'% EB]=(data['TNFM_role_%s'% BI]+data['TNFM_role_%s'% BBJ])
data['TNFM_role_%s'% EC]=(data['TNFM_role_%s'% BG]+data['TNFM_role_%s'% BD]+data['TNFM_role_%s'% BC]+data['TNFM_role_%s'% BF]+data['TNFM_role_%s'% BI]+data['TNFM_role_%s'% BBJ])
data['TNFM_role_%s'% EF]=(data['TNFM_role_%s'% BM]+data['TNFM_role_%s'% BN]+data['TNFM_role_%s'% BO]+data['TNFM_role_%s'% BP]+data['TNFM_role_%s'% BQ]+data['TNFM_role_%s'% BU]+data['TNFM_role_%s'% BS]+data['TNFM_role_%s'% BR])

data['BNFM_role_%s'% EA]=(data['BNFM_role_%s'% BG]+data['BNFM_role_%s'% BD]+data['BNFM_role_%s'% BC])
data['BNFM_role_%s'% EB]=(data['BNFM_role_%s'% BI]+data['BNFM_role_%s'% BBJ])
data['BNFM_role_%s'% EC]=(data['BNFM_role_%s'% BG]+data['BNFM_role_%s'% BD]+data['BNFM_role_%s'% BC]+data['BNFM_role_%s'% BF]+data['BNFM_role_%s'% BI]+data['BNFM_role_%s'% BBJ])
data['BNFM_role_%s'% EF]=(data['BNFM_role_%s'% BM]+data['BNFM_role_%s'% BN]+data['BNFM_role_%s'% BO]+data['BNFM_role_%s'% BP]+data['BNFM_role_%s'% BQ]+data['BNFM_role_%s'% BU]+data['BNFM_role_%s'% BS]+data['BNFM_role_%s'% BR])

data['ONFM_role_%s'% EA]=(data['ONFM_role_%s'% BG]+data['ONFM_role_%s'% BD]+data['ONFM_role_%s'% BC])
data['ONFM_role_%s'% EB]=(data['ONFM_role_%s'% BI]+data['ONFM_role_%s'% BBJ])
data['ONFM_role_%s'% EC]=(data['ONFM_role_%s'% BG]+data['ONFM_role_%s'% BD]+data['ONFM_role_%s'% BC]+data['ONFM_role_%s'% BF]+data['ONFM_role_%s'% BI]+data['ONFM_role_%s'% BBJ])
data['ONFM_role_%s'% EF]=(data['ONFM_role_%s'% BM]+data['ONFM_role_%s'% BN]+data['ONFM_role_%s'% BO]+data['ONFM_role_%s'% BP]+data['ONFM_role_%s'% BQ]+data['ONFM_role_%s'% BU]+data['ONFM_role_%s'% BS]+data['ONFM_role_%s'% BR])

data['TNCM_role_%s'% EA]=(data['TNCM_role_%s'% BG]+data['TNCM_role_%s'% BD]+data['TNCM_role_%s'% BC])
data['TNCM_role_%s'% EB]=(data['TNCM_role_%s'% BI]+data['TNCM_role_%s'% BBJ])
data['TNCM_role_%s'% EC]=(data['TNCM_role_%s'% BG]+data['TNCM_role_%s'% BD]+data['TNCM_role_%s'% BC]+data['TNCM_role_%s'% BF]+data['TNCM_role_%s'% BI]+data['TNCM_role_%s'% BBJ])
data['TNCM_role_%s'% EF]=(data['TNCM_role_%s'% BM]+data['TNCM_role_%s'% BN]+data['TNCM_role_%s'% BO]+data['TNCM_role_%s'% BP]+data['TNCM_role_%s'% BQ]+data['TNCM_role_%s'% BU]+data['TNCM_role_%s'% BS]+data['TNCM_role_%s'% BR])

data['BNCM_role_%s'% EA]=(data['BNCM_role_%s'% BG]+data['BNCM_role_%s'% BD]+data['BNCM_role_%s'% BC])
data['BNCM_role_%s'% EB]=(data['BNCM_role_%s'% BI]+data['BNCM_role_%s'% BBJ])
data['BNCM_role_%s'% EC]=(data['BNCM_role_%s'% BG]+data['BNCM_role_%s'% BD]+data['BNCM_role_%s'% BC]+data['BNCM_role_%s'% BF]+data['BNCM_role_%s'% BI]+data['BNCM_role_%s'% BBJ])
data['BNCM_role_%s'% EF]=(data['BNCM_role_%s'% BM]+data['BNCM_role_%s'% BN]+data['BNCM_role_%s'% BO]+data['BNCM_role_%s'% BP]+data['BNCM_role_%s'% BQ]+data['BNCM_role_%s'% BU]+data['BNCM_role_%s'% BS]+data['BNCM_role_%s'% BR])

data['ONCM_role_%s'% EA]=(data['ONCM_role_%s'% BG]+data['ONCM_role_%s'% BD]+data['ONCM_role_%s'% BC])
data['ONCM_role_%s'% EB]=(data['ONCM_role_%s'% BI]+data['ONCM_role_%s'% BBJ])
data['ONCM_role_%s'% EC]=(data['ONCM_role_%s'% BG]+data['ONCM_role_%s'% BD]+data['ONCM_role_%s'% BC]+data['ONCM_role_%s'% BF]+data['ONCM_role_%s'% BI]+data['ONCM_role_%s'% BBJ])
data['ONCM_role_%s'% EF]=(data['ONCM_role_%s'% BM]+data['ONCM_role_%s'% BN]+data['ONCM_role_%s'% BO]+data['ONCM_role_%s'% BP]+data['ONCM_role_%s'% BQ]+data['ONCM_role_%s'% BU]+data['ONCM_role_%s'% BS]+data['ONCM_role_%s'% BR])

data['TNW_role_%s'% EA]=(data['TNW_role_%s'% BG]+data['TNW_role_%s'% BD]+data['TNW_role_%s'% BC])
data['TNW_role_%s'% EB]=(data['TNW_role_%s'% BI]+data['TNW_role_%s'% BBJ])
data['TNW_role_%s'% EC]=(data['TNW_role_%s'% BG]+data['TNW_role_%s'% BD]+data['TNW_role_%s'% BC]+data['TNW_role_%s'% BF]+data['TNW_role_%s'% BI]+data['TNW_role_%s'% BBJ])
data['TNW_role_%s'% EF]=(data['TNW_role_%s'% BM]+data['TNW_role_%s'% BN]+data['TNW_role_%s'% BO]+data['TNW_role_%s'% BP]+data['TNW_role_%s'% BQ]+data['TNW_role_%s'% BU]+data['TNW_role_%s'% BS]+data['TNW_role_%s'% BR])

data['BNW_role_%s'% EA]=(data['BNW_role_%s'% BG]+data['BNW_role_%s'% BD]+data['BNW_role_%s'% BC])
data['BNW_role_%s'% EB]=(data['BNW_role_%s'% BI]+data['BNW_role_%s'% BBJ])
data['BNW_role_%s'% EC]=(data['BNW_role_%s'% BG]+data['BNW_role_%s'% BD]+data['BNW_role_%s'% BC]+data['BNW_role_%s'% BF]+data['BNW_role_%s'% BI]+data['BNW_role_%s'% BBJ])
data['BNW_role_%s'% EF]=(data['BNW_role_%s'% BM]+data['BNW_role_%s'% BN]+data['BNW_role_%s'% BO]+data['BNW_role_%s'% BP]+data['BNW_role_%s'% BQ]+data['BNW_role_%s'% BU]+data['BNW_role_%s'% BS]+data['BNW_role_%s'% BR])

data['ONW_role_%s'% EA]=(data['ONW_role_%s'% BG]+data['ONW_role_%s'% BD]+data['ONW_role_%s'% BC])
data['ONW_role_%s'% EB]=(data['ONW_role_%s'% BI]+data['ONW_role_%s'% BBJ])
data['ONW_role_%s'% EC]=(data['ONW_role_%s'% BG]+data['ONW_role_%s'% BD]+data['ONW_role_%s'% BC]+data['ONW_role_%s'% BF]+data['ONW_role_%s'% BI]+data['ONW_role_%s'% BBJ])
data['ONW_role_%s'% EF]=(data['ONW_role_%s'% BM]+data['ONW_role_%s'% BN]+data['ONW_role_%s'% BO]+data['ONW_role_%s'% BP]+data['ONW_role_%s'% BQ]+data['ONW_role_%s'% BU]+data['ONW_role_%s'% BS]+data['ONW_role_%s'% BR])

data['TNL_role_%s'% EA]=(data['TNL_role_%s'% BG]+data['TNL_role_%s'% BD]+data['TNL_role_%s'% BC])
data['TNL_role_%s'% EB]=(data['TNL_role_%s'% BI]+data['TNL_role_%s'% BBJ])
data['TNL_role_%s'% EC]=(data['TNL_role_%s'% BG]+data['TNL_role_%s'% BD]+data['TNL_role_%s'% BC]+data['TNL_role_%s'% BF]+data['TNL_role_%s'% BI]+data['TNL_role_%s'% BBJ])
data['TNL_role_%s'% EF]=(data['TNL_role_%s'% BM]+data['TNL_role_%s'% BN]+data['TNL_role_%s'% BO]+data['TNL_role_%s'% BP]+data['TNL_role_%s'% BQ]+data['TNL_role_%s'% BU]+data['TNL_role_%s'% BS]+data['TNL_role_%s'% BR])

data['BNL_role_%s'% EA]=(data['BNL_role_%s'% BG]+data['BNL_role_%s'% BD]+data['BNL_role_%s'% BC])
data['BNL_role_%s'% EB]=(data['BNL_role_%s'% BI]+data['BNL_role_%s'% BBJ])
data['BNL_role_%s'% EC]=(data['BNL_role_%s'% BG]+data['BNL_role_%s'% BD]+data['BNL_role_%s'% BC]+data['BNL_role_%s'% BF]+data['BNL_role_%s'% BI]+data['BNL_role_%s'% BBJ])
data['BNL_role_%s'% EF]=(data['BNL_role_%s'% BM]+data['BNL_role_%s'% BN]+data['BNL_role_%s'% BO]+data['BNL_role_%s'% BP]+data['BNL_role_%s'% BQ]+data['BNL_role_%s'% BU]+data['BNL_role_%s'% BS]+data['BNL_role_%s'% BR])

data['ONL_role_%s'% EA]=(data['ONL_role_%s'% BG]+data['ONL_role_%s'% BD]+data['ONL_role_%s'% BC])
data['ONL_role_%s'% EB]=(data['ONL_role_%s'% BI]+data['ONL_role_%s'% BBJ])
data['ONL_role_%s'% EC]=(data['ONL_role_%s'% BG]+data['ONL_role_%s'% BD]+data['ONL_role_%s'% BC]+data['ONL_role_%s'% BF]+data['ONL_role_%s'% BI]+data['ONL_role_%s'% BBJ])
data['ONL_role_%s'% EF]=(data['ONL_role_%s'% BM]+data['ONL_role_%s'% BN]+data['ONL_role_%s'% BO]+data['ONL_role_%s'% BP]+data['ONL_role_%s'% BQ]+data['ONL_role_%s'% BU]+data['ONL_role_%s'% BS]+data['ONL_role_%s'% BR])

data['TNO_role_%s'% EA]=(data['TNO_role_%s'% BG]+data['TNO_role_%s'% BD]+data['TNO_role_%s'% BC])
data['TNO_role_%s'% EB]=(data['TNO_role_%s'% BI]+data['TNO_role_%s'% BBJ])
data['TNO_role_%s'% EC]=(data['TNO_role_%s'% BG]+data['TNO_role_%s'% BD]+data['TNO_role_%s'% BC]+data['TNO_role_%s'% BF]+data['TNO_role_%s'% BI]+data['TNO_role_%s'% BBJ])
data['TNO_role_%s'% EF]=(data['TNO_role_%s'% BM]+data['TNO_role_%s'% BN]+data['TNO_role_%s'% BO]+data['TNO_role_%s'% BP]+data['TNO_role_%s'% BQ]+data['TNO_role_%s'% BU]+data['TNO_role_%s'% BS]+data['TNO_role_%s'% BR])

data['BNO_role_%s'% EA]=(data['BNO_role_%s'% BG]+data['BNO_role_%s'% BD]+data['BNO_role_%s'% BC])
data['BNO_role_%s'% EB]=(data['BNO_role_%s'% BI]+data['BNO_role_%s'% BBJ])
data['BNO_role_%s'% EC]=(data['BNO_role_%s'% BG]+data['BNO_role_%s'% BD]+data['BNO_role_%s'% BC]+data['BNO_role_%s'% BF]+data['BNO_role_%s'% BI]+data['BNO_role_%s'% BBJ])
data['BNO_role_%s'% EF]=(data['BNO_role_%s'% BM]+data['BNO_role_%s'% BN]+data['BNO_role_%s'% BO]+data['BNO_role_%s'% BP]+data['BNO_role_%s'% BQ]+data['BNO_role_%s'% BU]+data['BNO_role_%s'% BS]+data['BNO_role_%s'% BR])

data['ONO_role_%s'% EA]=(data['ONO_role_%s'% BG]+data['ONO_role_%s'% BD]+data['ONO_role_%s'% BC])
data['ONO_role_%s'% EB]=(data['ONO_role_%s'% BI]+data['ONO_role_%s'% BBJ])
data['ONO_role_%s'% EC]=(data['ONO_role_%s'% BG]+data['ONO_role_%s'% BD]+data['ONO_role_%s'% BC]+data['ONO_role_%s'% BF]+data['ONO_role_%s'% BI]+data['ONO_role_%s'% BBJ])
data['ONO_role_%s'% EF]=(data['ONO_role_%s'% BM]+data['ONO_role_%s'% BN]+data['ONO_role_%s'% BO]+data['ONO_role_%s'% BP]+data['ONO_role_%s'% BQ]+data['ONO_role_%s'% BU]+data['ONO_role_%s'% BS]+data['ONO_role_%s'% BR])

  
# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNCR_role_%s'% col_name]=(data['TNCF_role_%s'% col_name]+data['TNCM_role_%s'% col_name])
    data['TNFR_role_%s'% col_name]=(data['TNFF_role_%s'% col_name]+data['TNFM_role_%s'% col_name])

data['TNCR_role_%s'% EA]=(data['TNCF_role_%s'% EA]+data['TNCM_role_%s'% EA])
data['TNFR_role_%s'% EA]=(data['TNFF_role_%s'% EA]+data['TNFM_role_%s'% EA])
data['TNCR_role_%s'% EB]=(data['TNCF_role_%s'% EB]+data['TNCM_role_%s'% EB])
data['TNFR_role_%s'% EB]=(data['TNFF_role_%s'% EB]+data['TNFM_role_%s'% EB])
data['TNCR_role_%s'% EC]=(data['TNCF_role_%s'% EC]+data['TNCM_role_%s'% EC])
data['TNFR_role_%s'% EC]=(data['TNFF_role_%s'% EC]+data['TNFM_role_%s'% EC])
data['TNCR_role_%s'% EF]=(data['TNCF_role_%s'% EF]+data['TNCM_role_%s'% EF])
data['TNFR_role_%s'% EF]=(data['TNFF_role_%s'% EF]+data['TNFM_role_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNM_role_%s'% col_name]=(data['TNCM_role_%s'% col_name]+data['TNFM_role_%s'% col_name])
    data['TNF_role_%s'% col_name]=(data['TNFF_role_%s'% col_name]+data['TNCF_role_%s'% col_name])

data['TNM_role_%s'% EA]=(data['TNCM_role_%s'% EA]+data['TNFM_role_%s'% EA])
data['TNF_role_%s'% EA]=(data['TNFF_role_%s'% EA]+data['TNCF_role_%s'% EA])
data['TNM_role_%s'% EB]=(data['TNCM_role_%s'% EB]+data['TNFM_role_%s'% EB])
data['TNF_role_%s'% EB]=(data['TNFF_role_%s'% EB]+data['TNCF_role_%s'% EB])
data['TNM_role_%s'% EC]=(data['TNCM_role_%s'% EC]+data['TNFM_role_%s'% EC])
data['TNF_role_%s'% EC]=(data['TNFF_role_%s'% EC]+data['TNCF_role_%s'% EC])
data['TNM_role_%s'% EF]=(data['TNCM_role_%s'% EF]+data['TNFM_role_%s'% EF])
data['TNF_role_%s'% EF]=(data['TNFF_role_%s'% EF]+data['TNCF_role_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BNCR_role_%s'% col_name]=(data['BNCF_role_%s'% col_name]+data['BNCM_role_%s'% col_name])
    data['BNFR_role_%s'% col_name]=(data['BNFF_role_%s'% col_name]+data['BNFM_role_%s'% col_name])

data['BNCR_role_%s'% EA]=(data['BNCF_role_%s'% EA]+data['BNCM_role_%s'% EA])
data['BNFR_role_%s'% EA]=(data['BNFF_role_%s'% EA]+data['BNFM_role_%s'% EA])
data['BNCR_role_%s'% EB]=(data['BNCF_role_%s'% EB]+data['BNCM_role_%s'% EB])
data['BNFR_role_%s'% EB]=(data['BNFF_role_%s'% EB]+data['BNFM_role_%s'% EB])
data['BNCR_role_%s'% EC]=(data['BNCF_role_%s'% EC]+data['BNCM_role_%s'% EC])
data['BNFR_role_%s'% EC]=(data['BNFF_role_%s'% EC]+data['BNFM_role_%s'% EC])
data['BNCR_role_%s'% EF]=(data['BNCF_role_%s'% EF]+data['BNCM_role_%s'% EF])
data['BNFR_role_%s'% EF]=(data['BNFF_role_%s'% EF]+data['BNFM_role_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BNM_role_%s'% col_name]=(data['BNCM_role_%s'% col_name]+data['BNFM_role_%s'% col_name])
    data['BNF_role_%s'% col_name]=(data['BNFF_role_%s'% col_name]+data['BNCF_role_%s'% col_name])

data['BNM_role_%s'% EA]=(data['BNCM_role_%s'% EA]+data['BNFM_role_%s'% EA])
data['BNF_role_%s'% EA]=(data['BNFF_role_%s'% EA]+data['BNCF_role_%s'% EA])
data['BNM_role_%s'% EB]=(data['BNCM_role_%s'% EB]+data['BNFM_role_%s'% EB])
data['BNF_role_%s'% EB]=(data['BNFF_role_%s'% EB]+data['BNCF_role_%s'% EB])
data['BNM_role_%s'% EC]=(data['BNCM_role_%s'% EC]+data['BNFM_role_%s'% EC])
data['BNF_role_%s'% EC]=(data['BNFF_role_%s'% EC]+data['BNCF_role_%s'% EC])
data['BNM_role_%s'% EF]=(data['BNCM_role_%s'% EF]+data['BNFM_role_%s'% EF])
data['BNF_role_%s'% EF]=(data['BNFF_role_%s'% EF]+data['BNCF_role_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONCR_role_%s'% col_name]=(data['ONCF_role_%s'% col_name]+data['ONCM_role_%s'% col_name])
    data['ONFR_role_%s'% col_name]=(data['ONFF_role_%s'% col_name]+data['ONFM_role_%s'% col_name])

data['ONCR_role_%s'% EA]=(data['ONCF_role_%s'% EA]+data['ONCM_role_%s'% EA])
data['ONFR_role_%s'% EA]=(data['ONFF_role_%s'% EA]+data['ONFM_role_%s'% EA])
data['ONCR_role_%s'% EB]=(data['ONCF_role_%s'% EB]+data['ONCM_role_%s'% EB])
data['ONFR_role_%s'% EB]=(data['ONFF_role_%s'% EB]+data['ONFM_role_%s'% EB])
data['ONCR_role_%s'% EC]=(data['ONCF_role_%s'% EC]+data['ONCM_role_%s'% EC])
data['ONFR_role_%s'% EC]=(data['ONFF_role_%s'% EC]+data['ONFM_role_%s'% EC])
data['ONCR_role_%s'% EF]=(data['ONCF_role_%s'% EF]+data['ONCM_role_%s'% EF])
data['ONFR_role_%s'% EF]=(data['ONFF_role_%s'% EF]+data['ONFM_role_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONM_role_%s'% col_name]=(data['ONCM_role_%s'% col_name]+data['ONFM_role_%s'% col_name])
    data['ONF_role_%s'% col_name]=(data['ONFF_role_%s'% col_name]+data['ONCF_role_%s'% col_name])

data['ONM_role_%s'% EA]=(data['ONCM_role_%s'% EA]+data['ONFM_role_%s'% EA])
data['ONF_role_%s'% EA]=(data['ONFF_role_%s'% EA]+data['ONCF_role_%s'% EA])
data['ONM_role_%s'% EB]=(data['ONCM_role_%s'% EB]+data['ONFM_role_%s'% EB])
data['ONF_role_%s'% EB]=(data['ONFF_role_%s'% EB]+data['ONCF_role_%s'% EB])
data['ONM_role_%s'% EC]=(data['ONCM_role_%s'% EC]+data['ONFM_role_%s'% EC])
data['ONF_role_%s'% EC]=(data['ONFF_role_%s'% EC]+data['ONCF_role_%s'% EC])
data['ONM_role_%s'% EF]=(data['ONCM_role_%s'% EF]+data['ONFM_role_%s'% EF])
data['ONF_role_%s'% EF]=(data['ONFF_role_%s'% EF]+data['ONCF_role_%s'% EF])

# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TD_role_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_role_num'], np.NaN)
        data['TD_role_%s'% col_name]= np.where(data['TD_role_%s'% col_name]==1,data['obs_beh_role_sumdur'], np.NaN)
        data['TD_role_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TD_role_%s'% col_name])
        data['TD_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TD_role_%s'% col_name])
        data['TD_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TD_role_%s'% col_name]=np.where(data['TD_role_%s'% col_name]==99999, np.NaN, data['TD_role_%s'% col_name])
        data['TD_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TD_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TD_role_%s'% col_name]==88888),
            0,data['TD_role_%s'% col_name])
        data['TD_role_%s'% col_name]=np.where(data['TD_role_%s'% col_name]==88888, np.NaN, data['TD_role_%s'% col_name])
        data['TD_role_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BD_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_role_num'], np.NaN)
        data['BD_role_%s'% col_name]= np.where(data['BD_role_%s'% col_name]==1,data['obs_beh_loc_role_sumdur'], np.NaN)
        data['BD_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BD_role_%s'% col_name]=np.where(data['BD_role_%s'% col_name]==99999, np.NaN, data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BD_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BD_role_%s'% col_name]==88888), 
            0,data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name]=np.where(data['BD_role_%s'% col_name]==88888, np.NaN, data['BD_role_%s'% col_name])
        data['BD_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['OD_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_role_num'], np.NaN)
        data['OD_role_%s'% col_name]= np.where(data['OD_role_%s'% col_name]==1,data['obs_beh_loc_role_sumdur'], np.NaN)
        data['OD_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['OD_role_%s'% col_name]=np.where(data['OD_role_%s'% col_name]==99999, np.NaN, data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['OD_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['OD_role_%s'% col_name]==88888), 
            0,data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name]=np.where(data['OD_role_%s'% col_name]==88888, np.NaN, data['OD_role_%s'% col_name])
        data['OD_role_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additiODal behaviors for total envirODment, burrow, and open field    
data['TD_role_%s'% EA]=(data['TD_role_%s'% BG]+data['TD_role_%s'% BD]+data['TD_role_%s'% BC])
data['TD_role_%s'% EB]=(data['TD_role_%s'% BI]+data['TD_role_%s'% BBJ])
data['TD_role_%s'% EC]=(data['TD_role_%s'% BG]+data['TD_role_%s'% BD]+data['TD_role_%s'% BC]+data['TD_role_%s'% BF]+data['TD_role_%s'% BI]+data['TD_role_%s'% BBJ])
data['TD_role_%s'% ED]=(data['TD_role_%s'% BB]+data['TD_role_%s'% BH]+data['TD_role_%s'% BL])
data['TD_role_%s'% EE]=(data['TD_role_%s'% BA]+data['TD_role_%s'% BI]+data['TD_role_%s'% BBI]+data['TD_role_%s'% BBJ])
data['TD_role_%s'% EF]=(data['TD_role_%s'% BM]+data['TD_role_%s'% BD]+data['TD_role_%s'% BO]+data['TD_role_%s'% BP]+data['TD_role_%s'% BQ]+data['TD_role_%s'% BU]+data['TD_role_%s'% BS]+data['TD_role_%s'% BR])
data['TD_role_%s'% EG]=(data['TD_role_%s'% BE]+data['TD_role_%s'% BF])

data['BD_role_%s'% EA]=(data['BD_role_%s'% BG]+data['BD_role_%s'% BD]+data['BD_role_%s'% BC])
data['BD_role_%s'% EB]=(data['BD_role_%s'% BI]+data['BD_role_%s'% BBJ])
data['BD_role_%s'% EC]=(data['BD_role_%s'% BG]+data['BD_role_%s'% BD]+data['BD_role_%s'% BC]+data['BD_role_%s'% BF]+data['BD_role_%s'% BI]+data['BD_role_%s'% BBJ])
data['BD_role_%s'% ED]=(data['BD_role_%s'% BB]+data['BD_role_%s'% BH]+data['BD_role_%s'% BL])
data['BD_role_%s'% EE]=(data['BD_role_%s'% BA]+data['BD_role_%s'% BI]+data['BD_role_%s'% BBI]+data['BD_role_%s'% BBJ])
data['BD_role_%s'% EF]=(data['BD_role_%s'% BM]+data['BD_role_%s'% BD]+data['BD_role_%s'% BO]+data['BD_role_%s'% BP]+data['BD_role_%s'% BQ]+data['BD_role_%s'% BU]+data['BD_role_%s'% BS]+data['BD_role_%s'% BR])
data['BD_role_%s'% EG]=(data['BD_role_%s'% BE]+data['BD_role_%s'% BF])

data['OD_role_%s'% EA]=(data['OD_role_%s'% BG]+data['OD_role_%s'% BD]+data['OD_role_%s'% BC])
data['OD_role_%s'% EB]=(data['OD_role_%s'% BI]+data['OD_role_%s'% BBJ])
data['OD_role_%s'% EC]=(data['OD_role_%s'% BG]+data['OD_role_%s'% BD]+data['OD_role_%s'% BC]+data['OD_role_%s'% BF]+data['OD_role_%s'% BI]+data['OD_role_%s'% BBJ])
data['OD_role_%s'% ED]=(data['OD_role_%s'% BB]+data['OD_role_%s'% BH]+data['OD_role_%s'% BL])
data['OD_role_%s'% EE]=(data['OD_role_%s'% BA]+data['OD_role_%s'% BI]+data['OD_role_%s'% BBI]+data['OD_role_%s'% BBJ])
data['OD_role_%s'% EF]=(data['OD_role_%s'% BM]+data['OD_role_%s'% BD]+data['OD_role_%s'% BO]+data['OD_role_%s'% BP]+data['OD_role_%s'% BQ]+data['OD_role_%s'% BU]+data['OD_role_%s'% BS]+data['OD_role_%s'% BR])
data['OD_role_%s'% EG]=(data['OD_role_%s'% BE]+data['OD_role_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_role_num'], np.NaN)
    data['TDFF_role_%s'% col_name]= np.where(data['TDFF_role_%s'% col_name]==1,data['obs_beh_treat_role_sumdur'], np.NaN)
    data['TDFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFF_role_%s'% col_name]=np.where(data['TDFF_role_%s'% col_name]==99999, np.NaN, data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFF_role_%s'% col_name]==88888), 
        0,data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name]=np.where(data['TDFF_role_%s'% col_name]==88888, np.NaN, data['TDFF_role_%s'% col_name])
    data['TDFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total envirODment
    data['TDCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_role_num'], np.NaN)
    data['TDCF_role_%s'% col_name]= np.where(data['TDCF_role_%s'% col_name]==1,data['obs_beh_treat_role_sumdur'], np.NaN)
    data['TDCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCF_role_%s'% col_name]=np.where(data['TDCF_role_%s'% col_name]==99999, np.NaN, data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCF_role_%s'% col_name]==88888), 
        0,data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name]=np.where(data['TDCF_role_%s'% col_name]==88888, np.NaN, data['TDCF_role_%s'% col_name])
    data['TDCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total envirODment
    data['TDFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_role_num'], np.NaN)
    data['TDFM_role_%s'% col_name]= np.where(data['TDFM_role_%s'% col_name]==1,data['obs_beh_treat_role_sumdur'], np.NaN)
    data['TDFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFM_role_%s'% col_name]=np.where(data['TDFM_role_%s'% col_name]==99999, np.NaN, data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFM_role_%s'% col_name]==88888), 
        0,data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name]=np.where(data['TDFM_role_%s'% col_name]==88888, np.NaN, data['TDFM_role_%s'% col_name])
    data['TDFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total envirODment
    data['TDCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_role_num'], np.NaN)
    data['TDCM_role_%s'% col_name]= np.where(data['TDCM_role_%s'% col_name]==1,data['obs_beh_treat_role_sumdur'], np.NaN)
    data['TDCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCM_role_%s'% col_name]=np.where(data['TDCM_role_%s'% col_name]==99999, np.NaN, data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCM_role_%s'% col_name]==88888), 
        0,data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name]=np.where(data['TDCM_role_%s'% col_name]==88888, np.NaN, data['TDCM_role_%s'% col_name])
    data['TDCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BDFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BDFF_role_%s'% col_name]= np.where(data['BDFF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_role_%s'% col_name]=np.where(data['BDFF_role_%s'% col_name]==99999, np.NaN, data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFF_role_%s'% col_name]==88888), 
        0,data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name]=np.where(data['BDFF_role_%s'% col_name]==88888, np.NaN, data['BDFF_role_%s'% col_name])
    data['BDFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_role_%s'% col_name]=np.where(data['BDFF_role_%s'% col_name]==np.NaN,0, data['BDFF_role_%s'% col_name])

    data['BDCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BDCF_role_%s'% col_name]= np.where(data['BDCF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_role_%s'% col_name]=np.where(data['BDCF_role_%s'% col_name]==99999, np.NaN, data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCF_role_%s'% col_name]==88888), 
        0,data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name]=np.where(data['BDCF_role_%s'% col_name]==88888, np.NaN, data['BDCF_role_%s'% col_name])
    data['BDCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_role_%s'% col_name]=np.where(data['BDCF_role_%s'% col_name]== np.NaN,0, data['BDCF_role_%s'% col_name])

    data['BDFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BDFM_role_%s'% col_name]= np.where(data['BDFM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_role_%s'% col_name]=np.where(data['BDFM_role_%s'% col_name]==99999, np.NaN, data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFM_role_%s'% col_name]==88888), 
        0,data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name]=np.where(data['BDFM_role_%s'% col_name]==88888, np.NaN, data['BDFM_role_%s'% col_name])
    data['BDFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_role_%s'% col_name]=np.where(data['BDFM_role_%s'% col_name]==np.NaN,0, data['BDFM_role_%s'% col_name])
 
    data['BDCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['BDCM_role_%s'% col_name]= np.where(data['BDCM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_role_%s'% col_name]=np.where(data['BDCM_role_%s'% col_name]==99999, np.NaN, data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCM_role_%s'% col_name]==88888), 
        0,data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name]=np.where(data['BDCM_role_%s'% col_name]==88888, np.NaN, data['BDCM_role_%s'% col_name])
    data['BDCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_role_%s'% col_name]=np.where(data['BDCM_role_%s'% col_name]== np.NaN,0, data['BDCM_role_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ODFF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ODFF_role_%s'% col_name]= np.where(data['ODFF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_role_%s'% col_name]=np.where(data['ODFF_role_%s'% col_name]==99999, np.NaN, data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFF_role_%s'% col_name]==88888), 
        0,data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name]=np.where(data['ODFF_role_%s'% col_name]==88888, np.NaN, data['ODFF_role_%s'% col_name])
    data['ODFF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_role_%s'% col_name]=np.where(data['ODFF_role_%s'% col_name]== np.NaN,0, data['ODFF_role_%s'% col_name])

    data['ODCF_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ODCF_role_%s'% col_name]= np.where(data['ODCF_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_role_%s'% col_name]=np.where(data['ODCF_role_%s'% col_name]==99999, np.NaN, data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCF_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCF_role_%s'% col_name]==88888), 
        0,data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name]=np.where(data['ODCF_role_%s'% col_name]==88888, np.NaN, data['ODCF_role_%s'% col_name])
    data['ODCF_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_role_%s'% col_name]=np.where(data['ODCF_role_%s'% col_name]== np.NaN,0, data['ODCF_role_%s'% col_name])
    
    data['ODFM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ODFM_role_%s'% col_name]= np.where(data['ODFM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_role_%s'% col_name]=np.where(data['ODFM_role_%s'% col_name]==99999, np.NaN, data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFM_role_%s'% col_name]==88888), 
        0,data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name]=np.where(data['ODFM_role_%s'% col_name]==88888, np.NaN, data['ODFM_role_%s'% col_name])
    data['ODFM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_role_%s'% col_name]=np.where(data['ODFM_role_%s'% col_name]== np.NaN,0, data['ODFM_role_%s'% col_name])

    data['ODCM_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_role_num'], np.NaN)
    data['ODCM_role_%s'% col_name]= np.where(data['ODCM_role_%s'% col_name]==1,data['obs_beh_loc_treat_role_sumdur'], np.NaN)
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_role_%s'% col_name]=np.where(data['ODCM_role_%s'% col_name]==99999, np.NaN, data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCM_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCM_role_%s'% col_name]==88888), 
        0,data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name]=np.where(data['ODCM_role_%s'% col_name]==88888, np.NaN, data['ODCM_role_%s'% col_name])
    data['ODCM_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_role_%s'% col_name]=np.where(data['ODCM_role_%s'% col_name]== np.NaN,0, data['ODCM_role_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TDW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TDW_role_%s'% col_name]= np.where(data['TDW_role_%s'% col_name]==1,data['obs_beh_modwinner_role_sumdur'], np.NaN)
    data['TDW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDW_role_%s'% col_name]=np.where(data['TDW_role_%s'% col_name]==99999, np.NaN, data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDW_role_%s'% col_name]==88888), 
        0,data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name]=np.where(data['TDW_role_%s'% col_name]==88888, np.NaN, data['TDW_role_%s'% col_name])
    data['TDW_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TDL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TDL_role_%s'% col_name]= np.where(data['TDL_role_%s'% col_name]==1,data['obs_beh_modwinner_role_sumdur'], np.NaN)
    data['TDL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDL_role_%s'% col_name]=np.where(data['TDL_role_%s'% col_name]==99999, np.NaN, data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDL_role_%s'% col_name]==88888), 
        0,data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name]=np.where(data['TDL_role_%s'% col_name]==88888, np.NaN, data['TDL_role_%s'% col_name])
    data['TDL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TDO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')),data['obs_beh_modwinner_role_num'], np.NaN)
    data['TDO_role_%s'% col_name]= np.where(data['TDO_role_%s'% col_name]==1,data['obs_beh_modwinner_role_sumdur'], np.NaN)
    data['TDO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDO_role_%s'% col_name]=np.where(data['TDO_role_%s'% col_name]==99999, np.NaN, data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDO_role_%s'% col_name]==88888), 
        0,data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name]=np.where(data['TDO_role_%s'% col_name]==88888, np.NaN, data['TDO_role_%s'% col_name])
    data['TDO_role_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BDW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BDW_role_%s'% col_name]= np.where(data['BDW_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_role_%s'% col_name]=np.where(data['BDW_role_%s'% col_name]==99999, np.NaN, data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDW_role_%s'% col_name]==88888), 
        0,data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name]=np.where(data['BDW_role_%s'% col_name]==88888, np.NaN, data['BDW_role_%s'% col_name])
    data['BDW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_role_%s'% col_name]=np.where(data['BDW_role_%s'% col_name]== np.NaN,0, data['BDW_role_%s'% col_name])

    data['BDL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BDL_role_%s'% col_name]= np.where(data['BDL_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_role_%s'% col_name]=np.where(data['BDL_role_%s'% col_name]==99999, np.NaN, data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDL_role_%s'% col_name]==88888), 
        0,data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name]=np.where(data['BDL_role_%s'% col_name]==88888, np.NaN, data['BDL_role_%s'% col_name])
    data['BDL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_role_%s'% col_name]=np.where(data['BDL_role_%s'% col_name]== np.NaN,0, data['BDL_role_%s'% col_name])

    data['BDO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['BDO_role_%s'% col_name]= np.where(data['BDO_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_role_%s'% col_name]=np.where(data['BDO_role_%s'% col_name]==99999, np.NaN, data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDO_role_%s'% col_name]==88888), 
        0,data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name]=np.where(data['BDO_role_%s'% col_name]==88888, np.NaN, data['BDO_role_%s'% col_name])
    data['BDO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_role_%s'% col_name]=np.where(data['BDO_role_%s'% col_name]== np.NaN,0, data['BDO_role_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ODW_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ODW_role_%s'% col_name]= np.where(data['ODW_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_role_%s'% col_name]=np.where(data['ODW_role_%s'% col_name]==99999, np.NaN, data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODW_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODW_role_%s'% col_name]==88888), 
        0,data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name]=np.where(data['ODW_role_%s'% col_name]==88888, np.NaN, data['ODW_role_%s'% col_name])
    data['ODW_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_role_%s'% col_name]=np.where(data['ODW_role_%s'% col_name]== np.NaN,0, data['ODW_role_%s'% col_name])

    data['ODL_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ODL_role_%s'% col_name]= np.where(data['ODL_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_role_%s'% col_name]=np.where(data['ODL_role_%s'% col_name]==99999, np.NaN, data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODL_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODL_role_%s'% col_name]==88888), 
        0,data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name]=np.where(data['ODL_role_%s'% col_name]==88888, np.NaN, data['ODL_role_%s'% col_name])
    data['ODL_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_role_%s'% col_name]=np.where(data['ODL_role_%s'% col_name]== np.NaN,0, data['ODL_role_%s'% col_name])

    data['ODO_role_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_role_num'], np.NaN)
    data['ODO_role_%s'% col_name]= np.where(data['ODO_role_%s'% col_name]==1,data['obs_beh_loc_modwinner_role_sumdur'], np.NaN)
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_role_%s'% col_name]=np.where(data['ODO_role_%s'% col_name]==99999, np.NaN, data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODO_role_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODO_role_%s'% col_name]==88888), 
        0,data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name]=np.where(data['ODO_role_%s'% col_name]==88888, np.NaN, data['ODO_role_%s'% col_name])
    data['ODO_role_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_role_%s'% col_name]=np.where(data['ODO_role_%s'% col_name]== np.NaN,0, data['ODO_role_%s'% col_name])

# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TDFF_role_%s'% EA]=(data['TDFF_role_%s'% BG]+data['TDFF_role_%s'% BD]+data['TDFF_role_%s'% BC])
data['TDFF_role_%s'% EB]=(data['TDFF_role_%s'% BI]+data['TDFF_role_%s'% BBJ])
data['TDFF_role_%s'% EC]=(data['TDFF_role_%s'% BG]+data['TDFF_role_%s'% BD]+data['TDFF_role_%s'% BC]+data['TDFF_role_%s'% BF]+data['TDFF_role_%s'% BI]+data['TDFF_role_%s'% BBJ])
data['TDFF_role_%s'% EF]=(data['TDFF_role_%s'% BM]+data['TDFF_role_%s'% BN]+data['TDFF_role_%s'% BO]+data['TDFF_role_%s'% BP]+data['TDFF_role_%s'% BQ]+data['TDFF_role_%s'% BU]+data['TDFF_role_%s'% BS]+data['TDFF_role_%s'% BR])

data['BDFF_role_%s'% EA]=(data['BDFF_role_%s'% BG]+data['BDFF_role_%s'% BD]+data['BDFF_role_%s'% BC])
data['BDFF_role_%s'% EB]=(data['BDFF_role_%s'% BI]+data['BDFF_role_%s'% BBJ])
data['BDFF_role_%s'% EC]=(data['BDFF_role_%s'% BG]+data['BDFF_role_%s'% BD]+data['BDFF_role_%s'% BC]+data['BDFF_role_%s'% BF]+data['BDFF_role_%s'% BI]+data['BDFF_role_%s'% BBJ])
data['BDFF_role_%s'% EF]=(data['BDFF_role_%s'% BM]+data['BDFF_role_%s'% BN]+data['BDFF_role_%s'% BO]+data['BDFF_role_%s'% BP]+data['BDFF_role_%s'% BQ]+data['BDFF_role_%s'% BU]+data['BDFF_role_%s'% BS]+data['BDFF_role_%s'% BR])

data['ODFF_role_%s'% EA]=(data['ODFF_role_%s'% BG]+data['ODFF_role_%s'% BD]+data['ODFF_role_%s'% BC])
data['ODFF_role_%s'% EB]=(data['ODFF_role_%s'% BI]+data['ODFF_role_%s'% BBJ])
data['ODFF_role_%s'% EC]=(data['ODFF_role_%s'% BG]+data['ODFF_role_%s'% BD]+data['ODFF_role_%s'% BC]+data['ODFF_role_%s'% BF]+data['ODFF_role_%s'% BI]+data['ODFF_role_%s'% BBJ])
data['ODFF_role_%s'% EF]=(data['ODFF_role_%s'% BM]+data['ODFF_role_%s'% BN]+data['ODFF_role_%s'% BO]+data['ODFF_role_%s'% BP]+data['ODFF_role_%s'% BQ]+data['ODFF_role_%s'% BU]+data['ODFF_role_%s'% BS]+data['ODFF_role_%s'% BR])

data['TDCF_role_%s'% EA]=(data['TDCF_role_%s'% BG]+data['TDCF_role_%s'% BD]+data['TDCF_role_%s'% BC])
data['TDCF_role_%s'% EB]=(data['TDCF_role_%s'% BI]+data['TDCF_role_%s'% BBJ])
data['TDCF_role_%s'% EC]=(data['TDCF_role_%s'% BG]+data['TDCF_role_%s'% BD]+data['TDCF_role_%s'% BC]+data['TDCF_role_%s'% BF]+data['TDCF_role_%s'% BI]+data['TDCF_role_%s'% BBJ])
data['TDCF_role_%s'% EF]=(data['TDCF_role_%s'% BM]+data['TDCF_role_%s'% BN]+data['TDCF_role_%s'% BO]+data['TDCF_role_%s'% BP]+data['TDCF_role_%s'% BQ]+data['TDCF_role_%s'% BU]+data['TDCF_role_%s'% BS]+data['TDCF_role_%s'% BR])

data['BDCF_role_%s'% EA]=(data['BDCF_role_%s'% BG]+data['BDCF_role_%s'% BD]+data['BDCF_role_%s'% BC])
data['BDCF_role_%s'% EB]=(data['BDCF_role_%s'% BI]+data['BDCF_role_%s'% BBJ])
data['BDCF_role_%s'% EC]=(data['BDCF_role_%s'% BG]+data['BDCF_role_%s'% BD]+data['BDCF_role_%s'% BC]+data['BDCF_role_%s'% BF]+data['BDCF_role_%s'% BI]+data['BDCF_role_%s'% BBJ])
data['BDCF_role_%s'% EF]=(data['BDCF_role_%s'% BM]+data['BDCF_role_%s'% BN]+data['BDCF_role_%s'% BO]+data['BDCF_role_%s'% BP]+data['BDCF_role_%s'% BQ]+data['BDCF_role_%s'% BU]+data['BDCF_role_%s'% BS]+data['BDCF_role_%s'% BR])

data['ODCF_role_%s'% EA]=(data['ODCF_role_%s'% BG]+data['ODCF_role_%s'% BD]+data['ODCF_role_%s'% BC])
data['ODCF_role_%s'% EB]=(data['ODCF_role_%s'% BI]+data['ODCF_role_%s'% BBJ])
data['ODCF_role_%s'% EC]=(data['ODCF_role_%s'% BG]+data['ODCF_role_%s'% BD]+data['ODCF_role_%s'% BC]+data['ODCF_role_%s'% BF]+data['ODCF_role_%s'% BI]+data['ODCF_role_%s'% BBJ])
data['ODCF_role_%s'% EF]=(data['ODCF_role_%s'% BM]+data['ODCF_role_%s'% BN]+data['ODCF_role_%s'% BO]+data['ODCF_role_%s'% BP]+data['ODCF_role_%s'% BQ]+data['ODCF_role_%s'% BU]+data['ODCF_role_%s'% BS]+data['ODCF_role_%s'% BR])

data['TDFM_role_%s'% EA]=(data['TDFM_role_%s'% BG]+data['TDFM_role_%s'% BD]+data['TDFM_role_%s'% BC])
data['TDFM_role_%s'% EB]=(data['TDFM_role_%s'% BI]+data['TDFM_role_%s'% BBJ])
data['TDFM_role_%s'% EC]=(data['TDFM_role_%s'% BG]+data['TDFM_role_%s'% BD]+data['TDFM_role_%s'% BC]+data['TDFM_role_%s'% BF]+data['TDFM_role_%s'% BI]+data['TDFM_role_%s'% BBJ])
data['TDFM_role_%s'% EF]=(data['TDFM_role_%s'% BM]+data['TDFM_role_%s'% BN]+data['TDFM_role_%s'% BO]+data['TDFM_role_%s'% BP]+data['TDFM_role_%s'% BQ]+data['TDFM_role_%s'% BU]+data['TDFM_role_%s'% BS]+data['TDFM_role_%s'% BR])

data['BDFM_role_%s'% EA]=(data['BDFM_role_%s'% BG]+data['BDFM_role_%s'% BD]+data['BDFM_role_%s'% BC])
data['BDFM_role_%s'% EB]=(data['BDFM_role_%s'% BI]+data['BDFM_role_%s'% BBJ])
data['BDFM_role_%s'% EC]=(data['BDFM_role_%s'% BG]+data['BDFM_role_%s'% BD]+data['BDFM_role_%s'% BC]+data['BDFM_role_%s'% BF]+data['BDFM_role_%s'% BI]+data['BDFM_role_%s'% BBJ])
data['BDFM_role_%s'% EF]=(data['BDFM_role_%s'% BM]+data['BDFM_role_%s'% BN]+data['BDFM_role_%s'% BO]+data['BDFM_role_%s'% BP]+data['BDFM_role_%s'% BQ]+data['BDFM_role_%s'% BU]+data['BDFM_role_%s'% BS]+data['BDFM_role_%s'% BR])

data['ODFM_role_%s'% EA]=(data['ODFM_role_%s'% BG]+data['ODFM_role_%s'% BD]+data['ODFM_role_%s'% BC])
data['ODFM_role_%s'% EB]=(data['ODFM_role_%s'% BI]+data['ODFM_role_%s'% BBJ])
data['ODFM_role_%s'% EC]=(data['ODFM_role_%s'% BG]+data['ODFM_role_%s'% BD]+data['ODFM_role_%s'% BC]+data['ODFM_role_%s'% BF]+data['ODFM_role_%s'% BI]+data['ODFM_role_%s'% BBJ])
data['ODFM_role_%s'% EF]=(data['ODFM_role_%s'% BM]+data['ODFM_role_%s'% BN]+data['ODFM_role_%s'% BO]+data['ODFM_role_%s'% BP]+data['ODFM_role_%s'% BQ]+data['ODFM_role_%s'% BU]+data['ODFM_role_%s'% BS]+data['ODFM_role_%s'% BR])

data['TDCM_role_%s'% EA]=(data['TDCM_role_%s'% BG]+data['TDCM_role_%s'% BD]+data['TDCM_role_%s'% BC])
data['TDCM_role_%s'% EB]=(data['TDCM_role_%s'% BI]+data['TDCM_role_%s'% BBJ])
data['TDCM_role_%s'% EC]=(data['TDCM_role_%s'% BG]+data['TDCM_role_%s'% BD]+data['TDCM_role_%s'% BC]+data['TDCM_role_%s'% BF]+data['TDCM_role_%s'% BI]+data['TDCM_role_%s'% BBJ])
data['TDCM_role_%s'% EF]=(data['TDCM_role_%s'% BM]+data['TDCM_role_%s'% BN]+data['TDCM_role_%s'% BO]+data['TDCM_role_%s'% BP]+data['TDCM_role_%s'% BQ]+data['TDCM_role_%s'% BU]+data['TDCM_role_%s'% BS]+data['TDCM_role_%s'% BR])

data['BDCM_role_%s'% EA]=(data['BDCM_role_%s'% BG]+data['BDCM_role_%s'% BD]+data['BDCM_role_%s'% BC])
data['BDCM_role_%s'% EB]=(data['BDCM_role_%s'% BI]+data['BDCM_role_%s'% BBJ])
data['BDCM_role_%s'% EC]=(data['BDCM_role_%s'% BG]+data['BDCM_role_%s'% BD]+data['BDCM_role_%s'% BC]+data['BDCM_role_%s'% BF]+data['BDCM_role_%s'% BI]+data['BDCM_role_%s'% BBJ])
data['BDCM_role_%s'% EF]=(data['BDCM_role_%s'% BM]+data['BDCM_role_%s'% BN]+data['BDCM_role_%s'% BO]+data['BDCM_role_%s'% BP]+data['BDCM_role_%s'% BQ]+data['BDCM_role_%s'% BU]+data['BDCM_role_%s'% BS]+data['BDCM_role_%s'% BR])

data['ODCM_role_%s'% EA]=(data['ODCM_role_%s'% BG]+data['ODCM_role_%s'% BD]+data['ODCM_role_%s'% BC])
data['ODCM_role_%s'% EB]=(data['ODCM_role_%s'% BI]+data['ODCM_role_%s'% BBJ])
data['ODCM_role_%s'% EC]=(data['ODCM_role_%s'% BG]+data['ODCM_role_%s'% BD]+data['ODCM_role_%s'% BC]+data['ODCM_role_%s'% BF]+data['ODCM_role_%s'% BI]+data['ODCM_role_%s'% BBJ])
data['ODCM_role_%s'% EF]=(data['ODCM_role_%s'% BM]+data['ODCM_role_%s'% BN]+data['ODCM_role_%s'% BO]+data['ODCM_role_%s'% BP]+data['ODCM_role_%s'% BQ]+data['ODCM_role_%s'% BU]+data['ODCM_role_%s'% BS]+data['ODCM_role_%s'% BR])
   
data['TDW_role_%s'% EA]=(data['TDW_role_%s'% BG]+data['TDW_role_%s'% BD]+data['TDW_role_%s'% BC])
data['TDW_role_%s'% EB]=(data['TDW_role_%s'% BI]+data['TDW_role_%s'% BBJ])
data['TDW_role_%s'% EC]=(data['TDW_role_%s'% BG]+data['TDW_role_%s'% BD]+data['TDW_role_%s'% BC]+data['TDW_role_%s'% BF]+data['TDW_role_%s'% BI]+data['TDW_role_%s'% BBJ])
data['TDW_role_%s'% EF]=(data['TDW_role_%s'% BM]+data['TDW_role_%s'% BN]+data['TDW_role_%s'% BO]+data['TDW_role_%s'% BP]+data['TDW_role_%s'% BQ]+data['TDW_role_%s'% BU]+data['TDW_role_%s'% BS]+data['TDW_role_%s'% BR])

data['BDW_role_%s'% EA]=(data['BDW_role_%s'% BG]+data['BDW_role_%s'% BD]+data['BDW_role_%s'% BC])
data['BDW_role_%s'% EB]=(data['BDW_role_%s'% BI]+data['BDW_role_%s'% BBJ])
data['BDW_role_%s'% EC]=(data['BDW_role_%s'% BG]+data['BDW_role_%s'% BD]+data['BDW_role_%s'% BC]+data['BDW_role_%s'% BF]+data['BDW_role_%s'% BI]+data['BDW_role_%s'% BBJ])
data['BDW_role_%s'% EF]=(data['BDW_role_%s'% BM]+data['BDW_role_%s'% BN]+data['BDW_role_%s'% BO]+data['BDW_role_%s'% BP]+data['BDW_role_%s'% BQ]+data['BDW_role_%s'% BU]+data['BDW_role_%s'% BS]+data['BDW_role_%s'% BR])

data['ODW_role_%s'% EA]=(data['ODW_role_%s'% BG]+data['ODW_role_%s'% BD]+data['ODW_role_%s'% BC])
data['ODW_role_%s'% EB]=(data['ODW_role_%s'% BI]+data['ODW_role_%s'% BBJ])
data['ODW_role_%s'% EC]=(data['ODW_role_%s'% BG]+data['ODW_role_%s'% BD]+data['ODW_role_%s'% BC]+data['ODW_role_%s'% BF]+data['ODW_role_%s'% BI]+data['ODW_role_%s'% BBJ])
data['ODW_role_%s'% EF]=(data['ODW_role_%s'% BM]+data['ODW_role_%s'% BN]+data['ODW_role_%s'% BO]+data['ODW_role_%s'% BP]+data['ODW_role_%s'% BQ]+data['ODW_role_%s'% BU]+data['ODW_role_%s'% BS]+data['ODW_role_%s'% BR])

data['TDL_role_%s'% EA]=(data['TDL_role_%s'% BG]+data['TDL_role_%s'% BD]+data['TDL_role_%s'% BC])
data['TDL_role_%s'% EB]=(data['TDL_role_%s'% BI]+data['TDL_role_%s'% BBJ])
data['TDL_role_%s'% EC]=(data['TDL_role_%s'% BG]+data['TDL_role_%s'% BD]+data['TDL_role_%s'% BC]+data['TDL_role_%s'% BF]+data['TDL_role_%s'% BI]+data['TDL_role_%s'% BBJ])
data['TDL_role_%s'% EF]=(data['TDL_role_%s'% BM]+data['TDL_role_%s'% BN]+data['TDL_role_%s'% BO]+data['TDL_role_%s'% BP]+data['TDL_role_%s'% BQ]+data['TDL_role_%s'% BU]+data['TDL_role_%s'% BS]+data['TDL_role_%s'% BR])

data['BDL_role_%s'% EA]=(data['BDL_role_%s'% BG]+data['BDL_role_%s'% BD]+data['BDL_role_%s'% BC])
data['BDL_role_%s'% EB]=(data['BDL_role_%s'% BI]+data['BDL_role_%s'% BBJ])
data['BDL_role_%s'% EC]=(data['BDL_role_%s'% BG]+data['BDL_role_%s'% BD]+data['BDL_role_%s'% BC]+data['BDL_role_%s'% BF]+data['BDL_role_%s'% BI]+data['BDL_role_%s'% BBJ])
data['BDL_role_%s'% EF]=(data['BDL_role_%s'% BM]+data['BDL_role_%s'% BN]+data['BDL_role_%s'% BO]+data['BDL_role_%s'% BP]+data['BDL_role_%s'% BQ]+data['BDL_role_%s'% BU]+data['BDL_role_%s'% BS]+data['BDL_role_%s'% BR])

data['ODL_role_%s'% EA]=(data['ODL_role_%s'% BG]+data['ODL_role_%s'% BD]+data['ODL_role_%s'% BC])
data['ODL_role_%s'% EB]=(data['ODL_role_%s'% BI]+data['ODL_role_%s'% BBJ])
data['ODL_role_%s'% EC]=(data['ODL_role_%s'% BG]+data['ODL_role_%s'% BD]+data['ODL_role_%s'% BC]+data['ODL_role_%s'% BF]+data['ODL_role_%s'% BI]+data['ODL_role_%s'% BBJ])
data['ODL_role_%s'% EF]=(data['ODL_role_%s'% BM]+data['ODL_role_%s'% BN]+data['ODL_role_%s'% BO]+data['ODL_role_%s'% BP]+data['ODL_role_%s'% BQ]+data['ODL_role_%s'% BU]+data['ODL_role_%s'% BS]+data['ODL_role_%s'% BR])

data['TDO_role_%s'% EA]=(data['TDO_role_%s'% BG]+data['TDO_role_%s'% BD]+data['TDO_role_%s'% BC])
data['TDO_role_%s'% EB]=(data['TDO_role_%s'% BI]+data['TDO_role_%s'% BBJ])
data['TDO_role_%s'% EC]=(data['TDO_role_%s'% BG]+data['TDO_role_%s'% BD]+data['TDO_role_%s'% BC]+data['TDO_role_%s'% BF]+data['TDO_role_%s'% BI]+data['TDO_role_%s'% BBJ])
data['TDO_role_%s'% EF]=(data['TDO_role_%s'% BM]+data['TDO_role_%s'% BN]+data['TDO_role_%s'% BO]+data['TDO_role_%s'% BP]+data['TDO_role_%s'% BQ]+data['TDO_role_%s'% BU]+data['TDO_role_%s'% BS]+data['TDO_role_%s'% BR])

data['BDO_role_%s'% EA]=(data['BDO_role_%s'% BG]+data['BDO_role_%s'% BD]+data['BDO_role_%s'% BC])
data['BDO_role_%s'% EB]=(data['BDO_role_%s'% BI]+data['BDO_role_%s'% BBJ])
data['BDO_role_%s'% EC]=(data['BDO_role_%s'% BG]+data['BDO_role_%s'% BD]+data['BDO_role_%s'% BC]+data['BDO_role_%s'% BF]+data['BDO_role_%s'% BI]+data['BDO_role_%s'% BBJ])
data['BDO_role_%s'% EF]=(data['BDO_role_%s'% BM]+data['BDO_role_%s'% BN]+data['BDO_role_%s'% BO]+data['BDO_role_%s'% BP]+data['BDO_role_%s'% BQ]+data['BDO_role_%s'% BU]+data['BDO_role_%s'% BS]+data['BDO_role_%s'% BR])

data['ODO_role_%s'% EA]=(data['ODO_role_%s'% BG]+data['ODO_role_%s'% BD]+data['ODO_role_%s'% BC])
data['ODO_role_%s'% EB]=(data['ODO_role_%s'% BI]+data['ODO_role_%s'% BBJ])
data['ODO_role_%s'% EC]=(data['ODO_role_%s'% BG]+data['ODO_role_%s'% BD]+data['ODO_role_%s'% BC]+data['ODO_role_%s'% BF]+data['ODO_role_%s'% BI]+data['ODO_role_%s'% BBJ])
data['ODO_role_%s'% EF]=(data['ODO_role_%s'% BM]+data['ODO_role_%s'% BN]+data['ODO_role_%s'% BO]+data['ODO_role_%s'% BP]+data['ODO_role_%s'% BQ]+data['ODO_role_%s'% BU]+data['ODO_role_%s'% BS]+data['ODO_role_%s'% BR])


# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TDCR_role_%s'% col_name]=(data['TDCF_role_%s'% col_name]+data['TDCM_role_%s'% col_name])
    data['TDFR_role_%s'% col_name]=(data['TDFF_role_%s'% col_name]+data['TDFM_role_%s'% col_name])

data['TDCR_role_%s'% EA]=(data['TDCF_role_%s'% EA]+data['TDCM_role_%s'% EA])
data['TDFR_role_%s'% EA]=(data['TDFF_role_%s'% EA]+data['TDFM_role_%s'% EA])
data['TDCR_role_%s'% EB]=(data['TDCF_role_%s'% EB]+data['TDCM_role_%s'% EB])
data['TDFR_role_%s'% EB]=(data['TDFF_role_%s'% EB]+data['TDFM_role_%s'% EB])
data['TDCR_role_%s'% EC]=(data['TDCF_role_%s'% EC]+data['TDCM_role_%s'% EC])
data['TDFR_role_%s'% EC]=(data['TDFF_role_%s'% EC]+data['TDFM_role_%s'% EC])
data['TDCR_role_%s'% EF]=(data['TDCF_role_%s'% EF]+data['TDCM_role_%s'% EF])
data['TDFR_role_%s'% EF]=(data['TDFF_role_%s'% EF]+data['TDFM_role_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDM_role_%s'% col_name]=(data['TDCM_role_%s'% col_name]+data['TDFM_role_%s'% col_name])
    data['TDF_role_%s'% col_name]=(data['TDFF_role_%s'% col_name]+data['TDCF_role_%s'% col_name])

data['TDM_role_%s'% EA]=(data['TDCM_role_%s'% EA]+data['TDFM_role_%s'% EA])
data['TDF_role_%s'% EA]=(data['TDFF_role_%s'% EA]+data['TDCF_role_%s'% EA])
data['TDM_role_%s'% EB]=(data['TDCM_role_%s'% EB]+data['TDFM_role_%s'% EB])
data['TDF_role_%s'% EB]=(data['TDFF_role_%s'% EB]+data['TDCF_role_%s'% EB])
data['TDM_role_%s'% EC]=(data['TDCM_role_%s'% EC]+data['TDFM_role_%s'% EC])
data['TDF_role_%s'% EC]=(data['TDFF_role_%s'% EC]+data['TDCF_role_%s'% EC])
data['TDM_role_%s'% EF]=(data['TDCM_role_%s'% EF]+data['TDFM_role_%s'% EF])
data['TDF_role_%s'% EF]=(data['TDFF_role_%s'% EF]+data['TDCF_role_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BDCR_role_%s'% col_name]=(data['BDCF_role_%s'% col_name]+data['BDCM_role_%s'% col_name])
    data['BDFR_role_%s'% col_name]=(data['BDFF_role_%s'% col_name]+data['BDFM_role_%s'% col_name])

data['BDCR_role_%s'% EA]=(data['BDCF_role_%s'% EA]+data['BDCM_role_%s'% EA])
data['BDFR_role_%s'% EA]=(data['BDFF_role_%s'% EA]+data['BDFM_role_%s'% EA])
data['BDCR_role_%s'% EB]=(data['BDCF_role_%s'% EB]+data['BDCM_role_%s'% EB])
data['BDFR_role_%s'% EB]=(data['BDFF_role_%s'% EB]+data['BDFM_role_%s'% EB])
data['BDCR_role_%s'% EC]=(data['BDCF_role_%s'% EC]+data['BDCM_role_%s'% EC])
data['BDFR_role_%s'% EC]=(data['BDFF_role_%s'% EC]+data['BDFM_role_%s'% EC])
data['BDCR_role_%s'% EF]=(data['BDCF_role_%s'% EF]+data['BDCM_role_%s'% EF])
data['BDFR_role_%s'% EF]=(data['BDFF_role_%s'% EF]+data['BDFM_role_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BDM_role_%s'% col_name]=(data['BDCM_role_%s'% col_name]+data['BDFM_role_%s'% col_name])
    data['BDF_role_%s'% col_name]=(data['BDFF_role_%s'% col_name]+data['BDCF_role_%s'% col_name])

data['BDM_role_%s'% EA]=(data['BDCM_role_%s'% EA]+data['BDFM_role_%s'% EA])
data['BDF_role_%s'% EA]=(data['BDFF_role_%s'% EA]+data['BDCF_role_%s'% EA])
data['BDM_role_%s'% EB]=(data['BDCM_role_%s'% EB]+data['BDFM_role_%s'% EB])
data['BDF_role_%s'% EB]=(data['BDFF_role_%s'% EB]+data['BDCF_role_%s'% EB])
data['BDM_role_%s'% EC]=(data['BDCM_role_%s'% EC]+data['BDFM_role_%s'% EC])
data['BDF_role_%s'% EC]=(data['BDFF_role_%s'% EC]+data['BDCF_role_%s'% EC])
data['BDM_role_%s'% EF]=(data['BDCM_role_%s'% EF]+data['BDFM_role_%s'% EF])
data['BDF_role_%s'% EF]=(data['BDFF_role_%s'% EF]+data['BDCF_role_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODCR_role_%s'% col_name]=(data['ODCF_role_%s'% col_name]+data['ODCM_role_%s'% col_name])
    data['ODFR_role_%s'% col_name]=(data['ODFF_role_%s'% col_name]+data['ODFM_role_%s'% col_name])

data['ODCR_role_%s'% EA]=(data['ODCF_role_%s'% EA]+data['ODCM_role_%s'% EA])
data['ODFR_role_%s'% EA]=(data['ODFF_role_%s'% EA]+data['ODFM_role_%s'% EA])
data['ODCR_role_%s'% EB]=(data['ODCF_role_%s'% EB]+data['ODCM_role_%s'% EB])
data['ODFR_role_%s'% EB]=(data['ODFF_role_%s'% EB]+data['ODFM_role_%s'% EB])
data['ODCR_role_%s'% EC]=(data['ODCF_role_%s'% EC]+data['ODCM_role_%s'% EC])
data['ODFR_role_%s'% EC]=(data['ODFF_role_%s'% EC]+data['ODFM_role_%s'% EC])
data['ODCR_role_%s'% EF]=(data['ODCF_role_%s'% EF]+data['ODCM_role_%s'% EF])
data['ODFR_role_%s'% EF]=(data['ODFF_role_%s'% EF]+data['ODFM_role_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODM_role_%s'% col_name]=(data['ODCM_role_%s'% col_name]+data['ODFM_role_%s'% col_name])
    data['ODF_role_%s'% col_name]=(data['ODFF_role_%s'% col_name]+data['ODCF_role_%s'% col_name])

data['ODM_role_%s'% EA]=(data['ODCM_role_%s'% EA]+data['ODFM_role_%s'% EA])
data['ODF_role_%s'% EA]=(data['ODFF_role_%s'% EA]+data['ODCF_role_%s'% EA])
data['ODM_role_%s'% EB]=(data['ODCM_role_%s'% EB]+data['ODFM_role_%s'% EB])
data['ODF_role_%s'% EB]=(data['ODFF_role_%s'% EB]+data['ODCF_role_%s'% EB])
data['ODM_role_%s'% EC]=(data['ODCM_role_%s'% EC]+data['ODFM_role_%s'% EC])
data['ODF_role_%s'% EC]=(data['ODFF_role_%s'% EC]+data['ODCF_role_%s'% EC])
data['ODM_role_%s'% EF]=(data['ODCM_role_%s'% EF]+data['ODFM_role_%s'% EF])
data['ODF_role_%s'% EF]=(data['ODFF_role_%s'% EF]+data['ODCF_role_%s'% EF])

#NOW FOR EACH ROLE WITH WINNER LOSER AS WITNESS
# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TN_roleplus_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_roleplus_num'], np.NaN)
        data['TN_roleplus_%s'% col_name]= np.where(data['TN_roleplus_%s'% col_name]==1,data['obs_beh_roleplus_num_back'], np.NaN)
        data['TN_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TN_roleplus_%s'% col_name])
        data['TN_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TN_roleplus_%s'% col_name])
        data['TN_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TN_roleplus_%s'% col_name]=np.where(data['TN_roleplus_%s'% col_name]==99999, np.NaN, data['TN_roleplus_%s'% col_name])
        data['TN_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TN_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TN_roleplus_%s'% col_name]==88888),
            0,data['TN_roleplus_%s'% col_name])
        data['TN_roleplus_%s'% col_name]=np.where(data['TN_roleplus_%s'% col_name]==88888, np.NaN, data['TN_roleplus_%s'% col_name])
        data['TN_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BN_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_roleplus_num'], np.NaN)
        data['BN_roleplus_%s'% col_name]= np.where(data['BN_roleplus_%s'% col_name]==1,data['obs_beh_loc_roleplus_num_back'], np.NaN)
        data['BN_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BN_roleplus_%s'% col_name]=np.where(data['BN_roleplus_%s'% col_name]==99999, np.NaN, data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BN_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BN_roleplus_%s'% col_name]==88888), 
            0,data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name]=np.where(data['BN_roleplus_%s'% col_name]==88888, np.NaN, data['BN_roleplus_%s'% col_name])
        data['BN_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['ON_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_roleplus_num'], np.NaN)
        data['ON_roleplus_%s'% col_name]= np.where(data['ON_roleplus_%s'% col_name]==1,data['obs_beh_loc_roleplus_num_back'], np.NaN)
        data['ON_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ON_roleplus_%s'% col_name]=np.where(data['ON_roleplus_%s'% col_name]==99999, np.NaN, data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ON_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ON_roleplus_%s'% col_name]==88888), 
            0,data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name]=np.where(data['ON_roleplus_%s'% col_name]==88888, np.NaN, data['ON_roleplus_%s'% col_name])
        data['ON_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additional behaviors for total environment, burrow, and open field    
data['TN_roleplus_%s'% EA]=(data['TN_roleplus_%s'% BG]+data['TN_roleplus_%s'% BD]+data['TN_roleplus_%s'% BC])
data['TN_roleplus_%s'% EB]=(data['TN_roleplus_%s'% BI]+data['TN_roleplus_%s'% BBJ])
data['TN_roleplus_%s'% EC]=(data['TN_roleplus_%s'% BG]+data['TN_roleplus_%s'% BD]+data['TN_roleplus_%s'% BC]+data['TN_roleplus_%s'% BF]+data['TN_roleplus_%s'% BI]+data['TN_roleplus_%s'% BBJ])
data['TN_roleplus_%s'% ED]=(data['TN_roleplus_%s'% BB]+data['TN_roleplus_%s'% BH]+data['TN_roleplus_%s'% BL])
data['TN_roleplus_%s'% EE]=(data['TN_roleplus_%s'% BA]+data['TN_roleplus_%s'% BI]+data['TN_roleplus_%s'% BBI]+data['TN_roleplus_%s'% BBJ])
data['TN_roleplus_%s'% EF]=(data['TN_roleplus_%s'% BM]+data['TN_roleplus_%s'% BN]+data['TN_roleplus_%s'% BO]+data['TN_roleplus_%s'% BP]+data['TN_roleplus_%s'% BQ]+data['TN_roleplus_%s'% BU]+data['TN_roleplus_%s'% BS]+data['TN_roleplus_%s'% BR])
data['TN_roleplus_%s'% EG]=(data['TN_roleplus_%s'% BE]+data['TN_roleplus_%s'% BF])

data['BN_roleplus_%s'% EA]=(data['BN_roleplus_%s'% BG]+data['BN_roleplus_%s'% BD]+data['BN_roleplus_%s'% BC])
data['BN_roleplus_%s'% EB]=(data['BN_roleplus_%s'% BI]+data['BN_roleplus_%s'% BBJ])
data['BN_roleplus_%s'% EC]=(data['BN_roleplus_%s'% BG]+data['BN_roleplus_%s'% BD]+data['BN_roleplus_%s'% BC]+data['BN_roleplus_%s'% BF]+data['BN_roleplus_%s'% BI]+data['BN_roleplus_%s'% BBJ])
data['BN_roleplus_%s'% ED]=(data['BN_roleplus_%s'% BB]+data['BN_roleplus_%s'% BH]+data['BN_roleplus_%s'% BL])
data['BN_roleplus_%s'% EE]=(data['BN_roleplus_%s'% BA]+data['BN_roleplus_%s'% BI]+data['BN_roleplus_%s'% BBI]+data['BN_roleplus_%s'% BBJ])
data['BN_roleplus_%s'% EF]=(data['BN_roleplus_%s'% BM]+data['BN_roleplus_%s'% BN]+data['BN_roleplus_%s'% BO]+data['BN_roleplus_%s'% BP]+data['BN_roleplus_%s'% BQ]+data['BN_roleplus_%s'% BU]+data['BN_roleplus_%s'% BS]+data['BN_roleplus_%s'% BR])
data['BN_roleplus_%s'% EG]=(data['BN_roleplus_%s'% BE]+data['BN_roleplus_%s'% BF])

data['ON_roleplus_%s'% EA]=(data['ON_roleplus_%s'% BG]+data['ON_roleplus_%s'% BD]+data['ON_roleplus_%s'% BC])
data['ON_roleplus_%s'% EB]=(data['ON_roleplus_%s'% BI]+data['ON_roleplus_%s'% BBJ])
data['ON_roleplus_%s'% EC]=(data['ON_roleplus_%s'% BG]+data['ON_roleplus_%s'% BD]+data['ON_roleplus_%s'% BC]+data['ON_roleplus_%s'% BF]+data['ON_roleplus_%s'% BI]+data['ON_roleplus_%s'% BBJ])
data['ON_roleplus_%s'% ED]=(data['ON_roleplus_%s'% BB]+data['ON_roleplus_%s'% BH]+data['ON_roleplus_%s'% BL])
data['ON_roleplus_%s'% EE]=(data['ON_roleplus_%s'% BA]+data['ON_roleplus_%s'% BI]+data['ON_roleplus_%s'% BBI]+data['ON_roleplus_%s'% BBJ])
data['ON_roleplus_%s'% EF]=(data['ON_roleplus_%s'% BM]+data['ON_roleplus_%s'% BN]+data['ON_roleplus_%s'% BO]+data['ON_roleplus_%s'% BP]+data['ON_roleplus_%s'% BQ]+data['ON_roleplus_%s'% BU]+data['ON_roleplus_%s'% BS]+data['ON_roleplus_%s'% BR])
data['ON_roleplus_%s'% EG]=(data['ON_roleplus_%s'% BE]+data['ON_roleplus_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TNFF_roleplus_%s'% col_name]= np.where(data['TNFF_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_num_back'], np.NaN)
    data['TNFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFF_roleplus_%s'% col_name]=np.where(data['TNFF_roleplus_%s'% col_name]==99999, np.NaN, data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFF_roleplus_%s'% col_name]==88888), 
        0,data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name]=np.where(data['TNFF_roleplus_%s'% col_name]==88888, np.NaN, data['TNFF_roleplus_%s'% col_name])
    data['TNFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total environment
    data['TNCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TNCF_roleplus_%s'% col_name]= np.where(data['TNCF_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_num_back'], np.NaN)
    data['TNCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCF_roleplus_%s'% col_name]=np.where(data['TNCF_roleplus_%s'% col_name]==99999, np.NaN, data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCF_roleplus_%s'% col_name]==88888), 
        0,data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name]=np.where(data['TNCF_roleplus_%s'% col_name]==88888, np.NaN, data['TNCF_roleplus_%s'% col_name])
    data['TNCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total environment
    data['TNFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TNFM_roleplus_%s'% col_name]= np.where(data['TNFM_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_num_back'], np.NaN)
    data['TNFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNFM_roleplus_%s'% col_name]=np.where(data['TNFM_roleplus_%s'% col_name]==99999, np.NaN, data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNFM_roleplus_%s'% col_name]==88888), 
        0,data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name]=np.where(data['TNFM_roleplus_%s'% col_name]==88888, np.NaN, data['TNFM_roleplus_%s'% col_name])
    data['TNFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total environment
    data['TNCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TNCM_roleplus_%s'% col_name]= np.where(data['TNCM_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_num_back'], np.NaN)
    data['TNCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNCM_roleplus_%s'% col_name]=np.where(data['TNCM_roleplus_%s'% col_name]==99999, np.NaN, data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNCM_roleplus_%s'% col_name]==88888), 
        0,data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name]=np.where(data['TNCM_roleplus_%s'% col_name]==88888, np.NaN, data['TNCM_roleplus_%s'% col_name])
    data['TNCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TNW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TNW_roleplus_%s'% col_name]= np.where(data['TNW_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_num_back'], np.NaN)
    data['TNW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNW_roleplus_%s'% col_name]=np.where(data['TNW_roleplus_%s'% col_name]==99999, np.NaN, data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNW_roleplus_%s'% col_name]==88888), 
        0,data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name]=np.where(data['TNW_roleplus_%s'% col_name]==88888, np.NaN, data['TNW_roleplus_%s'% col_name])
    data['TNW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TNL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TNL_roleplus_%s'% col_name]= np.where(data['TNL_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_num_back'], np.NaN)
    data['TNL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNL_roleplus_%s'% col_name]=np.where(data['TNL_roleplus_%s'% col_name]==99999, np.NaN, data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNL_roleplus_%s'% col_name]==88888), 
        0,data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name]=np.where(data['TNL_roleplus_%s'% col_name]==88888, np.NaN, data['TNL_roleplus_%s'% col_name])
    data['TNL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TNO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Others')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TNO_roleplus_%s'% col_name]= np.where(data['TNO_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_num_back'], np.NaN)
    data['TNO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TNO_roleplus_%s'% col_name]=np.where(data['TNO_roleplus_%s'% col_name]==99999, np.NaN, data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TNO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TNO_roleplus_%s'% col_name]==88888), 
        0,data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name]=np.where(data['TNO_roleplus_%s'% col_name]==88888, np.NaN, data['TNO_roleplus_%s'% col_name])
    data['TNO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BNFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BNFF_roleplus_%s'% col_name]= np.where(data['BNFF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_roleplus_%s'% col_name]=np.where(data['BNFF_roleplus_%s'% col_name]==99999, np.NaN, data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFF_roleplus_%s'% col_name]==88888), 
        0,data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name]=np.where(data['BNFF_roleplus_%s'% col_name]==88888, np.NaN, data['BNFF_roleplus_%s'% col_name])
    data['BNFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFF_roleplus_%s'% col_name]=np.where(data['BNFF_roleplus_%s'% col_name]==np.NaN,0, data['BNFF_roleplus_%s'% col_name])

    data['BNCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BNCF_roleplus_%s'% col_name]= np.where(data['BNCF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_roleplus_%s'% col_name]=np.where(data['BNCF_roleplus_%s'% col_name]==99999, np.NaN, data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCF_roleplus_%s'% col_name]==88888), 
        0,data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name]=np.where(data['BNCF_roleplus_%s'% col_name]==88888, np.NaN, data['BNCF_roleplus_%s'% col_name])
    data['BNCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCF_roleplus_%s'% col_name]=np.where(data['BNCF_roleplus_%s'% col_name]== np.NaN,0, data['BNCF_roleplus_%s'% col_name])

    data['BNFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BNFM_roleplus_%s'% col_name]= np.where(data['BNFM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_roleplus_%s'% col_name]=np.where(data['BNFM_roleplus_%s'% col_name]==99999, np.NaN, data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNFM_roleplus_%s'% col_name]==88888), 
        0,data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name]=np.where(data['BNFM_roleplus_%s'% col_name]==88888, np.NaN, data['BNFM_roleplus_%s'% col_name])
    data['BNFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNFM_roleplus_%s'% col_name]=np.where(data['BNFM_roleplus_%s'% col_name]==np.NaN,0, data['BNFM_roleplus_%s'% col_name])
 
    data['BNCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BNCM_roleplus_%s'% col_name]= np.where(data['BNCM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_roleplus_%s'% col_name]=np.where(data['BNCM_roleplus_%s'% col_name]==99999, np.NaN, data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNCM_roleplus_%s'% col_name]==88888), 
        0,data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name]=np.where(data['BNCM_roleplus_%s'% col_name]==88888, np.NaN, data['BNCM_roleplus_%s'% col_name])
    data['BNCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNCM_roleplus_%s'% col_name]=np.where(data['BNCM_roleplus_%s'% col_name]== np.NaN,0, data['BNCM_roleplus_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ONFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ONFF_roleplus_%s'% col_name]= np.where(data['ONFF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_roleplus_%s'% col_name]=np.where(data['ONFF_roleplus_%s'% col_name]==99999, np.NaN, data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFF_roleplus_%s'% col_name]==88888), 
        0,data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name]=np.where(data['ONFF_roleplus_%s'% col_name]==88888, np.NaN, data['ONFF_roleplus_%s'% col_name])
    data['ONFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFF_roleplus_%s'% col_name]=np.where(data['ONFF_roleplus_%s'% col_name]== np.NaN,0, data['ONFF_roleplus_%s'% col_name])

    data['ONCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ONCF_roleplus_%s'% col_name]= np.where(data['ONCF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_roleplus_%s'% col_name]=np.where(data['ONCF_roleplus_%s'% col_name]==99999, np.NaN, data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCF_roleplus_%s'% col_name]==88888), 
        0,data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name]=np.where(data['ONCF_roleplus_%s'% col_name]==88888, np.NaN, data['ONCF_roleplus_%s'% col_name])
    data['ONCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCF_roleplus_%s'% col_name]=np.where(data['ONCF_roleplus_%s'% col_name]== np.NaN,0, data['ONCF_roleplus_%s'% col_name])
    
    data['ONFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ONFM_roleplus_%s'% col_name]= np.where(data['ONFM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_roleplus_%s'% col_name]=np.where(data['ONFM_roleplus_%s'% col_name]==99999, np.NaN, data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONFM_roleplus_%s'% col_name]==88888), 
        0,data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name]=np.where(data['ONFM_roleplus_%s'% col_name]==88888, np.NaN, data['ONFM_roleplus_%s'% col_name])
    data['ONFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONFM_roleplus_%s'% col_name]=np.where(data['ONFM_roleplus_%s'% col_name]== np.NaN,0, data['ONFM_roleplus_%s'% col_name])

    data['ONCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ONCM_roleplus_%s'% col_name]= np.where(data['ONCM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_num_back'], np.NaN)
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_roleplus_%s'% col_name]=np.where(data['ONCM_roleplus_%s'% col_name]==99999, np.NaN, data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONCM_roleplus_%s'% col_name]==88888), 
        0,data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name]=np.where(data['ONCM_roleplus_%s'% col_name]==88888, np.NaN, data['ONCM_roleplus_%s'% col_name])
    data['ONCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONCM_roleplus_%s'% col_name]=np.where(data['ONCM_roleplus_%s'% col_name]== np.NaN,0, data['ONCM_roleplus_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BNW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BNW_roleplus_%s'% col_name]= np.where(data['BNW_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_roleplus_%s'% col_name]=np.where(data['BNW_roleplus_%s'% col_name]==99999, np.NaN, data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNW_roleplus_%s'% col_name]==88888), 
        0,data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name]=np.where(data['BNW_roleplus_%s'% col_name]==88888, np.NaN, data['BNW_roleplus_%s'% col_name])
    data['BNW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNW_roleplus_%s'% col_name]=np.where(data['BNW_roleplus_%s'% col_name]== np.NaN,0, data['BNW_roleplus_%s'% col_name])

    data['BNL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BNL_roleplus_%s'% col_name]= np.where(data['BNL_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_roleplus_%s'% col_name]=np.where(data['BNL_roleplus_%s'% col_name]==99999, np.NaN, data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNL_roleplus_%s'% col_name]==88888), 
        0,data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name]=np.where(data['BNL_roleplus_%s'% col_name]==88888, np.NaN, data['BNL_roleplus_%s'% col_name])
    data['BNL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNL_roleplus_%s'% col_name]=np.where(data['BNL_roleplus_%s'% col_name]== np.NaN,0, data['BNL_roleplus_%s'% col_name])

    data['BNO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BNO_roleplus_%s'% col_name]= np.where(data['BNO_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_roleplus_%s'% col_name]=np.where(data['BNO_roleplus_%s'% col_name]==99999, np.NaN, data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BNO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BNO_roleplus_%s'% col_name]==88888), 
        0,data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name]=np.where(data['BNO_roleplus_%s'% col_name]==88888, np.NaN, data['BNO_roleplus_%s'% col_name])
    data['BNO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BNO_roleplus_%s'% col_name]=np.where(data['BNO_roleplus_%s'% col_name]== np.NaN,0, data['BNO_roleplus_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ONW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ONW_roleplus_%s'% col_name]= np.where(data['ONW_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_roleplus_%s'% col_name]=np.where(data['ONW_roleplus_%s'% col_name]==99999, np.NaN, data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONW_roleplus_%s'% col_name]==88888), 
        0,data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name]=np.where(data['ONW_roleplus_%s'% col_name]==88888, np.NaN, data['ONW_roleplus_%s'% col_name])
    data['ONW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONW_roleplus_%s'% col_name]=np.where(data['ONW_roleplus_%s'% col_name]== np.NaN,0, data['ONW_roleplus_%s'% col_name])

    data['ONL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ONL_roleplus_%s'% col_name]= np.where(data['ONL_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_roleplus_%s'% col_name]=np.where(data['ONL_roleplus_%s'% col_name]==99999, np.NaN, data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONL_roleplus_%s'% col_name]==88888), 
        0,data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name]=np.where(data['ONL_roleplus_%s'% col_name]==88888, np.NaN, data['ONL_roleplus_%s'% col_name])
    data['ONL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONL_roleplus_%s'% col_name]=np.where(data['ONL_roleplus_%s'% col_name]== np.NaN,0, data['ONL_roleplus_%s'% col_name])

    data['ONO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ONO_roleplus_%s'% col_name]= np.where(data['ONO_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_num_back'], np.NaN)
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_roleplus_%s'% col_name]=np.where(data['ONO_roleplus_%s'% col_name]==99999, np.NaN, data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ONO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ONO_roleplus_%s'% col_name]==88888), 
        0,data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name]=np.where(data['ONO_roleplus_%s'% col_name]==88888, np.NaN, data['ONO_roleplus_%s'% col_name])
    data['ONO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ONO_roleplus_%s'% col_name]=np.where(data['ONO_roleplus_%s'% col_name]== np.NaN,0, data['ONO_roleplus_%s'% col_name])


# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TNFF_roleplus_%s'% EA]=(data['TNFF_roleplus_%s'% BG]+data['TNFF_roleplus_%s'% BD]+data['TNFF_roleplus_%s'% BC])
data['TNFF_roleplus_%s'% EB]=(data['TNFF_roleplus_%s'% BI]+data['TNFF_roleplus_%s'% BBJ])
data['TNFF_roleplus_%s'% EC]=(data['TNFF_roleplus_%s'% BG]+data['TNFF_roleplus_%s'% BD]+data['TNFF_roleplus_%s'% BC]+data['TNFF_roleplus_%s'% BF]+data['TNFF_roleplus_%s'% BI]+data['TNFF_roleplus_%s'% BBJ])
data['TNFF_roleplus_%s'% EF]=(data['TNFF_roleplus_%s'% BM]+data['TNFF_roleplus_%s'% BN]+data['TNFF_roleplus_%s'% BO]+data['TNFF_roleplus_%s'% BP]+data['TNFF_roleplus_%s'% BQ]+data['TNFF_roleplus_%s'% BU]+data['TNFF_roleplus_%s'% BS]+data['TNFF_roleplus_%s'% BR])

data['BNFF_roleplus_%s'% EA]=(data['BNFF_roleplus_%s'% BG]+data['BNFF_roleplus_%s'% BD]+data['BNFF_roleplus_%s'% BC])
data['BNFF_roleplus_%s'% EB]=(data['BNFF_roleplus_%s'% BI]+data['BNFF_roleplus_%s'% BBJ])
data['BNFF_roleplus_%s'% EC]=(data['BNFF_roleplus_%s'% BG]+data['BNFF_roleplus_%s'% BD]+data['BNFF_roleplus_%s'% BC]+data['BNFF_roleplus_%s'% BF]+data['BNFF_roleplus_%s'% BI]+data['BNFF_roleplus_%s'% BBJ])
data['BNFF_roleplus_%s'% EF]=(data['BNFF_roleplus_%s'% BM]+data['BNFF_roleplus_%s'% BN]+data['BNFF_roleplus_%s'% BO]+data['BNFF_roleplus_%s'% BP]+data['BNFF_roleplus_%s'% BQ]+data['BNFF_roleplus_%s'% BU]+data['BNFF_roleplus_%s'% BS]+data['BNFF_roleplus_%s'% BR])

data['ONFF_roleplus_%s'% EA]=(data['ONFF_roleplus_%s'% BG]+data['ONFF_roleplus_%s'% BD]+data['ONFF_roleplus_%s'% BC])
data['ONFF_roleplus_%s'% EB]=(data['ONFF_roleplus_%s'% BI]+data['ONFF_roleplus_%s'% BBJ])
data['ONFF_roleplus_%s'% EC]=(data['ONFF_roleplus_%s'% BG]+data['ONFF_roleplus_%s'% BD]+data['ONFF_roleplus_%s'% BC]+data['ONFF_roleplus_%s'% BF]+data['ONFF_roleplus_%s'% BI]+data['ONFF_roleplus_%s'% BBJ])
data['ONFF_roleplus_%s'% EF]=(data['ONFF_roleplus_%s'% BM]+data['ONFF_roleplus_%s'% BN]+data['ONFF_roleplus_%s'% BO]+data['ONFF_roleplus_%s'% BP]+data['ONFF_roleplus_%s'% BQ]+data['ONFF_roleplus_%s'% BU]+data['ONFF_roleplus_%s'% BS]+data['ONFF_roleplus_%s'% BR])

data['TNCF_roleplus_%s'% EA]=(data['TNCF_roleplus_%s'% BG]+data['TNCF_roleplus_%s'% BD]+data['TNCF_roleplus_%s'% BC])
data['TNCF_roleplus_%s'% EB]=(data['TNCF_roleplus_%s'% BI]+data['TNCF_roleplus_%s'% BBJ])
data['TNCF_roleplus_%s'% EC]=(data['TNCF_roleplus_%s'% BG]+data['TNCF_roleplus_%s'% BD]+data['TNCF_roleplus_%s'% BC]+data['TNCF_roleplus_%s'% BF]+data['TNCF_roleplus_%s'% BI]+data['TNCF_roleplus_%s'% BBJ])
data['TNCF_roleplus_%s'% EF]=(data['TNCF_roleplus_%s'% BM]+data['TNCF_roleplus_%s'% BN]+data['TNCF_roleplus_%s'% BO]+data['TNCF_roleplus_%s'% BP]+data['TNCF_roleplus_%s'% BQ]+data['TNCF_roleplus_%s'% BU]+data['TNCF_roleplus_%s'% BS]+data['TNCF_roleplus_%s'% BR])

data['BNCF_roleplus_%s'% EA]=(data['BNCF_roleplus_%s'% BG]+data['BNCF_roleplus_%s'% BD]+data['BNCF_roleplus_%s'% BC])
data['BNCF_roleplus_%s'% EB]=(data['BNCF_roleplus_%s'% BI]+data['BNCF_roleplus_%s'% BBJ])
data['BNCF_roleplus_%s'% EC]=(data['BNCF_roleplus_%s'% BG]+data['BNCF_roleplus_%s'% BD]+data['BNCF_roleplus_%s'% BC]+data['BNCF_roleplus_%s'% BF]+data['BNCF_roleplus_%s'% BI]+data['BNCF_roleplus_%s'% BBJ])
data['BNCF_roleplus_%s'% EF]=(data['BNCF_roleplus_%s'% BM]+data['BNCF_roleplus_%s'% BN]+data['BNCF_roleplus_%s'% BO]+data['BNCF_roleplus_%s'% BP]+data['BNCF_roleplus_%s'% BQ]+data['BNCF_roleplus_%s'% BU]+data['BNCF_roleplus_%s'% BS]+data['BNCF_roleplus_%s'% BR])

data['ONCF_roleplus_%s'% EA]=(data['ONCF_roleplus_%s'% BG]+data['ONCF_roleplus_%s'% BD]+data['ONCF_roleplus_%s'% BC])
data['ONCF_roleplus_%s'% EB]=(data['ONCF_roleplus_%s'% BI]+data['ONCF_roleplus_%s'% BBJ])
data['ONCF_roleplus_%s'% EC]=(data['ONCF_roleplus_%s'% BG]+data['ONCF_roleplus_%s'% BD]+data['ONCF_roleplus_%s'% BC]+data['ONCF_roleplus_%s'% BF]+data['ONCF_roleplus_%s'% BI]+data['ONCF_roleplus_%s'% BBJ])
data['ONCF_roleplus_%s'% EF]=(data['ONCF_roleplus_%s'% BM]+data['ONCF_roleplus_%s'% BN]+data['ONCF_roleplus_%s'% BO]+data['ONCF_roleplus_%s'% BP]+data['ONCF_roleplus_%s'% BQ]+data['ONCF_roleplus_%s'% BU]+data['ONCF_roleplus_%s'% BS]+data['ONCF_roleplus_%s'% BR])

data['TNFM_roleplus_%s'% EA]=(data['TNFM_roleplus_%s'% BG]+data['TNFM_roleplus_%s'% BD]+data['TNFM_roleplus_%s'% BC])
data['TNFM_roleplus_%s'% EB]=(data['TNFM_roleplus_%s'% BI]+data['TNFM_roleplus_%s'% BBJ])
data['TNFM_roleplus_%s'% EC]=(data['TNFM_roleplus_%s'% BG]+data['TNFM_roleplus_%s'% BD]+data['TNFM_roleplus_%s'% BC]+data['TNFM_roleplus_%s'% BF]+data['TNFM_roleplus_%s'% BI]+data['TNFM_roleplus_%s'% BBJ])
data['TNFM_roleplus_%s'% EF]=(data['TNFM_roleplus_%s'% BM]+data['TNFM_roleplus_%s'% BN]+data['TNFM_roleplus_%s'% BO]+data['TNFM_roleplus_%s'% BP]+data['TNFM_roleplus_%s'% BQ]+data['TNFM_roleplus_%s'% BU]+data['TNFM_roleplus_%s'% BS]+data['TNFM_roleplus_%s'% BR])

data['BNFM_roleplus_%s'% EA]=(data['BNFM_roleplus_%s'% BG]+data['BNFM_roleplus_%s'% BD]+data['BNFM_roleplus_%s'% BC])
data['BNFM_roleplus_%s'% EB]=(data['BNFM_roleplus_%s'% BI]+data['BNFM_roleplus_%s'% BBJ])
data['BNFM_roleplus_%s'% EC]=(data['BNFM_roleplus_%s'% BG]+data['BNFM_roleplus_%s'% BD]+data['BNFM_roleplus_%s'% BC]+data['BNFM_roleplus_%s'% BF]+data['BNFM_roleplus_%s'% BI]+data['BNFM_roleplus_%s'% BBJ])
data['BNFM_roleplus_%s'% EF]=(data['BNFM_roleplus_%s'% BM]+data['BNFM_roleplus_%s'% BN]+data['BNFM_roleplus_%s'% BO]+data['BNFM_roleplus_%s'% BP]+data['BNFM_roleplus_%s'% BQ]+data['BNFM_roleplus_%s'% BU]+data['BNFM_roleplus_%s'% BS]+data['BNFM_roleplus_%s'% BR])

data['ONFM_roleplus_%s'% EA]=(data['ONFM_roleplus_%s'% BG]+data['ONFM_roleplus_%s'% BD]+data['ONFM_roleplus_%s'% BC])
data['ONFM_roleplus_%s'% EB]=(data['ONFM_roleplus_%s'% BI]+data['ONFM_roleplus_%s'% BBJ])
data['ONFM_roleplus_%s'% EC]=(data['ONFM_roleplus_%s'% BG]+data['ONFM_roleplus_%s'% BD]+data['ONFM_roleplus_%s'% BC]+data['ONFM_roleplus_%s'% BF]+data['ONFM_roleplus_%s'% BI]+data['ONFM_roleplus_%s'% BBJ])
data['ONFM_roleplus_%s'% EF]=(data['ONFM_roleplus_%s'% BM]+data['ONFM_roleplus_%s'% BN]+data['ONFM_roleplus_%s'% BO]+data['ONFM_roleplus_%s'% BP]+data['ONFM_roleplus_%s'% BQ]+data['ONFM_roleplus_%s'% BU]+data['ONFM_roleplus_%s'% BS]+data['ONFM_roleplus_%s'% BR])

data['TNCM_roleplus_%s'% EA]=(data['TNCM_roleplus_%s'% BG]+data['TNCM_roleplus_%s'% BD]+data['TNCM_roleplus_%s'% BC])
data['TNCM_roleplus_%s'% EB]=(data['TNCM_roleplus_%s'% BI]+data['TNCM_roleplus_%s'% BBJ])
data['TNCM_roleplus_%s'% EC]=(data['TNCM_roleplus_%s'% BG]+data['TNCM_roleplus_%s'% BD]+data['TNCM_roleplus_%s'% BC]+data['TNCM_roleplus_%s'% BF]+data['TNCM_roleplus_%s'% BI]+data['TNCM_roleplus_%s'% BBJ])
data['TNCM_roleplus_%s'% EF]=(data['TNCM_roleplus_%s'% BM]+data['TNCM_roleplus_%s'% BN]+data['TNCM_roleplus_%s'% BO]+data['TNCM_roleplus_%s'% BP]+data['TNCM_roleplus_%s'% BQ]+data['TNCM_roleplus_%s'% BU]+data['TNCM_roleplus_%s'% BS]+data['TNCM_roleplus_%s'% BR])

data['BNCM_roleplus_%s'% EA]=(data['BNCM_roleplus_%s'% BG]+data['BNCM_roleplus_%s'% BD]+data['BNCM_roleplus_%s'% BC])
data['BNCM_roleplus_%s'% EB]=(data['BNCM_roleplus_%s'% BI]+data['BNCM_roleplus_%s'% BBJ])
data['BNCM_roleplus_%s'% EC]=(data['BNCM_roleplus_%s'% BG]+data['BNCM_roleplus_%s'% BD]+data['BNCM_roleplus_%s'% BC]+data['BNCM_roleplus_%s'% BF]+data['BNCM_roleplus_%s'% BI]+data['BNCM_roleplus_%s'% BBJ])
data['BNCM_roleplus_%s'% EF]=(data['BNCM_roleplus_%s'% BM]+data['BNCM_roleplus_%s'% BN]+data['BNCM_roleplus_%s'% BO]+data['BNCM_roleplus_%s'% BP]+data['BNCM_roleplus_%s'% BQ]+data['BNCM_roleplus_%s'% BU]+data['BNCM_roleplus_%s'% BS]+data['BNCM_roleplus_%s'% BR])

data['ONCM_roleplus_%s'% EA]=(data['ONCM_roleplus_%s'% BG]+data['ONCM_roleplus_%s'% BD]+data['ONCM_roleplus_%s'% BC])
data['ONCM_roleplus_%s'% EB]=(data['ONCM_roleplus_%s'% BI]+data['ONCM_roleplus_%s'% BBJ])
data['ONCM_roleplus_%s'% EC]=(data['ONCM_roleplus_%s'% BG]+data['ONCM_roleplus_%s'% BD]+data['ONCM_roleplus_%s'% BC]+data['ONCM_roleplus_%s'% BF]+data['ONCM_roleplus_%s'% BI]+data['ONCM_roleplus_%s'% BBJ])
data['ONCM_roleplus_%s'% EF]=(data['ONCM_roleplus_%s'% BM]+data['ONCM_roleplus_%s'% BN]+data['ONCM_roleplus_%s'% BO]+data['ONCM_roleplus_%s'% BP]+data['ONCM_roleplus_%s'% BQ]+data['ONCM_roleplus_%s'% BU]+data['ONCM_roleplus_%s'% BS]+data['ONCM_roleplus_%s'% BR])

data['TNW_roleplus_%s'% EA]=(data['TNW_roleplus_%s'% BG]+data['TNW_roleplus_%s'% BD]+data['TNW_roleplus_%s'% BC])
data['TNW_roleplus_%s'% EB]=(data['TNW_roleplus_%s'% BI]+data['TNW_roleplus_%s'% BBJ])
data['TNW_roleplus_%s'% EC]=(data['TNW_roleplus_%s'% BG]+data['TNW_roleplus_%s'% BD]+data['TNW_roleplus_%s'% BC]+data['TNW_roleplus_%s'% BF]+data['TNW_roleplus_%s'% BI]+data['TNW_roleplus_%s'% BBJ])
data['TNW_roleplus_%s'% EF]=(data['TNW_roleplus_%s'% BM]+data['TNW_roleplus_%s'% BN]+data['TNW_roleplus_%s'% BO]+data['TNW_roleplus_%s'% BP]+data['TNW_roleplus_%s'% BQ]+data['TNW_roleplus_%s'% BU]+data['TNW_roleplus_%s'% BS]+data['TNW_roleplus_%s'% BR])

data['BNW_roleplus_%s'% EA]=(data['BNW_roleplus_%s'% BG]+data['BNW_roleplus_%s'% BD]+data['BNW_roleplus_%s'% BC])
data['BNW_roleplus_%s'% EB]=(data['BNW_roleplus_%s'% BI]+data['BNW_roleplus_%s'% BBJ])
data['BNW_roleplus_%s'% EC]=(data['BNW_roleplus_%s'% BG]+data['BNW_roleplus_%s'% BD]+data['BNW_roleplus_%s'% BC]+data['BNW_roleplus_%s'% BF]+data['BNW_roleplus_%s'% BI]+data['BNW_roleplus_%s'% BBJ])
data['BNW_roleplus_%s'% EF]=(data['BNW_roleplus_%s'% BM]+data['BNW_roleplus_%s'% BN]+data['BNW_roleplus_%s'% BO]+data['BNW_roleplus_%s'% BP]+data['BNW_roleplus_%s'% BQ]+data['BNW_roleplus_%s'% BU]+data['BNW_roleplus_%s'% BS]+data['BNW_roleplus_%s'% BR])

data['ONW_roleplus_%s'% EA]=(data['ONW_roleplus_%s'% BG]+data['ONW_roleplus_%s'% BD]+data['ONW_roleplus_%s'% BC])
data['ONW_roleplus_%s'% EB]=(data['ONW_roleplus_%s'% BI]+data['ONW_roleplus_%s'% BBJ])
data['ONW_roleplus_%s'% EC]=(data['ONW_roleplus_%s'% BG]+data['ONW_roleplus_%s'% BD]+data['ONW_roleplus_%s'% BC]+data['ONW_roleplus_%s'% BF]+data['ONW_roleplus_%s'% BI]+data['ONW_roleplus_%s'% BBJ])
data['ONW_roleplus_%s'% EF]=(data['ONW_roleplus_%s'% BM]+data['ONW_roleplus_%s'% BN]+data['ONW_roleplus_%s'% BO]+data['ONW_roleplus_%s'% BP]+data['ONW_roleplus_%s'% BQ]+data['ONW_roleplus_%s'% BU]+data['ONW_roleplus_%s'% BS]+data['ONW_roleplus_%s'% BR])

data['TNL_roleplus_%s'% EA]=(data['TNL_roleplus_%s'% BG]+data['TNL_roleplus_%s'% BD]+data['TNL_roleplus_%s'% BC])
data['TNL_roleplus_%s'% EB]=(data['TNL_roleplus_%s'% BI]+data['TNL_roleplus_%s'% BBJ])
data['TNL_roleplus_%s'% EC]=(data['TNL_roleplus_%s'% BG]+data['TNL_roleplus_%s'% BD]+data['TNL_roleplus_%s'% BC]+data['TNL_roleplus_%s'% BF]+data['TNL_roleplus_%s'% BI]+data['TNL_roleplus_%s'% BBJ])
data['TNL_roleplus_%s'% EF]=(data['TNL_roleplus_%s'% BM]+data['TNL_roleplus_%s'% BN]+data['TNL_roleplus_%s'% BO]+data['TNL_roleplus_%s'% BP]+data['TNL_roleplus_%s'% BQ]+data['TNL_roleplus_%s'% BU]+data['TNL_roleplus_%s'% BS]+data['TNL_roleplus_%s'% BR])

data['BNL_roleplus_%s'% EA]=(data['BNL_roleplus_%s'% BG]+data['BNL_roleplus_%s'% BD]+data['BNL_roleplus_%s'% BC])
data['BNL_roleplus_%s'% EB]=(data['BNL_roleplus_%s'% BI]+data['BNL_roleplus_%s'% BBJ])
data['BNL_roleplus_%s'% EC]=(data['BNL_roleplus_%s'% BG]+data['BNL_roleplus_%s'% BD]+data['BNL_roleplus_%s'% BC]+data['BNL_roleplus_%s'% BF]+data['BNL_roleplus_%s'% BI]+data['BNL_roleplus_%s'% BBJ])
data['BNL_roleplus_%s'% EF]=(data['BNL_roleplus_%s'% BM]+data['BNL_roleplus_%s'% BN]+data['BNL_roleplus_%s'% BO]+data['BNL_roleplus_%s'% BP]+data['BNL_roleplus_%s'% BQ]+data['BNL_roleplus_%s'% BU]+data['BNL_roleplus_%s'% BS]+data['BNL_roleplus_%s'% BR])

data['ONL_roleplus_%s'% EA]=(data['ONL_roleplus_%s'% BG]+data['ONL_roleplus_%s'% BD]+data['ONL_roleplus_%s'% BC])
data['ONL_roleplus_%s'% EB]=(data['ONL_roleplus_%s'% BI]+data['ONL_roleplus_%s'% BBJ])
data['ONL_roleplus_%s'% EC]=(data['ONL_roleplus_%s'% BG]+data['ONL_roleplus_%s'% BD]+data['ONL_roleplus_%s'% BC]+data['ONL_roleplus_%s'% BF]+data['ONL_roleplus_%s'% BI]+data['ONL_roleplus_%s'% BBJ])
data['ONL_roleplus_%s'% EF]=(data['ONL_roleplus_%s'% BM]+data['ONL_roleplus_%s'% BN]+data['ONL_roleplus_%s'% BO]+data['ONL_roleplus_%s'% BP]+data['ONL_roleplus_%s'% BQ]+data['ONL_roleplus_%s'% BU]+data['ONL_roleplus_%s'% BS]+data['ONL_roleplus_%s'% BR])

data['TNO_roleplus_%s'% EA]=(data['TNO_roleplus_%s'% BG]+data['TNO_roleplus_%s'% BD]+data['TNO_roleplus_%s'% BC])
data['TNO_roleplus_%s'% EB]=(data['TNO_roleplus_%s'% BI]+data['TNO_roleplus_%s'% BBJ])
data['TNO_roleplus_%s'% EC]=(data['TNO_roleplus_%s'% BG]+data['TNO_roleplus_%s'% BD]+data['TNO_roleplus_%s'% BC]+data['TNO_roleplus_%s'% BF]+data['TNO_roleplus_%s'% BI]+data['TNO_roleplus_%s'% BBJ])
data['TNO_roleplus_%s'% EF]=(data['TNO_roleplus_%s'% BM]+data['TNO_roleplus_%s'% BN]+data['TNO_roleplus_%s'% BO]+data['TNO_roleplus_%s'% BP]+data['TNO_roleplus_%s'% BQ]+data['TNO_roleplus_%s'% BU]+data['TNO_roleplus_%s'% BS]+data['TNO_roleplus_%s'% BR])

data['BNO_roleplus_%s'% EA]=(data['BNO_roleplus_%s'% BG]+data['BNO_roleplus_%s'% BD]+data['BNO_roleplus_%s'% BC])
data['BNO_roleplus_%s'% EB]=(data['BNO_roleplus_%s'% BI]+data['BNO_roleplus_%s'% BBJ])
data['BNO_roleplus_%s'% EC]=(data['BNO_roleplus_%s'% BG]+data['BNO_roleplus_%s'% BD]+data['BNO_roleplus_%s'% BC]+data['BNO_roleplus_%s'% BF]+data['BNO_roleplus_%s'% BI]+data['BNO_roleplus_%s'% BBJ])
data['BNO_roleplus_%s'% EF]=(data['BNO_roleplus_%s'% BM]+data['BNO_roleplus_%s'% BN]+data['BNO_roleplus_%s'% BO]+data['BNO_roleplus_%s'% BP]+data['BNO_roleplus_%s'% BQ]+data['BNO_roleplus_%s'% BU]+data['BNO_roleplus_%s'% BS]+data['BNO_roleplus_%s'% BR])

data['ONO_roleplus_%s'% EA]=(data['ONO_roleplus_%s'% BG]+data['ONO_roleplus_%s'% BD]+data['ONO_roleplus_%s'% BC])
data['ONO_roleplus_%s'% EB]=(data['ONO_roleplus_%s'% BI]+data['ONO_roleplus_%s'% BBJ])
data['ONO_roleplus_%s'% EC]=(data['ONO_roleplus_%s'% BG]+data['ONO_roleplus_%s'% BD]+data['ONO_roleplus_%s'% BC]+data['ONO_roleplus_%s'% BF]+data['ONO_roleplus_%s'% BI]+data['ONO_roleplus_%s'% BBJ])
data['ONO_roleplus_%s'% EF]=(data['ONO_roleplus_%s'% BM]+data['ONO_roleplus_%s'% BN]+data['ONO_roleplus_%s'% BO]+data['ONO_roleplus_%s'% BP]+data['ONO_roleplus_%s'% BQ]+data['ONO_roleplus_%s'% BU]+data['ONO_roleplus_%s'% BS]+data['ONO_roleplus_%s'% BR])

  
# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNCR_roleplus_%s'% col_name]=(data['TNCF_roleplus_%s'% col_name]+data['TNCM_roleplus_%s'% col_name])
    data['TNFR_roleplus_%s'% col_name]=(data['TNFF_roleplus_%s'% col_name]+data['TNFM_roleplus_%s'% col_name])

data['TNCR_roleplus_%s'% EA]=(data['TNCF_roleplus_%s'% EA]+data['TNCM_roleplus_%s'% EA])
data['TNFR_roleplus_%s'% EA]=(data['TNFF_roleplus_%s'% EA]+data['TNFM_roleplus_%s'% EA])
data['TNCR_roleplus_%s'% EB]=(data['TNCF_roleplus_%s'% EB]+data['TNCM_roleplus_%s'% EB])
data['TNFR_roleplus_%s'% EB]=(data['TNFF_roleplus_%s'% EB]+data['TNFM_roleplus_%s'% EB])
data['TNCR_roleplus_%s'% EC]=(data['TNCF_roleplus_%s'% EC]+data['TNCM_roleplus_%s'% EC])
data['TNFR_roleplus_%s'% EC]=(data['TNFF_roleplus_%s'% EC]+data['TNFM_roleplus_%s'% EC])
data['TNCR_roleplus_%s'% EF]=(data['TNCF_roleplus_%s'% EF]+data['TNCM_roleplus_%s'% EF])
data['TNFR_roleplus_%s'% EF]=(data['TNFF_roleplus_%s'% EF]+data['TNFM_roleplus_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total environment
for position, col_name in enumerate(list_behaviors_social):
    data['TNM_roleplus_%s'% col_name]=(data['TNCM_roleplus_%s'% col_name]+data['TNFM_roleplus_%s'% col_name])
    data['TNF_roleplus_%s'% col_name]=(data['TNFF_roleplus_%s'% col_name]+data['TNCF_roleplus_%s'% col_name])

data['TNM_roleplus_%s'% EA]=(data['TNCM_roleplus_%s'% EA]+data['TNFM_roleplus_%s'% EA])
data['TNF_roleplus_%s'% EA]=(data['TNFF_roleplus_%s'% EA]+data['TNCF_roleplus_%s'% EA])
data['TNM_roleplus_%s'% EB]=(data['TNCM_roleplus_%s'% EB]+data['TNFM_roleplus_%s'% EB])
data['TNF_roleplus_%s'% EB]=(data['TNFF_roleplus_%s'% EB]+data['TNCF_roleplus_%s'% EB])
data['TNM_roleplus_%s'% EC]=(data['TNCM_roleplus_%s'% EC]+data['TNFM_roleplus_%s'% EC])
data['TNF_roleplus_%s'% EC]=(data['TNFF_roleplus_%s'% EC]+data['TNCF_roleplus_%s'% EC])
data['TNM_roleplus_%s'% EF]=(data['TNCM_roleplus_%s'% EF]+data['TNFM_roleplus_%s'% EF])
data['TNF_roleplus_%s'% EF]=(data['TNFF_roleplus_%s'% EF]+data['TNCF_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BNCR_roleplus_%s'% col_name]=(data['BNCF_roleplus_%s'% col_name]+data['BNCM_roleplus_%s'% col_name])
    data['BNFR_roleplus_%s'% col_name]=(data['BNFF_roleplus_%s'% col_name]+data['BNFM_roleplus_%s'% col_name])

data['BNCR_roleplus_%s'% EA]=(data['BNCF_roleplus_%s'% EA]+data['BNCM_roleplus_%s'% EA])
data['BNFR_roleplus_%s'% EA]=(data['BNFF_roleplus_%s'% EA]+data['BNFM_roleplus_%s'% EA])
data['BNCR_roleplus_%s'% EB]=(data['BNCF_roleplus_%s'% EB]+data['BNCM_roleplus_%s'% EB])
data['BNFR_roleplus_%s'% EB]=(data['BNFF_roleplus_%s'% EB]+data['BNFM_roleplus_%s'% EB])
data['BNCR_roleplus_%s'% EC]=(data['BNCF_roleplus_%s'% EC]+data['BNCM_roleplus_%s'% EC])
data['BNFR_roleplus_%s'% EC]=(data['BNFF_roleplus_%s'% EC]+data['BNFM_roleplus_%s'% EC])
data['BNCR_roleplus_%s'% EF]=(data['BNCF_roleplus_%s'% EF]+data['BNCM_roleplus_%s'% EF])
data['BNFR_roleplus_%s'% EF]=(data['BNFF_roleplus_%s'% EF]+data['BNFM_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BNM_roleplus_%s'% col_name]=(data['BNCM_roleplus_%s'% col_name]+data['BNFM_roleplus_%s'% col_name])
    data['BNF_roleplus_%s'% col_name]=(data['BNFF_roleplus_%s'% col_name]+data['BNCF_roleplus_%s'% col_name])

data['BNM_roleplus_%s'% EA]=(data['BNCM_roleplus_%s'% EA]+data['BNFM_roleplus_%s'% EA])
data['BNF_roleplus_%s'% EA]=(data['BNFF_roleplus_%s'% EA]+data['BNCF_roleplus_%s'% EA])
data['BNM_roleplus_%s'% EB]=(data['BNCM_roleplus_%s'% EB]+data['BNFM_roleplus_%s'% EB])
data['BNF_roleplus_%s'% EB]=(data['BNFF_roleplus_%s'% EB]+data['BNCF_roleplus_%s'% EB])
data['BNM_roleplus_%s'% EC]=(data['BNCM_roleplus_%s'% EC]+data['BNFM_roleplus_%s'% EC])
data['BNF_roleplus_%s'% EC]=(data['BNFF_roleplus_%s'% EC]+data['BNCF_roleplus_%s'% EC])
data['BNM_roleplus_%s'% EF]=(data['BNCM_roleplus_%s'% EF]+data['BNFM_roleplus_%s'% EF])
data['BNF_roleplus_%s'% EF]=(data['BNFF_roleplus_%s'% EF]+data['BNCF_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONCR_roleplus_%s'% col_name]=(data['ONCF_roleplus_%s'% col_name]+data['ONCM_roleplus_%s'% col_name])
    data['ONFR_roleplus_%s'% col_name]=(data['ONFF_roleplus_%s'% col_name]+data['ONFM_roleplus_%s'% col_name])

data['ONCR_roleplus_%s'% EA]=(data['ONCF_roleplus_%s'% EA]+data['ONCM_roleplus_%s'% EA])
data['ONFR_roleplus_%s'% EA]=(data['ONFF_roleplus_%s'% EA]+data['ONFM_roleplus_%s'% EA])
data['ONCR_roleplus_%s'% EB]=(data['ONCF_roleplus_%s'% EB]+data['ONCM_roleplus_%s'% EB])
data['ONFR_roleplus_%s'% EB]=(data['ONFF_roleplus_%s'% EB]+data['ONFM_roleplus_%s'% EB])
data['ONCR_roleplus_%s'% EC]=(data['ONCF_roleplus_%s'% EC]+data['ONCM_roleplus_%s'% EC])
data['ONFR_roleplus_%s'% EC]=(data['ONFF_roleplus_%s'% EC]+data['ONFM_roleplus_%s'% EC])
data['ONCR_roleplus_%s'% EF]=(data['ONCF_roleplus_%s'% EF]+data['ONCM_roleplus_%s'% EF])
data['ONFR_roleplus_%s'% EF]=(data['ONFF_roleplus_%s'% EF]+data['ONFM_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ONM_roleplus_%s'% col_name]=(data['ONCM_roleplus_%s'% col_name]+data['ONFM_roleplus_%s'% col_name])
    data['ONF_roleplus_%s'% col_name]=(data['ONFF_roleplus_%s'% col_name]+data['ONCF_roleplus_%s'% col_name])

data['ONM_roleplus_%s'% EA]=(data['ONCM_roleplus_%s'% EA]+data['ONFM_roleplus_%s'% EA])
data['ONF_roleplus_%s'% EA]=(data['ONFF_roleplus_%s'% EA]+data['ONCF_roleplus_%s'% EA])
data['ONM_roleplus_%s'% EB]=(data['ONCM_roleplus_%s'% EB]+data['ONFM_roleplus_%s'% EB])
data['ONF_roleplus_%s'% EB]=(data['ONFF_roleplus_%s'% EB]+data['ONCF_roleplus_%s'% EB])
data['ONM_roleplus_%s'% EC]=(data['ONCM_roleplus_%s'% EC]+data['ONFM_roleplus_%s'% EC])
data['ONF_roleplus_%s'% EC]=(data['ONFF_roleplus_%s'% EC]+data['ONCF_roleplus_%s'% EC])
data['ONM_roleplus_%s'% EF]=(data['ONCM_roleplus_%s'% EF]+data['ONFM_roleplus_%s'% EF])
data['ONF_roleplus_%s'% EF]=(data['ONFF_roleplus_%s'% EF]+data['ONCF_roleplus_%s'% EF])

# Calculate total number of each behavior per rat in total environment
for position, col_name in enumerate(list_behaviors):
        data['TD_roleplus_%s'% col_name]= np.where(data[O]==col_name,data['obs_beh_roleplus_num'], np.NaN)
        data['TD_roleplus_%s'% col_name]= np.where(data['TD_roleplus_%s'% col_name]==1,data['obs_beh_roleplus_sumdur'], np.NaN)
        data['TD_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num']==1,data[O]!=col_name), 99999,
            data['TD_roleplus_%s'% col_name])
        data['TD_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']==1,data[O]!=col_name), 
            88888,data['TD_roleplus_%s'% col_name])
        data['TD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TD_roleplus_%s'% col_name]=np.where(data['TD_roleplus_%s'% col_name]==99999, np.NaN, data['TD_roleplus_%s'% col_name])
        data['TD_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TD_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TD_roleplus_%s'% col_name]==88888),
            0,data['TD_roleplus_%s'% col_name])
        data['TD_roleplus_%s'% col_name]=np.where(data['TD_roleplus_%s'% col_name]==88888, np.NaN, data['TD_roleplus_%s'% col_name])
        data['TD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)        
        
        # Calculate total number of each behavior per rat in burrow area
        data['BD_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Burrow')),data['obs_beh_loc_roleplus_num'], np.NaN)
        data['BD_roleplus_%s'% col_name]= np.where(data['BD_roleplus_%s'% col_name]==1,data['obs_beh_loc_roleplus_sumdur'], np.NaN)
        data['BD_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 99999,
            data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')), 
            88888,data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BD_roleplus_%s'% col_name]=np.where(data['BD_roleplus_%s'% col_name]==99999, np.NaN, data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BD_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BD_roleplus_%s'% col_name]==88888), 
            0,data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name]=np.where(data['BD_roleplus_%s'% col_name]==88888, np.NaN, data['BD_roleplus_%s'% col_name])
        data['BD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
        # Calculate total number of each behavior per rat in open area
        data['OD_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XL]=='Open field')),data['obs_beh_loc_roleplus_num'], np.NaN)
        data['OD_roleplus_%s'% col_name]= np.where(data['OD_roleplus_%s'% col_name]==1,data['obs_beh_loc_role_sumdur'], np.NaN)
        data['OD_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
            data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 99999,
            data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
            88888,data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')), 
            88888,data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['OD_roleplus_%s'% col_name]=np.where(data['OD_roleplus_%s'% col_name]==99999, np.NaN, data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['OD_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['OD_roleplus_%s'% col_name]==88888), 
            0,data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name]=np.where(data['OD_roleplus_%s'% col_name]==88888, np.NaN, data['OD_roleplus_%s'% col_name])
        data['OD_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)    
    
# Calculate the additiODal behaviors for total envirODment, burrow, and open field    
data['TD_roleplus_%s'% EA]=(data['TD_roleplus_%s'% BG]+data['TD_roleplus_%s'% BD]+data['TD_roleplus_%s'% BC])
data['TD_roleplus_%s'% EB]=(data['TD_roleplus_%s'% BI]+data['TD_roleplus_%s'% BBJ])
data['TD_roleplus_%s'% EC]=(data['TD_roleplus_%s'% BG]+data['TD_roleplus_%s'% BD]+data['TD_roleplus_%s'% BC]+data['TD_roleplus_%s'% BF]+data['TD_roleplus_%s'% BI]+data['TD_roleplus_%s'% BBJ])
data['TD_roleplus_%s'% ED]=(data['TD_roleplus_%s'% BB]+data['TD_roleplus_%s'% BH]+data['TD_roleplus_%s'% BL])
data['TD_roleplus_%s'% EE]=(data['TD_roleplus_%s'% BA]+data['TD_roleplus_%s'% BI]+data['TD_roleplus_%s'% BBI]+data['TD_roleplus_%s'% BBJ])
data['TD_roleplus_%s'% EF]=(data['TD_roleplus_%s'% BM]+data['TD_roleplus_%s'% BD]+data['TD_roleplus_%s'% BO]+data['TD_roleplus_%s'% BP]+data['TD_roleplus_%s'% BQ]+data['TD_roleplus_%s'% BU]+data['TD_roleplus_%s'% BS]+data['TD_roleplus_%s'% BR])
data['TD_roleplus_%s'% EG]=(data['TD_roleplus_%s'% BE]+data['TD_roleplus_%s'% BF])

data['BD_roleplus_%s'% EA]=(data['BD_roleplus_%s'% BG]+data['BD_roleplus_%s'% BD]+data['BD_roleplus_%s'% BC])
data['BD_roleplus_%s'% EB]=(data['BD_roleplus_%s'% BI]+data['BD_roleplus_%s'% BBJ])
data['BD_roleplus_%s'% EC]=(data['BD_roleplus_%s'% BG]+data['BD_roleplus_%s'% BD]+data['BD_roleplus_%s'% BC]+data['BD_roleplus_%s'% BF]+data['BD_roleplus_%s'% BI]+data['BD_roleplus_%s'% BBJ])
data['BD_roleplus_%s'% ED]=(data['BD_roleplus_%s'% BB]+data['BD_roleplus_%s'% BH]+data['BD_roleplus_%s'% BL])
data['BD_roleplus_%s'% EE]=(data['BD_roleplus_%s'% BA]+data['BD_roleplus_%s'% BI]+data['BD_roleplus_%s'% BBI]+data['BD_roleplus_%s'% BBJ])
data['BD_roleplus_%s'% EF]=(data['BD_roleplus_%s'% BM]+data['BD_roleplus_%s'% BD]+data['BD_roleplus_%s'% BO]+data['BD_roleplus_%s'% BP]+data['BD_roleplus_%s'% BQ]+data['BD_roleplus_%s'% BU]+data['BD_roleplus_%s'% BS]+data['BD_roleplus_%s'% BR])
data['BD_roleplus_%s'% EG]=(data['BD_roleplus_%s'% BE]+data['BD_roleplus_%s'% BF])

data['OD_roleplus_%s'% EA]=(data['OD_roleplus_%s'% BG]+data['OD_roleplus_%s'% BD]+data['OD_roleplus_%s'% BC])
data['OD_roleplus_%s'% EB]=(data['OD_roleplus_%s'% BI]+data['OD_roleplus_%s'% BBJ])
data['OD_roleplus_%s'% EC]=(data['OD_roleplus_%s'% BG]+data['OD_roleplus_%s'% BD]+data['OD_roleplus_%s'% BC]+data['OD_roleplus_%s'% BF]+data['OD_roleplus_%s'% BI]+data['OD_roleplus_%s'% BBJ])
data['OD_roleplus_%s'% ED]=(data['OD_roleplus_%s'% BB]+data['OD_roleplus_%s'% BH]+data['OD_roleplus_%s'% BL])
data['OD_roleplus_%s'% EE]=(data['OD_roleplus_%s'% BA]+data['OD_roleplus_%s'% BI]+data['OD_roleplus_%s'% BBI]+data['OD_roleplus_%s'% BBJ])
data['OD_roleplus_%s'% EF]=(data['OD_roleplus_%s'% BM]+data['OD_roleplus_%s'% BD]+data['OD_roleplus_%s'% BO]+data['OD_roleplus_%s'% BP]+data['OD_roleplus_%s'% BQ]+data['OD_roleplus_%s'% BU]+data['OD_roleplus_%s'% BS]+data['OD_roleplus_%s'% BR])
data['OD_roleplus_%s'% EG]=(data['OD_roleplus_%s'% BE]+data['OD_roleplus_%s'% BF])


# Calculate total number of each "social" behavior directed at FLX-female in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TDFF_roleplus_%s'% col_name]= np.where(data['TDFF_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_sumdur'], np.NaN)
    data['TDFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFF_roleplus_%s'% col_name]=np.where(data['TDFF_roleplus_%s'% col_name]==99999, np.NaN, data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFF_roleplus_%s'% col_name]==88888), 
        0,data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name]=np.where(data['TDFF_roleplus_%s'% col_name]==88888, np.NaN, data['TDFF_roleplus_%s'% col_name])
    data['TDFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at CTR-females in total envirODment
    data['TDCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TDCF_roleplus_%s'% col_name]= np.where(data['TDCF_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_sumdur'], np.NaN)
    data['TDCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='FLX-males')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCF_roleplus_%s'% col_name]=np.where(data['TDCF_roleplus_%s'% col_name]==99999, np.NaN, data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCF_roleplus_%s'% col_name]==88888), 
        0,data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name]=np.where(data['TDCF_roleplus_%s'% col_name]==88888, np.NaN, data['TDCF_roleplus_%s'% col_name])
    data['TDCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-males in total envirODment
    data['TDFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TDFM_roleplus_%s'% col_name]= np.where(data['TDFM_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_sumdur'], np.NaN)
    data['TDFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDFM_roleplus_%s'% col_name]=np.where(data['TDFM_roleplus_%s'% col_name]==99999, np.NaN, data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDFM_roleplus_%s'% col_name]==88888), 
        0,data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name]=np.where(data['TDFM_roleplus_%s'% col_name]==88888, np.NaN, data['TDFM_roleplus_%s'% col_name])
    data['TDFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at CTR-males in total envirODment
    data['TDCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')),data['obs_beh_treat_roleplus_num'], np.NaN)
    data['TDCM_roleplus_%s'% col_name]= np.where(data['TDCM_roleplus_%s'% col_name]==1,data['obs_beh_treat_roleplus_sumdur'], np.NaN)
    data['TDCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))), 99999,data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XI]=='CTR-females')|
            (data[XI]=='FLX-females')|(data[XI]=='FLX-males'))),88888,data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDCM_roleplus_%s'% col_name]=np.where(data['TDCM_roleplus_%s'% col_name]==99999, np.NaN, data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDCM_roleplus_%s'% col_name]==88888), 
        0,data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name]=np.where(data['TDCM_roleplus_%s'% col_name]==88888, np.NaN, data['TDCM_roleplus_%s'% col_name])
    data['TDCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in burrow
    data['BDFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BDFF_roleplus_%s'% col_name]= np.where(data['BDFF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_roleplus_%s'% col_name]=np.where(data['BDFF_roleplus_%s'% col_name]==99999, np.NaN, data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFF_roleplus_%s'% col_name]==88888), 
        0,data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name]=np.where(data['BDFF_roleplus_%s'% col_name]==88888, np.NaN, data['BDFF_roleplus_%s'% col_name])
    data['BDFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFF_roleplus_%s'% col_name]=np.where(data['BDFF_roleplus_%s'% col_name]==np.NaN,0, data['BDFF_roleplus_%s'% col_name])

    data['BDCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BDCF_roleplus_%s'% col_name]= np.where(data['BDCF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_roleplus_%s'% col_name]=np.where(data['BDCF_roleplus_%s'% col_name]==99999, np.NaN, data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCF_roleplus_%s'% col_name]==88888), 
        0,data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name]=np.where(data['BDCF_roleplus_%s'% col_name]==88888, np.NaN, data['BDCF_roleplus_%s'% col_name])
    data['BDCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCF_roleplus_%s'% col_name]=np.where(data['BDCF_roleplus_%s'% col_name]== np.NaN,0, data['BDCF_roleplus_%s'% col_name])

    data['BDFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BDFM_roleplus_%s'% col_name]= np.where(data['BDFM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_roleplus_%s'% col_name]=np.where(data['BDFM_roleplus_%s'% col_name]==99999, np.NaN, data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDFM_roleplus_%s'% col_name]==88888), 
        0,data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name]=np.where(data['BDFM_roleplus_%s'% col_name]==88888, np.NaN, data['BDFM_roleplus_%s'% col_name])
    data['BDFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDFM_roleplus_%s'% col_name]=np.where(data['BDFM_roleplus_%s'% col_name]==np.NaN,0, data['BDFM_roleplus_%s'% col_name])
 
    data['BDCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Burrow')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['BDCM_roleplus_%s'% col_name]= np.where(data['BDCM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_roleplus_%s'% col_name]=np.where(data['BDCM_roleplus_%s'% col_name]==99999, np.NaN, data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDCM_roleplus_%s'% col_name]==88888), 
        0,data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name]=np.where(data['BDCM_roleplus_%s'% col_name]==88888, np.NaN, data['BDCM_roleplus_%s'% col_name])
    data['BDCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDCM_roleplus_%s'% col_name]=np.where(data['BDCM_roleplus_%s'% col_name]== np.NaN,0, data['BDCM_roleplus_%s'% col_name])
    
    # Calculate total number of each "social" behavior directed at FLX-female/CTR-female
    # FLX-males/CTR-males in Open field
    data['ODFF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ODFF_roleplus_%s'% col_name]= np.where(data['ODFF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_roleplus_%s'% col_name]=np.where(data['ODFF_roleplus_%s'% col_name]==99999, np.NaN, data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFF_roleplus_%s'% col_name]==88888), 
        0,data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name]=np.where(data['ODFF_roleplus_%s'% col_name]==88888, np.NaN, data['ODFF_roleplus_%s'% col_name])
    data['ODFF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFF_roleplus_%s'% col_name]=np.where(data['ODFF_roleplus_%s'% col_name]== np.NaN,0, data['ODFF_roleplus_%s'% col_name])

    data['ODCF_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-females')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ODCF_roleplus_%s'% col_name]= np.where(data['ODCF_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))), 99999,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-males'))),88888,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_roleplus_%s'% col_name]=np.where(data['ODCF_roleplus_%s'% col_name]==99999, np.NaN, data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCF_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCF_roleplus_%s'% col_name]==88888), 
        0,data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name]=np.where(data['ODCF_roleplus_%s'% col_name]==88888, np.NaN, data['ODCF_roleplus_%s'% col_name])
    data['ODCF_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCF_roleplus_%s'% col_name]=np.where(data['ODCF_roleplus_%s'% col_name]== np.NaN,0, data['ODCF_roleplus_%s'% col_name])
    
    data['ODFM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='FLX-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ODFM_roleplus_%s'% col_name]= np.where(data['ODFM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))), 99999,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-females')|(data[XI]=='CTR-females')|(data[XI]=='CTR-males'))),88888,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_roleplus_%s'% col_name]=np.where(data['ODFM_roleplus_%s'% col_name]==99999, np.NaN, data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODFM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODFM_roleplus_%s'% col_name]==88888), 
        0,data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name]=np.where(data['ODFM_roleplus_%s'% col_name]==88888, np.NaN, data['ODFM_roleplus_%s'% col_name])
    data['ODFM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODFM_roleplus_%s'% col_name]=np.where(data['ODFM_roleplus_%s'% col_name]== np.NaN,0, data['ODFM_roleplus_%s'% col_name])

    data['ODCM_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XI]=='CTR-males')&(data[XL]=='Open field')),
        data['obs_beh_loc_treat_roleplus_num'], np.NaN)
    data['ODCM_roleplus_%s'% col_name]= np.where(data['ODCM_roleplus_%s'% col_name]==1,data['obs_beh_loc_treat_roleplus_sumdur'], np.NaN)
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))), 99999,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XI]=='FLX-males')|(data[XI]=='FLX-females')|(data[XI]=='CTR-females'))),88888,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_roleplus_%s'% col_name]=np.where(data['ODCM_roleplus_%s'% col_name]==99999, np.NaN, data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODCM_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODCM_roleplus_%s'% col_name]==88888), 
        0,data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name]=np.where(data['ODCM_roleplus_%s'% col_name]==88888, np.NaN, data['ODCM_roleplus_%s'% col_name])
    data['ODCM_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODCM_roleplus_%s'% col_name]=np.where(data['ODCM_roleplus_%s'% col_name]== np.NaN,0, data['ODCM_roleplus_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners in total environment
    data['TDW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TDW_roleplus_%s'% col_name]= np.where(data['TDW_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_sumdur'], np.NaN)
    data['TDW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))), 99999,data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Loser')|
            (data[XM]=='Other'))),88888,data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDW_roleplus_%s'% col_name]=np.where(data['TDW_roleplus_%s'% col_name]==99999, np.NaN, data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDW_roleplus_%s'% col_name]==88888), 
        0,data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name]=np.where(data['TDW_roleplus_%s'% col_name]==88888, np.NaN, data['TDW_roleplus_%s'% col_name])
    data['TDW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at losers in total environment
    data['TDL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TDL_roleplus_%s'% col_name]= np.where(data['TDL_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_sumdur'], np.NaN)
    data['TDL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))), 99999,data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Other'))),88888,data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDL_roleplus_%s'% col_name]=np.where(data['TDL_roleplus_%s'% col_name]==99999, np.NaN, data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDL_roleplus_%s'% col_name]==88888), 
        0,data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name]=np.where(data['TDL_roleplus_%s'% col_name]==88888, np.NaN, data['TDL_roleplus_%s'% col_name])
    data['TDL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    
    # Calculate total number of each "social" behavior directed at others in total environment
    data['TDO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')),data['obs_beh_modwinner_roleplus_num'], np.NaN)
    data['TDO_roleplus_%s'% col_name]= np.where(data['TDO_roleplus_%s'% col_name]==1,data['obs_beh_modwinner_roleplus_sumdur'], np.NaN)
    data['TDO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))), 99999,data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&((data[XM]=='Winner')|
            (data[XM]=='Loser'))),88888,data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['TDO_roleplus_%s'% col_name]=np.where(data['TDO_roleplus_%s'% col_name]==99999, np.NaN, data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['TDO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['TDO_roleplus_%s'% col_name]==88888), 
        0,data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name]=np.where(data['TDO_roleplus_%s'% col_name]==88888, np.NaN, data['TDO_roleplus_%s'% col_name])
    data['TDO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)

    # Calculate total number of each "social" behavior directed at winners/loser/others in BURROW
    data['BDW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BDW_roleplus_%s'% col_name]= np.where(data['BDW_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_roleplus_%s'% col_name]=np.where(data['BDW_roleplus_%s'% col_name]==99999, np.NaN, data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDW_roleplus_%s'% col_name]==88888), 
        0,data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name]=np.where(data['BDW_roleplus_%s'% col_name]==88888, np.NaN, data['BDW_roleplus_%s'% col_name])
    data['BDW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDW_roleplus_%s'% col_name]=np.where(data['BDW_roleplus_%s'% col_name]== np.NaN,0, data['BDW_roleplus_%s'% col_name])

    data['BDL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BDL_roleplus_%s'% col_name]= np.where(data['BDL_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_roleplus_%s'% col_name]=np.where(data['BDL_roleplus_%s'% col_name]==99999, np.NaN, data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDL_roleplus_%s'% col_name]==88888), 
        0,data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name]=np.where(data['BDL_roleplus_%s'% col_name]==88888, np.NaN, data['BDL_roleplus_%s'% col_name])
    data['BDL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDL_roleplus_%s'% col_name]=np.where(data['BDL_roleplus_%s'% col_name]== np.NaN,0, data['BDL_roleplus_%s'% col_name])

    data['BDO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Burrow')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['BDO_roleplus_%s'% col_name]= np.where(data['BDO_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        99999,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')),
        88888,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_roleplus_%s'% col_name]=np.where(data['BDO_roleplus_%s'% col_name]==99999, np.NaN, data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['BDO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['BDO_roleplus_%s'% col_name]==88888), 
        0,data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name]=np.where(data['BDO_roleplus_%s'% col_name]==88888, np.NaN, data['BDO_roleplus_%s'% col_name])
    data['BDO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['BDO_roleplus_%s'% col_name]=np.where(data['BDO_roleplus_%s'% col_name]== np.NaN,0, data['BDO_roleplus_%s'% col_name])

    # Calculate total number of each "social" behavior directed at winners/loser/others in open field
    data['ODW_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Winner')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ODW_roleplus_%s'% col_name]= np.where(data['ODW_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))), 99999,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Loser')|(data[XM]=='Other'))),88888,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_roleplus_%s'% col_name]=np.where(data['ODW_roleplus_%s'% col_name]==99999, np.NaN, data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODW_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODW_roleplus_%s'% col_name]==88888), 
        0,data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name]=np.where(data['ODW_roleplus_%s'% col_name]==88888, np.NaN, data['ODW_roleplus_%s'% col_name])
    data['ODW_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODW_roleplus_%s'% col_name]=np.where(data['ODW_roleplus_%s'% col_name]== np.NaN,0, data['ODW_roleplus_%s'% col_name])

    data['ODL_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Loser')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ODL_roleplus_%s'% col_name]= np.where(data['ODL_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))), 99999,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Other'))),88888,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_roleplus_%s'% col_name]=np.where(data['ODL_roleplus_%s'% col_name]==99999, np.NaN, data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODL_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODL_roleplus_%s'% col_name]==88888), 
        0,data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name]=np.where(data['ODL_roleplus_%s'% col_name]==88888, np.NaN, data['ODL_roleplus_%s'% col_name])
    data['ODL_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODL_roleplus_%s'% col_name]=np.where(data['ODL_roleplus_%s'% col_name]== np.NaN,0, data['ODL_roleplus_%s'% col_name])

    data['ODO_roleplus_%s'% col_name]= np.where(((data[O]==col_name)&(data[XM]=='Other')&(data[XL]=='Open field')),
        data['obs_beh_loc_modwinner_roleplus_num'], np.NaN)
    data['ODO_roleplus_%s'% col_name]= np.where(data['ODO_roleplus_%s'% col_name]==1,data['obs_beh_loc_modwinner_roleplus_sumdur'], np.NaN)
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]!=col_name)), 99999,
        data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        99999,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))), 99999,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]!=col_name)), 
        88888,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Burrow')),
        88888,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]= np.where(((data['obs_num_back']==1)&(data[O]==col_name)&(data[XL]=='Open field')&
        ((data[XM]=='Winner')|(data[XM]=='Loser'))),88888,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_roleplus_%s'% col_name]=np.where(data['ODO_roleplus_%s'% col_name]==99999, np.NaN, data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name].fillna(method = "backfill", inplace=True)
    data['ODO_roleplus_%s'% col_name]= np.where(np.logical_and(data['obs_num_back']!=1,data['ODO_roleplus_%s'% col_name]==88888), 
        0,data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name]=np.where(data['ODO_roleplus_%s'% col_name]==88888, np.NaN, data['ODO_roleplus_%s'% col_name])
    data['ODO_roleplus_%s'% col_name].fillna(method = "ffill", inplace=True)
    data['ODO_roleplus_%s'% col_name]=np.where(data['ODO_roleplus_%s'% col_name]== np.NaN,0, data['ODO_roleplus_%s'% col_name])

# Calculate the other behaviors for the social behaviors directed at each type of rat
data['TDFF_roleplus_%s'% EA]=(data['TDFF_roleplus_%s'% BG]+data['TDFF_roleplus_%s'% BD]+data['TDFF_roleplus_%s'% BC])
data['TDFF_roleplus_%s'% EB]=(data['TDFF_roleplus_%s'% BI]+data['TDFF_roleplus_%s'% BBJ])
data['TDFF_roleplus_%s'% EC]=(data['TDFF_roleplus_%s'% BG]+data['TDFF_roleplus_%s'% BD]+data['TDFF_roleplus_%s'% BC]+data['TDFF_roleplus_%s'% BF]+data['TDFF_roleplus_%s'% BI]+data['TDFF_roleplus_%s'% BBJ])
data['TDFF_roleplus_%s'% EF]=(data['TDFF_roleplus_%s'% BM]+data['TDFF_roleplus_%s'% BN]+data['TDFF_roleplus_%s'% BO]+data['TDFF_roleplus_%s'% BP]+data['TDFF_roleplus_%s'% BQ]+data['TDFF_roleplus_%s'% BU]+data['TDFF_roleplus_%s'% BS]+data['TDFF_roleplus_%s'% BR])

data['BDFF_roleplus_%s'% EA]=(data['BDFF_roleplus_%s'% BG]+data['BDFF_roleplus_%s'% BD]+data['BDFF_roleplus_%s'% BC])
data['BDFF_roleplus_%s'% EB]=(data['BDFF_roleplus_%s'% BI]+data['BDFF_roleplus_%s'% BBJ])
data['BDFF_roleplus_%s'% EC]=(data['BDFF_roleplus_%s'% BG]+data['BDFF_roleplus_%s'% BD]+data['BDFF_roleplus_%s'% BC]+data['BDFF_roleplus_%s'% BF]+data['BDFF_roleplus_%s'% BI]+data['BDFF_roleplus_%s'% BBJ])
data['BDFF_roleplus_%s'% EF]=(data['BDFF_roleplus_%s'% BM]+data['BDFF_roleplus_%s'% BN]+data['BDFF_roleplus_%s'% BO]+data['BDFF_roleplus_%s'% BP]+data['BDFF_roleplus_%s'% BQ]+data['BDFF_roleplus_%s'% BU]+data['BDFF_roleplus_%s'% BS]+data['BDFF_roleplus_%s'% BR])

data['ODFF_roleplus_%s'% EA]=(data['ODFF_roleplus_%s'% BG]+data['ODFF_roleplus_%s'% BD]+data['ODFF_roleplus_%s'% BC])
data['ODFF_roleplus_%s'% EB]=(data['ODFF_roleplus_%s'% BI]+data['ODFF_roleplus_%s'% BBJ])
data['ODFF_roleplus_%s'% EC]=(data['ODFF_roleplus_%s'% BG]+data['ODFF_roleplus_%s'% BD]+data['ODFF_roleplus_%s'% BC]+data['ODFF_roleplus_%s'% BF]+data['ODFF_roleplus_%s'% BI]+data['ODFF_roleplus_%s'% BBJ])
data['ODFF_roleplus_%s'% EF]=(data['ODFF_roleplus_%s'% BM]+data['ODFF_roleplus_%s'% BN]+data['ODFF_roleplus_%s'% BO]+data['ODFF_roleplus_%s'% BP]+data['ODFF_roleplus_%s'% BQ]+data['ODFF_roleplus_%s'% BU]+data['ODFF_roleplus_%s'% BS]+data['ODFF_roleplus_%s'% BR])

data['TDCF_roleplus_%s'% EA]=(data['TDCF_roleplus_%s'% BG]+data['TDCF_roleplus_%s'% BD]+data['TDCF_roleplus_%s'% BC])
data['TDCF_roleplus_%s'% EB]=(data['TDCF_roleplus_%s'% BI]+data['TDCF_roleplus_%s'% BBJ])
data['TDCF_roleplus_%s'% EC]=(data['TDCF_roleplus_%s'% BG]+data['TDCF_roleplus_%s'% BD]+data['TDCF_roleplus_%s'% BC]+data['TDCF_roleplus_%s'% BF]+data['TDCF_roleplus_%s'% BI]+data['TDCF_roleplus_%s'% BBJ])
data['TDCF_roleplus_%s'% EF]=(data['TDCF_roleplus_%s'% BM]+data['TDCF_roleplus_%s'% BN]+data['TDCF_roleplus_%s'% BO]+data['TDCF_roleplus_%s'% BP]+data['TDCF_roleplus_%s'% BQ]+data['TDCF_roleplus_%s'% BU]+data['TDCF_roleplus_%s'% BS]+data['TDCF_roleplus_%s'% BR])

data['BDCF_roleplus_%s'% EA]=(data['BDCF_roleplus_%s'% BG]+data['BDCF_roleplus_%s'% BD]+data['BDCF_roleplus_%s'% BC])
data['BDCF_roleplus_%s'% EB]=(data['BDCF_roleplus_%s'% BI]+data['BDCF_roleplus_%s'% BBJ])
data['BDCF_roleplus_%s'% EC]=(data['BDCF_roleplus_%s'% BG]+data['BDCF_roleplus_%s'% BD]+data['BDCF_roleplus_%s'% BC]+data['BDCF_roleplus_%s'% BF]+data['BDCF_roleplus_%s'% BI]+data['BDCF_roleplus_%s'% BBJ])
data['BDCF_roleplus_%s'% EF]=(data['BDCF_roleplus_%s'% BM]+data['BDCF_roleplus_%s'% BN]+data['BDCF_roleplus_%s'% BO]+data['BDCF_roleplus_%s'% BP]+data['BDCF_roleplus_%s'% BQ]+data['BDCF_roleplus_%s'% BU]+data['BDCF_roleplus_%s'% BS]+data['BDCF_roleplus_%s'% BR])

data['ODCF_roleplus_%s'% EA]=(data['ODCF_roleplus_%s'% BG]+data['ODCF_roleplus_%s'% BD]+data['ODCF_roleplus_%s'% BC])
data['ODCF_roleplus_%s'% EB]=(data['ODCF_roleplus_%s'% BI]+data['ODCF_roleplus_%s'% BBJ])
data['ODCF_roleplus_%s'% EC]=(data['ODCF_roleplus_%s'% BG]+data['ODCF_roleplus_%s'% BD]+data['ODCF_roleplus_%s'% BC]+data['ODCF_roleplus_%s'% BF]+data['ODCF_roleplus_%s'% BI]+data['ODCF_roleplus_%s'% BBJ])
data['ODCF_roleplus_%s'% EF]=(data['ODCF_roleplus_%s'% BM]+data['ODCF_roleplus_%s'% BN]+data['ODCF_roleplus_%s'% BO]+data['ODCF_roleplus_%s'% BP]+data['ODCF_roleplus_%s'% BQ]+data['ODCF_roleplus_%s'% BU]+data['ODCF_roleplus_%s'% BS]+data['ODCF_roleplus_%s'% BR])

data['TDFM_roleplus_%s'% EA]=(data['TDFM_roleplus_%s'% BG]+data['TDFM_roleplus_%s'% BD]+data['TDFM_roleplus_%s'% BC])
data['TDFM_roleplus_%s'% EB]=(data['TDFM_roleplus_%s'% BI]+data['TDFM_roleplus_%s'% BBJ])
data['TDFM_roleplus_%s'% EC]=(data['TDFM_roleplus_%s'% BG]+data['TDFM_roleplus_%s'% BD]+data['TDFM_roleplus_%s'% BC]+data['TDFM_roleplus_%s'% BF]+data['TDFM_roleplus_%s'% BI]+data['TDFM_roleplus_%s'% BBJ])
data['TDFM_roleplus_%s'% EF]=(data['TDFM_roleplus_%s'% BM]+data['TDFM_roleplus_%s'% BN]+data['TDFM_roleplus_%s'% BO]+data['TDFM_roleplus_%s'% BP]+data['TDFM_roleplus_%s'% BQ]+data['TDFM_roleplus_%s'% BU]+data['TDFM_roleplus_%s'% BS]+data['TDFM_roleplus_%s'% BR])

data['BDFM_roleplus_%s'% EA]=(data['BDFM_roleplus_%s'% BG]+data['BDFM_roleplus_%s'% BD]+data['BDFM_roleplus_%s'% BC])
data['BDFM_roleplus_%s'% EB]=(data['BDFM_roleplus_%s'% BI]+data['BDFM_roleplus_%s'% BBJ])
data['BDFM_roleplus_%s'% EC]=(data['BDFM_roleplus_%s'% BG]+data['BDFM_roleplus_%s'% BD]+data['BDFM_roleplus_%s'% BC]+data['BDFM_roleplus_%s'% BF]+data['BDFM_roleplus_%s'% BI]+data['BDFM_roleplus_%s'% BBJ])
data['BDFM_roleplus_%s'% EF]=(data['BDFM_roleplus_%s'% BM]+data['BDFM_roleplus_%s'% BN]+data['BDFM_roleplus_%s'% BO]+data['BDFM_roleplus_%s'% BP]+data['BDFM_roleplus_%s'% BQ]+data['BDFM_roleplus_%s'% BU]+data['BDFM_roleplus_%s'% BS]+data['BDFM_roleplus_%s'% BR])

data['ODFM_roleplus_%s'% EA]=(data['ODFM_roleplus_%s'% BG]+data['ODFM_roleplus_%s'% BD]+data['ODFM_roleplus_%s'% BC])
data['ODFM_roleplus_%s'% EB]=(data['ODFM_roleplus_%s'% BI]+data['ODFM_roleplus_%s'% BBJ])
data['ODFM_roleplus_%s'% EC]=(data['ODFM_roleplus_%s'% BG]+data['ODFM_roleplus_%s'% BD]+data['ODFM_roleplus_%s'% BC]+data['ODFM_roleplus_%s'% BF]+data['ODFM_roleplus_%s'% BI]+data['ODFM_roleplus_%s'% BBJ])
data['ODFM_roleplus_%s'% EF]=(data['ODFM_roleplus_%s'% BM]+data['ODFM_roleplus_%s'% BN]+data['ODFM_roleplus_%s'% BO]+data['ODFM_roleplus_%s'% BP]+data['ODFM_roleplus_%s'% BQ]+data['ODFM_roleplus_%s'% BU]+data['ODFM_roleplus_%s'% BS]+data['ODFM_roleplus_%s'% BR])

data['TDCM_roleplus_%s'% EA]=(data['TDCM_roleplus_%s'% BG]+data['TDCM_roleplus_%s'% BD]+data['TDCM_roleplus_%s'% BC])
data['TDCM_roleplus_%s'% EB]=(data['TDCM_roleplus_%s'% BI]+data['TDCM_roleplus_%s'% BBJ])
data['TDCM_roleplus_%s'% EC]=(data['TDCM_roleplus_%s'% BG]+data['TDCM_roleplus_%s'% BD]+data['TDCM_roleplus_%s'% BC]+data['TDCM_roleplus_%s'% BF]+data['TDCM_roleplus_%s'% BI]+data['TDCM_roleplus_%s'% BBJ])
data['TDCM_roleplus_%s'% EF]=(data['TDCM_roleplus_%s'% BM]+data['TDCM_roleplus_%s'% BN]+data['TDCM_roleplus_%s'% BO]+data['TDCM_roleplus_%s'% BP]+data['TDCM_roleplus_%s'% BQ]+data['TDCM_roleplus_%s'% BU]+data['TDCM_roleplus_%s'% BS]+data['TDCM_roleplus_%s'% BR])

data['BDCM_roleplus_%s'% EA]=(data['BDCM_roleplus_%s'% BG]+data['BDCM_roleplus_%s'% BD]+data['BDCM_roleplus_%s'% BC])
data['BDCM_roleplus_%s'% EB]=(data['BDCM_roleplus_%s'% BI]+data['BDCM_roleplus_%s'% BBJ])
data['BDCM_roleplus_%s'% EC]=(data['BDCM_roleplus_%s'% BG]+data['BDCM_roleplus_%s'% BD]+data['BDCM_roleplus_%s'% BC]+data['BDCM_roleplus_%s'% BF]+data['BDCM_roleplus_%s'% BI]+data['BDCM_roleplus_%s'% BBJ])
data['BDCM_roleplus_%s'% EF]=(data['BDCM_roleplus_%s'% BM]+data['BDCM_roleplus_%s'% BN]+data['BDCM_roleplus_%s'% BO]+data['BDCM_roleplus_%s'% BP]+data['BDCM_roleplus_%s'% BQ]+data['BDCM_roleplus_%s'% BU]+data['BDCM_roleplus_%s'% BS]+data['BDCM_roleplus_%s'% BR])

data['ODCM_roleplus_%s'% EA]=(data['ODCM_roleplus_%s'% BG]+data['ODCM_roleplus_%s'% BD]+data['ODCM_roleplus_%s'% BC])
data['ODCM_roleplus_%s'% EB]=(data['ODCM_roleplus_%s'% BI]+data['ODCM_roleplus_%s'% BBJ])
data['ODCM_roleplus_%s'% EC]=(data['ODCM_roleplus_%s'% BG]+data['ODCM_roleplus_%s'% BD]+data['ODCM_roleplus_%s'% BC]+data['ODCM_roleplus_%s'% BF]+data['ODCM_roleplus_%s'% BI]+data['ODCM_roleplus_%s'% BBJ])
data['ODCM_roleplus_%s'% EF]=(data['ODCM_roleplus_%s'% BM]+data['ODCM_roleplus_%s'% BN]+data['ODCM_roleplus_%s'% BO]+data['ODCM_roleplus_%s'% BP]+data['ODCM_roleplus_%s'% BQ]+data['ODCM_roleplus_%s'% BU]+data['ODCM_roleplus_%s'% BS]+data['ODCM_roleplus_%s'% BR])
   
data['TDW_roleplus_%s'% EA]=(data['TDW_roleplus_%s'% BG]+data['TDW_roleplus_%s'% BD]+data['TDW_roleplus_%s'% BC])
data['TDW_roleplus_%s'% EB]=(data['TDW_roleplus_%s'% BI]+data['TDW_roleplus_%s'% BBJ])
data['TDW_roleplus_%s'% EC]=(data['TDW_roleplus_%s'% BG]+data['TDW_roleplus_%s'% BD]+data['TDW_roleplus_%s'% BC]+data['TDW_roleplus_%s'% BF]+data['TDW_roleplus_%s'% BI]+data['TDW_roleplus_%s'% BBJ])
data['TDW_roleplus_%s'% EF]=(data['TDW_roleplus_%s'% BM]+data['TDW_roleplus_%s'% BN]+data['TDW_roleplus_%s'% BO]+data['TDW_roleplus_%s'% BP]+data['TDW_roleplus_%s'% BQ]+data['TDW_roleplus_%s'% BU]+data['TDW_roleplus_%s'% BS]+data['TDW_roleplus_%s'% BR])

data['BDW_roleplus_%s'% EA]=(data['BDW_roleplus_%s'% BG]+data['BDW_roleplus_%s'% BD]+data['BDW_roleplus_%s'% BC])
data['BDW_roleplus_%s'% EB]=(data['BDW_roleplus_%s'% BI]+data['BDW_roleplus_%s'% BBJ])
data['BDW_roleplus_%s'% EC]=(data['BDW_roleplus_%s'% BG]+data['BDW_roleplus_%s'% BD]+data['BDW_roleplus_%s'% BC]+data['BDW_roleplus_%s'% BF]+data['BDW_roleplus_%s'% BI]+data['BDW_roleplus_%s'% BBJ])
data['BDW_roleplus_%s'% EF]=(data['BDW_roleplus_%s'% BM]+data['BDW_roleplus_%s'% BN]+data['BDW_roleplus_%s'% BO]+data['BDW_roleplus_%s'% BP]+data['BDW_roleplus_%s'% BQ]+data['BDW_roleplus_%s'% BU]+data['BDW_roleplus_%s'% BS]+data['BDW_roleplus_%s'% BR])

data['ODW_roleplus_%s'% EA]=(data['ODW_roleplus_%s'% BG]+data['ODW_roleplus_%s'% BD]+data['ODW_roleplus_%s'% BC])
data['ODW_roleplus_%s'% EB]=(data['ODW_roleplus_%s'% BI]+data['ODW_roleplus_%s'% BBJ])
data['ODW_roleplus_%s'% EC]=(data['ODW_roleplus_%s'% BG]+data['ODW_roleplus_%s'% BD]+data['ODW_roleplus_%s'% BC]+data['ODW_roleplus_%s'% BF]+data['ODW_roleplus_%s'% BI]+data['ODW_roleplus_%s'% BBJ])
data['ODW_roleplus_%s'% EF]=(data['ODW_roleplus_%s'% BM]+data['ODW_roleplus_%s'% BN]+data['ODW_roleplus_%s'% BO]+data['ODW_roleplus_%s'% BP]+data['ODW_roleplus_%s'% BQ]+data['ODW_roleplus_%s'% BU]+data['ODW_roleplus_%s'% BS]+data['ODW_roleplus_%s'% BR])

data['TDL_roleplus_%s'% EA]=(data['TDL_roleplus_%s'% BG]+data['TDL_roleplus_%s'% BD]+data['TDL_roleplus_%s'% BC])
data['TDL_roleplus_%s'% EB]=(data['TDL_roleplus_%s'% BI]+data['TDL_roleplus_%s'% BBJ])
data['TDL_roleplus_%s'% EC]=(data['TDL_roleplus_%s'% BG]+data['TDL_roleplus_%s'% BD]+data['TDL_roleplus_%s'% BC]+data['TDL_roleplus_%s'% BF]+data['TDL_roleplus_%s'% BI]+data['TDL_roleplus_%s'% BBJ])
data['TDL_roleplus_%s'% EF]=(data['TDL_roleplus_%s'% BM]+data['TDL_roleplus_%s'% BN]+data['TDL_roleplus_%s'% BO]+data['TDL_roleplus_%s'% BP]+data['TDL_roleplus_%s'% BQ]+data['TDL_roleplus_%s'% BU]+data['TDL_roleplus_%s'% BS]+data['TDL_roleplus_%s'% BR])

data['BDL_roleplus_%s'% EA]=(data['BDL_roleplus_%s'% BG]+data['BDL_roleplus_%s'% BD]+data['BDL_roleplus_%s'% BC])
data['BDL_roleplus_%s'% EB]=(data['BDL_roleplus_%s'% BI]+data['BDL_roleplus_%s'% BBJ])
data['BDL_roleplus_%s'% EC]=(data['BDL_roleplus_%s'% BG]+data['BDL_roleplus_%s'% BD]+data['BDL_roleplus_%s'% BC]+data['BDL_roleplus_%s'% BF]+data['BDL_roleplus_%s'% BI]+data['BDL_roleplus_%s'% BBJ])
data['BDL_roleplus_%s'% EF]=(data['BDL_roleplus_%s'% BM]+data['BDL_roleplus_%s'% BN]+data['BDL_roleplus_%s'% BO]+data['BDL_roleplus_%s'% BP]+data['BDL_roleplus_%s'% BQ]+data['BDL_roleplus_%s'% BU]+data['BDL_roleplus_%s'% BS]+data['BDL_roleplus_%s'% BR])

data['ODL_roleplus_%s'% EA]=(data['ODL_roleplus_%s'% BG]+data['ODL_roleplus_%s'% BD]+data['ODL_roleplus_%s'% BC])
data['ODL_roleplus_%s'% EB]=(data['ODL_roleplus_%s'% BI]+data['ODL_roleplus_%s'% BBJ])
data['ODL_roleplus_%s'% EC]=(data['ODL_roleplus_%s'% BG]+data['ODL_roleplus_%s'% BD]+data['ODL_roleplus_%s'% BC]+data['ODL_roleplus_%s'% BF]+data['ODL_roleplus_%s'% BI]+data['ODL_roleplus_%s'% BBJ])
data['ODL_roleplus_%s'% EF]=(data['ODL_roleplus_%s'% BM]+data['ODL_roleplus_%s'% BN]+data['ODL_roleplus_%s'% BO]+data['ODL_roleplus_%s'% BP]+data['ODL_roleplus_%s'% BQ]+data['ODL_roleplus_%s'% BU]+data['ODL_roleplus_%s'% BS]+data['ODL_roleplus_%s'% BR])

data['TDO_roleplus_%s'% EA]=(data['TDO_roleplus_%s'% BG]+data['TDO_roleplus_%s'% BD]+data['TDO_roleplus_%s'% BC])
data['TDO_roleplus_%s'% EB]=(data['TDO_roleplus_%s'% BI]+data['TDO_roleplus_%s'% BBJ])
data['TDO_roleplus_%s'% EC]=(data['TDO_roleplus_%s'% BG]+data['TDO_roleplus_%s'% BD]+data['TDO_roleplus_%s'% BC]+data['TDO_roleplus_%s'% BF]+data['TDO_roleplus_%s'% BI]+data['TDO_roleplus_%s'% BBJ])
data['TDO_roleplus_%s'% EF]=(data['TDO_roleplus_%s'% BM]+data['TDO_roleplus_%s'% BN]+data['TDO_roleplus_%s'% BO]+data['TDO_roleplus_%s'% BP]+data['TDO_roleplus_%s'% BQ]+data['TDO_roleplus_%s'% BU]+data['TDO_roleplus_%s'% BS]+data['TDO_roleplus_%s'% BR])

data['BDO_roleplus_%s'% EA]=(data['BDO_roleplus_%s'% BG]+data['BDO_roleplus_%s'% BD]+data['BDO_roleplus_%s'% BC])
data['BDO_roleplus_%s'% EB]=(data['BDO_roleplus_%s'% BI]+data['BDO_roleplus_%s'% BBJ])
data['BDO_roleplus_%s'% EC]=(data['BDO_roleplus_%s'% BG]+data['BDO_roleplus_%s'% BD]+data['BDO_roleplus_%s'% BC]+data['BDO_roleplus_%s'% BF]+data['BDO_roleplus_%s'% BI]+data['BDO_roleplus_%s'% BBJ])
data['BDO_roleplus_%s'% EF]=(data['BDO_roleplus_%s'% BM]+data['BDO_roleplus_%s'% BN]+data['BDO_roleplus_%s'% BO]+data['BDO_roleplus_%s'% BP]+data['BDO_roleplus_%s'% BQ]+data['BDO_roleplus_%s'% BU]+data['BDO_roleplus_%s'% BS]+data['BDO_roleplus_%s'% BR])

data['ODO_roleplus_%s'% EA]=(data['ODO_roleplus_%s'% BG]+data['ODO_roleplus_%s'% BD]+data['ODO_roleplus_%s'% BC])
data['ODO_roleplus_%s'% EB]=(data['ODO_roleplus_%s'% BI]+data['ODO_roleplus_%s'% BBJ])
data['ODO_roleplus_%s'% EC]=(data['ODO_roleplus_%s'% BG]+data['ODO_roleplus_%s'% BD]+data['ODO_roleplus_%s'% BC]+data['ODO_roleplus_%s'% BF]+data['ODO_roleplus_%s'% BI]+data['ODO_roleplus_%s'% BBJ])
data['ODO_roleplus_%s'% EF]=(data['ODO_roleplus_%s'% BM]+data['ODO_roleplus_%s'% BN]+data['ODO_roleplus_%s'% BO]+data['ODO_roleplus_%s'% BP]+data['ODO_roleplus_%s'% BQ]+data['ODO_roleplus_%s'% BU]+data['ODO_roleplus_%s'% BS]+data['ODO_roleplus_%s'% BR])


# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDCR_roleplus_%s'% col_name]=(data['TDCF_roleplus_%s'% col_name]+data['TDCM_roleplus_%s'% col_name])
    data['TDFR_roleplus_%s'% col_name]=(data['TDFF_roleplus_%s'% col_name]+data['TDFM_roleplus_%s'% col_name])

data['TDCR_roleplus_%s'% EA]=(data['TDCF_roleplus_%s'% EA]+data['TDCM_roleplus_%s'% EA])
data['TDFR_roleplus_%s'% EA]=(data['TDFF_roleplus_%s'% EA]+data['TDFM_roleplus_%s'% EA])
data['TDCR_roleplus_%s'% EB]=(data['TDCF_roleplus_%s'% EB]+data['TDCM_roleplus_%s'% EB])
data['TDFR_roleplus_%s'% EB]=(data['TDFF_roleplus_%s'% EB]+data['TDFM_roleplus_%s'% EB])
data['TDCR_roleplus_%s'% EC]=(data['TDCF_roleplus_%s'% EC]+data['TDCM_roleplus_%s'% EC])
data['TDFR_roleplus_%s'% EC]=(data['TDFF_roleplus_%s'% EC]+data['TDFM_roleplus_%s'% EC])
data['TDCR_roleplus_%s'% EF]=(data['TDCF_roleplus_%s'% EF]+data['TDCM_roleplus_%s'% EF])
data['TDFR_roleplus_%s'% EF]=(data['TDFF_roleplus_%s'% EF]+data['TDFM_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in total envirODment
for position, col_name in enumerate(list_behaviors_social):
    data['TDM_roleplus_%s'% col_name]=(data['TDCM_roleplus_%s'% col_name]+data['TDFM_roleplus_%s'% col_name])
    data['TDF_roleplus_%s'% col_name]=(data['TDFF_roleplus_%s'% col_name]+data['TDCF_roleplus_%s'% col_name])

data['TDM_roleplus_%s'% EA]=(data['TDCM_roleplus_%s'% EA]+data['TDFM_roleplus_%s'% EA])
data['TDF_roleplus_%s'% EA]=(data['TDFF_roleplus_%s'% EA]+data['TDCF_roleplus_%s'% EA])
data['TDM_roleplus_%s'% EB]=(data['TDCM_roleplus_%s'% EB]+data['TDFM_roleplus_%s'% EB])
data['TDF_roleplus_%s'% EB]=(data['TDFF_roleplus_%s'% EB]+data['TDCF_roleplus_%s'% EB])
data['TDM_roleplus_%s'% EC]=(data['TDCM_roleplus_%s'% EC]+data['TDFM_roleplus_%s'% EC])
data['TDF_roleplus_%s'% EC]=(data['TDFF_roleplus_%s'% EC]+data['TDCF_roleplus_%s'% EC])
data['TDM_roleplus_%s'% EF]=(data['TDCM_roleplus_%s'% EF]+data['TDFM_roleplus_%s'% EF])
data['TDF_roleplus_%s'% EF]=(data['TDFF_roleplus_%s'% EF]+data['TDCF_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in burrow
for position, col_name in enumerate(list_behaviors_social):    
    data['BDCR_roleplus_%s'% col_name]=(data['BDCF_roleplus_%s'% col_name]+data['BDCM_roleplus_%s'% col_name])
    data['BDFR_roleplus_%s'% col_name]=(data['BDFF_roleplus_%s'% col_name]+data['BDFM_roleplus_%s'% col_name])

data['BDCR_roleplus_%s'% EA]=(data['BDCF_roleplus_%s'% EA]+data['BDCM_roleplus_%s'% EA])
data['BDFR_roleplus_%s'% EA]=(data['BDFF_roleplus_%s'% EA]+data['BDFM_roleplus_%s'% EA])
data['BDCR_roleplus_%s'% EB]=(data['BDCF_roleplus_%s'% EB]+data['BDCM_roleplus_%s'% EB])
data['BDFR_roleplus_%s'% EB]=(data['BDFF_roleplus_%s'% EB]+data['BDFM_roleplus_%s'% EB])
data['BDCR_roleplus_%s'% EC]=(data['BDCF_roleplus_%s'% EC]+data['BDCM_roleplus_%s'% EC])
data['BDFR_roleplus_%s'% EC]=(data['BDFF_roleplus_%s'% EC]+data['BDFM_roleplus_%s'% EC])
data['BDCR_roleplus_%s'% EF]=(data['BDCF_roleplus_%s'% EF]+data['BDCM_roleplus_%s'% EF])
data['BDFR_roleplus_%s'% EF]=(data['BDFF_roleplus_%s'% EF]+data['BDFM_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in burrow
for position, col_name in enumerate(list_behaviors_social): 
    data['BDM_roleplus_%s'% col_name]=(data['BDCM_roleplus_%s'% col_name]+data['BDFM_roleplus_%s'% col_name])
    data['BDF_roleplus_%s'% col_name]=(data['BDFF_roleplus_%s'% col_name]+data['BDCF_roleplus_%s'% col_name])

data['BDM_roleplus_%s'% EA]=(data['BDCM_roleplus_%s'% EA]+data['BDFM_roleplus_%s'% EA])
data['BDF_roleplus_%s'% EA]=(data['BDFF_roleplus_%s'% EA]+data['BDCF_roleplus_%s'% EA])
data['BDM_roleplus_%s'% EB]=(data['BDCM_roleplus_%s'% EB]+data['BDFM_roleplus_%s'% EB])
data['BDF_roleplus_%s'% EB]=(data['BDFF_roleplus_%s'% EB]+data['BDCF_roleplus_%s'% EB])
data['BDM_roleplus_%s'% EC]=(data['BDCM_roleplus_%s'% EC]+data['BDFM_roleplus_%s'% EC])
data['BDF_roleplus_%s'% EC]=(data['BDFF_roleplus_%s'% EC]+data['BDCF_roleplus_%s'% EC])
data['BDM_roleplus_%s'% EF]=(data['BDCM_roleplus_%s'% EF]+data['BDFM_roleplus_%s'% EF])
data['BDF_roleplus_%s'% EF]=(data['BDFF_roleplus_%s'% EF]+data['BDCF_roleplus_%s'% EF])

# Calculate total number of each "social" behavior directed at CTR-rats and FLX-rats
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODCR_roleplus_%s'% col_name]=(data['ODCF_roleplus_%s'% col_name]+data['ODCM_roleplus_%s'% col_name])
    data['ODFR_roleplus_%s'% col_name]=(data['ODFF_roleplus_%s'% col_name]+data['ODFM_roleplus_%s'% col_name])

data['ODCR_roleplus_%s'% EA]=(data['ODCF_roleplus_%s'% EA]+data['ODCM_roleplus_%s'% EA])
data['ODFR_roleplus_%s'% EA]=(data['ODFF_roleplus_%s'% EA]+data['ODFM_roleplus_%s'% EA])
data['ODCR_roleplus_%s'% EB]=(data['ODCF_roleplus_%s'% EB]+data['ODCM_roleplus_%s'% EB])
data['ODFR_roleplus_%s'% EB]=(data['ODFF_roleplus_%s'% EB]+data['ODFM_roleplus_%s'% EB])
data['ODCR_roleplus_%s'% EC]=(data['ODCF_roleplus_%s'% EC]+data['ODCM_roleplus_%s'% EC])
data['ODFR_roleplus_%s'% EC]=(data['ODFF_roleplus_%s'% EC]+data['ODFM_roleplus_%s'% EC])
data['ODCR_roleplus_%s'% EF]=(data['ODCF_roleplus_%s'% EF]+data['ODCM_roleplus_%s'% EF])
data['ODFR_roleplus_%s'% EF]=(data['ODFF_roleplus_%s'% EF]+data['ODFM_roleplus_%s'% EF])


# Calculate total number of each "social" behavior directed at MALES and FEMALES
# in Open field
for position, col_name in enumerate(list_behaviors_social): 
    data['ODM_roleplus_%s'% col_name]=(data['ODCM_roleplus_%s'% col_name]+data['ODFM_roleplus_%s'% col_name])
    data['ODF_roleplus_%s'% col_name]=(data['ODFF_roleplus_%s'% col_name]+data['ODCF_roleplus_%s'% col_name])

data['ODM_roleplus_%s'% EA]=(data['ODCM_roleplus_%s'% EA]+data['ODFM_roleplus_%s'% EA])
data['ODF_roleplus_%s'% EA]=(data['ODFF_roleplus_%s'% EA]+data['ODCF_roleplus_%s'% EA])
data['ODM_roleplus_%s'% EB]=(data['ODCM_roleplus_%s'% EB]+data['ODFM_roleplus_%s'% EB])
data['ODF_roleplus_%s'% EB]=(data['ODFF_roleplus_%s'% EB]+data['ODCF_roleplus_%s'% EB])
data['ODM_roleplus_%s'% EC]=(data['ODCM_roleplus_%s'% EC]+data['ODFM_roleplus_%s'% EC])
data['ODF_roleplus_%s'% EC]=(data['ODFF_roleplus_%s'% EC]+data['ODCF_roleplus_%s'% EC])
data['ODM_roleplus_%s'% EF]=(data['ODCM_roleplus_%s'% EF]+data['ODFM_roleplus_%s'% EF])
data['ODF_roleplus_%s'% EF]=(data['ODFF_roleplus_%s'% EF]+data['ODCF_roleplus_%s'% EF])

## now save the data frame to excel
#writer4 = pd.ExcelWriter(out_path4, engine='xlsxwriter')
#data.to_excel(writer4, sheet_name='data')
#writer4.save()
#writer4.close()
 
         
## now save the data frame to excel
data.to_csv("HN002 raw data.csv")

## Delete the rows without ratID
#data= data.dropna(axis=0, subset=[U])

# Calculate the results per rat and write to a new dataframe  
results_fight=data.groupby('ratID_Fight').max()
results_role=data.groupby('ratID_Fight_role').max()
results_roleplus=data.groupby('ratID_Fight_roleplus').max()

# Make excel sheets with relevant information
results_Total_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results): 
    results_Total_fight['TD_%s'% col_name]=results_fight['TD_%s'% col_name].copy()
    results_Total_fight['TN_%s'% col_name]=results_fight['TN_%s'% col_name].copy()

results_OF_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):    
    results_OF_fight['OD_%s'% col_name]=results_fight['OD_%s'% col_name].copy()
    results_OF_fight['ON_%s'% col_name]=results_fight['ON_%s'% col_name].copy()

results_Burrow_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):
    results_Burrow_fight['BD_%s'% col_name]=results_fight['BD_%s'% col_name].copy()
    results_Burrow_fight['BN_%s'% col_name]=results_fight['BN_%s'% col_name].copy()
    
results_Total_fight.columns = results_Total_fight.columns.str.replace(' ', '')
results_OF_fight.columns = results_OF_fight.columns.str.replace(' ', '')
results_Burrow_fight.columns = results_Burrow_fight.columns.str.replace(' ', '')

results_Total_fight.columns = results_Total_fight.columns.str.replace('/', '')
results_OF_fight.columns = results_OF_fight.columns.str.replace('/', '')
results_Burrow_fight.columns = results_Burrow_fight.columns.str.replace('/', '')

results_Total_fight.columns = results_Total_fight.columns.str.replace('-', '')
results_OF_fight.columns = results_OF_fight.columns.str.replace('-', '')
results_Burrow_fight.columns = results_Burrow_fight.columns.str.replace('-', '')

results_TN_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_mod_fight['TNM_%s'% col_name]=results_fight['TNM_%s'% col_name].copy()
    results_TN_mod_fight['TNF_%s'% col_name]=results_fight['TNF_%s'% col_name].copy()
    results_TN_mod_fight['TNCR_%s'% col_name]=results_fight['TNCR_%s'% col_name].copy()
    results_TN_mod_fight['TNFR_%s'% col_name]=results_fight['TNFR_%s'% col_name].copy()       
    results_TN_mod_fight['TNW_%s'% col_name]=results_fight['TNW_%s'% col_name].copy()       
    results_TN_mod_fight['TNL_%s'% col_name]=results_fight['TNL_%s'% col_name].copy()       
    results_TN_mod_fight['TNO_%s'% col_name]=results_fight['TNO_%s'% col_name].copy()       

results_ON_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_ON_mod_fight['ONM_%s'% col_name]=results_fight['ONM_%s'% col_name].copy()
    results_ON_mod_fight['ONF_%s'% col_name]=results_fight['ONF_%s'% col_name].copy()
    results_ON_mod_fight['ONCR_%s'% col_name]=results_fight['ONCR_%s'% col_name].copy()
    results_ON_mod_fight['ONFR_%s'% col_name]=results_fight['ONFR_%s'% col_name].copy() 
    results_ON_mod_fight['ONW_%s'% col_name]=results_fight['ONW_%s'% col_name].copy()       
    results_ON_mod_fight['ONL_%s'% col_name]=results_fight['ONL_%s'% col_name].copy()       
    results_ON_mod_fight['ONO_%s'% col_name]=results_fight['ONO_%s'% col_name].copy()       

results_BN_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BN_mod_fight['BNM_%s'% col_name]=results_fight['BNM_%s'% col_name].copy()
    results_BN_mod_fight['BNF_%s'% col_name]=results_fight['BNF_%s'% col_name].copy()
    results_BN_mod_fight['BNCR_%s'% col_name]=results_fight['BNCR_%s'% col_name].copy()
    results_BN_mod_fight['BNFR_%s'% col_name]=results_fight['BNFR_%s'% col_name].copy() 
    results_BN_mod_fight['BNW_%s'% col_name]=results_fight['BNW_%s'% col_name].copy()       
    results_BN_mod_fight['BNL_%s'% col_name]=results_fight['BNL_%s'% col_name].copy()       
    results_BN_mod_fight['BNO_%s'% col_name]=results_fight['BNO_%s'% col_name].copy()       
    
results_TD_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_mod_fight['TDM_%s'% col_name]=results_fight['TDM_%s'% col_name].copy()
    results_TD_mod_fight['TDF_%s'% col_name]=results_fight['TDF_%s'% col_name].copy()
    results_TD_mod_fight['TDCR_%s'% col_name]=results_fight['TDCR_%s'% col_name].copy()
    results_TD_mod_fight['TDFR_%s'% col_name]=results_fight['TDFR_%s'% col_name].copy()       
    results_TD_mod_fight['TDW_%s'% col_name]=results_fight['TDW_%s'% col_name].copy()       
    results_TD_mod_fight['TDL_%s'% col_name]=results_fight['TDL_%s'% col_name].copy()       
    results_TD_mod_fight['TDO_%s'% col_name]=results_fight['TDO_%s'% col_name].copy()       

results_OD_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_OD_mod_fight['ODM_%s'% col_name]=results_fight['ODM_%s'% col_name].copy()
    results_OD_mod_fight['ODF_%s'% col_name]=results_fight['ODF_%s'% col_name].copy()
    results_OD_mod_fight['ODCR_%s'% col_name]=results_fight['ODCR_%s'% col_name].copy()
    results_OD_mod_fight['ODFR_%s'% col_name]=results_fight['ODFR_%s'% col_name].copy() 
    results_OD_mod_fight['ODW_%s'% col_name]=results_fight['ODW_%s'% col_name].copy()       
    results_OD_mod_fight['ODL_%s'% col_name]=results_fight['ODL_%s'% col_name].copy()       
    results_OD_mod_fight['ODO_%s'% col_name]=results_fight['ODO_%s'% col_name].copy()       

results_BD_mod_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BD_mod_fight['BDM_%s'% col_name]=results_fight['BDM_%s'% col_name].copy()
    results_BD_mod_fight['BDF_%s'% col_name]=results_fight['BDF_%s'% col_name].copy()
    results_BD_mod_fight['BDCR_%s'% col_name]=results_fight['BDCR_%s'% col_name].copy()
    results_BD_mod_fight['BDFR_%s'% col_name]=results_fight['BDFR_%s'% col_name].copy() 
    results_BD_mod_fight['BDW_%s'% col_name]=results_fight['BDW_%s'% col_name].copy()       
    results_BD_mod_fight['BDL_%s'% col_name]=results_fight['BDL_%s'% col_name].copy()       
    results_BD_mod_fight['BDO_%s'% col_name]=results_fight['BDO_%s'% col_name].copy()       

results_TN_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_modtreat_fight['TNCF_%s'% col_name]=results_fight['TNCF_%s'% col_name].copy()
    results_TN_modtreat_fight['TNFF_%s'% col_name]=results_fight['TNFF_%s'% col_name].copy()
    results_TN_modtreat_fight['TNCM_%s'% col_name]=results_fight['TNCM_%s'% col_name].copy()
    results_TN_modtreat_fight['TNFM_%s'% col_name]=results_fight['TNFM_%s'% col_name].copy()       

results_ON_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_ON_modtreat_fight['ONCF_%s'% col_name]=results_fight['ONCF_%s'% col_name].copy()
    results_ON_modtreat_fight['ONFF_%s'% col_name]=results_fight['ONFF_%s'% col_name].copy()
    results_ON_modtreat_fight['ONCM_%s'% col_name]=results_fight['ONCM_%s'% col_name].copy()
    results_ON_modtreat_fight['ONFM_%s'% col_name]=results_fight['ONFM_%s'% col_name].copy()  

results_BN_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BN_modtreat_fight['BNCF_%s'% col_name]=results_fight['BNCF_%s'% col_name].copy()
    results_BN_modtreat_fight['BNFF_%s'% col_name]=results_fight['BNFF_%s'% col_name].copy()
    results_BN_modtreat_fight['BNCM_%s'% col_name]=results_fight['BNCM_%s'% col_name].copy()
    results_BN_modtreat_fight['BNFM_%s'% col_name]=results_fight['BNFM_%s'% col_name].copy()  
 
results_TD_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_modtreat_fight['TDCF_%s'% col_name]=results_fight['TDCF_%s'% col_name].copy()
    results_TD_modtreat_fight['TDFF_%s'% col_name]=results_fight['TDFF_%s'% col_name].copy()
    results_TD_modtreat_fight['TDCM_%s'% col_name]=results_fight['TDCM_%s'% col_name].copy()
    results_TD_modtreat_fight['TDFM_%s'% col_name]=results_fight['TDFM_%s'% col_name].copy()       

results_OD_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_OD_modtreat_fight['ODCF_%s'% col_name]=results_fight['ODCF_%s'% col_name].copy()
    results_OD_modtreat_fight['ODFF_%s'% col_name]=results_fight['ODFF_%s'% col_name].copy()
    results_OD_modtreat_fight['ODCM_%s'% col_name]=results_fight['ODCM_%s'% col_name].copy()
    results_OD_modtreat_fight['ODFM_%s'% col_name]=results_fight['ODFM_%s'% col_name].copy()  

results_BD_modtreat_fight=results_fight[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BD_modtreat_fight['BDCF_%s'% col_name]=results_fight['BDCF_%s'% col_name].copy()
    results_BD_modtreat_fight['BDFF_%s'% col_name]=results_fight['BDFF_%s'% col_name].copy()
    results_BD_modtreat_fight['BDCM_%s'% col_name]=results_fight['BDCM_%s'% col_name].copy()
    results_BD_modtreat_fight['BDFM_%s'% col_name]=results_fight['BDFM_%s'% col_name].copy()                

results_TN_mod_fight.columns = results_TN_mod_fight.columns.str.replace(' ', '')
results_ON_mod_fight.columns = results_ON_mod_fight.columns.str.replace(' ', '')
results_BN_mod_fight.columns = results_BN_mod_fight.columns.str.replace(' ', '')
results_TD_mod_fight.columns = results_TD_mod_fight.columns.str.replace(' ', '')
results_OD_mod_fight.columns = results_OD_mod_fight.columns.str.replace(' ', '')
results_BD_mod_fight.columns = results_BD_mod_fight.columns.str.replace(' ', '')

results_TN_modtreat_fight.columns = results_TN_modtreat_fight.columns.str.replace(' ', '')
results_ON_modtreat_fight.columns = results_ON_modtreat_fight.columns.str.replace(' ', '')
results_BN_modtreat_fight.columns = results_BN_modtreat_fight.columns.str.replace(' ', '')
results_TD_modtreat_fight.columns = results_TD_modtreat_fight.columns.str.replace(' ', '')
results_OD_modtreat_fight.columns = results_OD_modtreat_fight.columns.str.replace(' ', '')
results_BD_modtreat_fight.columns = results_BD_modtreat_fight.columns.str.replace(' ', '')

results_TN_mod_fight.columns = results_TN_mod_fight.columns.str.replace('/', '')
results_ON_mod_fight.columns = results_ON_mod_fight.columns.str.replace('/', '')
results_BN_mod_fight.columns = results_BN_mod_fight.columns.str.replace('/', '')
results_TD_mod_fight.columns = results_TD_mod_fight.columns.str.replace('/', '')
results_OD_mod_fight.columns = results_OD_mod_fight.columns.str.replace('/', '')
results_BD_mod_fight.columns = results_BD_mod_fight.columns.str.replace('/', '')

results_TN_modtreat_fight.columns = results_TN_modtreat_fight.columns.str.replace('/', '')
results_ON_modtreat_fight.columns = results_ON_modtreat_fight.columns.str.replace('/', '')
results_BN_modtreat_fight.columns = results_BN_modtreat_fight.columns.str.replace('/', '')
results_TD_modtreat_fight.columns = results_TD_modtreat_fight.columns.str.replace('/', '')
results_OD_modtreat_fight.columns = results_OD_modtreat_fight.columns.str.replace('/', '')
results_BD_modtreat_fight.columns = results_BD_modtreat_fight.columns.str.replace('/', '')

results_TN_mod_fight.columns = results_TN_mod_fight.columns.str.replace('-', '')
results_ON_mod_fight.columns = results_ON_mod_fight.columns.str.replace('-', '')
results_BN_mod_fight.columns = results_BN_mod_fight.columns.str.replace('-', '')
results_TD_mod_fight.columns = results_TD_mod_fight.columns.str.replace('-', '')
results_OD_mod_fight.columns = results_OD_mod_fight.columns.str.replace('-', '')
results_BD_mod_fight.columns = results_BD_mod_fight.columns.str.replace('-', '')

results_TN_modtreat_fight.columns = results_TN_modtreat_fight.columns.str.replace('-', '')
results_ON_modtreat_fight.columns = results_ON_modtreat_fight.columns.str.replace('-', '')
results_BN_modtreat_fight.columns = results_BN_modtreat_fight.columns.str.replace('-', '')
results_TD_modtreat_fight.columns = results_TD_modtreat_fight.columns.str.replace('-', '')
results_OD_modtreat_fight.columns = results_OD_modtreat_fight.columns.str.replace('-', '')
results_BD_modtreat_fight.columns = results_BD_modtreat_fight.columns.str.replace('-', '')

# Now for ROLE
# Make excel sheets with relevant information
results_Total_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results): 
    results_Total_role['TD_%s'% col_name]=results_role['TD_%s'% col_name].copy()
    results_Total_role['TN_%s'% col_name]=results_role['TN_%s'% col_name].copy()

results_OF_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):    
    results_OF_role['OD_%s'% col_name]=results_role['OD_%s'% col_name].copy()
    results_OF_role['ON_%s'% col_name]=results_role['ON_%s'% col_name].copy()

results_Burrow_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):
    results_Burrow_role['BD_%s'% col_name]=results_role['BD_%s'% col_name].copy()
    results_Burrow_role['BN_%s'% col_name]=results_role['BN_%s'% col_name].copy()
    
results_Total_role.columns = results_Total_role.columns.str.replace(' ', '')
results_OF_role.columns = results_OF_role.columns.str.replace(' ', '')
results_Burrow_role.columns = results_Burrow_role.columns.str.replace(' ', '')

results_Total_role.columns = results_Total_role.columns.str.replace('/', '')
results_OF_role.columns = results_OF_role.columns.str.replace('/', '')
results_Burrow_role.columns = results_Burrow_role.columns.str.replace('/', '')

results_Total_role.columns = results_Total_role.columns.str.replace('-', '')
results_OF_role.columns = results_OF_role.columns.str.replace('-', '')
results_Burrow_role.columns = results_Burrow_role.columns.str.replace('-', '')

results_TN_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_mod_role['TNM_%s'% col_name]=results_role['TNM_%s'% col_name].copy()
    results_TN_mod_role['TNF_%s'% col_name]=results_role['TNF_%s'% col_name].copy()
    results_TN_mod_role['TNCR_%s'% col_name]=results_role['TNCR_%s'% col_name].copy()
    results_TN_mod_role['TNFR_%s'% col_name]=results_role['TNFR_%s'% col_name].copy()       
    results_TN_mod_role['TNW_%s'% col_name]=results_role['TNW_%s'% col_name].copy()       
    results_TN_mod_role['TNL_%s'% col_name]=results_role['TNL_%s'% col_name].copy()       
    results_TN_mod_role['TNO_%s'% col_name]=results_role['TNO_%s'% col_name].copy()       

results_ON_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_ON_mod_role['ONM_%s'% col_name]=results_role['ONM_%s'% col_name].copy()
    results_ON_mod_role['ONF_%s'% col_name]=results_role['ONF_%s'% col_name].copy()
    results_ON_mod_role['ONCR_%s'% col_name]=results_role['ONCR_%s'% col_name].copy()
    results_ON_mod_role['ONFR_%s'% col_name]=results_role['ONFR_%s'% col_name].copy() 
    results_ON_mod_role['ONW_%s'% col_name]=results_role['ONW_%s'% col_name].copy()       
    results_ON_mod_role['ONL_%s'% col_name]=results_role['ONL_%s'% col_name].copy()       
    results_ON_mod_role['ONO_%s'% col_name]=results_role['ONO_%s'% col_name].copy()       

results_BN_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BN_mod_role['BNM_%s'% col_name]=results_role['BNM_%s'% col_name].copy()
    results_BN_mod_role['BNF_%s'% col_name]=results_role['BNF_%s'% col_name].copy()
    results_BN_mod_role['BNCR_%s'% col_name]=results_role['BNCR_%s'% col_name].copy()
    results_BN_mod_role['BNFR_%s'% col_name]=results_role['BNFR_%s'% col_name].copy() 
    results_BN_mod_role['BNW_%s'% col_name]=results_role['BNW_%s'% col_name].copy()       
    results_BN_mod_role['BNL_%s'% col_name]=results_role['BNL_%s'% col_name].copy()       
    results_BN_mod_role['BNO_%s'% col_name]=results_role['BNO_%s'% col_name].copy()       
    
results_TD_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_mod_role['TDM_%s'% col_name]=results_role['TDM_%s'% col_name].copy()
    results_TD_mod_role['TDF_%s'% col_name]=results_role['TDF_%s'% col_name].copy()
    results_TD_mod_role['TDCR_%s'% col_name]=results_role['TDCR_%s'% col_name].copy()
    results_TD_mod_role['TDFR_%s'% col_name]=results_role['TDFR_%s'% col_name].copy()       
    results_TD_mod_role['TDW_%s'% col_name]=results_role['TDW_%s'% col_name].copy()       
    results_TD_mod_role['TDL_%s'% col_name]=results_role['TDL_%s'% col_name].copy()       
    results_TD_mod_role['TDO_%s'% col_name]=results_role['TDO_%s'% col_name].copy()       

results_OD_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_OD_mod_role['ODM_%s'% col_name]=results_role['ODM_%s'% col_name].copy()
    results_OD_mod_role['ODF_%s'% col_name]=results_role['ODF_%s'% col_name].copy()
    results_OD_mod_role['ODCR_%s'% col_name]=results_role['ODCR_%s'% col_name].copy()
    results_OD_mod_role['ODFR_%s'% col_name]=results_role['ODFR_%s'% col_name].copy() 
    results_OD_mod_role['ODW_%s'% col_name]=results_role['ODW_%s'% col_name].copy()       
    results_OD_mod_role['ODL_%s'% col_name]=results_role['ODL_%s'% col_name].copy()       
    results_OD_mod_role['ODO_%s'% col_name]=results_role['ODO_%s'% col_name].copy()       

results_BD_mod_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BD_mod_role['BDM_%s'% col_name]=results_role['BDM_%s'% col_name].copy()
    results_BD_mod_role['BDF_%s'% col_name]=results_role['BDF_%s'% col_name].copy()
    results_BD_mod_role['BDCR_%s'% col_name]=results_role['BDCR_%s'% col_name].copy()
    results_BD_mod_role['BDFR_%s'% col_name]=results_role['BDFR_%s'% col_name].copy() 
    results_BD_mod_role['BDW_%s'% col_name]=results_role['BDW_%s'% col_name].copy()       
    results_BD_mod_role['BDL_%s'% col_name]=results_role['BDL_%s'% col_name].copy()       
    results_BD_mod_role['BDO_%s'% col_name]=results_role['BDO_%s'% col_name].copy()       

results_TN_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_modtreat_role['TNCF_%s'% col_name]=results_role['TNCF_%s'% col_name].copy()
    results_TN_modtreat_role['TNFF_%s'% col_name]=results_role['TNFF_%s'% col_name].copy()
    results_TN_modtreat_role['TNCM_%s'% col_name]=results_role['TNCM_%s'% col_name].copy()
    results_TN_modtreat_role['TNFM_%s'% col_name]=results_role['TNFM_%s'% col_name].copy()       

results_ON_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_ON_modtreat_role['ONCF_%s'% col_name]=results_role['ONCF_%s'% col_name].copy()
    results_ON_modtreat_role['ONFF_%s'% col_name]=results_role['ONFF_%s'% col_name].copy()
    results_ON_modtreat_role['ONCM_%s'% col_name]=results_role['ONCM_%s'% col_name].copy()
    results_ON_modtreat_role['ONFM_%s'% col_name]=results_role['ONFM_%s'% col_name].copy()  

results_BN_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BN_modtreat_role['BNCF_%s'% col_name]=results_role['BNCF_%s'% col_name].copy()
    results_BN_modtreat_role['BNFF_%s'% col_name]=results_role['BNFF_%s'% col_name].copy()
    results_BN_modtreat_role['BNCM_%s'% col_name]=results_role['BNCM_%s'% col_name].copy()
    results_BN_modtreat_role['BNFM_%s'% col_name]=results_role['BNFM_%s'% col_name].copy()  
 
results_TD_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_modtreat_role['TDCF_%s'% col_name]=results_role['TDCF_%s'% col_name].copy()
    results_TD_modtreat_role['TDFF_%s'% col_name]=results_role['TDFF_%s'% col_name].copy()
    results_TD_modtreat_role['TDCM_%s'% col_name]=results_role['TDCM_%s'% col_name].copy()
    results_TD_modtreat_role['TDFM_%s'% col_name]=results_role['TDFM_%s'% col_name].copy()       

results_OD_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_OD_modtreat_role['ODCF_%s'% col_name]=results_role['ODCF_%s'% col_name].copy()
    results_OD_modtreat_role['ODFF_%s'% col_name]=results_role['ODFF_%s'% col_name].copy()
    results_OD_modtreat_role['ODCM_%s'% col_name]=results_role['ODCM_%s'% col_name].copy()
    results_OD_modtreat_role['ODFM_%s'% col_name]=results_role['ODFM_%s'% col_name].copy()  

results_BD_modtreat_role=results_role[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BD_modtreat_role['BDCF_%s'% col_name]=results_role['BDCF_%s'% col_name].copy()
    results_BD_modtreat_role['BDFF_%s'% col_name]=results_role['BDFF_%s'% col_name].copy()
    results_BD_modtreat_role['BDCM_%s'% col_name]=results_role['BDCM_%s'% col_name].copy()
    results_BD_modtreat_role['BDFM_%s'% col_name]=results_role['BDFM_%s'% col_name].copy()                

results_TN_mod_role.columns = results_TN_mod_role.columns.str.replace(' ', '')
results_ON_mod_role.columns = results_ON_mod_role.columns.str.replace(' ', '')
results_BN_mod_role.columns = results_BN_mod_role.columns.str.replace(' ', '')
results_TD_mod_role.columns = results_TD_mod_role.columns.str.replace(' ', '')
results_OD_mod_role.columns = results_OD_mod_role.columns.str.replace(' ', '')
results_BD_mod_role.columns = results_BD_mod_role.columns.str.replace(' ', '')

results_TN_modtreat_role.columns = results_TN_modtreat_role.columns.str.replace(' ', '')
results_ON_modtreat_role.columns = results_ON_modtreat_role.columns.str.replace(' ', '')
results_BN_modtreat_role.columns = results_BN_modtreat_role.columns.str.replace(' ', '')
results_TD_modtreat_role.columns = results_TD_modtreat_role.columns.str.replace(' ', '')
results_OD_modtreat_role.columns = results_OD_modtreat_role.columns.str.replace(' ', '')
results_BD_modtreat_role.columns = results_BD_modtreat_role.columns.str.replace(' ', '')

results_TN_mod_role.columns = results_TN_mod_role.columns.str.replace('/', '')
results_ON_mod_role.columns = results_ON_mod_role.columns.str.replace('/', '')
results_BN_mod_role.columns = results_BN_mod_role.columns.str.replace('/', '')
results_TD_mod_role.columns = results_TD_mod_role.columns.str.replace('/', '')
results_OD_mod_role.columns = results_OD_mod_role.columns.str.replace('/', '')
results_BD_mod_role.columns = results_BD_mod_role.columns.str.replace('/', '')

results_TN_modtreat_role.columns = results_TN_modtreat_role.columns.str.replace('/', '')
results_ON_modtreat_role.columns = results_ON_modtreat_role.columns.str.replace('/', '')
results_BN_modtreat_role.columns = results_BN_modtreat_role.columns.str.replace('/', '')
results_TD_modtreat_role.columns = results_TD_modtreat_role.columns.str.replace('/', '')
results_OD_modtreat_role.columns = results_OD_modtreat_role.columns.str.replace('/', '')
results_BD_modtreat_role.columns = results_BD_modtreat_role.columns.str.replace('/', '')

results_TN_mod_role.columns = results_TN_mod_role.columns.str.replace('-', '')
results_ON_mod_role.columns = results_ON_mod_role.columns.str.replace('-', '')
results_BN_mod_role.columns = results_BN_mod_role.columns.str.replace('-', '')
results_TD_mod_role.columns = results_TD_mod_role.columns.str.replace('-', '')
results_OD_mod_role.columns = results_OD_mod_role.columns.str.replace('-', '')
results_BD_mod_role.columns = results_BD_mod_role.columns.str.replace('-', '')

results_TN_modtreat_role.columns = results_TN_modtreat_role.columns.str.replace('-', '')
results_ON_modtreat_role.columns = results_ON_modtreat_role.columns.str.replace('-', '')
results_BN_modtreat_role.columns = results_BN_modtreat_role.columns.str.replace('-', '')
results_TD_modtreat_role.columns = results_TD_modtreat_role.columns.str.replace('-', '')
results_OD_modtreat_role.columns = results_OD_modtreat_role.columns.str.replace('-', '')
results_BD_modtreat_role.columns = results_BD_modtreat_role.columns.str.replace('-', '')

# Now for ROLEPLUS
# Make excel sheets with relevant information
results_Total_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results): 
    results_Total_roleplus['TD_%s'% col_name]=results_roleplus['TD_%s'% col_name].copy()
    results_Total_roleplus['TN_%s'% col_name]=results_roleplus['TN_%s'% col_name].copy()

results_OF_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):    
    results_OF_roleplus['OD_%s'% col_name]=results_roleplus['OD_%s'% col_name].copy()
    results_OF_roleplus['ON_%s'% col_name]=results_roleplus['ON_%s'% col_name].copy()

results_Burrow_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']]
for position, col_name in enumerate(list_results):
    results_Burrow_roleplus['BD_%s'% col_name]=results_roleplus['BD_%s'% col_name].copy()
    results_Burrow_roleplus['BN_%s'% col_name]=results_roleplus['BN_%s'% col_name].copy()
    
results_Total_roleplus.columns = results_Total_roleplus.columns.str.replace(' ', '')
results_OF_roleplus.columns = results_OF_roleplus.columns.str.replace(' ', '')
results_Burrow_roleplus.columns = results_Burrow_roleplus.columns.str.replace(' ', '')

results_Total_roleplus.columns = results_Total_roleplus.columns.str.replace('/', '')
results_OF_roleplus.columns = results_OF_roleplus.columns.str.replace('/', '')
results_Burrow_roleplus.columns = results_Burrow_roleplus.columns.str.replace('/', '')

results_Total_roleplus.columns = results_Total_roleplus.columns.str.replace('-', '')
results_OF_roleplus.columns = results_OF_roleplus.columns.str.replace('-', '')
results_Burrow_roleplus.columns = results_Burrow_roleplus.columns.str.replace('-', '')

results_TN_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_mod_roleplus['TNM_%s'% col_name]=results_roleplus['TNM_%s'% col_name].copy()
    results_TN_mod_roleplus['TNF_%s'% col_name]=results_roleplus['TNF_%s'% col_name].copy()
    results_TN_mod_roleplus['TNCR_%s'% col_name]=results_roleplus['TNCR_%s'% col_name].copy()
    results_TN_mod_roleplus['TNFR_%s'% col_name]=results_roleplus['TNFR_%s'% col_name].copy()       
    results_TN_mod_roleplus['TNW_%s'% col_name]=results_roleplus['TNW_%s'% col_name].copy()       
    results_TN_mod_roleplus['TNL_%s'% col_name]=results_roleplus['TNL_%s'% col_name].copy()       
    results_TN_mod_roleplus['TNO_%s'% col_name]=results_roleplus['TNO_%s'% col_name].copy()       

results_ON_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_ON_mod_roleplus['ONM_%s'% col_name]=results_roleplus['ONM_%s'% col_name].copy()
    results_ON_mod_roleplus['ONF_%s'% col_name]=results_roleplus['ONF_%s'% col_name].copy()
    results_ON_mod_roleplus['ONCR_%s'% col_name]=results_roleplus['ONCR_%s'% col_name].copy()
    results_ON_mod_roleplus['ONFR_%s'% col_name]=results_roleplus['ONFR_%s'% col_name].copy() 
    results_ON_mod_roleplus['ONW_%s'% col_name]=results_roleplus['ONW_%s'% col_name].copy()       
    results_ON_mod_roleplus['ONL_%s'% col_name]=results_roleplus['ONL_%s'% col_name].copy()       
    results_ON_mod_roleplus['ONO_%s'% col_name]=results_roleplus['ONO_%s'% col_name].copy()       

results_BN_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BN_mod_roleplus['BNM_%s'% col_name]=results_roleplus['BNM_%s'% col_name].copy()
    results_BN_mod_roleplus['BNF_%s'% col_name]=results_roleplus['BNF_%s'% col_name].copy()
    results_BN_mod_roleplus['BNCR_%s'% col_name]=results_roleplus['BNCR_%s'% col_name].copy()
    results_BN_mod_roleplus['BNFR_%s'% col_name]=results_roleplus['BNFR_%s'% col_name].copy() 
    results_BN_mod_roleplus['BNW_%s'% col_name]=results_roleplus['BNW_%s'% col_name].copy()       
    results_BN_mod_roleplus['BNL_%s'% col_name]=results_roleplus['BNL_%s'% col_name].copy()       
    results_BN_mod_roleplus['BNO_%s'% col_name]=results_roleplus['BNO_%s'% col_name].copy()       
    
results_TD_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_mod_roleplus['TDM_%s'% col_name]=results_roleplus['TDM_%s'% col_name].copy()
    results_TD_mod_roleplus['TDF_%s'% col_name]=results_roleplus['TDF_%s'% col_name].copy()
    results_TD_mod_roleplus['TDCR_%s'% col_name]=results_roleplus['TDCR_%s'% col_name].copy()
    results_TD_mod_roleplus['TDFR_%s'% col_name]=results_roleplus['TDFR_%s'% col_name].copy()       
    results_TD_mod_roleplus['TDW_%s'% col_name]=results_roleplus['TDW_%s'% col_name].copy()       
    results_TD_mod_roleplus['TDL_%s'% col_name]=results_roleplus['TDL_%s'% col_name].copy()       
    results_TD_mod_roleplus['TDO_%s'% col_name]=results_roleplus['TDO_%s'% col_name].copy()       

results_OD_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_OD_mod_roleplus['ODM_%s'% col_name]=results_roleplus['ODM_%s'% col_name].copy()
    results_OD_mod_roleplus['ODF_%s'% col_name]=results_roleplus['ODF_%s'% col_name].copy()
    results_OD_mod_roleplus['ODCR_%s'% col_name]=results_roleplus['ODCR_%s'% col_name].copy()
    results_OD_mod_roleplus['ODFR_%s'% col_name]=results_roleplus['ODFR_%s'% col_name].copy() 
    results_OD_mod_roleplus['ODW_%s'% col_name]=results_roleplus['ODW_%s'% col_name].copy()       
    results_OD_mod_roleplus['ODL_%s'% col_name]=results_roleplus['ODL_%s'% col_name].copy()       
    results_OD_mod_roleplus['ODO_%s'% col_name]=results_roleplus['ODO_%s'% col_name].copy()       

results_BD_mod_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BD_mod_roleplus['BDM_%s'% col_name]=results_roleplus['BDM_%s'% col_name].copy()
    results_BD_mod_roleplus['BDF_%s'% col_name]=results_roleplus['BDF_%s'% col_name].copy()
    results_BD_mod_roleplus['BDCR_%s'% col_name]=results_roleplus['BDCR_%s'% col_name].copy()
    results_BD_mod_roleplus['BDFR_%s'% col_name]=results_roleplus['BDFR_%s'% col_name].copy() 
    results_BD_mod_roleplus['BDW_%s'% col_name]=results_roleplus['BDW_%s'% col_name].copy()       
    results_BD_mod_roleplus['BDL_%s'% col_name]=results_roleplus['BDL_%s'% col_name].copy()       
    results_BD_mod_roleplus['BDO_%s'% col_name]=results_roleplus['BDO_%s'% col_name].copy()       

results_TN_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TN_modtreat_roleplus['TNCF_%s'% col_name]=results_roleplus['TNCF_%s'% col_name].copy()
    results_TN_modtreat_roleplus['TNFF_%s'% col_name]=results_roleplus['TNFF_%s'% col_name].copy()
    results_TN_modtreat_roleplus['TNCM_%s'% col_name]=results_roleplus['TNCM_%s'% col_name].copy()
    results_TN_modtreat_roleplus['TNFM_%s'% col_name]=results_roleplus['TNFM_%s'% col_name].copy()       

results_ON_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_ON_modtreat_roleplus['ONCF_%s'% col_name]=results_roleplus['ONCF_%s'% col_name].copy()
    results_ON_modtreat_roleplus['ONFF_%s'% col_name]=results_roleplus['ONFF_%s'% col_name].copy()
    results_ON_modtreat_roleplus['ONCM_%s'% col_name]=results_roleplus['ONCM_%s'% col_name].copy()
    results_ON_modtreat_roleplus['ONFM_%s'% col_name]=results_roleplus['ONFM_%s'% col_name].copy()  

results_BN_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social): 
    results_BN_modtreat_roleplus['BNCF_%s'% col_name]=results_roleplus['BNCF_%s'% col_name].copy()
    results_BN_modtreat_roleplus['BNFF_%s'% col_name]=results_roleplus['BNFF_%s'% col_name].copy()
    results_BN_modtreat_roleplus['BNCM_%s'% col_name]=results_roleplus['BNCM_%s'% col_name].copy()
    results_BN_modtreat_roleplus['BNFM_%s'% col_name]=results_roleplus['BNFM_%s'% col_name].copy()  
 
results_TD_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):    
    results_TD_modtreat_roleplus['TDCF_%s'% col_name]=results_roleplus['TDCF_%s'% col_name].copy()
    results_TD_modtreat_roleplus['TDFF_%s'% col_name]=results_roleplus['TDFF_%s'% col_name].copy()
    results_TD_modtreat_roleplus['TDCM_%s'% col_name]=results_roleplus['TDCM_%s'% col_name].copy()
    results_TD_modtreat_roleplus['TDFM_%s'% col_name]=results_roleplus['TDFM_%s'% col_name].copy()       

results_OD_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_OD_modtreat_roleplus['ODCF_%s'% col_name]=results_roleplus['ODCF_%s'% col_name].copy()
    results_OD_modtreat_roleplus['ODFF_%s'% col_name]=results_roleplus['ODFF_%s'% col_name].copy()
    results_OD_modtreat_roleplus['ODCM_%s'% col_name]=results_roleplus['ODCM_%s'% col_name].copy()
    results_OD_modtreat_roleplus['ODFM_%s'% col_name]=results_roleplus['ODFM_%s'% col_name].copy()  

results_BD_modtreat_roleplus=results_roleplus[[L,XH,XN,XO,'Cohort','Day','Fight']] 
for position, col_name in enumerate(list_results_social):
    results_BD_modtreat_roleplus['BDCF_%s'% col_name]=results_roleplus['BDCF_%s'% col_name].copy()
    results_BD_modtreat_roleplus['BDFF_%s'% col_name]=results_roleplus['BDFF_%s'% col_name].copy()
    results_BD_modtreat_roleplus['BDCM_%s'% col_name]=results_roleplus['BDCM_%s'% col_name].copy()
    results_BD_modtreat_roleplus['BDFM_%s'% col_name]=results_roleplus['BDFM_%s'% col_name].copy()                

results_TN_mod_roleplus.columns = results_TN_mod_roleplus.columns.str.replace(' ', '')
results_ON_mod_roleplus.columns = results_ON_mod_roleplus.columns.str.replace(' ', '')
results_BN_mod_roleplus.columns = results_BN_mod_roleplus.columns.str.replace(' ', '')
results_TD_mod_roleplus.columns = results_TD_mod_roleplus.columns.str.replace(' ', '')
results_OD_mod_roleplus.columns = results_OD_mod_roleplus.columns.str.replace(' ', '')
results_BD_mod_roleplus.columns = results_BD_mod_roleplus.columns.str.replace(' ', '')

results_TN_modtreat_roleplus.columns = results_TN_modtreat_roleplus.columns.str.replace(' ', '')
results_ON_modtreat_roleplus.columns = results_ON_modtreat_roleplus.columns.str.replace(' ', '')
results_BN_modtreat_roleplus.columns = results_BN_modtreat_roleplus.columns.str.replace(' ', '')
results_TD_modtreat_roleplus.columns = results_TD_modtreat_roleplus.columns.str.replace(' ', '')
results_OD_modtreat_roleplus.columns = results_OD_modtreat_roleplus.columns.str.replace(' ', '')
results_BD_modtreat_roleplus.columns = results_BD_modtreat_roleplus.columns.str.replace(' ', '')

results_TN_mod_roleplus.columns = results_TN_mod_roleplus.columns.str.replace('/', '')
results_ON_mod_roleplus.columns = results_ON_mod_roleplus.columns.str.replace('/', '')
results_BN_mod_roleplus.columns = results_BN_mod_roleplus.columns.str.replace('/', '')
results_TD_mod_roleplus.columns = results_TD_mod_roleplus.columns.str.replace('/', '')
results_OD_mod_roleplus.columns = results_OD_mod_roleplus.columns.str.replace('/', '')
results_BD_mod_roleplus.columns = results_BD_mod_roleplus.columns.str.replace('/', '')

results_TN_modtreat_roleplus.columns = results_TN_modtreat_roleplus.columns.str.replace('/', '')
results_ON_modtreat_roleplus.columns = results_ON_modtreat_roleplus.columns.str.replace('/', '')
results_BN_modtreat_roleplus.columns = results_BN_modtreat_roleplus.columns.str.replace('/', '')
results_TD_modtreat_roleplus.columns = results_TD_modtreat_roleplus.columns.str.replace('/', '')
results_OD_modtreat_roleplus.columns = results_OD_modtreat_roleplus.columns.str.replace('/', '')
results_BD_modtreat_roleplus.columns = results_BD_modtreat_roleplus.columns.str.replace('/', '')

results_TN_mod_roleplus.columns = results_TN_mod_roleplus.columns.str.replace('-', '')
results_ON_mod_roleplus.columns = results_ON_mod_roleplus.columns.str.replace('-', '')
results_BN_mod_roleplus.columns = results_BN_mod_roleplus.columns.str.replace('-', '')
results_TD_mod_roleplus.columns = results_TD_mod_roleplus.columns.str.replace('-', '')
results_OD_mod_roleplus.columns = results_OD_mod_roleplus.columns.str.replace('-', '')
results_BD_mod_roleplus.columns = results_BD_mod_roleplus.columns.str.replace('-', '')

results_TN_modtreat_roleplus.columns = results_TN_modtreat_roleplus.columns.str.replace('-', '')
results_ON_modtreat_roleplus.columns = results_ON_modtreat_roleplus.columns.str.replace('-', '')
results_BN_modtreat_roleplus.columns = results_BN_modtreat_roleplus.columns.str.replace('-', '')
results_TD_modtreat_roleplus.columns = results_TD_modtreat_roleplus.columns.str.replace('-', '')
results_OD_modtreat_roleplus.columns = results_OD_modtreat_roleplus.columns.str.replace('-', '')
results_BD_modtreat_roleplus.columns = results_BD_modtreat_roleplus.columns.str.replace('-', '')


# Make a sheet to explain the columns
data_info=pd.DataFrame()
data_info['Code']=('Experiment','Treatment','RatID_witnes','RatID_witnesplus','Cohort','Day',
         'TN','ON','BN','TD','OD','BD','TN_min','ON_min','BN_min','TD_min','OD_min','BD_min',
         'TNM','ONM','BNM','TNF','ONF','BNF','TDM','ODM','BDM','TDF','ODF','BDF','TNFR','TNCR',
         'ONFR','ONCR','BNFR','BNCR','TDFR','TDCR','ODFR','ODCR','BDFR','BDCR','TNCM',
         'TNCF','TNFM','TNFF','ONCM','ONCF','ONFM','ONFF','BNCM','BNCF','BNFM','BNFF','TDCM',
         'TDCF','TDFM','TDFF','ODCM','ODCF','ODFM','ODFF','BDCM','BDCF','BDFM','BDFF',
         'TNW','TNL','TNO')
               
data_info['Explanation']=('Experiment','Treatment','Is the rat winner, loser, witness or not', 'winners and losers are also witness', 
         'Cohort','Day','Total number in total environment',
         'Total number in open field','Total number in burrow area','Total duration in total environment (s)',
         'Total durations in open field (s)','Total durations in burrow area (s)',
         'Total number in total environment corrected for time (per minute)',
         'Total number in open field corrected for time (per minute)','Total number in burrow area corrected for time (per minute)',
         'Total duration (s)in total environment corrected for time (per minute)',
         'Total duration (s) in open field corrected for time (per minute)',
         'Total duration (s) in burrow area corrected for time (per minute)',
         'Total number directed to males in total environment','Total number directed to males in open field',
         'Total number directed to males in burrow area','Total number directed to females in total environment',
         'Total number directed to females in open field','Total number directed to females in burrow area',
         'Total duration directed to males in total environment (s)','Total duration directed to males in open field (s)',
         'Total duration directed to males in burrow area (s)','Total duration directed to females in total environment (s)',
         'Total duration directed to females in open field (s)','Total duration directed to females in burrow area (s)',
         'Total number directed to FLX-rats in total environment','Total number directed to CTR-rats in total environment',
         'Total number directed to FLX-rats in open field','Total number directed to CTR-rats in open field',
         'Total number directed to FLX-rats in burrow area','Total number directed to CTR-rats in burrow area',
         'Total duration directed to FLX-rats in total environment (s)','Total duration directed to CTR-rats in total environment (s)',
         'Total duration directed to FLX-rats in open field (s)','Total duration directed to CTR-rats in open field(s)',
         'Total duration directed to FLX-rats in burrow area (s)','Total duration directed to CTR-rats in burrow area (s)',
         'Total number directed to CTR-males in total environment','Total number directed to CTR-females in total environment',
         'Total number directed to FLX-males in total environment','Total number directed to FLX-females in total environment',
         'Total number directed to CTR-males in open field','Total number directed to CTR-females in open field',
         'Total number directed to FLX-males in open field','Total number directed to FLX-females in open field',
         'Total number directed to CTR-males in burrow area','Total number directed to CTR-females in burrow area',
         'Total number directed to FLX-males in burrow area','Total number directed to FLX-females in burrow area',
         'Total duration directed to CTR-males in total environment (s)','Total duration directed to CTR-females in total environment (s)',
         'Total duration directed to FLX-males in total environment (s)','Total duration directed to FLX-females in total environment (s)',
         'Total duration directed to CTR-males in open field (s)','Total duration directed to CTR-females in open field (s)',
         'Total duration directed to FLX-males in open field (s)','Total duration directed to FLX-females in open field (s)',
         'Total duration directed to CTR-males in burrow area (s)','Total duration directed to CTR-females in burrow area (s)',
         'Total duration directed to FLX-males in burrow area (s)','Total duration directed to FLX-females in burrow area (S)',
         'Total number directed at winners','Total number directed at losers', 'Total number directed at others')
   
# Make an empty DataFrame for statistical output
data_stat_fight=pd.DataFrame()
data_stat_rest_fight=pd.DataFrame()
mean_TN_mod_fight=pd.DataFrame()
mean_ON_mod_fight=pd.DataFrame()
mean_BN_mod_fight=pd.DataFrame()
mean_TD_mod_fight=pd.DataFrame()
mean_OD_mod_fight=pd.DataFrame()
mean_BD_mod_fight=pd.DataFrame()
mean_TN_modtreat_fight=pd.DataFrame()
mean_ON_modtreat_fight=pd.DataFrame()
mean_BN_modtreat_fight=pd.DataFrame()
mean_TD_modtreat_fight=pd.DataFrame()
mean_OD_modtreat_fight=pd.DataFrame()
mean_BD_modtreat_fight=pd.DataFrame()

data_stat_role=pd.DataFrame()
data_stat_rest_role=pd.DataFrame()
mean_TN_mod_role=pd.DataFrame()
mean_ON_mod_role=pd.DataFrame()
mean_BN_mod_role=pd.DataFrame()
mean_TD_mod_role=pd.DataFrame()
mean_OD_mod_role=pd.DataFrame()
mean_BD_mod_role=pd.DataFrame()
mean_TN_modtreat_role=pd.DataFrame()
mean_ON_modtreat_role=pd.DataFrame()
mean_BN_modtreat_role=pd.DataFrame()
mean_TD_modtreat_role=pd.DataFrame()
mean_OD_modtreat_role=pd.DataFrame()
mean_BD_modtreat_role=pd.DataFrame()

data_stat_roleplus=pd.DataFrame()
data_stat_rest_roleplus=pd.DataFrame()
mean_TN_mod_roleplus=pd.DataFrame()
mean_ON_mod_roleplus=pd.DataFrame()
mean_BN_mod_roleplus=pd.DataFrame()
mean_TD_mod_roleplus=pd.DataFrame()
mean_OD_mod_roleplus=pd.DataFrame()
mean_BD_mod_roleplus=pd.DataFrame()
mean_TN_modtreat_roleplus=pd.DataFrame()
mean_ON_modtreat_roleplus=pd.DataFrame()
mean_BN_modtreat_roleplus=pd.DataFrame()
mean_TD_modtreat_roleplus=pd.DataFrame()
mean_OD_modtreat_roleplus=pd.DataFrame()
mean_BD_modtreat_roleplus=pd.DataFrame()

# Statistics on the data
# MEAN
mean_Total_fight=results_fight.groupby('Treatment')['Cohort','Day'].mean()
mean_Total_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Total_fight['mean_TD_%s'% col_name]=results_fight.groupby('Treatment')['TD_%s'% col_name].mean()
    mean_Total_fight['mean_TN_%s'% col_name]=results_fight.groupby('Treatment')['TN_%s'% col_name].mean()

mean_OF_fight=results_fight.groupby('Treatment')['Cohort','Day'].mean()
mean_OF_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_OF_fight['mean_OD_%s'% col_name]=results_fight.groupby('Treatment')['OD_%s'% col_name].mean()
    mean_OF_fight['mean_ON_%s'% col_name]=results_fight.groupby('Treatment')['ON_%s'% col_name].mean()

mean_Burrow_fight=results_fight.groupby('Treatment')['Cohort','Day'].mean()
mean_Burrow_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Burrow_fight['mean_BD_%s'% col_name]=results_fight.groupby('Treatment')['BD_%s'% col_name].mean()
    mean_Burrow_fight['mean_BN_%s'% col_name]=results_fight.groupby('Treatment')['BN_%s'% col_name].mean()

mean_Total_fight_columns=list(mean_Total_fight.columns.values)
mean_OF_fight_columns=list(mean_OF_fight.columns.values)
mean_Burrow_fight_columns=list(mean_Burrow_fight.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    mean_TN_mod_fight['mean_TNM_%s'% col_name]=results_fight.groupby('Treatment')['TNM_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNF_%s'% col_name]=results_fight.groupby('Treatment')['TNF_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNCR_%s'% col_name]=results_fight.groupby('Treatment')['TNCR_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNFR_%s'% col_name]=results_fight.groupby('Treatment')['TNFR_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNW_%s'% col_name]=results_fight.groupby('Treatment')['TNW_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNL_%s'% col_name]=results_fight.groupby('Treatment')['TNL_%s'% col_name].mean()
    mean_TN_mod_fight['mean_TNO_%s'% col_name]=results_fight.groupby('Treatment')['TNO_%s'% col_name].mean()
    mean_ON_mod_fight['mean_ONM_%s'% col_name]=results_fight.groupby('Treatment')['ONM_%s'% col_name].mean()
    mean_ON_mod_fight['mean_ONF_%s'% col_name]=results_fight.groupby('Treatment')['ONF_%s'% col_name].mean()
    mean_ON_mod_fight['mean_ONCR_%s'% col_name]=results_fight.groupby('Treatment')['ONCR_%s'% col_name].mean()
    mean_ON_mod_fight['mean_ONFR_%s'% col_name]=results_fight.groupby('Treatment')['ONFR_%s'% col_name].mean()
    mean_TN_mod_fight['mean_ONW_%s'% col_name]=results_fight.groupby('Treatment')['ONW_%s'% col_name].mean()
    mean_TN_mod_fight['mean_ONL_%s'% col_name]=results_fight.groupby('Treatment')['ONL_%s'% col_name].mean()
    mean_TN_mod_fight['mean_ONO_%s'% col_name]=results_fight.groupby('Treatment')['ONO_%s'% col_name].mean()
    mean_BN_mod_fight['mean_BNM_%s'% col_name]=results_fight.groupby('Treatment')['BNM_%s'% col_name].mean()
    mean_BN_mod_fight['mean_BNF_%s'% col_name]=results_fight.groupby('Treatment')['BNF_%s'% col_name].mean()
    mean_BN_mod_fight['mean_BNCR_%s'% col_name]=results_fight.groupby('Treatment')['BNCR_%s'% col_name].mean()
    mean_BN_mod_fight['mean_BNFR_%s'% col_name]=results_fight.groupby('Treatment')['BNFR_%s'% col_name].mean()
    mean_TN_mod_fight['mean_BNW_%s'% col_name]=results_fight.groupby('Treatment')['BNW_%s'% col_name].mean()
    mean_TN_mod_fight['mean_BNL_%s'% col_name]=results_fight.groupby('Treatment')['BNL_%s'% col_name].mean()
    mean_TN_mod_fight['mean_BNO_%s'% col_name]=results_fight.groupby('Treatment')['BNO_%s'% col_name].mean()
                   
    mean_TD_mod_fight['mean_TDM_%s'% col_name]=results_fight.groupby('Treatment')['TDM_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDF_%s'% col_name]=results_fight.groupby('Treatment')['TDF_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDCR_%s'% col_name]=results_fight.groupby('Treatment')['TDCR_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDFR_%s'% col_name]=results_fight.groupby('Treatment')['TDFR_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDW_%s'% col_name]=results_fight.groupby('Treatment')['TDW_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDL_%s'% col_name]=results_fight.groupby('Treatment')['TDL_%s'% col_name].mean()
    mean_TD_mod_fight['mean_TDO_%s'% col_name]=results_fight.groupby('Treatment')['TDO_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODM_%s'% col_name]=results_fight.groupby('Treatment')['ODM_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODF_%s'% col_name]=results_fight.groupby('Treatment')['ODF_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODCR_%s'% col_name]=results_fight.groupby('Treatment')['ODCR_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODFR_%s'% col_name]=results_fight.groupby('Treatment')['ODFR_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODW_%s'% col_name]=results_fight.groupby('Treatment')['ODW_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODL_%s'% col_name]=results_fight.groupby('Treatment')['ODL_%s'% col_name].mean()
    mean_OD_mod_fight['mean_ODO_%s'% col_name]=results_fight.groupby('Treatment')['ODO_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDM_%s'% col_name]=results_fight.groupby('Treatment')['BDM_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDF_%s'% col_name]=results_fight.groupby('Treatment')['BDF_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDCR_%s'% col_name]=results_fight.groupby('Treatment')['BDCR_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDFR_%s'% col_name]=results_fight.groupby('Treatment')['BDFR_%s'% col_name].mean()                   
    mean_BD_mod_fight['mean_BDW_%s'% col_name]=results_fight.groupby('Treatment')['BDW_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDL_%s'% col_name]=results_fight.groupby('Treatment')['BDL_%s'% col_name].mean()
    mean_BD_mod_fight['mean_BDO_%s'% col_name]=results_fight.groupby('Treatment')['BDO_%s'% col_name].mean()
         
    mean_TN_modtreat_fight['mean_TNCF_%s'% col_name]=results_fight.groupby('Treatment')['TNCF_%s'% col_name].mean()
    mean_TN_modtreat_fight['mean_TNFF_%s'% col_name]=results_fight.groupby('Treatment')['TNFF_%s'% col_name].mean()
    mean_TN_modtreat_fight['mean_TNCM_%s'% col_name]=results_fight.groupby('Treatment')['TNCM_%s'% col_name].mean()
    mean_TN_modtreat_fight['mean_TNFM_%s'% col_name]=results_fight.groupby('Treatment')['TNFM_%s'% col_name].mean()
    mean_ON_modtreat_fight['mean_ONCF_%s'% col_name]=results_fight.groupby('Treatment')['ONCF_%s'% col_name].mean()
    mean_ON_modtreat_fight['mean_ONFF_%s'% col_name]=results_fight.groupby('Treatment')['ONFF_%s'% col_name].mean()
    mean_ON_modtreat_fight['mean_ONCM_%s'% col_name]=results_fight.groupby('Treatment')['ONCM_%s'% col_name].mean()
    mean_ON_modtreat_fight['mean_ONFM_%s'% col_name]=results_fight.groupby('Treatment')['ONFM_%s'% col_name].mean()
    mean_BN_modtreat_fight['mean_BNCF_%s'% col_name]=results_fight.groupby('Treatment')['BNCF_%s'% col_name].mean()
    mean_BN_modtreat_fight['mean_BNFF_%s'% col_name]=results_fight.groupby('Treatment')['BNFF_%s'% col_name].mean()
    mean_BN_modtreat_fight['mean_BNCM_%s'% col_name]=results_fight.groupby('Treatment')['BNCM_%s'% col_name].mean()
    mean_BN_modtreat_fight['mean_BNFM_%s'% col_name]=results_fight.groupby('Treatment')['BNFM_%s'% col_name].mean()

    mean_TD_modtreat_fight['mean_TDCF_%s'% col_name]=results_fight.groupby('Treatment')['TDCF_%s'% col_name].mean()
    mean_TD_modtreat_fight['mean_TDFF_%s'% col_name]=results_fight.groupby('Treatment')['TDFF_%s'% col_name].mean()
    mean_TD_modtreat_fight['mean_TDCM_%s'% col_name]=results_fight.groupby('Treatment')['TDCM_%s'% col_name].mean()
    mean_TD_modtreat_fight['mean_TDFM_%s'% col_name]=results_fight.groupby('Treatment')['TDFM_%s'% col_name].mean()
    mean_OD_modtreat_fight['mean_ODCF_%s'% col_name]=results_fight.groupby('Treatment')['ODCF_%s'% col_name].mean()
    mean_OD_modtreat_fight['mean_ODFF_%s'% col_name]=results_fight.groupby('Treatment')['ODFF_%s'% col_name].mean()
    mean_OD_modtreat_fight['mean_ODCM_%s'% col_name]=results_fight.groupby('Treatment')['ODCM_%s'% col_name].mean()
    mean_OD_modtreat_fight['mean_ODFM_%s'% col_name]=results_fight.groupby('Treatment')['ODFM_%s'% col_name].mean()
    mean_BD_modtreat_fight['mean_BDCF_%s'% col_name]=results_fight.groupby('Treatment')['BDCF_%s'% col_name].mean()
    mean_BD_modtreat_fight['mean_BDFF_%s'% col_name]=results_fight.groupby('Treatment')['BDFF_%s'% col_name].mean()
    mean_BD_modtreat_fight['mean_BDCM_%s'% col_name]=results_fight.groupby('Treatment')['BDCM_%s'% col_name].mean()
    mean_BD_modtreat_fight['mean_BDFM_%s'% col_name]=results_fight.groupby('Treatment')['BDFM_%s'% col_name].mean()    

mean_TN_mod_fight_columns=list(mean_TN_mod_fight.columns.values)
mean_TD_mod_fight_columns=list(mean_TD_mod_fight.columns.values)
mean_TN_modtreat_fight_columns=list(mean_TN_modtreat_fight.columns.values)
mean_TD_modtreat_fight_columns=list(mean_TD_modtreat_fight.columns.values)    
mean_ON_mod_fight_columns=list(mean_ON_mod_fight.columns.values)
mean_OD_mod_fight_columns=list(mean_OD_mod_fight.columns.values)
mean_ON_modtreat_fight_columns=list(mean_ON_modtreat_fight.columns.values)
mean_OD_modtreat_fight_columns=list(mean_OD_modtreat_fight.columns.values)  
mean_BN_mod_fight_columns=list(mean_BN_mod_fight.columns.values)
mean_BD_mod_fight_columns=list(mean_BD_mod_fight.columns.values)
mean_BN_modtreat_fight_columns=list(mean_BN_modtreat_fight.columns.values)
mean_BD_modtreat_fight_columns=list(mean_BD_modtreat_fight.columns.values)  

# NOW FOR ROLE
# Statistics on the data
# MEAN
mean_Total_role=results_role.groupby('Treatment')['Cohort','Day'].mean()
mean_Total_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Total_role['mean_TD_%s'% col_name]=results_role.groupby('Treatment')['TD_%s'% col_name].mean()
    mean_Total_role['mean_TN_%s'% col_name]=results_role.groupby('Treatment')['TN_%s'% col_name].mean()

mean_OF_role=results_role.groupby('Treatment')['Cohort','Day'].mean()
mean_OF_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_OF_role['mean_OD_%s'% col_name]=results_role.groupby('Treatment')['OD_%s'% col_name].mean()
    mean_OF_role['mean_ON_%s'% col_name]=results_role.groupby('Treatment')['ON_%s'% col_name].mean()

mean_Burrow_role=results_role.groupby('Treatment')['Cohort','Day'].mean()
mean_Burrow_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Burrow_role['mean_BD_%s'% col_name]=results_role.groupby('Treatment')['BD_%s'% col_name].mean()
    mean_Burrow_role['mean_BN_%s'% col_name]=results_role.groupby('Treatment')['BN_%s'% col_name].mean()

mean_Total_role_columns=list(mean_Total_role.columns.values)
mean_OF_role_columns=list(mean_OF_role.columns.values)
mean_Burrow_role_columns=list(mean_Burrow_role.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    mean_TN_mod_role['mean_TNM_%s'% col_name]=results_role.groupby('Treatment')['TNM_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNF_%s'% col_name]=results_role.groupby('Treatment')['TNF_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNCR_%s'% col_name]=results_role.groupby('Treatment')['TNCR_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNFR_%s'% col_name]=results_role.groupby('Treatment')['TNFR_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNW_%s'% col_name]=results_role.groupby('Treatment')['TNW_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNL_%s'% col_name]=results_role.groupby('Treatment')['TNL_%s'% col_name].mean()
    mean_TN_mod_role['mean_TNO_%s'% col_name]=results_role.groupby('Treatment')['TNO_%s'% col_name].mean()
    mean_ON_mod_role['mean_ONM_%s'% col_name]=results_role.groupby('Treatment')['ONM_%s'% col_name].mean()
    mean_ON_mod_role['mean_ONF_%s'% col_name]=results_role.groupby('Treatment')['ONF_%s'% col_name].mean()
    mean_ON_mod_role['mean_ONCR_%s'% col_name]=results_role.groupby('Treatment')['ONCR_%s'% col_name].mean()
    mean_ON_mod_role['mean_ONFR_%s'% col_name]=results_role.groupby('Treatment')['ONFR_%s'% col_name].mean()
    mean_TN_mod_role['mean_ONW_%s'% col_name]=results_role.groupby('Treatment')['ONW_%s'% col_name].mean()
    mean_TN_mod_role['mean_ONL_%s'% col_name]=results_role.groupby('Treatment')['ONL_%s'% col_name].mean()
    mean_TN_mod_role['mean_ONO_%s'% col_name]=results_role.groupby('Treatment')['ONO_%s'% col_name].mean()
    mean_BN_mod_role['mean_BNM_%s'% col_name]=results_role.groupby('Treatment')['BNM_%s'% col_name].mean()
    mean_BN_mod_role['mean_BNF_%s'% col_name]=results_role.groupby('Treatment')['BNF_%s'% col_name].mean()
    mean_BN_mod_role['mean_BNCR_%s'% col_name]=results_role.groupby('Treatment')['BNCR_%s'% col_name].mean()
    mean_BN_mod_role['mean_BNFR_%s'% col_name]=results_role.groupby('Treatment')['BNFR_%s'% col_name].mean()
    mean_TN_mod_role['mean_BNW_%s'% col_name]=results_role.groupby('Treatment')['BNW_%s'% col_name].mean()
    mean_TN_mod_role['mean_BNL_%s'% col_name]=results_role.groupby('Treatment')['BNL_%s'% col_name].mean()
    mean_TN_mod_role['mean_BNO_%s'% col_name]=results_role.groupby('Treatment')['BNO_%s'% col_name].mean()
                   
    mean_TD_mod_role['mean_TDM_%s'% col_name]=results_role.groupby('Treatment')['TDM_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDF_%s'% col_name]=results_role.groupby('Treatment')['TDF_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDCR_%s'% col_name]=results_role.groupby('Treatment')['TDCR_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDFR_%s'% col_name]=results_role.groupby('Treatment')['TDFR_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDW_%s'% col_name]=results_role.groupby('Treatment')['TDW_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDL_%s'% col_name]=results_role.groupby('Treatment')['TDL_%s'% col_name].mean()
    mean_TD_mod_role['mean_TDO_%s'% col_name]=results_role.groupby('Treatment')['TDO_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODM_%s'% col_name]=results_role.groupby('Treatment')['ODM_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODF_%s'% col_name]=results_role.groupby('Treatment')['ODF_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODCR_%s'% col_name]=results_role.groupby('Treatment')['ODCR_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODFR_%s'% col_name]=results_role.groupby('Treatment')['ODFR_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODW_%s'% col_name]=results_role.groupby('Treatment')['ODW_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODL_%s'% col_name]=results_role.groupby('Treatment')['ODL_%s'% col_name].mean()
    mean_OD_mod_role['mean_ODO_%s'% col_name]=results_role.groupby('Treatment')['ODO_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDM_%s'% col_name]=results_role.groupby('Treatment')['BDM_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDF_%s'% col_name]=results_role.groupby('Treatment')['BDF_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDCR_%s'% col_name]=results_role.groupby('Treatment')['BDCR_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDFR_%s'% col_name]=results_role.groupby('Treatment')['BDFR_%s'% col_name].mean()                   
    mean_BD_mod_role['mean_BDW_%s'% col_name]=results_role.groupby('Treatment')['BDW_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDL_%s'% col_name]=results_role.groupby('Treatment')['BDL_%s'% col_name].mean()
    mean_BD_mod_role['mean_BDO_%s'% col_name]=results_role.groupby('Treatment')['BDO_%s'% col_name].mean()
         
    mean_TN_modtreat_role['mean_TNCF_%s'% col_name]=results_role.groupby('Treatment')['TNCF_%s'% col_name].mean()
    mean_TN_modtreat_role['mean_TNFF_%s'% col_name]=results_role.groupby('Treatment')['TNFF_%s'% col_name].mean()
    mean_TN_modtreat_role['mean_TNCM_%s'% col_name]=results_role.groupby('Treatment')['TNCM_%s'% col_name].mean()
    mean_TN_modtreat_role['mean_TNFM_%s'% col_name]=results_role.groupby('Treatment')['TNFM_%s'% col_name].mean()
    mean_ON_modtreat_role['mean_ONCF_%s'% col_name]=results_role.groupby('Treatment')['ONCF_%s'% col_name].mean()
    mean_ON_modtreat_role['mean_ONFF_%s'% col_name]=results_role.groupby('Treatment')['ONFF_%s'% col_name].mean()
    mean_ON_modtreat_role['mean_ONCM_%s'% col_name]=results_role.groupby('Treatment')['ONCM_%s'% col_name].mean()
    mean_ON_modtreat_role['mean_ONFM_%s'% col_name]=results_role.groupby('Treatment')['ONFM_%s'% col_name].mean()
    mean_BN_modtreat_role['mean_BNCF_%s'% col_name]=results_role.groupby('Treatment')['BNCF_%s'% col_name].mean()
    mean_BN_modtreat_role['mean_BNFF_%s'% col_name]=results_role.groupby('Treatment')['BNFF_%s'% col_name].mean()
    mean_BN_modtreat_role['mean_BNCM_%s'% col_name]=results_role.groupby('Treatment')['BNCM_%s'% col_name].mean()
    mean_BN_modtreat_role['mean_BNFM_%s'% col_name]=results_role.groupby('Treatment')['BNFM_%s'% col_name].mean()

    mean_TD_modtreat_role['mean_TDCF_%s'% col_name]=results_role.groupby('Treatment')['TDCF_%s'% col_name].mean()
    mean_TD_modtreat_role['mean_TDFF_%s'% col_name]=results_role.groupby('Treatment')['TDFF_%s'% col_name].mean()
    mean_TD_modtreat_role['mean_TDCM_%s'% col_name]=results_role.groupby('Treatment')['TDCM_%s'% col_name].mean()
    mean_TD_modtreat_role['mean_TDFM_%s'% col_name]=results_role.groupby('Treatment')['TDFM_%s'% col_name].mean()
    mean_OD_modtreat_role['mean_ODCF_%s'% col_name]=results_role.groupby('Treatment')['ODCF_%s'% col_name].mean()
    mean_OD_modtreat_role['mean_ODFF_%s'% col_name]=results_role.groupby('Treatment')['ODFF_%s'% col_name].mean()
    mean_OD_modtreat_role['mean_ODCM_%s'% col_name]=results_role.groupby('Treatment')['ODCM_%s'% col_name].mean()
    mean_OD_modtreat_role['mean_ODFM_%s'% col_name]=results_role.groupby('Treatment')['ODFM_%s'% col_name].mean()
    mean_BD_modtreat_role['mean_BDCF_%s'% col_name]=results_role.groupby('Treatment')['BDCF_%s'% col_name].mean()
    mean_BD_modtreat_role['mean_BDFF_%s'% col_name]=results_role.groupby('Treatment')['BDFF_%s'% col_name].mean()
    mean_BD_modtreat_role['mean_BDCM_%s'% col_name]=results_role.groupby('Treatment')['BDCM_%s'% col_name].mean()
    mean_BD_modtreat_role['mean_BDFM_%s'% col_name]=results_role.groupby('Treatment')['BDFM_%s'% col_name].mean()    

mean_TN_mod_role_columns=list(mean_TN_mod_role.columns.values)
mean_TD_mod_role_columns=list(mean_TD_mod_role.columns.values)
mean_TN_modtreat_role_columns=list(mean_TN_modtreat_role.columns.values)
mean_TD_modtreat_role_columns=list(mean_TD_modtreat_role.columns.values)    
mean_ON_mod_role_columns=list(mean_ON_mod_role.columns.values)
mean_OD_mod_role_columns=list(mean_OD_mod_role.columns.values)
mean_ON_modtreat_role_columns=list(mean_ON_modtreat_role.columns.values)
mean_OD_modtreat_role_columns=list(mean_OD_modtreat_role.columns.values)  
mean_BN_mod_role_columns=list(mean_BN_mod_role.columns.values)
mean_BD_mod_role_columns=list(mean_BD_mod_role.columns.values)
mean_BN_modtreat_role_columns=list(mean_BN_modtreat_role.columns.values)
mean_BD_modtreat_role_columns=list(mean_BD_modtreat_role.columns.values)  

# NOW FOR ROLEPLUS
# Statistics on the data
# MEAN
mean_Total_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].mean()
mean_Total_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Total_roleplus['mean_TD_%s'% col_name]=results_roleplus.groupby('RatID')['TD_%s'% col_name].mean()
    mean_Total_roleplus['mean_TN_%s'% col_name]=results_roleplus.groupby('RatID')['TN_%s'% col_name].mean()

mean_OF_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].mean()
mean_OF_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_OF_roleplus['mean_OD_%s'% col_name]=results_roleplus.groupby('RatID')['OD_%s'% col_name].mean()
    mean_OF_roleplus['mean_ON_%s'% col_name]=results_roleplus.groupby('RatID')['ON_%s'% col_name].mean()

mean_Burrow_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].mean()
mean_Burrow_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    mean_Burrow_roleplus['mean_BD_%s'% col_name]=results_roleplus.groupby('RatID')['BD_%s'% col_name].mean()
    mean_Burrow_roleplus['mean_BN_%s'% col_name]=results_roleplus.groupby('RatID')['BN_%s'% col_name].mean()

mean_Total_roleplus_columns=list(mean_Total_roleplus.columns.values)
mean_OF_roleplus_columns=list(mean_OF_roleplus.columns.values)
mean_Burrow_roleplus_columns=list(mean_Burrow_roleplus.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    mean_TN_mod_roleplus['mean_TNM_%s'% col_name]=results_roleplus.groupby('RatID')['TNM_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNF_%s'% col_name]=results_roleplus.groupby('RatID')['TNF_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNCR_%s'% col_name]=results_roleplus.groupby('RatID')['TNCR_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNFR_%s'% col_name]=results_roleplus.groupby('RatID')['TNFR_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNW_%s'% col_name]=results_roleplus.groupby('RatID')['TNW_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNL_%s'% col_name]=results_roleplus.groupby('RatID')['TNL_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_TNO_%s'% col_name]=results_roleplus.groupby('RatID')['TNO_%s'% col_name].mean()
    mean_ON_mod_roleplus['mean_ONM_%s'% col_name]=results_roleplus.groupby('RatID')['ONM_%s'% col_name].mean()
    mean_ON_mod_roleplus['mean_ONF_%s'% col_name]=results_roleplus.groupby('RatID')['ONF_%s'% col_name].mean()
    mean_ON_mod_roleplus['mean_ONCR_%s'% col_name]=results_roleplus.groupby('RatID')['ONCR_%s'% col_name].mean()
    mean_ON_mod_roleplus['mean_ONFR_%s'% col_name]=results_roleplus.groupby('RatID')['ONFR_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_ONW_%s'% col_name]=results_roleplus.groupby('RatID')['ONW_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_ONL_%s'% col_name]=results_roleplus.groupby('RatID')['ONL_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_ONO_%s'% col_name]=results_roleplus.groupby('RatID')['ONO_%s'% col_name].mean()
    mean_BN_mod_roleplus['mean_BNM_%s'% col_name]=results_roleplus.groupby('RatID')['BNM_%s'% col_name].mean()
    mean_BN_mod_roleplus['mean_BNF_%s'% col_name]=results_roleplus.groupby('RatID')['BNF_%s'% col_name].mean()
    mean_BN_mod_roleplus['mean_BNCR_%s'% col_name]=results_roleplus.groupby('RatID')['BNCR_%s'% col_name].mean()
    mean_BN_mod_roleplus['mean_BNFR_%s'% col_name]=results_roleplus.groupby('RatID')['BNFR_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_BNW_%s'% col_name]=results_roleplus.groupby('RatID')['BNW_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_BNL_%s'% col_name]=results_roleplus.groupby('RatID')['BNL_%s'% col_name].mean()
    mean_TN_mod_roleplus['mean_BNO_%s'% col_name]=results_roleplus.groupby('RatID')['BNO_%s'% col_name].mean()
                   
    mean_TD_mod_roleplus['mean_TDM_%s'% col_name]=results_roleplus.groupby('RatID')['TDM_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDF_%s'% col_name]=results_roleplus.groupby('RatID')['TDF_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDCR_%s'% col_name]=results_roleplus.groupby('RatID')['TDCR_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDFR_%s'% col_name]=results_roleplus.groupby('RatID')['TDFR_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDW_%s'% col_name]=results_roleplus.groupby('RatID')['TDW_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDL_%s'% col_name]=results_roleplus.groupby('RatID')['TDL_%s'% col_name].mean()
    mean_TD_mod_roleplus['mean_TDO_%s'% col_name]=results_roleplus.groupby('RatID')['TDO_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODM_%s'% col_name]=results_roleplus.groupby('RatID')['ODM_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODF_%s'% col_name]=results_roleplus.groupby('RatID')['ODF_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODCR_%s'% col_name]=results_roleplus.groupby('RatID')['ODCR_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODFR_%s'% col_name]=results_roleplus.groupby('RatID')['ODFR_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODW_%s'% col_name]=results_roleplus.groupby('RatID')['ODW_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODL_%s'% col_name]=results_roleplus.groupby('RatID')['ODL_%s'% col_name].mean()
    mean_OD_mod_roleplus['mean_ODO_%s'% col_name]=results_roleplus.groupby('RatID')['ODO_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDM_%s'% col_name]=results_roleplus.groupby('RatID')['BDM_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDF_%s'% col_name]=results_roleplus.groupby('RatID')['BDF_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDCR_%s'% col_name]=results_roleplus.groupby('RatID')['BDCR_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDFR_%s'% col_name]=results_roleplus.groupby('RatID')['BDFR_%s'% col_name].mean()                   
    mean_BD_mod_roleplus['mean_BDW_%s'% col_name]=results_roleplus.groupby('RatID')['BDW_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDL_%s'% col_name]=results_roleplus.groupby('RatID')['BDL_%s'% col_name].mean()
    mean_BD_mod_roleplus['mean_BDO_%s'% col_name]=results_roleplus.groupby('RatID')['BDO_%s'% col_name].mean()
         
    mean_TN_modtreat_roleplus['mean_TNCF_%s'% col_name]=results_roleplus.groupby('RatID')['TNCF_%s'% col_name].mean()
    mean_TN_modtreat_roleplus['mean_TNFF_%s'% col_name]=results_roleplus.groupby('RatID')['TNFF_%s'% col_name].mean()
    mean_TN_modtreat_roleplus['mean_TNCM_%s'% col_name]=results_roleplus.groupby('RatID')['TNCM_%s'% col_name].mean()
    mean_TN_modtreat_roleplus['mean_TNFM_%s'% col_name]=results_roleplus.groupby('RatID')['TNFM_%s'% col_name].mean()
    mean_ON_modtreat_roleplus['mean_ONCF_%s'% col_name]=results_roleplus.groupby('RatID')['ONCF_%s'% col_name].mean()
    mean_ON_modtreat_roleplus['mean_ONFF_%s'% col_name]=results_roleplus.groupby('RatID')['ONFF_%s'% col_name].mean()
    mean_ON_modtreat_roleplus['mean_ONCM_%s'% col_name]=results_roleplus.groupby('RatID')['ONCM_%s'% col_name].mean()
    mean_ON_modtreat_roleplus['mean_ONFM_%s'% col_name]=results_roleplus.groupby('RatID')['ONFM_%s'% col_name].mean()
    mean_BN_modtreat_roleplus['mean_BNCF_%s'% col_name]=results_roleplus.groupby('RatID')['BNCF_%s'% col_name].mean()
    mean_BN_modtreat_roleplus['mean_BNFF_%s'% col_name]=results_roleplus.groupby('RatID')['BNFF_%s'% col_name].mean()
    mean_BN_modtreat_roleplus['mean_BNCM_%s'% col_name]=results_roleplus.groupby('RatID')['BNCM_%s'% col_name].mean()
    mean_BN_modtreat_roleplus['mean_BNFM_%s'% col_name]=results_roleplus.groupby('RatID')['BNFM_%s'% col_name].mean()

    mean_TD_modtreat_roleplus['mean_TDCF_%s'% col_name]=results_roleplus.groupby('RatID')['TDCF_%s'% col_name].mean()
    mean_TD_modtreat_roleplus['mean_TDFF_%s'% col_name]=results_roleplus.groupby('RatID')['TDFF_%s'% col_name].mean()
    mean_TD_modtreat_roleplus['mean_TDCM_%s'% col_name]=results_roleplus.groupby('RatID')['TDCM_%s'% col_name].mean()
    mean_TD_modtreat_roleplus['mean_TDFM_%s'% col_name]=results_roleplus.groupby('RatID')['TDFM_%s'% col_name].mean()
    mean_OD_modtreat_roleplus['mean_ODCF_%s'% col_name]=results_roleplus.groupby('RatID')['ODCF_%s'% col_name].mean()
    mean_OD_modtreat_roleplus['mean_ODFF_%s'% col_name]=results_roleplus.groupby('RatID')['ODFF_%s'% col_name].mean()
    mean_OD_modtreat_roleplus['mean_ODCM_%s'% col_name]=results_roleplus.groupby('RatID')['ODCM_%s'% col_name].mean()
    mean_OD_modtreat_roleplus['mean_ODFM_%s'% col_name]=results_roleplus.groupby('RatID')['ODFM_%s'% col_name].mean()
    mean_BD_modtreat_roleplus['mean_BDCF_%s'% col_name]=results_roleplus.groupby('RatID')['BDCF_%s'% col_name].mean()
    mean_BD_modtreat_roleplus['mean_BDFF_%s'% col_name]=results_roleplus.groupby('RatID')['BDFF_%s'% col_name].mean()
    mean_BD_modtreat_roleplus['mean_BDCM_%s'% col_name]=results_roleplus.groupby('RatID')['BDCM_%s'% col_name].mean()
    mean_BD_modtreat_roleplus['mean_BDFM_%s'% col_name]=results_roleplus.groupby('RatID')['BDFM_%s'% col_name].mean()    

mean_TN_mod_roleplus_columns=list(mean_TN_mod_roleplus.columns.values)
mean_TD_mod_roleplus_columns=list(mean_TD_mod_roleplus.columns.values)
mean_TN_modtreat_roleplus_columns=list(mean_TN_modtreat_roleplus.columns.values)
mean_TD_modtreat_roleplus_columns=list(mean_TD_modtreat_roleplus.columns.values)    
mean_ON_mod_roleplus_columns=list(mean_ON_mod_roleplus.columns.values)
mean_OD_mod_roleplus_columns=list(mean_OD_mod_roleplus.columns.values)
mean_ON_modtreat_roleplus_columns=list(mean_ON_modtreat_roleplus.columns.values)
mean_OD_modtreat_roleplus_columns=list(mean_OD_modtreat_roleplus.columns.values)  
mean_BN_mod_roleplus_columns=list(mean_BN_mod_roleplus.columns.values)
mean_BD_mod_roleplus_columns=list(mean_BD_mod_roleplus.columns.values)
mean_BN_modtreat_roleplus_columns=list(mean_BN_modtreat_roleplus.columns.values)
mean_BD_modtreat_roleplus_columns=list(mean_BD_modtreat_roleplus.columns.values)  


# Statistics on the data
# MEDIAN
median_TN_mod_fight=pd.DataFrame()
median_ON_mod_fight=pd.DataFrame()
median_BN_mod_fight=pd.DataFrame()
median_TD_mod_fight=pd.DataFrame()
median_OD_mod_fight=pd.DataFrame()
median_BD_mod_fight=pd.DataFrame()
median_TN_modtreat_fight=pd.DataFrame()
median_ON_modtreat_fight=pd.DataFrame()
median_BN_modtreat_fight=pd.DataFrame()
median_TD_modtreat_fight=pd.DataFrame()
median_OD_modtreat_fight=pd.DataFrame()
median_BD_modtreat_fight=pd.DataFrame()

median_TN_mod_role=pd.DataFrame()
median_ON_mod_role=pd.DataFrame()
median_BN_mod_role=pd.DataFrame()
median_TD_mod_role=pd.DataFrame()
median_OD_mod_role=pd.DataFrame()
median_BD_mod_role=pd.DataFrame()
median_TN_modtreat_role=pd.DataFrame()
median_ON_modtreat_role=pd.DataFrame()
median_BN_modtreat_role=pd.DataFrame()
median_TD_modtreat_role=pd.DataFrame()
median_OD_modtreat_role=pd.DataFrame()
median_BD_modtreat_role=pd.DataFrame()

median_TN_mod_roleplus=pd.DataFrame()
median_ON_mod_roleplus=pd.DataFrame()
median_BN_mod_roleplus=pd.DataFrame()
median_TD_mod_roleplus=pd.DataFrame()
median_OD_mod_roleplus=pd.DataFrame()
median_BD_mod_roleplus=pd.DataFrame()
median_TN_modtreat_roleplus=pd.DataFrame()
median_ON_modtreat_roleplus=pd.DataFrame()
median_BN_modtreat_roleplus=pd.DataFrame()
median_TD_modtreat_roleplus=pd.DataFrame()
median_OD_modtreat_roleplus=pd.DataFrame()
median_BD_modtreat_roleplus=pd.DataFrame()

median_Total_fight=results_fight.groupby('Treatment')['Cohort','Day'].median()
median_Total_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Total_fight['median_TD_%s'% col_name]=results_fight.groupby('Treatment')['TD_%s'% col_name].median()
    median_Total_fight['median_TN_%s'% col_name]=results_fight.groupby('Treatment')['TN_%s'% col_name].median()

median_OF_fight=results_fight.groupby('Treatment')['Cohort','Day'].median()
median_OF_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_OF_fight['median_OD_%s'% col_name]=results_fight.groupby('Treatment')['OD_%s'% col_name].median()
    median_OF_fight['median_ON_%s'% col_name]=results_fight.groupby('Treatment')['ON_%s'% col_name].median()

median_Burrow_fight=results_fight.groupby('Treatment')['Cohort','Day'].median()
median_Burrow_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Burrow_fight['median_BD_%s'% col_name]=results_fight.groupby('Treatment')['BD_%s'% col_name].median()
    median_Burrow_fight['median_BN_%s'% col_name]=results_fight.groupby('Treatment')['BN_%s'% col_name].median()

median_Total_fight_columns=list(median_Total_fight.columns.values)
median_OF_fight_columns=list(median_OF_fight.columns.values)
median_Burrow_fight_columns=list(median_Burrow_fight.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    median_TN_mod_fight['median_TNM_%s'% col_name]=results_fight.groupby('Treatment')['TNM_%s'% col_name].median()
    median_TN_mod_fight['median_TNF_%s'% col_name]=results_fight.groupby('Treatment')['TNF_%s'% col_name].median()
    median_TN_mod_fight['median_TNCR_%s'% col_name]=results_fight.groupby('Treatment')['TNCR_%s'% col_name].median()
    median_TN_mod_fight['median_TNFR_%s'% col_name]=results_fight.groupby('Treatment')['TNFR_%s'% col_name].median()
    median_TN_mod_fight['median_TNW_%s'% col_name]=results_fight.groupby('Treatment')['TNW_%s'% col_name].median()
    median_TN_mod_fight['median_TNL_%s'% col_name]=results_fight.groupby('Treatment')['TNL_%s'% col_name].median()
    median_TN_mod_fight['median_TNO_%s'% col_name]=results_fight.groupby('Treatment')['TNO_%s'% col_name].median()
    median_ON_mod_fight['median_ONM_%s'% col_name]=results_fight.groupby('Treatment')['ONM_%s'% col_name].median()
    median_ON_mod_fight['median_ONF_%s'% col_name]=results_fight.groupby('Treatment')['ONF_%s'% col_name].median()
    median_ON_mod_fight['median_ONCR_%s'% col_name]=results_fight.groupby('Treatment')['ONCR_%s'% col_name].median()
    median_ON_mod_fight['median_ONFR_%s'% col_name]=results_fight.groupby('Treatment')['ONFR_%s'% col_name].median()
    median_TN_mod_fight['median_ONW_%s'% col_name]=results_fight.groupby('Treatment')['ONW_%s'% col_name].median()
    median_TN_mod_fight['median_ONL_%s'% col_name]=results_fight.groupby('Treatment')['ONL_%s'% col_name].median()
    median_TN_mod_fight['median_ONO_%s'% col_name]=results_fight.groupby('Treatment')['ONO_%s'% col_name].median()
    median_BN_mod_fight['median_BNM_%s'% col_name]=results_fight.groupby('Treatment')['BNM_%s'% col_name].median()
    median_BN_mod_fight['median_BNF_%s'% col_name]=results_fight.groupby('Treatment')['BNF_%s'% col_name].median()
    median_BN_mod_fight['median_BNCR_%s'% col_name]=results_fight.groupby('Treatment')['BNCR_%s'% col_name].median()
    median_BN_mod_fight['median_BNFR_%s'% col_name]=results_fight.groupby('Treatment')['BNFR_%s'% col_name].median()
    median_TN_mod_fight['median_BNW_%s'% col_name]=results_fight.groupby('Treatment')['BNW_%s'% col_name].median()
    median_TN_mod_fight['median_BNL_%s'% col_name]=results_fight.groupby('Treatment')['BNL_%s'% col_name].median()
    median_TN_mod_fight['median_BNO_%s'% col_name]=results_fight.groupby('Treatment')['BNO_%s'% col_name].median()
                   
    median_TD_mod_fight['median_TDM_%s'% col_name]=results_fight.groupby('Treatment')['TDM_%s'% col_name].median()
    median_TD_mod_fight['median_TDF_%s'% col_name]=results_fight.groupby('Treatment')['TDF_%s'% col_name].median()
    median_TD_mod_fight['median_TDCR_%s'% col_name]=results_fight.groupby('Treatment')['TDCR_%s'% col_name].median()
    median_TD_mod_fight['median_TDFR_%s'% col_name]=results_fight.groupby('Treatment')['TDFR_%s'% col_name].median()
    median_TD_mod_fight['median_TDW_%s'% col_name]=results_fight.groupby('Treatment')['TDW_%s'% col_name].median()
    median_TD_mod_fight['median_TDL_%s'% col_name]=results_fight.groupby('Treatment')['TDL_%s'% col_name].median()
    median_TD_mod_fight['median_TDO_%s'% col_name]=results_fight.groupby('Treatment')['TDO_%s'% col_name].median()
    median_OD_mod_fight['median_ODM_%s'% col_name]=results_fight.groupby('Treatment')['ODM_%s'% col_name].median()
    median_OD_mod_fight['median_ODF_%s'% col_name]=results_fight.groupby('Treatment')['ODF_%s'% col_name].median()
    median_OD_mod_fight['median_ODCR_%s'% col_name]=results_fight.groupby('Treatment')['ODCR_%s'% col_name].median()
    median_OD_mod_fight['median_ODFR_%s'% col_name]=results_fight.groupby('Treatment')['ODFR_%s'% col_name].median()
    median_OD_mod_fight['median_ODW_%s'% col_name]=results_fight.groupby('Treatment')['ODW_%s'% col_name].median()
    median_OD_mod_fight['median_ODL_%s'% col_name]=results_fight.groupby('Treatment')['ODL_%s'% col_name].median()
    median_OD_mod_fight['median_ODO_%s'% col_name]=results_fight.groupby('Treatment')['ODO_%s'% col_name].median()
    median_BD_mod_fight['median_BDM_%s'% col_name]=results_fight.groupby('Treatment')['BDM_%s'% col_name].median()
    median_BD_mod_fight['median_BDF_%s'% col_name]=results_fight.groupby('Treatment')['BDF_%s'% col_name].median()
    median_BD_mod_fight['median_BDCR_%s'% col_name]=results_fight.groupby('Treatment')['BDCR_%s'% col_name].median()
    median_BD_mod_fight['median_BDFR_%s'% col_name]=results_fight.groupby('Treatment')['BDFR_%s'% col_name].median()                   
    median_BD_mod_fight['median_BDW_%s'% col_name]=results_fight.groupby('Treatment')['BDW_%s'% col_name].median()
    median_BD_mod_fight['median_BDL_%s'% col_name]=results_fight.groupby('Treatment')['BDL_%s'% col_name].median()
    median_BD_mod_fight['median_BDO_%s'% col_name]=results_fight.groupby('Treatment')['BDO_%s'% col_name].median()
         
    median_TN_modtreat_fight['median_TNCF_%s'% col_name]=results_fight.groupby('Treatment')['TNCF_%s'% col_name].median()
    median_TN_modtreat_fight['median_TNFF_%s'% col_name]=results_fight.groupby('Treatment')['TNFF_%s'% col_name].median()
    median_TN_modtreat_fight['median_TNCM_%s'% col_name]=results_fight.groupby('Treatment')['TNCM_%s'% col_name].median()
    median_TN_modtreat_fight['median_TNFM_%s'% col_name]=results_fight.groupby('Treatment')['TNFM_%s'% col_name].median()
    median_ON_modtreat_fight['median_ONCF_%s'% col_name]=results_fight.groupby('Treatment')['ONCF_%s'% col_name].median()
    median_ON_modtreat_fight['median_ONFF_%s'% col_name]=results_fight.groupby('Treatment')['ONFF_%s'% col_name].median()
    median_ON_modtreat_fight['median_ONCM_%s'% col_name]=results_fight.groupby('Treatment')['ONCM_%s'% col_name].median()
    median_ON_modtreat_fight['median_ONFM_%s'% col_name]=results_fight.groupby('Treatment')['ONFM_%s'% col_name].median()
    median_BN_modtreat_fight['median_BNCF_%s'% col_name]=results_fight.groupby('Treatment')['BNCF_%s'% col_name].median()
    median_BN_modtreat_fight['median_BNFF_%s'% col_name]=results_fight.groupby('Treatment')['BNFF_%s'% col_name].median()
    median_BN_modtreat_fight['median_BNCM_%s'% col_name]=results_fight.groupby('Treatment')['BNCM_%s'% col_name].median()
    median_BN_modtreat_fight['median_BNFM_%s'% col_name]=results_fight.groupby('Treatment')['BNFM_%s'% col_name].median()

    median_TD_modtreat_fight['median_TDCF_%s'% col_name]=results_fight.groupby('Treatment')['TDCF_%s'% col_name].median()
    median_TD_modtreat_fight['median_TDFF_%s'% col_name]=results_fight.groupby('Treatment')['TDFF_%s'% col_name].median()
    median_TD_modtreat_fight['median_TDCM_%s'% col_name]=results_fight.groupby('Treatment')['TDCM_%s'% col_name].median()
    median_TD_modtreat_fight['median_TDFM_%s'% col_name]=results_fight.groupby('Treatment')['TDFM_%s'% col_name].median()
    median_OD_modtreat_fight['median_ODCF_%s'% col_name]=results_fight.groupby('Treatment')['ODCF_%s'% col_name].median()
    median_OD_modtreat_fight['median_ODFF_%s'% col_name]=results_fight.groupby('Treatment')['ODFF_%s'% col_name].median()
    median_OD_modtreat_fight['median_ODCM_%s'% col_name]=results_fight.groupby('Treatment')['ODCM_%s'% col_name].median()
    median_OD_modtreat_fight['median_ODFM_%s'% col_name]=results_fight.groupby('Treatment')['ODFM_%s'% col_name].median()
    median_BD_modtreat_fight['median_BDCF_%s'% col_name]=results_fight.groupby('Treatment')['BDCF_%s'% col_name].median()
    median_BD_modtreat_fight['median_BDFF_%s'% col_name]=results_fight.groupby('Treatment')['BDFF_%s'% col_name].median()
    median_BD_modtreat_fight['median_BDCM_%s'% col_name]=results_fight.groupby('Treatment')['BDCM_%s'% col_name].median()
    median_BD_modtreat_fight['median_BDFM_%s'% col_name]=results_fight.groupby('Treatment')['BDFM_%s'% col_name].median()    

median_TN_mod_fight_columns=list(median_TN_mod_fight.columns.values)
median_TD_mod_fight_columns=list(median_TD_mod_fight.columns.values)
median_TN_modtreat_fight_columns=list(median_TN_modtreat_fight.columns.values)
median_TD_modtreat_fight_columns=list(median_TD_modtreat_fight.columns.values)    
median_ON_mod_fight_columns=list(median_ON_mod_fight.columns.values)
median_OD_mod_fight_columns=list(median_OD_mod_fight.columns.values)
median_ON_modtreat_fight_columns=list(median_ON_modtreat_fight.columns.values)
median_OD_modtreat_fight_columns=list(median_OD_modtreat_fight.columns.values)  
median_BN_mod_fight_columns=list(median_BN_mod_fight.columns.values)
median_BD_mod_fight_columns=list(median_BD_mod_fight.columns.values)
median_BN_modtreat_fight_columns=list(median_BN_modtreat_fight.columns.values)
median_BD_modtreat_fight_columns=list(median_BD_modtreat_fight.columns.values)  

# NOW FOR ROLE
# Statistics on the data
# MEDIAN
median_Total_role=results_role.groupby('Treatment')['Cohort','Day'].median()
median_Total_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Total_role['median_TD_%s'% col_name]=results_role.groupby('Treatment')['TD_%s'% col_name].median()
    median_Total_role['median_TN_%s'% col_name]=results_role.groupby('Treatment')['TN_%s'% col_name].median()

median_OF_role=results_role.groupby('Treatment')['Cohort','Day'].median()
median_OF_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_OF_role['median_OD_%s'% col_name]=results_role.groupby('Treatment')['OD_%s'% col_name].median()
    median_OF_role['median_ON_%s'% col_name]=results_role.groupby('Treatment')['ON_%s'% col_name].median()

median_Burrow_role=results_role.groupby('Treatment')['Cohort','Day'].median()
median_Burrow_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Burrow_role['median_BD_%s'% col_name]=results_role.groupby('Treatment')['BD_%s'% col_name].median()
    median_Burrow_role['median_BN_%s'% col_name]=results_role.groupby('Treatment')['BN_%s'% col_name].median()

median_Total_role_columns=list(median_Total_role.columns.values)
median_OF_role_columns=list(median_OF_role.columns.values)
median_Burrow_role_columns=list(median_Burrow_role.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    median_TN_mod_role['median_TNM_%s'% col_name]=results_role.groupby('Treatment')['TNM_%s'% col_name].median()
    median_TN_mod_role['median_TNF_%s'% col_name]=results_role.groupby('Treatment')['TNF_%s'% col_name].median()
    median_TN_mod_role['median_TNCR_%s'% col_name]=results_role.groupby('Treatment')['TNCR_%s'% col_name].median()
    median_TN_mod_role['median_TNFR_%s'% col_name]=results_role.groupby('Treatment')['TNFR_%s'% col_name].median()
    median_TN_mod_role['median_TNW_%s'% col_name]=results_role.groupby('Treatment')['TNW_%s'% col_name].median()
    median_TN_mod_role['median_TNL_%s'% col_name]=results_role.groupby('Treatment')['TNL_%s'% col_name].median()
    median_TN_mod_role['median_TNO_%s'% col_name]=results_role.groupby('Treatment')['TNO_%s'% col_name].median()
    median_ON_mod_role['median_ONM_%s'% col_name]=results_role.groupby('Treatment')['ONM_%s'% col_name].median()
    median_ON_mod_role['median_ONF_%s'% col_name]=results_role.groupby('Treatment')['ONF_%s'% col_name].median()
    median_ON_mod_role['median_ONCR_%s'% col_name]=results_role.groupby('Treatment')['ONCR_%s'% col_name].median()
    median_ON_mod_role['median_ONFR_%s'% col_name]=results_role.groupby('Treatment')['ONFR_%s'% col_name].median()
    median_TN_mod_role['median_ONW_%s'% col_name]=results_role.groupby('Treatment')['ONW_%s'% col_name].median()
    median_TN_mod_role['median_ONL_%s'% col_name]=results_role.groupby('Treatment')['ONL_%s'% col_name].median()
    median_TN_mod_role['median_ONO_%s'% col_name]=results_role.groupby('Treatment')['ONO_%s'% col_name].median()
    median_BN_mod_role['median_BNM_%s'% col_name]=results_role.groupby('Treatment')['BNM_%s'% col_name].median()
    median_BN_mod_role['median_BNF_%s'% col_name]=results_role.groupby('Treatment')['BNF_%s'% col_name].median()
    median_BN_mod_role['median_BNCR_%s'% col_name]=results_role.groupby('Treatment')['BNCR_%s'% col_name].median()
    median_BN_mod_role['median_BNFR_%s'% col_name]=results_role.groupby('Treatment')['BNFR_%s'% col_name].median()
    median_TN_mod_role['median_BNW_%s'% col_name]=results_role.groupby('Treatment')['BNW_%s'% col_name].median()
    median_TN_mod_role['median_BNL_%s'% col_name]=results_role.groupby('Treatment')['BNL_%s'% col_name].median()
    median_TN_mod_role['median_BNO_%s'% col_name]=results_role.groupby('Treatment')['BNO_%s'% col_name].median()
                   
    median_TD_mod_role['median_TDM_%s'% col_name]=results_role.groupby('Treatment')['TDM_%s'% col_name].median()
    median_TD_mod_role['median_TDF_%s'% col_name]=results_role.groupby('Treatment')['TDF_%s'% col_name].median()
    median_TD_mod_role['median_TDCR_%s'% col_name]=results_role.groupby('Treatment')['TDCR_%s'% col_name].median()
    median_TD_mod_role['median_TDFR_%s'% col_name]=results_role.groupby('Treatment')['TDFR_%s'% col_name].median()
    median_TD_mod_role['median_TDW_%s'% col_name]=results_role.groupby('Treatment')['TDW_%s'% col_name].median()
    median_TD_mod_role['median_TDL_%s'% col_name]=results_role.groupby('Treatment')['TDL_%s'% col_name].median()
    median_TD_mod_role['median_TDO_%s'% col_name]=results_role.groupby('Treatment')['TDO_%s'% col_name].median()
    median_OD_mod_role['median_ODM_%s'% col_name]=results_role.groupby('Treatment')['ODM_%s'% col_name].median()
    median_OD_mod_role['median_ODF_%s'% col_name]=results_role.groupby('Treatment')['ODF_%s'% col_name].median()
    median_OD_mod_role['median_ODCR_%s'% col_name]=results_role.groupby('Treatment')['ODCR_%s'% col_name].median()
    median_OD_mod_role['median_ODFR_%s'% col_name]=results_role.groupby('Treatment')['ODFR_%s'% col_name].median()
    median_OD_mod_role['median_ODW_%s'% col_name]=results_role.groupby('Treatment')['ODW_%s'% col_name].median()
    median_OD_mod_role['median_ODL_%s'% col_name]=results_role.groupby('Treatment')['ODL_%s'% col_name].median()
    median_OD_mod_role['median_ODO_%s'% col_name]=results_role.groupby('Treatment')['ODO_%s'% col_name].median()
    median_BD_mod_role['median_BDM_%s'% col_name]=results_role.groupby('Treatment')['BDM_%s'% col_name].median()
    median_BD_mod_role['median_BDF_%s'% col_name]=results_role.groupby('Treatment')['BDF_%s'% col_name].median()
    median_BD_mod_role['median_BDCR_%s'% col_name]=results_role.groupby('Treatment')['BDCR_%s'% col_name].median()
    median_BD_mod_role['median_BDFR_%s'% col_name]=results_role.groupby('Treatment')['BDFR_%s'% col_name].median()                   
    median_BD_mod_role['median_BDW_%s'% col_name]=results_role.groupby('Treatment')['BDW_%s'% col_name].median()
    median_BD_mod_role['median_BDL_%s'% col_name]=results_role.groupby('Treatment')['BDL_%s'% col_name].median()
    median_BD_mod_role['median_BDO_%s'% col_name]=results_role.groupby('Treatment')['BDO_%s'% col_name].median()
         
    median_TN_modtreat_role['median_TNCF_%s'% col_name]=results_role.groupby('Treatment')['TNCF_%s'% col_name].median()
    median_TN_modtreat_role['median_TNFF_%s'% col_name]=results_role.groupby('Treatment')['TNFF_%s'% col_name].median()
    median_TN_modtreat_role['median_TNCM_%s'% col_name]=results_role.groupby('Treatment')['TNCM_%s'% col_name].median()
    median_TN_modtreat_role['median_TNFM_%s'% col_name]=results_role.groupby('Treatment')['TNFM_%s'% col_name].median()
    median_ON_modtreat_role['median_ONCF_%s'% col_name]=results_role.groupby('Treatment')['ONCF_%s'% col_name].median()
    median_ON_modtreat_role['median_ONFF_%s'% col_name]=results_role.groupby('Treatment')['ONFF_%s'% col_name].median()
    median_ON_modtreat_role['median_ONCM_%s'% col_name]=results_role.groupby('Treatment')['ONCM_%s'% col_name].median()
    median_ON_modtreat_role['median_ONFM_%s'% col_name]=results_role.groupby('Treatment')['ONFM_%s'% col_name].median()
    median_BN_modtreat_role['median_BNCF_%s'% col_name]=results_role.groupby('Treatment')['BNCF_%s'% col_name].median()
    median_BN_modtreat_role['median_BNFF_%s'% col_name]=results_role.groupby('Treatment')['BNFF_%s'% col_name].median()
    median_BN_modtreat_role['median_BNCM_%s'% col_name]=results_role.groupby('Treatment')['BNCM_%s'% col_name].median()
    median_BN_modtreat_role['median_BNFM_%s'% col_name]=results_role.groupby('Treatment')['BNFM_%s'% col_name].median()

    median_TD_modtreat_role['median_TDCF_%s'% col_name]=results_role.groupby('Treatment')['TDCF_%s'% col_name].median()
    median_TD_modtreat_role['median_TDFF_%s'% col_name]=results_role.groupby('Treatment')['TDFF_%s'% col_name].median()
    median_TD_modtreat_role['median_TDCM_%s'% col_name]=results_role.groupby('Treatment')['TDCM_%s'% col_name].median()
    median_TD_modtreat_role['median_TDFM_%s'% col_name]=results_role.groupby('Treatment')['TDFM_%s'% col_name].median()
    median_OD_modtreat_role['median_ODCF_%s'% col_name]=results_role.groupby('Treatment')['ODCF_%s'% col_name].median()
    median_OD_modtreat_role['median_ODFF_%s'% col_name]=results_role.groupby('Treatment')['ODFF_%s'% col_name].median()
    median_OD_modtreat_role['median_ODCM_%s'% col_name]=results_role.groupby('Treatment')['ODCM_%s'% col_name].median()
    median_OD_modtreat_role['median_ODFM_%s'% col_name]=results_role.groupby('Treatment')['ODFM_%s'% col_name].median()
    median_BD_modtreat_role['median_BDCF_%s'% col_name]=results_role.groupby('Treatment')['BDCF_%s'% col_name].median()
    median_BD_modtreat_role['median_BDFF_%s'% col_name]=results_role.groupby('Treatment')['BDFF_%s'% col_name].median()
    median_BD_modtreat_role['median_BDCM_%s'% col_name]=results_role.groupby('Treatment')['BDCM_%s'% col_name].median()
    median_BD_modtreat_role['median_BDFM_%s'% col_name]=results_role.groupby('Treatment')['BDFM_%s'% col_name].median()    

median_TN_mod_role_columns=list(median_TN_mod_role.columns.values)
median_TD_mod_role_columns=list(median_TD_mod_role.columns.values)
median_TN_modtreat_role_columns=list(median_TN_modtreat_role.columns.values)
median_TD_modtreat_role_columns=list(median_TD_modtreat_role.columns.values)    
median_ON_mod_role_columns=list(median_ON_mod_role.columns.values)
median_OD_mod_role_columns=list(median_OD_mod_role.columns.values)
median_ON_modtreat_role_columns=list(median_ON_modtreat_role.columns.values)
median_OD_modtreat_role_columns=list(median_OD_modtreat_role.columns.values)  
median_BN_mod_role_columns=list(median_BN_mod_role.columns.values)
median_BD_mod_role_columns=list(median_BD_mod_role.columns.values)
median_BN_modtreat_role_columns=list(median_BN_modtreat_role.columns.values)
median_BD_modtreat_role_columns=list(median_BD_modtreat_role.columns.values)  

# NOW FOR ROLEPLUS
# Statistics on the data
# MEDIAN
median_Total_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].median()
median_Total_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Total_roleplus['median_TD_%s'% col_name]=results_roleplus.groupby('RatID')['TD_%s'% col_name].median()
    median_Total_roleplus['median_TN_%s'% col_name]=results_roleplus.groupby('RatID')['TN_%s'% col_name].median()

median_OF_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].median()
median_OF_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_OF_roleplus['median_OD_%s'% col_name]=results_roleplus.groupby('RatID')['OD_%s'% col_name].median()
    median_OF_roleplus['median_ON_%s'% col_name]=results_roleplus.groupby('RatID')['ON_%s'% col_name].median()

median_Burrow_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].median()
median_Burrow_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    median_Burrow_roleplus['median_BD_%s'% col_name]=results_roleplus.groupby('RatID')['BD_%s'% col_name].median()
    median_Burrow_roleplus['median_BN_%s'% col_name]=results_roleplus.groupby('RatID')['BN_%s'% col_name].median()

median_Total_roleplus_columns=list(median_Total_roleplus.columns.values)
median_OF_roleplus_columns=list(median_OF_roleplus.columns.values)
median_Burrow_roleplus_columns=list(median_Burrow_roleplus.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    median_TN_mod_roleplus['median_TNM_%s'% col_name]=results_roleplus.groupby('RatID')['TNM_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNF_%s'% col_name]=results_roleplus.groupby('RatID')['TNF_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNCR_%s'% col_name]=results_roleplus.groupby('RatID')['TNCR_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNFR_%s'% col_name]=results_roleplus.groupby('RatID')['TNFR_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNW_%s'% col_name]=results_roleplus.groupby('RatID')['TNW_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNL_%s'% col_name]=results_roleplus.groupby('RatID')['TNL_%s'% col_name].median()
    median_TN_mod_roleplus['median_TNO_%s'% col_name]=results_roleplus.groupby('RatID')['TNO_%s'% col_name].median()
    median_ON_mod_roleplus['median_ONM_%s'% col_name]=results_roleplus.groupby('RatID')['ONM_%s'% col_name].median()
    median_ON_mod_roleplus['median_ONF_%s'% col_name]=results_roleplus.groupby('RatID')['ONF_%s'% col_name].median()
    median_ON_mod_roleplus['median_ONCR_%s'% col_name]=results_roleplus.groupby('RatID')['ONCR_%s'% col_name].median()
    median_ON_mod_roleplus['median_ONFR_%s'% col_name]=results_roleplus.groupby('RatID')['ONFR_%s'% col_name].median()
    median_TN_mod_roleplus['median_ONW_%s'% col_name]=results_roleplus.groupby('RatID')['ONW_%s'% col_name].median()
    median_TN_mod_roleplus['median_ONL_%s'% col_name]=results_roleplus.groupby('RatID')['ONL_%s'% col_name].median()
    median_TN_mod_roleplus['median_ONO_%s'% col_name]=results_roleplus.groupby('RatID')['ONO_%s'% col_name].median()
    median_BN_mod_roleplus['median_BNM_%s'% col_name]=results_roleplus.groupby('RatID')['BNM_%s'% col_name].median()
    median_BN_mod_roleplus['median_BNF_%s'% col_name]=results_roleplus.groupby('RatID')['BNF_%s'% col_name].median()
    median_BN_mod_roleplus['median_BNCR_%s'% col_name]=results_roleplus.groupby('RatID')['BNCR_%s'% col_name].median()
    median_BN_mod_roleplus['median_BNFR_%s'% col_name]=results_roleplus.groupby('RatID')['BNFR_%s'% col_name].median()
    median_TN_mod_roleplus['median_BNW_%s'% col_name]=results_roleplus.groupby('RatID')['BNW_%s'% col_name].median()
    median_TN_mod_roleplus['median_BNL_%s'% col_name]=results_roleplus.groupby('RatID')['BNL_%s'% col_name].median()
    median_TN_mod_roleplus['median_BNO_%s'% col_name]=results_roleplus.groupby('RatID')['BNO_%s'% col_name].median()
                   
    median_TD_mod_roleplus['median_TDM_%s'% col_name]=results_roleplus.groupby('RatID')['TDM_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDF_%s'% col_name]=results_roleplus.groupby('RatID')['TDF_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDCR_%s'% col_name]=results_roleplus.groupby('RatID')['TDCR_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDFR_%s'% col_name]=results_roleplus.groupby('RatID')['TDFR_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDW_%s'% col_name]=results_roleplus.groupby('RatID')['TDW_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDL_%s'% col_name]=results_roleplus.groupby('RatID')['TDL_%s'% col_name].median()
    median_TD_mod_roleplus['median_TDO_%s'% col_name]=results_roleplus.groupby('RatID')['TDO_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODM_%s'% col_name]=results_roleplus.groupby('RatID')['ODM_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODF_%s'% col_name]=results_roleplus.groupby('RatID')['ODF_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODCR_%s'% col_name]=results_roleplus.groupby('RatID')['ODCR_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODFR_%s'% col_name]=results_roleplus.groupby('RatID')['ODFR_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODW_%s'% col_name]=results_roleplus.groupby('RatID')['ODW_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODL_%s'% col_name]=results_roleplus.groupby('RatID')['ODL_%s'% col_name].median()
    median_OD_mod_roleplus['median_ODO_%s'% col_name]=results_roleplus.groupby('RatID')['ODO_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDM_%s'% col_name]=results_roleplus.groupby('RatID')['BDM_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDF_%s'% col_name]=results_roleplus.groupby('RatID')['BDF_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDCR_%s'% col_name]=results_roleplus.groupby('RatID')['BDCR_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDFR_%s'% col_name]=results_roleplus.groupby('RatID')['BDFR_%s'% col_name].median()                   
    median_BD_mod_roleplus['median_BDW_%s'% col_name]=results_roleplus.groupby('RatID')['BDW_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDL_%s'% col_name]=results_roleplus.groupby('RatID')['BDL_%s'% col_name].median()
    median_BD_mod_roleplus['median_BDO_%s'% col_name]=results_roleplus.groupby('RatID')['BDO_%s'% col_name].median()
         
    median_TN_modtreat_roleplus['median_TNCF_%s'% col_name]=results_roleplus.groupby('RatID')['TNCF_%s'% col_name].median()
    median_TN_modtreat_roleplus['median_TNFF_%s'% col_name]=results_roleplus.groupby('RatID')['TNFF_%s'% col_name].median()
    median_TN_modtreat_roleplus['median_TNCM_%s'% col_name]=results_roleplus.groupby('RatID')['TNCM_%s'% col_name].median()
    median_TN_modtreat_roleplus['median_TNFM_%s'% col_name]=results_roleplus.groupby('RatID')['TNFM_%s'% col_name].median()
    median_ON_modtreat_roleplus['median_ONCF_%s'% col_name]=results_roleplus.groupby('RatID')['ONCF_%s'% col_name].median()
    median_ON_modtreat_roleplus['median_ONFF_%s'% col_name]=results_roleplus.groupby('RatID')['ONFF_%s'% col_name].median()
    median_ON_modtreat_roleplus['median_ONCM_%s'% col_name]=results_roleplus.groupby('RatID')['ONCM_%s'% col_name].median()
    median_ON_modtreat_roleplus['median_ONFM_%s'% col_name]=results_roleplus.groupby('RatID')['ONFM_%s'% col_name].median()
    median_BN_modtreat_roleplus['median_BNCF_%s'% col_name]=results_roleplus.groupby('RatID')['BNCF_%s'% col_name].median()
    median_BN_modtreat_roleplus['median_BNFF_%s'% col_name]=results_roleplus.groupby('RatID')['BNFF_%s'% col_name].median()
    median_BN_modtreat_roleplus['median_BNCM_%s'% col_name]=results_roleplus.groupby('RatID')['BNCM_%s'% col_name].median()
    median_BN_modtreat_roleplus['median_BNFM_%s'% col_name]=results_roleplus.groupby('RatID')['BNFM_%s'% col_name].median()

    median_TD_modtreat_roleplus['median_TDCF_%s'% col_name]=results_roleplus.groupby('RatID')['TDCF_%s'% col_name].median()
    median_TD_modtreat_roleplus['median_TDFF_%s'% col_name]=results_roleplus.groupby('RatID')['TDFF_%s'% col_name].median()
    median_TD_modtreat_roleplus['median_TDCM_%s'% col_name]=results_roleplus.groupby('RatID')['TDCM_%s'% col_name].median()
    median_TD_modtreat_roleplus['median_TDFM_%s'% col_name]=results_roleplus.groupby('RatID')['TDFM_%s'% col_name].median()
    median_OD_modtreat_roleplus['median_ODCF_%s'% col_name]=results_roleplus.groupby('RatID')['ODCF_%s'% col_name].median()
    median_OD_modtreat_roleplus['median_ODFF_%s'% col_name]=results_roleplus.groupby('RatID')['ODFF_%s'% col_name].median()
    median_OD_modtreat_roleplus['median_ODCM_%s'% col_name]=results_roleplus.groupby('RatID')['ODCM_%s'% col_name].median()
    median_OD_modtreat_roleplus['median_ODFM_%s'% col_name]=results_roleplus.groupby('RatID')['ODFM_%s'% col_name].median()
    median_BD_modtreat_roleplus['median_BDCF_%s'% col_name]=results_roleplus.groupby('RatID')['BDCF_%s'% col_name].median()
    median_BD_modtreat_roleplus['median_BDFF_%s'% col_name]=results_roleplus.groupby('RatID')['BDFF_%s'% col_name].median()
    median_BD_modtreat_roleplus['median_BDCM_%s'% col_name]=results_roleplus.groupby('RatID')['BDCM_%s'% col_name].median()
    median_BD_modtreat_roleplus['median_BDFM_%s'% col_name]=results_roleplus.groupby('RatID')['BDFM_%s'% col_name].median()    

median_TN_mod_roleplus_columns=list(median_TN_mod_roleplus.columns.values)
median_TD_mod_roleplus_columns=list(median_TD_mod_roleplus.columns.values)
median_TN_modtreat_roleplus_columns=list(median_TN_modtreat_roleplus.columns.values)
median_TD_modtreat_roleplus_columns=list(median_TD_modtreat_roleplus.columns.values)    
median_ON_mod_roleplus_columns=list(median_ON_mod_roleplus.columns.values)
median_OD_mod_roleplus_columns=list(median_OD_mod_roleplus.columns.values)
median_ON_modtreat_roleplus_columns=list(median_ON_modtreat_roleplus.columns.values)
median_OD_modtreat_roleplus_columns=list(median_OD_modtreat_roleplus.columns.values)  
median_BN_mod_roleplus_columns=list(median_BN_mod_roleplus.columns.values)
median_BD_mod_roleplus_columns=list(median_BD_mod_roleplus.columns.values)
median_BN_modtreat_roleplus_columns=list(median_BN_modtreat_roleplus.columns.values)
median_BD_modtreat_roleplus_columns=list(median_BD_modtreat_roleplus.columns.values)  


# Statistics on the data
# SEM
sem_TN_mod_fight=pd.DataFrame()
sem_ON_mod_fight=pd.DataFrame()
sem_BN_mod_fight=pd.DataFrame()
sem_TD_mod_fight=pd.DataFrame()
sem_OD_mod_fight=pd.DataFrame()
sem_BD_mod_fight=pd.DataFrame()
sem_TN_modtreat_fight=pd.DataFrame()
sem_ON_modtreat_fight=pd.DataFrame()
sem_BN_modtreat_fight=pd.DataFrame()
sem_TD_modtreat_fight=pd.DataFrame()
sem_OD_modtreat_fight=pd.DataFrame()
sem_BD_modtreat_fight=pd.DataFrame()

sem_TN_mod_role=pd.DataFrame()
sem_ON_mod_role=pd.DataFrame()
sem_BN_mod_role=pd.DataFrame()
sem_TD_mod_role=pd.DataFrame()
sem_OD_mod_role=pd.DataFrame()
sem_BD_mod_role=pd.DataFrame()
sem_TN_modtreat_role=pd.DataFrame()
sem_ON_modtreat_role=pd.DataFrame()
sem_BN_modtreat_role=pd.DataFrame()
sem_TD_modtreat_role=pd.DataFrame()
sem_OD_modtreat_role=pd.DataFrame()
sem_BD_modtreat_role=pd.DataFrame()

sem_TN_mod_roleplus=pd.DataFrame()
sem_ON_mod_roleplus=pd.DataFrame()
sem_BN_mod_roleplus=pd.DataFrame()
sem_TD_mod_roleplus=pd.DataFrame()
sem_OD_mod_roleplus=pd.DataFrame()
sem_BD_mod_roleplus=pd.DataFrame()
sem_TN_modtreat_roleplus=pd.DataFrame()
sem_ON_modtreat_roleplus=pd.DataFrame()
sem_BN_modtreat_roleplus=pd.DataFrame()
sem_TD_modtreat_roleplus=pd.DataFrame()
sem_OD_modtreat_roleplus=pd.DataFrame()
sem_BD_modtreat_roleplus=pd.DataFrame()

sem_Total_fight=results_fight.groupby('Treatment')['Cohort','Day'].sem()
sem_Total_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Total_fight['sem_TD_%s'% col_name]=results_fight.groupby('Treatment')['TD_%s'% col_name].sem()
    sem_Total_fight['sem_TN_%s'% col_name]=results_fight.groupby('Treatment')['TN_%s'% col_name].sem()

sem_OF_fight=results_fight.groupby('Treatment')['Cohort','Day'].sem()
sem_OF_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_OF_fight['sem_OD_%s'% col_name]=results_fight.groupby('Treatment')['OD_%s'% col_name].sem()
    sem_OF_fight['sem_ON_%s'% col_name]=results_fight.groupby('Treatment')['ON_%s'% col_name].sem()

sem_Burrow_fight=results_fight.groupby('Treatment')['Cohort','Day'].sem()
sem_Burrow_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Burrow_fight['sem_BD_%s'% col_name]=results_fight.groupby('Treatment')['BD_%s'% col_name].sem()
    sem_Burrow_fight['sem_BN_%s'% col_name]=results_fight.groupby('Treatment')['BN_%s'% col_name].sem()

sem_Total_fight_columns=list(sem_Total_fight.columns.values)
sem_OF_fight_columns=list(sem_OF_fight.columns.values)
sem_Burrow_fight_columns=list(sem_Burrow_fight.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    sem_TN_mod_fight['sem_TNM_%s'% col_name]=results_fight.groupby('Treatment')['TNM_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNF_%s'% col_name]=results_fight.groupby('Treatment')['TNF_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNCR_%s'% col_name]=results_fight.groupby('Treatment')['TNCR_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNFR_%s'% col_name]=results_fight.groupby('Treatment')['TNFR_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNW_%s'% col_name]=results_fight.groupby('Treatment')['TNW_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNL_%s'% col_name]=results_fight.groupby('Treatment')['TNL_%s'% col_name].sem()
    sem_TN_mod_fight['sem_TNO_%s'% col_name]=results_fight.groupby('Treatment')['TNO_%s'% col_name].sem()
    sem_ON_mod_fight['sem_ONM_%s'% col_name]=results_fight.groupby('Treatment')['ONM_%s'% col_name].sem()
    sem_ON_mod_fight['sem_ONF_%s'% col_name]=results_fight.groupby('Treatment')['ONF_%s'% col_name].sem()
    sem_ON_mod_fight['sem_ONCR_%s'% col_name]=results_fight.groupby('Treatment')['ONCR_%s'% col_name].sem()
    sem_ON_mod_fight['sem_ONFR_%s'% col_name]=results_fight.groupby('Treatment')['ONFR_%s'% col_name].sem()
    sem_TN_mod_fight['sem_ONW_%s'% col_name]=results_fight.groupby('Treatment')['ONW_%s'% col_name].sem()
    sem_TN_mod_fight['sem_ONL_%s'% col_name]=results_fight.groupby('Treatment')['ONL_%s'% col_name].sem()
    sem_TN_mod_fight['sem_ONO_%s'% col_name]=results_fight.groupby('Treatment')['ONO_%s'% col_name].sem()
    sem_BN_mod_fight['sem_BNM_%s'% col_name]=results_fight.groupby('Treatment')['BNM_%s'% col_name].sem()
    sem_BN_mod_fight['sem_BNF_%s'% col_name]=results_fight.groupby('Treatment')['BNF_%s'% col_name].sem()
    sem_BN_mod_fight['sem_BNCR_%s'% col_name]=results_fight.groupby('Treatment')['BNCR_%s'% col_name].sem()
    sem_BN_mod_fight['sem_BNFR_%s'% col_name]=results_fight.groupby('Treatment')['BNFR_%s'% col_name].sem()
    sem_TN_mod_fight['sem_BNW_%s'% col_name]=results_fight.groupby('Treatment')['BNW_%s'% col_name].sem()
    sem_TN_mod_fight['sem_BNL_%s'% col_name]=results_fight.groupby('Treatment')['BNL_%s'% col_name].sem()
    sem_TN_mod_fight['sem_BNO_%s'% col_name]=results_fight.groupby('Treatment')['BNO_%s'% col_name].sem()
                   
    sem_TD_mod_fight['sem_TDM_%s'% col_name]=results_fight.groupby('Treatment')['TDM_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDF_%s'% col_name]=results_fight.groupby('Treatment')['TDF_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDCR_%s'% col_name]=results_fight.groupby('Treatment')['TDCR_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDFR_%s'% col_name]=results_fight.groupby('Treatment')['TDFR_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDW_%s'% col_name]=results_fight.groupby('Treatment')['TDW_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDL_%s'% col_name]=results_fight.groupby('Treatment')['TDL_%s'% col_name].sem()
    sem_TD_mod_fight['sem_TDO_%s'% col_name]=results_fight.groupby('Treatment')['TDO_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODM_%s'% col_name]=results_fight.groupby('Treatment')['ODM_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODF_%s'% col_name]=results_fight.groupby('Treatment')['ODF_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODCR_%s'% col_name]=results_fight.groupby('Treatment')['ODCR_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODFR_%s'% col_name]=results_fight.groupby('Treatment')['ODFR_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODW_%s'% col_name]=results_fight.groupby('Treatment')['ODW_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODL_%s'% col_name]=results_fight.groupby('Treatment')['ODL_%s'% col_name].sem()
    sem_OD_mod_fight['sem_ODO_%s'% col_name]=results_fight.groupby('Treatment')['ODO_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDM_%s'% col_name]=results_fight.groupby('Treatment')['BDM_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDF_%s'% col_name]=results_fight.groupby('Treatment')['BDF_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDCR_%s'% col_name]=results_fight.groupby('Treatment')['BDCR_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDFR_%s'% col_name]=results_fight.groupby('Treatment')['BDFR_%s'% col_name].sem()                   
    sem_BD_mod_fight['sem_BDW_%s'% col_name]=results_fight.groupby('Treatment')['BDW_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDL_%s'% col_name]=results_fight.groupby('Treatment')['BDL_%s'% col_name].sem()
    sem_BD_mod_fight['sem_BDO_%s'% col_name]=results_fight.groupby('Treatment')['BDO_%s'% col_name].sem()
         
    sem_TN_modtreat_fight['sem_TNCF_%s'% col_name]=results_fight.groupby('Treatment')['TNCF_%s'% col_name].sem()
    sem_TN_modtreat_fight['sem_TNFF_%s'% col_name]=results_fight.groupby('Treatment')['TNFF_%s'% col_name].sem()
    sem_TN_modtreat_fight['sem_TNCM_%s'% col_name]=results_fight.groupby('Treatment')['TNCM_%s'% col_name].sem()
    sem_TN_modtreat_fight['sem_TNFM_%s'% col_name]=results_fight.groupby('Treatment')['TNFM_%s'% col_name].sem()
    sem_ON_modtreat_fight['sem_ONCF_%s'% col_name]=results_fight.groupby('Treatment')['ONCF_%s'% col_name].sem()
    sem_ON_modtreat_fight['sem_ONFF_%s'% col_name]=results_fight.groupby('Treatment')['ONFF_%s'% col_name].sem()
    sem_ON_modtreat_fight['sem_ONCM_%s'% col_name]=results_fight.groupby('Treatment')['ONCM_%s'% col_name].sem()
    sem_ON_modtreat_fight['sem_ONFM_%s'% col_name]=results_fight.groupby('Treatment')['ONFM_%s'% col_name].sem()
    sem_BN_modtreat_fight['sem_BNCF_%s'% col_name]=results_fight.groupby('Treatment')['BNCF_%s'% col_name].sem()
    sem_BN_modtreat_fight['sem_BNFF_%s'% col_name]=results_fight.groupby('Treatment')['BNFF_%s'% col_name].sem()
    sem_BN_modtreat_fight['sem_BNCM_%s'% col_name]=results_fight.groupby('Treatment')['BNCM_%s'% col_name].sem()
    sem_BN_modtreat_fight['sem_BNFM_%s'% col_name]=results_fight.groupby('Treatment')['BNFM_%s'% col_name].sem()

    sem_TD_modtreat_fight['sem_TDCF_%s'% col_name]=results_fight.groupby('Treatment')['TDCF_%s'% col_name].sem()
    sem_TD_modtreat_fight['sem_TDFF_%s'% col_name]=results_fight.groupby('Treatment')['TDFF_%s'% col_name].sem()
    sem_TD_modtreat_fight['sem_TDCM_%s'% col_name]=results_fight.groupby('Treatment')['TDCM_%s'% col_name].sem()
    sem_TD_modtreat_fight['sem_TDFM_%s'% col_name]=results_fight.groupby('Treatment')['TDFM_%s'% col_name].sem()
    sem_OD_modtreat_fight['sem_ODCF_%s'% col_name]=results_fight.groupby('Treatment')['ODCF_%s'% col_name].sem()
    sem_OD_modtreat_fight['sem_ODFF_%s'% col_name]=results_fight.groupby('Treatment')['ODFF_%s'% col_name].sem()
    sem_OD_modtreat_fight['sem_ODCM_%s'% col_name]=results_fight.groupby('Treatment')['ODCM_%s'% col_name].sem()
    sem_OD_modtreat_fight['sem_ODFM_%s'% col_name]=results_fight.groupby('Treatment')['ODFM_%s'% col_name].sem()
    sem_BD_modtreat_fight['sem_BDCF_%s'% col_name]=results_fight.groupby('Treatment')['BDCF_%s'% col_name].sem()
    sem_BD_modtreat_fight['sem_BDFF_%s'% col_name]=results_fight.groupby('Treatment')['BDFF_%s'% col_name].sem()
    sem_BD_modtreat_fight['sem_BDCM_%s'% col_name]=results_fight.groupby('Treatment')['BDCM_%s'% col_name].sem()
    sem_BD_modtreat_fight['sem_BDFM_%s'% col_name]=results_fight.groupby('Treatment')['BDFM_%s'% col_name].sem()    

sem_TN_mod_fight_columns=list(sem_TN_mod_fight.columns.values)
sem_TD_mod_fight_columns=list(sem_TD_mod_fight.columns.values)
sem_TN_modtreat_fight_columns=list(sem_TN_modtreat_fight.columns.values)
sem_TD_modtreat_fight_columns=list(sem_TD_modtreat_fight.columns.values)    
sem_ON_mod_fight_columns=list(sem_ON_mod_fight.columns.values)
sem_OD_mod_fight_columns=list(sem_OD_mod_fight.columns.values)
sem_ON_modtreat_fight_columns=list(sem_ON_modtreat_fight.columns.values)
sem_OD_modtreat_fight_columns=list(sem_OD_modtreat_fight.columns.values)  
sem_BN_mod_fight_columns=list(sem_BN_mod_fight.columns.values)
sem_BD_mod_fight_columns=list(sem_BD_mod_fight.columns.values)
sem_BN_modtreat_fight_columns=list(sem_BN_modtreat_fight.columns.values)
sem_BD_modtreat_fight_columns=list(sem_BD_modtreat_fight.columns.values)  

# NOW FOR ROLE
# Statistics on the data
# SEM
sem_Total_role=results_role.groupby('Treatment')['Cohort','Day'].sem()
sem_Total_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Total_role['sem_TD_%s'% col_name]=results_role.groupby('Treatment')['TD_%s'% col_name].sem()
    sem_Total_role['sem_TN_%s'% col_name]=results_role.groupby('Treatment')['TN_%s'% col_name].sem()

sem_OF_role=results_role.groupby('Treatment')['Cohort','Day'].sem()
sem_OF_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_OF_role['sem_OD_%s'% col_name]=results_role.groupby('Treatment')['OD_%s'% col_name].sem()
    sem_OF_role['sem_ON_%s'% col_name]=results_role.groupby('Treatment')['ON_%s'% col_name].sem()

sem_Burrow_role=results_role.groupby('Treatment')['Cohort','Day'].sem()
sem_Burrow_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Burrow_role['sem_BD_%s'% col_name]=results_role.groupby('Treatment')['BD_%s'% col_name].sem()
    sem_Burrow_role['sem_BN_%s'% col_name]=results_role.groupby('Treatment')['BN_%s'% col_name].sem()

sem_Total_role_columns=list(sem_Total_role.columns.values)
sem_OF_role_columns=list(sem_OF_role.columns.values)
sem_Burrow_role_columns=list(sem_Burrow_role.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    sem_TN_mod_role['sem_TNM_%s'% col_name]=results_role.groupby('Treatment')['TNM_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNF_%s'% col_name]=results_role.groupby('Treatment')['TNF_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNCR_%s'% col_name]=results_role.groupby('Treatment')['TNCR_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNFR_%s'% col_name]=results_role.groupby('Treatment')['TNFR_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNW_%s'% col_name]=results_role.groupby('Treatment')['TNW_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNL_%s'% col_name]=results_role.groupby('Treatment')['TNL_%s'% col_name].sem()
    sem_TN_mod_role['sem_TNO_%s'% col_name]=results_role.groupby('Treatment')['TNO_%s'% col_name].sem()
    sem_ON_mod_role['sem_ONM_%s'% col_name]=results_role.groupby('Treatment')['ONM_%s'% col_name].sem()
    sem_ON_mod_role['sem_ONF_%s'% col_name]=results_role.groupby('Treatment')['ONF_%s'% col_name].sem()
    sem_ON_mod_role['sem_ONCR_%s'% col_name]=results_role.groupby('Treatment')['ONCR_%s'% col_name].sem()
    sem_ON_mod_role['sem_ONFR_%s'% col_name]=results_role.groupby('Treatment')['ONFR_%s'% col_name].sem()
    sem_TN_mod_role['sem_ONW_%s'% col_name]=results_role.groupby('Treatment')['ONW_%s'% col_name].sem()
    sem_TN_mod_role['sem_ONL_%s'% col_name]=results_role.groupby('Treatment')['ONL_%s'% col_name].sem()
    sem_TN_mod_role['sem_ONO_%s'% col_name]=results_role.groupby('Treatment')['ONO_%s'% col_name].sem()
    sem_BN_mod_role['sem_BNM_%s'% col_name]=results_role.groupby('Treatment')['BNM_%s'% col_name].sem()
    sem_BN_mod_role['sem_BNF_%s'% col_name]=results_role.groupby('Treatment')['BNF_%s'% col_name].sem()
    sem_BN_mod_role['sem_BNCR_%s'% col_name]=results_role.groupby('Treatment')['BNCR_%s'% col_name].sem()
    sem_BN_mod_role['sem_BNFR_%s'% col_name]=results_role.groupby('Treatment')['BNFR_%s'% col_name].sem()
    sem_TN_mod_role['sem_BNW_%s'% col_name]=results_role.groupby('Treatment')['BNW_%s'% col_name].sem()
    sem_TN_mod_role['sem_BNL_%s'% col_name]=results_role.groupby('Treatment')['BNL_%s'% col_name].sem()
    sem_TN_mod_role['sem_BNO_%s'% col_name]=results_role.groupby('Treatment')['BNO_%s'% col_name].sem()
                   
    sem_TD_mod_role['sem_TDM_%s'% col_name]=results_role.groupby('Treatment')['TDM_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDF_%s'% col_name]=results_role.groupby('Treatment')['TDF_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDCR_%s'% col_name]=results_role.groupby('Treatment')['TDCR_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDFR_%s'% col_name]=results_role.groupby('Treatment')['TDFR_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDW_%s'% col_name]=results_role.groupby('Treatment')['TDW_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDL_%s'% col_name]=results_role.groupby('Treatment')['TDL_%s'% col_name].sem()
    sem_TD_mod_role['sem_TDO_%s'% col_name]=results_role.groupby('Treatment')['TDO_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODM_%s'% col_name]=results_role.groupby('Treatment')['ODM_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODF_%s'% col_name]=results_role.groupby('Treatment')['ODF_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODCR_%s'% col_name]=results_role.groupby('Treatment')['ODCR_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODFR_%s'% col_name]=results_role.groupby('Treatment')['ODFR_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODW_%s'% col_name]=results_role.groupby('Treatment')['ODW_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODL_%s'% col_name]=results_role.groupby('Treatment')['ODL_%s'% col_name].sem()
    sem_OD_mod_role['sem_ODO_%s'% col_name]=results_role.groupby('Treatment')['ODO_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDM_%s'% col_name]=results_role.groupby('Treatment')['BDM_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDF_%s'% col_name]=results_role.groupby('Treatment')['BDF_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDCR_%s'% col_name]=results_role.groupby('Treatment')['BDCR_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDFR_%s'% col_name]=results_role.groupby('Treatment')['BDFR_%s'% col_name].sem()                   
    sem_BD_mod_role['sem_BDW_%s'% col_name]=results_role.groupby('Treatment')['BDW_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDL_%s'% col_name]=results_role.groupby('Treatment')['BDL_%s'% col_name].sem()
    sem_BD_mod_role['sem_BDO_%s'% col_name]=results_role.groupby('Treatment')['BDO_%s'% col_name].sem()
         
    sem_TN_modtreat_role['sem_TNCF_%s'% col_name]=results_role.groupby('Treatment')['TNCF_%s'% col_name].sem()
    sem_TN_modtreat_role['sem_TNFF_%s'% col_name]=results_role.groupby('Treatment')['TNFF_%s'% col_name].sem()
    sem_TN_modtreat_role['sem_TNCM_%s'% col_name]=results_role.groupby('Treatment')['TNCM_%s'% col_name].sem()
    sem_TN_modtreat_role['sem_TNFM_%s'% col_name]=results_role.groupby('Treatment')['TNFM_%s'% col_name].sem()
    sem_ON_modtreat_role['sem_ONCF_%s'% col_name]=results_role.groupby('Treatment')['ONCF_%s'% col_name].sem()
    sem_ON_modtreat_role['sem_ONFF_%s'% col_name]=results_role.groupby('Treatment')['ONFF_%s'% col_name].sem()
    sem_ON_modtreat_role['sem_ONCM_%s'% col_name]=results_role.groupby('Treatment')['ONCM_%s'% col_name].sem()
    sem_ON_modtreat_role['sem_ONFM_%s'% col_name]=results_role.groupby('Treatment')['ONFM_%s'% col_name].sem()
    sem_BN_modtreat_role['sem_BNCF_%s'% col_name]=results_role.groupby('Treatment')['BNCF_%s'% col_name].sem()
    sem_BN_modtreat_role['sem_BNFF_%s'% col_name]=results_role.groupby('Treatment')['BNFF_%s'% col_name].sem()
    sem_BN_modtreat_role['sem_BNCM_%s'% col_name]=results_role.groupby('Treatment')['BNCM_%s'% col_name].sem()
    sem_BN_modtreat_role['sem_BNFM_%s'% col_name]=results_role.groupby('Treatment')['BNFM_%s'% col_name].sem()

    sem_TD_modtreat_role['sem_TDCF_%s'% col_name]=results_role.groupby('Treatment')['TDCF_%s'% col_name].sem()
    sem_TD_modtreat_role['sem_TDFF_%s'% col_name]=results_role.groupby('Treatment')['TDFF_%s'% col_name].sem()
    sem_TD_modtreat_role['sem_TDCM_%s'% col_name]=results_role.groupby('Treatment')['TDCM_%s'% col_name].sem()
    sem_TD_modtreat_role['sem_TDFM_%s'% col_name]=results_role.groupby('Treatment')['TDFM_%s'% col_name].sem()
    sem_OD_modtreat_role['sem_ODCF_%s'% col_name]=results_role.groupby('Treatment')['ODCF_%s'% col_name].sem()
    sem_OD_modtreat_role['sem_ODFF_%s'% col_name]=results_role.groupby('Treatment')['ODFF_%s'% col_name].sem()
    sem_OD_modtreat_role['sem_ODCM_%s'% col_name]=results_role.groupby('Treatment')['ODCM_%s'% col_name].sem()
    sem_OD_modtreat_role['sem_ODFM_%s'% col_name]=results_role.groupby('Treatment')['ODFM_%s'% col_name].sem()
    sem_BD_modtreat_role['sem_BDCF_%s'% col_name]=results_role.groupby('Treatment')['BDCF_%s'% col_name].sem()
    sem_BD_modtreat_role['sem_BDFF_%s'% col_name]=results_role.groupby('Treatment')['BDFF_%s'% col_name].sem()
    sem_BD_modtreat_role['sem_BDCM_%s'% col_name]=results_role.groupby('Treatment')['BDCM_%s'% col_name].sem()
    sem_BD_modtreat_role['sem_BDFM_%s'% col_name]=results_role.groupby('Treatment')['BDFM_%s'% col_name].sem()    

sem_TN_mod_role_columns=list(sem_TN_mod_role.columns.values)
sem_TD_mod_role_columns=list(sem_TD_mod_role.columns.values)
sem_TN_modtreat_role_columns=list(sem_TN_modtreat_role.columns.values)
sem_TD_modtreat_role_columns=list(sem_TD_modtreat_role.columns.values)    
sem_ON_mod_role_columns=list(sem_ON_mod_role.columns.values)
sem_OD_mod_role_columns=list(sem_OD_mod_role.columns.values)
sem_ON_modtreat_role_columns=list(sem_ON_modtreat_role.columns.values)
sem_OD_modtreat_role_columns=list(sem_OD_modtreat_role.columns.values)  
sem_BN_mod_role_columns=list(sem_BN_mod_role.columns.values)
sem_BD_mod_role_columns=list(sem_BD_mod_role.columns.values)
sem_BN_modtreat_role_columns=list(sem_BN_modtreat_role.columns.values)
sem_BD_modtreat_role_columns=list(sem_BD_modtreat_role.columns.values)  

# NOW FOR ROLEPLUS
# Statistics on the data
# SEM
sem_Total_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].sem()
sem_Total_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Total_roleplus['sem_TD_%s'% col_name]=results_roleplus.groupby('RatID')['TD_%s'% col_name].sem()
    sem_Total_roleplus['sem_TN_%s'% col_name]=results_roleplus.groupby('RatID')['TN_%s'% col_name].sem()

sem_OF_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].sem()
sem_OF_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_OF_roleplus['sem_OD_%s'% col_name]=results_roleplus.groupby('RatID')['OD_%s'% col_name].sem()
    sem_OF_roleplus['sem_ON_%s'% col_name]=results_roleplus.groupby('RatID')['ON_%s'% col_name].sem()

sem_Burrow_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].sem()
sem_Burrow_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    sem_Burrow_roleplus['sem_BD_%s'% col_name]=results_roleplus.groupby('RatID')['BD_%s'% col_name].sem()
    sem_Burrow_roleplus['sem_BN_%s'% col_name]=results_roleplus.groupby('RatID')['BN_%s'% col_name].sem()

sem_Total_roleplus_columns=list(sem_Total_roleplus.columns.values)
sem_OF_roleplus_columns=list(sem_OF_roleplus.columns.values)
sem_Burrow_roleplus_columns=list(sem_Burrow_roleplus.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    sem_TN_mod_roleplus['sem_TNM_%s'% col_name]=results_roleplus.groupby('RatID')['TNM_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNF_%s'% col_name]=results_roleplus.groupby('RatID')['TNF_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNCR_%s'% col_name]=results_roleplus.groupby('RatID')['TNCR_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNFR_%s'% col_name]=results_roleplus.groupby('RatID')['TNFR_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNW_%s'% col_name]=results_roleplus.groupby('RatID')['TNW_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNL_%s'% col_name]=results_roleplus.groupby('RatID')['TNL_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_TNO_%s'% col_name]=results_roleplus.groupby('RatID')['TNO_%s'% col_name].sem()
    sem_ON_mod_roleplus['sem_ONM_%s'% col_name]=results_roleplus.groupby('RatID')['ONM_%s'% col_name].sem()
    sem_ON_mod_roleplus['sem_ONF_%s'% col_name]=results_roleplus.groupby('RatID')['ONF_%s'% col_name].sem()
    sem_ON_mod_roleplus['sem_ONCR_%s'% col_name]=results_roleplus.groupby('RatID')['ONCR_%s'% col_name].sem()
    sem_ON_mod_roleplus['sem_ONFR_%s'% col_name]=results_roleplus.groupby('RatID')['ONFR_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_ONW_%s'% col_name]=results_roleplus.groupby('RatID')['ONW_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_ONL_%s'% col_name]=results_roleplus.groupby('RatID')['ONL_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_ONO_%s'% col_name]=results_roleplus.groupby('RatID')['ONO_%s'% col_name].sem()
    sem_BN_mod_roleplus['sem_BNM_%s'% col_name]=results_roleplus.groupby('RatID')['BNM_%s'% col_name].sem()
    sem_BN_mod_roleplus['sem_BNF_%s'% col_name]=results_roleplus.groupby('RatID')['BNF_%s'% col_name].sem()
    sem_BN_mod_roleplus['sem_BNCR_%s'% col_name]=results_roleplus.groupby('RatID')['BNCR_%s'% col_name].sem()
    sem_BN_mod_roleplus['sem_BNFR_%s'% col_name]=results_roleplus.groupby('RatID')['BNFR_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_BNW_%s'% col_name]=results_roleplus.groupby('RatID')['BNW_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_BNL_%s'% col_name]=results_roleplus.groupby('RatID')['BNL_%s'% col_name].sem()
    sem_TN_mod_roleplus['sem_BNO_%s'% col_name]=results_roleplus.groupby('RatID')['BNO_%s'% col_name].sem()
                   
    sem_TD_mod_roleplus['sem_TDM_%s'% col_name]=results_roleplus.groupby('RatID')['TDM_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDF_%s'% col_name]=results_roleplus.groupby('RatID')['TDF_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDCR_%s'% col_name]=results_roleplus.groupby('RatID')['TDCR_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDFR_%s'% col_name]=results_roleplus.groupby('RatID')['TDFR_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDW_%s'% col_name]=results_roleplus.groupby('RatID')['TDW_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDL_%s'% col_name]=results_roleplus.groupby('RatID')['TDL_%s'% col_name].sem()
    sem_TD_mod_roleplus['sem_TDO_%s'% col_name]=results_roleplus.groupby('RatID')['TDO_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODM_%s'% col_name]=results_roleplus.groupby('RatID')['ODM_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODF_%s'% col_name]=results_roleplus.groupby('RatID')['ODF_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODCR_%s'% col_name]=results_roleplus.groupby('RatID')['ODCR_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODFR_%s'% col_name]=results_roleplus.groupby('RatID')['ODFR_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODW_%s'% col_name]=results_roleplus.groupby('RatID')['ODW_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODL_%s'% col_name]=results_roleplus.groupby('RatID')['ODL_%s'% col_name].sem()
    sem_OD_mod_roleplus['sem_ODO_%s'% col_name]=results_roleplus.groupby('RatID')['ODO_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDM_%s'% col_name]=results_roleplus.groupby('RatID')['BDM_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDF_%s'% col_name]=results_roleplus.groupby('RatID')['BDF_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDCR_%s'% col_name]=results_roleplus.groupby('RatID')['BDCR_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDFR_%s'% col_name]=results_roleplus.groupby('RatID')['BDFR_%s'% col_name].sem()                   
    sem_BD_mod_roleplus['sem_BDW_%s'% col_name]=results_roleplus.groupby('RatID')['BDW_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDL_%s'% col_name]=results_roleplus.groupby('RatID')['BDL_%s'% col_name].sem()
    sem_BD_mod_roleplus['sem_BDO_%s'% col_name]=results_roleplus.groupby('RatID')['BDO_%s'% col_name].sem()
         
    sem_TN_modtreat_roleplus['sem_TNCF_%s'% col_name]=results_roleplus.groupby('RatID')['TNCF_%s'% col_name].sem()
    sem_TN_modtreat_roleplus['sem_TNFF_%s'% col_name]=results_roleplus.groupby('RatID')['TNFF_%s'% col_name].sem()
    sem_TN_modtreat_roleplus['sem_TNCM_%s'% col_name]=results_roleplus.groupby('RatID')['TNCM_%s'% col_name].sem()
    sem_TN_modtreat_roleplus['sem_TNFM_%s'% col_name]=results_roleplus.groupby('RatID')['TNFM_%s'% col_name].sem()
    sem_ON_modtreat_roleplus['sem_ONCF_%s'% col_name]=results_roleplus.groupby('RatID')['ONCF_%s'% col_name].sem()
    sem_ON_modtreat_roleplus['sem_ONFF_%s'% col_name]=results_roleplus.groupby('RatID')['ONFF_%s'% col_name].sem()
    sem_ON_modtreat_roleplus['sem_ONCM_%s'% col_name]=results_roleplus.groupby('RatID')['ONCM_%s'% col_name].sem()
    sem_ON_modtreat_roleplus['sem_ONFM_%s'% col_name]=results_roleplus.groupby('RatID')['ONFM_%s'% col_name].sem()
    sem_BN_modtreat_roleplus['sem_BNCF_%s'% col_name]=results_roleplus.groupby('RatID')['BNCF_%s'% col_name].sem()
    sem_BN_modtreat_roleplus['sem_BNFF_%s'% col_name]=results_roleplus.groupby('RatID')['BNFF_%s'% col_name].sem()
    sem_BN_modtreat_roleplus['sem_BNCM_%s'% col_name]=results_roleplus.groupby('RatID')['BNCM_%s'% col_name].sem()
    sem_BN_modtreat_roleplus['sem_BNFM_%s'% col_name]=results_roleplus.groupby('RatID')['BNFM_%s'% col_name].sem()

    sem_TD_modtreat_roleplus['sem_TDCF_%s'% col_name]=results_roleplus.groupby('RatID')['TDCF_%s'% col_name].sem()
    sem_TD_modtreat_roleplus['sem_TDFF_%s'% col_name]=results_roleplus.groupby('RatID')['TDFF_%s'% col_name].sem()
    sem_TD_modtreat_roleplus['sem_TDCM_%s'% col_name]=results_roleplus.groupby('RatID')['TDCM_%s'% col_name].sem()
    sem_TD_modtreat_roleplus['sem_TDFM_%s'% col_name]=results_roleplus.groupby('RatID')['TDFM_%s'% col_name].sem()
    sem_OD_modtreat_roleplus['sem_ODCF_%s'% col_name]=results_roleplus.groupby('RatID')['ODCF_%s'% col_name].sem()
    sem_OD_modtreat_roleplus['sem_ODFF_%s'% col_name]=results_roleplus.groupby('RatID')['ODFF_%s'% col_name].sem()
    sem_OD_modtreat_roleplus['sem_ODCM_%s'% col_name]=results_roleplus.groupby('RatID')['ODCM_%s'% col_name].sem()
    sem_OD_modtreat_roleplus['sem_ODFM_%s'% col_name]=results_roleplus.groupby('RatID')['ODFM_%s'% col_name].sem()
    sem_BD_modtreat_roleplus['sem_BDCF_%s'% col_name]=results_roleplus.groupby('RatID')['BDCF_%s'% col_name].sem()
    sem_BD_modtreat_roleplus['sem_BDFF_%s'% col_name]=results_roleplus.groupby('RatID')['BDFF_%s'% col_name].sem()
    sem_BD_modtreat_roleplus['sem_BDCM_%s'% col_name]=results_roleplus.groupby('RatID')['BDCM_%s'% col_name].sem()
    sem_BD_modtreat_roleplus['sem_BDFM_%s'% col_name]=results_roleplus.groupby('RatID')['BDFM_%s'% col_name].sem()    

sem_TN_mod_roleplus_columns=list(sem_TN_mod_roleplus.columns.values)
sem_TD_mod_roleplus_columns=list(sem_TD_mod_roleplus.columns.values)
sem_TN_modtreat_roleplus_columns=list(sem_TN_modtreat_roleplus.columns.values)
sem_TD_modtreat_roleplus_columns=list(sem_TD_modtreat_roleplus.columns.values)    
sem_ON_mod_roleplus_columns=list(sem_ON_mod_roleplus.columns.values)
sem_OD_mod_roleplus_columns=list(sem_OD_mod_roleplus.columns.values)
sem_ON_modtreat_roleplus_columns=list(sem_ON_modtreat_roleplus.columns.values)
sem_OD_modtreat_roleplus_columns=list(sem_OD_modtreat_roleplus.columns.values)  
sem_BN_mod_roleplus_columns=list(sem_BN_mod_roleplus.columns.values)
sem_BD_mod_roleplus_columns=list(sem_BD_mod_roleplus.columns.values)
sem_BN_modtreat_roleplus_columns=list(sem_BN_modtreat_roleplus.columns.values)
sem_BD_modtreat_roleplus_columns=list(sem_BD_modtreat_roleplus.columns.values)  


# Statistics on the data
# STD
std_TN_mod_fight=pd.DataFrame()
std_ON_mod_fight=pd.DataFrame()
std_BN_mod_fight=pd.DataFrame()
std_TD_mod_fight=pd.DataFrame()
std_OD_mod_fight=pd.DataFrame()
std_BD_mod_fight=pd.DataFrame()
std_TN_modtreat_fight=pd.DataFrame()
std_ON_modtreat_fight=pd.DataFrame()
std_BN_modtreat_fight=pd.DataFrame()
std_TD_modtreat_fight=pd.DataFrame()
std_OD_modtreat_fight=pd.DataFrame()
std_BD_modtreat_fight=pd.DataFrame()

std_TN_mod_role=pd.DataFrame()
std_ON_mod_role=pd.DataFrame()
std_BN_mod_role=pd.DataFrame()
std_TD_mod_role=pd.DataFrame()
std_OD_mod_role=pd.DataFrame()
std_BD_mod_role=pd.DataFrame()
std_TN_modtreat_role=pd.DataFrame()
std_ON_modtreat_role=pd.DataFrame()
std_BN_modtreat_role=pd.DataFrame()
std_TD_modtreat_role=pd.DataFrame()
std_OD_modtreat_role=pd.DataFrame()
std_BD_modtreat_role=pd.DataFrame()

std_TN_mod_roleplus=pd.DataFrame()
std_ON_mod_roleplus=pd.DataFrame()
std_BN_mod_roleplus=pd.DataFrame()
std_TD_mod_roleplus=pd.DataFrame()
std_OD_mod_roleplus=pd.DataFrame()
std_BD_mod_roleplus=pd.DataFrame()
std_TN_modtreat_roleplus=pd.DataFrame()
std_ON_modtreat_roleplus=pd.DataFrame()
std_BN_modtreat_roleplus=pd.DataFrame()
std_TD_modtreat_roleplus=pd.DataFrame()
std_OD_modtreat_roleplus=pd.DataFrame()
std_BD_modtreat_roleplus=pd.DataFrame()

std_Total_fight=results_fight.groupby('Treatment')['Cohort','Day'].std()
std_Total_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Total_fight['std_TD_%s'% col_name]=results_fight.groupby('Treatment')['TD_%s'% col_name].std()
    std_Total_fight['std_TN_%s'% col_name]=results_fight.groupby('Treatment')['TN_%s'% col_name].std()

std_OF_fight=results_fight.groupby('Treatment')['Cohort','Day'].std()
std_OF_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_OF_fight['std_OD_%s'% col_name]=results_fight.groupby('Treatment')['OD_%s'% col_name].std()
    std_OF_fight['std_ON_%s'% col_name]=results_fight.groupby('Treatment')['ON_%s'% col_name].std()

std_Burrow_fight=results_fight.groupby('Treatment')['Cohort','Day'].std()
std_Burrow_fight.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Burrow_fight['std_BD_%s'% col_name]=results_fight.groupby('Treatment')['BD_%s'% col_name].std()
    std_Burrow_fight['std_BN_%s'% col_name]=results_fight.groupby('Treatment')['BN_%s'% col_name].std()

std_Total_fight_columns=list(std_Total_fight.columns.values)
std_OF_fight_columns=list(std_OF_fight.columns.values)
std_Burrow_fight_columns=list(std_Burrow_fight.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    std_TN_mod_fight['std_TNM_%s'% col_name]=results_fight.groupby('Treatment')['TNM_%s'% col_name].std()
    std_TN_mod_fight['std_TNF_%s'% col_name]=results_fight.groupby('Treatment')['TNF_%s'% col_name].std()
    std_TN_mod_fight['std_TNCR_%s'% col_name]=results_fight.groupby('Treatment')['TNCR_%s'% col_name].std()
    std_TN_mod_fight['std_TNFR_%s'% col_name]=results_fight.groupby('Treatment')['TNFR_%s'% col_name].std()
    std_TN_mod_fight['std_TNW_%s'% col_name]=results_fight.groupby('Treatment')['TNW_%s'% col_name].std()
    std_TN_mod_fight['std_TNL_%s'% col_name]=results_fight.groupby('Treatment')['TNL_%s'% col_name].std()
    std_TN_mod_fight['std_TNO_%s'% col_name]=results_fight.groupby('Treatment')['TNO_%s'% col_name].std()
    std_ON_mod_fight['std_ONM_%s'% col_name]=results_fight.groupby('Treatment')['ONM_%s'% col_name].std()
    std_ON_mod_fight['std_ONF_%s'% col_name]=results_fight.groupby('Treatment')['ONF_%s'% col_name].std()
    std_ON_mod_fight['std_ONCR_%s'% col_name]=results_fight.groupby('Treatment')['ONCR_%s'% col_name].std()
    std_ON_mod_fight['std_ONFR_%s'% col_name]=results_fight.groupby('Treatment')['ONFR_%s'% col_name].std()
    std_TN_mod_fight['std_ONW_%s'% col_name]=results_fight.groupby('Treatment')['ONW_%s'% col_name].std()
    std_TN_mod_fight['std_ONL_%s'% col_name]=results_fight.groupby('Treatment')['ONL_%s'% col_name].std()
    std_TN_mod_fight['std_ONO_%s'% col_name]=results_fight.groupby('Treatment')['ONO_%s'% col_name].std()
    std_BN_mod_fight['std_BNM_%s'% col_name]=results_fight.groupby('Treatment')['BNM_%s'% col_name].std()
    std_BN_mod_fight['std_BNF_%s'% col_name]=results_fight.groupby('Treatment')['BNF_%s'% col_name].std()
    std_BN_mod_fight['std_BNCR_%s'% col_name]=results_fight.groupby('Treatment')['BNCR_%s'% col_name].std()
    std_BN_mod_fight['std_BNFR_%s'% col_name]=results_fight.groupby('Treatment')['BNFR_%s'% col_name].std()
    std_TN_mod_fight['std_BNW_%s'% col_name]=results_fight.groupby('Treatment')['BNW_%s'% col_name].std()
    std_TN_mod_fight['std_BNL_%s'% col_name]=results_fight.groupby('Treatment')['BNL_%s'% col_name].std()
    std_TN_mod_fight['std_BNO_%s'% col_name]=results_fight.groupby('Treatment')['BNO_%s'% col_name].std()
                   
    std_TD_mod_fight['std_TDM_%s'% col_name]=results_fight.groupby('Treatment')['TDM_%s'% col_name].std()
    std_TD_mod_fight['std_TDF_%s'% col_name]=results_fight.groupby('Treatment')['TDF_%s'% col_name].std()
    std_TD_mod_fight['std_TDCR_%s'% col_name]=results_fight.groupby('Treatment')['TDCR_%s'% col_name].std()
    std_TD_mod_fight['std_TDFR_%s'% col_name]=results_fight.groupby('Treatment')['TDFR_%s'% col_name].std()
    std_TD_mod_fight['std_TDW_%s'% col_name]=results_fight.groupby('Treatment')['TDW_%s'% col_name].std()
    std_TD_mod_fight['std_TDL_%s'% col_name]=results_fight.groupby('Treatment')['TDL_%s'% col_name].std()
    std_TD_mod_fight['std_TDO_%s'% col_name]=results_fight.groupby('Treatment')['TDO_%s'% col_name].std()
    std_OD_mod_fight['std_ODM_%s'% col_name]=results_fight.groupby('Treatment')['ODM_%s'% col_name].std()
    std_OD_mod_fight['std_ODF_%s'% col_name]=results_fight.groupby('Treatment')['ODF_%s'% col_name].std()
    std_OD_mod_fight['std_ODCR_%s'% col_name]=results_fight.groupby('Treatment')['ODCR_%s'% col_name].std()
    std_OD_mod_fight['std_ODFR_%s'% col_name]=results_fight.groupby('Treatment')['ODFR_%s'% col_name].std()
    std_OD_mod_fight['std_ODW_%s'% col_name]=results_fight.groupby('Treatment')['ODW_%s'% col_name].std()
    std_OD_mod_fight['std_ODL_%s'% col_name]=results_fight.groupby('Treatment')['ODL_%s'% col_name].std()
    std_OD_mod_fight['std_ODO_%s'% col_name]=results_fight.groupby('Treatment')['ODO_%s'% col_name].std()
    std_BD_mod_fight['std_BDM_%s'% col_name]=results_fight.groupby('Treatment')['BDM_%s'% col_name].std()
    std_BD_mod_fight['std_BDF_%s'% col_name]=results_fight.groupby('Treatment')['BDF_%s'% col_name].std()
    std_BD_mod_fight['std_BDCR_%s'% col_name]=results_fight.groupby('Treatment')['BDCR_%s'% col_name].std()
    std_BD_mod_fight['std_BDFR_%s'% col_name]=results_fight.groupby('Treatment')['BDFR_%s'% col_name].std()                   
    std_BD_mod_fight['std_BDW_%s'% col_name]=results_fight.groupby('Treatment')['BDW_%s'% col_name].std()
    std_BD_mod_fight['std_BDL_%s'% col_name]=results_fight.groupby('Treatment')['BDL_%s'% col_name].std()
    std_BD_mod_fight['std_BDO_%s'% col_name]=results_fight.groupby('Treatment')['BDO_%s'% col_name].std()
         
    std_TN_modtreat_fight['std_TNCF_%s'% col_name]=results_fight.groupby('Treatment')['TNCF_%s'% col_name].std()
    std_TN_modtreat_fight['std_TNFF_%s'% col_name]=results_fight.groupby('Treatment')['TNFF_%s'% col_name].std()
    std_TN_modtreat_fight['std_TNCM_%s'% col_name]=results_fight.groupby('Treatment')['TNCM_%s'% col_name].std()
    std_TN_modtreat_fight['std_TNFM_%s'% col_name]=results_fight.groupby('Treatment')['TNFM_%s'% col_name].std()
    std_ON_modtreat_fight['std_ONCF_%s'% col_name]=results_fight.groupby('Treatment')['ONCF_%s'% col_name].std()
    std_ON_modtreat_fight['std_ONFF_%s'% col_name]=results_fight.groupby('Treatment')['ONFF_%s'% col_name].std()
    std_ON_modtreat_fight['std_ONCM_%s'% col_name]=results_fight.groupby('Treatment')['ONCM_%s'% col_name].std()
    std_ON_modtreat_fight['std_ONFM_%s'% col_name]=results_fight.groupby('Treatment')['ONFM_%s'% col_name].std()
    std_BN_modtreat_fight['std_BNCF_%s'% col_name]=results_fight.groupby('Treatment')['BNCF_%s'% col_name].std()
    std_BN_modtreat_fight['std_BNFF_%s'% col_name]=results_fight.groupby('Treatment')['BNFF_%s'% col_name].std()
    std_BN_modtreat_fight['std_BNCM_%s'% col_name]=results_fight.groupby('Treatment')['BNCM_%s'% col_name].std()
    std_BN_modtreat_fight['std_BNFM_%s'% col_name]=results_fight.groupby('Treatment')['BNFM_%s'% col_name].std()

    std_TD_modtreat_fight['std_TDCF_%s'% col_name]=results_fight.groupby('Treatment')['TDCF_%s'% col_name].std()
    std_TD_modtreat_fight['std_TDFF_%s'% col_name]=results_fight.groupby('Treatment')['TDFF_%s'% col_name].std()
    std_TD_modtreat_fight['std_TDCM_%s'% col_name]=results_fight.groupby('Treatment')['TDCM_%s'% col_name].std()
    std_TD_modtreat_fight['std_TDFM_%s'% col_name]=results_fight.groupby('Treatment')['TDFM_%s'% col_name].std()
    std_OD_modtreat_fight['std_ODCF_%s'% col_name]=results_fight.groupby('Treatment')['ODCF_%s'% col_name].std()
    std_OD_modtreat_fight['std_ODFF_%s'% col_name]=results_fight.groupby('Treatment')['ODFF_%s'% col_name].std()
    std_OD_modtreat_fight['std_ODCM_%s'% col_name]=results_fight.groupby('Treatment')['ODCM_%s'% col_name].std()
    std_OD_modtreat_fight['std_ODFM_%s'% col_name]=results_fight.groupby('Treatment')['ODFM_%s'% col_name].std()
    std_BD_modtreat_fight['std_BDCF_%s'% col_name]=results_fight.groupby('Treatment')['BDCF_%s'% col_name].std()
    std_BD_modtreat_fight['std_BDFF_%s'% col_name]=results_fight.groupby('Treatment')['BDFF_%s'% col_name].std()
    std_BD_modtreat_fight['std_BDCM_%s'% col_name]=results_fight.groupby('Treatment')['BDCM_%s'% col_name].std()
    std_BD_modtreat_fight['std_BDFM_%s'% col_name]=results_fight.groupby('Treatment')['BDFM_%s'% col_name].std()    

std_TN_mod_fight_columns=list(std_TN_mod_fight.columns.values)
std_TD_mod_fight_columns=list(std_TD_mod_fight.columns.values)
std_TN_modtreat_fight_columns=list(std_TN_modtreat_fight.columns.values)
std_TD_modtreat_fight_columns=list(std_TD_modtreat_fight.columns.values)    
std_ON_mod_fight_columns=list(std_ON_mod_fight.columns.values)
std_OD_mod_fight_columns=list(std_OD_mod_fight.columns.values)
std_ON_modtreat_fight_columns=list(std_ON_modtreat_fight.columns.values)
std_OD_modtreat_fight_columns=list(std_OD_modtreat_fight.columns.values)  
std_BN_mod_fight_columns=list(std_BN_mod_fight.columns.values)
std_BD_mod_fight_columns=list(std_BD_mod_fight.columns.values)
std_BN_modtreat_fight_columns=list(std_BN_modtreat_fight.columns.values)
std_BD_modtreat_fight_columns=list(std_BD_modtreat_fight.columns.values)  

# NOW FOR ROLE
# Statistics on the data
# STD
std_Total_role=results_role.groupby('Treatment')['Cohort','Day'].std()
std_Total_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Total_role['std_TD_%s'% col_name]=results_role.groupby('Treatment')['TD_%s'% col_name].std()
    std_Total_role['std_TN_%s'% col_name]=results_role.groupby('Treatment')['TN_%s'% col_name].std()

std_OF_role=results_role.groupby('Treatment')['Cohort','Day'].std()
std_OF_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_OF_role['std_OD_%s'% col_name]=results_role.groupby('Treatment')['OD_%s'% col_name].std()
    std_OF_role['std_ON_%s'% col_name]=results_role.groupby('Treatment')['ON_%s'% col_name].std()

std_Burrow_role=results_role.groupby('Treatment')['Cohort','Day'].std()
std_Burrow_role.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Burrow_role['std_BD_%s'% col_name]=results_role.groupby('Treatment')['BD_%s'% col_name].std()
    std_Burrow_role['std_BN_%s'% col_name]=results_role.groupby('Treatment')['BN_%s'% col_name].std()

std_Total_role_columns=list(std_Total_role.columns.values)
std_OF_role_columns=list(std_OF_role.columns.values)
std_Burrow_role_columns=list(std_Burrow_role.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    std_TN_mod_role['std_TNM_%s'% col_name]=results_role.groupby('Treatment')['TNM_%s'% col_name].std()
    std_TN_mod_role['std_TNF_%s'% col_name]=results_role.groupby('Treatment')['TNF_%s'% col_name].std()
    std_TN_mod_role['std_TNCR_%s'% col_name]=results_role.groupby('Treatment')['TNCR_%s'% col_name].std()
    std_TN_mod_role['std_TNFR_%s'% col_name]=results_role.groupby('Treatment')['TNFR_%s'% col_name].std()
    std_TN_mod_role['std_TNW_%s'% col_name]=results_role.groupby('Treatment')['TNW_%s'% col_name].std()
    std_TN_mod_role['std_TNL_%s'% col_name]=results_role.groupby('Treatment')['TNL_%s'% col_name].std()
    std_TN_mod_role['std_TNO_%s'% col_name]=results_role.groupby('Treatment')['TNO_%s'% col_name].std()
    std_ON_mod_role['std_ONM_%s'% col_name]=results_role.groupby('Treatment')['ONM_%s'% col_name].std()
    std_ON_mod_role['std_ONF_%s'% col_name]=results_role.groupby('Treatment')['ONF_%s'% col_name].std()
    std_ON_mod_role['std_ONCR_%s'% col_name]=results_role.groupby('Treatment')['ONCR_%s'% col_name].std()
    std_ON_mod_role['std_ONFR_%s'% col_name]=results_role.groupby('Treatment')['ONFR_%s'% col_name].std()
    std_TN_mod_role['std_ONW_%s'% col_name]=results_role.groupby('Treatment')['ONW_%s'% col_name].std()
    std_TN_mod_role['std_ONL_%s'% col_name]=results_role.groupby('Treatment')['ONL_%s'% col_name].std()
    std_TN_mod_role['std_ONO_%s'% col_name]=results_role.groupby('Treatment')['ONO_%s'% col_name].std()
    std_BN_mod_role['std_BNM_%s'% col_name]=results_role.groupby('Treatment')['BNM_%s'% col_name].std()
    std_BN_mod_role['std_BNF_%s'% col_name]=results_role.groupby('Treatment')['BNF_%s'% col_name].std()
    std_BN_mod_role['std_BNCR_%s'% col_name]=results_role.groupby('Treatment')['BNCR_%s'% col_name].std()
    std_BN_mod_role['std_BNFR_%s'% col_name]=results_role.groupby('Treatment')['BNFR_%s'% col_name].std()
    std_TN_mod_role['std_BNW_%s'% col_name]=results_role.groupby('Treatment')['BNW_%s'% col_name].std()
    std_TN_mod_role['std_BNL_%s'% col_name]=results_role.groupby('Treatment')['BNL_%s'% col_name].std()
    std_TN_mod_role['std_BNO_%s'% col_name]=results_role.groupby('Treatment')['BNO_%s'% col_name].std()
                   
    std_TD_mod_role['std_TDM_%s'% col_name]=results_role.groupby('Treatment')['TDM_%s'% col_name].std()
    std_TD_mod_role['std_TDF_%s'% col_name]=results_role.groupby('Treatment')['TDF_%s'% col_name].std()
    std_TD_mod_role['std_TDCR_%s'% col_name]=results_role.groupby('Treatment')['TDCR_%s'% col_name].std()
    std_TD_mod_role['std_TDFR_%s'% col_name]=results_role.groupby('Treatment')['TDFR_%s'% col_name].std()
    std_TD_mod_role['std_TDW_%s'% col_name]=results_role.groupby('Treatment')['TDW_%s'% col_name].std()
    std_TD_mod_role['std_TDL_%s'% col_name]=results_role.groupby('Treatment')['TDL_%s'% col_name].std()
    std_TD_mod_role['std_TDO_%s'% col_name]=results_role.groupby('Treatment')['TDO_%s'% col_name].std()
    std_OD_mod_role['std_ODM_%s'% col_name]=results_role.groupby('Treatment')['ODM_%s'% col_name].std()
    std_OD_mod_role['std_ODF_%s'% col_name]=results_role.groupby('Treatment')['ODF_%s'% col_name].std()
    std_OD_mod_role['std_ODCR_%s'% col_name]=results_role.groupby('Treatment')['ODCR_%s'% col_name].std()
    std_OD_mod_role['std_ODFR_%s'% col_name]=results_role.groupby('Treatment')['ODFR_%s'% col_name].std()
    std_OD_mod_role['std_ODW_%s'% col_name]=results_role.groupby('Treatment')['ODW_%s'% col_name].std()
    std_OD_mod_role['std_ODL_%s'% col_name]=results_role.groupby('Treatment')['ODL_%s'% col_name].std()
    std_OD_mod_role['std_ODO_%s'% col_name]=results_role.groupby('Treatment')['ODO_%s'% col_name].std()
    std_BD_mod_role['std_BDM_%s'% col_name]=results_role.groupby('Treatment')['BDM_%s'% col_name].std()
    std_BD_mod_role['std_BDF_%s'% col_name]=results_role.groupby('Treatment')['BDF_%s'% col_name].std()
    std_BD_mod_role['std_BDCR_%s'% col_name]=results_role.groupby('Treatment')['BDCR_%s'% col_name].std()
    std_BD_mod_role['std_BDFR_%s'% col_name]=results_role.groupby('Treatment')['BDFR_%s'% col_name].std()                   
    std_BD_mod_role['std_BDW_%s'% col_name]=results_role.groupby('Treatment')['BDW_%s'% col_name].std()
    std_BD_mod_role['std_BDL_%s'% col_name]=results_role.groupby('Treatment')['BDL_%s'% col_name].std()
    std_BD_mod_role['std_BDO_%s'% col_name]=results_role.groupby('Treatment')['BDO_%s'% col_name].std()
         
    std_TN_modtreat_role['std_TNCF_%s'% col_name]=results_role.groupby('Treatment')['TNCF_%s'% col_name].std()
    std_TN_modtreat_role['std_TNFF_%s'% col_name]=results_role.groupby('Treatment')['TNFF_%s'% col_name].std()
    std_TN_modtreat_role['std_TNCM_%s'% col_name]=results_role.groupby('Treatment')['TNCM_%s'% col_name].std()
    std_TN_modtreat_role['std_TNFM_%s'% col_name]=results_role.groupby('Treatment')['TNFM_%s'% col_name].std()
    std_ON_modtreat_role['std_ONCF_%s'% col_name]=results_role.groupby('Treatment')['ONCF_%s'% col_name].std()
    std_ON_modtreat_role['std_ONFF_%s'% col_name]=results_role.groupby('Treatment')['ONFF_%s'% col_name].std()
    std_ON_modtreat_role['std_ONCM_%s'% col_name]=results_role.groupby('Treatment')['ONCM_%s'% col_name].std()
    std_ON_modtreat_role['std_ONFM_%s'% col_name]=results_role.groupby('Treatment')['ONFM_%s'% col_name].std()
    std_BN_modtreat_role['std_BNCF_%s'% col_name]=results_role.groupby('Treatment')['BNCF_%s'% col_name].std()
    std_BN_modtreat_role['std_BNFF_%s'% col_name]=results_role.groupby('Treatment')['BNFF_%s'% col_name].std()
    std_BN_modtreat_role['std_BNCM_%s'% col_name]=results_role.groupby('Treatment')['BNCM_%s'% col_name].std()
    std_BN_modtreat_role['std_BNFM_%s'% col_name]=results_role.groupby('Treatment')['BNFM_%s'% col_name].std()

    std_TD_modtreat_role['std_TDCF_%s'% col_name]=results_role.groupby('Treatment')['TDCF_%s'% col_name].std()
    std_TD_modtreat_role['std_TDFF_%s'% col_name]=results_role.groupby('Treatment')['TDFF_%s'% col_name].std()
    std_TD_modtreat_role['std_TDCM_%s'% col_name]=results_role.groupby('Treatment')['TDCM_%s'% col_name].std()
    std_TD_modtreat_role['std_TDFM_%s'% col_name]=results_role.groupby('Treatment')['TDFM_%s'% col_name].std()
    std_OD_modtreat_role['std_ODCF_%s'% col_name]=results_role.groupby('Treatment')['ODCF_%s'% col_name].std()
    std_OD_modtreat_role['std_ODFF_%s'% col_name]=results_role.groupby('Treatment')['ODFF_%s'% col_name].std()
    std_OD_modtreat_role['std_ODCM_%s'% col_name]=results_role.groupby('Treatment')['ODCM_%s'% col_name].std()
    std_OD_modtreat_role['std_ODFM_%s'% col_name]=results_role.groupby('Treatment')['ODFM_%s'% col_name].std()
    std_BD_modtreat_role['std_BDCF_%s'% col_name]=results_role.groupby('Treatment')['BDCF_%s'% col_name].std()
    std_BD_modtreat_role['std_BDFF_%s'% col_name]=results_role.groupby('Treatment')['BDFF_%s'% col_name].std()
    std_BD_modtreat_role['std_BDCM_%s'% col_name]=results_role.groupby('Treatment')['BDCM_%s'% col_name].std()
    std_BD_modtreat_role['std_BDFM_%s'% col_name]=results_role.groupby('Treatment')['BDFM_%s'% col_name].std()    

std_TN_mod_role_columns=list(std_TN_mod_role.columns.values)
std_TD_mod_role_columns=list(std_TD_mod_role.columns.values)
std_TN_modtreat_role_columns=list(std_TN_modtreat_role.columns.values)
std_TD_modtreat_role_columns=list(std_TD_modtreat_role.columns.values)    
std_ON_mod_role_columns=list(std_ON_mod_role.columns.values)
std_OD_mod_role_columns=list(std_OD_mod_role.columns.values)
std_ON_modtreat_role_columns=list(std_ON_modtreat_role.columns.values)
std_OD_modtreat_role_columns=list(std_OD_modtreat_role.columns.values)  
std_BN_mod_role_columns=list(std_BN_mod_role.columns.values)
std_BD_mod_role_columns=list(std_BD_mod_role.columns.values)
std_BN_modtreat_role_columns=list(std_BN_modtreat_role.columns.values)
std_BD_modtreat_role_columns=list(std_BD_modtreat_role.columns.values)  

# NOW FOR ROLEPLUS
# Statistics on the data
# STD
std_Total_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].std()
std_Total_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Total_roleplus['std_TD_%s'% col_name]=results_roleplus.groupby('RatID')['TD_%s'% col_name].std()
    std_Total_roleplus['std_TN_%s'% col_name]=results_roleplus.groupby('RatID')['TN_%s'% col_name].std()

std_OF_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].std()
std_OF_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_OF_roleplus['std_OD_%s'% col_name]=results_roleplus.groupby('RatID')['OD_%s'% col_name].std()
    std_OF_roleplus['std_ON_%s'% col_name]=results_roleplus.groupby('RatID')['ON_%s'% col_name].std()

std_Burrow_roleplus=results_roleplus.groupby('RatID')['Cohort','Day'].std()
std_Burrow_roleplus.columns=['Cohort','Day']

for position, col_name in enumerate(list_results): 
    std_Burrow_roleplus['std_BD_%s'% col_name]=results_roleplus.groupby('RatID')['BD_%s'% col_name].std()
    std_Burrow_roleplus['std_BN_%s'% col_name]=results_roleplus.groupby('RatID')['BN_%s'% col_name].std()

std_Total_roleplus_columns=list(std_Total_roleplus.columns.values)
std_OF_roleplus_columns=list(std_OF_roleplus.columns.values)
std_Burrow_roleplus_columns=list(std_Burrow_roleplus.columns.values)
                        
for position, col_name in enumerate(list_results_social):     
    std_TN_mod_roleplus['std_TNM_%s'% col_name]=results_roleplus.groupby('RatID')['TNM_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNF_%s'% col_name]=results_roleplus.groupby('RatID')['TNF_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNCR_%s'% col_name]=results_roleplus.groupby('RatID')['TNCR_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNFR_%s'% col_name]=results_roleplus.groupby('RatID')['TNFR_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNW_%s'% col_name]=results_roleplus.groupby('RatID')['TNW_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNL_%s'% col_name]=results_roleplus.groupby('RatID')['TNL_%s'% col_name].std()
    std_TN_mod_roleplus['std_TNO_%s'% col_name]=results_roleplus.groupby('RatID')['TNO_%s'% col_name].std()
    std_ON_mod_roleplus['std_ONM_%s'% col_name]=results_roleplus.groupby('RatID')['ONM_%s'% col_name].std()
    std_ON_mod_roleplus['std_ONF_%s'% col_name]=results_roleplus.groupby('RatID')['ONF_%s'% col_name].std()
    std_ON_mod_roleplus['std_ONCR_%s'% col_name]=results_roleplus.groupby('RatID')['ONCR_%s'% col_name].std()
    std_ON_mod_roleplus['std_ONFR_%s'% col_name]=results_roleplus.groupby('RatID')['ONFR_%s'% col_name].std()
    std_TN_mod_roleplus['std_ONW_%s'% col_name]=results_roleplus.groupby('RatID')['ONW_%s'% col_name].std()
    std_TN_mod_roleplus['std_ONL_%s'% col_name]=results_roleplus.groupby('RatID')['ONL_%s'% col_name].std()
    std_TN_mod_roleplus['std_ONO_%s'% col_name]=results_roleplus.groupby('RatID')['ONO_%s'% col_name].std()
    std_BN_mod_roleplus['std_BNM_%s'% col_name]=results_roleplus.groupby('RatID')['BNM_%s'% col_name].std()
    std_BN_mod_roleplus['std_BNF_%s'% col_name]=results_roleplus.groupby('RatID')['BNF_%s'% col_name].std()
    std_BN_mod_roleplus['std_BNCR_%s'% col_name]=results_roleplus.groupby('RatID')['BNCR_%s'% col_name].std()
    std_BN_mod_roleplus['std_BNFR_%s'% col_name]=results_roleplus.groupby('RatID')['BNFR_%s'% col_name].std()
    std_TN_mod_roleplus['std_BNW_%s'% col_name]=results_roleplus.groupby('RatID')['BNW_%s'% col_name].std()
    std_TN_mod_roleplus['std_BNL_%s'% col_name]=results_roleplus.groupby('RatID')['BNL_%s'% col_name].std()
    std_TN_mod_roleplus['std_BNO_%s'% col_name]=results_roleplus.groupby('RatID')['BNO_%s'% col_name].std()
                   
    std_TD_mod_roleplus['std_TDM_%s'% col_name]=results_roleplus.groupby('RatID')['TDM_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDF_%s'% col_name]=results_roleplus.groupby('RatID')['TDF_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDCR_%s'% col_name]=results_roleplus.groupby('RatID')['TDCR_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDFR_%s'% col_name]=results_roleplus.groupby('RatID')['TDFR_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDW_%s'% col_name]=results_roleplus.groupby('RatID')['TDW_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDL_%s'% col_name]=results_roleplus.groupby('RatID')['TDL_%s'% col_name].std()
    std_TD_mod_roleplus['std_TDO_%s'% col_name]=results_roleplus.groupby('RatID')['TDO_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODM_%s'% col_name]=results_roleplus.groupby('RatID')['ODM_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODF_%s'% col_name]=results_roleplus.groupby('RatID')['ODF_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODCR_%s'% col_name]=results_roleplus.groupby('RatID')['ODCR_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODFR_%s'% col_name]=results_roleplus.groupby('RatID')['ODFR_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODW_%s'% col_name]=results_roleplus.groupby('RatID')['ODW_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODL_%s'% col_name]=results_roleplus.groupby('RatID')['ODL_%s'% col_name].std()
    std_OD_mod_roleplus['std_ODO_%s'% col_name]=results_roleplus.groupby('RatID')['ODO_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDM_%s'% col_name]=results_roleplus.groupby('RatID')['BDM_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDF_%s'% col_name]=results_roleplus.groupby('RatID')['BDF_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDCR_%s'% col_name]=results_roleplus.groupby('RatID')['BDCR_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDFR_%s'% col_name]=results_roleplus.groupby('RatID')['BDFR_%s'% col_name].std()                   
    std_BD_mod_roleplus['std_BDW_%s'% col_name]=results_roleplus.groupby('RatID')['BDW_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDL_%s'% col_name]=results_roleplus.groupby('RatID')['BDL_%s'% col_name].std()
    std_BD_mod_roleplus['std_BDO_%s'% col_name]=results_roleplus.groupby('RatID')['BDO_%s'% col_name].std()
         
    std_TN_modtreat_roleplus['std_TNCF_%s'% col_name]=results_roleplus.groupby('RatID')['TNCF_%s'% col_name].std()
    std_TN_modtreat_roleplus['std_TNFF_%s'% col_name]=results_roleplus.groupby('RatID')['TNFF_%s'% col_name].std()
    std_TN_modtreat_roleplus['std_TNCM_%s'% col_name]=results_roleplus.groupby('RatID')['TNCM_%s'% col_name].std()
    std_TN_modtreat_roleplus['std_TNFM_%s'% col_name]=results_roleplus.groupby('RatID')['TNFM_%s'% col_name].std()
    std_ON_modtreat_roleplus['std_ONCF_%s'% col_name]=results_roleplus.groupby('RatID')['ONCF_%s'% col_name].std()
    std_ON_modtreat_roleplus['std_ONFF_%s'% col_name]=results_roleplus.groupby('RatID')['ONFF_%s'% col_name].std()
    std_ON_modtreat_roleplus['std_ONCM_%s'% col_name]=results_roleplus.groupby('RatID')['ONCM_%s'% col_name].std()
    std_ON_modtreat_roleplus['std_ONFM_%s'% col_name]=results_roleplus.groupby('RatID')['ONFM_%s'% col_name].std()
    std_BN_modtreat_roleplus['std_BNCF_%s'% col_name]=results_roleplus.groupby('RatID')['BNCF_%s'% col_name].std()
    std_BN_modtreat_roleplus['std_BNFF_%s'% col_name]=results_roleplus.groupby('RatID')['BNFF_%s'% col_name].std()
    std_BN_modtreat_roleplus['std_BNCM_%s'% col_name]=results_roleplus.groupby('RatID')['BNCM_%s'% col_name].std()
    std_BN_modtreat_roleplus['std_BNFM_%s'% col_name]=results_roleplus.groupby('RatID')['BNFM_%s'% col_name].std()

    std_TD_modtreat_roleplus['std_TDCF_%s'% col_name]=results_roleplus.groupby('RatID')['TDCF_%s'% col_name].std()
    std_TD_modtreat_roleplus['std_TDFF_%s'% col_name]=results_roleplus.groupby('RatID')['TDFF_%s'% col_name].std()
    std_TD_modtreat_roleplus['std_TDCM_%s'% col_name]=results_roleplus.groupby('RatID')['TDCM_%s'% col_name].std()
    std_TD_modtreat_roleplus['std_TDFM_%s'% col_name]=results_roleplus.groupby('RatID')['TDFM_%s'% col_name].std()
    std_OD_modtreat_roleplus['std_ODCF_%s'% col_name]=results_roleplus.groupby('RatID')['ODCF_%s'% col_name].std()
    std_OD_modtreat_roleplus['std_ODFF_%s'% col_name]=results_roleplus.groupby('RatID')['ODFF_%s'% col_name].std()
    std_OD_modtreat_roleplus['std_ODCM_%s'% col_name]=results_roleplus.groupby('RatID')['ODCM_%s'% col_name].std()
    std_OD_modtreat_roleplus['std_ODFM_%s'% col_name]=results_roleplus.groupby('RatID')['ODFM_%s'% col_name].std()
    std_BD_modtreat_roleplus['std_BDCF_%s'% col_name]=results_roleplus.groupby('RatID')['BDCF_%s'% col_name].std()
    std_BD_modtreat_roleplus['std_BDFF_%s'% col_name]=results_roleplus.groupby('RatID')['BDFF_%s'% col_name].std()
    std_BD_modtreat_roleplus['std_BDCM_%s'% col_name]=results_roleplus.groupby('RatID')['BDCM_%s'% col_name].std()
    std_BD_modtreat_roleplus['std_BDFM_%s'% col_name]=results_roleplus.groupby('RatID')['BDFM_%s'% col_name].std()    

std_TN_mod_roleplus_columns=list(std_TN_mod_roleplus.columns.values)
std_TD_mod_roleplus_columns=list(std_TD_mod_roleplus.columns.values)
std_TN_modtreat_roleplus_columns=list(std_TN_modtreat_roleplus.columns.values)
std_TD_modtreat_roleplus_columns=list(std_TD_modtreat_roleplus.columns.values)    
std_ON_mod_roleplus_columns=list(std_ON_mod_roleplus.columns.values)
std_OD_mod_roleplus_columns=list(std_OD_mod_roleplus.columns.values)
std_ON_modtreat_roleplus_columns=list(std_ON_modtreat_roleplus.columns.values)
std_OD_modtreat_roleplus_columns=list(std_OD_modtreat_roleplus.columns.values)  
std_BN_mod_roleplus_columns=list(std_BN_mod_roleplus.columns.values)
std_BD_mod_roleplus_columns=list(std_BD_mod_roleplus.columns.values)
std_BN_modtreat_roleplus_columns=list(std_BN_modtreat_roleplus.columns.values)
std_BD_modtreat_roleplus_columns=list(std_BD_modtreat_roleplus.columns.values)  

  
# Write mean statistics to the new dataframe data_stat
data_stat_mean_Total_fight= pd.concat([data_stat_fight, mean_Total_fight, sem_Total_fight], sort=False, axis=1)
data_stat_mean_TN_mod_fight=pd.concat([data_stat_fight, mean_TN_mod_fight, sem_TN_mod_fight], sort=False, axis=1)
data_stat_mean_TD_mod_fight=pd.concat([data_stat_fight, mean_TD_mod_fight, sem_TD_mod_fight], sort=False, axis=1)
data_stat_mean_TN_modtreat_fight=pd.concat([data_stat_fight, mean_TN_modtreat_fight, sem_TN_modtreat_fight], sort=False, axis=1)
data_stat_mean_TD_modtreat_fight=pd.concat([data_stat_fight, mean_TD_modtreat_fight, sem_TD_modtreat_fight], sort=False, axis=1)

data_stat_mean_OF_fight= pd.concat([data_stat_fight, mean_OF_fight, sem_OF_fight], sort=False, axis=1)
data_stat_mean_ON_mod_fight=pd.concat([data_stat_fight, mean_ON_mod_fight, sem_ON_mod_fight], sort=False, axis=1)
data_stat_mean_OD_mod_fight=pd.concat([data_stat_fight, mean_OD_mod_fight, sem_OD_mod_fight], sort=False, axis=1)
data_stat_mean_ON_modtreat_fight=pd.concat([data_stat_fight, mean_ON_modtreat_fight, sem_ON_modtreat_fight], sort=False, axis=1)
data_stat_mean_OD_modtreat_fight=pd.concat([data_stat_fight, mean_OD_modtreat_fight, sem_OD_modtreat_fight], sort=False, axis=1)

data_stat_mean_Burrow_fight= pd.concat([data_stat_fight, mean_Burrow_fight, sem_Burrow_fight], sort=False, axis=1)
data_stat_mean_BN_mod_fight=pd.concat([data_stat_fight, mean_BN_mod_fight, sem_BN_mod_fight], sort=False, axis=1)
data_stat_mean_BD_mod_fight=pd.concat([data_stat_fight, mean_BD_mod_fight, sem_BD_mod_fight], sort=False, axis=1)
data_stat_mean_BN_modtreat_fight=pd.concat([data_stat_fight, mean_BN_modtreat_fight, sem_BN_modtreat_fight], sort=False, axis=1)
data_stat_mean_BD_modtreat_fight=pd.concat([data_stat_fight, mean_BD_modtreat_fight, sem_BD_modtreat_fight], sort=False, axis=1)


data_stat_rest_Total_fight= pd.concat([data_stat_rest_fight, median_Total_fight, std_Total_fight], sort=False, axis=1)
data_stat_rest_TN_mod_fight=pd.concat([data_stat_rest_fight, median_TN_mod_fight, std_TN_mod_fight], sort=False, axis=1)
data_stat_rest_TD_mod_fight=pd.concat([data_stat_rest_fight, median_TD_mod_fight, std_TD_mod_fight], sort=False, axis=1)
data_stat_rest_TN_modtreat_fight=pd.concat([data_stat_rest_fight, median_TN_modtreat_fight, std_TN_modtreat_fight], sort=False, axis=1)
data_stat_rest_TD_modtreat_fight=pd.concat([data_stat_rest_fight, median_TD_modtreat_fight, std_TD_modtreat_fight], sort=False, axis=1)

data_stat_rest_OF_fight= pd.concat([data_stat_rest_fight, median_OF_fight, std_OF_fight], sort=False, axis=1)
data_stat_rest_ON_mod_fight=pd.concat([data_stat_rest_fight, median_ON_mod_fight, std_ON_mod_fight], sort=False, axis=1)
data_stat_rest_OD_mod_fight=pd.concat([data_stat_rest_fight, median_OD_mod_fight, std_OD_mod_fight], sort=False, axis=1)
data_stat_rest_ON_modtreat_fight=pd.concat([data_stat_rest_fight, median_ON_modtreat_fight, std_ON_modtreat_fight], sort=False, axis=1)
data_stat_rest_OD_modtreat_fight=pd.concat([data_stat_rest_fight, median_OD_modtreat_fight, std_OD_modtreat_fight], sort=False, axis=1)

data_stat_rest_Burrow_fight= pd.concat([data_stat_rest_fight, median_Burrow_fight, std_Burrow_fight], sort=False, axis=1)
data_stat_rest_BN_mod_fight=pd.concat([data_stat_rest_fight, median_BN_mod_fight, std_BN_mod_fight], sort=False, axis=1)
data_stat_rest_BD_mod_fight=pd.concat([data_stat_rest_fight, median_BD_mod_fight, std_BD_mod_fight], sort=False, axis=1)
data_stat_rest_BN_modtreat_fight=pd.concat([data_stat_rest_fight, median_BN_modtreat_fight, std_BN_modtreat_fight], sort=False, axis=1)
data_stat_rest_BD_modtreat_fight=pd.concat([data_stat_rest_fight, median_BD_modtreat_fight, std_BD_modtreat_fight], sort=False, axis=1)

bigList_mean_Total_fight = []
for a,b in zip(mean_Total_fight_columns, sem_Total_fight_columns):
	bigList_mean_Total_fight.append(a)
	bigList_mean_Total_fight.append(b)

data_stat_mean_Total_fight=data_stat_mean_Total_fight[bigList_mean_Total_fight]

bigList_mean_TN_mod_fight = []
for a,b in zip(mean_TN_mod_fight_columns, sem_TN_mod_fight_columns):
	bigList_mean_TN_mod_fight.append(a)
	bigList_mean_TN_mod_fight.append(b)
data_stat_mean_TN_mod_fight=data_stat_mean_TN_mod_fight[bigList_mean_TN_mod_fight]

bigList_mean_TD_mod_fight = []
for a,b in zip(mean_TD_mod_fight_columns, sem_TD_mod_fight_columns):
	bigList_mean_TD_mod_fight.append(a)
	bigList_mean_TD_mod_fight.append(b)
data_stat_mean_TD_mod_fight=data_stat_mean_TD_mod_fight[bigList_mean_TD_mod_fight]

bigList_mean_TN_modtreat_fight = []
for a,b in zip(mean_TN_modtreat_fight_columns, sem_TN_modtreat_fight_columns):
	bigList_mean_TN_modtreat_fight.append(a)
	bigList_mean_TN_modtreat_fight.append(b)
data_stat_mean_TN_modtreat_fight=data_stat_mean_TN_modtreat_fight[bigList_mean_TN_modtreat_fight]

bigList_mean_TD_modtreat_fight = []
for a,b in zip(mean_TD_modtreat_fight_columns, sem_TD_modtreat_fight_columns):
	bigList_mean_TD_modtreat_fight.append(a)
	bigList_mean_TD_modtreat_fight.append(b)
data_stat_mean_TD_modtreat_fight=data_stat_mean_TD_modtreat_fight[bigList_mean_TD_modtreat_fight]

bigList_mean_OF_fight = []
for a,b in zip(mean_OF_fight_columns, sem_OF_fight_columns):
	bigList_mean_OF_fight.append(a)
	bigList_mean_OF_fight.append(b)

data_stat_mean_OF_fight=data_stat_mean_OF_fight[bigList_mean_OF_fight]

bigList_mean_ON_mod_fight = []
for a,b in zip(mean_ON_mod_fight_columns, sem_ON_mod_fight_columns):
	bigList_mean_ON_mod_fight.append(a)
	bigList_mean_ON_mod_fight.append(b)
data_stat_mean_ON_mod_fight=data_stat_mean_ON_mod_fight[bigList_mean_ON_mod_fight]

bigList_mean_OD_mod_fight = []
for a,b in zip(mean_OD_mod_fight_columns, sem_OD_mod_fight_columns):
	bigList_mean_OD_mod_fight.append(a)
	bigList_mean_OD_mod_fight.append(b)
data_stat_mean_OD_mod_fight=data_stat_mean_OD_mod_fight[bigList_mean_OD_mod_fight]

bigList_mean_ON_modtreat_fight = []
for a,b in zip(mean_ON_modtreat_fight_columns, sem_ON_modtreat_fight_columns):
	bigList_mean_ON_modtreat_fight.append(a)
	bigList_mean_ON_modtreat_fight.append(b)
data_stat_mean_ON_modtreat_fight=data_stat_mean_ON_modtreat_fight[bigList_mean_ON_modtreat_fight]

bigList_mean_OD_modtreat_fight = []
for a,b in zip(mean_OD_modtreat_fight_columns, sem_OD_modtreat_fight_columns):
	bigList_mean_OD_modtreat_fight.append(a)
	bigList_mean_OD_modtreat_fight.append(b)
data_stat_mean_OD_modtreat_fight=data_stat_mean_OD_modtreat_fight[bigList_mean_OD_modtreat_fight]

bigList_mean_Burrow_fight = []
for a,b in zip(mean_Burrow_fight_columns, sem_Burrow_fight_columns):
	bigList_mean_Burrow_fight.append(a)
	bigList_mean_Burrow_fight.append(b)

data_stat_mean_Burrow_fight=data_stat_mean_Burrow_fight[bigList_mean_Burrow_fight]

bigList_mean_BN_mod_fight = []
for a,b in zip(mean_BN_mod_fight_columns, sem_BN_mod_fight_columns):
	bigList_mean_BN_mod_fight.append(a)
	bigList_mean_BN_mod_fight.append(b)
data_stat_mean_BN_mod_fight=data_stat_mean_BN_mod_fight[bigList_mean_BN_mod_fight]

bigList_mean_BD_mod_fight = []
for a,b in zip(mean_BD_mod_fight_columns, sem_BD_mod_fight_columns):
	bigList_mean_BD_mod_fight.append(a)
	bigList_mean_BD_mod_fight.append(b)
data_stat_mean_BD_mod_fight=data_stat_mean_BD_mod_fight[bigList_mean_BD_mod_fight]

bigList_mean_BN_modtreat_fight = []
for a,b in zip(mean_BN_modtreat_fight_columns, sem_BN_modtreat_fight_columns):
	bigList_mean_BN_modtreat_fight.append(a)
	bigList_mean_BN_modtreat_fight.append(b)
data_stat_mean_BN_modtreat_fight=data_stat_mean_BN_modtreat_fight[bigList_mean_BN_modtreat_fight]

bigList_mean_BD_modtreat_fight = []
for a,b in zip(mean_BD_modtreat_fight_columns, sem_BD_modtreat_fight_columns):
	bigList_mean_BD_modtreat_fight.append(a)
	bigList_mean_BD_modtreat_fight.append(b)
data_stat_mean_BD_modtreat_fight=data_stat_mean_BD_modtreat_fight[bigList_mean_BD_modtreat_fight]

# FOR ROLE
# Write mean statistics to the new dataframe data_stat
data_stat_mean_Total_role= pd.concat([data_stat_role, mean_Total_role, sem_Total_role], sort=False, axis=1)
data_stat_mean_TN_mod_role=pd.concat([data_stat_role, mean_TN_mod_role, sem_TN_mod_role], sort=False, axis=1)
data_stat_mean_TD_mod_role=pd.concat([data_stat_role, mean_TD_mod_role, sem_TD_mod_role], sort=False, axis=1)
data_stat_mean_TN_modtreat_role=pd.concat([data_stat_role, mean_TN_modtreat_role, sem_TN_modtreat_role], sort=False, axis=1)
data_stat_mean_TD_modtreat_role=pd.concat([data_stat_role, mean_TD_modtreat_role, sem_TD_modtreat_role], sort=False, axis=1)

data_stat_mean_OF_role= pd.concat([data_stat_role, mean_OF_role, sem_OF_role], sort=False, axis=1)
data_stat_mean_ON_mod_role=pd.concat([data_stat_role, mean_ON_mod_role, sem_ON_mod_role], sort=False, axis=1)
data_stat_mean_OD_mod_role=pd.concat([data_stat_role, mean_OD_mod_role, sem_OD_mod_role], sort=False, axis=1)
data_stat_mean_ON_modtreat_role=pd.concat([data_stat_role, mean_ON_modtreat_role, sem_ON_modtreat_role], sort=False, axis=1)
data_stat_mean_OD_modtreat_role=pd.concat([data_stat_role, mean_OD_modtreat_role, sem_OD_modtreat_role], sort=False, axis=1)

data_stat_mean_Burrow_role= pd.concat([data_stat_role, mean_Burrow_role, sem_Burrow_role], sort=False, axis=1)
data_stat_mean_BN_mod_role=pd.concat([data_stat_role, mean_BN_mod_role, sem_BN_mod_role], sort=False, axis=1)
data_stat_mean_BD_mod_role=pd.concat([data_stat_role, mean_BD_mod_role, sem_BD_mod_role], sort=False, axis=1)
data_stat_mean_BN_modtreat_role=pd.concat([data_stat_role, mean_BN_modtreat_role, sem_BN_modtreat_role], sort=False, axis=1)
data_stat_mean_BD_modtreat_role=pd.concat([data_stat_role, mean_BD_modtreat_role, sem_BD_modtreat_role], sort=False, axis=1)

data_stat_rest_Total_role= pd.concat([data_stat_rest_role, median_Total_role, std_Total_role], sort=False, axis=1)
data_stat_rest_TN_mod_role=pd.concat([data_stat_rest_role, median_TN_mod_role, std_TN_mod_role], sort=False, axis=1)
data_stat_rest_TD_mod_role=pd.concat([data_stat_rest_role, median_TD_mod_role, std_TD_mod_role], sort=False, axis=1)
data_stat_rest_TN_modtreat_role=pd.concat([data_stat_rest_role, median_TN_modtreat_role, std_TN_modtreat_role], sort=False, axis=1)
data_stat_rest_TD_modtreat_role=pd.concat([data_stat_rest_role, median_TD_modtreat_role, std_TD_modtreat_role], sort=False, axis=1)

data_stat_rest_OF_role= pd.concat([data_stat_rest_role, median_OF_role, std_OF_role], sort=False, axis=1)
data_stat_rest_ON_mod_role=pd.concat([data_stat_rest_role, median_ON_mod_role, std_ON_mod_role], sort=False, axis=1)
data_stat_rest_OD_mod_role=pd.concat([data_stat_rest_role, median_OD_mod_role, std_OD_mod_role], sort=False, axis=1)
data_stat_rest_ON_modtreat_role=pd.concat([data_stat_rest_role, median_ON_modtreat_role, std_ON_modtreat_role], sort=False, axis=1)
data_stat_rest_OD_modtreat_role=pd.concat([data_stat_rest_role, median_OD_modtreat_role, std_OD_modtreat_role], sort=False, axis=1)

data_stat_rest_Burrow_role= pd.concat([data_stat_rest_role, median_Burrow_role, std_Burrow_role], sort=False, axis=1)
data_stat_rest_BN_mod_role=pd.concat([data_stat_rest_role, median_BN_mod_role, std_BN_mod_role], sort=False, axis=1)
data_stat_rest_BD_mod_role=pd.concat([data_stat_rest_role, median_BD_mod_role, std_BD_mod_role], sort=False, axis=1)
data_stat_rest_BN_modtreat_role=pd.concat([data_stat_rest_role, median_BN_modtreat_role, std_BN_modtreat_role], sort=False, axis=1)
data_stat_rest_BD_modtreat_role=pd.concat([data_stat_rest_role, median_BD_modtreat_role, std_BD_modtreat_role], sort=False, axis=1)

bigList_mean_Total_role = []
for a,b in zip(mean_Total_role_columns, sem_Total_role_columns):
	bigList_mean_Total_role.append(a)
	bigList_mean_Total_role.append(b)

data_stat_mean_Total_role=data_stat_mean_Total_role[bigList_mean_Total_role]

bigList_mean_TN_mod_role = []
for a,b in zip(mean_TN_mod_role_columns, sem_TN_mod_role_columns):
	bigList_mean_TN_mod_role.append(a)
	bigList_mean_TN_mod_role.append(b)
data_stat_mean_TN_mod_role=data_stat_mean_TN_mod_role[bigList_mean_TN_mod_role]

bigList_mean_TD_mod_role = []
for a,b in zip(mean_TD_mod_role_columns, sem_TD_mod_role_columns):
	bigList_mean_TD_mod_role.append(a)
	bigList_mean_TD_mod_role.append(b)
data_stat_mean_TD_mod_role=data_stat_mean_TD_mod_role[bigList_mean_TD_mod_role]

bigList_mean_TN_modtreat_role = []
for a,b in zip(mean_TN_modtreat_role_columns, sem_TN_modtreat_role_columns):
	bigList_mean_TN_modtreat_role.append(a)
	bigList_mean_TN_modtreat_role.append(b)
data_stat_mean_TN_modtreat_role=data_stat_mean_TN_modtreat_role[bigList_mean_TN_modtreat_role]

bigList_mean_TD_modtreat_role = []
for a,b in zip(mean_TD_modtreat_role_columns, sem_TD_modtreat_role_columns):
	bigList_mean_TD_modtreat_role.append(a)
	bigList_mean_TD_modtreat_role.append(b)
data_stat_mean_TD_modtreat_role=data_stat_mean_TD_modtreat_role[bigList_mean_TD_modtreat_role]

bigList_mean_OF_role = []
for a,b in zip(mean_OF_role_columns, sem_OF_role_columns):
	bigList_mean_OF_role.append(a)
	bigList_mean_OF_role.append(b)

data_stat_mean_OF_role=data_stat_mean_OF_role[bigList_mean_OF_role]

bigList_mean_ON_mod_role = []
for a,b in zip(mean_ON_mod_role_columns, sem_ON_mod_role_columns):
	bigList_mean_ON_mod_role.append(a)
	bigList_mean_ON_mod_role.append(b)
data_stat_mean_ON_mod_role=data_stat_mean_ON_mod_role[bigList_mean_ON_mod_role]

bigList_mean_OD_mod_role = []
for a,b in zip(mean_OD_mod_role_columns, sem_OD_mod_role_columns):
	bigList_mean_OD_mod_role.append(a)
	bigList_mean_OD_mod_role.append(b)
data_stat_mean_OD_mod_role=data_stat_mean_OD_mod_role[bigList_mean_OD_mod_role]

bigList_mean_ON_modtreat_role = []
for a,b in zip(mean_ON_modtreat_role_columns, sem_ON_modtreat_role_columns):
	bigList_mean_ON_modtreat_role.append(a)
	bigList_mean_ON_modtreat_role.append(b)
data_stat_mean_ON_modtreat_role=data_stat_mean_ON_modtreat_role[bigList_mean_ON_modtreat_role]

bigList_mean_OD_modtreat_role = []
for a,b in zip(mean_OD_modtreat_role_columns, sem_OD_modtreat_role_columns):
	bigList_mean_OD_modtreat_role.append(a)
	bigList_mean_OD_modtreat_role.append(b)
data_stat_mean_OD_modtreat_role=data_stat_mean_OD_modtreat_role[bigList_mean_OD_modtreat_role]

bigList_mean_Burrow_role = []
for a,b in zip(mean_Burrow_role_columns, sem_Burrow_role_columns):
	bigList_mean_Burrow_role.append(a)
	bigList_mean_Burrow_role.append(b)

data_stat_mean_Burrow_role=data_stat_mean_Burrow_role[bigList_mean_Burrow_role]

bigList_mean_BN_mod_role = []
for a,b in zip(mean_BN_mod_role_columns, sem_BN_mod_role_columns):
	bigList_mean_BN_mod_role.append(a)
	bigList_mean_BN_mod_role.append(b)
data_stat_mean_BN_mod_role=data_stat_mean_BN_mod_role[bigList_mean_BN_mod_role]

bigList_mean_BD_mod_role = []
for a,b in zip(mean_BD_mod_role_columns, sem_BD_mod_role_columns):
	bigList_mean_BD_mod_role.append(a)
	bigList_mean_BD_mod_role.append(b)
data_stat_mean_BD_mod_role=data_stat_mean_BD_mod_role[bigList_mean_BD_mod_role]

bigList_mean_BN_modtreat_role = []
for a,b in zip(mean_BN_modtreat_role_columns, sem_BN_modtreat_role_columns):
	bigList_mean_BN_modtreat_role.append(a)
	bigList_mean_BN_modtreat_role.append(b)
data_stat_mean_BN_modtreat_role=data_stat_mean_BN_modtreat_role[bigList_mean_BN_modtreat_role]

bigList_mean_BD_modtreat_role = []
for a,b in zip(mean_BD_modtreat_role_columns, sem_BD_modtreat_role_columns):
	bigList_mean_BD_modtreat_role.append(a)
	bigList_mean_BD_modtreat_role.append(b)
data_stat_mean_BD_modtreat_role=data_stat_mean_BD_modtreat_role[bigList_mean_BD_modtreat_role] 

# FOR ROLEPLUS
# Write mean statistics to the new dataframe data_stat
data_stat_mean_Total_roleplus= pd.concat([data_stat_roleplus, mean_Total_roleplus, sem_Total_roleplus], sort=False, axis=1)
data_stat_mean_TN_mod_roleplus=pd.concat([data_stat_roleplus, mean_TN_mod_roleplus, sem_TN_mod_roleplus], sort=False, axis=1)
data_stat_mean_TD_mod_roleplus=pd.concat([data_stat_roleplus, mean_TD_mod_roleplus, sem_TD_mod_roleplus], sort=False, axis=1)
data_stat_mean_TN_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_TN_modtreat_roleplus, sem_TN_modtreat_roleplus], sort=False, axis=1)
data_stat_mean_TD_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_TD_modtreat_roleplus, sem_TD_modtreat_roleplus], sort=False, axis=1)

data_stat_mean_OF_roleplus= pd.concat([data_stat_roleplus, mean_OF_roleplus, sem_OF_roleplus], sort=False, axis=1)
data_stat_mean_ON_mod_roleplus=pd.concat([data_stat_roleplus, mean_ON_mod_roleplus, sem_ON_mod_roleplus], sort=False, axis=1)
data_stat_mean_OD_mod_roleplus=pd.concat([data_stat_roleplus, mean_OD_mod_roleplus, sem_OD_mod_roleplus], sort=False, axis=1)
data_stat_mean_ON_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_ON_modtreat_roleplus, sem_ON_modtreat_roleplus], sort=False, axis=1)
data_stat_mean_OD_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_OD_modtreat_roleplus, sem_OD_modtreat_roleplus], sort=False, axis=1)

data_stat_mean_Burrow_roleplus= pd.concat([data_stat_roleplus, mean_Burrow_roleplus, sem_Burrow_roleplus], sort=False, axis=1)
data_stat_mean_BN_mod_roleplus=pd.concat([data_stat_roleplus, mean_BN_mod_roleplus, sem_BN_mod_roleplus], sort=False, axis=1)
data_stat_mean_BD_mod_roleplus=pd.concat([data_stat_roleplus, mean_BD_mod_roleplus, sem_BD_mod_roleplus], sort=False, axis=1)
data_stat_mean_BN_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_BN_modtreat_roleplus, sem_BN_modtreat_roleplus], sort=False, axis=1)
data_stat_mean_BD_modtreat_roleplus=pd.concat([data_stat_roleplus, mean_BD_modtreat_roleplus, sem_BD_modtreat_roleplus], sort=False, axis=1)

data_stat_rest_Total_roleplus= pd.concat([data_stat_rest_roleplus, median_Total_roleplus, std_Total_roleplus], sort=False, axis=1)
data_stat_rest_TN_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_TN_mod_roleplus, std_TN_mod_roleplus], sort=False, axis=1)
data_stat_rest_TD_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_TD_mod_roleplus, std_TD_mod_roleplus], sort=False, axis=1)
data_stat_rest_TN_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_TN_modtreat_roleplus, std_TN_modtreat_roleplus], sort=False, axis=1)
data_stat_rest_TD_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_TD_modtreat_roleplus, std_TD_modtreat_roleplus], sort=False, axis=1)

data_stat_rest_OF_roleplus= pd.concat([data_stat_rest_roleplus, median_OF_roleplus, std_OF_roleplus], sort=False, axis=1)
data_stat_rest_ON_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_ON_mod_roleplus, std_ON_mod_roleplus], sort=False, axis=1)
data_stat_rest_OD_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_OD_mod_roleplus, std_OD_mod_roleplus], sort=False, axis=1)
data_stat_rest_ON_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_ON_modtreat_roleplus, std_ON_modtreat_roleplus], sort=False, axis=1)
data_stat_rest_OD_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_OD_modtreat_roleplus, std_OD_modtreat_roleplus], sort=False, axis=1)

data_stat_rest_Burrow_roleplus= pd.concat([data_stat_rest_roleplus, median_Burrow_roleplus, std_Burrow_roleplus], sort=False, axis=1)
data_stat_rest_BN_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_BN_mod_roleplus, std_BN_mod_roleplus], sort=False, axis=1)
data_stat_rest_BD_mod_roleplus=pd.concat([data_stat_rest_roleplus, median_BD_mod_roleplus, std_BD_mod_roleplus], sort=False, axis=1)
data_stat_rest_BN_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_BN_modtreat_roleplus, std_BN_modtreat_roleplus], sort=False, axis=1)
data_stat_rest_BD_modtreat_roleplus=pd.concat([data_stat_rest_roleplus, median_BD_modtreat_roleplus, std_BD_modtreat_roleplus], sort=False, axis=1)

bigList_mean_Total_roleplus = []
for a,b in zip(mean_Total_roleplus_columns, sem_Total_roleplus_columns):
	bigList_mean_Total_roleplus.append(a)
	bigList_mean_Total_roleplus.append(b)

data_stat_mean_Total_roleplus=data_stat_mean_Total_roleplus[bigList_mean_Total_roleplus]

bigList_mean_TN_mod_roleplus = []
for a,b in zip(mean_TN_mod_roleplus_columns, sem_TN_mod_roleplus_columns):
	bigList_mean_TN_mod_roleplus.append(a)
	bigList_mean_TN_mod_roleplus.append(b)
data_stat_mean_TN_mod_roleplus=data_stat_mean_TN_mod_roleplus[bigList_mean_TN_mod_roleplus]

bigList_mean_TD_mod_roleplus = []
for a,b in zip(mean_TD_mod_roleplus_columns, sem_TD_mod_roleplus_columns):
	bigList_mean_TD_mod_roleplus.append(a)
	bigList_mean_TD_mod_roleplus.append(b)
data_stat_mean_TD_mod_roleplus=data_stat_mean_TD_mod_roleplus[bigList_mean_TD_mod_roleplus]

bigList_mean_TN_modtreat_roleplus = []
for a,b in zip(mean_TN_modtreat_roleplus_columns, sem_TN_modtreat_roleplus_columns):
	bigList_mean_TN_modtreat_roleplus.append(a)
	bigList_mean_TN_modtreat_roleplus.append(b)
data_stat_mean_TN_modtreat_roleplus=data_stat_mean_TN_modtreat_roleplus[bigList_mean_TN_modtreat_roleplus]

bigList_mean_TD_modtreat_roleplus = []
for a,b in zip(mean_TD_modtreat_roleplus_columns, sem_TD_modtreat_roleplus_columns):
	bigList_mean_TD_modtreat_roleplus.append(a)
	bigList_mean_TD_modtreat_roleplus.append(b)
data_stat_mean_TD_modtreat_roleplus=data_stat_mean_TD_modtreat_roleplus[bigList_mean_TD_modtreat_roleplus]

bigList_mean_OF_roleplus = []
for a,b in zip(mean_OF_roleplus_columns, sem_OF_roleplus_columns):
	bigList_mean_OF_roleplus.append(a)
	bigList_mean_OF_roleplus.append(b)

data_stat_mean_OF_roleplus=data_stat_mean_OF_roleplus[bigList_mean_OF_roleplus]

bigList_mean_ON_mod_roleplus = []
for a,b in zip(mean_ON_mod_roleplus_columns, sem_ON_mod_roleplus_columns):
	bigList_mean_ON_mod_roleplus.append(a)
	bigList_mean_ON_mod_roleplus.append(b)
data_stat_mean_ON_mod_roleplus=data_stat_mean_ON_mod_roleplus[bigList_mean_ON_mod_roleplus]

bigList_mean_OD_mod_roleplus = []
for a,b in zip(mean_OD_mod_roleplus_columns, sem_OD_mod_roleplus_columns):
	bigList_mean_OD_mod_roleplus.append(a)
	bigList_mean_OD_mod_roleplus.append(b)
data_stat_mean_OD_mod_roleplus=data_stat_mean_OD_mod_roleplus[bigList_mean_OD_mod_roleplus]

bigList_mean_ON_modtreat_roleplus = []
for a,b in zip(mean_ON_modtreat_roleplus_columns, sem_ON_modtreat_roleplus_columns):
	bigList_mean_ON_modtreat_roleplus.append(a)
	bigList_mean_ON_modtreat_roleplus.append(b)
data_stat_mean_ON_modtreat_roleplus=data_stat_mean_ON_modtreat_roleplus[bigList_mean_ON_modtreat_roleplus]

bigList_mean_OD_modtreat_roleplus = []
for a,b in zip(mean_OD_modtreat_roleplus_columns, sem_OD_modtreat_roleplus_columns):
	bigList_mean_OD_modtreat_roleplus.append(a)
	bigList_mean_OD_modtreat_roleplus.append(b)
data_stat_mean_OD_modtreat_roleplus=data_stat_mean_OD_modtreat_roleplus[bigList_mean_OD_modtreat_roleplus]

bigList_mean_Burrow_roleplus = []
for a,b in zip(mean_Burrow_roleplus_columns, sem_Burrow_roleplus_columns):
	bigList_mean_Burrow_roleplus.append(a)
	bigList_mean_Burrow_roleplus.append(b)

data_stat_mean_Burrow_roleplus=data_stat_mean_Burrow_roleplus[bigList_mean_Burrow_roleplus]

bigList_mean_BN_mod_roleplus = []
for a,b in zip(mean_BN_mod_roleplus_columns, sem_BN_mod_roleplus_columns):
	bigList_mean_BN_mod_roleplus.append(a)
	bigList_mean_BN_mod_roleplus.append(b)
data_stat_mean_BN_mod_roleplus=data_stat_mean_BN_mod_roleplus[bigList_mean_BN_mod_roleplus]

bigList_mean_BD_mod_roleplus = []
for a,b in zip(mean_BD_mod_roleplus_columns, sem_BD_mod_roleplus_columns):
	bigList_mean_BD_mod_roleplus.append(a)
	bigList_mean_BD_mod_roleplus.append(b)
data_stat_mean_BD_mod_roleplus=data_stat_mean_BD_mod_roleplus[bigList_mean_BD_mod_roleplus]

bigList_mean_BN_modtreat_roleplus = []
for a,b in zip(mean_BN_modtreat_roleplus_columns, sem_BN_modtreat_roleplus_columns):
	bigList_mean_BN_modtreat_roleplus.append(a)
	bigList_mean_BN_modtreat_roleplus.append(b)
data_stat_mean_BN_modtreat_roleplus=data_stat_mean_BN_modtreat_roleplus[bigList_mean_BN_modtreat_roleplus]

bigList_mean_BD_modtreat_roleplus = []
for a,b in zip(mean_BD_modtreat_roleplus_columns, sem_BD_modtreat_roleplus_columns):
	bigList_mean_BD_modtreat_roleplus.append(a)
	bigList_mean_BD_modtreat_roleplus.append(b)
data_stat_mean_BD_modtreat_roleplus=data_stat_mean_BD_modtreat_roleplus[bigList_mean_BD_modtreat_roleplus] 


## Say where to save the file and with what name (note the use of / instead of \)
#out_path1 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_results.xlsx"
#out_path2 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_results_role.xlsx"
#out_path3 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_results_roleplus.xlsx"
#out_path4 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_resultsmod.xlsx"
#out_path5 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_resultsmod_role.xlsx"
#out_path6 = "C:/Users/esn001/Desktop/python/HN Roy/Output/HN002_resultsmod_roleplus.xlsx"


# now save the data frame to excel
writer1 = pd.ExcelWriter(out_path1, engine='xlsxwriter')
writer2 = pd.ExcelWriter(out_path2, engine='xlsxwriter')
writer3 = pd.ExcelWriter(out_path3, engine='xlsxwriter')
writer4 = pd.ExcelWriter(out_path4, engine='xlsxwriter')
writer5 = pd.ExcelWriter(out_path5, engine='xlsxwriter')
writer6 = pd.ExcelWriter(out_path6, engine='xlsxwriter')

data_info.to_excel(writer1,'data_info')
data_info.to_excel(writer2,'data_info')
data_info.to_excel(writer3,'data_info')
data_info.to_excel(writer4,'data_info')
data_info.to_excel(writer5,'data_info')
data_info.to_excel(writer6,'data_info')

results_Total_fight.to_excel(writer1, sheet_name='Total environment')
results_OF_fight.to_excel(writer1, sheet_name='OF')
results_Burrow_fight.to_excel(writer1, sheet_name='Burrow')
data_stat_mean_Total_fight.to_excel(writer1, sheet_name='stat_Total')
data_stat_mean_OF_fight.to_excel(writer1, sheet_name='stat_OF')
data_stat_mean_Burrow_fight.to_excel(writer1, sheet_name='stat_Burrow')
data_stat_rest_Total_fight.to_excel(writer1, sheet_name='statrest_Total')
data_stat_rest_OF_fight.to_excel(writer1, sheet_name='statrest_OF')
data_stat_rest_Burrow_fight.to_excel(writer1, sheet_name='statrest_Burrow')

results_Total_role.to_excel(writer2, sheet_name='Total environment')
results_OF_role.to_excel(writer2, sheet_name='OF')
results_Burrow_role.to_excel(writer2, sheet_name='Burrow')
data_stat_mean_Total_role.to_excel(writer2, sheet_name='stat_Total')
data_stat_mean_OF_role.to_excel(writer2, sheet_name='stat_OF')
data_stat_mean_Burrow_role.to_excel(writer2, sheet_name='stat_Burrow')
data_stat_rest_Total_role.to_excel(writer2, sheet_name='statrest_Total')
data_stat_rest_OF_role.to_excel(writer2, sheet_name='statrest_OF')
data_stat_rest_Burrow_role.to_excel(writer2, sheet_name='statrest_Burrow')

results_Total_roleplus.to_excel(writer3, sheet_name='Total environment')
results_OF_roleplus.to_excel(writer3, sheet_name='OF')
results_Burrow_roleplus.to_excel(writer3, sheet_name='Burrow')
data_stat_mean_Total_roleplus.to_excel(writer3, sheet_name='stat_Total')
data_stat_mean_OF_roleplus.to_excel(writer3, sheet_name='stat_OF')
data_stat_mean_Burrow_roleplus.to_excel(writer3, sheet_name='stat_Burrow')
data_stat_rest_Total_roleplus.to_excel(writer3, sheet_name='statrest_Total')
data_stat_rest_OF_roleplus.to_excel(writer3, sheet_name='statrest_OF')
data_stat_rest_Burrow_roleplus.to_excel(writer3, sheet_name='statrest_Burrow')

results_TD_mod_fight.to_excel(writer4, sheet_name='duration_mod')
results_TN_mod_fight.to_excel(writer4, sheet_name='number_mod')
results_TD_modtreat_fight.to_excel(writer4, sheet_name='duration_modtreat')
results_TN_modtreat_fight.to_excel(writer4, sheet_name='number_modtreat')
results_OD_mod_fight.to_excel(writer4, sheet_name='OF duration_mod')
results_ON_mod_fight.to_excel(writer4, sheet_name='OF number_mod')
results_OD_modtreat_fight.to_excel(writer4, sheet_name='OF duration_modtreat')
results_ON_modtreat_fight.to_excel(writer4, sheet_name='OF number_modtreat')
results_BD_mod_fight.to_excel(writer4, sheet_name='Burrow duration_mod')
results_BN_mod_fight.to_excel(writer4, sheet_name='Burrow number_mod')
results_BD_modtreat_fight.to_excel(writer4, sheet_name='Burrow duration_modtreat')
results_BN_modtreat_fight.to_excel(writer4, sheet_name='Burrow number_modtreat')
data_stat_mean_TD_mod_fight.to_excel(writer4, sheet_name='stat_TD_mod')
data_stat_mean_TN_mod_fight.to_excel(writer4, sheet_name='stat_TN_mod')
data_stat_mean_TD_modtreat_fight.to_excel(writer4, sheet_name='stat_TD_modtreat')
data_stat_mean_TN_modtreat_fight.to_excel(writer4, sheet_name='stat_TN_modtreat')
data_stat_mean_OD_mod_fight.to_excel(writer4, sheet_name='stat_OD_mod')
data_stat_mean_ON_mod_fight.to_excel(writer4, sheet_name='stat_ON_mod')
data_stat_mean_OD_modtreat_fight.to_excel(writer4, sheet_name='stat_OD_modtreat')
data_stat_mean_ON_modtreat_fight.to_excel(writer4, sheet_name='stat_ON_modtreat')
data_stat_mean_BD_mod_fight.to_excel(writer4, sheet_name='stat_BD_mod')
data_stat_mean_BN_mod_fight.to_excel(writer4, sheet_name='stat_BN_mod')
data_stat_mean_BD_modtreat_fight.to_excel(writer4, sheet_name='stat_BD_modtreat')
data_stat_mean_BN_modtreat_fight.to_excel(writer4, sheet_name='stat_BN_modtreat')
data_stat_rest_TD_mod_fight.to_excel(writer4, sheet_name='statrest_TD_mod')
data_stat_rest_TN_mod_fight.to_excel(writer4, sheet_name='statrest_TN_mod')
data_stat_rest_TD_modtreat_fight.to_excel(writer4, sheet_name='statrest_TD_modtreat')
data_stat_rest_TN_modtreat_fight.to_excel(writer4, sheet_name='statrest_TN_modtreat')
data_stat_rest_OD_mod_fight.to_excel(writer4, sheet_name='statrest_OD_mod')
data_stat_rest_ON_mod_fight.to_excel(writer4, sheet_name='statrest_ON_mod')
data_stat_rest_OD_modtreat_fight.to_excel(writer4, sheet_name='statrest_OD_modtreat')
data_stat_rest_ON_modtreat_fight.to_excel(writer4, sheet_name='statrest_ON_modtreat')
data_stat_rest_BD_mod_fight.to_excel(writer4, sheet_name='statrest_BD_mod')
data_stat_rest_BN_mod_fight.to_excel(writer4, sheet_name='statrest_BN_mod')
data_stat_rest_BD_modtreat_fight.to_excel(writer4, sheet_name='statrest_BD_modtreat')
data_stat_rest_BN_modtreat_fight.to_excel(writer4, sheet_name='statrest_BN_modtreat')

results_TD_mod_role.to_excel(writer4, sheet_name='duration_mod')
results_TN_mod_role.to_excel(writer4, sheet_name='number_mod')
results_TD_modtreat_role.to_excel(writer4, sheet_name='duration_modtreat')
results_TN_modtreat_role.to_excel(writer4, sheet_name='number_modtreat')
results_OD_mod_role.to_excel(writer4, sheet_name='OF duration_mod')
results_ON_mod_role.to_excel(writer4, sheet_name='OF number_mod')
results_OD_modtreat_role.to_excel(writer4, sheet_name='OF duration_modtreat')
results_ON_modtreat_role.to_excel(writer4, sheet_name='OF number_modtreat')
results_BD_mod_role.to_excel(writer4, sheet_name='Burrow duration_mod')
results_BN_mod_role.to_excel(writer4, sheet_name='Burrow number_mod')
results_BD_modtreat_role.to_excel(writer4, sheet_name='Burrow duration_modtreat')
results_BN_modtreat_role.to_excel(writer4, sheet_name='Burrow number_modtreat')
data_stat_mean_TD_mod_role.to_excel(writer4, sheet_name='stat_TD_mod')
data_stat_mean_TN_mod_role.to_excel(writer4, sheet_name='stat_TN_mod')
data_stat_mean_TD_modtreat_role.to_excel(writer4, sheet_name='stat_TD_modtreat')
data_stat_mean_TN_modtreat_role.to_excel(writer4, sheet_name='stat_TN_modtreat')
data_stat_mean_OD_mod_role.to_excel(writer4, sheet_name='stat_OD_mod')
data_stat_mean_ON_mod_role.to_excel(writer4, sheet_name='stat_ON_mod')
data_stat_mean_OD_modtreat_role.to_excel(writer4, sheet_name='stat_OD_modtreat')
data_stat_mean_ON_modtreat_role.to_excel(writer4, sheet_name='stat_ON_modtreat')
data_stat_mean_BD_mod_role.to_excel(writer4, sheet_name='stat_BD_mod')
data_stat_mean_BN_mod_role.to_excel(writer4, sheet_name='stat_BN_mod')
data_stat_mean_BD_modtreat_role.to_excel(writer4, sheet_name='stat_BD_modtreat')
data_stat_mean_BN_modtreat_role.to_excel(writer4, sheet_name='stat_BN_modtreat')
data_stat_rest_TD_mod_role.to_excel(writer4, sheet_name='statrest_TD_mod')
data_stat_rest_TN_mod_role.to_excel(writer4, sheet_name='statrest_TN_mod')
data_stat_rest_TD_modtreat_role.to_excel(writer4, sheet_name='statrest_TD_modtreat')
data_stat_rest_TN_modtreat_role.to_excel(writer4, sheet_name='statrest_TN_modtreat')
data_stat_rest_OD_mod_role.to_excel(writer4, sheet_name='statrest_OD_mod')
data_stat_rest_ON_mod_role.to_excel(writer4, sheet_name='statrest_ON_mod')
data_stat_rest_OD_modtreat_role.to_excel(writer4, sheet_name='statrest_OD_modtreat')
data_stat_rest_ON_modtreat_role.to_excel(writer4, sheet_name='statrest_ON_modtreat')
data_stat_rest_BD_mod_role.to_excel(writer4, sheet_name='statrest_BD_mod')
data_stat_rest_BN_mod_role.to_excel(writer4, sheet_name='statrest_BN_mod')
data_stat_rest_BD_modtreat_role.to_excel(writer4, sheet_name='statrest_BD_modtreat')
data_stat_rest_BN_modtreat_role.to_excel(writer4, sheet_name='statrest_BN_modtreat')

results_TD_mod_roleplus.to_excel(writer6, sheet_name='duration_mod')
results_TN_mod_roleplus.to_excel(writer6, sheet_name='number_mod')
results_TD_modtreat_roleplus.to_excel(writer6, sheet_name='duration_modtreat')
results_TN_modtreat_roleplus.to_excel(writer6, sheet_name='number_modtreat')
results_OD_mod_roleplus.to_excel(writer6, sheet_name='OF duration_mod')
results_ON_mod_roleplus.to_excel(writer6, sheet_name='OF number_mod')
results_OD_modtreat_roleplus.to_excel(writer6, sheet_name='OF duration_modtreat')
results_ON_modtreat_roleplus.to_excel(writer6, sheet_name='OF number_modtreat')
results_BD_mod_roleplus.to_excel(writer6, sheet_name='Burrow duration_mod')
results_BN_mod_roleplus.to_excel(writer6, sheet_name='Burrow number_mod')
results_BD_modtreat_roleplus.to_excel(writer6, sheet_name='Burrow duration_modtreat')
results_BN_modtreat_roleplus.to_excel(writer6, sheet_name='Burrow number_modtreat')
data_stat_mean_TD_mod_roleplus.to_excel(writer6, sheet_name='stat_TD_mod')
data_stat_mean_TN_mod_roleplus.to_excel(writer6, sheet_name='stat_TN_mod')
data_stat_mean_TD_modtreat_roleplus.to_excel(writer6, sheet_name='stat_TD_modtreat')
data_stat_mean_TN_modtreat_roleplus.to_excel(writer6, sheet_name='stat_TN_modtreat')
data_stat_mean_OD_mod_roleplus.to_excel(writer6, sheet_name='stat_OD_mod')
data_stat_mean_ON_mod_roleplus.to_excel(writer6, sheet_name='stat_ON_mod')
data_stat_mean_OD_modtreat_roleplus.to_excel(writer6, sheet_name='stat_OD_modtreat')
data_stat_mean_ON_modtreat_roleplus.to_excel(writer6, sheet_name='stat_ON_modtreat')
data_stat_mean_BD_mod_roleplus.to_excel(writer6, sheet_name='stat_BD_mod')
data_stat_mean_BN_mod_roleplus.to_excel(writer6, sheet_name='stat_BN_mod')
data_stat_mean_BD_modtreat_roleplus.to_excel(writer6, sheet_name='stat_BD_modtreat')
data_stat_mean_BN_modtreat_roleplus.to_excel(writer6, sheet_name='stat_BN_modtreat')
data_stat_rest_TD_mod_roleplus.to_excel(writer6, sheet_name='statrest_TD_mod')
data_stat_rest_TN_mod_roleplus.to_excel(writer6, sheet_name='statrest_TN_mod')
data_stat_rest_TD_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_TD_modtreat')
data_stat_rest_TN_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_TN_modtreat')
data_stat_rest_OD_mod_roleplus.to_excel(writer6, sheet_name='statrest_OD_mod')
data_stat_rest_ON_mod_roleplus.to_excel(writer6, sheet_name='statrest_ON_mod')
data_stat_rest_OD_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_OD_modtreat')
data_stat_rest_ON_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_ON_modtreat')
data_stat_rest_BD_mod_roleplus.to_excel(writer6, sheet_name='statrest_BD_mod')
data_stat_rest_BN_mod_roleplus.to_excel(writer6, sheet_name='statrest_BN_mod')
data_stat_rest_BD_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_BD_modtreat')
data_stat_rest_BN_modtreat_roleplus.to_excel(writer6, sheet_name='statrest_BN_modtreat')

data.to_csv("HN004 raw data.csv")
writer1.save()
writer2.save()
writer3.save()
writer4.save()
writer5.save()
writer6.save()
writer1.close()
writer2.close()
writer3.close()
writer4.close()
writer5.close()
writer6.close()

## Make the graphs per column:
#with PdfPages('results_figures.pdf') as pdf:
#    for position, col_name in enumerate(list(results_duration.columns)):
#        if(position>3):
#            fig = plt.figure( dpi=300, figsize=(16.0, 10.0))
#            plt.bar(x3, mean_duration[col_name], color= 'blue', width=barWidth, edgecolor='white')
#            h1 = results_duration[col_name].max()
#            highest = (h1+(h1/6))
#            plt.xticks([r + 0 for r in x3], Treatment_values, rotation='vertical')
#            plt.title('Results'+ col_name , fontweight = 'bold', fontsize = 16)
#            plt.ylim(bottom=0, top= highest)
#            plt.scatter(results['Treatment']*3-3, results[col_name], facecolors=['black'],
#                              edgecolors='none',s=40, alpha=1, linewidth=1, zorder=20)
#            plt.tight_layout()
#            pdf.savefig(fig)
#    
#            plt.close()
#            print(position, col_name)

