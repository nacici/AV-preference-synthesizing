# Synthesizing neighborhood-level AV preferences
Developed a machine-learning based microsimulation approach to understand the spatial distribution of public opinion towards privately-owned automated vehicles and shared automated vehicles. 

The approach is three folded. 

## [1] Machine Learning Classifier for AV opinions
Machine learning classifier is developed using the national public opinion survey conducted by [Dr. Robert Noland](https://bloustein.rutgers.edu/noland/) and Sicheng Wang at Rutgers University and [Dr. Andrew Mondschein](https://www.arch.virginia.edu/people/andrew-mondschein) and Zhiqiu Jiang at University of Virginia in 2017. To make the model transferrable to [2017 National Household Travel Survey (NHTS)](https://nhts.ornl.gov/), only variables that are shared by both surveys are used in the model training process. Common variables are selected, cleaned, and recoded using python notebook "common_variables_recoding" in the repository. The common variables and corresponding coding are as follows:

1. gender (male, female, other, prefer not to say)
2. hispanic (yes, no, prefer not to say)
3. race (white, african american, asian, other, prefer not to say)
4. age (Under 25 years old, 25-34 years, 35-44 years, 45-54 years, 55-64 years, 65-74 years, 75-84 years, 85 or years older)
5. generation (Baby Boomers (age 55-74); Generation X (age 35-54); Millennials (age <=34); The Silent Generation (age above 75))
6. vehicle ownership (0, 1, 2, 3, 4, 5, 6+)
7. number of kid (0, 1, 2, 3, 4+)
8. income (Under $25,000, $25,000 to under $50,000, $50,000 to under $100,000, $100,000 or greater, prefer not to say)
9. ridesharing frequency (A few teims per year, Once per month, Once per week, Several times per week, Never)
10. education (Four-year college degree, Two-year collge degree, Some College, Graduate or professional degree, High school or GED, Less than high school, Master's degree, Prefer not to say, Two-year collge degree, Other)
11. commute mode (Biking & Wlaking, Not Applicable, Other method, Personal Automobiles, Public Transit, Taxi, Uber, or Lyft)

Machine learning models are developed separately for interests in 

1. purchasing Automated Vehicles (binary);
2. sharing Automated Vehicles (i.e., using Taxi, Uber, Lyft, etc., but without drivers) (binary). 

The following machine learning models are trained and tuned in this study, using 10 fold cross validation method. Python package [scikit-learn](https://scikit-learn.org/stable/) is used.  

* sklearn.tree.DecisionTreeClassifier
* sklearn.tree.ExtraTreeClassifier
* sklearn.neighbors.KNeighborsClassifier
* sklearn.svm.LinearSV
* sklearn.linear_model.LogisticRegression
* sklearn.neural_network.MLPClassifier
* sklearn.neighbors.NearestCentroid
* sklearn.neighbors.RadiusNeighborsClassifier
* sklearn.ensemble.RandomForestClassifier
* sklearn.linear_model.RidgeClassifier
* sklearn.ensemble.GradientBoostingClassifier

## [2] NHTS data AV preferences Imputation
The finalized machine learning models are then applied to NHTS dataset (after cleaning and recoding the common variables to match that used in the machine learning models) to impute the preferences for PAVs and SAVs for each individual in the NHTS data. The process and results can be found in python notebook xxx.
  
## [3] Understanding the spatial distribution of Public Opinions
We then use the NHTS data as the seed matrix and census tract level household and personal varialbes as the marginal controls to synthesize households and population in several selected cities to understand the spatial distribution of the opinions at the census tract level. This process is implemented using PopGen1.1, an open source population synthesizer developed by [Dr. Ram Pendyala and his research team](https://www.mobilityanalytics.org/popgen.html) at Arizona State University. Note, it is also possible to synthesize to census blockgroup and/or census block level. However, it will take longer time for the mdoel to converge, when the spaital resolution is more refined. In this project, we synthesized neighborhood-level AV preferences for three cities, namely San Francisco, CA, Austin, TX, and Atlanta, GA at the census tract level. The results (in .csv format) can be found in the folder "Synthesize Results". 

## [4] Research Team
[Wenwen Zhang](https://wenwenz.com/)<br>
Assistant Professor<br>
Urban Affairs and Planning<br>
Virginia Polytechnic Institute and State University<br>
Email: wenwenz3@vt.edu<br>
<hr>
Kaidi Wang<br>
Ph.D. Student<br>
Urban Affairs and Planning<br>
Virginia Polytechnic Institute and State University<br>
Email: kaidi@vt.edu<br>
<hr>
Sicheng Wang<br>
Ph.D. Student<br>
Edward J. Bloustein School of Planning and Public Policy<br>
Rutgers University<br>
E-mail: sw826@scarletmail.rutgers.edu<br>
<hr>
Zhiqiu Jiang<br>
Ph.D. Student<br>
Department of Urban and Environmental Planning<br>
University of Virginia School of Architecture<br>
E-mail: zj3av@virginia.edu<br>
<hr>
[Andrew Mondschein](http://www.andrewmondschein.com/)<br>
Associate Professor<br>
Department of Urban and Environmental Planning<br>
University of Virginia School of Architecture<br>
E-mail: mondschein@virginia.edu<br>
<hr>
[Robert B. Noland](https://bloustein.rutgers.edu/noland/)<br>
Distinguished Professor<br>
Edward J. Bloustein School of Planning and Public Policy<br>
Rutgers University<br>
E-mail: rnoland@ejb.rutgers.edu<br>




