import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
# x: 生成100个等间距点位于[-1,1]
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
# y = x^2 + rand()
y = x.pow(2) + 0.2 * torch.rand(x.size())
# 画出x和y关系图
#plt.scatter(x.data.numpy(), y.data.numpy())
#plt.show()

# 定义一个Neuron Networks类，
class NN(torch.nn.Module):
    def __init__(self):
        super().__init__() #初始化父类
        self.hidden = torch.nn.Linear(1, 10) #定义隐藏层，十个神经元
        self.output = torch.nn.Linear(10, 1) #定义输出层，一个神经元

    def forward(self, x):
        x = F.relu(self.hidden(x)) #隐藏层使用relu()激活函数
        x = self.output(x)         #输出层不使用激活函数
        return x

nn = NN() #实例化一个神经网络
print(nn) #输出神经网络结构
plt.ion() #启动matplotlib交互模式

optimizer = torch.optim.SGD(nn.parameters(), lr=0.2)  #选择SGD作为优化器
loss_func = torch.nn.MSELoss()  #选择均方差作为损失函数
# 神经网络训练过程
for step in range(200):
    prediction = nn(x) #计算预测值
    loss = loss_func(prediction, y) # 计算loss值
    optimizer.zero_grad() #将梯度清零
    loss.backward()  #反向传播求梯度
    optimizer.step() #更新所有参数
    if step % 5 == 0:#每五步可视化训练结果
        plt.cla()
        plt.xlim(-1.5, 1.5)
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.3f'%loss.data.float(), fontdict={'size': 20,'color': 'red'})
        plt.pause(0.1)
plt.ioff()
plt.show()