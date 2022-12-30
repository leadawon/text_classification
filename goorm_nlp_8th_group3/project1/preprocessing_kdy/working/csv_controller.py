import pandas as pd

dev0 = pd.read_csv(".sentiment_dev_0.csv")
dev1 = pd.read_csv("sentiment_dev_1.csv")
train0 = pd.read_csv("sentiment_train_0.csv")
train1 = pd.read_csv("sentiment_train_1.csv")

print(dev0)
