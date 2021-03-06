from sklearn.ensemble import GradientBoostingClassifier
import pickle
import pandas as pd
from sklearn.utils import resample

clf_file = "../Model/PAV_GradientBoostingClassifier.pickle"

with open(clf_file, "rb") as handle:
	clf = pickle.load(handle)

fav_file = "../fav.csv"
nhts_file = "../NHTS_SAV_ATLANTA.csv"
target_v_name = "Target_PAV_1.0"

df_fav = pd.read_csv(fav_file)
df_nhts = pd.read_csv(nhts_file)

df_fav = df_fav.dropna(subset=[target_v_name])
print df_fav[target_v_name].value_counts()


df_majority = df_fav[df_fav[target_v_name] == 0]
df_minority = df_fav[df_fav[target_v_name] == 1]

df_majority_downsampled = resample(df_majority, 
                                 replace=False,    # sample without replacement
                                 n_samples=277,     # to match minority class
                                 random_state=123)
X = pd.concat([df_majority_downsampled, df_minority])

print X[target_v_name].value_counts()

y_fav = X[[target_v_name]].values
X_fav = X.drop([target_v_name,"Target_SAV_1.0"], 1)


clf.fit(X_fav,y_fav)
print clf.score(X_fav,y_fav)
x_nhts = df_nhts.drop(["HOUSEID","PERSONID","SAV"], axis = 1)
pred = clf.predict(x_nhts)
print len(pred)

print "percent PAV in the nhts data", float(pred.sum())/len(df_nhts), len(df_nhts)
print "percent PAV in the fav data", 189.0/641	

pred = pd.DataFrame({"PAV":pred})
nhts = pd.concat([df_nhts, pred], axis = 1) # axis = 1 conbine columns together
nhts.to_csv("../NHTS_SAV_PAV_ATLANTAcsv", index= False)




