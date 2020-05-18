import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
# 生成两类数据
n_data = torch.ones(100, 2)
x0 = torch.normal(n_data, 1)  # 类别0
y0 = torch.zeros(100)         # 标签0
x1 = torch.normal(-n_data, 1) # 类别1
y1 = torch.ones(100)          # 标签1
x = torch.cat((x0, x1), 0)    # 将两类数据连接起来
y = torch.cat((y0, y1), 0).type(torch.LongTensor) #标签是整数

# 定义一个Neuron Networks类，
class NN(torch.nn.Module):
    def __init__(self):
        super().__init__()  #初始化父类
        #由于每个样本有两个特征值，所以输入层为两个神经元
        self.hidden = torch.nn.Linear(2, 10)  #定义隐藏层，十个神经元
        self.output = torch.nn.Linear(10, 2)  #定义输出层，二个神经元

    def forward(self, x):
        x = F.relu(self.hidden(x))  #隐藏层使用relu()激活函数
        x = self.output(x)  #输出层不使用激活函数
        return x

nn = NN()  #实例化一个神经网络
print(nn)  #输出神经网络结构
plt.ion()  #启动matplotlib交互模式

optimizer = torch.optim.SGD(nn.parameters(), lr=0.02)  #选择SGD作为优化器
loss_func = torch.nn.CrossEntropyLoss()   #分类应用选择交叉熵作为损失函数
# 神经网络训练过程
for step in range(200):
    prediction = nn(x)  #计算预测值
    loss = loss_func(prediction, y)  # 计算loss值
    optimizer.zero_grad()  #将梯度清零
    loss.backward()  #反向传播求梯度
    optimizer.step()  #更新所有参数
    if step % 5 == 0:  #每五步可视化训练结果
        plt.cla()
        pred = torch.max(prediction, 1)[1]
        pred_y = pred.data.numpy()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        plt.text(1.5, 4, 'Loss=%.3f' % loss.data.float(), fontdict={'size': 20,'color': 'red'})
        plt.pause(0.1)
plt.ioff()
plt.show()