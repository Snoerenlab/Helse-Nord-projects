# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:50:09 2019 update 03-9-2020 run in Python 3.7.3


@author: Eelke Snoeren

THIS PYTHON SCRIPT WILL CREATE A RESULT EXCEL-FILE
FROM RAW DATA FROM OBSERVER. IT IS DEVELOPED ON HN003, THE FEMALE RAT SEX DATA.

A partner mistake is set on less than 5 copulations. Check the raw data to check
whether these were really mistakes.

TO DO BEFOREHAND
1) CHANGE THE PATH OF PYTHON TO YOUR DATA FOLDER 
2) CHANGE THE PATH AND FILENAME TO THE RIGHT RESULTS DOCUMENT
3) FILL IN TREATMENT GROUPS (if your have more than 6, the program needs adjustments)
6) MATCH X-AX SCALE TO NUMBER OF TREATMENT GROUPS
7) FILL IN THE COLUMNS FROM YOUR RAW EXCEL FILE, AND ADAPT THE DATAFRAME COLUMNS
8) FILL IN THE BEHAVIORS YOU SCORE FROM BA-BZ
9) FILL OUT YOUR OBSERVATION NAMES AS THEY WERE IN OA-OZ
10) FILL OUT YOUR RATCODE IN EF/EM
11) FILL IN RESULT SHEET LIST

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
from pandas import ExcelWriter
import openpyxl
pd.set_option('use_inf_as_na', True)

# Define the directory in which you stored the data (use / instead of \)
directory= "C:/Users/esn001/Documents/python/Python 3.8/Data projects/HN Jan"

# Define the directory from which the files should come
os.chdir(directory)

# Define output file names
out_path1 = "%s/Output/HN003_5perc_results.xlsx" % directory
out_path2 = "%s/Output/HN003_5perc_resultspermin.xlsx" % directory
out_path3 = "%s/Output/HN003_5perc_resultsmod.xlsx" % directory
out_path4 = "%s/Output/HN003_5perc_resultsmodtreat.xlsx" % directory
out_path5 = "%s/Output/HN003_5perc_statistics.xlsx" % directory
out_path6 = "%s/Output/HN003_5perc_testresults.xlsx" % directory

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
#writer5 = pd.ExcelWriter(out_path5, engine='xlsxwriter')
#data_CB1.to_excel(writer5, sheet_name='data_CB1')
#data.to_excel(writer5,sheet_name='data')
#writer5.save()
#writer5.close()

# Fill out your short column names behind the definition a-z
A='Index'
B='Date_Time_Absolute_dmy_hmsf'
C='Date_dmy'
D='Time_Absolute_hms'
E='Time_Absolute_f'
F='Time_Relative_hmsf'
G='Time_Relative_hms'
H='Time_Relative_f'
I='Time_Relative_sf' # Time
J='Duration_sf'
K='Observation'
L='Event_Log'
M='Subject_raw'
N='Behavior'
O='Modifier_1'
P='Modifier_2'
Q='Event_Type'
R='Comment' 
S='RatID_raw'
T='Treatment_raw'

# For the rest of the document we will use these new terms for the "important behaviors"
TIME='Time'
OBS='Observation'
BEH='Behavior'
SUBRAW='Subject_raw'
MODSUB='Modifier_subject'
MODLOC='Modifier_location'
EVENT='Event_type'
RATIDRAW='RatID_raw'
RATID='RatID'
MODID='ModID'
TREATRAW='Treatment_raw'
TREAT='Treatment'
MODTREAT='Treatment_mod'
MODSEX='Sex_mod'
MODGROUP='Group_mod'

# Fill out your treatment/stimulus behind definition SA-SZ
SA='CTR-females'
SB='FLX-females'
SC='CTR-males'
SD='FLX-males'
SE='Stimulus4'
SF='Stimulus5' 

Stimuli_values= (SA,SB,SC,SD)

# Fill in which columns are important per result excel sheet later
list_resultsheet=(OBS,'Cohort','CB',TREAT,'Start_estrus','End_estrus','Duration_estrus_min')

# Set position of bar on X axis - MAKE SURE IT MATCHES YOUR NUMBER OF GROUPS
# set width of bar
barWidth = 2
x1 = [0, 5, 10, 15, 20, 25] 
x2 = [x + barWidth for x in x1]
x3 = [0, 3, 6, 9, 12, 15]

Treatment_values= (SA,SB)

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

## ratcodes males
#ratcodes=(EM11,EM12,EM13,EM14,EM21,EM22,EM23,EM24,EM31,EM32,EM33,EM34,EM41,EM42,EM43,EM44,EM51,EM52,EM53,EM54)

# ratcodes females
ratcodes=(EF11,EF12,EF13,EF14,EF21,EF22,EF23,EF24,EF31,EF32,EF33,EF34,EF41,EF42,EF43,EF44,EF51,EF52,EF53,EF54)

# Fill out your behavioral observations behind definition BA-BZ and BSA-BSZ
BA='Any other behavior'
BB='Rejection'
BC='start copulatory bout'
BD='white noise on'
BE='white noise off'

BSA='lordosisdoubt'
BSB='Lordosis'
BSC='Paracopulatory behavior'
BSD='Mount (receiving)'
BSE='Intromission (receiving)'
BSF='Ejaculation (receiving)'
BSG='Sniffing others'
BSH='Grooming others'
BSI='Sniffing anogenitally'
BSJ='Pursuing/chasing'
BCA='Boxing/wrestling'
BCB='Nose-off'
BCC='Fighting with other'
BCD='Flee'

# Fill in your extra behavioral calculations behind definition EA-EZ
EA='Total copulations' # mounts, intromissions and ejaculations
EB='Lordosis quotient' # lordosis / copulations * 100%
EC='Active social behavior' # grooming + sniffing + anogenitally sniffing
#ED='Active social behavior plus' # grooming + pursuing + sniffing + anogenitally sniffing
EE='Conflict behavior' # nose-off + boxing + fighting + chase away + flee
EF='Total lordosis' # lordosis + lordosisdoubt
EG='Lordosis quotient plus' # LQ on Total lordosis
#EF='Total self-grooming' #postcopulatory grooming + selfgrooming

# Make a list of the standard behaviors and the to be calculated behaviors
list_behaviors=list((BA,BB,BSA,BSB,BSC,BSD,BSE,BSF,BSG,BSH,BSI,BSJ,BCA,BCB,BCC,BCD))
list_behaviors_social =list((BSA,BSB,BSC,BSD,BSE,BSF,BSG,BSH,BSI,BSJ,BCA,BCB,BCC,BCD))
list_behaviors_extra=list((EA,EB,EC,EE,EF,EG))
list_behaviors_sex=list((BSA,BSB,BSC,BSD,BSE,BSF))
list_results=list((BSA,BSB,BSC,BSD,BSE,BSF,EA,EB,EC,EE,EF,EG,BSG,BSH,BSI,BSJ,BCA,BCB,BCC,BCD,BA,BB))
list_results_social=list((BSA,BSB,BSC,BSD,BSE,BSF,BSG,BSH,BSI,BSJ,BCA,BCB,BCC,BCD))
list_intervals=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

# Fill out your observation names, so that they can be splitted in the right experiment
#OA= 
# Rename columns (add or remove letters according to number of columns)
dataraw.columns = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]
dataraw.columns=[A,B,C,D,E,F,G,H,TIME,J,OBS,L,SUBRAW,BEH,MODSUB,MODLOC,EVENT,R,RATIDRAW,TREATRAW]

# Make a new datafile with selected columns
data_full=dataraw[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT]]
data_full = data_full.loc[((data_full[SUBRAW] == 'F1') | (data_full[SUBRAW] == 'F2') |(data_full[SUBRAW] == 'F3') |(data_full[SUBRAW] == 'F4')),:]
data_full[SUBRAW]=data_full[SUBRAW].replace({'F': 'Female '},regex=True)

# Make a column for the experiment number
#data_full=data_full.assign(CB =lambda x: data_full.Observation.str.split('\s+').str[-1])
data_full=data_full.assign(Cohort =lambda x: data_full.Observation.str.split('- ').str[-1])
data_full['Cohort']=data_full['Cohort'].str.upper()

# Make a columns with RatID
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Female 1'),EF11, "")
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Female 2'),EF12, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Female 3'),EF13, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Female 4'),EF14, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Male 1'),EM11, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Male 2'),EM12, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Male 3'),EM13, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE1')&(data_full[SUBRAW]=='Male 4'),EM14, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Female 1'),EF21, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Female 2'),EF22, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Female 3'),EF23, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Female 4'),EF24, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Male 1'),EM21, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Male 2'),EM22, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Male 3'),EM23, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE2')&(data_full[SUBRAW]=='Male 4'),EM24, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Female 1'),EF31, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Female 2'),EF32, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Female 3'),EF33, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Female 4'),EF34, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Male 1'),EM31, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Male 2'),EM32, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Male 3'),EM33, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE3')&(data_full[SUBRAW]=='Male 4'),EM34, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Female 1'),EF41, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Female 2'),EF42, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Female 3'),EF43, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Female 4'),EF44, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Male 1'),EM41, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Male 2'),EM42, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Male 3'),EM43, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE4')&(data_full[SUBRAW]=='Male 4'),EM44, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Female 1'),EF51, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Female 2'),EF52, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Female 3'),EF53, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Female 4'),EF54, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Male 1'),EM51, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Male 2'),EM52, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Male 3'),EM53, data_full[RATID])
data_full[RATID]=np.where((data_full['Cohort']=='SNE5')&(data_full[SUBRAW]=='Male 4'),EM54, data_full[RATID])
data_full[RATID]=np.where(data_full[SUBRAW]=='unclear','unclear', data_full[RATID])

# Make sure all rats are in the dataframe, otherwise fill in empty row.
ratcodes_in=list(data_full.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing= list(returnNotMatches(ratcodes_in,ratcodes))
for i in missing:
    s_missing = pd.Series([np.NaN,np.NaN,i,'Any other behavior',np.NaN,np.NaN,np.NaN,np.NaN,i], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID])
    data_full= data_full.append(s_missing, ignore_index=True)

# Create dataframes for ModID for the modifier subject based on experiments 
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Female 1'),EF11, "")
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Female 2'),EF12, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Female 3'),EF13, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Female 4'),EF14, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Male 1'),EM11, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Male 2'),EM12, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Male 3'),EM13, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE1')&(data_full[MODSUB]=='Male 4'),EM14, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Female 1'),EF21, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Female 2'),EF22, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Female 3'),EF23, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Female 4'),EF24, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Male 1'),EM21, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Male 2'),EM22, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Male 3'),EM23, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE2')&(data_full[MODSUB]=='Male 4'),EM24, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Female 1'),EF31, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Female 2'),EF32, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Female 3'),EF33, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Female 4'),EF34, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Male 1'),EM31, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Male 2'),EM32, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Male 3'),EM33, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE3')&(data_full[MODSUB]=='Male 4'),EM34, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Female 1'),EF41, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Female 2'),EF42, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Female 3'),EF43, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Female 4'),EF44, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Male 1'),EM41, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Male 2'),EM42, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Male 3'),EM43, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE4')&(data_full[MODSUB]=='Male 4'),EM44, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Female 1'),EF51, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Female 2'),EF52, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Female 3'),EF53, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Female 4'),EF54, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Male 1'),EM51, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Male 2'),EM52, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Male 3'),EM53, data_full[MODID])
data_full[MODID]=np.where((data_full['Cohort']=='SNE5')&(data_full[MODSUB]=='Male 4'),EM54, data_full[MODID])
data_full[MODID]=np.where(data_full[MODSUB]=='unclear','unclear', data_full[MODID])


# Make a column with the treatments per rat
data_full[TREAT]=np.where(((data_full[RATID]=='FC1')|(data_full[RATID]=='FC2')|(data_full[RATID]=='FC3')|(data_full[RATID]=='FC4')|
        (data_full[RATID]=='FC5')|(data_full[RATID]=='FC6')|(data_full[RATID]=='FC7')|(data_full[RATID]=='FC8')|(data_full[RATID]=='FC9')|
        (data_full[RATID]=='FC10')),SA, "")
data_full[TREAT]=np.where(((data_full[RATID]=='FF1')|(data_full[RATID]=='FF2')|(data_full[RATID]=='FF3')|(data_full[RATID]=='FF4')|
        (data_full[RATID]=='FF5')|(data_full[RATID]=='FF6')|(data_full[RATID]=='FF7')|(data_full[RATID]=='FF8')|(data_full[RATID]=='FF9')|
        (data_full[RATID]=='FF10')),SB, data_full[TREAT])
data_full[TREAT]=np.where(((data_full[RATID]=='MC1')|(data_full[RATID]=='MC2')|(data_full[RATID]=='MC3')|(data_full[RATID]=='MC4')|
        (data_full[RATID]=='MC5')|(data_full[RATID]=='MC6')|(data_full[RATID]=='MC7')|(data_full[RATID]=='MC8')|(data_full[RATID]=='MC9')|
        (data_full[RATID]=='MC10')),SC, data_full[TREAT])
data_full[TREAT]=np.where(((data_full[RATID]=='MF1')|(data_full[RATID]=='MF2')|(data_full[RATID]=='MF3')|(data_full[RATID]=='MF4')|
        (data_full[RATID]=='MF5')|(data_full[RATID]=='MF6')|(data_full[RATID]=='MF7')|(data_full[RATID]=='MF8')|(data_full[RATID]=='MF9')|
        (data_full[RATID]=='MF10')),SD, data_full[TREAT])

# Make a column with the treatments per modifier
data_full[MODTREAT]=np.where(((data_full[MODID]=='FC1')|(data_full[MODID]=='FC2')|(data_full[MODID]=='FC3')|(data_full[MODID]=='FC4')|
        (data_full[MODID]=='FC5')|(data_full[MODID]=='FC6')|(data_full[MODID]=='FC7')|(data_full[MODID]=='FC8')|(data_full[MODID]=='FC9')|
        (data_full[MODID]=='FC10')),SA, "")
data_full[MODTREAT]=np.where(((data_full[MODID]=='FF1')|(data_full[MODID]=='FF2')|(data_full[MODID]=='FF3')|(data_full[MODID]=='FF4')|
        (data_full[MODID]=='FF5')|(data_full[MODID]=='FF6')|(data_full[MODID]=='FF7')|(data_full[MODID]=='FF8')|(data_full[MODID]=='FF9')|
        (data_full[MODID]=='FF10')),SB, data_full[MODTREAT])
data_full[MODTREAT]=np.where(((data_full[MODID]=='MC1')|(data_full[MODID]=='MC2')|(data_full[MODID]=='MC3')|(data_full[MODID]=='MC4')|
        (data_full[MODID]=='MC5')|(data_full[MODID]=='MC6')|(data_full[MODID]=='MC7')|(data_full[MODID]=='MC8')|(data_full[MODID]=='MC9')|
        (data_full[MODID]=='MC10')),SC, data_full[MODTREAT])
data_full[MODTREAT]=np.where(((data_full[MODID]=='MF1')|(data_full[MODID]=='MF2')|(data_full[MODID]=='MF3')|(data_full[MODID]=='MF4')|
        (data_full[MODID]=='MF5')|(data_full[MODID]=='MF6')|(data_full[MODID]=='MF7')|(data_full[MODID]=='MF8')|(data_full[MODID]=='MF9')|
        (data_full[MODID]=='MF10')),SD, data_full[MODTREAT])

# Make a column with sex per modifier
data_full[MODSEX]=np.where((data_full[MODTREAT]==SA)|(data_full[MODTREAT]==SB),'female','male')
data_full[MODSEX]=np.where(data_full[MODID]=="","",data_full[MODSEX])

# Make a column with treatmentgroup per modifier
data_full[MODGROUP]=np.where((data_full[MODTREAT]==SA)|(data_full[MODTREAT]==SC),'CTR','FLX')
data_full[MODGROUP]=np.where(data_full[MODID]=="","",data_full[MODGROUP])

# Delete the rows that "end" a behavior
# Drop a row by condition
data_full=data_full[data_full.Event_type != 'State stop']

# Delete the rows that do not contain a behavior or ratID
data_full=data_full[data_full.Subject_raw != ""]
data_full=data_full[data_full.Behavior != ""]

# Calculate the durations of each behavior
data_full= data_full.sort_values(by=['RatID','Time'])
data_full['time_diff'] = data_full['Time'].diff()

# Delete the times there were the RatID of next rat starts
data_full.loc[data_full.RatID != data_full.RatID.shift(), 'time_diff'] = None

# Now put the time differences to the right behavior in column 'durations'
data_full['durations'] = data_full.time_diff.shift(-1)

for i in missing:
    data_full['durations']=np.where(data_full[RATID]==i,0.001,data_full['durations'])

data_full= data_full.dropna(axis=0, subset=['durations'])

# Mark beginning per rat
data_full['obs_num'] = data_full.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_full = data_full.sort_values(by=['RatID','Time'], ascending = False)
data_full['obs_num_back'] = data_full.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_full = data_full.sort_values(by=['RatID','Time'])

# Mark the lordosis
data_full['Lordosis_mark']=np.where(data_full[BEH]=='Lordosis',1,np.NaN)
data_full['Lordosis_marktime']=np.where(data_full['Lordosis_mark']==1,data_full[TIME],np.NaN)
data_full['Lordosis_marktime']=np.where(data_full['obs_num']==1,data_full[TIME],data_full['Lordosis_marktime'])
data_full['Lordosis_marktime'].fillna(method = "ffill", inplace=True)        
data_full['Lordosis_diff']=np.where(data_full['Lordosis_mark']==1,data_full['Lordosis_marktime'].diff(),np.NaN)

# make a counter for lordosis per rat
data_full['ratID_lord'] = data_full['Lordosis_mark'].map(str) + data_full[RATID]
data_full['Firstlordosis'] = data_full.groupby('ratID_lord')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_full['Firstlordosis'] = np.where(data_full['Lordosis_mark'] ==1, data_full['Firstlordosis'], np.NaN)

data_full = data_full.sort_values(by=['RatID','Time'], ascending = False)
data_full['Lastlordosis'] = data_full.groupby('ratID_lord')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_full = data_full.sort_values(by=['RatID','Time'])
data_full['Lastlordosis'] = np.where(data_full['Lordosis_mark'] ==1, data_full['Lastlordosis'], np.NaN)

# Mark start of CB
data_full['Start_CB']=np.where((data_full['Lordosis_diff']>3600),"Start_CB","")
data_full['Start_CB']=np.where((data_full['Firstlordosis']==1),"Start_CB",data_full['Start_CB'])

# Mark the lordosis for end of CB
data_full['Lordosis_diff2'] = data_full.Lordosis_diff.shift(-1)
data_full['Lordosis_diff2'] = np.where(data_full['obs_num_back']==1,3700,data_full['Lordosis_diff2'])
data_full['Lordosis_diff2'].fillna(method = "bfill", inplace=True)   
data_full['Lordosis_diff2']=np.where(data_full['Lordosis_mark']==1,data_full['Lordosis_diff2'],np.NaN)

# Mark end of CB
data_full['End_CB']=np.where((data_full['Lordosis_diff2']>3600),"End_CB","")
data_full['End_CB']=np.where((data_full['Lastlordosis']==1),"End_CB",data_full['End_CB'])

# Final mark CB
data_full['CB_mark']=np.where((data_full['Start_CB']=="Start_CB")&(data_full['End_CB']=="End_CB"),"Single",data_full['Start_CB'])
data_full['CB_mark']=np.where((data_full['CB_mark']!=""),data_full['CB_mark'],data_full['End_CB'])

# Count the copulatory bouts
data_full['RatID_CBmark'] = data_full['RatID'].map(str) + data_full['CB_mark']
data_full['CB_count']=data_full.groupby('RatID_CBmark')['CB_mark'].transform(lambda x: np.arange(1, len(x) + 1))

# forward fill the start CB
data_full['CB_pre']=np.where(data_full['CB_mark']=="Start_CB",11111,np.NaN)
data_full['CB_pre']=np.where(data_full['CB_mark']=="End_CB",22222,data_full['CB_pre'])
data_full['CB_pre']=np.where(data_full['CB_mark']=="Single",33333,data_full['CB_pre'])
data_full['CB_pre'].fillna(method = "ffill", inplace=True)

data_full['CB_pre']=np.where(data_full['CB_mark']=="Start_CB",(data_full['CB_pre']+data_full['CB_count']),data_full['CB_pre'])
data_full['CB_pre']=np.where(data_full['CB_pre']==11111,np.NaN,data_full['CB_pre'])
data_full['CB_pre']=np.where(data_full['CB_mark']=="End_CB",((data_full['CB_pre']+data_full['CB_count'])-11111),data_full['CB_pre'])
data_full['CB_pre'].fillna(method = "ffill", inplace=True)
data_full['CB_pre']=np.where(data_full['CB_pre']==22222,np.NaN,data_full['CB_pre'])
data_full['CB_pre']=np.where(data_full['CB_mark']=="Single",(data_full['CB_count']+44444),data_full['CB_pre'])
data_full['CB_pre']=np.where(data_full['CB_pre']==33333,np.NaN,data_full['CB_pre'])

data_full['CB']=np.where(data_full['CB_pre']==11112,"CB1","")
data_full['CB']=np.where(data_full['CB_pre']==11113,"CB2",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11114,"CB3",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11115,"CB4",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11116,"CB5",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11117,"CB6",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11118,"CB7",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11119,"CB8",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11120,"CB9",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11121,"CB10",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11122,"CB11",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11123,"CB12",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11124,"CB13",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11125,"CB14",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']==11126,"CB15",data_full['CB'])
data_full['CB']=np.where(data_full['CB_pre']>44444,"Single",data_full['CB'])

# Get dataframe data with only data from CB and single lordosis  
data_all = data_full.loc[(data_full['CB'] != ""),:]
data_all=data_all[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB1 = data_full.loc[(data_full['CB'] == "CB1"),:]
data_CB1=data_CB1[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB2 = data_full.loc[(data_full['CB'] == "CB2"),:]
data_CB2=data_CB2[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB3 = data_full.loc[(data_full['CB'] == "CB3"),:]
data_CB3=data_CB3[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB4 = data_full.loc[(data_full['CB'] == "CB4"),:]
data_CB4=data_CB4[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB5 = data_full.loc[(data_full['CB'] == "CB5"),:]
data_CB5=data_CB5[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]
data_CB6 = data_full.loc[(data_full['CB'] == "CB6"),:]
data_CB6=data_CB6[[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB']]


# Make sure all rats are in the dataframe of data and data_CB1, otherwise fill in empty row.
ratcodes_in_data_all=list(data_all.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_all= list(returnNotMatches(ratcodes_in_data_all,ratcodes))
for i in missing_all:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_all= data_all.append(s_missing, ignore_index=True)

ratcodes_in_data_CB1=list(data_CB1.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB1= list(returnNotMatches(ratcodes_in_data_CB1,ratcodes))
for i in missing_CB1:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB1= data_CB1.append(s_missing, ignore_index=True)

ratcodes_in_data_CB2=list(data_CB2.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB2= list(returnNotMatches(ratcodes_in_data_CB2,ratcodes))
for i in missing_CB2:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB2= data_CB2.append(s_missing, ignore_index=True)

ratcodes_in_data_CB3=list(data_CB3.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB3= list(returnNotMatches(ratcodes_in_data_CB3,ratcodes))
for i in missing_CB3:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB3= data_CB3.append(s_missing, ignore_index=True)

ratcodes_in_data_CB4=list(data_CB4.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB4= list(returnNotMatches(ratcodes_in_data_CB4,ratcodes))
for i in missing_CB4:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB4= data_CB4.append(s_missing, ignore_index=True)

ratcodes_in_data_CB5=list(data_CB5.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB5= list(returnNotMatches(ratcodes_in_data_CB5,ratcodes))
for i in missing_CB5:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB5= data_CB5.append(s_missing, ignore_index=True)

ratcodes_in_data_CB6=list(data_CB6.RatID.unique())
def returnNotMatches(a, b):
    return ((x for x in b if x not in a))

missing_CB6= list(returnNotMatches(ratcodes_in_data_CB6,ratcodes))
for i in missing_CB6:
    s_missing = pd.Series([np.NaN,np.NaN,i,'None','other','Burrow',np.NaN,np.NaN,i,np.NaN,'other','other','other',
                           'other',0.001,np.NaN,np.NaN,np.NaN], 
                          index=[TIME,OBS,SUBRAW,BEH,MODSUB,MODLOC,EVENT,'Cohort',RATID,MODID,TREAT,MODTREAT,MODSEX,MODGROUP,'durations',
           'Start_CB','End_CB','CB'])
    data_CB6= data_CB6.append(s_missing, ignore_index=True)

# Just to get notification this part is finished
print("loading finished")

# PREPARE THE DATAFRAME FOR ALL DATA
# Create unique code per behavior per rat
data_all['ratID_beh'] = data_all[BEH].map(str) + data_all[RATID]
 
# Create unique code per behavior per rat per location
data_all['ratID_beh_loc'] = data_all[MODLOC].map(str) + data_all['ratID_beh']

# Create unique code per behavior per rat per sex
data_all['ratID_beh_sex'] = data_all['ratID_beh'].map(str) + data_all[MODSEX]

# Create unique code per behavior per rat per treatment group
data_all['ratID_beh_treat'] = data_all['ratID_beh'].map(str) + data_all[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_all['ratID_beh_loc_treat'] = data_all['ratID_beh_loc'].map(str) + data_all[MODTREAT]

# Create unique code per behavior per rat per ModID
data_all['ratID_beh_modsub'] = data_all[MODSUB].map(str)+data_all['ratID_beh'] 

# Mark beginning per rat
data_all['obs_num'] = data_all.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_all['obs_beh_num'] = data_all.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_loc_num'] = data_all.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_sex_num'] = data_all.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_treat_num'] = data_all.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_loc_treat_num'] = data_all.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_modsub_num'] = data_all.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_all = data_all.sort_values(by=['ratID_beh','Time'], ascending = False)
data_all['obs_beh_num_back'] = data_all.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_loc_num_back'] = data_all.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_sex_num_back'] = data_all.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_treat_num_back'] = data_all.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_loc_treat_num_back'] = data_all.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_modsub_num_back'] = data_all.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all = data_all.sort_values(by=['RatID','Time'], ascending = False)
data_all['obs_num_back'] = data_all.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all = data_all.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_all['obs_beh_sumdur']=data_all.groupby('ratID_beh')['durations'].cumsum()
data_all['obs_beh_loc_sumdur']=data_all.groupby('ratID_beh_loc')['durations'].cumsum()
data_all['obs_beh_treat_sumdur']=data_all.groupby('ratID_beh_treat')['durations'].cumsum()
data_all['obs_beh_loc_treat_sumdur']=data_all.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_all['obs_beh_modsub_sumdur']=data_all.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_all['Start_estrus']= np.where(data_all['obs_num']==1,data_all[TIME], np.NaN)
data_all['Start_estrus'].fillna(method="ffill", inplace=True)
data_all['End_estrus']= np.where(data_all['obs_num_back']==1,data_all[TIME], np.NaN)
data_all['End_estrus'].fillna(method="backfill", inplace=True)
data_all['Duration_estrus_min']=((data_all['End_estrus']-data_all['Start_estrus'])/60)

for i in missing_all:
    data_all['Start_estrus']=np.where(data_all[RATID]==i,np.NaN,data_all['Start_estrus'])
    data_all['End_estrus']=np.where(data_all[RATID]==i,np.NaN,data_all['End_estrus'])
    data_all['Duration_estrus_min']=np.where(data_all[RATID]==i,np.NaN,data_all['Duration_estrus_min'])


# PREPARE THE FRAME FOR ALL DATA_CB1
# Create unique code per behavior per rat
data_CB1['ratID_beh'] = data_CB1[BEH].map(str) + data_CB1[RATID]
 
# Create unique code per behavior per rat per location
data_CB1['ratID_beh_loc'] = data_CB1[MODLOC].map(str) + data_CB1['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB1['ratID_beh_sex'] = data_CB1['ratID_beh'].map(str) + data_CB1[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB1['ratID_beh_treat'] = data_CB1['ratID_beh'].map(str) + data_CB1[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB1['ratID_beh_loc_treat'] = data_CB1['ratID_beh_loc'].map(str) + data_CB1[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB1['ratID_beh_modsub'] = data_CB1[MODSUB].map(str)+data_CB1['ratID_beh'] 

# Mark beginning per rat
data_CB1['obs_num'] = data_CB1.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB1['obs_beh_num'] = data_CB1.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_loc_num'] = data_CB1.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_sex_num'] = data_CB1.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_treat_num'] = data_CB1.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_loc_treat_num'] = data_CB1.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_modsub_num'] = data_CB1.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB1 = data_CB1.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB1['obs_beh_num_back'] = data_CB1.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_loc_num_back'] = data_CB1.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_sex_num_back'] = data_CB1.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_treat_num_back'] = data_CB1.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_loc_treat_num_back'] = data_CB1.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_modsub_num_back'] = data_CB1.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1 = data_CB1.sort_values(by=['RatID','Time'], ascending = False)
data_CB1['obs_num_back'] = data_CB1.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1 = data_CB1.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB1['obs_beh_sumdur']=data_CB1.groupby('ratID_beh')['durations'].cumsum()
data_CB1['obs_beh_loc_sumdur']=data_CB1.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB1['obs_beh_treat_sumdur']=data_CB1.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB1['obs_beh_loc_treat_sumdur']=data_CB1.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB1['obs_beh_modsub_sumdur']=data_CB1.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB1['Start_estrus']= np.where(data_CB1['obs_num']==1,data_CB1[TIME], np.NaN)
data_CB1['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB1['End_estrus']= np.where(data_CB1['obs_num_back']==1,data_CB1[TIME], np.NaN)
data_CB1['End_estrus'].fillna(method="backfill", inplace=True)
data_CB1['Duration_estrus_min']=((data_CB1['End_estrus']-data_CB1['Start_estrus'])/60)

for i in missing_CB1:
    data_CB1['Start_estrus']=np.where(data_CB1[RATID]==i,np.NaN,data_CB1['Start_estrus'])
    data_CB1['End_estrus']=np.where(data_CB1[RATID]==i,np.NaN,data_CB1['End_estrus'])
    data_CB1['Duration_estrus_min']=np.where(data_CB1[RATID]==i,np.NaN,data_CB1['Duration_estrus_min'])

# PREPARE THE FRAME FOR ALL DATA_CB2
# Create unique code per behavior per rat
data_CB2['ratID_beh'] = data_CB2[BEH].map(str) + data_CB2[RATID]
 
# Create unique code per behavior per rat per location
data_CB2['ratID_beh_loc'] = data_CB2[MODLOC].map(str) + data_CB2['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB2['ratID_beh_sex'] = data_CB2['ratID_beh'].map(str) + data_CB2[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB2['ratID_beh_treat'] = data_CB2['ratID_beh'].map(str) + data_CB2[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB2['ratID_beh_loc_treat'] = data_CB2['ratID_beh_loc'].map(str) + data_CB2[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB2['ratID_beh_modsub'] = data_CB2[MODSUB].map(str)+data_CB2['ratID_beh'] 

# Mark beginning per rat
data_CB2['obs_num'] = data_CB2.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB2['obs_beh_num'] = data_CB2.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_loc_num'] = data_CB2.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_sex_num'] = data_CB2.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_treat_num'] = data_CB2.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_loc_treat_num'] = data_CB2.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_modsub_num'] = data_CB2.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB2 = data_CB2.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB2['obs_beh_num_back'] = data_CB2.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_loc_num_back'] = data_CB2.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_sex_num_back'] = data_CB2.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_treat_num_back'] = data_CB2.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_loc_treat_num_back'] = data_CB2.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_modsub_num_back'] = data_CB2.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2 = data_CB2.sort_values(by=['RatID','Time'], ascending = False)
data_CB2['obs_num_back'] = data_CB2.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2 = data_CB2.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB2['obs_beh_sumdur']=data_CB2.groupby('ratID_beh')['durations'].cumsum()
data_CB2['obs_beh_loc_sumdur']=data_CB2.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB2['obs_beh_treat_sumdur']=data_CB2.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB2['obs_beh_loc_treat_sumdur']=data_CB2.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB2['obs_beh_modsub_sumdur']=data_CB2.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB2['Start_estrus']= np.where(data_CB2['obs_num']==1,data_CB2[TIME], np.NaN)
data_CB2['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB2['End_estrus']= np.where(data_CB2['obs_num_back']==1,data_CB2[TIME], np.NaN)
data_CB2['End_estrus'].fillna(method="backfill", inplace=True)
data_CB2['Duration_estrus_min']=((data_CB2['End_estrus']-data_CB2['Start_estrus'])/60)

for i in missing_CB2:
    data_CB2['Start_estrus']=np.where(data_CB2[RATID]==i,np.NaN,data_CB2['Start_estrus'])
    data_CB2['End_estrus']=np.where(data_CB2[RATID]==i,np.NaN,data_CB2['End_estrus'])
    data_CB2['Duration_estrus_min']=np.where(data_CB2[RATID]==i,np.NaN,data_CB2['Duration_estrus_min'])

# PREPARE THE FRAME FOR ALL DATA_CB3
# Create unique code per behavior per rat
data_CB3['ratID_beh'] = data_CB3[BEH].map(str) + data_CB3[RATID]
 
# Create unique code per behavior per rat per location
data_CB3['ratID_beh_loc'] = data_CB3[MODLOC].map(str) + data_CB3['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB3['ratID_beh_sex'] = data_CB3['ratID_beh'].map(str) + data_CB3[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB3['ratID_beh_treat'] = data_CB3['ratID_beh'].map(str) + data_CB3[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB3['ratID_beh_loc_treat'] = data_CB3['ratID_beh_loc'].map(str) + data_CB3[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB3['ratID_beh_modsub'] = data_CB3[MODSUB].map(str)+data_CB3['ratID_beh'] 

# Mark beginning per rat
data_CB3['obs_num'] = data_CB3.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB3['obs_beh_num'] = data_CB3.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_loc_num'] = data_CB3.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_sex_num'] = data_CB3.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_treat_num'] = data_CB3.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_loc_treat_num'] = data_CB3.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_modsub_num'] = data_CB3.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB3 = data_CB3.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB3['obs_beh_num_back'] = data_CB3.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_loc_num_back'] = data_CB3.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_sex_num_back'] = data_CB3.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_treat_num_back'] = data_CB3.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_loc_treat_num_back'] = data_CB3.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_modsub_num_back'] = data_CB3.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3 = data_CB3.sort_values(by=['RatID','Time'], ascending = False)
data_CB3['obs_num_back'] = data_CB3.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3 = data_CB3.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB3['obs_beh_sumdur']=data_CB3.groupby('ratID_beh')['durations'].cumsum()
data_CB3['obs_beh_loc_sumdur']=data_CB3.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB3['obs_beh_treat_sumdur']=data_CB3.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB3['obs_beh_loc_treat_sumdur']=data_CB3.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB3['obs_beh_modsub_sumdur']=data_CB3.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB3['Start_estrus']= np.where(data_CB3['obs_num']==1,data_CB3[TIME], np.NaN)
data_CB3['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB3['End_estrus']= np.where(data_CB3['obs_num_back']==1,data_CB3[TIME], np.NaN)
data_CB3['End_estrus'].fillna(method="backfill", inplace=True)
data_CB3['Duration_estrus_min']=((data_CB3['End_estrus']-data_CB3['Start_estrus'])/60)

for i in missing_CB3:
    data_CB3['Start_estrus']=np.where(data_CB3[RATID]==i,np.NaN,data_CB3['Start_estrus'])
    data_CB3['End_estrus']=np.where(data_CB3[RATID]==i,np.NaN,data_CB3['End_estrus'])
    data_CB3['Duration_estrus_min']=np.where(data_CB3[RATID]==i,np.NaN,data_CB3['Duration_estrus_min'])

# PREPARE THE FRAME FOR ALL DATA_CB4
# Create unique code per behavior per rat
data_CB4['ratID_beh'] = data_CB4[BEH].map(str) + data_CB4[RATID]
 
# Create unique code per behavior per rat per location
data_CB4['ratID_beh_loc'] = data_CB4[MODLOC].map(str) + data_CB4['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB4['ratID_beh_sex'] = data_CB4['ratID_beh'].map(str) + data_CB4[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB4['ratID_beh_treat'] = data_CB4['ratID_beh'].map(str) + data_CB4[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB4['ratID_beh_loc_treat'] = data_CB4['ratID_beh_loc'].map(str) + data_CB4[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB4['ratID_beh_modsub'] = data_CB4[MODSUB].map(str)+data_CB4['ratID_beh'] 

# Mark beginning per rat
data_CB4['obs_num'] = data_CB4.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB4['obs_beh_num'] = data_CB4.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_loc_num'] = data_CB4.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_sex_num'] = data_CB4.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_treat_num'] = data_CB4.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_loc_treat_num'] = data_CB4.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_modsub_num'] = data_CB4.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB4 = data_CB4.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB4['obs_beh_num_back'] = data_CB4.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_loc_num_back'] = data_CB4.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_sex_num_back'] = data_CB4.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_treat_num_back'] = data_CB4.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_loc_treat_num_back'] = data_CB4.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_modsub_num_back'] = data_CB4.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4 = data_CB4.sort_values(by=['RatID','Time'], ascending = False)
data_CB4['obs_num_back'] = data_CB4.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4 = data_CB4.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB4['obs_beh_sumdur']=data_CB4.groupby('ratID_beh')['durations'].cumsum()
data_CB4['obs_beh_loc_sumdur']=data_CB4.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB4['obs_beh_treat_sumdur']=data_CB4.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB4['obs_beh_loc_treat_sumdur']=data_CB4.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB4['obs_beh_modsub_sumdur']=data_CB4.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB4['Start_estrus']= np.where(data_CB4['obs_num']==1,data_CB4[TIME], np.NaN)
data_CB4['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB4['End_estrus']= np.where(data_CB4['obs_num_back']==1,data_CB4[TIME], np.NaN)
data_CB4['End_estrus'].fillna(method="backfill", inplace=True)
data_CB4['Duration_estrus_min']=((data_CB4['End_estrus']-data_CB4['Start_estrus'])/60)

for i in missing_CB4:
    data_CB4['Start_estrus']=np.where(data_CB4[RATID]==i,np.NaN,data_CB4['Start_estrus'])
    data_CB4['End_estrus']=np.where(data_CB4[RATID]==i,np.NaN,data_CB4['End_estrus'])
    data_CB4['Duration_estrus_min']=np.where(data_CB4[RATID]==i,np.NaN,data_CB4['Duration_estrus_min'])

# PREPARE THE FRAME FOR ALL DATA_CB5
# Create unique code per behavior per rat
data_CB5['ratID_beh'] = data_CB5[BEH].map(str) + data_CB5[RATID]
 
# Create unique code per behavior per rat per location
data_CB5['ratID_beh_loc'] = data_CB5[MODLOC].map(str) + data_CB5['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB5['ratID_beh_sex'] = data_CB5['ratID_beh'].map(str) + data_CB5[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB5['ratID_beh_treat'] = data_CB5['ratID_beh'].map(str) + data_CB5[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB5['ratID_beh_loc_treat'] = data_CB5['ratID_beh_loc'].map(str) + data_CB5[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB5['ratID_beh_modsub'] = data_CB5[MODSUB].map(str)+data_CB5['ratID_beh'] 

# Mark beginning per rat
data_CB5['obs_num'] = data_CB5.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB5['obs_beh_num'] = data_CB5.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_loc_num'] = data_CB5.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_sex_num'] = data_CB5.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_treat_num'] = data_CB5.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_loc_treat_num'] = data_CB5.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_modsub_num'] = data_CB5.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB5 = data_CB5.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB5['obs_beh_num_back'] = data_CB5.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_loc_num_back'] = data_CB5.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_sex_num_back'] = data_CB5.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_treat_num_back'] = data_CB5.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_loc_treat_num_back'] = data_CB5.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_modsub_num_back'] = data_CB5.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5 = data_CB5.sort_values(by=['RatID','Time'], ascending = False)
data_CB5['obs_num_back'] = data_CB5.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5 = data_CB5.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB5['obs_beh_sumdur']=data_CB5.groupby('ratID_beh')['durations'].cumsum()
data_CB5['obs_beh_loc_sumdur']=data_CB5.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB5['obs_beh_treat_sumdur']=data_CB5.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB5['obs_beh_loc_treat_sumdur']=data_CB5.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB5['obs_beh_modsub_sumdur']=data_CB5.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB5['Start_estrus']= np.where(data_CB5['obs_num']==1,data_CB5[TIME], np.NaN)
data_CB5['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB5['End_estrus']= np.where(data_CB5['obs_num_back']==1,data_CB5[TIME], np.NaN)
data_CB5['End_estrus'].fillna(method="backfill", inplace=True)
data_CB5['Duration_estrus_min']=((data_CB5['End_estrus']-data_CB5['Start_estrus'])/60)

for i in missing_CB5:
    data_CB5['Start_estrus']=np.where(data_CB5[RATID]==i,np.NaN,data_CB5['Start_estrus'])
    data_CB5['End_estrus']=np.where(data_CB5[RATID]==i,np.NaN,data_CB5['End_estrus'])
    data_CB5['Duration_estrus_min']=np.where(data_CB5[RATID]==i,np.NaN,data_CB5['Duration_estrus_min'])

# PREPARE THE FRAME FOR ALL DATA_CB6
# Create unique code per behavior per rat
data_CB6['ratID_beh'] = data_CB6[BEH].map(str) + data_CB6[RATID]
 
# Create unique code per behavior per rat per location
data_CB6['ratID_beh_loc'] = data_CB6[MODLOC].map(str) + data_CB6['ratID_beh']

# Create unique code per behavior per rat per sex
data_CB6['ratID_beh_sex'] = data_CB6['ratID_beh'].map(str) + data_CB6[MODSEX]

# Create unique code per behavior per rat per treatment group
data_CB6['ratID_beh_treat'] = data_CB6['ratID_beh'].map(str) + data_CB6[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB6['ratID_beh_loc_treat'] = data_CB6['ratID_beh_loc'].map(str) + data_CB6[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB6['ratID_beh_modsub'] = data_CB6[MODSUB].map(str)+data_CB6['ratID_beh'] 

# Mark beginning per rat
data_CB6['obs_num'] = data_CB6.groupby(RATID)[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors on occurance
data_CB6['obs_beh_num'] = data_CB6.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_loc_num'] = data_CB6.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_sex_num'] = data_CB6.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_treat_num'] = data_CB6.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_loc_treat_num'] = data_CB6.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_modsub_num'] = data_CB6.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB6 = data_CB6.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB6['obs_beh_num_back'] = data_CB6.groupby('ratID_beh')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_loc_num_back'] = data_CB6.groupby('ratID_beh_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_sex_num_back'] = data_CB6.groupby('ratID_beh_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_treat_num_back'] = data_CB6.groupby('ratID_beh_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_loc_treat_num_back'] = data_CB6.groupby('ratID_beh_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_modsub_num_back'] = data_CB6.groupby('ratID_beh_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6 = data_CB6.sort_values(by=['RatID','Time'], ascending = False)
data_CB6['obs_num_back'] = data_CB6.groupby('RatID')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6 = data_CB6.sort_values(by=['RatID','Time'])

# Sum up the durations on occurance
data_CB6['obs_beh_sumdur']=data_CB6.groupby('ratID_beh')['durations'].cumsum()
data_CB6['obs_beh_loc_sumdur']=data_CB6.groupby('ratID_beh_loc')['durations'].cumsum()
data_CB6['obs_beh_treat_sumdur']=data_CB6.groupby('ratID_beh_treat')['durations'].cumsum()
data_CB6['obs_beh_loc_treat_sumdur']=data_CB6.groupby('ratID_beh_loc_treat')['durations'].cumsum()
data_CB6['obs_beh_modsub_sumdur']=data_CB6.groupby('ratID_beh_modsub')['durations'].cumsum()

# Calculate start behavioral estrus
data_CB6['Start_estrus']= np.where(data_CB6['obs_num']==1,data_CB6[TIME], np.NaN)
data_CB6['Start_estrus'].fillna(method="ffill", inplace=True)
data_CB6['End_estrus']= np.where(data_CB6['obs_num_back']==1,data_CB6[TIME], np.NaN)
data_CB6['End_estrus'].fillna(method="backfill", inplace=True)
data_CB6['Duration_estrus_min']=((data_CB6['End_estrus']-data_CB6['Start_estrus'])/60)

for i in missing_CB6:
    data_CB6['Start_estrus']=np.where(data_CB6[RATID]==i,np.NaN,data_CB6['Start_estrus'])
    data_CB6['End_estrus']=np.where(data_CB6[RATID]==i,np.NaN,data_CB6['End_estrus'])
    data_CB6['Duration_estrus_min']=np.where(data_CB6[RATID]==i,np.NaN,data_CB6['Duration_estrus_min'])

# Just to get notification this part is finished
print("bouts finished")

# Calculate how long a 5% time interval is seconds
data_all['5%_interval_sec']=(data_all['Duration_estrus_min']/20*60)
data_all['5%_interval_min']=(data_all['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_all['5%_max']=(data_all['Start_estrus']+data_all['5%_interval_sec'])
data_all['10%_max']=(data_all['Start_estrus']+(2*data_all['5%_interval_sec']))
data_all['15%_max']=(data_all['Start_estrus']+(3*data_all['5%_interval_sec']))
data_all['20%_max']=(data_all['Start_estrus']+(4*data_all['5%_interval_sec']))
data_all['25%_max']=(data_all['Start_estrus']+(5*data_all['5%_interval_sec']))
data_all['30%_max']=(data_all['Start_estrus']+(6*data_all['5%_interval_sec']))
data_all['35%_max']=(data_all['Start_estrus']+(7*data_all['5%_interval_sec']))
data_all['40%_max']=(data_all['Start_estrus']+(8*data_all['5%_interval_sec']))
data_all['45%_max']=(data_all['Start_estrus']+(9*data_all['5%_interval_sec']))
data_all['50%_max']=(data_all['Start_estrus']+(10*data_all['5%_interval_sec']))
data_all['55%_max']=(data_all['Start_estrus']+(11*data_all['5%_interval_sec']))
data_all['60%_max']=(data_all['Start_estrus']+(12*data_all['5%_interval_sec']))
data_all['65%_max']=(data_all['Start_estrus']+(13*data_all['5%_interval_sec']))
data_all['70%_max']=(data_all['Start_estrus']+(14*data_all['5%_interval_sec']))
data_all['75%_max']=(data_all['Start_estrus']+(15*data_all['5%_interval_sec']))
data_all['80%_max']=(data_all['Start_estrus']+(16*data_all['5%_interval_sec']))
data_all['85%_max']=(data_all['Start_estrus']+(17*data_all['5%_interval_sec']))
data_all['90%_max']=(data_all['Start_estrus']+(18*data_all['5%_interval_sec']))
data_all['95%_max']=(data_all['Start_estrus']+(19*data_all['5%_interval_sec']))

data_all['interval']=np.where(((data_all[TIME]>data_all['Start_estrus'])&(data_all[TIME]<data_all['5%_max'])),5,np.NaN)
data_all['interval']=np.where(((data_all[TIME]>data_all['5%_max'])&(data_all[TIME]<data_all['10%_max'])),10,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['10%_max'])&(data_all[TIME]<data_all['15%_max'])),15,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['15%_max'])&(data_all[TIME]<data_all['20%_max'])),20,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['20%_max'])&(data_all[TIME]<data_all['25%_max'])),25,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['25%_max'])&(data_all[TIME]<data_all['30%_max'])),30,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['30%_max'])&(data_all[TIME]<data_all['35%_max'])),35,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['35%_max'])&(data_all[TIME]<data_all['40%_max'])),40,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['40%_max'])&(data_all[TIME]<data_all['45%_max'])),45,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['45%_max'])&(data_all[TIME]<data_all['50%_max'])),50,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['50%_max'])&(data_all[TIME]<data_all['55%_max'])),55,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['55%_max'])&(data_all[TIME]<data_all['60%_max'])),60,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['60%_max'])&(data_all[TIME]<data_all['65%_max'])),65,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['65%_max'])&(data_all[TIME]<data_all['70%_max'])),70,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['70%_max'])&(data_all[TIME]<data_all['75%_max'])),75,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['75%_max'])&(data_all[TIME]<data_all['80%_max'])),80,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['80%_max'])&(data_all[TIME]<data_all['85%_max'])),85,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['85%_max'])&(data_all[TIME]<data_all['90%_max'])),90,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['90%_max'])&(data_all[TIME]<data_all['95%_max'])),95,data_all['interval'])
data_all['interval']=np.where(((data_all[TIME]>data_all['95%_max'])&(data_all[TIME]<data_all['End_estrus'])),100,data_all['interval'])

# mark the last behaviors before a new interval
data_all['interval_check']=np.where((data_all['interval']>1),1,np.NaN)
data_all['interval_check']=np.where(((data_all['interval']!=data_all['interval'].shift(-1))&(data_all['interval_check']==1)&(data_all[BEH]!=BSB)),1,np.NaN)
data_all['interval_check']=np.where(((data_all['interval_check']==1) & (data_all['interval']==100)),np.NaN,data_all['interval_check'])

# determine the amount of second left within the interval
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==5)),(data_all['5%_max']-data_all[TIME]),np.NaN)
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==10)),(data_all['10%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==15)),(data_all['15%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==20)),(data_all['20%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==25)),(data_all['25%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==30)),(data_all['30%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==35)),(data_all['35%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==40)),(data_all['40%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==45)),(data_all['45%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==50)),(data_all['50%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==55)),(data_all['55%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==60)),(data_all['60%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==65)),(data_all['65%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==70)),(data_all['70%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==75)),(data_all['75%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==80)),(data_all['80%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==85)),(data_all['85%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==90)),(data_all['90%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])
data_all['behavior_duration_checkleft']=np.where(((data_all['interval_check']==1)&(data_all['interval']==95)),(data_all['95%_max']-data_all[TIME]),data_all['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_all['behavior_duration_fixtonext']=data_all['durations']-data_all['behavior_duration_checkleft']
data_all['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_all['interval_fix']=np.where(data_all['interval_check']==1,(data_all['interval']+5),np.NaN)
data_all['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_all['behavior_fix']=np.where(data_all['interval_check']==1,data_all[BEH],np.NaN)
data_all['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_all['ratID_beh_int'] = data_all['interval'].map(str) + data_all['ratID_beh']

# Create unique code per behavior per rat per location
data_all['ratID_beh_int_loc'] = data_all[MODLOC].map(str) + data_all['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_all['ratID_beh_int_sex'] = data_all['ratID_beh_int'].map(str) + data_all[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_all['ratID_beh_int_treat'] = data_all['ratID_beh_int'].map(str) + data_all[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_all['ratID_beh_int_loc_treat'] = data_all['ratID_beh_int_loc'].map(str) + data_all[MODTREAT]

# Create unique code per behavior per rat per ModID
data_all['ratID_beh_int_modsub'] = data_all[MODSUB].map(str)+data_all['ratID_beh_int'] 

# Number the behaviors on occurance
data_all['obs_beh_int_num'] = data_all.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_loc_num'] = data_all.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_sex_num'] = data_all.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_treat_num'] = data_all.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_loc_treat_num'] = data_all.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_modsub_num'] = data_all.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_all = data_all.sort_values(by=['ratID_beh','Time'], ascending = False)
data_all['obs_beh_int_num_back'] = data_all.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_loc_num_back'] = data_all.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_sex_num_back'] = data_all.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_treat_num_back'] = data_all.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_loc_treat_num_back'] = data_all.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_all['obs_beh_int_modsub_num_back'] = data_all.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_all = data_all.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_all['durations']=np.where(data_all['interval_check']==1, data_all['behavior_duration_checkleft'],data_all['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_all['durations']=np.where(((data_all['interval']==data_all['interval_fix'])&(data_all['behavior_fix']==data_all[BEH])&
        (data_all['obs_beh_int_num']==1)),(data_all['durations']+data_all['behavior_duration_fixtonext']),data_all['durations'])

# Sum up the durations on occurance
data_all['obs_beh_int_sumdur']=data_all.groupby('ratID_beh_int')['durations'].cumsum()
data_all['obs_beh_int_loc_sumdur']=data_all.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_all['obs_beh_int_treat_sumdur']=data_all.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_all['obs_beh_int_sex_sumdur']=data_all.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_all['obs_beh_int_loc_treat_sumdur']=data_all.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_all['obs_beh_int_modsub_sumdur']=data_all.groupby('ratID_beh_int_modsub')['durations'].cumsum()


# Calculate how long a 5% time interval is seconds
data_CB1['5%_interval_sec']=(data_CB1['Duration_estrus_min']/20*60)
data_CB1['5%_interval_min']=(data_CB1['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB1['5%_max']=(data_CB1['Start_estrus']+data_CB1['5%_interval_sec'])
data_CB1['10%_max']=(data_CB1['Start_estrus']+(2*data_CB1['5%_interval_sec']))
data_CB1['15%_max']=(data_CB1['Start_estrus']+(3*data_CB1['5%_interval_sec']))
data_CB1['20%_max']=(data_CB1['Start_estrus']+(4*data_CB1['5%_interval_sec']))
data_CB1['25%_max']=(data_CB1['Start_estrus']+(5*data_CB1['5%_interval_sec']))
data_CB1['30%_max']=(data_CB1['Start_estrus']+(6*data_CB1['5%_interval_sec']))
data_CB1['35%_max']=(data_CB1['Start_estrus']+(7*data_CB1['5%_interval_sec']))
data_CB1['40%_max']=(data_CB1['Start_estrus']+(8*data_CB1['5%_interval_sec']))
data_CB1['45%_max']=(data_CB1['Start_estrus']+(9*data_CB1['5%_interval_sec']))
data_CB1['50%_max']=(data_CB1['Start_estrus']+(10*data_CB1['5%_interval_sec']))
data_CB1['55%_max']=(data_CB1['Start_estrus']+(11*data_CB1['5%_interval_sec']))
data_CB1['60%_max']=(data_CB1['Start_estrus']+(12*data_CB1['5%_interval_sec']))
data_CB1['65%_max']=(data_CB1['Start_estrus']+(13*data_CB1['5%_interval_sec']))
data_CB1['70%_max']=(data_CB1['Start_estrus']+(14*data_CB1['5%_interval_sec']))
data_CB1['75%_max']=(data_CB1['Start_estrus']+(15*data_CB1['5%_interval_sec']))
data_CB1['80%_max']=(data_CB1['Start_estrus']+(16*data_CB1['5%_interval_sec']))
data_CB1['85%_max']=(data_CB1['Start_estrus']+(17*data_CB1['5%_interval_sec']))
data_CB1['90%_max']=(data_CB1['Start_estrus']+(18*data_CB1['5%_interval_sec']))
data_CB1['95%_max']=(data_CB1['Start_estrus']+(19*data_CB1['5%_interval_sec']))

data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['Start_estrus'])&(data_CB1[TIME]<data_CB1['5%_max'])),5,np.NaN)
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['5%_max'])&(data_CB1[TIME]<data_CB1['10%_max'])),10,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['10%_max'])&(data_CB1[TIME]<data_CB1['15%_max'])),15,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['15%_max'])&(data_CB1[TIME]<data_CB1['20%_max'])),20,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['20%_max'])&(data_CB1[TIME]<data_CB1['25%_max'])),25,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['25%_max'])&(data_CB1[TIME]<data_CB1['30%_max'])),30,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['30%_max'])&(data_CB1[TIME]<data_CB1['35%_max'])),35,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['35%_max'])&(data_CB1[TIME]<data_CB1['40%_max'])),40,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['40%_max'])&(data_CB1[TIME]<data_CB1['45%_max'])),45,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['45%_max'])&(data_CB1[TIME]<data_CB1['50%_max'])),50,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['50%_max'])&(data_CB1[TIME]<data_CB1['55%_max'])),55,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['55%_max'])&(data_CB1[TIME]<data_CB1['60%_max'])),60,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['60%_max'])&(data_CB1[TIME]<data_CB1['65%_max'])),65,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['65%_max'])&(data_CB1[TIME]<data_CB1['70%_max'])),70,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['70%_max'])&(data_CB1[TIME]<data_CB1['75%_max'])),75,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['75%_max'])&(data_CB1[TIME]<data_CB1['80%_max'])),80,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['80%_max'])&(data_CB1[TIME]<data_CB1['85%_max'])),85,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['85%_max'])&(data_CB1[TIME]<data_CB1['90%_max'])),90,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['90%_max'])&(data_CB1[TIME]<data_CB1['95%_max'])),95,data_CB1['interval'])
data_CB1['interval']=np.where(((data_CB1[TIME]>data_CB1['95%_max'])&(data_CB1[TIME]<data_CB1['End_estrus'])),100,data_CB1['interval'])

# mark the last behaviors before a new interval
data_CB1['interval_check']=np.where((data_CB1['interval']>1),1,np.NaN)
data_CB1['interval_check']=np.where(((data_CB1['interval']!=data_CB1['interval'].shift(-1))&(data_CB1['interval_check']==1)&(data_CB1[BEH]!=BSB)),1,np.NaN)
data_CB1['interval_check']=np.where(((data_CB1['interval_check']==1) & (data_CB1['interval']==100)),np.NaN,data_CB1['interval_check'])

# determine the amount of second left within the interval
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==5)),(data_CB1['5%_max']-data_CB1[TIME]),np.NaN)
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==10)),(data_CB1['10%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==15)),(data_CB1['15%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==20)),(data_CB1['20%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==25)),(data_CB1['25%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==30)),(data_CB1['30%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==35)),(data_CB1['35%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==40)),(data_CB1['40%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==45)),(data_CB1['45%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==50)),(data_CB1['50%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==55)),(data_CB1['55%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==60)),(data_CB1['60%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==65)),(data_CB1['65%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==70)),(data_CB1['70%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==75)),(data_CB1['75%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==80)),(data_CB1['80%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==85)),(data_CB1['85%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==90)),(data_CB1['90%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])
data_CB1['behavior_duration_checkleft']=np.where(((data_CB1['interval_check']==1)&(data_CB1['interval']==95)),(data_CB1['95%_max']-data_CB1[TIME]),data_CB1['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB1['behavior_duration_fixtonext']=data_CB1['durations']-data_CB1['behavior_duration_checkleft']
data_CB1['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB1['interval_fix']=np.where(data_CB1['interval_check']==1,(data_CB1['interval']+5),np.NaN)
data_CB1['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB1['behavior_fix']=np.where(data_CB1['interval_check']==1,data_CB1[BEH],np.NaN)
data_CB1['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB1['ratID_beh_int'] = data_CB1['interval'].map(str) + data_CB1['ratID_beh']

# Create unique code per behavior per rat per location
data_CB1['ratID_beh_int_loc'] = data_CB1[MODLOC].map(str) + data_CB1['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB1['ratID_beh_int_sex'] = data_CB1['ratID_beh_int'].map(str) + data_CB1[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB1['ratID_beh_int_treat'] = data_CB1['ratID_beh_int'].map(str) + data_CB1[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB1['ratID_beh_int_loc_treat'] = data_CB1['ratID_beh_int_loc'].map(str) + data_CB1[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB1['ratID_beh_int_modsub'] = data_CB1[MODSUB].map(str)+data_CB1['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB1['obs_beh_int_num'] = data_CB1.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_loc_num'] = data_CB1.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_sex_num'] = data_CB1.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_treat_num'] = data_CB1.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_loc_treat_num'] = data_CB1.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_modsub_num'] = data_CB1.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB1 = data_CB1.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB1['obs_beh_int_num_back'] = data_CB1.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_loc_num_back'] = data_CB1.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_sex_num_back'] = data_CB1.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_treat_num_back'] = data_CB1.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_loc_treat_num_back'] = data_CB1.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB1['obs_beh_int_modsub_num_back'] = data_CB1.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB1 = data_CB1.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB1['durations']=np.where(data_CB1['interval_check']==1, data_CB1['behavior_duration_checkleft'],data_CB1['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB1['durations']=np.where(((data_CB1['interval']==data_CB1['interval_fix'])&(data_CB1['behavior_fix']==data_CB1[BEH])&
        (data_CB1['obs_beh_int_num']==1)),(data_CB1['durations']+data_CB1['behavior_duration_fixtonext']),data_CB1['durations'])

# Sum up the durations on occurance
data_CB1['obs_beh_int_sumdur']=data_CB1.groupby('ratID_beh_int')['durations'].cumsum()
data_CB1['obs_beh_int_loc_sumdur']=data_CB1.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB1['obs_beh_int_treat_sumdur']=data_CB1.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB1['obs_beh_int_sex_sumdur']=data_CB1.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB1['obs_beh_int_loc_treat_sumdur']=data_CB1.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB1['obs_beh_int_modsub_sumdur']=data_CB1.groupby('ratID_beh_int_modsub')['durations'].cumsum()

# Calculate how long a 5% time interval is seconds
data_CB2['5%_interval_sec']=(data_CB2['Duration_estrus_min']/20*60)
data_CB2['5%_interval_min']=(data_CB2['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB2['5%_max']=(data_CB2['Start_estrus']+data_CB2['5%_interval_sec'])
data_CB2['10%_max']=(data_CB2['Start_estrus']+(2*data_CB2['5%_interval_sec']))
data_CB2['15%_max']=(data_CB2['Start_estrus']+(3*data_CB2['5%_interval_sec']))
data_CB2['20%_max']=(data_CB2['Start_estrus']+(4*data_CB2['5%_interval_sec']))
data_CB2['25%_max']=(data_CB2['Start_estrus']+(5*data_CB2['5%_interval_sec']))
data_CB2['30%_max']=(data_CB2['Start_estrus']+(6*data_CB2['5%_interval_sec']))
data_CB2['35%_max']=(data_CB2['Start_estrus']+(7*data_CB2['5%_interval_sec']))
data_CB2['40%_max']=(data_CB2['Start_estrus']+(8*data_CB2['5%_interval_sec']))
data_CB2['45%_max']=(data_CB2['Start_estrus']+(9*data_CB2['5%_interval_sec']))
data_CB2['50%_max']=(data_CB2['Start_estrus']+(10*data_CB2['5%_interval_sec']))
data_CB2['55%_max']=(data_CB2['Start_estrus']+(11*data_CB2['5%_interval_sec']))
data_CB2['60%_max']=(data_CB2['Start_estrus']+(12*data_CB2['5%_interval_sec']))
data_CB2['65%_max']=(data_CB2['Start_estrus']+(13*data_CB2['5%_interval_sec']))
data_CB2['70%_max']=(data_CB2['Start_estrus']+(14*data_CB2['5%_interval_sec']))
data_CB2['75%_max']=(data_CB2['Start_estrus']+(15*data_CB2['5%_interval_sec']))
data_CB2['80%_max']=(data_CB2['Start_estrus']+(16*data_CB2['5%_interval_sec']))
data_CB2['85%_max']=(data_CB2['Start_estrus']+(17*data_CB2['5%_interval_sec']))
data_CB2['90%_max']=(data_CB2['Start_estrus']+(18*data_CB2['5%_interval_sec']))
data_CB2['95%_max']=(data_CB2['Start_estrus']+(19*data_CB2['5%_interval_sec']))

data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['Start_estrus'])&(data_CB2[TIME]<data_CB2['5%_max'])),5,np.NaN)
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['5%_max'])&(data_CB2[TIME]<data_CB2['10%_max'])),10,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['10%_max'])&(data_CB2[TIME]<data_CB2['15%_max'])),15,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['15%_max'])&(data_CB2[TIME]<data_CB2['20%_max'])),20,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['20%_max'])&(data_CB2[TIME]<data_CB2['25%_max'])),25,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['25%_max'])&(data_CB2[TIME]<data_CB2['30%_max'])),30,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['30%_max'])&(data_CB2[TIME]<data_CB2['35%_max'])),35,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['35%_max'])&(data_CB2[TIME]<data_CB2['40%_max'])),40,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['40%_max'])&(data_CB2[TIME]<data_CB2['45%_max'])),45,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['45%_max'])&(data_CB2[TIME]<data_CB2['50%_max'])),50,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['50%_max'])&(data_CB2[TIME]<data_CB2['55%_max'])),55,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['55%_max'])&(data_CB2[TIME]<data_CB2['60%_max'])),60,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['60%_max'])&(data_CB2[TIME]<data_CB2['65%_max'])),65,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['65%_max'])&(data_CB2[TIME]<data_CB2['70%_max'])),70,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['70%_max'])&(data_CB2[TIME]<data_CB2['75%_max'])),75,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['75%_max'])&(data_CB2[TIME]<data_CB2['80%_max'])),80,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['80%_max'])&(data_CB2[TIME]<data_CB2['85%_max'])),85,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['85%_max'])&(data_CB2[TIME]<data_CB2['90%_max'])),90,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['90%_max'])&(data_CB2[TIME]<data_CB2['95%_max'])),95,data_CB2['interval'])
data_CB2['interval']=np.where(((data_CB2[TIME]>data_CB2['95%_max'])&(data_CB2[TIME]<data_CB2['End_estrus'])),100,data_CB2['interval'])

# mark the last behaviors before a new interval
data_CB2['interval_check']=np.where((data_CB2['interval']>1),1,np.NaN)
data_CB2['interval_check']=np.where(((data_CB2['interval']!=data_CB2['interval'].shift(-1))&(data_CB2['interval_check']==1)&(data_CB2[BEH]!=BSB)),1,np.NaN)
data_CB2['interval_check']=np.where(((data_CB2['interval_check']==1) & (data_CB2['interval']==100)),np.NaN,data_CB2['interval_check'])

# determine the amount of second left within the interval
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==5)),(data_CB2['5%_max']-data_CB2[TIME]),np.NaN)
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==10)),(data_CB2['10%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==15)),(data_CB2['15%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==20)),(data_CB2['20%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==25)),(data_CB2['25%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==30)),(data_CB2['30%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==35)),(data_CB2['35%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==40)),(data_CB2['40%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==45)),(data_CB2['45%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==50)),(data_CB2['50%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==55)),(data_CB2['55%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==60)),(data_CB2['60%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==65)),(data_CB2['65%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==70)),(data_CB2['70%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==75)),(data_CB2['75%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==80)),(data_CB2['80%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==85)),(data_CB2['85%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==90)),(data_CB2['90%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])
data_CB2['behavior_duration_checkleft']=np.where(((data_CB2['interval_check']==1)&(data_CB2['interval']==95)),(data_CB2['95%_max']-data_CB2[TIME]),data_CB2['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB2['behavior_duration_fixtonext']=data_CB2['durations']-data_CB2['behavior_duration_checkleft']
data_CB2['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB2['interval_fix']=np.where(data_CB2['interval_check']==1,(data_CB2['interval']+5),np.NaN)
data_CB2['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB2['behavior_fix']=np.where(data_CB2['interval_check']==1,data_CB2[BEH],np.NaN)
data_CB2['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB2['ratID_beh_int'] = data_CB2['interval'].map(str) + data_CB2['ratID_beh']

# Create unique code per behavior per rat per location
data_CB2['ratID_beh_int_loc'] = data_CB2[MODLOC].map(str) + data_CB2['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB2['ratID_beh_int_sex'] = data_CB2['ratID_beh_int'].map(str) + data_CB2[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB2['ratID_beh_int_treat'] = data_CB2['ratID_beh_int'].map(str) + data_CB2[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB2['ratID_beh_int_loc_treat'] = data_CB2['ratID_beh_int_loc'].map(str) + data_CB2[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB2['ratID_beh_int_modsub'] = data_CB2[MODSUB].map(str)+data_CB2['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB2['obs_beh_int_num'] = data_CB2.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_loc_num'] = data_CB2.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_sex_num'] = data_CB2.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_treat_num'] = data_CB2.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_loc_treat_num'] = data_CB2.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_modsub_num'] = data_CB2.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB2 = data_CB2.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB2['obs_beh_int_num_back'] = data_CB2.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_loc_num_back'] = data_CB2.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_sex_num_back'] = data_CB2.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_treat_num_back'] = data_CB2.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_loc_treat_num_back'] = data_CB2.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB2['obs_beh_int_modsub_num_back'] = data_CB2.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB2 = data_CB2.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB2['durations']=np.where(data_CB2['interval_check']==1, data_CB2['behavior_duration_checkleft'],data_CB2['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB2['durations']=np.where(((data_CB2['interval']==data_CB2['interval_fix'])&(data_CB2['behavior_fix']==data_CB2[BEH])&
        (data_CB2['obs_beh_int_num']==1)),(data_CB2['durations']+data_CB2['behavior_duration_fixtonext']),data_CB2['durations'])

# Sum up the durations on occurance
data_CB2['obs_beh_int_sumdur']=data_CB2.groupby('ratID_beh_int')['durations'].cumsum()
data_CB2['obs_beh_int_loc_sumdur']=data_CB2.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB2['obs_beh_int_treat_sumdur']=data_CB2.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB2['obs_beh_int_sex_sumdur']=data_CB2.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB2['obs_beh_int_loc_treat_sumdur']=data_CB2.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB2['obs_beh_int_modsub_sumdur']=data_CB2.groupby('ratID_beh_int_modsub')['durations'].cumsum()

# Calculate how long a 5% time interval is seconds
data_CB3['5%_interval_sec']=(data_CB3['Duration_estrus_min']/20*60)
data_CB3['5%_interval_min']=(data_CB3['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB3['5%_max']=(data_CB3['Start_estrus']+data_CB3['5%_interval_sec'])
data_CB3['10%_max']=(data_CB3['Start_estrus']+(2*data_CB3['5%_interval_sec']))
data_CB3['15%_max']=(data_CB3['Start_estrus']+(3*data_CB3['5%_interval_sec']))
data_CB3['20%_max']=(data_CB3['Start_estrus']+(4*data_CB3['5%_interval_sec']))
data_CB3['25%_max']=(data_CB3['Start_estrus']+(5*data_CB3['5%_interval_sec']))
data_CB3['30%_max']=(data_CB3['Start_estrus']+(6*data_CB3['5%_interval_sec']))
data_CB3['35%_max']=(data_CB3['Start_estrus']+(7*data_CB3['5%_interval_sec']))
data_CB3['40%_max']=(data_CB3['Start_estrus']+(8*data_CB3['5%_interval_sec']))
data_CB3['45%_max']=(data_CB3['Start_estrus']+(9*data_CB3['5%_interval_sec']))
data_CB3['50%_max']=(data_CB3['Start_estrus']+(10*data_CB3['5%_interval_sec']))
data_CB3['55%_max']=(data_CB3['Start_estrus']+(11*data_CB3['5%_interval_sec']))
data_CB3['60%_max']=(data_CB3['Start_estrus']+(12*data_CB3['5%_interval_sec']))
data_CB3['65%_max']=(data_CB3['Start_estrus']+(13*data_CB3['5%_interval_sec']))
data_CB3['70%_max']=(data_CB3['Start_estrus']+(14*data_CB3['5%_interval_sec']))
data_CB3['75%_max']=(data_CB3['Start_estrus']+(15*data_CB3['5%_interval_sec']))
data_CB3['80%_max']=(data_CB3['Start_estrus']+(16*data_CB3['5%_interval_sec']))
data_CB3['85%_max']=(data_CB3['Start_estrus']+(17*data_CB3['5%_interval_sec']))
data_CB3['90%_max']=(data_CB3['Start_estrus']+(18*data_CB3['5%_interval_sec']))
data_CB3['95%_max']=(data_CB3['Start_estrus']+(19*data_CB3['5%_interval_sec']))

data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['Start_estrus'])&(data_CB3[TIME]<data_CB3['5%_max'])),5,np.NaN)
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['5%_max'])&(data_CB3[TIME]<data_CB3['10%_max'])),10,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['10%_max'])&(data_CB3[TIME]<data_CB3['15%_max'])),15,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['15%_max'])&(data_CB3[TIME]<data_CB3['20%_max'])),20,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['20%_max'])&(data_CB3[TIME]<data_CB3['25%_max'])),25,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['25%_max'])&(data_CB3[TIME]<data_CB3['30%_max'])),30,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['30%_max'])&(data_CB3[TIME]<data_CB3['35%_max'])),35,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['35%_max'])&(data_CB3[TIME]<data_CB3['40%_max'])),40,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['40%_max'])&(data_CB3[TIME]<data_CB3['45%_max'])),45,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['45%_max'])&(data_CB3[TIME]<data_CB3['50%_max'])),50,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['50%_max'])&(data_CB3[TIME]<data_CB3['55%_max'])),55,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['55%_max'])&(data_CB3[TIME]<data_CB3['60%_max'])),60,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['60%_max'])&(data_CB3[TIME]<data_CB3['65%_max'])),65,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['65%_max'])&(data_CB3[TIME]<data_CB3['70%_max'])),70,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['70%_max'])&(data_CB3[TIME]<data_CB3['75%_max'])),75,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['75%_max'])&(data_CB3[TIME]<data_CB3['80%_max'])),80,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['80%_max'])&(data_CB3[TIME]<data_CB3['85%_max'])),85,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['85%_max'])&(data_CB3[TIME]<data_CB3['90%_max'])),90,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['90%_max'])&(data_CB3[TIME]<data_CB3['95%_max'])),95,data_CB3['interval'])
data_CB3['interval']=np.where(((data_CB3[TIME]>data_CB3['95%_max'])&(data_CB3[TIME]<data_CB3['End_estrus'])),100,data_CB3['interval'])

# mark the last behaviors before a new interval
data_CB3['interval_check']=np.where((data_CB3['interval']>1),1,np.NaN)
data_CB3['interval_check']=np.where(((data_CB3['interval']!=data_CB3['interval'].shift(-1))&(data_CB3['interval_check']==1)&(data_CB3[BEH]!=BSB)),1,np.NaN)
data_CB3['interval_check']=np.where(((data_CB3['interval_check']==1) & (data_CB3['interval']==100)),np.NaN,data_CB3['interval_check'])

# determine the amount of second left within the interval
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==5)),(data_CB3['5%_max']-data_CB3[TIME]),np.NaN)
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==10)),(data_CB3['10%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==15)),(data_CB3['15%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==20)),(data_CB3['20%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==25)),(data_CB3['25%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==30)),(data_CB3['30%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==35)),(data_CB3['35%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==40)),(data_CB3['40%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==45)),(data_CB3['45%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==50)),(data_CB3['50%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==55)),(data_CB3['55%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==60)),(data_CB3['60%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==65)),(data_CB3['65%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==70)),(data_CB3['70%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==75)),(data_CB3['75%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==80)),(data_CB3['80%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==85)),(data_CB3['85%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==90)),(data_CB3['90%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])
data_CB3['behavior_duration_checkleft']=np.where(((data_CB3['interval_check']==1)&(data_CB3['interval']==95)),(data_CB3['95%_max']-data_CB3[TIME]),data_CB3['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB3['behavior_duration_fixtonext']=data_CB3['durations']-data_CB3['behavior_duration_checkleft']
data_CB3['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB3['interval_fix']=np.where(data_CB3['interval_check']==1,(data_CB3['interval']+5),np.NaN)
data_CB3['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB3['behavior_fix']=np.where(data_CB3['interval_check']==1,data_CB3[BEH],np.NaN)
data_CB3['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB3['ratID_beh_int'] = data_CB3['interval'].map(str) + data_CB3['ratID_beh']

# Create unique code per behavior per rat per location
data_CB3['ratID_beh_int_loc'] = data_CB3[MODLOC].map(str) + data_CB3['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB3['ratID_beh_int_sex'] = data_CB3['ratID_beh_int'].map(str) + data_CB3[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB3['ratID_beh_int_treat'] = data_CB3['ratID_beh_int'].map(str) + data_CB3[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB3['ratID_beh_int_loc_treat'] = data_CB3['ratID_beh_int_loc'].map(str) + data_CB3[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB3['ratID_beh_int_modsub'] = data_CB3[MODSUB].map(str)+data_CB3['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB3['obs_beh_int_num'] = data_CB3.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_loc_num'] = data_CB3.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_sex_num'] = data_CB3.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_treat_num'] = data_CB3.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_loc_treat_num'] = data_CB3.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_modsub_num'] = data_CB3.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB3 = data_CB3.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB3['obs_beh_int_num_back'] = data_CB3.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_loc_num_back'] = data_CB3.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_sex_num_back'] = data_CB3.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_treat_num_back'] = data_CB3.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_loc_treat_num_back'] = data_CB3.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB3['obs_beh_int_modsub_num_back'] = data_CB3.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB3 = data_CB3.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB3['durations']=np.where(data_CB3['interval_check']==1, data_CB3['behavior_duration_checkleft'],data_CB3['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB3['durations']=np.where(((data_CB3['interval']==data_CB3['interval_fix'])&(data_CB3['behavior_fix']==data_CB3[BEH])&
        (data_CB3['obs_beh_int_num']==1)),(data_CB3['durations']+data_CB3['behavior_duration_fixtonext']),data_CB3['durations'])

# Sum up the durations on occurance
data_CB3['obs_beh_int_sumdur']=data_CB3.groupby('ratID_beh_int')['durations'].cumsum()
data_CB3['obs_beh_int_loc_sumdur']=data_CB3.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB3['obs_beh_int_treat_sumdur']=data_CB3.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB3['obs_beh_int_sex_sumdur']=data_CB3.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB3['obs_beh_int_loc_treat_sumdur']=data_CB3.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB3['obs_beh_int_modsub_sumdur']=data_CB3.groupby('ratID_beh_int_modsub')['durations'].cumsum()

# Calculate how long a 5% time interval is seconds
data_CB4['5%_interval_sec']=(data_CB4['Duration_estrus_min']/20*60)
data_CB4['5%_interval_min']=(data_CB4['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB4['5%_max']=(data_CB4['Start_estrus']+data_CB4['5%_interval_sec'])
data_CB4['10%_max']=(data_CB4['Start_estrus']+(2*data_CB4['5%_interval_sec']))
data_CB4['15%_max']=(data_CB4['Start_estrus']+(3*data_CB4['5%_interval_sec']))
data_CB4['20%_max']=(data_CB4['Start_estrus']+(4*data_CB4['5%_interval_sec']))
data_CB4['25%_max']=(data_CB4['Start_estrus']+(5*data_CB4['5%_interval_sec']))
data_CB4['30%_max']=(data_CB4['Start_estrus']+(6*data_CB4['5%_interval_sec']))
data_CB4['35%_max']=(data_CB4['Start_estrus']+(7*data_CB4['5%_interval_sec']))
data_CB4['40%_max']=(data_CB4['Start_estrus']+(8*data_CB4['5%_interval_sec']))
data_CB4['45%_max']=(data_CB4['Start_estrus']+(9*data_CB4['5%_interval_sec']))
data_CB4['50%_max']=(data_CB4['Start_estrus']+(10*data_CB4['5%_interval_sec']))
data_CB4['55%_max']=(data_CB4['Start_estrus']+(11*data_CB4['5%_interval_sec']))
data_CB4['60%_max']=(data_CB4['Start_estrus']+(12*data_CB4['5%_interval_sec']))
data_CB4['65%_max']=(data_CB4['Start_estrus']+(13*data_CB4['5%_interval_sec']))
data_CB4['70%_max']=(data_CB4['Start_estrus']+(14*data_CB4['5%_interval_sec']))
data_CB4['75%_max']=(data_CB4['Start_estrus']+(15*data_CB4['5%_interval_sec']))
data_CB4['80%_max']=(data_CB4['Start_estrus']+(16*data_CB4['5%_interval_sec']))
data_CB4['85%_max']=(data_CB4['Start_estrus']+(17*data_CB4['5%_interval_sec']))
data_CB4['90%_max']=(data_CB4['Start_estrus']+(18*data_CB4['5%_interval_sec']))
data_CB4['95%_max']=(data_CB4['Start_estrus']+(19*data_CB4['5%_interval_sec']))

data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['Start_estrus'])&(data_CB4[TIME]<data_CB4['5%_max'])),5,np.NaN)
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['5%_max'])&(data_CB4[TIME]<data_CB4['10%_max'])),10,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['10%_max'])&(data_CB4[TIME]<data_CB4['15%_max'])),15,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['15%_max'])&(data_CB4[TIME]<data_CB4['20%_max'])),20,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['20%_max'])&(data_CB4[TIME]<data_CB4['25%_max'])),25,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['25%_max'])&(data_CB4[TIME]<data_CB4['30%_max'])),30,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['30%_max'])&(data_CB4[TIME]<data_CB4['35%_max'])),35,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['35%_max'])&(data_CB4[TIME]<data_CB4['40%_max'])),40,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['40%_max'])&(data_CB4[TIME]<data_CB4['45%_max'])),45,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['45%_max'])&(data_CB4[TIME]<data_CB4['50%_max'])),50,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['50%_max'])&(data_CB4[TIME]<data_CB4['55%_max'])),55,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['55%_max'])&(data_CB4[TIME]<data_CB4['60%_max'])),60,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['60%_max'])&(data_CB4[TIME]<data_CB4['65%_max'])),65,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['65%_max'])&(data_CB4[TIME]<data_CB4['70%_max'])),70,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['70%_max'])&(data_CB4[TIME]<data_CB4['75%_max'])),75,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['75%_max'])&(data_CB4[TIME]<data_CB4['80%_max'])),80,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['80%_max'])&(data_CB4[TIME]<data_CB4['85%_max'])),85,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['85%_max'])&(data_CB4[TIME]<data_CB4['90%_max'])),90,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['90%_max'])&(data_CB4[TIME]<data_CB4['95%_max'])),95,data_CB4['interval'])
data_CB4['interval']=np.where(((data_CB4[TIME]>data_CB4['95%_max'])&(data_CB4[TIME]<data_CB4['End_estrus'])),100,data_CB4['interval'])

# mark the last behaviors before a new interval
data_CB4['interval_check']=np.where((data_CB4['interval']>1),1,np.NaN)
data_CB4['interval_check']=np.where(((data_CB4['interval']!=data_CB4['interval'].shift(-1))&(data_CB4['interval_check']==1)&(data_CB4[BEH]!=BSB)),1,np.NaN)
data_CB4['interval_check']=np.where(((data_CB4['interval_check']==1) & (data_CB4['interval']==100)),np.NaN,data_CB4['interval_check'])

# determine the amount of second left within the interval
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==5)),(data_CB4['5%_max']-data_CB4[TIME]),np.NaN)
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==10)),(data_CB4['10%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==15)),(data_CB4['15%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==20)),(data_CB4['20%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==25)),(data_CB4['25%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==30)),(data_CB4['30%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==35)),(data_CB4['35%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==40)),(data_CB4['40%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==45)),(data_CB4['45%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==50)),(data_CB4['50%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==55)),(data_CB4['55%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==60)),(data_CB4['60%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==65)),(data_CB4['65%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==70)),(data_CB4['70%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==75)),(data_CB4['75%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==80)),(data_CB4['80%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==85)),(data_CB4['85%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==90)),(data_CB4['90%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])
data_CB4['behavior_duration_checkleft']=np.where(((data_CB4['interval_check']==1)&(data_CB4['interval']==95)),(data_CB4['95%_max']-data_CB4[TIME]),data_CB4['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB4['behavior_duration_fixtonext']=data_CB4['durations']-data_CB4['behavior_duration_checkleft']
data_CB4['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB4['interval_fix']=np.where(data_CB4['interval_check']==1,(data_CB4['interval']+5),np.NaN)
data_CB4['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB4['behavior_fix']=np.where(data_CB4['interval_check']==1,data_CB4[BEH],np.NaN)
data_CB4['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB4['ratID_beh_int'] = data_CB4['interval'].map(str) + data_CB4['ratID_beh']

# Create unique code per behavior per rat per location
data_CB4['ratID_beh_int_loc'] = data_CB4[MODLOC].map(str) + data_CB4['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB4['ratID_beh_int_sex'] = data_CB4['ratID_beh_int'].map(str) + data_CB4[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB4['ratID_beh_int_treat'] = data_CB4['ratID_beh_int'].map(str) + data_CB4[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB4['ratID_beh_int_loc_treat'] = data_CB4['ratID_beh_int_loc'].map(str) + data_CB4[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB4['ratID_beh_int_modsub'] = data_CB4[MODSUB].map(str)+data_CB4['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB4['obs_beh_int_num'] = data_CB4.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_loc_num'] = data_CB4.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_sex_num'] = data_CB4.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_treat_num'] = data_CB4.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_loc_treat_num'] = data_CB4.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_modsub_num'] = data_CB4.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB4 = data_CB4.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB4['obs_beh_int_num_back'] = data_CB4.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_loc_num_back'] = data_CB4.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_sex_num_back'] = data_CB4.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_treat_num_back'] = data_CB4.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_loc_treat_num_back'] = data_CB4.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB4['obs_beh_int_modsub_num_back'] = data_CB4.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB4 = data_CB4.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB4['durations']=np.where(data_CB4['interval_check']==1, data_CB4['behavior_duration_checkleft'],data_CB4['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB4['durations']=np.where(((data_CB4['interval']==data_CB4['interval_fix'])&(data_CB4['behavior_fix']==data_CB4[BEH])&
        (data_CB4['obs_beh_int_num']==1)),(data_CB4['durations']+data_CB4['behavior_duration_fixtonext']),data_CB4['durations'])

# Sum up the durations on occurance
data_CB4['obs_beh_int_sumdur']=data_CB4.groupby('ratID_beh_int')['durations'].cumsum()
data_CB4['obs_beh_int_loc_sumdur']=data_CB4.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB4['obs_beh_int_treat_sumdur']=data_CB4.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB4['obs_beh_int_sex_sumdur']=data_CB4.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB4['obs_beh_int_loc_treat_sumdur']=data_CB4.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB4['obs_beh_int_modsub_sumdur']=data_CB4.groupby('ratID_beh_int_modsub')['durations'].cumsum()

# Calculate how long a 5% time interval is seconds
data_CB5['5%_interval_sec']=(data_CB5['Duration_estrus_min']/20*60)
data_CB5['5%_interval_min']=(data_CB5['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB5['5%_max']=(data_CB5['Start_estrus']+data_CB5['5%_interval_sec'])
data_CB5['10%_max']=(data_CB5['Start_estrus']+(2*data_CB5['5%_interval_sec']))
data_CB5['15%_max']=(data_CB5['Start_estrus']+(3*data_CB5['5%_interval_sec']))
data_CB5['20%_max']=(data_CB5['Start_estrus']+(4*data_CB5['5%_interval_sec']))
data_CB5['25%_max']=(data_CB5['Start_estrus']+(5*data_CB5['5%_interval_sec']))
data_CB5['30%_max']=(data_CB5['Start_estrus']+(6*data_CB5['5%_interval_sec']))
data_CB5['35%_max']=(data_CB5['Start_estrus']+(7*data_CB5['5%_interval_sec']))
data_CB5['40%_max']=(data_CB5['Start_estrus']+(8*data_CB5['5%_interval_sec']))
data_CB5['45%_max']=(data_CB5['Start_estrus']+(9*data_CB5['5%_interval_sec']))
data_CB5['50%_max']=(data_CB5['Start_estrus']+(10*data_CB5['5%_interval_sec']))
data_CB5['55%_max']=(data_CB5['Start_estrus']+(11*data_CB5['5%_interval_sec']))
data_CB5['60%_max']=(data_CB5['Start_estrus']+(12*data_CB5['5%_interval_sec']))
data_CB5['65%_max']=(data_CB5['Start_estrus']+(13*data_CB5['5%_interval_sec']))
data_CB5['70%_max']=(data_CB5['Start_estrus']+(14*data_CB5['5%_interval_sec']))
data_CB5['75%_max']=(data_CB5['Start_estrus']+(15*data_CB5['5%_interval_sec']))
data_CB5['80%_max']=(data_CB5['Start_estrus']+(16*data_CB5['5%_interval_sec']))
data_CB5['85%_max']=(data_CB5['Start_estrus']+(17*data_CB5['5%_interval_sec']))
data_CB5['90%_max']=(data_CB5['Start_estrus']+(18*data_CB5['5%_interval_sec']))
data_CB5['95%_max']=(data_CB5['Start_estrus']+(19*data_CB5['5%_interval_sec']))

data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['Start_estrus'])&(data_CB5[TIME]<data_CB5['5%_max'])),5,np.NaN)
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['5%_max'])&(data_CB5[TIME]<data_CB5['10%_max'])),10,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['10%_max'])&(data_CB5[TIME]<data_CB5['15%_max'])),15,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['15%_max'])&(data_CB5[TIME]<data_CB5['20%_max'])),20,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['20%_max'])&(data_CB5[TIME]<data_CB5['25%_max'])),25,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['25%_max'])&(data_CB5[TIME]<data_CB5['30%_max'])),30,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['30%_max'])&(data_CB5[TIME]<data_CB5['35%_max'])),35,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['35%_max'])&(data_CB5[TIME]<data_CB5['40%_max'])),40,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['40%_max'])&(data_CB5[TIME]<data_CB5['45%_max'])),45,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['45%_max'])&(data_CB5[TIME]<data_CB5['50%_max'])),50,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['50%_max'])&(data_CB5[TIME]<data_CB5['55%_max'])),55,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['55%_max'])&(data_CB5[TIME]<data_CB5['60%_max'])),60,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['60%_max'])&(data_CB5[TIME]<data_CB5['65%_max'])),65,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['65%_max'])&(data_CB5[TIME]<data_CB5['70%_max'])),70,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['70%_max'])&(data_CB5[TIME]<data_CB5['75%_max'])),75,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['75%_max'])&(data_CB5[TIME]<data_CB5['80%_max'])),80,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['80%_max'])&(data_CB5[TIME]<data_CB5['85%_max'])),85,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['85%_max'])&(data_CB5[TIME]<data_CB5['90%_max'])),90,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['90%_max'])&(data_CB5[TIME]<data_CB5['95%_max'])),95,data_CB5['interval'])
data_CB5['interval']=np.where(((data_CB5[TIME]>data_CB5['95%_max'])&(data_CB5[TIME]<data_CB5['End_estrus'])),100,data_CB5['interval'])

# mark the last behaviors before a new interval
data_CB5['interval_check']=np.where((data_CB5['interval']>1),1,np.NaN)
data_CB5['interval_check']=np.where(((data_CB5['interval']!=data_CB5['interval'].shift(-1))&(data_CB5['interval_check']==1)&(data_CB5[BEH]!=BSB)),1,np.NaN)
data_CB5['interval_check']=np.where(((data_CB5['interval_check']==1) & (data_CB5['interval']==100)),np.NaN,data_CB5['interval_check'])

# determine the amount of second left within the interval
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==5)),(data_CB5['5%_max']-data_CB5[TIME]),np.NaN)
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==10)),(data_CB5['10%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==15)),(data_CB5['15%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==20)),(data_CB5['20%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==25)),(data_CB5['25%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==30)),(data_CB5['30%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==35)),(data_CB5['35%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==40)),(data_CB5['40%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==45)),(data_CB5['45%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==50)),(data_CB5['50%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==55)),(data_CB5['55%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==60)),(data_CB5['60%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==65)),(data_CB5['65%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==70)),(data_CB5['70%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==75)),(data_CB5['75%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==80)),(data_CB5['80%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==85)),(data_CB5['85%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==90)),(data_CB5['90%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])
data_CB5['behavior_duration_checkleft']=np.where(((data_CB5['interval_check']==1)&(data_CB5['interval']==95)),(data_CB5['95%_max']-data_CB5[TIME]),data_CB5['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB5['behavior_duration_fixtonext']=data_CB5['durations']-data_CB5['behavior_duration_checkleft']
data_CB5['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB5['interval_fix']=np.where(data_CB5['interval_check']==1,(data_CB5['interval']+5),np.NaN)
data_CB5['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB5['behavior_fix']=np.where(data_CB5['interval_check']==1,data_CB5[BEH],np.NaN)
data_CB5['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB5['ratID_beh_int'] = data_CB5['interval'].map(str) + data_CB5['ratID_beh']

# Create unique code per behavior per rat per location
data_CB5['ratID_beh_int_loc'] = data_CB5[MODLOC].map(str) + data_CB5['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB5['ratID_beh_int_sex'] = data_CB5['ratID_beh_int'].map(str) + data_CB5[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB5['ratID_beh_int_treat'] = data_CB5['ratID_beh_int'].map(str) + data_CB5[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB5['ratID_beh_int_loc_treat'] = data_CB5['ratID_beh_int_loc'].map(str) + data_CB5[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB5['ratID_beh_int_modsub'] = data_CB5[MODSUB].map(str)+data_CB5['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB5['obs_beh_int_num'] = data_CB5.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_loc_num'] = data_CB5.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_sex_num'] = data_CB5.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_treat_num'] = data_CB5.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_loc_treat_num'] = data_CB5.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_modsub_num'] = data_CB5.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB5 = data_CB5.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB5['obs_beh_int_num_back'] = data_CB5.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_loc_num_back'] = data_CB5.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_sex_num_back'] = data_CB5.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_treat_num_back'] = data_CB5.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_loc_treat_num_back'] = data_CB5.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB5['obs_beh_int_modsub_num_back'] = data_CB5.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB5 = data_CB5.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB5['durations']=np.where(data_CB5['interval_check']==1, data_CB5['behavior_duration_checkleft'],data_CB5['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB5['durations']=np.where(((data_CB5['interval']==data_CB5['interval_fix'])&(data_CB5['behavior_fix']==data_CB5[BEH])&
        (data_CB5['obs_beh_int_num']==1)),(data_CB5['durations']+data_CB5['behavior_duration_fixtonext']),data_CB5['durations'])

# Sum up the durations on occurance
data_CB5['obs_beh_int_sumdur']=data_CB5.groupby('ratID_beh_int')['durations'].cumsum()
data_CB5['obs_beh_int_loc_sumdur']=data_CB5.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB5['obs_beh_int_treat_sumdur']=data_CB5.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB5['obs_beh_int_sex_sumdur']=data_CB5.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB5['obs_beh_int_loc_treat_sumdur']=data_CB5.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB5['obs_beh_int_modsub_sumdur']=data_CB5.groupby('ratID_beh_int_modsub')['durations'].cumsum()

# Calculate how long a 5% time interval is seconds
data_CB6['5%_interval_sec']=(data_CB6['Duration_estrus_min']/20*60)
data_CB6['5%_interval_min']=(data_CB6['Duration_estrus_min']/20)

# Calculate the cummulative 5% interval end per rat
data_CB6['5%_max']=(data_CB6['Start_estrus']+data_CB6['5%_interval_sec'])
data_CB6['10%_max']=(data_CB6['Start_estrus']+(2*data_CB6['5%_interval_sec']))
data_CB6['15%_max']=(data_CB6['Start_estrus']+(3*data_CB6['5%_interval_sec']))
data_CB6['20%_max']=(data_CB6['Start_estrus']+(4*data_CB6['5%_interval_sec']))
data_CB6['25%_max']=(data_CB6['Start_estrus']+(5*data_CB6['5%_interval_sec']))
data_CB6['30%_max']=(data_CB6['Start_estrus']+(6*data_CB6['5%_interval_sec']))
data_CB6['35%_max']=(data_CB6['Start_estrus']+(7*data_CB6['5%_interval_sec']))
data_CB6['40%_max']=(data_CB6['Start_estrus']+(8*data_CB6['5%_interval_sec']))
data_CB6['45%_max']=(data_CB6['Start_estrus']+(9*data_CB6['5%_interval_sec']))
data_CB6['50%_max']=(data_CB6['Start_estrus']+(10*data_CB6['5%_interval_sec']))
data_CB6['55%_max']=(data_CB6['Start_estrus']+(11*data_CB6['5%_interval_sec']))
data_CB6['60%_max']=(data_CB6['Start_estrus']+(12*data_CB6['5%_interval_sec']))
data_CB6['65%_max']=(data_CB6['Start_estrus']+(13*data_CB6['5%_interval_sec']))
data_CB6['70%_max']=(data_CB6['Start_estrus']+(14*data_CB6['5%_interval_sec']))
data_CB6['75%_max']=(data_CB6['Start_estrus']+(15*data_CB6['5%_interval_sec']))
data_CB6['80%_max']=(data_CB6['Start_estrus']+(16*data_CB6['5%_interval_sec']))
data_CB6['85%_max']=(data_CB6['Start_estrus']+(17*data_CB6['5%_interval_sec']))
data_CB6['90%_max']=(data_CB6['Start_estrus']+(18*data_CB6['5%_interval_sec']))
data_CB6['95%_max']=(data_CB6['Start_estrus']+(19*data_CB6['5%_interval_sec']))

data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['Start_estrus'])&(data_CB6[TIME]<data_CB6['5%_max'])),5,np.NaN)
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['5%_max'])&(data_CB6[TIME]<data_CB6['10%_max'])),10,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['10%_max'])&(data_CB6[TIME]<data_CB6['15%_max'])),15,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['15%_max'])&(data_CB6[TIME]<data_CB6['20%_max'])),20,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['20%_max'])&(data_CB6[TIME]<data_CB6['25%_max'])),25,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['25%_max'])&(data_CB6[TIME]<data_CB6['30%_max'])),30,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['30%_max'])&(data_CB6[TIME]<data_CB6['35%_max'])),35,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['35%_max'])&(data_CB6[TIME]<data_CB6['40%_max'])),40,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['40%_max'])&(data_CB6[TIME]<data_CB6['45%_max'])),45,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['45%_max'])&(data_CB6[TIME]<data_CB6['50%_max'])),50,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['50%_max'])&(data_CB6[TIME]<data_CB6['55%_max'])),55,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['55%_max'])&(data_CB6[TIME]<data_CB6['60%_max'])),60,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['60%_max'])&(data_CB6[TIME]<data_CB6['65%_max'])),65,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['65%_max'])&(data_CB6[TIME]<data_CB6['70%_max'])),70,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['70%_max'])&(data_CB6[TIME]<data_CB6['75%_max'])),75,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['75%_max'])&(data_CB6[TIME]<data_CB6['80%_max'])),80,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['80%_max'])&(data_CB6[TIME]<data_CB6['85%_max'])),85,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['85%_max'])&(data_CB6[TIME]<data_CB6['90%_max'])),90,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['90%_max'])&(data_CB6[TIME]<data_CB6['95%_max'])),95,data_CB6['interval'])
data_CB6['interval']=np.where(((data_CB6[TIME]>data_CB6['95%_max'])&(data_CB6[TIME]<data_CB6['End_estrus'])),100,data_CB6['interval'])

# mark the last behaviors before a new interval
data_CB6['interval_check']=np.where((data_CB6['interval']>1),1,np.NaN)
data_CB6['interval_check']=np.where(((data_CB6['interval']!=data_CB6['interval'].shift(-1))&(data_CB6['interval_check']==1)&(data_CB6[BEH]!=BSB)),1,np.NaN)
data_CB6['interval_check']=np.where(((data_CB6['interval_check']==1) & (data_CB6['interval']==100)),np.NaN,data_CB6['interval_check'])

# determine the amount of second left within the interval
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==5)),(data_CB6['5%_max']-data_CB6[TIME]),np.NaN)
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==10)),(data_CB6['10%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==15)),(data_CB6['15%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==20)),(data_CB6['20%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==25)),(data_CB6['25%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==30)),(data_CB6['30%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==35)),(data_CB6['35%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==40)),(data_CB6['40%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==45)),(data_CB6['45%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==50)),(data_CB6['50%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==55)),(data_CB6['55%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==60)),(data_CB6['60%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==65)),(data_CB6['65%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==70)),(data_CB6['70%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==75)),(data_CB6['75%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==80)),(data_CB6['80%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==85)),(data_CB6['85%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==90)),(data_CB6['90%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])
data_CB6['behavior_duration_checkleft']=np.where(((data_CB6['interval_check']==1)&(data_CB6['interval']==95)),(data_CB6['95%_max']-data_CB6[TIME]),data_CB6['behavior_duration_checkleft'])

# determine the amount of seconds that actually takes place in the next interval
data_CB6['behavior_duration_fixtonext']=data_CB6['durations']-data_CB6['behavior_duration_checkleft']
data_CB6['behavior_duration_fixtonext'].fillna(method = "ffill", inplace=True)

# create a column that places the behaviors in the right interval, which can be added later
data_CB6['interval_fix']=np.where(data_CB6['interval_check']==1,(data_CB6['interval']+5),np.NaN)
data_CB6['interval_fix'].fillna(method = "ffill", inplace=True)

# create a column with the behavior that needs to be changed
data_CB6['behavior_fix']=np.where(data_CB6['interval_check']==1,data_CB6[BEH],np.NaN)
data_CB6['behavior_fix'].fillna(method = "ffill", inplace=True)

# Create unique code per behavior per rat per interval
data_CB6['ratID_beh_int'] = data_CB6['interval'].map(str) + data_CB6['ratID_beh']

# Create unique code per behavior per rat per location
data_CB6['ratID_beh_int_loc'] = data_CB6[MODLOC].map(str) + data_CB6['ratID_beh_int']

# Create unique code per behavior per rat per interval per modifier sex
data_CB6['ratID_beh_int_sex'] = data_CB6['ratID_beh_int'].map(str) + data_CB6[MODSEX]

# Create unique code per behavior per rat per interval per modifier treatment group
data_CB6['ratID_beh_int_treat'] = data_CB6['ratID_beh_int'].map(str) + data_CB6[MODTREAT]

# Create unique code per behavior per rat per treatment group
data_CB6['ratID_beh_int_loc_treat'] = data_CB6['ratID_beh_int_loc'].map(str) + data_CB6[MODTREAT]

# Create unique code per behavior per rat per ModID
data_CB6['ratID_beh_int_modsub'] = data_CB6[MODSUB].map(str)+data_CB6['ratID_beh_int'] 

# Number the behaviors on occurance
data_CB6['obs_beh_int_num'] = data_CB6.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_loc_num'] = data_CB6.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_sex_num'] = data_CB6.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_treat_num'] = data_CB6.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_loc_treat_num'] = data_CB6.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_modsub_num'] = data_CB6.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

# Number the behaviors backwards and end per rat
data_CB6 = data_CB6.sort_values(by=['ratID_beh','Time'], ascending = False)
data_CB6['obs_beh_int_num_back'] = data_CB6.groupby('ratID_beh_int')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_loc_num_back'] = data_CB6.groupby('ratID_beh_int_loc')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_sex_num_back'] = data_CB6.groupby('ratID_beh_int_sex')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_treat_num_back'] = data_CB6.groupby('ratID_beh_int_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_loc_treat_num_back'] = data_CB6.groupby('ratID_beh_int_loc_treat')[BEH].transform(lambda x: np.arange(1, len(x) + 1))
data_CB6['obs_beh_int_modsub_num_back'] = data_CB6.groupby('ratID_beh_int_modsub')[BEH].transform(lambda x: np.arange(1, len(x) + 1))

data_CB6 = data_CB6.sort_values(by=['RatID','Time'])

# Correct the duration of the last behavior that needs fixing
data_CB6['durations']=np.where(data_CB6['interval_check']==1, data_CB6['behavior_duration_checkleft'],data_CB6['durations'])

# Correct the duration of the first behavior that needs to be fixed in the next timeslot
data_CB6['durations']=np.where(((data_CB6['interval']==data_CB6['interval_fix'])&(data_CB6['behavior_fix']==data_CB6[BEH])&
        (data_CB6['obs_beh_int_num']==1)),(data_CB6['durations']+data_CB6['behavior_duration_fixtonext']),data_CB6['durations'])

# Sum up the durations on occurance
data_CB6['obs_beh_int_sumdur']=data_CB6.groupby('ratID_beh_int')['durations'].cumsum()
data_CB6['obs_beh_int_loc_sumdur']=data_CB6.groupby('ratID_beh_int_loc')['durations'].cumsum()
data_CB6['obs_beh_int_treat_sumdur']=data_CB6.groupby('ratID_beh_int_treat')['durations'].cumsum()
data_CB6['obs_beh_int_sex_sumdur']=data_CB6.groupby('ratID_beh_int_sex')['durations'].cumsum()
data_CB6['obs_beh_int_loc_treat_sumdur']=data_CB6.groupby('ratID_beh_int_loc_treat')['durations'].cumsum()
data_CB6['obs_beh_int_modsub_sumdur']=data_CB6.groupby('ratID_beh_int_modsub')['durations'].cumsum()
  
# Just to get notification this part is finished
print("intervals finished")
 
# Loop the rest over the dataframes
df_CB=[data_all,data_CB1,data_CB2,data_CB3,data_CB4,data_CB5,data_CB6]

for dt, dataframe in enumerate(df_CB): 
    data=dataframe
    
    # Calculate total number of each behavior per rat in total environment
    for position, col_name in enumerate(list_behaviors):

        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):

            data['%d_TN_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TN_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TN_%s'% (perc, col_name)]) 
            data['%d_TN_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_num']==1)&(data['interval']==perc)), data['obs_beh_int_num_back'], 
                data['%d_TN_%s'% (perc, col_name)]) 
            data['%d_TN_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TN_%s'% (perc, col_name)]=np.where(data['%d_TN_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TN_%s'% (perc, col_name)])
            data['%d_TN_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TN_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TN_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TN_%s'% (perc, col_name)])
            data['%d_TN_%s'% (perc, col_name)]=np.where(data['%d_TN_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TN_%s'% (perc, col_name)])
            data['%d_TN_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TN_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TN_%s'% (perc, col_name)])
        
                
            # Calculate total number of each behavior per rat in burrow
            data['%d_BN_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_BN_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_BN_%s'% (perc, col_name)]) 
            data['%d_BN_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_loc_num']==1)&(data[MODLOC]=='Burrow')&(data['interval']==perc)), 
                data['obs_beh_int_loc_num_back'], data['%d_BN_%s'% (perc, col_name)]) 
            data['%d_BN_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_BN_%s'% (perc, col_name)]=np.where(data['%d_BN_%s'% (perc, col_name)]==99999, np.NaN, data['%d_BN_%s'% (perc, col_name)])
            data['%d_BN_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_BN_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_BN_%s'% (perc, col_name)]==88888)), 
                0,data['%d_BN_%s'% (perc, col_name)])
            data['%d_BN_%s'% (perc, col_name)]=np.where(data['%d_BN_%s'% (perc, col_name)]==88888, np.NaN, data['%d_BN_%s'% (perc, col_name)])
            data['%d_BN_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_BN_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_BN_%s'% (perc, col_name)])
        
            # Calculate total number of each behavior per rat in burrow
            data['%d_ON_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_ON_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_ON_%s'% (perc, col_name)]) 
            data['%d_ON_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_loc_num']==1)&(data[MODLOC]=='Open field')&(data['interval']==perc)), 
                data['obs_beh_int_loc_num_back'], data['%d_ON_%s'% (perc, col_name)]) 
            data['%d_ON_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_ON_%s'% (perc, col_name)]=np.where(data['%d_ON_%s'% (perc, col_name)]==99999, np.NaN, data['%d_ON_%s'% (perc, col_name)])
            data['%d_ON_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_ON_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_ON_%s'% (perc, col_name)]==88888)), 
                0,data['%d_ON_%s'% (perc, col_name)])
            data['%d_ON_%s'% (perc, col_name)]=np.where(data['%d_ON_%s'% (perc, col_name)]==88888, np.NaN, data['%d_ON_%s'% (perc, col_name)])
            data['%d_ON_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_ON_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_ON_%s'% (perc, col_name)])

           
    # Calculate total number of each behavior per rat in total environment for each interval
    for rank, perc in enumerate(list_intervals):
     
        # Calculate the additional behaviors for total environment, burrow, and open field    
        data['%d_TN_%s'% (perc, EA)]= (data['%d_TN_%s'% (perc, BSD)]+data['%d_TN_%s'% (perc, BSE)]+data['%d_TN_%s'% (perc, BSF)])
        data['%d_TN_%s'% (perc, EB)]= (data['%d_TN_%s'% (perc, BSB)]/data['%d_TN_%s'% (perc, EA)]*100)
        data['%d_TN_%s'% (perc, EC)]= (data['%d_TN_%s'% (perc, BSG)]+data['%d_TN_%s'% (perc, BSH)]+data['%d_TN_%s'% (perc, BSI)])
        data['%d_TN_%s'% (perc, EE)]= (data['%d_TN_%s'% (perc, BCA)]+data['%d_TN_%s'% (perc, BCB)]+data['%d_TN_%s'% (perc, BCC)]+data['%d_TN_%s'% (perc, BCD)])
        data['%d_TN_%s'% (perc, EF)]= (data['%d_TN_%s'% (perc, BSA)]+data['%d_TN_%s'% (perc, BSB)])
        data['%d_TN_%s'% (perc, EG)]= (data['%d_TN_%s'% (perc, EF)]/data['%d_TN_%s'% (perc, EA)]*100)
        
        data['%d_ON_%s'% (perc, EA)]= (data['%d_ON_%s'% (perc, BSD)]+data['%d_ON_%s'% (perc, BSE)]+data['%d_ON_%s'% (perc, BSF)])
        data['%d_ON_%s'% (perc, EB)]= (data['%d_ON_%s'% (perc, BSB)]/data['%d_ON_%s'% (perc, EA)]*100)
        data['%d_ON_%s'% (perc, EC)]= (data['%d_ON_%s'% (perc, BSG)]+data['%d_ON_%s'% (perc, BSH)]+data['%d_ON_%s'% (perc, BSI)])
        data['%d_ON_%s'% (perc, EE)]= (data['%d_ON_%s'% (perc, BCA)]+data['%d_ON_%s'% (perc, BCB)]+data['%d_ON_%s'% (perc, BCC)]+data['%d_ON_%s'% (perc, BCD)])
        data['%d_ON_%s'% (perc, EF)]= (data['%d_ON_%s'% (perc, BSA)]+data['%d_ON_%s'% (perc, BSB)])
        data['%d_ON_%s'% (perc, EG)]= (data['%d_ON_%s'% (perc, EF)]/data['%d_ON_%s'% (perc, EA)]*100)
        
        data['%d_BN_%s'% (perc, EA)]= (data['%d_BN_%s'% (perc, BSD)]+data['%d_BN_%s'% (perc, BSE)]+data['%d_BN_%s'% (perc, BSF)])
        data['%d_BN_%s'% (perc, EB)]= (data['%d_BN_%s'% (perc, BSB)]/data['%d_BN_%s'% (perc, EA)]*100)
        data['%d_BN_%s'% (perc, EC)]= (data['%d_BN_%s'% (perc, BSG)]+data['%d_BN_%s'% (perc, BSH)]+data['%d_BN_%s'% (perc, BSI)])
        data['%d_BN_%s'% (perc, EE)]= (data['%d_BN_%s'% (perc, BCA)]+data['%d_BN_%s'% (perc, BCB)]+data['%d_BN_%s'% (perc, BCC)]+data['%d_BN_%s'% (perc, BCD)])
        data['%d_BN_%s'% (perc, EF)]= (data['%d_BN_%s'% (perc, BSA)]+data['%d_BN_%s'% (perc, BSB)])
        data['%d_BN_%s'% (perc, EG)]= (data['%d_BN_%s'% (perc, EF)]/data['%d_BN_%s'% (perc, EA)]*100)
    
    # Calculate the number of behaviors corrected for time behavioral estrus
    for position, col_name in enumerate(list_behaviors):
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):

            data['%d_TN_min_%s'% (perc, col_name)]=(data['%d_TN_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_BN_min_%s'% (perc, col_name)]=(data['%d_BN_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_ON_min_%s'% (perc, col_name)]=(data['%d_ON_%s'% (perc, col_name)]/data['5%_interval_min'])
            
            data['%d_TN_min_%s'% (perc, col_name)]=np.where((data['%d_TN_min_%s'% (perc, col_name)]>0),data['%d_TN_min_%s'% (perc, col_name)],0)
            data['%d_BN_min_%s'% (perc, col_name)]=np.where((data['%d_BN_min_%s'% (perc, col_name)]>0),data['%d_BN_min_%s'% (perc, col_name)],0)
            data['%d_ON_min_%s'% (perc, col_name)]=np.where((data['%d_ON_min_%s'% (perc, col_name)]>0),data['%d_ON_min_%s'% (perc, col_name)],0)
        
    for position, col_name in enumerate(list_behaviors_extra):
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TN_min_%s'% (perc, col_name)]=(data['%d_TN_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_BN_min_%s'% (perc, col_name)]=(data['%d_BN_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_ON_min_%s'% (perc, col_name)]=(data['%d_ON_%s'% (perc, col_name)]/data['5%_interval_min'])
        
            data['%d_TN_min_%s'% (perc, col_name)]=np.where((data['%d_TN_min_%s'% (perc, col_name)]>0),data['%d_TN_min_%s'% (perc, col_name)],0)
            data['%d_BN_min_%s'% (perc, col_name)]=np.where((data['%d_BN_min_%s'% (perc, col_name)]>0),data['%d_BN_min_%s'% (perc, col_name)],0)
            data['%d_ON_min_%s'% (perc, col_name)]=np.where((data['%d_ON_min_%s'% (perc, col_name)]>0),data['%d_ON_min_%s'% (perc, col_name)],0)
        
    # Calculate total duration of each behavior per rat in total environment
    for position, col_name in enumerate(list_behaviors): 
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TD_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TD_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TD_%s'% (perc, col_name)]) 
            data['%d_TD_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_num_back']==1)&(data['interval']==perc)), data['obs_beh_int_sumdur'], 
                data['%d_TD_%s'% (perc, col_name)]) 
            data['%d_TD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TD_%s'% (perc, col_name)]=np.where(data['%d_TD_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TD_%s'% (perc, col_name)])
            data['%d_TD_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TD_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TD_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TD_%s'% (perc, col_name)])
            data['%d_TD_%s'% (perc, col_name)]=np.where(data['%d_TD_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TD_%s'% (perc, col_name)])
            data['%d_TD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TD_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TD_%s'% (perc, col_name)])
        
            # Calculate total duration of each behavior per rat in burrow
            data['%d_BD_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_BD_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_BD_%s'% (perc, col_name)]) 
            data['%d_BD_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_loc_num_back']==1)&(data[MODLOC]=='Burrow')&(data['interval']==perc)), data['obs_beh_int_loc_sumdur'], 
                data['%d_BD_%s'% (perc, col_name)]) 
            data['%d_BD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_BD_%s'% (perc, col_name)]=np.where(data['%d_BD_%s'% (perc, col_name)]==99999, np.NaN, data['%d_BD_%s'% (perc, col_name)])
            data['%d_BD_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_BD_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_BD_%s'% (perc, col_name)]==88888)), 
                0,data['%d_BD_%s'% (perc, col_name)])
            data['%d_BD_%s'% (perc, col_name)]=np.where(data['%d_BD_%s'% (perc, col_name)]==88888, np.NaN, data['%d_BD_%s'% (perc, col_name)])
            data['%d_BD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_BD_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_BD_%s'% (perc, col_name)])
        
            # Calculate total duration of each behavior per rat in open field
            data['%d_OD_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_OD_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_OD_%s'% (perc, col_name)]) 
            data['%d_OD_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_loc_num_back']==1)&(data[MODLOC]=='Open field')&(data['interval']==perc)), data['obs_beh_int_loc_sumdur'], 
                data['%d_OD_%s'% (perc, col_name)]) 
            data['%d_OD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_OD_%s'% (perc, col_name)]=np.where(data['%d_OD_%s'% (perc, col_name)]==99999, np.NaN, data['%d_OD_%s'% (perc, col_name)])
            data['%d_OD_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_OD_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_OD_%s'% (perc, col_name)]==88888)), 
                0,data['%d_OD_%s'% (perc, col_name)])
            data['%d_OD_%s'% (perc, col_name)]=np.where(data['%d_OD_%s'% (perc, col_name)]==88888, np.NaN, data['%d_OD_%s'% (perc, col_name)])
            data['%d_OD_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_OD_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_OD_%s'% (perc, col_name)])

    # Calculate total number of each behavior per rat in total environment for each interval
    for rank, perc in enumerate(list_intervals):
        
        # Calculate the other behaviors
        data['%d_TD_%s'% (perc, EA)]= (data['%d_TD_%s'% (perc, BSD)]+data['%d_TD_%s'% (perc, BSE)]+data['%d_TD_%s'% (perc, BSF)])
        data['%d_TD_%s'% (perc, EB)]= (data['%d_TD_%s'% (perc, BSB)]/data['%d_TD_%s'% (perc, EA)]*100)
        data['%d_TD_%s'% (perc, EC)]= (data['%d_TD_%s'% (perc, BSG)]+data['%d_TD_%s'% (perc, BSH)]+data['%d_TD_%s'% (perc, BSI)])
        data['%d_TD_%s'% (perc, EE)]= (data['%d_TD_%s'% (perc, BCA)]+data['%d_TD_%s'% (perc, BCB)]+data['%d_TD_%s'% (perc, BCC)]+data['%d_TD_%s'% (perc, BCD)])
        data['%d_TD_%s'% (perc, EF)]= (data['%d_TD_%s'% (perc, BSA)]+data['%d_TD_%s'% (perc, BSB)])
        data['%d_TD_%s'% (perc, EG)]= (data['%d_TD_%s'% (perc, EF)]/data['%d_TD_%s'% (perc, EA)]*100)
        
        data['%d_OD_%s'% (perc, EA)]= (data['%d_OD_%s'% (perc, BSD)]+data['%d_OD_%s'% (perc, BSE)]+data['%d_OD_%s'% (perc, BSF)])
        data['%d_OD_%s'% (perc, EB)]= (data['%d_OD_%s'% (perc, BSB)]/data['%d_OD_%s'% (perc, EA)]*100)
        data['%d_OD_%s'% (perc, EC)]= (data['%d_OD_%s'% (perc, BSG)]+data['%d_OD_%s'% (perc, BSH)]+data['%d_OD_%s'% (perc, BSI)])
        data['%d_OD_%s'% (perc, EE)]= (data['%d_OD_%s'% (perc, BCA)]+data['%d_OD_%s'% (perc, BCB)]+data['%d_OD_%s'% (perc, BCC)]+data['%d_OD_%s'% (perc, BCD)])
        data['%d_OD_%s'% (perc, EF)]= (data['%d_OD_%s'% (perc, BSA)]+data['%d_OD_%s'% (perc, BSB)])
        data['%d_OD_%s'% (perc, EG)]= (data['%d_OD_%s'% (perc, EF)]/data['%d_OD_%s'% (perc, EA)]*100)
        
        data['%d_BD_%s'% (perc, EA)]= (data['%d_BD_%s'% (perc, BSD)]+data['%d_BD_%s'% (perc, BSE)]+data['%d_BD_%s'% (perc, BSF)])
        data['%d_BD_%s'% (perc, EB)]= (data['%d_BD_%s'% (perc, BSB)]/data['%d_BD_%s'% (perc, EA)]*100)
        data['%d_BD_%s'% (perc, EC)]= (data['%d_BD_%s'% (perc, BSG)]+data['%d_BD_%s'% (perc, BSH)]+data['%d_BD_%s'% (perc, BSI)])
        data['%d_BD_%s'% (perc, EE)]= (data['%d_BD_%s'% (perc, BCA)]+data['%d_BD_%s'% (perc, BCB)]+data['%d_BD_%s'% (perc, BCC)]+data['%d_BD_%s'% (perc, BCD)])
        data['%d_BD_%s'% (perc, EF)]= (data['%d_BD_%s'% (perc, BSA)]+data['%d_BD_%s'% (perc, BSB)])
        data['%d_BD_%s'% (perc, EG)]= (data['%d_BD_%s'% (perc, EF)]/data['%d_BD_%s'% (perc, EA)]*100)
        
    # Calculate the durations of behaviors corrected for time behavioral estrus
    for position, col_name in enumerate(list_behaviors): 
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TD_min_%s'% (perc, col_name)]=(data['%d_TD_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_BD_min_%s'% (perc, col_name)]=(data['%d_BD_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_OD_min_%s'% (perc, col_name)]=(data['%d_OD_%s'% (perc, col_name)]/data['5%_interval_min'])
        
            data['%d_TD_min_%s'% (perc, col_name)]=np.where((data['%d_TD_min_%s'% (perc, col_name)]>0),data['%d_TD_min_%s'% (perc, col_name)],0)
            data['%d_BD_min_%s'% (perc, col_name)]=np.where((data['%d_BD_min_%s'% (perc, col_name)]>0),data['%d_BD_min_%s'% (perc, col_name)],0)
            data['%d_OD_min_%s'% (perc, col_name)]=np.where((data['%d_OD_min_%s'% (perc, col_name)]>0),data['%d_OD_min_%s'% (perc, col_name)],0)
        
    for position, col_name in enumerate(list_behaviors_extra): 
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TD_min_%s'% (perc, col_name)]=(data['%d_TD_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_BD_min_%s'% (perc, col_name)]=(data['%d_BD_%s'% (perc, col_name)]/data['5%_interval_min'])
            data['%d_OD_min_%s'% (perc, col_name)]=(data['%d_OD_%s'% (perc, col_name)]/data['5%_interval_min'])
        
            data['%d_TD_min_%s'% (perc, col_name)]=np.where((data['%d_TD_min_%s'% (perc, col_name)]>0),data['%d_TD_min_%s'% (perc, col_name)],0)
            data['%d_BD_min_%s'% (perc, col_name)]=np.where((data['%d_BD_min_%s'% (perc, col_name)]>0),data['%d_BD_min_%s'% (perc, col_name)],0)
            data['%d_OD_min_%s'% (perc, col_name)]=np.where((data['%d_OD_min_%s'% (perc, col_name)]>0),data['%d_OD_min_%s'% (perc, col_name)],0)
        
    # Calculate total number of each behavior per rat in total environment for each interval
    for rank, perc in enumerate(list_intervals):
        
        # Calculate time spent in open field versus burrow area
        data['%d_Time_OA']=(data['%d_OD_%s'% (perc, BA)]+data['%d_OD_%s'% (perc, BB)]+data['%d_OD_%s'% (perc, BSA)]+data['%d_OD_%s'% (perc, BSB)]+
            data['%d_OD_%s'% (perc, BSC)]+data['%d_OD_%s'% (perc, BSD)]+data['%d_OD_%s'% (perc, BSE)]+data['%d_OD_%s'% (perc, BSF)]+data['%d_OD_%s'% (perc, BSG)]+
            data['%d_OD_%s'% (perc, BSH)]+data['%d_OD_%s'% (perc, BSI)]+data['%d_OD_%s'% (perc, BSJ)]+data['%d_OD_%s'% (perc, BCA)]+data['%d_OD_%s'% (perc, BCB)]+
            data['%d_OD_%s'% (perc, BCC)]+data['%d_OD_%s'% (perc, BCD)])
        data['%d_Time_Burrow']=(data['%d_BD_%s'% (perc, BA)]+data['%d_BD_%s'% (perc, BB)]+data['%d_BD_%s'% (perc, BSA)]+data['%d_BD_%s'% (perc, BSB)]+
            data['%d_BD_%s'% (perc, BSC)]+data['%d_BD_%s'% (perc, BSD)]+data['%d_BD_%s'% (perc, BSE)]+data['%d_BD_%s'% (perc, BSF)]+data['%d_BD_%s'% (perc, BSG)]+
            data['%d_BD_%s'% (perc, BSH)]+data['%d_BD_%s'% (perc, BSI)]+data['%d_BD_%s'% (perc, BSJ)]+data['%d_BD_%s'% (perc, BCA)]+data['%d_BD_%s'% (perc, BCB)]+
            data['%d_BD_%s'% (perc, BCC)]+data['%d_BD_%s'% (perc, BCD)])
        
#### BLOCKED BECAUSE IT IS NOW FOR DATA JAN IN WHICH ONLY PREFERRED MALE IS IMPORTANT
#    # Calculate total number of each "social" behavior directed at each female in total environment
#    for position, col_name in enumerate(list_behaviors_social):
#        # Calculate total number of each behavior per rat in total environment for each interval
#        for rank, perc in enumerate(list_intervals):
#            data['%d_TNF1_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TNF1_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNF1_%s'% (perc, col_name)]) 
#            data['%d_TNF1_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Female 1')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_num_back'], data['%d_TNF1_%s'% (perc, col_name)]) 
#            data['%d_TNF1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TNF1_%s'% (perc, col_name)]=np.where(data['%d_TNF1_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNF1_%s'% (perc, col_name)])
#            data['%d_TNF1_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TNF1_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNF1_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TNF1_%s'% (perc, col_name)])
#            data['%d_TNF1_%s'% (perc, col_name)]=np.where(data['%d_TNF1_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNF1_%s'% (perc, col_name)])
#            data['%d_TNF1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TNF1_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNF1_%s'% (perc, col_name)])
#        
#            data['%d_TNF2_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TNF2_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNF2_%s'% (perc, col_name)]) 
#            data['%d_TNF2_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Female 2')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_num_back'], data['%d_TNF2_%s'% (perc, col_name)]) 
#            data['%d_TNF2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TNF2_%s'% (perc, col_name)]=np.where(data['%d_TNF2_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNF2_%s'% (perc, col_name)])
#            data['%d_TNF2_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TNF2_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNF2_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TNF2_%s'% (perc, col_name)])
#            data['%d_TNF2_%s'% (perc, col_name)]=np.where(data['%d_TNF2_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNF2_%s'% (perc, col_name)])
#            data['%d_TNF2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TNF2_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNF2_%s'% (perc, col_name)])
#        
#            data['%d_TNF3_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TNF3_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNF3_%s'% (perc, col_name)]) 
#            data['%d_TNF3_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Female 3')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_num_back'], data['%d_TNF3_%s'% (perc, col_name)]) 
#            data['%d_TNF3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TNF3_%s'% (perc, col_name)]=np.where(data['%d_TNF3_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNF3_%s'% (perc, col_name)])
#            data['%d_TNF3_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TNF3_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNF3_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TNF3_%s'% (perc, col_name)])
#            data['%d_TNF3_%s'% (perc, col_name)]=np.where(data['%d_TNF3_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNF3_%s'% (perc, col_name)])
#            data['%d_TNF3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TNF3_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNF3_%s'% (perc, col_name)])
#        
#            data['%d_TNF4_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TNF4_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNF4_%s'% (perc, col_name)]) 
#            data['%d_TNF4_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Female 4')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_num_back'], data['%d_TNF4_%s'% (perc, col_name)]) 
#            data['%d_TNF4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TNF4_%s'% (perc, col_name)]=np.where(data['%d_TNF4_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNF4_%s'% (perc, col_name)])
#            data['%d_TNF4_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TNF4_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNF4_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TNF4_%s'% (perc, col_name)])
#            data['%d_TNF4_%s'% (perc, col_name)]=np.where(data['%d_TNF4_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNF4_%s'% (perc, col_name)])
#            data['%d_TNF4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TNF4_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNF4_%s'% (perc, col_name)])
#        
#            # Calculate total duration of each "social" behavior directed at each female in total environment
#            data['%d_TDF1_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TDF1_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDF1_%s'% (perc, col_name)]) 
#            data['%d_TDF1_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Female 1')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_sumdur'], data['%d_TDF1_%s'% (perc, col_name)]) 
#            data['%d_TDF1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TDF1_%s'% (perc, col_name)]=np.where(data['%d_TDF1_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDF1_%s'% (perc, col_name)])
#            data['%d_TDF1_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TDF1_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDF1_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TDF1_%s'% (perc, col_name)])
#            data['%d_TDF1_%s'% (perc, col_name)]=np.where(data['%d_TDF1_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDF1_%s'% (perc, col_name)])
#            data['%d_TDF1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TDF1_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDF1_%s'% (perc, col_name)])
#        
#            data['%d_TDF2_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TDF2_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDF2_%s'% (perc, col_name)]) 
#            data['%d_TDF2_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Female 2')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_sumdur'], data['%d_TDF2_%s'% (perc, col_name)]) 
#            data['%d_TDF2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TDF2_%s'% (perc, col_name)]=np.where(data['%d_TDF2_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDF2_%s'% (perc, col_name)])
#            data['%d_TDF2_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TDF2_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDF2_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TDF2_%s'% (perc, col_name)])
#            data['%d_TDF2_%s'% (perc, col_name)]=np.where(data['%d_TDF2_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDF2_%s'% (perc, col_name)])
#            data['%d_TDF2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TDF2_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDF2_%s'% (perc, col_name)])
#        
#            data['%d_TDF3_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TDF3_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDF3_%s'% (perc, col_name)]) 
#            data['%d_TDF3_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Female 3')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_sumdur'], data['%d_TDF3_%s'% (perc, col_name)]) 
#            data['%d_TDF3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TDF3_%s'% (perc, col_name)]=np.where(data['%d_TDF3_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDF3_%s'% (perc, col_name)])
#            data['%d_TDF3_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TDF3_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDF3_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TDF3_%s'% (perc, col_name)])
#            data['%d_TDF3_%s'% (perc, col_name)]=np.where(data['%d_TDF3_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDF3_%s'% (perc, col_name)])
#            data['%d_TDF3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TDF3_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDF3_%s'% (perc, col_name)])
#        
#            data['%d_TDF4_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
#            data['%d_TDF4_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDF4_%s'% (perc, col_name)]) 
#            data['%d_TDF4_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Female 4')&(data['interval']==perc)), 
#                data['obs_beh_int_modsub_sumdur'], data['%d_TDF4_%s'% (perc, col_name)]) 
#            data['%d_TDF4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
#            data['%d_TDF4_%s'% (perc, col_name)]=np.where(data['%d_TDF4_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDF4_%s'% (perc, col_name)])
#            data['%d_TDF4_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
#            data['%d_TDF4_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDF4_%s'% (perc, col_name)]==88888)), 
#                0,data['%d_TDF4_%s'% (perc, col_name)])
#            data['%d_TDF4_%s'% (perc, col_name)]=np.where(data['%d_TDF4_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDF4_%s'% (perc, col_name)])
#            data['%d_TDF4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
#            data['%d_TDF4_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDF4_%s'% (perc, col_name)])
#
#    # Calculate total number of each behavior per rat in total environment for each interval
#    for rank, perc in enumerate(list_intervals):
#            
#        # Calculate with which female is copulated the most
#        data['%d_TNF1_%s'% (perc, EA)]= (data['%d_TNF1_%s'% (perc, BSD)]+data['%d_TNF1_%s'% (perc, BSE)]+data['%d_TNF1_%s'% (perc, BSF)])
#        data['%d_TNF2_%s'% (perc, EA)]= (data['%d_TNF2_%s'% (perc, BSD)]+data['%d_TNF2_%s'% (perc, BSE)]+data['%d_TNF2_%s'% (perc, BSF)])
#        data['%d_TNF3_%s'% (perc, EA)]= (data['%d_TNF3_%s'% (perc, BSD)]+data['%d_TNF3_%s'% (perc, BSE)]+data['%d_TNF3_%s'% (perc, BSF)])
#        data['%d_TNF4_%s'% (perc, EA)]= (data['%d_TNF4_%s'% (perc, BSD)]+data['%d_TNF4_%s'% (perc, BSE)]+data['%d_TNF4_%s'% (perc, BSF)])
#        
#        data['%d_preferred_female' % perc]=np.where((data['%d_TNF1_%s'% (perc, EA)]>data['%d_TNF2_%s'% (perc, EA)])&(data['%d_TNF1_%s'% (perc, EA)]>data['%d_TNF3_%s'% (perc, EA)])&
#            (data['%d_TNF1_%s'% (perc, EA)]>data['%d_TNF4_%s'% (perc, EA)]),"Female 1", "")
#        data['%d_preferred_female' % perc]=np.where((data['%d_TNF2_%s'% (perc, EA)]>data['%d_TNF1_%s'% (perc, EA)])&(data['%d_TNF2_%s'% (perc, EA)]>data['%d_TNF3_%s'% (perc, EA)])&
#            (data['%d_TNF2_%s'% (perc, EA)]>data['%d_TNF4_%s'% (perc, EA)]),"Female 2", data['%d_preferred_female' % perc])  
#        data['%d_preferred_female' % perc]=np.where((data['%d_TNF3_%s'% (perc, EA)]>data['%d_TNF1_%s'% (perc, EA)])&(data['%d_TNF3_%s'% (perc, EA)]>data['%d_TNF2_%s'% (perc, EA)])&
#            (data['%d_TNF3_%s'% (perc, EA)]>data['%d_TNF4_%s'% (perc, EA)]),"Female 3", data['%d_preferred_female' % perc])  
#        data['%d_preferred_female' % perc]=np.where((data['%d_TNF4_%s'% (perc, EA)]>data['%d_TNF1_%s'% (perc, EA)])&(data['%d_TNF4_%s'% (perc, EA)]>data['%d_TNF3_%s'% (perc, EA)])&
#            (data['%d_TNF4_%s'% (perc, EA)]>data['%d_TNF2_%s'% (perc, EA)]),"Female 4", data['%d_preferred_female' % perc])  
#        
#        # Calculate number of sexpartners
#        data['%d_femalepartner1'% perc]=np.where(data['%d_TNF1_%s'% (perc, EA)]==0,0,1)
#        data['%d_femalepartner2'% perc]=np.where(data['%d_TNF2_%s'% (perc, EA)]==0,0,1)
#        data['%d_femalepartner3'% perc]=np.where(data['%d_TNF3_%s'% (perc, EA)]==0,0,1)
#        data['%d_femalepartner4'% perc]=np.where(data['%d_TNF4_%s'% (perc, EA)]==0,0,1)
#        
#        data['%d_nr_femalepartners'% perc]=data['%d_femalepartner1'% perc]+data['%d_femalepartner2'% perc]+data['%d_femalepartner3'% perc]+data['%d_femalepartner4'% perc]
#        
#        data['%d_femalepartner1_mistake'% perc]=np.where(data['%d_TNF1_%s'% (perc, EA)]<5,0,1)
#        data['%d_femalepartner2_mistake'% perc]=np.where(data['%d_TNF2_%s'% (perc, EA)]<5,0,1)
#        data['%d_femalepartner3_mistake'% perc]=np.where(data['%d_TNF3_%s'% (perc, EA)]<5,0,1)
#        data['%d_femalepartner4_mistake'% perc]=np.where(data['%d_TNF4_%s'% (perc, EA)]<5,0,1)
#        
#        data['%d_nr_femalepartners_mistake'% perc]=(data['%d_femalepartner1_mistake'% perc]+data['%d_femalepartner2_mistake'% perc]+
#            data['%d_femalepartner3_mistake'% perc]+data['%d_femalepartner4_mistake'% perc])
#        
#        # Create column for the ratID for the preferred female
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_female' % perc]=='Female 1'),EF11, "")
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_female' % perc]=='Female 2'),EF12, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_female' % perc]=='Female 3'),EF13, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_female' % perc]=='Female 4'),EF14, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_female' % perc]=='Female 1'),EF21, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_female' % perc]=='Female 2'),EF22, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_female' % perc]=='Female 3'),EF23, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_female' % perc]=='Female 4'),EF24, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_female' % perc]=='Female 1'),EF31, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_female' % perc]=='Female 2'),EF32, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_female' % perc]=='Female 3'),EF33, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_female' % perc]=='Female 4'),EF34, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_female' % perc]=='Female 1'),EF41, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_female' % perc]=='Female 2'),EF42, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_female' % perc]=='Female 3'),EF43, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_female' % perc]=='Female 4'),EF44, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_female' % perc]=='Female 1'),EF51, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_female' % perc]=='Female 2'),EF52, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_female' % perc]=='Female 3'),EF53, data['%d_pref_fem_RatID' % perc])
#        data['%d_pref_fem_RatID' % perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_female' % perc]=='Female 4'),EF54, data['%d_pref_fem_RatID' % perc])
#        
#    # Number and durations of behaviors directed at the preferred copulation partner
#    for position, col_name in enumerate(list_behaviors_social): 
#        # Calculate total number of each behavior per rat in total environment for each interval
#        for rank, perc in enumerate(list_intervals):
#            data['%d_TN_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 2', data['%d_TNF2_%s'% (perc, col_name)],
#                data['%d_TN_pref_fem_%s'% (perc, col_name)]) 
#            data['%d_TN_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 3', data['%d_TNF3_%s'% (perc, col_name)],
#                data['%d_TN_pref_fem_%s'%  (perc, col_name)]) 
#            data['%d_TN_pref_fem_%s'%  (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 4', data['%d_TNF4_%s'% (perc, col_name)],
#                data['%d_TN_pref_fem_%s'%  (perc, col_name)])     
#            
#            data['%d_TN_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 1',((data['%d_TNF2_%s'% (perc, col_name)]+ 
#                data['%d_TNF3_%s'% (perc, col_name)]+ data['%d_TNF4_%s'% (perc, col_name)])/3),np.NaN)
#            data['%d_TN_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 2',((data['%d_TNF1_%s'% (perc, col_name)]+ 
#                data['%d_TNF3_%s'% (perc, col_name)]+ data['%d_TNF4_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_fem_%s'% (perc, col_name)])    
#            data['%d_TN_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 3',((data['%d_TNF1_%s'% (perc, col_name)]+ 
#                    data['%d_TDF2_%s'% (perc, col_name)]+ data['%d_TNF4_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_fem_%s'% (perc, col_name)])
#            data['%d_TN_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 4',((data['%d_TNF1_%s'% (perc, col_name)]+ 
#                data['%d_TNF3_%s'% (perc, col_name)]+ data['%d_TNF2_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_fem_%s'% (perc, col_name)]) 
#                 
#            data['%d_TD_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 1', data['%d_TDF1_%s'% (perc, col_name)],np.NaN)
#            data['%d_TD_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 2', data['%d_TDF2_%s'% (perc, col_name)],
#                data['%d_TD_pref_fem_%s'% (perc, col_name)]) 
#            data['%d_TD_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 3', data['%d_TDF3_%s'% (perc, col_name)],
#                data['%d_TD_pref_fem_%s'% (perc, col_name)]) 
#            data['%d_TD_pref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 4', data['%d_TDF4_%s'% (perc, col_name)],
#                data['%d_TD_pref_fem_%s'% (perc, col_name)])     
#            
#            data['%d_TD_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 1',((data['%d_TDF2_%s'% (perc, col_name)]+ 
#                data['%d_TDF3_%s'% (perc, col_name)]+ data['%d_TDF4_%s'% (perc, col_name)])/3),np.NaN)
#            data['%d_TD_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 2',((data['%d_TDF1_%s'% (perc, col_name)]+ 
#                data['%d_TDF3_%s'% (perc, col_name)]+ data['%d_TDF4_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_fem_%s'% (perc, col_name)])    
#            data['%d_TD_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 3',((data['%d_TDF1_%s'% (perc, col_name)]+ 
#                    data['%d_TDF2_%s'% (perc, col_name)]+ data['%d_TDF4_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_fem_%s'% (perc, col_name)])
#            data['%d_TD_nonpref_fem_%s'% (perc, col_name)]=np.where(data['%d_preferred_female' % perc]=='Female 4',((data['%d_TDF1_%s'% (perc, col_name)]+ 
#                data['%d_TDF3_%s'% (perc, col_name)]+ data['%d_TDF2_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_fem_%s'% (perc, col_name)]) 
#        
#    for position, col_name in enumerate(list_behaviors_social): 
#        # Calculate total number of each behavior per rat in total environment for each interval
#        for rank, perc in enumerate(list_intervals):
#            data['%d_TN_nonprefmale_%s'% (perc, col_name)]=(data['%d_TNM_%s'% (perc, col_name)]/4) # This is to compare preferred female and other females to contact with males
#            data['%d_TD_nonprefmale_%s'% (perc, col_name)]=(data['%d_TDM_%s'% (perc, col_name)]/4)
#
#    # Calculate total number of each behavior per rat in total environment for each interval
#    for rank, perc in enumerate(list_intervals):
#        
#        data['%d_TN_pref_fem_%s'% (perc, EC)]= (data['%d_TN_pref_fem_%s'% (perc, BSG)]+data['%d_TN_pref_fem_%s'% (perc, BSH)]+data['%d_TN_pref_fem_%s'% (perc, BSI)])
#        data['%d_TN_pref_fem_%s'% (perc, EE)]= (data['%d_TN_pref_fem_%s'% (perc, BCA)]+data['%d_TN_pref_fem_%s'% (perc, BCB)]+data['%d_TN_pref_fem_%s'% (perc, BCC)]+
#            data['%d_TN_pref_fem_%s'% (perc, BCD)])
#        
#        data['%d_TN_nonpref_fem_%s'% (perc, EC)]= (data['%d_TN_nonpref_fem_%s'% (perc, BSG)]+data['%d_TN_nonpref_fem_%s'% (perc, BSH)]+data['%d_TN_nonpref_fem_%s'% (perc, BSI)])
#        data['%d_TN_nonpref_fem_%s'% (perc, EE)]= (data['%d_TN_nonpref_fem_%s'% (perc, BCA)]+data['%d_TN_nonpref_fem_%s'% (perc, BCB)]+data['%d_TN_nonpref_fem_%s'% (perc, BCC)]+
#            data['%d_TN_nonpref_fem_%s'% (perc, BCD)])
#        
#        data['%d_TN_nonprefmale_%s'% (perc, EC)]= (data['%d_TN_nonprefmale_%s'% (perc, BSG)]+data['%d_TN_nonprefmale_%s'% (perc, BSH)]+data['%d_TN_nonprefmale_%s'% (perc, BSI)])
#        data['%d_TN_nonprefmale_%s'% (perc, EE)]= (data['%d_TN_nonprefmale_%s'% (perc, BCA)]+data['%d_TN_nonprefmale_%s'% (perc, BCB)]+data['%d_TN_nonprefmale_%s'% (perc, BCC)]+
#            data['%d_TN_nonprefmale_%s'% (perc, BCD)])
#        
#        data['%d_TD_pref_fem_%s'% (perc, EC)]= (data['%d_TD_pref_fem_%s'% (perc, BSG)]+data['%d_TD_pref_fem_%s'% (perc, BSH)]+data['%d_TD_pref_fem_%s'% (perc, BSI)])
#        data['%d_TD_pref_fem_%s'% (perc, EE)]= (data['%d_TD_pref_fem_%s'% (perc, BCA)]+data['%d_TD_pref_fem_%s'% (perc, BCB)]+data['%d_TD_pref_fem_%s'% (perc, BCC)]+data['%d_TD_pref_fem_%s'% (perc, BCD)])
#        
#        data['%d_TD_nonpref_fem_%s'% (perc, EC)]= (data['%d_TD_nonpref_fem_%s'% (perc, BSG)]+data['%d_TD_nonpref_fem_%s'% (perc, BSH)]+data['%d_TD_nonpref_fem_%s'% (perc, BSI)])
#        data['%d_TD_nonpref_fem_%s'% (perc, EE)]= (data['%d_TD_nonpref_fem_%s'% (perc, BCA)]+data['%d_TD_nonpref_fem_%s'% (perc, BCB)]+data['%d_TD_nonpref_fem_%s'% (perc, BCC)]+
#            data['%d_TD_nonpref_fem_%s'% (perc, BCD)])
#        
#        data['%d_TD_nonprefmale_%s'% (perc, EC)]= (data['%d_TD_nonprefmale_%s'% (perc, BSG)]+data['%d_TD_nonprefmale_%s'% (perc, BSH)]+data['%d_TD_nonprefmale_%s'% (perc, BSI)])
#        data['%d_TD_nonprefmale_%s'% (perc, EE)]= (data['%d_TD_nonprefmale_%s'% (perc, BCA)]+data['%d_TD_nonprefmale_%s'% (perc, BCB)]+data['%d_TD_nonprefmale_%s'% (perc, BCC)]+
#            data['%d_TD_nonprefmale_%s'% (perc, BCD)])
        
    # Calculate total number of each "social" behavior directed at each male in total environment
    for position, col_name in enumerate(list_behaviors_social):
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TNM1_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TNM1_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNM1_%s'% (perc, col_name)]) 
            data['%d_TNM1_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Male 1')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_num_back'], data['%d_TNM1_%s'% (perc, col_name)]) 
            data['%d_TNM1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TNM1_%s'% (perc, col_name)]=np.where(data['%d_TNM1_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNM1_%s'% (perc, col_name)])
            data['%d_TNM1_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TNM1_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNM1_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TNM1_%s'% (perc, col_name)])
            data['%d_TNM1_%s'% (perc, col_name)]=np.where(data['%d_TNM1_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNM1_%s'% (perc, col_name)])
            data['%d_TNM1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TNM1_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNM1_%s'% (perc, col_name)])
  
            data['%d_TNM2_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TNM2_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNM2_%s'% (perc, col_name)]) 
            data['%d_TNM2_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Male 2')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_num_back'], data['%d_TNM2_%s'% (perc, col_name)]) 
            data['%d_TNM2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TNM2_%s'% (perc, col_name)]=np.where(data['%d_TNM2_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNM2_%s'% (perc, col_name)])
            data['%d_TNM2_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TNM2_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNM2_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TNM2_%s'% (perc, col_name)])
            data['%d_TNM2_%s'% (perc, col_name)]=np.where(data['%d_TNM2_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNM2_%s'% (perc, col_name)])
            data['%d_TNM2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TNM2_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNM2_%s'% (perc, col_name)])
        
            data['%d_TNM3_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TNM3_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNM3_%s'% (perc, col_name)]) 
            data['%d_TNM3_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Male 3')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_num_back'], data['%d_TNM3_%s'% (perc, col_name)]) 
            data['%d_TNM3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TNM3_%s'% (perc, col_name)]=np.where(data['%d_TNM3_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNM3_%s'% (perc, col_name)])
            data['%d_TNM3_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TNM3_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNM3_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TNM3_%s'% (perc, col_name)])
            data['%d_TNM3_%s'% (perc, col_name)]=np.where(data['%d_TNM3_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNM3_%s'% (perc, col_name)])
            data['%d_TNM3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TNM3_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNM3_%s'% (perc, col_name)])
        
            data['%d_TNM4_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TNM4_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TNM4_%s'% (perc, col_name)]) 
            data['%d_TNM4_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num']==1)&(data[MODSUB]=='Male 4')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_num_back'], data['%d_TNM4_%s'% (perc, col_name)]) 
            data['%d_TNM4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TNM4_%s'% (perc, col_name)]=np.where(data['%d_TNM4_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TNM4_%s'% (perc, col_name)])
            data['%d_TNM4_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TNM4_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TNM4_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TNM4_%s'% (perc, col_name)])
            data['%d_TNM4_%s'% (perc, col_name)]=np.where(data['%d_TNM4_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TNM4_%s'% (perc, col_name)])
            data['%d_TNM4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TNM4_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TNM4_%s'% (perc, col_name)])
        
            # Calculate total duration of each "social" behavior directed at each Male in total environment
            data['%d_TDM1_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TDM1_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDM1_%s'% (perc, col_name)]) 
            data['%d_TDM1_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Male 1')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_sumdur'], data['%d_TDM1_%s'% (perc, col_name)]) 
            data['%d_TDM1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TDM1_%s'% (perc, col_name)]=np.where(data['%d_TDM1_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDM1_%s'% (perc, col_name)])
            data['%d_TDM1_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TDM1_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDM1_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TDM1_%s'% (perc, col_name)])
            data['%d_TDM1_%s'% (perc, col_name)]=np.where(data['%d_TDM1_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDM1_%s'% (perc, col_name)])
            data['%d_TDM1_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TDM1_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDM1_%s'% (perc, col_name)])
        
            data['%d_TDM2_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TDM2_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDM2_%s'% (perc, col_name)]) 
            data['%d_TDM2_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Male 2')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_sumdur'], data['%d_TDM2_%s'% (perc, col_name)]) 
            data['%d_TDM2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TDM2_%s'% (perc, col_name)]=np.where(data['%d_TDM2_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDM2_%s'% (perc, col_name)])
            data['%d_TDM2_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TDM2_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDM2_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TDM2_%s'% (perc, col_name)])
            data['%d_TDM2_%s'% (perc, col_name)]=np.where(data['%d_TDM2_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDM2_%s'% (perc, col_name)])
            data['%d_TDM2_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TDM2_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDM2_%s'% (perc, col_name)])
        
            data['%d_TDM3_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TDM3_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDM3_%s'% (perc, col_name)]) 
            data['%d_TDM3_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Male 3')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_sumdur'], data['%d_TDM3_%s'% (perc, col_name)]) 
            data['%d_TDM3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TDM3_%s'% (perc, col_name)]=np.where(data['%d_TDM3_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDM3_%s'% (perc, col_name)])
            data['%d_TDM3_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TDM3_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDM3_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TDM3_%s'% (perc, col_name)])
            data['%d_TDM3_%s'% (perc, col_name)]=np.where(data['%d_TDM3_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDM3_%s'% (perc, col_name)])
            data['%d_TDM3_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TDM3_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDM3_%s'% (perc, col_name)])
        
            data['%d_TDM4_%s'% (perc, col_name)]= np.where(data['obs_num']==1,99999, np.NaN) 
            data['%d_TDM4_%s'% (perc, col_name)]= np.where(data['obs_num_back']==1,88888, data['%d_TDM4_%s'% (perc, col_name)]) 
            data['%d_TDM4_%s'% (perc, col_name)]= np.where(((data[BEH]==col_name)&(data['obs_beh_int_modsub_num_back']==1)&(data[MODSUB]=='Male 4')&(data['interval']==perc)), 
                data['obs_beh_int_modsub_sumdur'], data['%d_TDM4_%s'% (perc, col_name)]) 
            data['%d_TDM4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)        
            data['%d_TDM4_%s'% (perc, col_name)]=np.where(data['%d_TDM4_%s'% (perc, col_name)]==99999, np.NaN, data['%d_TDM4_%s'% (perc, col_name)])
            data['%d_TDM4_%s'% (perc, col_name)].fillna(method = "backfill", inplace=True)
            data['%d_TDM4_%s'% (perc, col_name)]= np.where(((data['obs_num_back']!=1)&(data['%d_TDM4_%s'% (perc, col_name)]==88888)), 
                0,data['%d_TDM4_%s'% (perc, col_name)])
            data['%d_TDM4_%s'% (perc, col_name)]=np.where(data['%d_TDM4_%s'% (perc, col_name)]==88888, np.NaN, data['%d_TDM4_%s'% (perc, col_name)])
            data['%d_TDM4_%s'% (perc, col_name)].fillna(method = "ffill", inplace=True)
            data['%d_TDM4_%s'% (perc, col_name)]= np.where(data[BEH]=='None',0,data['%d_TDM4_%s'% (perc, col_name)])

    
    # Calculate total number of each behavior per rat in total environment for each interval
    for rank, perc in enumerate(list_intervals):
        
        # Calculate with which male is copulated the most
        data['%d_TNM1_%s'% (perc, EA)]= (data['%d_TNM1_%s'% (perc, BSD)]+data['%d_TNM1_%s'% (perc, BSE)]+data['%d_TNM1_%s'% (perc, BSF)])
        data['%d_TNM2_%s'% (perc, EA)]= (data['%d_TNM2_%s'% (perc, BSD)]+data['%d_TNM2_%s'% (perc, BSE)]+data['%d_TNM2_%s'% (perc, BSF)])
        data['%d_TNM3_%s'% (perc, EA)]= (data['%d_TNM3_%s'% (perc, BSD)]+data['%d_TNM3_%s'% (perc, BSE)]+data['%d_TNM3_%s'% (perc, BSF)])
        data['%d_TNM4_%s'% (perc, EA)]= (data['%d_TNM4_%s'% (perc, BSD)]+data['%d_TNM4_%s'% (perc, BSE)]+data['%d_TNM4_%s'% (perc, BSF)])
        
        data['%d_preferred_male' % perc]=np.where(((data['%d_TNM1_%s'% (perc, EA)]>data['%d_TNM2_%s'% (perc, EA)])&(data['%d_TNM1_%s'% (perc, EA)]>data['%d_TNM3_%s'% (perc, EA)])&
            (data['%d_TNM1_%s'% (perc, EA)]>data['%d_TNM4_%s'% (perc, EA)])),"Male 1", "")
        data['%d_preferred_male' % perc]=np.where(((data['%d_TNM2_%s'% (perc, EA)]>data['%d_TNM1_%s'% (perc, EA)])&(data['%d_TNM2_%s'% (perc, EA)]>data['%d_TNM3_%s'% (perc, EA)])&
            (data['%d_TNM2_%s'% (perc, EA)]>data['%d_TNM4_%s'% (perc, EA)])),"Male 2", data['%d_preferred_male' % perc])  
        data['%d_preferred_male' % perc]=np.where(((data['%d_TNM3_%s'% (perc, EA)]>data['%d_TNM1_%s'% (perc, EA)])&(data['%d_TNM3_%s'% (perc, EA)]>data['%d_TNM2_%s'% (perc, EA)])&
            (data['%d_TNM3_%s'% (perc, EA)]>data['%d_TNM4_%s'% (perc, EA)])),"Male 3", data['%d_preferred_male' % perc])  
        data['%d_preferred_male' % perc]=np.where(((data['%d_TNM4_%s'% (perc, EA)]>data['%d_TNM1_%s'% (perc, EA)])&(data['%d_TNM4_%s'% (perc, EA)]>data['%d_TNM3_%s'% (perc, EA)])&
            (data['%d_TNM4_%s'% (perc, EA)]>data['%d_TNM2_%s'% (perc, EA)])),"Male 4", data['%d_preferred_male' % perc])  
        
        # Create column for the ratID for the preferred male
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_male' % perc]=='Male 1'),EM11, "")
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_male' % perc]=='Male 2'),EM12, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_male' % perc]=='Male 3'),EM13, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE1')&(data['%d_preferred_male' % perc]=='Male 4'),EM14, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_male' % perc]=='Male 1'),EM21, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_male' % perc]=='Male 2'),EM22, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_male' % perc]=='Male 3'),EM23, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE2')&(data['%d_preferred_male' % perc]=='Male 4'),EM24, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_male' % perc]=='Male 1'),EM31, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_male' % perc]=='Male 2'),EM32, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_male' % perc]=='Male 3'),EM33, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE3')&(data['%d_preferred_male' % perc]=='Male 4'),EM34, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_male' % perc]=='Male 1'),EM41, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_male' % perc]=='Male 2'),EM42, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_male' % perc]=='Male 3'),EM43, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE4')&(data['%d_preferred_male' % perc]=='Male 4'),EM44, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_male' % perc]=='Male 1'),EM51, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_male' % perc]=='Male 2'),EM52, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_male' % perc]=='Male 3'),EM53, data['%d_pref_male_RatID'% perc])
        data['%d_pref_male_RatID'% perc]=np.where((data['Cohort']=='SNE5')&(data['%d_preferred_male' % perc]=='Male 4'),EM54, data['%d_pref_male_RatID'% perc])
        
    # Number and durations of behaviors directed at the preferred copulation partner
    for position, col_name in enumerate(list_behaviors_social): 
        # Calculate total number of each behavior per rat in total environment for each interval
        for rank, perc in enumerate(list_intervals):
            data['%d_TN_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 1', data['%d_TNM1_%s'% (perc, col_name)],np.NaN)
            data['%d_TN_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 2', data['%d_TNM2_%s'% (perc, col_name)],
                data['%d_TN_pref_male_%s'% (perc, col_name)]) 
            data['%d_TN_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 3', data['%d_TNM3_%s'% (perc, col_name)],
                data['%d_TN_pref_male_%s'% (perc, col_name)]) 
            data['%d_TN_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 4', data['%d_TNM4_%s'% (perc, col_name)],
                data['%d_TN_pref_male_%s'% (perc, col_name)])     
            
            data['%d_TN_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 1',((data['%d_TNM2_%s'% (perc, col_name)]+ 
                data['%d_TNM3_%s'% (perc, col_name)]+ data['%d_TNM4_%s'% (perc, col_name)])/3),np.NaN)
            data['%d_TN_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 2',((data['%d_TNM1_%s'% (perc, col_name)]+ 
                data['%d_TNM3_%s'% (perc, col_name)]+ data['%d_TNM4_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_male_%s'% (perc, col_name)])    
            data['%d_TN_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 3',((data['%d_TNM1_%s'% (perc, col_name)]+ 
                    data['%d_TDM2_%s'% (perc, col_name)]+ data['%d_TNM4_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_male_%s'% (perc, col_name)])
            data['%d_TN_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 4',((data['%d_TNM1_%s'% (perc, col_name)]+ 
                data['%d_TNM3_%s'% (perc, col_name)]+ data['%d_TNM2_%s'% (perc, col_name)])/3),data['%d_TN_nonpref_male_%s'% (perc, col_name)]) 
                 
            data['%d_TD_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 1', data['%d_TDM1_%s'% (perc, col_name)],np.NaN)
            data['%d_TD_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 2', data['%d_TDM2_%s'% (perc, col_name)],
                data['%d_TD_pref_male_%s'% (perc, col_name)]) 
            data['%d_TD_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 3', data['%d_TDM3_%s'% (perc, col_name)],
                data['%d_TD_pref_male_%s'% (perc, col_name)]) 
            data['%d_TD_pref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 4',data['%d_TDM4_%s'% (perc, col_name)],
                data['%d_TD_pref_male_%s'% (perc, col_name)])     
            
            data['%d_TD_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 1',((data['%d_TDM2_%s'% (perc, col_name)]+ 
                data['%d_TDM3_%s'% (perc, col_name)]+data['%d_TDM4_%s'% (perc, col_name)])/3),np.NaN)
            data['%d_TD_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 2',((data['%d_TDM1_%s'% (perc, col_name)]+ 
                data['%d_TDM3_%s'% (perc, col_name)]+data['%d_TDM4_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_male_%s'% (perc, col_name)])    
            data['%d_TD_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 3',((data['%d_TDM1_%s'% (perc, col_name)]+ 
                    data['%d_TDM2_%s'% (perc, col_name)]+data['%d_TDM4_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_male_%s'% (perc, col_name)])
            data['%d_TD_nonpref_male_%s'% (perc, col_name)]=np.where(data['%d_preferred_male' % perc]=='Male 4',((data['%d_TDM1_%s'% (perc, col_name)]+ 
                data['%d_TDM3_%s'% (perc, col_name)]+ data['%d_TDM2_%s'% (perc, col_name)])/3),data['%d_TD_nonpref_male_%s'% (perc, col_name)]) 
   
    # Calculate total number of each behavior per rat in total environment for each interval
    for rank, perc in enumerate(list_intervals):
       
        data['%d_TN_pref_male_%s'% (perc, EC)]= (data['%d_TN_pref_male_%s'% (perc, BSG)]+data['%d_TN_pref_male_%s'% (perc, BSH)]+data['%d_TN_pref_male_%s'% (perc, BSI)])
        data['%d_TN_pref_male_%s'% (perc, EE)]= (data['%d_TN_pref_male_%s'% (perc, BCA)]+data['%d_TN_pref_male_%s'% (perc, BCB)]+data['%d_TN_pref_male_%s'% (perc, BCC)]+
            data['%d_TN_pref_male_%s'% (perc, BCD)])
        
        data['%d_TN_nonpref_male_%s'% (perc, EC)]= (data['%d_TN_nonpref_male_%s'% (perc, BSG)]+data['%d_TN_nonpref_male_%s'% (perc, BSH)]+data['%d_TN_nonpref_male_%s'% (perc, BSI)])
        data['%d_TN_nonpref_male_%s'% (perc, EE)]= (data['%d_TN_nonpref_male_%s'% (perc, BCA)]+data['%d_TN_nonpref_male_%s'% (perc, BCB)]+data['%d_TN_nonpref_male_%s'% (perc, BCC)]+
            data['%d_TN_nonpref_male_%s'% (perc, BCD)])
        
       
        data['%d_TD_pref_male_%s'% (perc, EC)]= (data['%d_TD_pref_male_%s'% (perc, BSG)]+data['%d_TD_pref_male_%s'% (perc, BSH)]+data['%d_TD_pref_male_%s'% (perc, BSI)])
        data['%d_TD_pref_male_%s'% (perc, EE)]= (data['%d_TD_pref_male_%s'% (perc, BCA)]+data['%d_TD_pref_male_%s'% (perc, BCB)]+data['%d_TD_pref_male_%s'% (perc, BCC)]+data['%d_TD_pref_male_%s'% (perc, BCD)])
        
        data['%d_TD_nonpref_male_%s'% (perc, EC)]= (data['%d_TD_nonpref_male_%s'% (perc, BSG)]+data['%d_TD_nonpref_male_%s'% (perc, BSH)]+data['%d_TD_nonpref_male_%s'% (perc, BSI)])
        data['%d_TD_nonpref_male_%s'% (perc, EE)]= (data['%d_TD_nonpref_male_%s'% (perc, BCA)]+data['%d_TD_nonpref_male_%s'% (perc, BCB)]+data['%d_TD_nonpref_male_%s'% (perc, BCC)]+
            data['%d_TD_nonpref_male_%s'% (perc, BCD)])
        

# Make sure that all the rats that did not show behavior gets the numbers deleted.
data_all_columns=list(data_all.columns.values)
relevant_data_all_columns=data_all_columns[97:]

for i in missing_all:
    for position, column in enumerate(relevant_data_all_columns):
        data_all[column]=np.where(data_all[SUBRAW]==i,0,data_all[column])

data_CB1_columns=list(data_CB1.columns.values)
relevant_data_CB1_columns=data_CB1_columns[97:]

for i in missing_CB1:
    for position, column in enumerate(relevant_data_CB1_columns):
        data_CB1[column]=np.where(data_CB1[SUBRAW]==i,0,data_CB1[column])

data_CB2_columns=list(data_CB2.columns.values)
relevant_data_CB2_columns=data_CB2_columns[97:]

for i in missing_CB2:
    for position, column in enumerate(relevant_data_CB2_columns):
        data_CB2[column]=np.where(data_CB2[SUBRAW]==i,np.NaN,data_CB2[column])

data_CB3_columns=list(data_CB3.columns.values)
relevant_data_CB3_columns=data_CB3_columns[97:]

for i in missing_CB3:
    for position, column in enumerate(relevant_data_CB3_columns):
        data_CB3[column]=np.where(data_CB3[SUBRAW]==i,np.NaN,data_CB3[column])

data_CB4_columns=list(data_CB4.columns.values)
relevant_data_CB4_columns=data_CB4_columns[97:]

for i in missing_CB4:
    for position, column in enumerate(relevant_data_CB4_columns):
        data_CB4[column]=np.where(data_CB4[SUBRAW]==i,np.NaN,data_CB4[column])

data_CB5_columns=list(data_CB5.columns.values)
relevant_data_CB5_columns=data_CB5_columns[97:]

for i in missing_CB5:
    for position, column in enumerate(relevant_data_CB5_columns):
        data_CB5[column]=np.where(data_CB5[SUBRAW]==i,np.NaN,data_CB5[column])

data_CB6_columns=list(data_CB6.columns.values)
relevant_data_CB6_columns=data_CB6_columns[97:]

for i in missing_CB6:
    for position, column in enumerate(relevant_data_CB6_columns):
        data_CB6[column]=np.where(data_CB6[SUBRAW]==i,np.NaN,data_CB6[column])

# Just to get notification this part is finished
print("data finished")

## now save the data frame to excel
#data_full.to_csv("HN003 raw data full_perc.csv")
#data_all.to_csv("HN003 raw data all_perc.csv")
#data_CB1.to_csv("HN003 raw data CB1_perc.csv")
#data_CB2.to_csv("HN003 raw data CB2_perc.csv")
#data_CB3.to_csv("HN003 raw data CB3_perc.csv")
#data_CB4.to_csv("HN003 raw data CB4_perc.csv")
#data_CB5.to_csv("HN003 raw data CB5_perc.csv")
#data_CB6.to_csv("HN003 raw data CB6_perc.csv")

#Now continue with getting result files out of the different dataframes:
df_CB=[data_all,data_CB1,data_CB2,data_CB3,data_CB4,data_CB5,data_CB6]
for dt, dataframe in enumerate(df_CB): 
    data=dataframe

    # Delete the rows without ratID
    data= data.dropna(axis=0, subset=['RatID'])
    
# Calculate the results per rat and write to a new dataframe  
results_all=data_all.groupby(RATID).max()
results_CB1=data_CB1.groupby(RATID).max()
results_CB2=data_CB2.groupby(RATID).max()
results_CB3=data_CB3.groupby(RATID).max()
results_CB4=data_CB4.groupby(RATID).max()
results_CB5=data_CB5.groupby(RATID).max()
results_CB6=data_CB6.groupby(RATID).max()

# Get the most active bout
# First add the CB to column title
results_CB1.columns = ['CB1_'+ str(col) for col in results_CB1.columns]
results_CB2.columns = ['CB2_'+ str(col) for col in results_CB2.columns]
results_CB3.columns = ['CB3_'+ str(col) for col in results_CB3.columns]
results_CB4.columns = ['CB4_'+ str(col) for col in results_CB4.columns]
results_CB5.columns = ['CB5_'+ str(col) for col in results_CB5.columns]
results_CB6.columns = ['CB6_'+ str(col) for col in results_CB6.columns]

# Create a new dataframe with all the columns
results_MAB_full= pd.concat([results_CB1, results_CB2,results_CB3,results_CB4,results_CB5,results_CB6], sort=False, axis=1)

## Make a column that mentions the most active bout
results_MAB_full=results_MAB_full.reset_index()
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC1','CB1',"")
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC2','CB5',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC3','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC4','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC5','CB2',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC6','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC7','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC8','CB2',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC9','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FC10','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF1','CB2',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF2','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF3','CB2',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF4','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF5','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF6','CB1',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF7','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF8','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF9','CB3',results_MAB_full['MAB_CB'])
results_MAB_full['MAB_CB']=np.where(results_MAB_full['RatID']=='FF10','CB4',results_MAB_full['MAB_CB'])
   
results_MAB_full=results_MAB_full.set_index('RatID')
    
## Make sure to remove the zeros from CB2 and higher
#results_MAB_full['CB2_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
#results_MAB_full['CB3_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
#results_MAB_full['CB4_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
#results_MAB_full['CB5_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
#results_MAB_full['CB6_TN_%s'% BSB].replace(0, np.NaN, inplace = True)

# Make dataframes for the most active bout
results_MAB_CB1=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB1',results_MAB_full.columns.str.contains('CB1_')]
results_MAB_CB2=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB2',results_MAB_full.columns.str.contains('CB2_')]
results_MAB_CB3=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB3',results_MAB_full.columns.str.contains('CB3_')]
results_MAB_CB4=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB4',results_MAB_full.columns.str.contains('CB4_')]
results_MAB_CB5=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB5',results_MAB_full.columns.str.contains('CB5_')]
results_MAB_CB6=results_MAB_full.loc[results_MAB_full['MAB_CB']=='CB6',results_MAB_full.columns.str.contains('CB6_')]

# Make sure to remove the CB in column title
results_CB1.columns = results_CB1.columns.str.replace('CB1_', '')
results_CB2.columns = results_CB2.columns.str.replace('CB2_', '')
results_CB3.columns = results_CB3.columns.str.replace('CB3_', '')
results_CB4.columns = results_CB4.columns.str.replace('CB4_', '')
results_CB5.columns = results_CB5.columns.str.replace('CB5_', '')
results_CB6.columns = results_CB6.columns.str.replace('CB6_', '')
results_MAB_CB1.columns = results_MAB_CB1.columns.str.replace('CB1_', '')
results_MAB_CB2.columns = results_MAB_CB2.columns.str.replace('CB2_', '')
results_MAB_CB3.columns = results_MAB_CB3.columns.str.replace('CB3_', '')
results_MAB_CB4.columns = results_MAB_CB4.columns.str.replace('CB4_', '')
results_MAB_CB5.columns = results_MAB_CB5.columns.str.replace('CB5_', '')
results_MAB_CB6.columns = results_MAB_CB6.columns.str.replace('CB6_', '')

# Make one dataframe of the MAB
results_MAB=pd.concat([results_MAB_CB1,results_MAB_CB2,results_MAB_CB3,results_MAB_CB4,results_MAB_CB5,results_MAB_CB6], sort=False, axis=0)

# Make excel sheets with relevant information
results_all_pre=results_all.loc[:,(list_resultsheet)]
results_CB1_pre=results_CB1.loc[:,(list_resultsheet)]
results_CB2_pre=results_CB2.loc[:,(list_resultsheet)]
results_CB3_pre=results_CB3.loc[:,(list_resultsheet)]
results_CB4_pre=results_CB4.loc[:,(list_resultsheet)]
results_CB5_pre=results_CB5.loc[:,(list_resultsheet)]
results_CB6_pre=results_CB6.loc[:,(list_resultsheet)]
results_MAB_pre=results_MAB.loc[:,(list_resultsheet)]

results_all_pre2=results_all.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB1_pre2=results_CB1.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB2_pre2=results_CB2.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB3_pre2=results_CB3.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB4_pre2=results_CB4.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB5_pre2=results_CB5.loc[:,(OBS,'Cohort','CB',TREAT)]
results_CB6_pre2=results_CB6.loc[:,(OBS,'Cohort','CB',TREAT)]
results_MAB_pre2=results_MAB.loc[:,(OBS,'Cohort','CB',TREAT)]

results_all_TN= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB1_TN= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB2_TN= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB3_TN= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB4_TN= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB5_TN= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('TN_')]], sort=False, axis=1)
results_CB6_TN= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('TN_')]], sort=False, axis=1)
results_MAB_TN= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('TN_')]], sort=False, axis=1)

results_all_TN.drop([col for col in results_all_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB1_TN.drop([col for col in results_CB1_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB2_TN.drop([col for col in results_CB2_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB3_TN.drop([col for col in results_CB3_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB4_TN.drop([col for col in results_CB4_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB5_TN.drop([col for col in results_CB5_TN.columns if 'min' in col],axis=1,inplace=True)
results_CB6_TN.drop([col for col in results_CB6_TN.columns if 'min' in col],axis=1,inplace=True)
results_MAB_TN.drop([col for col in results_MAB_TN.columns if 'min' in col],axis=1,inplace=True)

results_all_ON= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB1_ON= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB2_ON= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB3_ON= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB4_ON= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB5_ON= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('ON_')]], sort=False, axis=1)
results_CB6_ON= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('ON_')]], sort=False, axis=1)
results_MAB_ON= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('ON_')]], sort=False, axis=1)

results_all_ON.drop([col for col in results_all_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB1_ON.drop([col for col in results_CB1_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB2_ON.drop([col for col in results_CB2_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB3_ON.drop([col for col in results_CB3_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB4_ON.drop([col for col in results_CB4_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB5_ON.drop([col for col in results_CB5_ON.columns if 'min' in col],axis=1,inplace=True)
results_CB6_ON.drop([col for col in results_CB6_ON.columns if 'min' in col],axis=1,inplace=True)
results_MAB_ON.drop([col for col in results_MAB_ON.columns if 'min' in col],axis=1,inplace=True)

results_all_BN= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB1_BN= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB2_BN= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB3_BN= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB4_BN= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB5_BN= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('BN_')]], sort=False, axis=1)
results_CB6_BN= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('BN_')]], sort=False, axis=1)
results_MAB_BN= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('BN_')]], sort=False, axis=1)

results_all_BN.drop([col for col in results_all_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB1_BN.drop([col for col in results_CB1_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB2_BN.drop([col for col in results_CB2_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB3_BN.drop([col for col in results_CB3_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB4_BN.drop([col for col in results_CB4_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB5_BN.drop([col for col in results_CB5_BN.columns if 'min' in col],axis=1,inplace=True)
results_CB6_BN.drop([col for col in results_CB6_BN.columns if 'min' in col],axis=1,inplace=True)
results_MAB_BN.drop([col for col in results_MAB_BN.columns if 'min' in col],axis=1,inplace=True)

results_all_TD= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB1_TD= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB2_TD= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB3_TD= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB4_TD= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB5_TD= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('TD_')]], sort=False, axis=1)
results_CB6_TD= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('TD_')]], sort=False, axis=1)
results_MAB_TD= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('TD_')]], sort=False, axis=1)

results_all_TD.drop([col for col in results_all_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB1_TD.drop([col for col in results_CB1_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB2_TD.drop([col for col in results_CB2_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB3_TD.drop([col for col in results_CB3_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB4_TD.drop([col for col in results_CB4_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB5_TD.drop([col for col in results_CB5_TD.columns if 'min' in col],axis=1,inplace=True)
results_CB6_TD.drop([col for col in results_CB6_TD.columns if 'min' in col],axis=1,inplace=True)
results_MAB_TD.drop([col for col in results_MAB_TD.columns if 'min' in col],axis=1,inplace=True)

results_all_OD= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB1_OD= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB2_OD= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB3_OD= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB4_OD= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB5_OD= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('OD_')]], sort=False, axis=1)
results_CB6_OD= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('OD_')]], sort=False, axis=1)
results_MAB_OD= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('OD_')]], sort=False, axis=1)

results_all_OD.drop([col for col in results_all_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB1_OD.drop([col for col in results_CB1_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB2_OD.drop([col for col in results_CB2_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB3_OD.drop([col for col in results_CB3_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB4_OD.drop([col for col in results_CB4_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB5_OD.drop([col for col in results_CB5_OD.columns if 'min' in col],axis=1,inplace=True)
results_CB6_OD.drop([col for col in results_CB6_OD.columns if 'min' in col],axis=1,inplace=True)
results_MAB_OD.drop([col for col in results_MAB_OD.columns if 'min' in col],axis=1,inplace=True)

results_all_BD= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB1_BD= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB2_BD= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB3_BD= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB4_BD= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB5_BD= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('BD_')]], sort=False, axis=1)
results_CB6_BD= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('BD_')]], sort=False, axis=1)
results_MAB_BD= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('BD_')]], sort=False, axis=1)

results_all_BD.drop([col for col in results_all_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB1_BD.drop([col for col in results_CB1_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB2_BD.drop([col for col in results_CB2_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB3_BD.drop([col for col in results_CB3_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB4_BD.drop([col for col in results_CB4_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB5_BD.drop([col for col in results_CB5_BD.columns if 'min' in col],axis=1,inplace=True)
results_CB6_BD.drop([col for col in results_CB6_BD.columns if 'min' in col],axis=1,inplace=True)
results_MAB_BD.drop([col for col in results_MAB_BD.columns if 'min' in col],axis=1,inplace=True)

results_all_TN_min= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB1_TN_min= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB2_TN_min= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB3_TN_min= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB4_TN_min= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB5_TN_min= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TN_min')]], sort=False, axis=1)
results_CB6_TN_min= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TN_min')]], sort=False, axis=1)
results_MAB_TN_min= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TN_min')]], sort=False, axis=1)

results_all_ON_min= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB1_ON_min= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB2_ON_min= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB3_ON_min= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB4_ON_min= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB5_ON_min= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('ON_min')]], sort=False, axis=1)
results_CB6_ON_min= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('ON_min')]], sort=False, axis=1)
results_MAB_ON_min= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('ON_min')]], sort=False, axis=1)

results_all_BN_min= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB1_BN_min= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB2_BN_min= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB3_BN_min= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB4_BN_min= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB5_BN_min= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('BN_min')]], sort=False, axis=1)
results_CB6_BN_min= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('BN_min')]], sort=False, axis=1)
results_MAB_BN_min= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('BN_min')]], sort=False, axis=1)

results_all_TD_min= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB1_TD_min= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB2_TD_min= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB3_TD_min= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB4_TD_min= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB5_TD_min= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TD_min')]], sort=False, axis=1)
results_CB6_TD_min= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TD_min')]], sort=False, axis=1)
results_MAB_TD_min= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TD_min')]], sort=False, axis=1)

results_all_OD_min= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB1_OD_min= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB2_OD_min= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB3_OD_min= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB4_OD_min= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB5_OD_min= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('OD_min')]], sort=False, axis=1)
results_CB6_OD_min= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('OD_min')]], sort=False, axis=1)
results_MAB_OD_min= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('OD_min')]], sort=False, axis=1)

results_all_BD_min= pd.concat([results_all_pre, results_all.loc[:, results_all.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB1_BD_min= pd.concat([results_CB1_pre, results_CB1.loc[:, results_CB1.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB2_BD_min= pd.concat([results_CB2_pre, results_CB2.loc[:, results_CB2.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB3_BD_min= pd.concat([results_CB3_pre, results_CB3.loc[:, results_CB3.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB4_BD_min= pd.concat([results_CB4_pre, results_CB4.loc[:, results_CB4.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB5_BD_min= pd.concat([results_CB5_pre, results_CB5.loc[:, results_CB5.columns.str.contains('BD_min')]], sort=False, axis=1)
results_CB6_BD_min= pd.concat([results_CB6_pre, results_CB6.loc[:, results_CB6.columns.str.contains('BD_min')]], sort=False, axis=1)
results_MAB_BD_min= pd.concat([results_MAB_pre, results_MAB.loc[:, results_MAB.columns.str.contains('BD_min')]], sort=False, axis=1)

# Make a list of all result dataframes
list_df_results=[results_all_TN,results_all_ON,results_all_BN,results_all_TD,results_all_OD,results_all_BD,
                 results_CB1_TN,results_CB1_ON,results_CB1_BN,results_CB1_TD,results_CB1_OD,results_CB1_BD,
                 results_CB2_TN,results_CB2_ON,results_CB2_BN,results_CB2_TD,results_CB2_OD,results_CB2_BD,
                 results_CB3_TN,results_CB3_ON,results_CB3_BN,results_CB3_TD,results_CB3_OD,results_CB3_BD,
                 results_CB4_TN,results_CB4_ON,results_CB4_BN,results_CB4_TD,results_CB4_OD,results_CB4_BD,
                 results_CB5_TN,results_CB5_ON,results_CB5_BN,results_CB5_TD,results_CB5_OD,results_CB5_BD,
                 results_CB6_TN,results_CB6_ON,results_CB6_BN,results_CB6_TD,results_CB6_OD,results_CB6_BD,
                 results_MAB_TN,results_MAB_ON,results_MAB_BN,results_MAB_TD,results_MAB_OD,results_MAB_BD,
                 results_all_TN_min,results_all_ON_min,results_all_BN_min,results_all_TD_min,results_all_OD_min,results_all_BD_min,
                 results_CB1_TN_min,results_CB1_ON_min,results_CB1_BN_min,results_CB1_TD_min,results_CB1_OD_min,results_CB1_BD_min,
                 results_CB2_TN_min,results_CB2_ON_min,results_CB2_BN_min,results_CB2_TD_min,results_CB2_OD_min,results_CB2_BD_min,
                 results_CB3_TN_min,results_CB3_ON_min,results_CB3_BN_min,results_CB3_TD_min,results_CB3_OD_min,results_CB3_BD_min,
                 results_CB4_TN_min,results_CB4_ON_min,results_CB4_BN_min,results_CB4_TD_min,results_CB4_OD_min,results_CB4_BD_min,
                 results_CB5_TN_min,results_CB5_ON_min,results_CB5_BN_min,results_CB5_TD_min,results_CB5_OD_min,results_CB5_BD_min,
                 results_CB6_TN_min,results_CB6_ON_min,results_CB6_BN_min,results_CB6_TD_min,results_CB6_OD_min,results_CB6_BD_min,
                 results_MAB_TN_min,results_MAB_ON_min,results_MAB_BN_min,results_MAB_TD_min,results_MAB_OD_min,results_MAB_BD_min]


for item, df in enumerate(list_df_results):
    df.columns=df.columns.str.replace(' ', '')
    df.columns=df.columns.str.replace('/', '')
    df.columns=df.columns.str.replace('-', '')
    df.columns=df.columns.str.replace('(', '')
    df.columns=df.columns.str.replace(')', '')

# Just to get notification this part is finished
print("results finished")

# Make a sheet to explain the columns
data_info=pd.DataFrame()
data_info['Code']=('Observation','Cohort','Treatment','Start_estrus','End_estrus','Duration_estrus_min','Total copulation',
         'Lordosis quotient', 'Active social behavior', 'conflict behavior','Total lordosis','lordosis quotient plus',
         'TN','ON','BN','TD','OD','BD','TN_min','ON_min','BN_min','TD_min','OD_min','BD_min',
         'TNM','ONM','BNM','TNF','ONF','BNF','TDM','ODM','BDM','TDF','ODF','BDF','TNFR','TNCR',
         'ONFR','ONCR','BNFR','BNCR','TDFR','TDCR','ODFR','ODCR','BDFR','BDCR','TNCM',
         'TNCF','TNFM','TNFF','ONCM','ONCF','ONFM','ONFF','BNCM','BNCF','BNFM','BNFF','TDCM',
         'TDCF','TDFM','TDFF','ODCM','ODCF','ODFM','ODFF','BDCM','BDCF','BDFM','BDFF',
         'TNF1','TNF2','TNF3','TNF4','TDF1','TDF2','TDF3','TDF4','preferred_female','pref_fem_RatID',
         'TN_pref_female','TN_nonpref_female','TN_nonprefmale','TD_pref_female','TD_nonpref_female','TD_nonprefmale',
         'TNM1','TNM2','TNM3','TNM4','TDM1','TDM2','TDM3','TDM4','preferred_male','pref_male_RatID',
         'TN_pref_male','TN_nonpref_male','TN_nonpreffemale','TD_pref_male','TD_nonpref_male','TD_nonpreffemale','nr_sexpartners', 
         'nr sexpartners_mistake')
               
data_info['Explanation']=('Experiment','Cohort','Treatment','Start time behavioral estrus', 'End time behavioral estrus',
         'Duration of behavioral estrus (in minutes)','mounts, intromissions and ejaculations',
         'lordosis / copulations * 100%', 'grooming + sniffing + anogenitally sniffing',
         'nose-off + boxing + fighting + chase away + flee',
         'lordosis + lordosis doubts','LQ for total lordosis','Total number in total environment',
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
         'Total number of behaviors to Female 1 modifier', 'Total number of behaviors to Female 2 modifier', 
       'Total number of behaviors to Female 3 modifier', 'Total number of behaviors to Female 4 modifier',
       'Total duration of behaviors to Female 1 modifier', 'Total duration of behaviors to Female 2 modifier', 
       'Total duration of behaviors to Female 3 modifier', 'Total duration of behaviors to Female 4 modifier',
       'Female with who most copulations took place','RatID of the preferred female','Total number of behaviors with preferred female',
       'Total number of behaviors with non-preferred females divided by 3','Total number of behaviors with males divided by 4',
       'Total duration of behaviors with preferred female','Total duration of behaviors with non-preferred females divided by 3', 
       'Total duration of behaviors with non-preferred males divided by 4',
        'Total number of behaviors to Male 1 modifier', 'Total number of behaviors to Male 2 modifier', 
       'Total number of behaviors to Male 3 modifier', 'Total number of behaviors to Male 4 modifier',
       'Total duration of behaviors to Male 1 modifier', 'Total duration of behaviors to Male 2 modifier', 
       'Total duration of behaviors to Male 3 modifier', 'Total duration of behaviors to Male 4 modifier',
       'Male with who most copulations took place','RatID of the preferred Male','Total number of behaviors with preferred Male',
       'Total number of behaviors with non-preferred Males divided by 3','Total number of behaviors with females divided by 4',
       'Total duration of behaviors with preferred Male','Total duration of behaviors with non-preferred Males divided by 3', 
       'Total duration of behaviors with non-preferred males divided by 4','Number of copulation partners', 
       'Number of copulation partners without possible mistakes counting')
   

# Statistics on the data
# Make lists with the titles for the keys of the dictionairies for the statistics
list_mean_titles=['mean_all_TN','mean_all_TD',
                 'mean_CB1_TN','mean_CB1_TD',
                 'mean_CB2_TN','mean_CB2_TD',
                 'mean_CB3_TN','mean_CB3_TD',
                 'mean_CB4_TN','mean_CB4_TD',
                 'mean_CB5_TN','mean_CB5_TD',
                 'mean_CB6_TN','mean_CB6_TD',
                 'mean_MAB_TN','mean_MAB_TD',
                 'mean_all_TN_min','mean_all_TD_min',
                 'mean_CB1_TN_min','mean_CB1_TD_min',
                 'mean_CB2_TN_min','mean_CB2_TD_min',
                 'mean_CB3_TN_min','mean_CB3_TD_min',
                 'mean_CB4_TN_min','mean_CB4_TD_min',
                 'mean_CB5_TN_min','mean_CB5_TD_min',
                 'mean_CB6_TN_min','mean_CB6_TD_min',
                 'mean_MAB_TN_min','mean_MAB_TD_min']

# Make lists with the titles for the keys of the dictionairies for the statistics
list_mean_titles=['mean_all_TN','mean_all_ON','mean_all_BN','mean_all_TD','mean_all_OD','mean_all_BD',
                 'mean_CB1_TN','mean_CB1_ON','mean_CB1_BN','mean_CB1_TD','mean_CB1_OD','mean_CB1_BD',
                 'mean_CB2_TN','mean_CB2_ON','mean_CB2_BN','mean_CB2_TD','mean_CB2_OD','mean_CB2_BD',
                 'mean_CB3_TN','mean_CB3_ON','mean_CB3_BN','mean_CB3_TD','mean_CB3_OD','mean_CB3_BD',
                 'mean_CB4_TN','mean_CB4_ON','mean_CB4_BN','mean_CB4_TD','mean_CB4_OD','mean_CB4_BD',
                 'mean_CB5_TN','mean_CB5_ON','mean_CB5_BN','mean_CB5_TD','mean_CB5_OD','mean_CB5_BD',
                 'mean_CB6_TN','mean_CB6_ON','mean_CB6_BN','mean_CB6_TD','mean_CB6_OD','mean_CB6_BD',
                 'mean_MAB_TN','mean_MAB_ON','mean_MAB_BN','mean_MAB_TD','mean_MAB_OD','mean_MAB_BD',
                 'mean_all_TN_min','mean_all_ON_min','mean_all_BN_min','mean_all_TD_min','mean_all_OD_min','mean_all_BD_min',
                 'mean_CB1_TN_min','mean_CB1_ON_min','mean_CB1_BN_min','mean_CB1_TD_min','mean_CB1_OD_min','mean_CB1_BD_min',
                 'mean_CB2_TN_min','mean_CB2_ON_min','mean_CB2_BN_min','mean_CB2_TD_min','mean_CB2_OD_min','mean_CB2_BD_min',
                 'mean_CB3_TN_min','mean_CB3_ON_min','mean_CB3_BN_min','mean_CB3_TD_min','mean_CB3_OD_min','mean_CB3_BD_min',
                 'mean_CB4_TN_min','mean_CB4_ON_min','mean_CB4_BN_min','mean_CB4_TD_min','mean_CB4_OD_min','mean_CB4_BD_min',
                 'mean_CB5_TN_min','mean_CB5_ON_min','mean_CB5_BN_min','mean_CB5_TD_min','mean_CB5_OD_min','mean_CB5_BD_min',
                 'mean_CB6_TN_min','mean_CB6_ON_min','mean_CB6_BN_min','mean_CB6_TD_min','mean_CB6_OD_min','mean_CB6_BD_min',
                 'mean_MAB_TN_min','mean_MAB_ON_min','mean_MAB_BN_min','mean_MAB_TD_min','mean_MAB_OD_min','mean_CB6_BD_min']


list_median_titles=[]
list_std_titles=[]
list_sem_titles=[]
list_var_titles=[]
list_q25_titles=[]
list_q75_titles=[]
list_stat_titles=[]
list_results_titles=[]

for i, stat in enumerate(list_mean_titles):
    temp=stat.replace('mean','median')
    list_median_titles.append(temp)
    temp=stat.replace('mean','std')
    list_std_titles.append(temp)
    temp=stat.replace('mean','sem')
    list_sem_titles.append(temp)
    temp=stat.replace('mean','var')
    list_var_titles.append(temp)
    temp=stat.replace('mean','q25')
    list_q25_titles.append(temp)
    temp=stat.replace('mean','q75')
    list_q75_titles.append(temp)
    temp=stat.replace('mean_','')
    list_stat_titles.append(temp)
    temp=stat.replace('mean_','')
    list_results_titles.append(temp)

# Make dictionairy for the stats    
dict_mean={}
dict_median={}
dict_std={}
dict_sem={}
dict_var={}
dict_q25={}
dict_q75={}

for k, df_result in enumerate(list_df_results):
    dict_mean[k]=df_result.groupby(TREAT).mean()
    dict_median[k]=df_result.groupby(TREAT).median()
    dict_sem[k]=df_result.groupby(TREAT).sem()
    dict_std[k]=df_result.groupby(TREAT).std()
    dict_var[k]=df_result.groupby(TREAT).var()
    dict_q25[k]=df_result.groupby(TREAT).quantile(q=0.25, axis=0)
    dict_q75[k]=df_result.groupby(TREAT).quantile(q=0.75, axis=0)

# Rename the keys to the right stat names
dict_mean = dict(zip(list_stat_titles, list(dict_mean.values())))
dict_median = dict(zip(list_stat_titles, list(dict_median.values())))
dict_std = dict(zip(list_stat_titles, list(dict_std.values())))
dict_sem = dict(zip(list_stat_titles, list(dict_sem.values())))
dict_var = dict(zip(list_stat_titles, list(dict_var.values())))
dict_q25 = dict(zip(list_stat_titles, list(dict_q25.values())))
dict_q75 = dict(zip(list_stat_titles, list(dict_q75.values())))

# Now make dataframes from the dictionairies
df_mean=pd.DataFrame.from_dict({(i,j): dict_mean[i][j] 
                           for i in dict_mean.keys() 
                           for j in dict_mean[i].keys()},
                       orient='index')
df_mean=df_mean.loc[:,['CTR-females','FLX-females']]
df_mean.columns = ['mean_'+ str(col) for col in df_mean.columns]

df_sem=pd.DataFrame.from_dict({(i,j): dict_sem[i][j] 
                           for i in dict_sem.keys() 
                           for j in dict_sem[i].keys()},
                       orient='index')
df_sem=df_sem.loc[:,['CTR-females','FLX-females']]
df_sem.columns = ['sem_'+ str(col) for col in df_sem.columns]

df_median=pd.DataFrame.from_dict({(i,j): dict_median[i][j] 
                           for i in dict_median.keys() 
                           for j in dict_median[i].keys()},
                       orient='index')
df_median=df_median.loc[:,['CTR-females','FLX-females']]
df_median.columns = ['median_'+ str(col) for col in df_median.columns]

df_q25=pd.DataFrame.from_dict({(i,j): dict_q25[i][j] 
                           for i in dict_q25.keys() 
                           for j in dict_q25[i].keys()},
                       orient='index')
df_q25=df_q25.loc[:,['CTR-females','FLX-females']]
df_q25.columns = ['q25_'+ str(col) for col in df_q25.columns]

df_q75=pd.DataFrame.from_dict({(i,j): dict_q75[i][j] 
                           for i in dict_q75.keys() 
                           for j in dict_q75[i].keys()},
                       orient='index')
df_q75=df_q75.loc[:,['CTR-females','FLX-females']]
df_q75.columns = ['q75_'+ str(col) for col in df_q75.columns]

df_std=pd.DataFrame.from_dict({(i,j): dict_std[i][j] 
                           for i in dict_std.keys() 
                           for j in dict_std[i].keys()},
                       orient='index')
df_std=df_std.loc[:,['CTR-females','FLX-females']]
df_std.columns = ['std_'+ str(col) for col in df_std.columns]

df_var=pd.DataFrame.from_dict({(i,j): dict_var[i][j] 
                           for i in dict_var.keys() 
                           for j in dict_var[i].keys()},
                       orient='index')
df_var=df_var.loc[:,['CTR-females','FLX-females']]
df_var.columns = ['var_'+ str(col) for col in df_var.columns]

# Calculate the SEM of the median
# Calculate n per group and squareroot for sem median
npg=10
sqrtn=np.sqrt(npg)*1.34

df_errormedian=pd.concat([df_q25,df_q75], sort=False, axis=1)
df_errormedian['SEM_median_CTR-females']=((df_errormedian['q75_CTR-females']-df_errormedian['q25_CTR-females'])/sqrtn)
df_errormedian['SEM_median_FLX-females']=((df_errormedian['q75_FLX-females']-df_errormedian['q25_FLX-females'])/sqrtn)
df_semedian=df_errormedian.loc[:,['SEM_median_CTR-females','SEM_median_FLX-females']]

df_stat=pd.concat([df_mean,df_sem,df_median,df_semedian,df_std,df_var,df_q25,df_q75], sort=False, axis=1)

# sort the dataframe properly on behavior
df_stat=df_stat.reset_index()
df_stat=df_stat.assign(Behavior =lambda x: df_stat.level_1.str.split('_').str[-1])
df_stat=df_stat.assign(Percentage =lambda x: df_stat.level_1.str.split('_').str[0])
df_stat.columns=['Outcome','Beh_perc', 'mean_CTR-females', 'mean_FLX-females', 'sem_CTR-females',
       'sem_FLX-females', 'median_CTR-females', 'median_FLX-females',
       'SEM_median_CTR-females', 'SEM_median_FLX-females', 'std_CTR-females',
       'std_FLX-females', 'var_CTR-females', 'var_FLX-females',
       'q25_CTR-females', 'q25_FLX-females', 'q75_CTR-females',
       'q75_FLX-females','Behavior', 'Percentage'] 
df_stat=df_stat[['Outcome','Beh_perc', 'Behavior', 'Percentage','mean_CTR-females', 'mean_FLX-females', 'sem_CTR-females',
       'sem_FLX-females', 'median_CTR-females', 'median_FLX-females',
       'SEM_median_CTR-females', 'SEM_median_FLX-females', 'std_CTR-females',
       'std_FLX-females', 'var_CTR-females', 'var_FLX-females',
       'q25_CTR-females', 'q25_FLX-females', 'q75_CTR-females',
       'q75_FLX-females']] 
df_stat=df_stat.set_index('Outcome','Behavior')
df_stat.sort_values(['Percentage'],ascending=[True])

# To make the excel sheet nice
# Make a list of all result dataframes

list_index=[]
for i, name in enumerate(list_mean_titles):
    temp=name.replace('mean_','')
    list_index.append(temp)

list_all=[x for x in list_index if 'all' in x]
list_CB1=[x for x in list_index if 'CB1' in x]
list_CB2=[x for x in list_index if 'CB2' in x]
list_CB3=[x for x in list_index if 'CB3' in x]
list_CB4=[x for x in list_index if 'CB4' in x]
list_CB5=[x for x in list_index if 'CB5' in x]
list_CB6=[x for x in list_index if 'CB6' in x]
list_MAB=[x for x in list_index if 'MAB' in x]

df_stat_all=df_stat.loc[(list_all),:]
df_stat_CB1=df_stat.loc[(list_CB1),:]
df_stat_CB2=df_stat.loc[(list_CB2),:]
df_stat_CB3=df_stat.loc[(list_CB3),:]
df_stat_CB4=df_stat.loc[(list_CB4),:]
df_stat_CB5=df_stat.loc[(list_CB5),:]
df_stat_CB6=df_stat.loc[(list_CB6),:]
df_stat_MAB=df_stat.loc[(list_MAB),:]

# Make lists with right files to write to excel
list_df_results2= list_df_results[:48]
list_df_results_min= list_df_results[48:96]
list_stat=[df_stat_all,df_stat_CB1,df_stat_CB2,df_stat_CB3,df_stat_CB4,df_stat_CB5,df_stat_CB6,df_stat_MAB]

# Make lists with right files to write to excel
list_results= list_results_titles[:48]
list_results_min= list_results_titles[48:96]
list_stat_titles=['df_stat_all','df_stat_CB1','df_stat_CB2','df_stat_CB3','df_stat_CB4','df_stat_CB5','df_stat_CB6',
                  'df_stat_MAB']

list_stat_titles_pre=[]
for z, title in enumerate(list_stat_titles):
    temp=title.replace('df_','')
    list_stat_titles_pre.append(temp)


# now save the data frame to excel
def save_xls(list_dfs, list_titles, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            data_info.to_excel(writer,'data_info')
            name = list_titles[n]
            df.to_excel(writer, name)
        writer.save()

save_xls(list_df_results2,list_results,out_path1)
save_xls(list_df_results_min,list_results_min,out_path2)
save_xls(list_stat,list_stat_titles,out_path5)

# Just to get notification this part is finished
print("everything finished")

