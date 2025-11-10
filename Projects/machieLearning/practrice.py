import pandas as pd

from Projects.machieLearning.index import predicted_target

dataset=pd.read_csv(r'C:\Users\buthm\Downloads\drive-download-20251108T071551Z-1-001\iris.csv').values
# print(dataset)
data=dataset[:,0:4]
target=dataset[:,4]
# print(data)
# print(target)
from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.2)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(train_data,train_target)
predicted_target=model.predict(test_data)
print("Actual Target:",test_target)
print("Predicted Target:",predicted_target)