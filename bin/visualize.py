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


# Create subplot for Pclasses
fig, axs = plt.subplots(1,3)
df[df.Pclass==1].Survived.value_counts().plot(kind='bar', color=colors['alivedead'], ax=axs[0], title='Pclass 1 Survival')
df[df.Pclass==2].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[1], title='Pclass 2 Survival')
df[df.Pclass==3].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[2], title='Pclass 3 Survival')

# Subplot for male pclass plot
fig, axs = plt.subplots(1,3)
df[(df.Pclass==1) & (df.Sex=='male')].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[0], title='Pclass 1 Male Survival')
df[(df.Pclass==2) & (df.Sex=='male')].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[1], title='Pclass 2 Male Survival')
df[(df.Pclass==3) & (df.Sex=='male')].Survived.value_counts().plot(kind='bar', color=colors['deadalive'], ax=axs[2], title='Pclass 3 Male Survival')

fig, axs = plt.subplots(1,3)
df[(df.Pclass==1) & (df.Sex=='female')].Survived.value_counts().plot(kind='bar', color=colors['alivedead'], ax=axs[0], title='Pclass 1 Women Survival')
df[(df.Pclass==2) & (df.Sex=='female')].Survived.value_counts().plot(kind='bar', color=colors['alivedead'], ax=axs[1], title='Pclass 2 Women Survival')
df[(df.Pclass==3) & (df.Sex=='female')].Survived.value_counts().plot(kind='bar', color=colors['alivedead'], ax=axs[2], title='Pclass 3 Women Survival')

plt.show()
