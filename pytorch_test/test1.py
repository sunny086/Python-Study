# train_pytorch.py
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt  # ⭐️ 新增

# 生成假数据
X = torch.randn(100, 10)
y = torch.randn(100, 1)

# 简单的两层神经网络
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Net()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

loss_list = []  # ⭐️ 新增：记录每次 loss

# 训练循环
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    loss_list.append(loss.item())  # ⭐️ 新增
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# ⭐️ 新增：画出 Loss 曲线
plt.plot(loss_list)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.grid(True)
plt.show()
