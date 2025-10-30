import numpy as np
import pandas as pd
dataset=pd.read_csv(r'C:\Users\buthm\Downloads\drive-download-20251030T091159Z-1-001\student-marks.csv').values
avg=np.mean(dataset[:,1:4],axis=1)
avg=avg.reshape(-1,1)
def findGrade(mark):
    if(mark>=75):
        grade="A"
    elif(mark>=65):
        grade="B"
    elif(mark>=55):
        grade="C"
    elif(mark>=35):
        grade="S"
    else:
        grade="F"
    return grade
mathsGrade=np.array([findGrade(i) for i in dataset[:,1]])
mathsGrade=mathsGrade.reshape(-1,1)

phyGrade=np.array([findGrade(i) for i in dataset[:,2]])
phyGrade=phyGrade.reshape(-1,1)

chemGrade=np.array([findGrade(i) for i in dataset[:,3]])
chemGrade=chemGrade.reshape(-1,1)

dataset=np.append(dataset,mathsGrade,axis=1)
dataset=np.append(dataset,phyGrade,axis=1)
dataset=np.append(dataset,chemGrade,axis=1)
dataset=np.append(dataset,avg,axis=1)
np.save('newDataSet',dataset)