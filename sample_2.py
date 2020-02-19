import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
import sklearn.metrics as metrics
from statistics import mean
import heapq
from sklearn.model_selection import validation_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle

  data = pd.read_csv("book.csv")
  data = data.fillna('')
  data.head()
  data = shuffle(data)
  X = pd.DataFrame(data.iloc[:,:-1])
  X
  y = pd.DataFrame(data.iloc[:,-1])
  y
  X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
  max_depth = 30
  regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth,random_state=2)
  print(regr_rf)
  regr_rf.fit(X_train, y_train.values.ravel())
  y_rf = regr_rf.predict(X_test)
  print(X_test)
  print(y_rf)
  mean_average_error = metrics.mean_absolute_error(y_test,y_rf)
  print("mean avaergae precision ",mean_average_error)
  Accuracy = (100 - mean_average_error)
  print(Accuracy)
  print('Accuracy:', round(Accuracy,2), '.%')
  param_range = np.arange(1, 250, 2)
  train_scores, test_scores = validation_curve(RandomForestClassifier(), 
                                             X, 
                                             y, 
                                             param_name="n_estimators", 
                                             param_range=param_range,
                                             cv=3, 
                                             scoring="accuracy", 
                                             n_jobs=-1)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
plt.plot(param_range, train_mean, label="Training score", color="black")
plt.plot(param_range, test_mean, label="Cross-validation score", color="red")
plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color="red")
plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color="green")
time_slot = input("Time slot for the job\t :")
time_slot_length =len(time_slot)
if time_slot_length == 6 and time_slot != '000000':
    index = X[X['TIME_SLOT']==[int(time_slot)]].index.values
    n = len(index)
    rest = []
    for i in range (n):
        yr = X.loc[index[i]]
        press = regr_rf.predict([yr])
        rest.append(press[0])
        code = mean(rest)   
    if code == 1:
        print("The job can scheduled, it has sufficient resources to run.")
    else :
        print("The resources are limited;check whether the job can run with the limited resources\n")
        print("If the job is new enter 101 as job id if not enter the corresponding job id")
        job_id = input("Job id: ")
        if job_id == '101':
            da = pd.read_csv("datares.csv")
            col = da[da.TIME_SLOT > [int(time_slot)]]
            start_index= da[da['TIME_SLOT']==[int(time_slot)]].index.values
            re = start_index
            res = re[0]
            end  = da.last_valid_index()
            end=end +1
            col = da.iloc[res:end]
            codex =1.6
            i = 1
            j=0
            dss = col["OS_CPU_IDLE"]
            while (codex > 1.5) :
                while(i<20):
                    ed = heapq.nlargest(i, dss)
                    vb = ed[j]
                    int(vb)
                    ind1 = col[col['OS_CPU_IDLE']==[vb]].index.values               
                    fe = da.iloc[int(ind1)]['OS_CPU_IDLE']
                    print("CPU_IDLE_TIME ",fe)
                    edu = da.iloc[int(ind1)]['TIME_SLOT']
                    print("TIME_SLOT",edu)
                    r=[]
                    red=[]
                    red = col[col['TIME_SLOT']==[edu]].index.values
                    for k in range (len(red)):
                        yrs = X.loc[red[k]]
                        pr = regr_rf.predict([yrs])
                        r.append(pr[0])
                    cod = mean(r)
                    if(cod < 1.2):
                        i+=20
                        codex = cod
                    else:
                        i+=1
                        j+=1
            print(edu)
            print ("The new can be scheduled at time",int(edu))
        else:
            sa = pd.read_csv("datafor.csv")
            sa.head()
            sa = sa.fillna('')
            feature = pd.DataFrame(sa.iloc[:,1:-1])
            target = pd.DataFrame(sa.iloc[:,-1])
            feature_train,feature_test,target_train,target_test=train_test_split(feature,target,test_size=0.20)
            Regressor = RandomForestRegressor(n_estimators=20,random_state=0)
            Regressor.fit(feature_train, target_train.values.ravel())
            pred = Regressor.predict(feature_test)
            mae = metrics.mean_absolute_error(target_test,pred)
            print(mae)
            accu = (100-mae)
            print(accu)
            index = sa[sa['JOB_ID']==[int(job_id)]].index.values
            rest = index[0]
            test = sa.iloc[[int(rest)]].values
            test1 = test[[0][0]]
            value = []
            for temp in test1:
                value.append(temp)
            k_test =np.array([[value[1],value[2], value[3],value[4],value[5],value[6]]])
            pred = Regressor.predict(k_test)
            if pred < 311.9:
                print("Runs successfully")
            elif pred < 312.9:
                print("Runs but takes more time")
            else:
                print("Fails")
else:
    print("Please enter a valid time slot")
