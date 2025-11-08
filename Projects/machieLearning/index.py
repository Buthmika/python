
import pandas as pd


dataset=pd.read_csv(r'C:\Users\buthm\Downloads\drive-download-20251108T071551Z-1-001\iris.csv').values

# print(dataset.shape)
# print(dataset)
data=dataset[:,0:4]
target=dataset[:,4]
print(data)
print(target)
print("---------------------------------------------------------------------------------")

from sklearn.model_selection import train_test_split
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.2)
print(train_data.shape)
print(test_data.shape)



from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()