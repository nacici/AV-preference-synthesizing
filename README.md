# AV-opinion
Developed a machine-learning based microsimulation approach to understand the spatial distribution of public opinion towards privately-owned automated vehicles and shared automated vehicles. 

The approach is three folded. 

<ol>
  
<b><li>Machine Learning Classifier for AV opinions</li></b>
Machine learning classifier is developed using the national public opinion survey conducted by Dr. Robert Noland and Sicheng Wang at Rutgers University and Andrew  and Xiaoqiu Jiang at University of Virginia in 2017. To make the model transferrable to National Household Travel Survey, only variables that are shared by both survey are used in the model training process. Common variables are selected, cleaned, and recoded using python notebook xxx in the repository. Machine learning models are developed separately for interests in (1) purchasing Automated Vehicles and (2) sharing Automated Vehicles (i.e., using Taxi, Uber, Lyft, etc., but without drivers). The best machine learning models are applied to survey data from Seattle to validate the developed models (thanks for xx for sharing the seattle travel survey!). Please check python notebook xx and xx to for model performance on national public opinion survey data and seattle travel survey data. 
   
<b><li>Statistically Joining/Imputing AV opinions to NHTS data</li></b>
The finalized machien learning models are then applied to NHTS dataset (after cleaning and recoding the common variables to match that used in the machine learning models) to statistically joining or imputing the AV opinions to NHTS data. The process and results can be found in python notebook xxx.
  
<b><li>Understanding the spatial distribution of Public Opinions</li></b>
We then use the NHTS data as the seed matrix and census tract level household and personal varialbes as the marginal controls to synthesize households and population in several selected cities to understand the spatial distribution of the opinions at the census tract level. This process is implemented using PopGen1.1, an open source population synthesizer developed by Dr. Ram Pendyala and his research team at Arizona State University. Note, it is also possible to synthesize to census blockgroup and/or census block level. However, it will take longer time for the mdoel to converge, when the spaital resolution is more refined. The results are visualized in the python notebook xxx. 
</ol>
 
In this repository, we share the % of willingness to adopt PAV and SAV at the census tract level for researchers for further analysis. The data is saved in csv format. 


