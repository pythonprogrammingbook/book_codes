import torch  
import matplotlib.pyplot as plt  
# 生成两类数据  
n_data = torch.ones(100, 2)  
x0 = torch.normal(n_data, 1)  # 类别0  
y0 = torch.zeros(100)         # 标签0  
x1 = torch.normal(-n_data, 1) # 类别1  
y1 = torch.ones(100)          # 标签1  
x = torch.cat((x0, x1), 0)    # 将两类数据连接起来  
y = torch.cat((y0, y1), 0).type(torch.LongTensor) #标签是整数  
#显示数据  
plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')  
plt.show() 
