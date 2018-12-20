import numpy

class NeuralNetwork:
    def __init__(self,type = "CNN"):
        self.type = "CNN"

    def train(self):
        return

    def predict(self):
        return
#转化数据成向量
def transform(filename):
    ArrayX = []
    ArrayY = []
    maxvalue = [-1,-1,-1,-1]
    minvalue = [100,100,100,100]
    with open(filename,'r') as f:
        for each in f.readlines():
            n = each.strip("\n").split(',')
            if n[-1] == "Iris-setosa":
                ArrayY.append([1, 0, 0])
            elif n[-1] == "Iris-versicolor":
                ArrayY.append([0, 1, 0])
            elif n[-1] == "Iris-virginica":
                ArrayY.append([0, 0, 1])
            n.pop(-1)
            for i in range(0, 4):
                if float(n[i]) > maxvalue[i]:
                    maxvalue[i] = float(n[i])
                if float(n[i]) < minvalue[i]:
                    minvalue[i] = float(n[i])
            ArrayX.append(n)
    for each in ArrayX:
        each[0] = (float(each[0]) - minvalue[0]) / (maxvalue[0] - minvalue[0])
        each[1] = (float(each[1]) - minvalue[1]) / (maxvalue[1] - minvalue[1])
        each[2] = (float(each[2]) - minvalue[2]) / (maxvalue[2] - minvalue[2])
        each[3] = (float(each[3]) - minvalue[3]) / (maxvalue[3] - minvalue[3])
    return ArrayX,ArrayY

#划分测试数据和训练数据
def devide(arrayX,arrayY,train_rate,test_rate):
    train_ArrayX = []
    train_ArrayY = []
    test_ArrayX = []
    test_ArrayY = []
    train_ArrayX.extend(ArrayX[0:40])
    train_ArrayY.extend(ArrayY[0:40])
    test_ArrayX.extend(ArrayX[40:50])
    test_ArrayY.extend(ArrayY[40:50])
    print(train_ArrayX)
    print(train_ArrayY)
    print(test_ArrayX)
    print(test_ArrayY)


if __name__ == "__main__":
    filename = r"C:\Users\phuawei666\Desktop\data set\莺尾花\Iris.txt"
    neural_network = NeuralNetwork()
    ArrayX,ArrayY = transform(filename)
    print(ArrayX)
    print(ArrayY)
    train_arrayX,train_arrayY,test_arrayX,test_arrayY = devide(ArrayX,ArrayY,train_rate = 4,test_rate = 1)


