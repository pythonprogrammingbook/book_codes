import numpy as np  
class Neuron: #定义一个Neuron类  
    def __init__(self, weights, bias): #获得权重和偏置  
        self.weights = weights  
        self.bias = bias  
    def relu(self, z): #定义激活函数relu  
        return max(0,z)
    def feedforward(self, inputs):  
    #神经元输入与权重(Weights)相乘，再与偏置(bias)相加  
        z = np.dot(self.weights, inputs) + self.bias  
        return self.relu(z) #返回经过激活函数处理的神经元输出
