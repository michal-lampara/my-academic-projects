import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

columns = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason',
              'guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities',
              'nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health',
              'absences','G1','G2','G3']
df = pandas.read_csv("student-mat.csv", names=columns)
print(df)

#SCHOOL
d = {'GP':0, 'MS':1}
df['school'] = df['school'].map(d)

#SEX
d = {'M':0, 'F':1}
df['sex'] = df['sex'].map(d)

#AGE
d = {'15':0, '16':1, '17':2, '18':3, '19':4, '20':5, '21':6, '22':7}
df['age'] = df['age'].map(d)

#ADDRESS
d = {'U':0, 'R':1}
df['address'] = df['address'].map(d)

#FAMILY SIZE
d = {'GT3':0, 'LE3':1}
df['famsize'] = df['famsize'].map(d)

#PARENT STATUS   A-Apart | T-Living Together
d = {'A':0, 'T':1}
df['Pstatus'] = df['Pstatus'].map(d)

#MOTHER JOB
d = {'15':0, '16':1, '17':2, '18':3, '19':4, '20':5, '21':6, '22':7}
df['Mjob'] = df['Mjob'].map(d)

#FATHER JOB
d = {'at_home':0, 'health':1, 'services':2, 'teacher':3, 'other':4, '20':5, '21':6, '22':7}
df['Fjob'] = df['Fjob'].map(d)

#REASON
d = {'home':0, 'other':1, 'reputation':2, 'course':3}
df['reason'] = df['reason'].map(d)

#GUARDIAN
d = {'other':0, 'mother':1, 'father':2}
df['guardian'] = df['guardian'].map(d)

#SCHOOLSUP
d = {'yes':0, 'no':1}
df['schoolsup'] = df['schoolsup'].map(d)

#FAMSUP
d = {'yes':0, 'no':1}
df['famsup'] = df['famsup'].map(d)

#PAID
d = {'yes':0, 'no':1}
df['paid'] = df['paid'].map(d)

#ACTIVITIES
d = {'yes':0, 'no':1}
df['activities'] = df['activities'].map(d)

#NURSERY
d = {'yes':0, 'no':1}
df['nursery'] = df['nursery'].map(d)

#HIGHER
d = {'yes':0, 'no':1}
df['higher'] = df['higher'].map(d)

#INTERNET
d = {'yes':0, 'no':1}
df['internet'] = df['internet'].map(d)

#ROMANTIC
d = {'yes':0, 'no':1}
df['romantic'] = df['romantic'].map(d)

features = ['sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']

X = df[features]
y = df['school']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X,y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('decisiontree.png')

img = pltimg.imread('decisiontree.png')
imgplot = plt.imshow(img)
plt.show()

tree.plot_tree(dtree,feature_names=features)