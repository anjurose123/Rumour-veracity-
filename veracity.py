import pandas
from pandas.plotting import scatter_matrix
#import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


dataset = pandas.read_csv('veracity_final.csv')
array = dataset.values
#print array
#print'-------------------------------------------------------------------------------------\n\n'
X = array[:,0:10]
#print X
#print'-------------------------------------------------------------------------------------\n\n'
Y = array[:,10]
#print Y
#print'-------------------------------------------------------------------------------------\n\n'
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#print (X_train.head(5))
seed = 7
scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
print 'Accuracy of models - mean (std.devaition)'
print'----------------------------------------------------------------------\n\n'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)



print'----------------------------------------------------------------------\n\n'
'''fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()'''

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
#print X_validation
#print '-----------------------------------------'
predictions = knn.predict(X_validation)
#print predictions
print 'Accuracy testing'
print(accuracy_score(Y_validation, predictions))
print'----------------------------------------------------------------------\n\n'
print 'Confusion_matrix'
print(confusion_matrix(Y_validation, predictions))
print'----------------------------------------------------------------------\n\n'
print 'Classification_Report'
print(classification_report(Y_validation, predictions))
print'----------------------------------------------------------------------\n\n'
