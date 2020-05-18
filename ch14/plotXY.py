import torch  
import matplotlib.pyplot as plt  
# x: 生成100个等间距点位于[-1,1]  
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  
# y = x^2 + rand()  
y = x.pow(2) + 0.2 * torch.rand(x.size())  
# 画出x和y关系图  
plt.scatter(x.data.numpy(), y.data.numpy())
plt.xlabel("X")
plt.ylabel("Y")
plt.show() 
