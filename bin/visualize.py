import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("../Data/train.csv")

colors = {'mf':['#69B4FF', '#FF69B4'], 'deadalive':["#FF0000","#09d209"], 'alivedead': ["#09d209","#FF0000"]}

# Checking to see if the Sex category has null values, thankfully it doesn't
print(df.Sex.isnull().sum().sum())
# Plots sex distribution
df.Sex.value_counts().plot(kind='bar', color=colors['mf'])

# Create subplot so I can graph the surivors/non survivors of both sexes
fig, axs = plt.subplots(1,2)

df[df.Sex=='male'].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[0], title="Men Survival")
df[df.Sex=='female'].Survived.value_counts().plot(kind='bar',color=colors['alivedead'], ax=axs[1], title="Women Survival")
plt.show()
