import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

#read file
if __name__ == '__main__':
    savename= r'D:\Doc\Personal\buyComputer.dot'
    filename= r'D:\Doc\Personal\buyComputer.csv'
    f = open(filename)
    reader = csv.reader(f)

    headers = next(reader)
    print(headers)

    featureList = []
    LabelList = []

    for row in reader:
        LabelList.append(row[-1])
        rowDict = {}
        for i in range(1,len(row)-1):
            rowDict[headers[i]] = row[i]
        featureList.append(rowDict)
    for each in featureList:
        print(each)
    print('')
    print(LabelList)

    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    print(dummyX)

    lbb = preprocessing.LabelBinarizer()
    dummyY = lbb.fit_transform(LabelList)
    print(dummyY)

    clf = tree.DecisionTreeClassifier(criterion="entropy")
    clf = clf.fit(dummyX,dummyY)
    print("clf:"+str(clf))

    m = open(savename,'w')
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=m)
    # with open(savename,'w') as f:
    #     f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

    oneRowX = dummyX[0,:]
    newRowX = []
    print("oneRowX:" + str(oneRowX))
    oneRowX[0] = 1
    oneRowX[2] = 0
    print("oneRowX:" + str(oneRowX))
    newRowX.append(oneRowX)

    print("newRowX" + str(newRowX))
    predictY = clf.predict(newRowX)
    print("PredictY:"+str(predictY))