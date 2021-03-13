# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:50:09 2019 update 14-8-2020 run in Python 3.7.3

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
out_path1 = "%s/Output/HN003_results.xlsx" % directory
out_path2 = "%s/Output/HN003_resultspermin.xlsx" % directory
out_path3 = "%s/Output/HN003_resultsmod.xlsx" % directory
out_path4 = "%s/Output/HN003_resultsmodtreat.xlsx" % directory
out_path5 = "%s/Output/HN003_statistics.xlsx" % directory
out_path6 = "%s/Output/HN003_testresults.xlsx" % directory

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
list_resultsheet=(OBS,'Cohort','CB',TREAT,'Start_estrus','End_estrus','Duration_estrus_min',
                            'preferred_male','nr_malepartner','nr_malepartner_mistake')

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
BC='start copualtory bout'
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

## now save the data frame to excel
#writer5 = pd.ExcelWriter(out_path6, engine='xlsxwriter')
#data_CB1.to_excel(writer5, sheet_name='data_CB1')
#data_CB6.to_excel(writer5,sheet_name='data_CB6')
#writer5.save()
#writer5.close()

# Just to get notification this part is finished
print("bouts finished")

# Loop the rest over the dataframes
df_CB=[data_all,data_CB1,data_CB2,data_CB3,data_CB4,data_CB5,data_CB6]
for dt, dataframe in enumerate(df_CB): 
    data=dataframe

    # Calculate total number of each behavior per rat in total environment
    for position, col_name in enumerate(list_behaviors):
        data['TN_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TN_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TN_%s'% col_name]) 
        data['TN_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_num']==1)), data['obs_beh_num_back'], 
            data['TN_%s'% col_name]) 
        data['TN_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TN_%s'% col_name]=np.where(data['TN_%s'% col_name]==99999, np.NaN, data['TN_%s'% col_name])
        data['TN_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TN_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TN_%s'% col_name]==88888)), 
            0,data['TN_%s'% col_name])
        data['TN_%s'% col_name]=np.where(data['TN_%s'% col_name]==88888, np.NaN, data['TN_%s'% col_name])
        data['TN_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TN_%s'% col_name]= np.where(data[BEH]=='None',0,data['TN_%s'% col_name])
    
            
        # Calculate total number of each behavior per rat in burrow
        data['BN_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BN_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BN_%s'% col_name]) 
        data['BN_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_num']==1)&(data[MODLOC]=='Burrow')), 
            data['obs_beh_loc_num_back'], data['BN_%s'% col_name]) 
        data['BN_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BN_%s'% col_name]=np.where(data['BN_%s'% col_name]==99999, np.NaN, data['BN_%s'% col_name])
        data['BN_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BN_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BN_%s'% col_name]==88888)), 
            0,data['BN_%s'% col_name])
        data['BN_%s'% col_name]=np.where(data['BN_%s'% col_name]==88888, np.NaN, data['BN_%s'% col_name])
        data['BN_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BN_%s'% col_name]= np.where(data[BEH]=='None',0,data['BN_%s'% col_name])
    
        # Calculate total number of each behavior per rat in burrow
        data['ON_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ON_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ON_%s'% col_name]) 
        data['ON_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_num']==1)&(data[MODLOC]=='Open field')), 
            data['obs_beh_loc_num_back'], data['ON_%s'% col_name]) 
        data['ON_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ON_%s'% col_name]=np.where(data['ON_%s'% col_name]==99999, np.NaN, data['ON_%s'% col_name])
        data['ON_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ON_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ON_%s'% col_name]==88888)), 
            0,data['ON_%s'% col_name])
        data['ON_%s'% col_name]=np.where(data['ON_%s'% col_name]==88888, np.NaN, data['ON_%s'% col_name])
        data['ON_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ON_%s'% col_name]= np.where(data[BEH]=='None',0,data['ON_%s'% col_name])

    # Calculate the additional behaviors for total environment, burrow, and open field    
    data['TN_%s'% EA]= (data['TN_%s'% BSD]+data['TN_%s'% BSE]+data['TN_%s'% BSF])
    data['TN_%s'% EB]= (data['TN_%s'% BSB]/data['TN_%s'% EA]*100)
    data['TN_%s'% EC]= (data['TN_%s'% BSG]+data['TN_%s'% BSH]+data['TN_%s'% BSI])
    data['TN_%s'% EE]= (data['TN_%s'% BCA]+data['TN_%s'% BCB]+data['TN_%s'% BCC]+data['TN_%s'% BCD])
    data['TN_%s'% EF]= (data['TN_%s'% BSA]+data['TN_%s'% BSB])
    data['TN_%s'% EG]= (data['TN_%s'% EF]/data['TN_%s'% EA]*100)
    
    data['ON_%s'% EA]= (data['ON_%s'% BSD]+data['ON_%s'% BSE]+data['ON_%s'% BSF])
    data['ON_%s'% EB]= (data['ON_%s'% BSB]/data['ON_%s'% EA]*100)
    data['ON_%s'% EC]= (data['ON_%s'% BSG]+data['ON_%s'% BSH]+data['ON_%s'% BSI])
    data['ON_%s'% EE]= (data['ON_%s'% BCA]+data['ON_%s'% BCB]+data['ON_%s'% BCC]+data['ON_%s'% BCD])
    data['ON_%s'% EF]= (data['ON_%s'% BSA]+data['ON_%s'% BSB])
    data['ON_%s'% EG]= (data['ON_%s'% EF]/data['ON_%s'% EA]*100)
    
    data['BN_%s'% EA]= (data['BN_%s'% BSD]+data['BN_%s'% BSE]+data['BN_%s'% BSF])
    data['BN_%s'% EB]= (data['BN_%s'% BSB]/data['BN_%s'% EA]*100)
    data['BN_%s'% EC]= (data['BN_%s'% BSG]+data['BN_%s'% BSH]+data['BN_%s'% BSI])
    data['BN_%s'% EE]= (data['BN_%s'% BCA]+data['BN_%s'% BCB]+data['BN_%s'% BCC]+data['BN_%s'% BCD])
    data['BN_%s'% EF]= (data['BN_%s'% BSA]+data['BN_%s'% BSB])
    data['BN_%s'% EG]= (data['BN_%s'% EF]/data['BN_%s'% EA]*100)

    # Calculate the number of behaviors corrected for time behavioral estrus
    for position, col_name in enumerate(list_behaviors):
        data['TN_min_%s'% col_name]=(data['TN_%s'% col_name]/data['Duration_estrus_min'])
        data['BN_min_%s'% col_name]=(data['BN_%s'% col_name]/data['Duration_estrus_min'])
        data['ON_min_%s'% col_name]=(data['ON_%s'% col_name]/data['Duration_estrus_min'])
        
        data['TN_min_%s'% col_name]=np.where((data['TN_min_%s'% col_name]>0),data['TN_min_%s'% col_name],0)
        data['BN_min_%s'% col_name]=np.where((data['BN_min_%s'% col_name]>0),data['BN_min_%s'% col_name],0)
        data['ON_min_%s'% col_name]=np.where((data['ON_min_%s'% col_name]>0),data['ON_min_%s'% col_name],0)
    
    for position, col_name in enumerate(list_behaviors_extra):
        data['TN_min_%s'% col_name]=(data['TN_%s'% col_name]/data['Duration_estrus_min'])
        data['BN_min_%s'% col_name]=(data['BN_%s'% col_name]/data['Duration_estrus_min'])
        data['ON_min_%s'% col_name]=(data['ON_%s'% col_name]/data['Duration_estrus_min'])
    
        data['TN_min_%s'% col_name]=np.where((data['TN_min_%s'% col_name]>0),data['TN_min_%s'% col_name],0)
        data['BN_min_%s'% col_name]=np.where((data['BN_min_%s'% col_name]>0),data['BN_min_%s'% col_name],0)
        data['ON_min_%s'% col_name]=np.where((data['ON_min_%s'% col_name]>0),data['ON_min_%s'% col_name],0)
    
    # Calculate total number of each "social" behavior directed at FLX-female in total environment
    for position, col_name in enumerate(list_behaviors_social):
        data['TNFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNFF_%s'% col_name]) 
        data['TNFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num']==1)&(data[MODTREAT]=='FLX-females')), 
            data['obs_beh_treat_num_back'], data['TNFF_%s'% col_name]) 
        data['TNFF_%s'% col_name].fillna(method = "ffill", inplace=True)     
        data['TNFF_%s'% col_name]=np.where(data['TNFF_%s'% col_name]==99999, np.NaN, data['TNFF_%s'% col_name])
        data['TNFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNFF_%s'% col_name]==88888)), 
            0,data['TNFF_%s'% col_name])
        data['TNFF_%s'% col_name]=np.where(data['TNFF_%s'% col_name]==88888, np.NaN, data['TNFF_%s'% col_name])
        data['TNFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNFF_%s'% col_name])

        # Calculate total number of each "social" behavior directed at CTR female in total environment
        data['TNCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNCF_%s'% col_name]) 
        data['TNCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num']==1)&(data[MODTREAT]=='CTR-females')), 
            data['obs_beh_treat_num_back'], data['TNCF_%s'% col_name]) 
        data['TNCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNCF_%s'% col_name]=np.where(data['TNCF_%s'% col_name]==99999, np.NaN, data['TNCF_%s'% col_name])
        data['TNCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNCF_%s'% col_name]==88888)), 
            0,data['TNCF_%s'% col_name])
        data['TNCF_%s'% col_name]=np.where(data['TNCF_%s'% col_name]==88888, np.NaN, data['TNCF_%s'% col_name])
        data['TNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNCF_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at FLX male in total environment
        data['TNFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNFM_%s'% col_name]) 
        data['TNFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num']==1)&(data[MODTREAT]=='FLX-males')), 
            data['obs_beh_treat_num_back'], data['TNFM_%s'% col_name]) 
        data['TNFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNFM_%s'% col_name]=np.where(data['TNFM_%s'% col_name]==99999, np.NaN, data['TNFM_%s'% col_name])
        data['TNFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNFM_%s'% col_name]==88888)), 
            0,data['TNFM_%s'% col_name])
        data['TNFM_%s'% col_name]=np.where(data['TNFM_%s'% col_name]==88888, np.NaN, data['TNFM_%s'% col_name])
        data['TNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNFM_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at  CTR male in total environment
        data['TNCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNCM_%s'% col_name]) 
        data['TNCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num']==1)&(data[MODTREAT]=='CTR-males')), 
            data['obs_beh_treat_num_back'], data['TNCM_%s'% col_name]) 
        data['TNCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNCM_%s'% col_name]=np.where(data['TNCM_%s'% col_name]==99999, np.NaN, data['TNCM_%s'% col_name])
        data['TNCM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNCM_%s'% col_name]==88888)), 
            0,data['TNCM_%s'% col_name])
        data['TNCM_%s'% col_name]=np.where(data['TNCM_%s'% col_name]==88888, np.NaN, data['TNCM_%s'% col_name])
        data['TNCM_%s'% col_name].fillna(method = "ffill", inplace=True)
      
        # Calculate total number of each "social" behavior directed at FLX female in burrow
        data['BNFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BNFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BNFF_%s'% col_name]) 
        data['BNFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='FLX-females')&(data[MODLOC]=='Burrow')), data['obs_beh_loc_treat_num_back'], data['BNFF_%s'% col_name]) 
        data['BNFF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BNFF_%s'% col_name]=np.where(data['BNFF_%s'% col_name]==99999, np.NaN, data['BNFF_%s'% col_name])
        data['BNFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BNFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BNFF_%s'% col_name]==88888)), 
            0,data['BNFF_%s'% col_name])
        data['BNFF_%s'% col_name]=np.where(data['BNFF_%s'% col_name]==88888, np.NaN, data['BNFF_%s'% col_name])
        data['BNFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BNFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['BNFF_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at CTR female in burrow
        data['BNCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BNCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BNCF_%s'% col_name]) 
        data['BNCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='CTR-females')&(data[MODLOC]=='Burrow')), data['obs_beh_loc_treat_num_back'], data['BNCF_%s'% col_name]) 
        data['BNCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BNCF_%s'% col_name]=np.where(data['BNCF_%s'% col_name]==99999, np.NaN, data['BNCF_%s'% col_name])
        data['BNCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BNCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BNCF_%s'% col_name]==88888)), 
            0,data['BNCF_%s'% col_name])
        data['BNCF_%s'% col_name]=np.where(data['BNCF_%s'% col_name]==88888, np.NaN, data['BNCF_%s'% col_name])
        data['BNCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BNCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['BNCF_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at FLX male in burrow
        data['BNFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BNFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BNFM_%s'% col_name]) 
        data['BNFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='FLX-males')&(data[MODLOC]=='Burrow')), data['obs_beh_loc_treat_num_back'], data['BNFM_%s'% col_name]) 
        data['BNFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BNFM_%s'% col_name]=np.where(data['BNFM_%s'% col_name]==99999, np.NaN, data['BNFM_%s'% col_name])
        data['BNFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BNFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BNFM_%s'% col_name]==88888)), 
            0,data['BNFM_%s'% col_name])
        data['BNFM_%s'% col_name]=np.where(data['BNFM_%s'% col_name]==88888, np.NaN, data['BNFM_%s'% col_name])
        data['BNFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BNFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['BNFM_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at CTR male in burrow
        data['BNCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BNCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BNCM_%s'% col_name]) 
        data['BNCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='CTR-males')&(data[MODLOC]=='Burrow')),data['obs_beh_loc_treat_num_back'], data['BNCM_%s'% col_name]) 
        data['BNCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BNCM_%s'% col_name]=np.where(data['BNCM_%s'% col_name]==99999, np.NaN, data['BNCM_%s'% col_name])
        data['BNCM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BNCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BNCM_%s'% col_name]==88888)), 
            0,data['BNCM_%s'% col_name])
        data['BNCM_%s'% col_name]=np.where(data['BNCM_%s'% col_name]==88888, np.NaN, data['BNCM_%s'% col_name])
        data['BNCM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BNCM_%s'% col_name]= np.where(data[BEH]=='None',0,data['BNCM_%s'% col_name])
      
        # Calculate total number of each "social" behavior directed at FLX female in open field
        data['ONFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ONFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ONFF_%s'% col_name]) 
        data['ONFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='FLX-females')&(data[MODLOC]=='Open field')), data['obs_beh_loc_treat_num_back'], data['ONFF_%s'% col_name]) 
        data['ONFF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ONFF_%s'% col_name]=np.where(data['ONFF_%s'% col_name]==99999, np.NaN, data['ONFF_%s'% col_name])
        data['ONFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ONFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ONFF_%s'% col_name]==88888)), 
            0,data['ONFF_%s'% col_name])
        data['ONFF_%s'% col_name]=np.where(data['ONFF_%s'% col_name]==88888, np.NaN, data['ONFF_%s'% col_name])
        data['ONFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ONFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['ONFF_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at CTR female in open field
        data['ONCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ONCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ONCF_%s'% col_name]) 
        data['ONCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='CTR-females')&(data[MODLOC]=='Open field')), data['obs_beh_loc_treat_num_back'], data['ONCF_%s'% col_name]) 
        data['ONCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ONCF_%s'% col_name]=np.where(data['ONCF_%s'% col_name]==99999, np.NaN, data['ONCF_%s'% col_name])
        data['ONCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ONCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ONCF_%s'% col_name]==88888)), 
            0,data['ONCF_%s'% col_name])
        data['ONCF_%s'% col_name]=np.where(data['ONCF_%s'% col_name]==88888, np.NaN, data['ONCF_%s'% col_name])
        data['ONCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ONCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['ONCF_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at FLX male in open field
        data['ONFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ONFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ONFM_%s'% col_name]) 
        data['ONFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='FLX-males')&(data[MODLOC]=='Open field')), data['obs_beh_loc_treat_num_back'], data['ONFM_%s'% col_name]) 
        data['ONFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ONFM_%s'% col_name]=np.where(data['ONFM_%s'% col_name]==99999, np.NaN, data['ONFM_%s'% col_name])
        data['ONFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ONFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ONFM_%s'% col_name]==88888)), 
            0,data['ONFM_%s'% col_name])
        data['ONFM_%s'% col_name]=np.where(data['ONFM_%s'% col_name]==88888, np.NaN, data['ONFM_%s'% col_name])
        data['ONFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ONFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['ONFM_%s'% col_name])
    
        # Calculate total number of each "social" behavior directed at CTR male in open field
        data['ONCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ONCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ONCM_%s'% col_name]) 
        data['ONCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num']==1)&
            (data[MODTREAT]=='CTR-males')&(data[MODLOC]=='Open field')),data['obs_beh_loc_treat_num_back'], data['ONCM_%s'% col_name]) 
        data['ONCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ONCM_%s'% col_name]=np.where(data['ONCM_%s'% col_name]==99999, np.NaN, data['ONCM_%s'% col_name])
        data['ONCM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ONCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ONCM_%s'% col_name]==88888)), 
            0,data['ONCM_%s'% col_name])
        data['ONCM_%s'% col_name]=np.where(data['ONCM_%s'% col_name]==88888, np.NaN, data['ONCM_%s'% col_name])
        data['ONCM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ONCM_%s'% col_name]= np.where(data[BEH]=='None',0,data['ONCM_%s'% col_name])
    
    # Calculate the other behaviors for the social behaviors directed at each type of rat
        # In total environment, open field and burrow    
    data['TNFF_%s'% EA]= (data['TNFF_%s'% BSD]+data['TNFF_%s'% BSE]+data['TNFF_%s'% BSF])
    data['TNFF_%s'% EB]= (data['TNFF_%s'% BSB]/data['TNFF_%s'% EA]*100)
    data['TNFF_%s'% EC]= (data['TNFF_%s'% BSG]+data['TNFF_%s'% BSH]+data['TNFF_%s'% BSI])
    data['TNFF_%s'% EE]= (data['TNFF_%s'% BCA]+data['TNFF_%s'% BCB]+data['TNFF_%s'% BCC]+data['TNFF_%s'% BCD])
    data['TNFF_%s'% EF]= (data['TNFF_%s'% BSA]+data['TNFF_%s'% BSB])
    data['TNFF_%s'% EG]= (data['TNFF_%s'% EF]/data['TNFF_%s'% EA]*100)
    
    data['ONFF_%s'% EA]= (data['ONFF_%s'% BSD]+data['ONFF_%s'% BSE]+data['ONFF_%s'% BSF])
    data['ONFF_%s'% EB]= (data['ONFF_%s'% BSB]/data['ONFF_%s'% EA]*100)
    data['ONFF_%s'% EC]= (data['ONFF_%s'% BSG]+data['ONFF_%s'% BSH]+data['ONFF_%s'% BSI])
    data['ONFF_%s'% EE]= (data['ONFF_%s'% BCA]+data['ONFF_%s'% BCB]+data['ONFF_%s'% BCC]+data['ONFF_%s'% BCD])
    data['ONFF_%s'% EF]= (data['ONFF_%s'% BSA]+data['ONFF_%s'% BSB])
    data['ONFF_%s'% EG]= (data['ONFF_%s'% EF]/data['ONFF_%s'% EA]*100)
    
    data['BNFF_%s'% EA]= (data['BNFF_%s'% BSD]+data['BNFF_%s'% BSE]+data['BNFF_%s'% BSF])
    data['BNFF_%s'% EB]= (data['BNFF_%s'% BSB]/data['BNFF_%s'% EA]*100)
    data['BNFF_%s'% EC]= (data['BNFF_%s'% BSG]+data['BNFF_%s'% BSH]+data['BNFF_%s'% BSI])
    data['BNFF_%s'% EE]= (data['BNFF_%s'% BCA]+data['BNFF_%s'% BCB]+data['BNFF_%s'% BCC]+data['BNFF_%s'% BCD])
    data['BNFF_%s'% EF]= (data['BNFF_%s'% BSA]+data['BNFF_%s'% BSB])
    data['BNFF_%s'% EG]= (data['BNFF_%s'% EF]/data['BNFF_%s'% EA]*100)
    
    data['TNCF_%s'% EA]= (data['TNCF_%s'% BSD]+data['TNCF_%s'% BSE]+data['TNCF_%s'% BSF])
    data['TNCF_%s'% EB]= (data['TNCF_%s'% BSB]/data['TNCF_%s'% EA]*100)
    data['TNCF_%s'% EC]= (data['TNCF_%s'% BSG]+data['TNCF_%s'% BSH]+data['TNCF_%s'% BSI])
    data['TNCF_%s'% EE]= (data['TNCF_%s'% BCA]+data['TNCF_%s'% BCB]+data['TNCF_%s'% BCC]+data['TNCF_%s'% BCD])
    data['TNCF_%s'% EF]= (data['TNCF_%s'% BSA]+data['TNCF_%s'% BSB])
    data['TNCF_%s'% EG]= (data['TNCF_%s'% EF]/data['TNCF_%s'% EA]*100)
    
    data['ONCF_%s'% EA]= (data['ONCF_%s'% BSD]+data['ONCF_%s'% BSE]+data['ONCF_%s'% BSF])
    data['ONCF_%s'% EB]= (data['ONCF_%s'% BSB]/data['ONCF_%s'% EA]*100)
    data['ONCF_%s'% EC]= (data['ONCF_%s'% BSG]+data['ONCF_%s'% BSH]+data['ONCF_%s'% BSI])
    data['ONCF_%s'% EE]= (data['ONCF_%s'% BCA]+data['ONCF_%s'% BCB]+data['ONCF_%s'% BCC]+data['ONCF_%s'% BCD])
    data['ONCF_%s'% EF]= (data['ONCF_%s'% BSA]+data['ONCF_%s'% BSB])
    data['ONCF_%s'% EG]= (data['ONCF_%s'% EF]/data['ONCF_%s'% EA]*100)
    
    data['BNCF_%s'% EA]= (data['BNCF_%s'% BSD]+data['BNCF_%s'% BSE]+data['BNCF_%s'% BSF])
    data['BNCF_%s'% EB]= (data['BNCF_%s'% BSB]/data['BNCF_%s'% EA]*100)
    data['BNCF_%s'% EC]= (data['BNCF_%s'% BSG]+data['BNCF_%s'% BSH]+data['BNCF_%s'% BSI])
    data['BNCF_%s'% EE]= (data['BNCF_%s'% BCA]+data['BNCF_%s'% BCB]+data['BNCF_%s'% BCC]+data['BNCF_%s'% BCD])
    data['BNCF_%s'% EF]= (data['BNCF_%s'% BSA]+data['BNCF_%s'% BSB])
    data['BNCF_%s'% EG]= (data['BNCF_%s'% EF]/data['BNCF_%s'% EA]*100)
    
    data['TNFM_%s'% EA]= (data['TNFM_%s'% BSD]+data['TNFM_%s'% BSE]+data['TNFM_%s'% BSF])
    data['TNFM_%s'% EB]= (data['TNFM_%s'% BSB]/data['TNFM_%s'% EA]*100)
    data['TNFM_%s'% EC]= (data['TNFM_%s'% BSG]+data['TNFM_%s'% BSH]+data['TNFM_%s'% BSI])
    data['TNFM_%s'% EE]= (data['TNFM_%s'% BCA]+data['TNFM_%s'% BCB]+data['TNFM_%s'% BCC]+data['TNFM_%s'% BCD])
    data['TNFM_%s'% EF]= (data['TNFM_%s'% BSA]+data['TNFM_%s'% BSB])
    data['TNFM_%s'% EG]= (data['TNFM_%s'% EF]/data['TNFM_%s'% EA]*100)
    
    data['ONFM_%s'% EA]= (data['ONFM_%s'% BSD]+data['ONFM_%s'% BSE]+data['ONFM_%s'% BSF])
    data['ONFM_%s'% EB]= (data['ONFM_%s'% BSB]/data['ONFM_%s'% EA]*100)
    data['ONFM_%s'% EC]= (data['ONFM_%s'% BSG]+data['ONFM_%s'% BSH]+data['ONFM_%s'% BSI])
    data['ONFM_%s'% EE]= (data['ONFM_%s'% BCA]+data['ONFM_%s'% BCB]+data['ONFM_%s'% BCC]+data['ONFM_%s'% BCD])
    data['ONFM_%s'% EF]= (data['ONFM_%s'% BSA]+data['ONFM_%s'% BSB])
    data['ONFM_%s'% EG]= (data['ONFM_%s'% EF]/data['ONFM_%s'% EA]*100)
    
    data['BNFM_%s'% EA]= (data['BNFM_%s'% BSD]+data['BNFM_%s'% BSE]+data['BNFM_%s'% BSF])
    data['BNFM_%s'% EB]= (data['BNFM_%s'% BSB]/data['BNFM_%s'% EA]*100)
    data['BNFM_%s'% EC]= (data['BNFM_%s'% BSG]+data['BNFM_%s'% BSH]+data['BNFM_%s'% BSI])
    data['BNFM_%s'% EE]= (data['BNFM_%s'% BCA]+data['BNFM_%s'% BCB]+data['BNFM_%s'% BCC]+data['BNFM_%s'% BCD])
    data['BNFM_%s'% EF]= (data['BNFM_%s'% BSA]+data['BNFM_%s'% BSB])
    data['BNFM_%s'% EG]= (data['BNFM_%s'% EF]/data['BNFM_%s'% EA]*100)
    
    data['TNCM_%s'% EA]= (data['TNCM_%s'% BSD]+data['TNCM_%s'% BSE]+data['TNCM_%s'% BSF])
    data['TNCM_%s'% EB]= (data['TNCM_%s'% BSB]/data['TNCM_%s'% EA]*100)
    data['TNCM_%s'% EC]= (data['TNCM_%s'% BSG]+data['TNCM_%s'% BSH]+data['TNCM_%s'% BSI])
    data['TNCM_%s'% EE]= (data['TNCM_%s'% BCA]+data['TNCM_%s'% BCB]+data['TNCM_%s'% BCC]+data['TNCM_%s'% BCD])
    data['TNCM_%s'% EF]= (data['TNCM_%s'% BSA]+data['TNCM_%s'% BSB])
    data['TNCM_%s'% EG]= (data['TNCM_%s'% EF]/data['TNCM_%s'% EA]*100)
    
    data['ONCM_%s'% EA]= (data['ONCM_%s'% BSD]+data['ONCM_%s'% BSE]+data['ONCM_%s'% BSF])
    data['ONCM_%s'% EB]= (data['ONCM_%s'% BSB]/data['ONCM_%s'% EA]*100)
    data['ONCM_%s'% EC]= (data['ONCM_%s'% BSG]+data['ONCM_%s'% BSH]+data['ONCM_%s'% BSI])
    data['ONCM_%s'% EE]= (data['ONCM_%s'% BCA]+data['ONCM_%s'% BCB]+data['ONCM_%s'% BCC]+data['ONCM_%s'% BCD])
    data['ONCM_%s'% EF]= (data['ONCM_%s'% BSA]+data['ONCM_%s'% BSB])
    data['ONCM_%s'% EG]= (data['ONCM_%s'% EF]/data['ONCM_%s'% EA]*100)
    
    data['BNCM_%s'% EA]= (data['BNCM_%s'% BSD]+data['BNCM_%s'% BSE]+data['BNCM_%s'% BSF])
    data['BNCM_%s'% EB]= (data['BNCM_%s'% BSB]/data['BNCM_%s'% EA]*100)
    data['BNCM_%s'% EC]= (data['BNCM_%s'% BSG]+data['BNCM_%s'% BSH]+data['BNCM_%s'% BSI])
    data['BNCM_%s'% EE]= (data['BNCM_%s'% BCA]+data['BNCM_%s'% BCB]+data['BNCM_%s'% BCC]+data['BNCM_%s'% BCD])
    data['BNCM_%s'% EF]= (data['BNCM_%s'% BSA]+data['BNCM_%s'% BSB])
    data['BNCM_%s'% EG]= (data['BNCM_%s'% EF]/data['BNCM_%s'% EA]*100)
    
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
    data['TNCR_%s'% EE]=(data['TNCF_%s'% EE]+data['TNCM_%s'% EE])
    data['TNFR_%s'% EE]=(data['TNFF_%s'% EE]+data['TNFM_%s'% EE])
    data['TNCR_%s'% EF]=(data['TNCF_%s'% EF]+data['TNCM_%s'% EF])
    data['TNFR_%s'% EF]=(data['TNFF_%s'% EF]+data['TNFM_%s'% EF])
    data['TNCR_%s'% EG]=(data['TNCF_%s'% EG]+data['TNCM_%s'% EG])
    data['TNFR_%s'% EG]=(data['TNFF_%s'% EG]+data['TNFM_%s'% EG])
    
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
    data['TNM_%s'% EE]=(data['TNCM_%s'% EE]+data['TNFM_%s'% EE])
    data['TNF_%s'% EE]=(data['TNFF_%s'% EE]+data['TNCF_%s'% EE])
    data['TNM_%s'% EF]=(data['TNCM_%s'% EF]+data['TNFM_%s'% EF])
    data['TNF_%s'% EF]=(data['TNFF_%s'% EF]+data['TNCF_%s'% EF])
    data['TNM_%s'% EG]=(data['TNCM_%s'% EG]+data['TNFM_%s'% EG])
    data['TNF_%s'% EG]=(data['TNFF_%s'% EG]+data['TNCF_%s'% EG])
    
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
    data['BNCR_%s'% EE]=(data['BNCF_%s'% EE]+data['BNCM_%s'% EE])
    data['BNFR_%s'% EE]=(data['BNFF_%s'% EE]+data['BNFM_%s'% EE])
    data['BNCR_%s'% EF]=(data['BNCF_%s'% EF]+data['BNCM_%s'% EF])
    data['BNFR_%s'% EF]=(data['BNFF_%s'% EF]+data['BNFM_%s'% EF])
    data['BNCR_%s'% EG]=(data['BNCF_%s'% EG]+data['BNCM_%s'% EG])
    data['BNFR_%s'% EG]=(data['BNFF_%s'% EG]+data['BNFM_%s'% EG])
    
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
    data['BNM_%s'% EE]=(data['BNCM_%s'% EE]+data['BNFM_%s'% EE])
    data['BNF_%s'% EE]=(data['BNFF_%s'% EE]+data['BNCF_%s'% EE])
    data['BNM_%s'% EF]=(data['BNCM_%s'% EF]+data['BNFM_%s'% EF])
    data['BNF_%s'% EF]=(data['BNFF_%s'% EF]+data['BNCF_%s'% EF])
    data['BNM_%s'% EG]=(data['BNCM_%s'% EG]+data['BNFM_%s'% EG])
    data['BNF_%s'% EG]=(data['BNFF_%s'% EG]+data['BNCF_%s'% EG])
    
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
    data['ONCR_%s'% EE]=(data['ONCF_%s'% EE]+data['ONCM_%s'% EE])
    data['ONFR_%s'% EE]=(data['ONFF_%s'% EE]+data['ONFM_%s'% EE])
    data['ONCR_%s'% EF]=(data['ONCF_%s'% EF]+data['ONCM_%s'% EF])
    data['ONFR_%s'% EF]=(data['ONFF_%s'% EF]+data['ONFM_%s'% EF])
    data['ONCR_%s'% EG]=(data['ONCF_%s'% EG]+data['ONCM_%s'% EG])
    data['ONFR_%s'% EG]=(data['ONFF_%s'% EG]+data['ONFM_%s'% EG])
    
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
    data['ONM_%s'% EE]=(data['ONCM_%s'% EE]+data['ONFM_%s'% EE])
    data['ONF_%s'% EE]=(data['ONFF_%s'% EE]+data['ONCF_%s'% EE])
    data['ONM_%s'% EF]=(data['ONCM_%s'% EF]+data['ONFM_%s'% EF])
    data['ONF_%s'% EF]=(data['ONFF_%s'% EF]+data['ONCF_%s'% EF])
    data['ONM_%s'% EG]=(data['ONCM_%s'% EG]+data['ONFM_%s'% EG])
    data['ONF_%s'% EG]=(data['ONFF_%s'% EG]+data['ONCF_%s'% EG])

    # Calculate total duration of each behavior per rat in total environment
    for position, col_name in enumerate(list_behaviors): 
        data['TD_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TD_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TD_%s'% col_name]) 
        data['TD_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_num_back']==1)), data['obs_beh_sumdur'], 
            data['TD_%s'% col_name]) 
        data['TD_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TD_%s'% col_name]=np.where(data['TD_%s'% col_name]==99999, np.NaN, data['TD_%s'% col_name])
        data['TD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TD_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TD_%s'% col_name]==88888)), 
            0,data['TD_%s'% col_name])
        data['TD_%s'% col_name]=np.where(data['TD_%s'% col_name]==88888, np.NaN, data['TD_%s'% col_name])
        data['TD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TD_%s'% col_name]= np.where(data[BEH]=='None',0,data['TD_%s'% col_name])
    
        # Calculate total duration of each behavior per rat in burrow
        data['BD_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BD_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BD_%s'% col_name]) 
        data['BD_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_num_back']==1)&(data[MODLOC]=='Burrow')), data['obs_beh_loc_sumdur'], 
            data['BD_%s'% col_name]) 
        data['BD_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BD_%s'% col_name]=np.where(data['BD_%s'% col_name]==99999, np.NaN, data['BD_%s'% col_name])
        data['BD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BD_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BD_%s'% col_name]==88888)), 
            0,data['BD_%s'% col_name])
        data['BD_%s'% col_name]=np.where(data['BD_%s'% col_name]==88888, np.NaN, data['BD_%s'% col_name])
        data['BD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BD_%s'% col_name]= np.where(data[BEH]=='None',0,data['BD_%s'% col_name])
    
        # Calculate total duration of each behavior per rat in open field
        data['OD_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['OD_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['OD_%s'% col_name]) 
        data['OD_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_num_back']==1)&(data[MODLOC]=='Open field')), data['obs_beh_loc_sumdur'], 
            data['OD_%s'% col_name]) 
        data['OD_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['OD_%s'% col_name]=np.where(data['OD_%s'% col_name]==99999, np.NaN, data['OD_%s'% col_name])
        data['OD_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['OD_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['OD_%s'% col_name]==88888)), 
            0,data['OD_%s'% col_name])
        data['OD_%s'% col_name]=np.where(data['OD_%s'% col_name]==88888, np.NaN, data['OD_%s'% col_name])
        data['OD_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['OD_%s'% col_name]= np.where(data[BEH]=='None',0,data['OD_%s'% col_name])
    
    # Calculate the other behaviors
    data['TD_%s'% EA]= (data['TD_%s'% BSD]+data['TD_%s'% BSE]+data['TD_%s'% BSF])
    data['TD_%s'% EB]= (data['TD_%s'% BSB]/data['TD_%s'% EA]*100)
    data['TD_%s'% EC]= (data['TD_%s'% BSG]+data['TD_%s'% BSH]+data['TD_%s'% BSI])
    data['TD_%s'% EE]= (data['TD_%s'% BCA]+data['TD_%s'% BCB]+data['TD_%s'% BCC]+data['TD_%s'% BCD])
    data['TD_%s'% EF]= (data['TD_%s'% BSA]+data['TD_%s'% BSB])
    data['TD_%s'% EG]= (data['TD_%s'% EF]/data['TD_%s'% EA]*100)
    
    data['OD_%s'% EA]= (data['OD_%s'% BSD]+data['OD_%s'% BSE]+data['OD_%s'% BSF])
    data['OD_%s'% EB]= (data['OD_%s'% BSB]/data['OD_%s'% EA]*100)
    data['OD_%s'% EC]= (data['OD_%s'% BSG]+data['OD_%s'% BSH]+data['OD_%s'% BSI])
    data['OD_%s'% EE]= (data['OD_%s'% BCA]+data['OD_%s'% BCB]+data['OD_%s'% BCC]+data['OD_%s'% BCD])
    data['OD_%s'% EF]= (data['OD_%s'% BSA]+data['OD_%s'% BSB])
    data['OD_%s'% EG]= (data['OD_%s'% EF]/data['OD_%s'% EA]*100)
    
    data['BD_%s'% EA]= (data['BD_%s'% BSD]+data['BD_%s'% BSE]+data['BD_%s'% BSF])
    data['BD_%s'% EB]= (data['BD_%s'% BSB]/data['BD_%s'% EA]*100)
    data['BD_%s'% EC]= (data['BD_%s'% BSG]+data['BD_%s'% BSH]+data['BD_%s'% BSI])
    data['BD_%s'% EE]= (data['BD_%s'% BCA]+data['BD_%s'% BCB]+data['BD_%s'% BCC]+data['BD_%s'% BCD])
    data['BD_%s'% EF]= (data['BD_%s'% BSA]+data['BD_%s'% BSB])
    data['BD_%s'% EG]= (data['BD_%s'% EF]/data['BD_%s'% EA]*100)
    
    # Calculate the durations of behaviors corrected for time behavioral estrus
    for position, col_name in enumerate(list_behaviors): 
        data['TD_min_%s'% col_name]=(data['TD_%s'% col_name]/data['Duration_estrus_min'])
        data['BD_min_%s'% col_name]=(data['BD_%s'% col_name]/data['Duration_estrus_min'])
        data['OD_min_%s'% col_name]=(data['OD_%s'% col_name]/data['Duration_estrus_min'])
    
        data['TD_min_%s'% col_name]=np.where((data['TD_min_%s'% col_name]>0),data['TD_min_%s'% col_name],0)
        data['BD_min_%s'% col_name]=np.where((data['BD_min_%s'% col_name]>0),data['BD_min_%s'% col_name],0)
        data['OD_min_%s'% col_name]=np.where((data['OD_min_%s'% col_name]>0),data['OD_min_%s'% col_name],0)
    
    for position, col_name in enumerate(list_behaviors_extra): 
        data['TD_min_%s'% col_name]=(data['TD_%s'% col_name]/data['Duration_estrus_min'])
        data['BD_min_%s'% col_name]=(data['BD_%s'% col_name]/data['Duration_estrus_min'])
        data['OD_min_%s'% col_name]=(data['OD_%s'% col_name]/data['Duration_estrus_min'])
    
        data['TD_min_%s'% col_name]=np.where((data['TD_min_%s'% col_name]>0),data['TD_min_%s'% col_name],0)
        data['BD_min_%s'% col_name]=np.where((data['BD_min_%s'% col_name]>0),data['BD_min_%s'% col_name],0)
        data['OD_min_%s'% col_name]=np.where((data['OD_min_%s'% col_name]>0),data['OD_min_%s'% col_name],0)
    
    # Calculate total duration of each "social" behavior directed at FLX-female in total environment
    for position, col_name in enumerate(list_behaviors_social): 
        data['TDFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDFF_%s'% col_name]) 
        data['TDFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num_back']==1)&(data[MODTREAT]=='FLX-females')),
            data['obs_beh_treat_sumdur'], data['TDFF_%s'% col_name]) 
        data['TDFF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDFF_%s'% col_name]=np.where(data['TDFF_%s'% col_name]==99999, np.NaN, data['TDFF_%s'% col_name])
        data['TDFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDFF_%s'% col_name]==88888)), 
            0,data['TDFF_%s'% col_name])
        data['TDFF_%s'% col_name]=np.where(data['TDFF_%s'% col_name]==88888, np.NaN, data['TDFF_%s'% col_name])
        data['TDFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDFF_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-females in total environment
        data['TDCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDCF_%s'% col_name]) 
        data['TDCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num_back']==1)&(data[MODTREAT]=='CTR-females')),
            data['obs_beh_treat_sumdur'], data['TDCF_%s'% col_name]) 
        data['TDCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDCF_%s'% col_name]=np.where(data['TDCF_%s'% col_name]==99999, np.NaN, data['TDCF_%s'% col_name])
        data['TDCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDCF_%s'% col_name]==88888)), 
            0,data['TDCF_%s'% col_name])
        data['TDCF_%s'% col_name]=np.where(data['TDCF_%s'% col_name]==88888, np.NaN, data['TDCF_%s'% col_name])
        data['TDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDCF_%s'% col_name])
        
        # Calculate total duration of each "social" behavior directed at FLX-male in total environment
        data['TDFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDFM_%s'% col_name]) 
        data['TDFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num_back']==1)&(data[MODTREAT]=='FLX-males')),
            data['obs_beh_treat_sumdur'], data['TDFM_%s'% col_name]) 
        data['TDFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDFM_%s'% col_name]=np.where(data['TDFM_%s'% col_name]==99999, np.NaN, data['TDFM_%s'% col_name])
        data['TDFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDFM_%s'% col_name]==88888)), 
            0,data['TDFM_%s'% col_name])
        data['TDFM_%s'% col_name]=np.where(data['TDFM_%s'% col_name]==88888, np.NaN, data['TDFM_%s'% col_name])
        data['TDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDFM_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-males in total environment
        data['TDCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDCM_%s'% col_name]) 
        data['TDCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_treat_num_back']==1)&(data[MODTREAT]=='CTR-males')),
            data['obs_beh_treat_sumdur'], data['TDCM_%s'% col_name]) 
        data['TDCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDCM_%s'% col_name]=np.where(data['TDCM_%s'% col_name]==99999, np.NaN, data['TDCM_%s'% col_name])
        data['TDCM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDCM_%s'% col_name]==88888)), 
            0,data['TDCM_%s'% col_name])
        data['TDCM_%s'% col_name]=np.where(data['TDCM_%s'% col_name]==88888, np.NaN, data['TDCM_%s'% col_name])
        data['TDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDCM_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDCM_%s'% col_name])
    
        # Calculate total duration of each "social" behavior directed at FLX-female in burrow
        data['BDFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BDFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BDFF_%s'% col_name]) 
        data['BDFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='FLX-females')&(data[MODLOC]=='Burrow')),
            data['obs_beh_loc_treat_sumdur'], data['BDFF_%s'% col_name]) 
        data['BDFF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BDFF_%s'% col_name]=np.where(data['BDFF_%s'% col_name]==99999, np.NaN, data['BDFF_%s'% col_name])
        data['BDFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BDFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BDFF_%s'% col_name]==88888)), 
            0,data['BDFF_%s'% col_name])
        data['BDFF_%s'% col_name]=np.where(data['BDFF_%s'% col_name]==88888, np.NaN, data['BDFF_%s'% col_name])
        data['BDFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BDFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['BDFF_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-females in burrow
        data['BDCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BDCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BDCF_%s'% col_name]) 
        data['BDCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='CTR-females')&(data[MODLOC]=='Burrow')),
            data['obs_beh_loc_treat_sumdur'], data['BDCF_%s'% col_name]) 
        data['BDCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BDCF_%s'% col_name]=np.where(data['BDCF_%s'% col_name]==99999, np.NaN, data['BDCF_%s'% col_name])
        data['BDCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BDCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BDCF_%s'% col_name]==88888)), 
            0,data['BDCF_%s'% col_name])
        data['BDCF_%s'% col_name]=np.where(data['BDCF_%s'% col_name]==88888, np.NaN, data['BDCF_%s'% col_name])
        data['BDCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BDCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['BDCF_%s'% col_name])
        
        # Calculate total duration of each "social" behavior directed at FLX-male in burrow
        data['BDFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BDFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BDFM_%s'% col_name]) 
        data['BDFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='FLX-males')&(data[MODLOC]=='Burrow')),
            data['obs_beh_loc_treat_sumdur'], data['BDFM_%s'% col_name]) 
        data['BDFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BDFM_%s'% col_name]=np.where(data['BDFM_%s'% col_name]==99999, np.NaN, data['BDFM_%s'% col_name])
        data['BDFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BDFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BDFM_%s'% col_name]==88888)), 
            0,data['BDFM_%s'% col_name])
        data['BDFM_%s'% col_name]=np.where(data['BDFM_%s'% col_name]==88888, np.NaN, data['BDFM_%s'% col_name])
        data['BDFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BDFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['BDFM_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-males in burrow
        data['BDCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['BDCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['BDCM_%s'% col_name]) 
        data['BDCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='CTR-males')&(data[MODLOC]=='Burrow')),
            data['obs_beh_loc_treat_sumdur'], data['BDCM_%s'% col_name]) 
        data['BDCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['BDCM_%s'% col_name]=np.where(data['BDCM_%s'% col_name]==99999, np.NaN, data['BDCM_%s'% col_name])
        data['BDCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['BDCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['BDCM_%s'% col_name]==88888)), 
            0,data['BDCM_%s'% col_name])
        data['BDCM_%s'% col_name]=np.where(data['BDCM_%s'% col_name]==88888, np.NaN, data['BDCM_%s'% col_name])
        data['BDCM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['BDCM_%s'% col_name]= np.where(data[BEH]=='None',0,data['BDCM_%s'% col_name])
    
        # Calculate total duration of each "social" behavior directed at FLX-female in open field
        data['ODFF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ODFF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ODFF_%s'% col_name]) 
        data['ODFF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='FLX-females')&(data[MODLOC]=='Open field')),
            data['obs_beh_loc_treat_sumdur'], data['ODFF_%s'% col_name]) 
        data['ODFF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ODFF_%s'% col_name]=np.where(data['ODFF_%s'% col_name]==99999, np.NaN, data['ODFF_%s'% col_name])
        data['ODFF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ODFF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ODFF_%s'% col_name]==88888)), 
            0,data['ODFF_%s'% col_name])
        data['ODFF_%s'% col_name]=np.where(data['ODFF_%s'% col_name]==88888, np.NaN, data['ODFF_%s'% col_name])
        data['ODFF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ODFF_%s'% col_name]= np.where(data[BEH]=='None',0,data['ODFF_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-females in open field
        data['ODCF_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ODCF_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ODCF_%s'% col_name]) 
        data['ODCF_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='CTR-females')&(data[MODLOC]=='Open field')),
            data['obs_beh_loc_treat_sumdur'], data['ODCF_%s'% col_name]) 
        data['ODCF_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ODCF_%s'% col_name]=np.where(data['ODCF_%s'% col_name]==99999, np.NaN, data['ODCF_%s'% col_name])
        data['ODCF_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ODCF_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ODCF_%s'% col_name]==88888)), 
            0,data['ODCF_%s'% col_name])
        data['ODCF_%s'% col_name]=np.where(data['ODCF_%s'% col_name]==88888, np.NaN, data['ODCF_%s'% col_name])
        data['ODCF_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ODCF_%s'% col_name]= np.where(data[BEH]=='None',0,data['ODCF_%s'% col_name])
        
        # Calculate total duration of each "social" behavior directed at FLX-male in open field
        data['ODFM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ODFM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ODFM_%s'% col_name]) 
        data['ODFM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='FLX-males')&(data[MODLOC]=='Open field')),
            data['obs_beh_loc_treat_sumdur'], data['ODFM_%s'% col_name]) 
        data['ODFM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ODFM_%s'% col_name]=np.where(data['ODFM_%s'% col_name]==99999, np.NaN, data['ODFM_%s'% col_name])
        data['ODFM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ODFM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ODFM_%s'% col_name]==88888)), 
            0,data['ODFM_%s'% col_name])
        data['ODFM_%s'% col_name]=np.where(data['ODFM_%s'% col_name]==88888, np.NaN, data['ODFM_%s'% col_name])
        data['ODFM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ODFM_%s'% col_name]= np.where(data[BEH]=='None',0,data['ODFM_%s'% col_name])
        
            # Calculate total duration of each "social" behavior directed at CTR-males in open field
        data['ODCM_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['ODCM_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['ODCM_%s'% col_name]) 
        data['ODCM_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_loc_treat_num_back']==1)&(data[MODTREAT]=='CTR-males')&(data[MODLOC]=='Open field')),
            data['obs_beh_loc_treat_sumdur'], data['ODCM_%s'% col_name]) 
        data['ODCM_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['ODCM_%s'% col_name]=np.where(data['ODCM_%s'% col_name]==99999, np.NaN, data['ODCM_%s'% col_name])
        data['ODCM_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['ODCM_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['ODCM_%s'% col_name]==88888)), 
            0,data['ODCM_%s'% col_name])
        data['ODCM_%s'% col_name]=np.where(data['ODCM_%s'% col_name]==88888, np.NaN, data['ODCM_%s'% col_name])
        data['ODCM_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['ODCM_%s'% col_name]= np.where(data[BEH]=='None',0,data['ODCM_%s'% col_name])
    
    # Calculate the duration of other behaviors for the social behaviors directed at each type of rat
        # In total environment, burrow and open field    
    data['TDFF_%s'% EA]= (data['TDFF_%s'% BSD]+data['TDFF_%s'% BSE]+data['TDFF_%s'% BSF])
    data['TDFF_%s'% EB]= (data['TDFF_%s'% BSB]/data['TDFF_%s'% EA]*100)
    data['TDFF_%s'% EC]= (data['TDFF_%s'% BSG]+data['TDFF_%s'% BSH]+data['TDFF_%s'% BSI])
    data['TDFF_%s'% EE]= (data['TDFF_%s'% BCA]+data['TDFF_%s'% BCB]+data['TDFF_%s'% BCC]+data['TDFF_%s'% BCD])
    data['TDFF_%s'% EF]= (data['TDFF_%s'% BSA]+data['TDFF_%s'% BSB])
    data['TDFF_%s'% EG]= (data['TDFF_%s'% EF]/data['TDFF_%s'% EA]*100)
    
    data['ODFF_%s'% EA]= (data['ODFF_%s'% BSD]+data['ODFF_%s'% BSE]+data['ODFF_%s'% BSF])
    data['ODFF_%s'% EB]= (data['ODFF_%s'% BSB]/data['ODFF_%s'% EA]*100)
    data['ODFF_%s'% EC]= (data['ODFF_%s'% BSG]+data['ODFF_%s'% BSH]+data['ODFF_%s'% BSI])
    data['ODFF_%s'% EE]= (data['ODFF_%s'% BCA]+data['ODFF_%s'% BCB]+data['ODFF_%s'% BCC]+data['ODFF_%s'% BCD])
    data['ODFF_%s'% EF]= (data['ODFF_%s'% BSA]+data['ODFF_%s'% BSB])
    data['ODFF_%s'% EG]= (data['ODFF_%s'% EF]/data['ODFF_%s'% EA]*100)
    
    data['BDFF_%s'% EA]= (data['BDFF_%s'% BSD]+data['BDFF_%s'% BSE]+data['BDFF_%s'% BSF])
    data['BDFF_%s'% EB]= (data['BDFF_%s'% BSB]/data['BDFF_%s'% EA]*100)
    data['BDFF_%s'% EC]= (data['BDFF_%s'% BSG]+data['BDFF_%s'% BSH]+data['BDFF_%s'% BSI])
    data['BDFF_%s'% EE]= (data['BDFF_%s'% BCA]+data['BDFF_%s'% BCB]+data['BDFF_%s'% BCC]+data['BDFF_%s'% BCD])
    data['BDFF_%s'% EF]= (data['BDFF_%s'% BSA]+data['BDFF_%s'% BSB])
    data['BDFF_%s'% EG]= (data['BDFF_%s'% EF]/data['BDFF_%s'% EA]*100)
    
    data['TDCF_%s'% EA]= (data['TDCF_%s'% BSD]+data['TDCF_%s'% BSE]+data['TDCF_%s'% BSF])
    data['TDCF_%s'% EB]= (data['TDCF_%s'% BSB]/data['TDCF_%s'% EA]*100)
    data['TDCF_%s'% EC]= (data['TDCF_%s'% BSG]+data['TDCF_%s'% BSH]+data['TDCF_%s'% BSI])
    data['TDCF_%s'% EE]= (data['TDCF_%s'% BCA]+data['TDCF_%s'% BCB]+data['TDCF_%s'% BCC]+data['TDCF_%s'% BCD])
    data['TDCF_%s'% EF]= (data['TDCF_%s'% BSA]+data['TDCF_%s'% BSB])
    data['TDCF_%s'% EG]= (data['TDCF_%s'% EF]/data['TDCF_%s'% EA]*100)
    
    data['ODCF_%s'% EA]= (data['ODCF_%s'% BSD]+data['ODCF_%s'% BSE]+data['ODCF_%s'% BSF])
    data['ODCF_%s'% EB]= (data['ODCF_%s'% BSB]/data['ODCF_%s'% EA]*100)
    data['ODCF_%s'% EC]= (data['ODCF_%s'% BSG]+data['ODCF_%s'% BSH]+data['ODCF_%s'% BSI])
    data['ODCF_%s'% EE]= (data['ODCF_%s'% BCA]+data['ODCF_%s'% BCB]+data['ODCF_%s'% BCC]+data['ODCF_%s'% BCD])
    data['ODCF_%s'% EF]= (data['ODCF_%s'% BSA]+data['ODCF_%s'% BSB])
    data['ODCF_%s'% EG]= (data['ODCF_%s'% EF]/data['ODCF_%s'% EA]*100)
    
    data['BDCF_%s'% EA]= (data['BDCF_%s'% BSD]+data['BDCF_%s'% BSE]+data['BDCF_%s'% BSF])
    data['BDCF_%s'% EB]= (data['BDCF_%s'% BSB]/data['BDCF_%s'% EA]*100)
    data['BDCF_%s'% EC]= (data['BDCF_%s'% BSG]+data['BDCF_%s'% BSH]+data['BDCF_%s'% BSI])
    data['BDCF_%s'% EE]= (data['BDCF_%s'% BCA]+data['BDCF_%s'% BCB]+data['BDCF_%s'% BCC]+data['BDCF_%s'% BCD])
    data['BDCF_%s'% EF]= (data['BDCF_%s'% BSA]+data['BDCF_%s'% BSB])
    data['BDCF_%s'% EG]= (data['BDCF_%s'% EF]/data['BDCF_%s'% EA]*100)
    
    data['TDFM_%s'% EA]= (data['TDFM_%s'% BSD]+data['TDFM_%s'% BSE]+data['TDFM_%s'% BSF])
    data['TDFM_%s'% EB]= (data['TDFM_%s'% BSB]/data['TDFM_%s'% EA]*100)
    data['TDFM_%s'% EC]= (data['TDFM_%s'% BSG]+data['TDFM_%s'% BSH]+data['TDFM_%s'% BSI])
    data['TDFM_%s'% EE]= (data['TDFM_%s'% BCA]+data['TDFM_%s'% BCB]+data['TDFM_%s'% BCC]+data['TDFM_%s'% BCD])
    data['TDFM_%s'% EF]= (data['TDFM_%s'% BSA]+data['TDFM_%s'% BSB])
    data['TDFM_%s'% EG]= (data['TDFM_%s'% EF]/data['TDFM_%s'% EA]*100)
    
    data['ODFM_%s'% EA]= (data['ODFM_%s'% BSD]+data['ODFM_%s'% BSE]+data['ODFM_%s'% BSF])
    data['ODFM_%s'% EB]= (data['ODFM_%s'% BSB]/data['ODFM_%s'% EA]*100)
    data['ODFM_%s'% EC]= (data['ODFM_%s'% BSG]+data['ODFM_%s'% BSH]+data['ODFM_%s'% BSI])
    data['ODFM_%s'% EE]= (data['ODFM_%s'% BCA]+data['ODFM_%s'% BCB]+data['ODFM_%s'% BCC]+data['ODFM_%s'% BCD])
    data['ODFM_%s'% EF]= (data['ODFM_%s'% BSA]+data['ODFM_%s'% BSB])
    data['ODFM_%s'% EG]= (data['ODFM_%s'% EF]/data['ODFM_%s'% EA]*100)
    
    data['BDFM_%s'% EA]= (data['BDFM_%s'% BSD]+data['BDFM_%s'% BSE]+data['BDFM_%s'% BSF])
    data['BDFM_%s'% EB]= (data['BDFM_%s'% BSB]/data['BDFM_%s'% EA]*100)
    data['BDFM_%s'% EC]= (data['BDFM_%s'% BSG]+data['BDFM_%s'% BSH]+data['BDFM_%s'% BSI])
    data['BDFM_%s'% EE]= (data['BDFM_%s'% BCA]+data['BDFM_%s'% BCB]+data['BDFM_%s'% BCC]+data['BDFM_%s'% BCD])
    data['BDFM_%s'% EF]= (data['BDFM_%s'% BSA]+data['BDFM_%s'% BSB])
    data['BDFM_%s'% EG]= (data['BDFM_%s'% EF]/data['BDFM_%s'% EA]*100)
    
    data['TDCM_%s'% EA]= (data['TDCM_%s'% BSD]+data['TDCM_%s'% BSE]+data['TDCM_%s'% BSF])
    data['TDCM_%s'% EB]= (data['TDCM_%s'% BSB]/data['TDCM_%s'% EA]*100)
    data['TDCM_%s'% EC]= (data['TDCM_%s'% BSG]+data['TDCM_%s'% BSH]+data['TDCM_%s'% BSI])
    data['TDCM_%s'% EE]= (data['TDCM_%s'% BCA]+data['TDCM_%s'% BCB]+data['TDCM_%s'% BCC]+data['TDCM_%s'% BCD])
    data['TDCM_%s'% EF]= (data['TDCM_%s'% BSA]+data['TDCM_%s'% BSB])
    data['TDCM_%s'% EG]= (data['TDCM_%s'% EF]/data['TDCM_%s'% EA]*100)
    
    data['ODCM_%s'% EA]= (data['ODCM_%s'% BSD]+data['ODCM_%s'% BSE]+data['ODCM_%s'% BSF])
    data['ODCM_%s'% EB]= (data['ODCM_%s'% BSB]/data['ODCM_%s'% EA]*100)
    data['ODCM_%s'% EC]= (data['ODCM_%s'% BSG]+data['ODCM_%s'% BSH]+data['ODCM_%s'% BSI])
    data['ODCM_%s'% EE]= (data['ODCM_%s'% BCA]+data['ODCM_%s'% BCB]+data['ODCM_%s'% BCC]+data['ODCM_%s'% BCD])
    data['ODCM_%s'% EF]= (data['ODCM_%s'% BSA]+data['ODCM_%s'% BSB])
    data['ODCM_%s'% EG]= (data['ODCM_%s'% EF]/data['ODCM_%s'% EA]*100)
    
    data['BDCM_%s'% EA]= (data['BDCM_%s'% BSD]+data['BDCM_%s'% BSE]+data['BDCM_%s'% BSF])
    data['BDCM_%s'% EB]= (data['BDCM_%s'% BSB]/data['BDCM_%s'% EA]*100)
    data['BDCM_%s'% EC]= (data['BDCM_%s'% BSG]+data['BDCM_%s'% BSH]+data['BDCM_%s'% BSI])
    data['BDCM_%s'% EE]= (data['BDCM_%s'% BCA]+data['BDCM_%s'% BCB]+data['BDCM_%s'% BCC]+data['BDCM_%s'% BCD])
    data['BDCM_%s'% EF]= (data['BDCM_%s'% BSA]+data['BDCM_%s'% BSB])
    data['BDCM_%s'% EG]= (data['BDCM_%s'% EF]/data['BDCM_%s'% EA]*100)
        
    # Calculate total duration of each "social" behavior directed at CTR-rats and FLX-rats
    # in total environment
    for position, col_name in enumerate(list_behaviors_social): 
        data['TDCR_%s'% col_name]=(data['TDCF_%s'% col_name]+data['TDCM_%s'% col_name])
        data['TDFR_%s'% col_name]=(data['TDFF_%s'% col_name]+data['TDFM_%s'% col_name])
    
    data['TDCR_%s'% EA]=(data['TDCF_%s'% EA]+data['TDCM_%s'% EA])
    data['TDFR_%s'% EA]=(data['TDFF_%s'% EA]+data['TDFM_%s'% EA])
    data['TDCR_%s'% EB]=(data['TDCF_%s'% EB]+data['TDCM_%s'% EB])
    data['TDFR_%s'% EB]=(data['TDFF_%s'% EB]+data['TDFM_%s'% EB])
    data['TDCR_%s'% EC]=(data['TDCF_%s'% EC]+data['TDCM_%s'% EC])
    data['TDFR_%s'% EC]=(data['TDFF_%s'% EC]+data['TDFM_%s'% EC])
    data['TDCR_%s'% EE]=(data['TDCF_%s'% EE]+data['TDCM_%s'% EE])
    data['TDFR_%s'% EE]=(data['TDFF_%s'% EE]+data['TDFM_%s'% EE])
    data['TDCR_%s'% EF]=(data['TDCF_%s'% EF]+data['TDCM_%s'% EF])
    data['TDFR_%s'% EF]=(data['TDFF_%s'% EF]+data['TDFM_%s'% EF])
    data['TDCR_%s'% EG]=(data['TDCF_%s'% EG]+data['TDCM_%s'% EG])
    data['TDFR_%s'% EG]=(data['TDFF_%s'% EG]+data['TDFM_%s'% EG])
    
    # Calculate total duration of each "social" behavior directed at MALES and FEMALES
    # in total environment
    for position, col_name in enumerate(list_behaviors_social): 
        data['TDM_%s'% col_name]=(data['TDCM_%s'% col_name]+data['TDFM_%s'% col_name])
        data['TDF_%s'% col_name]=(data['TDFF_%s'% col_name]+data['TDCF_%s'% col_name])
    
    data['TDM_%s'% EA]=(data['TDCM_%s'% EA]+data['TDFM_%s'% EA])
    data['TDF_%s'% EA]=(data['TDFF_%s'% EA]+data['TDCF_%s'% EA])
    data['TDM_%s'% EB]=(data['TDCM_%s'% EB]+data['TDFM_%s'% EB])
    data['TDF_%s'% EB]=(data['TDFF_%s'% EB]+data['TDCF_%s'% EB])
    data['TDM_%s'% EC]=(data['TDCM_%s'% EC]+data['TDFM_%s'% EC])
    data['TDF_%s'% EC]=(data['TDFF_%s'% EC]+data['TDCF_%s'% EC])
    data['TDM_%s'% EE]=(data['TDCM_%s'% EE]+data['TDFM_%s'% EE])
    data['TDF_%s'% EE]=(data['TDFF_%s'% EE]+data['TDCF_%s'% EE])
    data['TDM_%s'% EF]=(data['TDCM_%s'% EF]+data['TDFM_%s'% EF])
    data['TDF_%s'% EF]=(data['TDFF_%s'% EF]+data['TDCF_%s'% EF])
    data['TDM_%s'% EG]=(data['TDCM_%s'% EG]+data['TDFM_%s'% EG])
    data['TDF_%s'% EG]=(data['TDFF_%s'% EG]+data['TDCF_%s'% EG])
    
    # Calculate total duration of each "social" behavior directed at CTR-rats and FLX-rats
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
    data['BDCR_%s'% EE]=(data['BDCF_%s'% EE]+data['BDCM_%s'% EE])
    data['BDFR_%s'% EE]=(data['BDFF_%s'% EE]+data['BDFM_%s'% EE])
    data['BDCR_%s'% EF]=(data['BDCF_%s'% EF]+data['BDCM_%s'% EF])
    data['BDFR_%s'% EF]=(data['BDFF_%s'% EF]+data['BDFM_%s'% EF])
    data['BDCR_%s'% EG]=(data['BDCF_%s'% EG]+data['BDCM_%s'% EG])
    data['BDFR_%s'% EG]=(data['BDFF_%s'% EG]+data['BDFM_%s'% EG])
    
    # Calculate total duration of each "social" behavior directed at MALES and FEMALES
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
    data['BDM_%s'% EE]=(data['BDCM_%s'% EE]+data['BDFM_%s'% EE])
    data['BDF_%s'% EE]=(data['BDFF_%s'% EE]+data['BDCF_%s'% EE])
    data['BDM_%s'% EF]=(data['BDCM_%s'% EF]+data['BDFM_%s'% EF])
    data['BDF_%s'% EF]=(data['BDFF_%s'% EF]+data['BDCF_%s'% EF])
    data['BDM_%s'% EG]=(data['BDCM_%s'% EG]+data['BDFM_%s'% EG])
    data['BDF_%s'% EG]=(data['BDFF_%s'% EG]+data['BDCF_%s'% EG])
    
    # Calculate total duration of each "social" behavior directed at CTR-rats and FLX-rats
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
    data['ODCR_%s'% EE]=(data['ODCF_%s'% EE]+data['ODCM_%s'% EE])
    data['ODFR_%s'% EE]=(data['ODFF_%s'% EE]+data['ODFM_%s'% EE])
    data['ODCR_%s'% EF]=(data['ODCF_%s'% EF]+data['ODCM_%s'% EF])
    data['ODFR_%s'% EF]=(data['ODFF_%s'% EF]+data['ODFM_%s'% EF])
    data['ODCR_%s'% EG]=(data['ODCF_%s'% EG]+data['ODCM_%s'% EG])
    data['ODFR_%s'% EG]=(data['ODFF_%s'% EG]+data['ODFM_%s'% EG])
    
    # Calculate total duration of each "social" behavior directed at MALES and FEMALES
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
    data['ODM_%s'% EE]=(data['ODCM_%s'% EE]+data['ODFM_%s'% EE])
    data['ODF_%s'% EE]=(data['ODFF_%s'% EE]+data['ODCF_%s'% EE])
    data['ODM_%s'% EF]=(data['ODCM_%s'% EF]+data['ODFM_%s'% EF])
    data['ODF_%s'% EF]=(data['ODFF_%s'% EF]+data['ODCF_%s'% EF])
    data['ODM_%s'% EG]=(data['ODCM_%s'% EG]+data['ODFM_%s'% EG])
    data['ODF_%s'% EG]=(data['ODFF_%s'% EG]+data['ODCF_%s'% EG])
    
    # Calculate time spent in open field versus burrow area
    data['Time_OA']=(data['OD_%s'% BA]+data['OD_%s'% BB]+data['OD_%s'% BSA]+data['OD_%s'% BSB]+
        data['OD_%s'% BSC]+data['OD_%s'% BSD]+data['OD_%s'% BSE]+data['OD_%s'% BSF]+data['OD_%s'% BSG]+
        data['OD_%s'% BSH]+data['OD_%s'% BSI]+data['OD_%s'% BSJ]+data['OD_%s'% BCA]+data['OD_%s'% BCB]+
        data['OD_%s'% BCC]+data['OD_%s'% BCD])
    data['Time_Burrow']=(data['BD_%s'% BA]+data['BD_%s'% BB]+data['BD_%s'% BSA]+data['BD_%s'% BSB]+
        data['BD_%s'% BSC]+data['BD_%s'% BSD]+data['BD_%s'% BSE]+data['BD_%s'% BSF]+data['BD_%s'% BSG]+
        data['BD_%s'% BSH]+data['BD_%s'% BSI]+data['BD_%s'% BSJ]+data['BD_%s'% BCA]+data['BD_%s'% BCB]+
        data['BD_%s'% BCC]+data['BD_%s'% BCD])
    

    
    # Calculate total number of each "social" behavior directed at each female in total environment
    for position, col_name in enumerate(list_behaviors_social):
        data['TNF1_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNF1_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNF1_%s'% col_name]) 
        data['TNF1_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Female 1')), 
            data['obs_beh_modsub_num_back'], data['TNF1_%s'% col_name]) 
        data['TNF1_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNF1_%s'% col_name]=np.where(data['TNF1_%s'% col_name]==99999, np.NaN, data['TNF1_%s'% col_name])
        data['TNF1_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNF1_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNF1_%s'% col_name]==88888)), 
            0,data['TNF1_%s'% col_name])
        data['TNF1_%s'% col_name]=np.where(data['TNF1_%s'% col_name]==88888, np.NaN, data['TNF1_%s'% col_name])
        data['TNF1_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNF1_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNF1_%s'% col_name])
    
        data['TNF2_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNF2_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNF2_%s'% col_name]) 
        data['TNF2_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Female 2')), 
            data['obs_beh_modsub_num_back'], data['TNF2_%s'% col_name]) 
        data['TNF2_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNF2_%s'% col_name]=np.where(data['TNF2_%s'% col_name]==99999, np.NaN, data['TNF2_%s'% col_name])
        data['TNF2_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNF2_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNF2_%s'% col_name]==88888)), 
            0,data['TNF2_%s'% col_name])
        data['TNF2_%s'% col_name]=np.where(data['TNF2_%s'% col_name]==88888, np.NaN, data['TNF2_%s'% col_name])
        data['TNF2_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNF2_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNF2_%s'% col_name])
    
        data['TNF3_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNF3_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNF3_%s'% col_name]) 
        data['TNF3_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Female 3')), 
            data['obs_beh_modsub_num_back'], data['TNF3_%s'% col_name]) 
        data['TNF3_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNF3_%s'% col_name]=np.where(data['TNF3_%s'% col_name]==99999, np.NaN, data['TNF3_%s'% col_name])
        data['TNF3_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNF3_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNF3_%s'% col_name]==88888)), 
            0,data['TNF3_%s'% col_name])
        data['TNF3_%s'% col_name]=np.where(data['TNF3_%s'% col_name]==88888, np.NaN, data['TNF3_%s'% col_name])
        data['TNF3_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNF3_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNF3_%s'% col_name])
    
        data['TNF4_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNF4_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNF4_%s'% col_name]) 
        data['TNF4_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Female 4')), 
            data['obs_beh_modsub_num_back'], data['TNF4_%s'% col_name]) 
        data['TNF4_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNF4_%s'% col_name]=np.where(data['TNF4_%s'% col_name]==99999, np.NaN, data['TNF4_%s'% col_name])
        data['TNF4_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNF4_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNF4_%s'% col_name]==88888)), 
            0,data['TNF4_%s'% col_name])
        data['TNF4_%s'% col_name]=np.where(data['TNF4_%s'% col_name]==88888, np.NaN, data['TNF4_%s'% col_name])
        data['TNF4_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNF4_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNF4_%s'% col_name])
    
        # Calculate total duration of each "social" behavior directed at each female in total environment
        data['TDF1_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDF1_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDF1_%s'% col_name]) 
        data['TDF1_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Female 1')), 
            data['obs_beh_modsub_sumdur'], data['TDF1_%s'% col_name]) 
        data['TDF1_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDF1_%s'% col_name]=np.where(data['TDF1_%s'% col_name]==99999, np.NaN, data['TDF1_%s'% col_name])
        data['TDF1_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDF1_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDF1_%s'% col_name]==88888)), 
            0,data['TDF1_%s'% col_name])
        data['TDF1_%s'% col_name]=np.where(data['TDF1_%s'% col_name]==88888, np.NaN, data['TDF1_%s'% col_name])
        data['TDF1_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDF1_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDF1_%s'% col_name])
    
        data['TDF2_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDF2_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDF2_%s'% col_name]) 
        data['TDF2_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Female 2')), 
            data['obs_beh_modsub_sumdur'], data['TDF2_%s'% col_name]) 
        data['TDF2_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDF2_%s'% col_name]=np.where(data['TDF2_%s'% col_name]==99999, np.NaN, data['TDF2_%s'% col_name])
        data['TDF2_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDF2_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDF2_%s'% col_name]==88888)), 
            0,data['TDF2_%s'% col_name])
        data['TDF2_%s'% col_name]=np.where(data['TDF2_%s'% col_name]==88888, np.NaN, data['TDF2_%s'% col_name])
        data['TDF2_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDF2_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDF2_%s'% col_name])
    
        data['TDF3_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDF3_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDF3_%s'% col_name]) 
        data['TDF3_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Female 3')), 
            data['obs_beh_modsub_sumdur'], data['TDF3_%s'% col_name]) 
        data['TDF3_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDF3_%s'% col_name]=np.where(data['TDF3_%s'% col_name]==99999, np.NaN, data['TDF3_%s'% col_name])
        data['TDF3_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDF3_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDF3_%s'% col_name]==88888)), 
            0,data['TDF3_%s'% col_name])
        data['TDF3_%s'% col_name]=np.where(data['TDF3_%s'% col_name]==88888, np.NaN, data['TDF3_%s'% col_name])
        data['TDF3_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDF3_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDF3_%s'% col_name])
    
        data['TDF4_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDF4_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDF4_%s'% col_name]) 
        data['TDF4_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Female 4')), 
            data['obs_beh_modsub_sumdur'], data['TDF4_%s'% col_name]) 
        data['TDF4_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDF4_%s'% col_name]=np.where(data['TDF4_%s'% col_name]==99999, np.NaN, data['TDF4_%s'% col_name])
        data['TDF4_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDF4_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDF4_%s'% col_name]==88888)), 
            0,data['TDF4_%s'% col_name])
        data['TDF4_%s'% col_name]=np.where(data['TDF4_%s'% col_name]==88888, np.NaN, data['TDF4_%s'% col_name])
        data['TDF4_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDF4_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDF4_%s'% col_name])
        
    # Calculate with which female is copulated the most
    data['TNF1_%s'% EA]= (data['TNF1_%s'% BSD]+data['TNF1_%s'% BSE]+data['TNF1_%s'% BSF])
    data['TNF2_%s'% EA]= (data['TNF2_%s'% BSD]+data['TNF2_%s'% BSE]+data['TNF2_%s'% BSF])
    data['TNF3_%s'% EA]= (data['TNF3_%s'% BSD]+data['TNF3_%s'% BSE]+data['TNF3_%s'% BSF])
    data['TNF4_%s'% EA]= (data['TNF4_%s'% BSD]+data['TNF4_%s'% BSE]+data['TNF4_%s'% BSF])
    
    data['preferred_female']=np.where((data['TNF1_%s'% EA]>data['TNF2_%s'% EA])&(data['TNF1_%s'% EA]>data['TNF3_%s'% EA])&
        (data['TNF1_%s'% EA]>data['TNF4_%s'% EA]),"Female 1", "")
    data['preferred_female']=np.where((data['TNF2_%s'% EA]>data['TNF1_%s'% EA])&(data['TNF2_%s'% EA]>data['TNF3_%s'% EA])&
        (data['TNF2_%s'% EA]>data['TNF4_%s'% EA]),"Female 2", data['preferred_female'])  
    data['preferred_female']=np.where((data['TNF3_%s'% EA]>data['TNF1_%s'% EA])&(data['TNF3_%s'% EA]>data['TNF2_%s'% EA])&
        (data['TNF3_%s'% EA]>data['TNF4_%s'% EA]),"Female 3", data['preferred_female'])  
    data['preferred_female']=np.where((data['TNF4_%s'% EA]>data['TNF1_%s'% EA])&(data['TNF4_%s'% EA]>data['TNF3_%s'% EA])&
        (data['TNF4_%s'% EA]>data['TNF2_%s'% EA]),"Female 4", data['preferred_female'])  
    
    # Calculate number of sexpartners
    data['femalepartner1']=np.where(data['TNF1_%s'% EA]==0,0,1)
    data['femalepartner2']=np.where(data['TNF2_%s'% EA]==0,0,1)
    data['femalepartner3']=np.where(data['TNF3_%s'% EA]==0,0,1)
    data['femalepartner4']=np.where(data['TNF4_%s'% EA]==0,0,1)
    
    data['nr_femalepartners']=data['femalepartner1']+data['femalepartner2']+data['femalepartner3']+data['femalepartner4']
    
    data['femalepartner1_mistake']=np.where(data['TNF1_%s'% EA]<5,0,1)
    data['femalepartner2_mistake']=np.where(data['TNF2_%s'% EA]<5,0,1)
    data['femalepartner3_mistake']=np.where(data['TNF3_%s'% EA]<5,0,1)
    data['femalepartner4_mistake']=np.where(data['TNF4_%s'% EA]<5,0,1)
    
    data['nr_femalepartners_mistake']=(data['femalepartner1_mistake']+data['femalepartner2_mistake']+
        data['femalepartner3_mistake']+data['femalepartner4_mistake'])
    
    # Create column for the ratID for the preferred female
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_female']=='Female 1'),EF11, "")
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_female']=='Female 2'),EF12, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_female']=='Female 3'),EF13, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_female']=='Female 4'),EF14, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_female']=='Female 1'),EF21, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_female']=='Female 2'),EF22, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_female']=='Female 3'),EF23, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_female']=='Female 4'),EF24, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_female']=='Female 1'),EF31, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_female']=='Female 2'),EF32, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_female']=='Female 3'),EF33, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_female']=='Female 4'),EF34, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_female']=='Female 1'),EF41, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_female']=='Female 2'),EF42, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_female']=='Female 3'),EF43, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_female']=='Female 4'),EF44, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_female']=='Female 1'),EF51, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_female']=='Female 2'),EF52, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_female']=='Female 3'),EF53, data['pref_fem_RatID'])
    data['pref_fem_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_female']=='Female 4'),EF54, data['pref_fem_RatID'])
    
    # Number and durations of behaviors directed at the preferred copulation partner
    for position, col_name in enumerate(list_behaviors_social): 
        data['TN_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 1', data['TNF1_%s'% col_name],np.NaN)
        data['TN_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 2', data['TNF2_%s'% col_name],
            data['TN_pref_fem_%s'% col_name]) 
        data['TN_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 3', data['TNF3_%s'% col_name],
            data['TN_pref_fem_%s'% col_name]) 
        data['TN_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 4', data['TNF4_%s'% col_name],
            data['TN_pref_fem_%s'% col_name])     
        
        data['TN_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 1',((data['TNF2_%s'% col_name]+ 
            data['TNF3_%s'% col_name]+ data['TNF4_%s'% col_name])/3),np.NaN)
        data['TN_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 2',((data['TNF1_%s'% col_name]+ 
            data['TNF3_%s'% col_name]+ data['TNF4_%s'% col_name])/3),data['TN_nonpref_fem_%s'% col_name])    
        data['TN_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 3',((data['TNF1_%s'% col_name]+ 
                data['TDF2_%s'% col_name]+ data['TNF4_%s'% col_name])/3),data['TN_nonpref_fem_%s'% col_name])
        data['TN_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 4',((data['TNF1_%s'% col_name]+ 
            data['TNF3_%s'% col_name]+ data['TNF2_%s'% col_name])/3),data['TN_nonpref_fem_%s'% col_name]) 
             
        data['TD_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 1', data['TDF1_%s'% col_name],np.NaN)
        data['TD_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 2', data['TDF2_%s'% col_name],
            data['TD_pref_fem_%s'% col_name]) 
        data['TD_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 3', data['TDF3_%s'% col_name],
            data['TD_pref_fem_%s'% col_name]) 
        data['TD_pref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 4', data['TDF4_%s'% col_name],
            data['TD_pref_fem_%s'% col_name])     
        
        data['TD_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 1',((data['TDF2_%s'% col_name]+ 
            data['TDF3_%s'% col_name]+ data['TDF4_%s'% col_name])/3),np.NaN)
        data['TD_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 2',((data['TDF1_%s'% col_name]+ 
            data['TDF3_%s'% col_name]+ data['TDF4_%s'% col_name])/3),data['TD_nonpref_fem_%s'% col_name])    
        data['TD_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 3',((data['TDF1_%s'% col_name]+ 
                data['TDF2_%s'% col_name]+ data['TDF4_%s'% col_name])/3),data['TD_nonpref_fem_%s'% col_name])
        data['TD_nonpref_fem_%s'% col_name]=np.where(data['preferred_female']=='Female 4',((data['TDF1_%s'% col_name]+ 
            data['TDF3_%s'% col_name]+ data['TDF2_%s'% col_name])/3),data['TD_nonpref_fem_%s'% col_name]) 
    
    for position, col_name in enumerate(list_behaviors_social): 
        data['TN_nonprefmale_%s'% col_name]=(data['TNM_%s'% col_name]/4) # This is to compare preferred female and other females to contact with males
        data['TD_nonprefmale_%s'% col_name]=(data['TDM_%s'% col_name]/4)
    
    data['TN_pref_fem_%s'% EC]= (data['TN_pref_fem_%s'% BSG]+data['TN_pref_fem_%s'% BSH]+data['TN_pref_fem_%s'% BSI])
    data['TN_pref_fem_%s'% EE]= (data['TN_pref_fem_%s'% BCA]+data['TN_pref_fem_%s'% BCB]+data['TN_pref_fem_%s'% BCC]+
        data['TN_pref_fem_%s'% BCD])
    
    data['TN_nonpref_fem_%s'% EC]= (data['TN_nonpref_fem_%s'% BSG]+data['TN_nonpref_fem_%s'% BSH]+data['TN_nonpref_fem_%s'% BSI])
    data['TN_nonpref_fem_%s'% EE]= (data['TN_nonpref_fem_%s'% BCA]+data['TN_nonpref_fem_%s'% BCB]+data['TN_nonpref_fem_%s'% BCC]+
        data['TN_nonpref_fem_%s'% BCD])
    
    data['TN_nonprefmale_%s'% EC]= (data['TN_nonprefmale_%s'% BSG]+data['TN_nonprefmale_%s'% BSH]+data['TN_nonprefmale_%s'% BSI])
    data['TN_nonprefmale_%s'% EE]= (data['TN_nonprefmale_%s'% BCA]+data['TN_nonprefmale_%s'% BCB]+data['TN_nonprefmale_%s'% BCC]+
        data['TN_nonprefmale_%s'% BCD])
    
    data['TD_pref_fem_%s'% EC]= (data['TD_pref_fem_%s'% BSG]+data['TD_pref_fem_%s'% BSH]+data['TD_pref_fem_%s'% BSI])
    data['TD_pref_fem_%s'% EE]= (data['TD_pref_fem_%s'% BCA]+data['TD_pref_fem_%s'% BCB]+data['TD_pref_fem_%s'% BCC]+data['TD_pref_fem_%s'% BCD])
    
    data['TD_nonpref_fem_%s'% EC]= (data['TD_nonpref_fem_%s'% BSG]+data['TD_nonpref_fem_%s'% BSH]+data['TD_nonpref_fem_%s'% BSI])
    data['TD_nonpref_fem_%s'% EE]= (data['TD_nonpref_fem_%s'% BCA]+data['TD_nonpref_fem_%s'% BCB]+data['TD_nonpref_fem_%s'% BCC]+
        data['TD_nonpref_fem_%s'% BCD])
    
    data['TD_nonprefmale_%s'% EC]= (data['TD_nonprefmale_%s'% BSG]+data['TD_nonprefmale_%s'% BSH]+data['TD_nonprefmale_%s'% BSI])
    data['TD_nonprefmale_%s'% EE]= (data['TD_nonprefmale_%s'% BCA]+data['TD_nonprefmale_%s'% BCB]+data['TD_nonprefmale_%s'% BCC]+
        data['TD_nonprefmale_%s'% BCD])
    
    # Calculate total number of each "social" behavior directed at each male in total environment
    for position, col_name in enumerate(list_behaviors_social):
        data['TNM1_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNM1_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNM1_%s'% col_name]) 
        data['TNM1_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Male 1')), 
            data['obs_beh_modsub_num_back'], data['TNM1_%s'% col_name]) 
        data['TNM1_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNM1_%s'% col_name]=np.where(data['TNM1_%s'% col_name]==99999, np.NaN, data['TNM1_%s'% col_name])
        data['TNM1_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNM1_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNM1_%s'% col_name]==88888)), 
            0,data['TNM1_%s'% col_name])
        data['TNM1_%s'% col_name]=np.where(data['TNM1_%s'% col_name]==88888, np.NaN, data['TNM1_%s'% col_name])
        data['TNM1_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNM1_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNM1_%s'% col_name])
    
        data['TNM2_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNM2_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNM2_%s'% col_name]) 
        data['TNM2_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Male 2')), 
            data['obs_beh_modsub_num_back'], data['TNM2_%s'% col_name]) 
        data['TNM2_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNM2_%s'% col_name]=np.where(data['TNM2_%s'% col_name]==99999, np.NaN, data['TNM2_%s'% col_name])
        data['TNM2_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNM2_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNM2_%s'% col_name]==88888)), 
            0,data['TNM2_%s'% col_name])
        data['TNM2_%s'% col_name]=np.where(data['TNM2_%s'% col_name]==88888, np.NaN, data['TNM2_%s'% col_name])
        data['TNM2_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNM2_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNM2_%s'% col_name])
    
        data['TNM3_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNM3_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNM3_%s'% col_name]) 
        data['TNM3_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Male 3')), 
            data['obs_beh_modsub_num_back'], data['TNM3_%s'% col_name]) 
        data['TNM3_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNM3_%s'% col_name]=np.where(data['TNM3_%s'% col_name]==99999, np.NaN, data['TNM3_%s'% col_name])
        data['TNM3_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNM3_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNM3_%s'% col_name]==88888)), 
            0,data['TNM3_%s'% col_name])
        data['TNM3_%s'% col_name]=np.where(data['TNM3_%s'% col_name]==88888, np.NaN, data['TNM3_%s'% col_name])
        data['TNM3_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNM3_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNM3_%s'% col_name])
    
        data['TNM4_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TNM4_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TNM4_%s'% col_name]) 
        data['TNM4_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num']==1)&(data[MODSUB]=='Male 4')), 
            data['obs_beh_modsub_num_back'], data['TNM4_%s'% col_name]) 
        data['TNM4_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TNM4_%s'% col_name]=np.where(data['TNM4_%s'% col_name]==99999, np.NaN, data['TNM4_%s'% col_name])
        data['TNM4_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TNM4_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TNM4_%s'% col_name]==88888)), 
            0,data['TNM4_%s'% col_name])
        data['TNM4_%s'% col_name]=np.where(data['TNM4_%s'% col_name]==88888, np.NaN, data['TNM4_%s'% col_name])
        data['TNM4_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TNM4_%s'% col_name]= np.where(data[BEH]=='None',0,data['TNM4_%s'% col_name])
    
        # Calculate total duration of each "social" behavior directed at each Male in total environment
        data['TDM1_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDM1_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDM1_%s'% col_name]) 
        data['TDM1_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Male 1')), 
            data['obs_beh_modsub_sumdur'], data['TDM1_%s'% col_name]) 
        data['TDM1_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDM1_%s'% col_name]=np.where(data['TDM1_%s'% col_name]==99999, np.NaN, data['TDM1_%s'% col_name])
        data['TDM1_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDM1_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDM1_%s'% col_name]==88888)), 
            0,data['TDM1_%s'% col_name])
        data['TDM1_%s'% col_name]=np.where(data['TDM1_%s'% col_name]==88888, np.NaN, data['TDM1_%s'% col_name])
        data['TDM1_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDM1_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDM1_%s'% col_name])
    
        data['TDM2_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDM2_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDM2_%s'% col_name]) 
        data['TDM2_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Male 2')), 
            data['obs_beh_modsub_sumdur'], data['TDM2_%s'% col_name]) 
        data['TDM2_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDM2_%s'% col_name]=np.where(data['TDM2_%s'% col_name]==99999, np.NaN, data['TDM2_%s'% col_name])
        data['TDM2_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDM2_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDM2_%s'% col_name]==88888)), 
            0,data['TDM2_%s'% col_name])
        data['TDM2_%s'% col_name]=np.where(data['TDM2_%s'% col_name]==88888, np.NaN, data['TDM2_%s'% col_name])
        data['TDM2_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDM2_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDM2_%s'% col_name])
    
        data['TDM3_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDM3_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDM3_%s'% col_name]) 
        data['TDM3_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Male 3')), 
            data['obs_beh_modsub_sumdur'], data['TDM3_%s'% col_name]) 
        data['TDM3_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDM3_%s'% col_name]=np.where(data['TDM3_%s'% col_name]==99999, np.NaN, data['TDM3_%s'% col_name])
        data['TDM3_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDM3_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDM3_%s'% col_name]==88888)), 
            0,data['TDM3_%s'% col_name])
        data['TDM3_%s'% col_name]=np.where(data['TDM3_%s'% col_name]==88888, np.NaN, data['TDM3_%s'% col_name])
        data['TDM3_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDM3_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDM3_%s'% col_name])
    
        data['TDM4_%s'% col_name]= np.where(data['obs_num']==1,99999, np.NaN) 
        data['TDM4_%s'% col_name]= np.where(data['obs_num_back']==1,88888, data['TDM4_%s'% col_name]) 
        data['TDM4_%s'% col_name]= np.where(((data[BEH]==col_name)&(data['obs_beh_modsub_num_back']==1)&(data[MODSUB]=='Male 4')), 
            data['obs_beh_modsub_sumdur'], data['TDM4_%s'% col_name]) 
        data['TDM4_%s'% col_name].fillna(method = "ffill", inplace=True)        
        data['TDM4_%s'% col_name]=np.where(data['TDM4_%s'% col_name]==99999, np.NaN, data['TDM4_%s'% col_name])
        data['TDM4_%s'% col_name].fillna(method = "backfill", inplace=True)
        data['TDM4_%s'% col_name]= np.where(((data['obs_num_back']!=1)&(data['TDM4_%s'% col_name]==88888)), 
            0,data['TDM4_%s'% col_name])
        data['TDM4_%s'% col_name]=np.where(data['TDM4_%s'% col_name]==88888, np.NaN, data['TDM4_%s'% col_name])
        data['TDM4_%s'% col_name].fillna(method = "ffill", inplace=True)
        data['TDM4_%s'% col_name]= np.where(data[BEH]=='None',0,data['TDM4_%s'% col_name])
        
    # Calculate with which male is copulated the most
    data['TNM1_%s'% EA]= (data['TNM1_%s'% BSD]+data['TNM1_%s'% BSE]+data['TNM1_%s'% BSF])
    data['TNM2_%s'% EA]= (data['TNM2_%s'% BSD]+data['TNM2_%s'% BSE]+data['TNM2_%s'% BSF])
    data['TNM3_%s'% EA]= (data['TNM3_%s'% BSD]+data['TNM3_%s'% BSE]+data['TNM3_%s'% BSF])
    data['TNM4_%s'% EA]= (data['TNM4_%s'% BSD]+data['TNM4_%s'% BSE]+data['TNM4_%s'% BSF])
    
    data['preferred_male']=np.where((data['TNM1_%s'% EA]>data['TNM2_%s'% EA])&(data['TNM1_%s'% EA]>data['TNM3_%s'% EA])&
        (data['TNM1_%s'% EA]>data['TNM4_%s'% EA]),"Male 1", "")
    data['preferred_male']=np.where((data['TNM2_%s'% EA]>data['TNM1_%s'% EA])&(data['TNM2_%s'% EA]>data['TNM3_%s'% EA])&
        (data['TNM2_%s'% EA]>data['TNM4_%s'% EA]),"Male 2", data['preferred_male'])  
    data['preferred_male']=np.where((data['TNM3_%s'% EA]>data['TNM1_%s'% EA])&(data['TNM3_%s'% EA]>data['TNM2_%s'% EA])&
        (data['TNM3_%s'% EA]>data['TNM4_%s'% EA]),"Male 3", data['preferred_male'])  
    data['preferred_male']=np.where((data['TNM4_%s'% EA]>data['TNM1_%s'% EA])&(data['TNM4_%s'% EA]>data['TNM3_%s'% EA])&
        (data['TNM4_%s'% EA]>data['TNM2_%s'% EA]),"Male 4", data['preferred_male'])  
    
    # Calculate number of sexpartners
    data['malepartner1']=np.where(data['TNM1_%s'% EA]==0,0,1)
    data['malepartner2']=np.where(data['TNM2_%s'% EA]==0,0,1)
    data['malepartner3']=np.where(data['TNM3_%s'% EA]==0,0,1)
    data['malepartner4']=np.where(data['TNM4_%s'% EA]==0,0,1)
    
    data['nr_malepartner']=data['malepartner1']+data['malepartner2']+data['malepartner3']+data['malepartner4']
    
    data['malepartner1_mistake']=np.where(data['TNM1_%s'% EA]<5,0,1)
    data['malepartner2_mistake']=np.where(data['TNM2_%s'% EA]<5,0,1)
    data['malepartner3_mistake']=np.where(data['TNM3_%s'% EA]<5,0,1)
    data['malepartner4_mistake']=np.where(data['TNM4_%s'% EA]<5,0,1)
    
    data['nr_malepartner_mistake']=(data['malepartner1_mistake']+data['malepartner2_mistake']+
        data['malepartner3_mistake']+data['malepartner4_mistake'])
    
    # Create column for the ratID for the preferred male
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_male']=='Male 1'),EM11, "")
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_male']=='Male 2'),EM12, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_male']=='Male 3'),EM13, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE1')&(data['preferred_male']=='Male 4'),EM14, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_male']=='Male 1'),EM21, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_male']=='Male 2'),EM22, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_male']=='Male 3'),EM23, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE2')&(data['preferred_male']=='Male 4'),EM24, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_male']=='Male 1'),EM31, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_male']=='Male 2'),EM32, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_male']=='Male 3'),EM33, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE3')&(data['preferred_male']=='Male 4'),EM34, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_male']=='Male 1'),EM41, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_male']=='Male 2'),EM42, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_male']=='Male 3'),EM43, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE4')&(data['preferred_male']=='Male 4'),EM44, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_male']=='Male 1'),EM51, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_male']=='Male 2'),EM52, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_male']=='Male 3'),EM53, data['pref_male_RatID'])
    data['pref_male_RatID']=np.where((data['Cohort']=='SNE5')&(data['preferred_male']=='Male 4'),EM54, data['pref_male_RatID'])
    
    # Number and durations of behaviors directed at the preferred copulation partner
    for position, col_name in enumerate(list_behaviors_social): 
        data['TN_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 1', data['TNM1_%s'% col_name],np.NaN)
        data['TN_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 2', data['TNM2_%s'% col_name],
            data['TN_pref_male_%s'% col_name]) 
        data['TN_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 3', data['TNM3_%s'% col_name],
            data['TN_pref_male_%s'% col_name]) 
        data['TN_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 4', data['TNM4_%s'% col_name],
            data['TN_pref_male_%s'% col_name])     
        
        data['TN_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 1',((data['TNM2_%s'% col_name]+ 
            data['TNM3_%s'% col_name]+ data['TNM4_%s'% col_name])/3),np.NaN)
        data['TN_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 2',((data['TNM1_%s'% col_name]+ 
            data['TNM3_%s'% col_name]+ data['TNM4_%s'% col_name])/3),data['TN_nonpref_male_%s'% col_name])    
        data['TN_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 3',((data['TNM1_%s'% col_name]+ 
                data['TDM2_%s'% col_name]+ data['TNM4_%s'% col_name])/3),data['TN_nonpref_male_%s'% col_name])
        data['TN_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 4',((data['TNM1_%s'% col_name]+ 
            data['TNM3_%s'% col_name]+ data['TNM2_%s'% col_name])/3),data['TN_nonpref_male_%s'% col_name]) 
             
        data['TD_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 1', data['TDM1_%s'% col_name],np.NaN)
        data['TD_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 2', data['TDM2_%s'% col_name],
            data['TD_pref_male_%s'% col_name]) 
        data['TD_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 3', data['TDM3_%s'% col_name],
            data['TD_pref_male_%s'% col_name]) 
        data['TD_pref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 4', data['TDM4_%s'% col_name],
            data['TD_pref_male_%s'% col_name])     
        
        data['TD_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 1',((data['TDM2_%s'% col_name]+ 
            data['TDM3_%s'% col_name]+ data['TDM4_%s'% col_name])/3),np.NaN)
        data['TD_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 2',((data['TDM1_%s'% col_name]+ 
            data['TDM3_%s'% col_name]+ data['TDM4_%s'% col_name])/3),data['TD_nonpref_male_%s'% col_name])    
        data['TD_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 3',((data['TDM1_%s'% col_name]+ 
                data['TDM2_%s'% col_name]+ data['TDM4_%s'% col_name])/3),data['TD_nonpref_male_%s'% col_name])
        data['TD_nonpref_male_%s'% col_name]=np.where(data['preferred_male']=='Male 4',((data['TDM1_%s'% col_name]+ 
            data['TDM3_%s'% col_name]+ data['TDM2_%s'% col_name])/3),data['TD_nonpref_male_%s'% col_name]) 
    
    for position, col_name in enumerate(list_behaviors_social): 
        data['TN_nonpreffemale_%s'% col_name]=(data['TNF_%s'% col_name]/4) # This is to compare preferred male and other males to contact with females
        data['TD_nonpreffemale_%s'% col_name]=(data['TDF_%s'% col_name]/4)
    
    data['TN_pref_male_%s'% EC]= (data['TN_pref_male_%s'% BSG]+data['TN_pref_male_%s'% BSH]+data['TN_pref_male_%s'% BSI])
    data['TN_pref_male_%s'% EE]= (data['TN_pref_male_%s'% BCA]+data['TN_pref_male_%s'% BCB]+data['TN_pref_male_%s'% BCC]+
        data['TN_pref_male_%s'% BCD])
    
    data['TN_nonpref_male_%s'% EC]= (data['TN_nonpref_male_%s'% BSG]+data['TN_nonpref_male_%s'% BSH]+data['TN_nonpref_male_%s'% BSI])
    data['TN_nonpref_male_%s'% EE]= (data['TN_nonpref_male_%s'% BCA]+data['TN_nonpref_male_%s'% BCB]+data['TN_nonpref_male_%s'% BCC]+
        data['TN_nonpref_male_%s'% BCD])
    
    data['TN_nonpreffemale_%s'% EC]= (data['TN_nonpreffemale_%s'% BSG]+data['TN_nonpreffemale_%s'% BSH]+data['TN_nonpreffemale_%s'% BSI])
    data['TN_nonpreffemale_%s'% EE]= (data['TN_nonpreffemale_%s'% BCA]+data['TN_nonpreffemale_%s'% BCB]+data['TN_nonpreffemale_%s'% BCC]+
        data['TN_nonpreffemale_%s'% BCD])
    
    data['TD_pref_male_%s'% EC]= (data['TD_pref_male_%s'% BSG]+data['TD_pref_male_%s'% BSH]+data['TD_pref_male_%s'% BSI])
    data['TD_pref_male_%s'% EE]= (data['TD_pref_male_%s'% BCA]+data['TD_pref_male_%s'% BCB]+data['TD_pref_male_%s'% BCC]+data['TD_pref_male_%s'% BCD])
    
    data['TD_nonpref_male_%s'% EC]= (data['TD_nonpref_male_%s'% BSG]+data['TD_nonpref_male_%s'% BSH]+data['TD_nonpref_male_%s'% BSI])
    data['TD_nonpref_male_%s'% EE]= (data['TD_nonpref_male_%s'% BCA]+data['TD_nonpref_male_%s'% BCB]+data['TD_nonpref_male_%s'% BCC]+
        data['TD_nonpref_male_%s'% BCD])
    
    data['TD_nonpreffemale_%s'% EC]= (data['TD_nonpreffemale_%s'% BSG]+data['TD_nonpreffemale_%s'% BSH]+data['TD_nonpreffemale_%s'% BSI])
    data['TD_nonpreffemale_%s'% EE]= (data['TD_nonpreffemale_%s'% BCA]+data['TD_nonpreffemale_%s'% BCB]+data['TD_nonpreffemale_%s'% BCC]+
        data['TD_nonpreffemale_%s'% BCD])

# Just to get notification this part is finished
print("data calculations finished")

# Make sure that all the rats that did not show behavior gets the numbers deleted.
data_all_columns=list(data_all.columns.values)
relevant_data_all_columns=data_all_columns[46:]

for i in missing_all:
    for position, column in enumerate(relevant_data_all_columns):
        data_all[column]=np.where(data_all[SUBRAW]==i,0,data_all[column])

data_CB1_columns=list(data_CB1.columns.values)
relevant_data_CB1_columns=data_CB1_columns[46:]

for i in missing_CB1:
    for position, column in enumerate(relevant_data_CB1_columns):
        data_CB1[column]=np.where(data_CB1[SUBRAW]==i,0,data_CB1[column])

data_CB2_columns=list(data_CB2.columns.values)
relevant_data_CB2_columns=data_CB2_columns[46:]

for i in missing_CB2:
    for position, column in enumerate(relevant_data_CB2_columns):
        data_CB2[column]=np.where(data_CB2[SUBRAW]==i,np.NaN,data_CB2[column])

data_CB3_columns=list(data_CB3.columns.values)
relevant_data_CB3_columns=data_CB3_columns[46:]

for i in missing_CB3:
    for position, column in enumerate(relevant_data_CB3_columns):
        data_CB3[column]=np.where(data_CB3[SUBRAW]==i,np.NaN,data_CB3[column])

data_CB4_columns=list(data_CB4.columns.values)
relevant_data_CB4_columns=data_CB4_columns[46:]

for i in missing_CB4:
    for position, column in enumerate(relevant_data_CB4_columns):
        data_CB4[column]=np.where(data_CB4[SUBRAW]==i,np.NaN,data_CB4[column])

data_CB5_columns=list(data_CB5.columns.values)
relevant_data_CB5_columns=data_CB5_columns[46:]

for i in missing_CB5:
    for position, column in enumerate(relevant_data_CB5_columns):
        data_CB5[column]=np.where(data_CB5[SUBRAW]==i,np.NaN,data_CB5[column])

data_CB6_columns=list(data_CB6.columns.values)
relevant_data_CB6_columns=data_CB6_columns[46:]

for i in missing_CB6:
    for position, column in enumerate(relevant_data_CB6_columns):
        data_CB6[column]=np.where(data_CB6[SUBRAW]==i,np.NaN,data_CB6[column])


# now save the data frame to excel
data_full.to_csv("Output/HN003 raw data full.csv")
data_all.to_csv("Output/HN003 raw data all.csv")
data_CB1.to_csv("Output/HN003 raw data CB1.csv")
data_CB2.to_csv("Output/HN003 raw data CB2.csv")
data_CB3.to_csv("Output/HN003 raw data CB3.csv")
data_CB4.to_csv("Output/HN003 raw data CB4.csv")
data_CB5.to_csv("Output/HN003 raw data CB5.csv")
data_CB6.to_csv("Output/HN003 raw data CB6.csv")

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

 # Replace the empty cells with zeros (otherwise the function after does not work)
 results_MAB_full['CB1_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)
 results_MAB_full['CB2_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)
 results_MAB_full['CB3_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)
 results_MAB_full['CB4_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)
 results_MAB_full['CB5_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)
 results_MAB_full['CB6_TN_%s'% BSB].replace(np.NaN, 0, inplace = True)

 # Make a column that mentions the most active bout
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB1_TN_%s'% BSB]>=results_MAB_full['CB2_TN_%s'% BSB])&
                 (results_MAB_full['CB1_TN_%s'% BSB]>=results_MAB_full['CB3_TN_%s'% BSB])&
                 (results_MAB_full['CB1_TN_%s'% BSB]>=results_MAB_full['CB4_TN_%s'% BSB])&
                 (results_MAB_full['CB1_TN_%s'% BSB]>=results_MAB_full['CB5_TN_%s'% BSB])&
                 (results_MAB_full['CB1_TN_%s'% BSB]>=results_MAB_full['CB6_TN_%s'% BSB])),"CB1",
                 np.NaN)
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB2_TN_%s'% BSB]>results_MAB_full['CB1_TN_%s'% BSB])&
                 (results_MAB_full['CB2_TN_%s'% BSB]>=results_MAB_full['CB3_TN_%s'% BSB])&
                 (results_MAB_full['CB2_TN_%s'% BSB]>=results_MAB_full['CB4_TN_%s'% BSB])&
                 (results_MAB_full['CB2_TN_%s'% BSB]>=results_MAB_full['CB5_TN_%s'% BSB])&
                 (results_MAB_full['CB2_TN_%s'% BSB]>=results_MAB_full['CB6_TN_%s'% BSB])),"CB2",
                 results_MAB_full['MAB_CB'])
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB3_TN_%s'% BSB]>results_MAB_full['CB1_TN_%s'% BSB])&
                 (results_MAB_full['CB3_TN_%s'% BSB]>results_MAB_full['CB2_TN_%s'% BSB])&
                 (results_MAB_full['CB3_TN_%s'% BSB]>=results_MAB_full['CB4_TN_%s'% BSB])&
                 (results_MAB_full['CB3_TN_%s'% BSB]>=results_MAB_full['CB5_TN_%s'% BSB])&
                 (results_MAB_full['CB3_TN_%s'% BSB]>=results_MAB_full['CB6_TN_%s'% BSB])),"CB3",
                 results_MAB_full['MAB_CB'])
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB4_TN_%s'% BSB]>results_MAB_full['CB1_TN_%s'% BSB])&
                 (results_MAB_full['CB4_TN_%s'% BSB]>results_MAB_full['CB3_TN_%s'% BSB])&
                 (results_MAB_full['CB4_TN_%s'% BSB]>results_MAB_full['CB2_TN_%s'% BSB])&
                 (results_MAB_full['CB4_TN_%s'% BSB]>=results_MAB_full['CB5_TN_%s'% BSB])&
                 (results_MAB_full['CB4_TN_%s'% BSB]>=results_MAB_full['CB6_TN_%s'% BSB])),"CB4",
                 results_MAB_full['MAB_CB'])
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB5_TN_%s'% BSB]>results_MAB_full['CB1_TN_%s'% BSB])&
                 (results_MAB_full['CB5_TN_%s'% BSB]>results_MAB_full['CB3_TN_%s'% BSB])&
                 (results_MAB_full['CB5_TN_%s'% BSB]>results_MAB_full['CB4_TN_%s'% BSB])&
                 (results_MAB_full['CB5_TN_%s'% BSB]>results_MAB_full['CB2_TN_%s'% BSB])&
                 (results_MAB_full['CB5_TN_%s'% BSB]>=results_MAB_full['CB6_TN_%s'% BSB])),"CB5",
                 results_MAB_full['MAB_CB'])
 results_MAB_full['MAB_CB']=np.where(((results_MAB_full['CB6_TN_%s'% BSB]>results_MAB_full['CB1_TN_%s'% BSB])&
                 (results_MAB_full['CB6_TN_%s'% BSB]>results_MAB_full['CB3_TN_%s'% BSB])&
                 (results_MAB_full['CB6_TN_%s'% BSB]>results_MAB_full['CB4_TN_%s'% BSB])&
                 (results_MAB_full['CB6_TN_%s'% BSB]>results_MAB_full['CB5_TN_%s'% BSB])&
                 (results_MAB_full['CB6_TN_%s'% BSB]>results_MAB_full['CB2_TN_%s'% BSB])),"CB6",
                 results_MAB_full['MAB_CB'])

 # Make sure to remove the zeros from CB2 and higher
 results_MAB_full['CB2_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
 results_MAB_full['CB3_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
 results_MAB_full['CB4_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
 results_MAB_full['CB5_TN_%s'% BSB].replace(0, np.NaN, inplace = True)
 results_MAB_full['CB6_TN_%s'% BSB].replace(0, np.NaN, inplace = True)

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

 ## Make excel sheets with relevant information
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

 results_all_TN_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB1_TN_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB2_TN_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB3_TN_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB4_TN_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB5_TN_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_CB6_TN_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)
 results_MAB_TN_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TNM_|TNF_|TNCR_|TNFR_|TN_pref_male_|TN_nonpref_male_|TN_nonpreffemale')]], sort=False, axis=1)

 results_all_ON_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB1_ON_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB2_ON_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB3_ON_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB4_ON_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB5_ON_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_CB6_ON_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)
 results_MAB_ON_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('ONM_|ONF_|ONCR_|ONFR_|ON_pref_male_|ON_nonpref_male_|ON_nonpreffemale')]], sort=False, axis=1)

 results_all_BN_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB1_BN_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB2_BN_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB3_BN_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB4_BN_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB5_BN_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_CB6_BN_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)
 results_MAB_BN_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('BNM_|BNF_|BNCR_|BNFR_|BN_pref_male_|BN_nonpref_male_|BN_nonpreffemale')]], sort=False, axis=1)

 results_all_TD_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB1_TD_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB2_TD_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB3_TD_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB4_TD_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB5_TD_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_CB6_TD_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)
 results_MAB_TD_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TDM_|TDF_|TDCR_|TDFR_|TD_pref_male_|TD_nonpref_male_|TD_nonpreffemale')]], sort=False, axis=1)

 results_all_OD_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB1_OD_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB2_OD_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB3_OD_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB4_OD_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB5_OD_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_CB6_OD_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)
 results_MAB_OD_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('ODM_|ODF_|ODCR_|ODFR_|OD_pref_male_|OD_nonpref_male_|OD_nonpreffemale')]], sort=False, axis=1)

 results_all_BD_mod= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB1_BD_mod= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB2_BD_mod= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB3_BD_mod= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB4_BD_mod= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB5_BD_mod= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_CB6_BD_mod= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)
 results_MAB_BD_mod= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('BDM_|BDF_|BDCR_|BDFR_|BD_pref_male_|BD_nonpref_male_|BD_nonpreffemale')]], sort=False, axis=1)

 results_all_TN_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB1_TN_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB2_TN_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB3_TN_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB4_TN_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB5_TN_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_CB6_TN_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)
 results_MAB_TN_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TNCF_|TNFF_|TNCM_|TNFM_')]], sort=False, axis=1)

 results_all_ON_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB1_ON_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB2_ON_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB3_ON_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB4_ON_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB5_ON_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_CB6_ON_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)
 results_MAB_ON_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('ONCF_|ONFF_|ONCM_|ONFM_')]], sort=False, axis=1)

 results_all_BN_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB1_BN_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB2_BN_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB3_BN_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB4_BN_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB5_BN_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_CB6_BN_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)
 results_MAB_BN_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('BNCF_|BNFF_|BNCM_|BNFM_')]], sort=False, axis=1)

 results_all_TD_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB1_TD_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB2_TD_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB3_TD_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB4_TD_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB5_TD_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_CB6_TD_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)
 results_MAB_TD_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('TDCF_|TDFF_|TDCM_|TDFM_')]], sort=False, axis=1)

 results_all_OD_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB1_OD_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB2_OD_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB3_OD_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB4_OD_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB5_OD_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_CB6_OD_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)
 results_MAB_OD_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('ODCF_|ODFF_|ODCM_|ODFM_')]], sort=False, axis=1)

 results_all_BD_modtreat= pd.concat([results_all_pre2, results_all.loc[:, results_all.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB1_BD_modtreat= pd.concat([results_CB1_pre2, results_CB1.loc[:, results_CB1.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB2_BD_modtreat= pd.concat([results_CB2_pre2, results_CB2.loc[:, results_CB2.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB3_BD_modtreat= pd.concat([results_CB3_pre2, results_CB3.loc[:, results_CB3.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB4_BD_modtreat= pd.concat([results_CB4_pre2, results_CB4.loc[:, results_CB4.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB5_BD_modtreat= pd.concat([results_CB5_pre2, results_CB5.loc[:, results_CB5.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_CB6_BD_modtreat= pd.concat([results_CB6_pre2, results_CB6.loc[:, results_CB6.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)
 results_MAB_BD_modtreat= pd.concat([results_MAB_pre2, results_MAB.loc[:, results_MAB.columns.str.contains('BDCF_|BDFF_|BDCM_|BDFM_')]], sort=False, axis=1)

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
                   results_MAB_TN_min,results_MAB_ON_min,results_MAB_BN_min,results_MAB_TD_min,results_MAB_OD_min,results_MAB_BD_min,
                   results_all_TN_mod,results_all_ON_mod,results_all_BN_mod,results_all_TD_mod,results_all_OD_mod,results_all_BD_mod,
                   results_CB1_TN_mod,results_CB1_ON_mod,results_CB1_BN_mod,results_CB1_TD_mod,results_CB1_OD_mod,results_CB1_BD_mod,
                   results_CB2_TN_mod,results_CB2_ON_mod,results_CB2_BN_mod,results_CB2_TD_mod,results_CB2_OD_mod,results_CB2_BD_mod,
                   results_CB3_TN_mod,results_CB3_ON_mod,results_CB3_BN_mod,results_CB3_TD_mod,results_CB3_OD_mod,results_CB3_BD_mod,
                   results_CB4_TN_mod,results_CB4_ON_mod,results_CB4_BN_mod,results_CB4_TD_mod,results_CB4_OD_mod,results_CB4_BD_mod,
                   results_CB5_TN_mod,results_CB5_ON_mod,results_CB5_BN_mod,results_CB5_TD_mod,results_CB5_OD_mod,results_CB5_BD_mod,
                   results_CB6_TN_mod,results_CB6_ON_mod,results_CB6_BN_mod,results_CB6_TD_mod,results_CB6_OD_mod,results_CB6_BD_mod,
                   results_MAB_TN_mod,results_MAB_ON_mod,results_MAB_BN_mod,results_MAB_TD_mod,results_MAB_OD_mod,results_MAB_BD_mod,
                   results_all_TN_modtreat,results_all_ON_modtreat,results_all_BN_modtreat,results_all_TD_modtreat,results_all_OD_modtreat,results_all_BD_modtreat,
                   results_CB1_TN_modtreat,results_CB1_ON_modtreat,results_CB1_BN_modtreat,results_CB1_TD_modtreat,results_CB1_OD_modtreat,results_CB1_BD_modtreat,
                   results_CB2_TN_modtreat,results_CB2_ON_modtreat,results_CB2_BN_modtreat,results_CB2_TD_modtreat,results_CB2_OD_modtreat,results_CB2_BD_modtreat,
                   results_CB3_TN_modtreat,results_CB3_ON_modtreat,results_CB3_BN_modtreat,results_CB3_TD_modtreat,results_CB3_OD_modtreat,results_CB3_BD_modtreat,
                   results_CB4_TN_modtreat,results_CB4_ON_modtreat,results_CB4_BN_modtreat,results_CB4_TD_modtreat,results_CB4_OD_modtreat,results_CB4_BD_modtreat,
                   results_CB5_TN_modtreat,results_CB5_ON_modtreat,results_CB5_BN_modtreat,results_CB5_TD_modtreat,results_CB5_OD_modtreat,results_CB5_BD_modtreat,
                   results_CB6_TN_modtreat,results_CB6_ON_modtreat,results_CB6_BN_modtreat,results_CB6_TD_modtreat,results_CB6_OD_modtreat,results_CB6_BD_modtreat,
                   results_MAB_TN_modtreat,results_MAB_ON_modtreat,results_MAB_BN_modtreat,results_MAB_TD_modtreat,results_MAB_OD_modtreat,results_MAB_BD_modtreat]

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
                   'mean_MAB_TN_min','mean_MAB_ON_min','mean_MAB_BN_min','mean_MAB_TD_min','mean_MAB_OD_min','mean_MAB_BD_min',
                   'mean_all_TN_mod','mean_all_ON_mod','mean_all_BN_mod','mean_all_TD_mod','mean_all_OD_mod','mean_all_BD_mod',
                   'mean_CB1_TN_mod','mean_CB1_ON_mod','mean_CB1_BN_mod','mean_CB1_TD_mod','mean_CB1_OD_mod','mean_CB1_BD_mod',
                   'mean_CB2_TN_mod','mean_CB2_ON_mod','mean_CB2_BN_mod','mean_CB2_TD_mod','mean_CB2_OD_mod','mean_CB2_BD_mod',
                   'mean_CB3_TN_mod','mean_CB3_ON_mod','mean_CB3_BN_mod','mean_CB3_TD_mod','mean_CB3_OD_mod','mean_CB3_BD_mod',
                   'mean_CB4_TN_mod','mean_CB4_ON_mod','mean_CB4_BN_mod','mean_CB4_TD_mod','mean_CB4_OD_mod','mean_CB4_BD_mod',
                   'mean_CB5_TN_mod','mean_CB5_ON_mod','mean_CB5_BN_mod','mean_CB5_TD_mod','mean_CB5_OD_mod','mean_CB5_BD_mod',
                   'mean_CB6_TN_mod','mean_CB6_ON_mod','mean_CB6_BN_mod','mean_CB6_TD_mod','mean_CB6_OD_mod','mean_CB6_BD_mod',
                   'mean_MAB_TN_mod','mean_MAB_ON_mod','mean_MAB_BN_mod','mean_MAB_TD_mod','mean_MAB_OD_mod','mean_MAB_BD_mod',
                   'mean_all_TN_modtreat','mean_all_ON_modtreat','mean_all_BN_modtreat','mean_all_TD_modtreat','mean_all_OD_modtreat','mean_all_BD_modtreat',
                   'mean_CB1_TN_modtreat','mean_CB1_ON_modtreat','mean_CB1_BN_modtreat','mean_CB1_TD_modtreat','mean_CB1_OD_modtreat','mean_CB1_BD_modtreat',
                   'mean_CB2_TN_modtreat','mean_CB2_ON_modtreat','mean_CB2_BN_modtreat','mean_CB2_TD_modtreat','mean_CB2_OD_modtreat','mean_CB2_BD_modtreat',
                   'mean_CB3_TN_modtreat','mean_CB3_ON_modtreat','mean_CB3_BN_modtreat','mean_CB3_TD_modtreat','mean_CB3_OD_modtreat','mean_CB3_BD_modtreat',
                   'mean_CB4_TN_modtreat','mean_CB4_ON_modtreat','mean_CB4_BN_modtreat','mean_CB4_TD_modtreat','mean_CB4_OD_modtreat','mean_CB4_BD_modtreat',
                   'mean_CB5_TN_modtreat','mean_CB5_ON_modtreat','mean_CB5_BN_modtreat','mean_CB5_TD_modtreat','mean_CB5_OD_modtreat','mean_CB5_BD_modtreat',
                   'mean_CB6_TN_modtreat','mean_CB6_ON_modtreat','mean_CB6_BN_modtreat','mean_CB6_TD_modtreat','mean_CB6_OD_modtreat','mean_CB6_BD_modtreat',
                   'mean_MAB_TN_modtreat','mean_MAB_ON_modtreat','mean_MAB_BN_modtreat','mean_MAB_TD_modtreat','mean_MAB_OD_modtreat','mean_MAB_BD_modtreat']

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
     dict_q25[k]=df_result.groupby(TREAT).quantile(q=0.25)
     dict_q75[k]=df_result.groupby(TREAT).quantile(q=0.75)

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

 # Just to get notification this part is finished
 print("stats finished")

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
 list_df_results_mod= list_df_results[96:144]
 list_df_results_modtreat= list_df_results[144:192]
 list_stat=[df_stat_all,df_stat_CB1,df_stat_CB2,df_stat_CB3,df_stat_CB4,df_stat_CB5,df_stat_CB6,df_stat_MAB]

 # Make lists with right files to write to excel
 list_results= list_results_titles[:48]
 list_results_min= list_results_titles[48:96]
 list_results_mod= list_results_titles[96:144]
 list_results_modtreat= list_results_titles[144:192]
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
 save_xls(list_df_results_mod,list_results_mod,out_path3)
 save_xls(list_df_results_modtreat,list_results_modtreat,out_path4)
 save_xls(list_stat,list_stat_titles,out_path5)


 # ### Run statistics
 # ##
 # ### Shapiro-Wilk Test for normality testing
 # ##from scipy.stats import shapiro
 # ##from scipy.stats import kruskal
 # ##
 # ### normality test with Shapiro-Wilk Test
 # ##dict_normtest={}
 # ##def normtest (list_dfs, list_titles):
 # ##    for dt, dataframe in enumerate(list_dfs): 
 # ##        df_name= list_titles[dt]
 # ##        for position, col_name in enumerate(list(dataframe.columns)):
 # ##            if(position>6):
 # ##                stat, p = shapiro(dataframe[col_name])
 # ##                print('Statistics=%.3f, p=%.3f' % (stat, p))
 # ##                
 # ##                # interpret
 # ##                alpha = 0.05
 # ##                if p > alpha:
 # ##                	dict_normtest[df_name,col_name]='Normal distributed (parametric)'
 # ##                else:
 # ##                	dict_normtest[df_name,col_name]='Not normally distributed (non-parametric)'
 # ##
 # ##dict_kruskaltest={}
 # ##def  kruskaltest (list_dfs, list_titles):
 # ##     for dt, dataframe in enumerate(list_dfs): 
 # ##        df_name= list_titles[dt]
 # ##        data1= dataframe.loc[dataframe[TREAT]==SA,:]
 # ##        data2= dataframe.loc[dataframe[TREAT]==SB,:]
 # ##
 # ##        for position, col_name in enumerate(list(data1.columns)):
 # ##            if(position>6):
 # ##                stat, p = kruskal(data1,data2)
 # ##
 # ##                # interpret
 # ##                alpha = 0.05
 # ##                if p > alpha:
 # ##                	dict_kruskaltest[df_name,col_name]=''
 # ##                else:
 # ##                	dict_kruskaltest[df_name,col_name]=('H=%.3f, p=%.3f' % (stat, p))
 # ## 
 # ##
 # ##
 # ##
 # ##normtest(list_df_results2,list_results)
 # ##kruskaltest(list_df_results2,list_results)
 # #
 # #
 # #
 # #
 # ##
 # ###### Make the graphs per column:
 # #####with PdfPages('results_figures.pdf') as pdf:
 # #####    for position, col_name in enumerate(list(results_duration.columns)):
 # #####        if(position>3):
 # #####            fig = plt.figure( dpi=300, figsize=(16.0, 10.0))
 # #####            plt.bar(x3, mean_duration[col_name], color= 'blue', width=barWidth, edgecolor='white')
 # #####            h1 = results_duration[col_name].max()
 # #####            highest = (h1+(h1/6))
 # #####            plt.xticks([r + 0 for r in x3], Treatment_values, rotation='vertical')
 # #####            plt.title('Results'+ col_name , fontweight = 'bold', fontsize = 16)
 # #####            plt.ylim(bottom=0, top= highest)
 # #####            plt.scatter(results['Treatment']*3-3, results[col_name], facecolors=['black'],
 # #####                              edgecolors='none',s=40, alpha=1, linewidth=1, zorder=20)
 # #####            plt.tight_layout()
 # #####            pdf.savefig(fig)
 # #####    
 # #####            plt.close()
 # #####            print(position, col_name)
 # ####
