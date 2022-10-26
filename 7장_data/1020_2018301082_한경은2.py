Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import seaborn as sns
>>> import pandas as pd
>>> titanic = sns.load_dataset("titanic")
>>> titanic.to_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/titanic.csv', index = False)
>>> titanic.isnull().sum()
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
>>> titanic['age'] = titanic['age'].fillna(titanic['age'].median())
>>> titanic['embarked'].value_counts()
S    644
C    168
Q     77
Name: embarked, dtype: int64
>>> titanic['embarked'] = titanic['embarked'].fillna('S')
>>> titanic['embark_town'].value_counts()
Southampton    644
Cherbourg      168
Queenstown      77
Name: embark_town, dtype: int64
>>> titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
>>> titanic['deck'].value_counts()
C    59
B    47
D    33
E    32
A    15
F    13
G     4
Name: deck, dtype: int64
titanic['deck'] = titanic['deck'].fillna('C')
titanic.isnull().sum()
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           0
embark_town    0
alive          0
alone          0
dtype: int64
titanic.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          891 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     891 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         891 non-null    category
 12  embark_town  891 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#15>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],autopct = '%1.1f%%', ax = ax[0], shadow = True)
<AxesSubplot: ylabel='survived'>
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
<AxesSubplot: ylabel='survived'>
ax[0].set_title('Survived (Male)')
Text(0.5, 1.0, 'Survived (Male)')
ax[1].set_title('Survived (Female)')
Text(0.5, 1.0, 'Survived (Female)')
plt.show()
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#21>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
 titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],
autopct = '%1.1f%%', ax = ax[0], shadow = True)
 
SyntaxError: unexpected indent
 titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
 
SyntaxError: unexpected indent
 titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
SyntaxError: unexpected indent
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
<AxesSubplot: ylabel='survived'>
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
<AxesSubplot: ylabel='survived'>
ax[0].set_title('Survived (Male)')
Text(0.5, 1.0, 'Survived (Male)')
ax[1].set_title('Survived (Female)')
Text(0.5, 1.0, 'Survived (Female)')
plt.show()
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#31>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
titanic.survived.value_counts()
0    549
1    342
Name: survived, dtype: int64
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#34>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
f, ax = plt.subplots(1, 2, figsize = (10, 5))
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],autopct = '%1.1f%%', ax = ax[0], shadow = True)
<AxesSubplot: ylabel='survived'>
plt.show()
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
<AxesSubplot: ylabel='survived'>
ax[0].set_title('Survived (Male)')
Text(0.5, 1.0, 'Survived (Male)')
ax[1].set_title('Survived (Female)')
Text(0.5, 1.0, 'Survived (Female)')
plt.show()
plt.show()
plt.show()
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))


Warning (from warnings module):
  File "<pyshell#45>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
f, ax = plt.subplots(1, 2, figsize = (10, 5))
itanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],autopct = '%1.1f%%', ax = ax[0], shadow = True)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    itanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],autopct = '%1.1f%%', ax = ax[0], shadow = True)
NameError: name 'itanic' is not defined. Did you mean: 'titanic'?
itanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    itanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
NameError: name 'itanic' is not defined. Did you mean: 'titanic'?
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
<AxesSubplot: ylabel='survived'>
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],
autopct = '%1.1f%%', ax = ax[0], shadow = True)
<AxesSubplot: ylabel='survived'>
ax[0].set_title('Survived (Male)')
Text(0.5, 1.0, 'Survived (Male)')
ax[1].set_title('Survived (Female)')
Text(0.5, 1.0, 'Survived (Female)')
plt.show()
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#55>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
 import matplotlib.pyplot as plt
 
SyntaxError: unexpected indent
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1],
autopct = '%1.1f%%', ax = ax[0], shadow = True)
<AxesSubplot: ylabel='survived'>
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
<AxesSubplot: ylabel='survived'>
ax[0].set_title('Survived (Male)')
Text(0.5, 1.0, 'Survived (Male)')
ax[1].set_title('Survived (Female)')
Text(0.5, 1.0, 'Survived (Female)')
plt.show()
sns.countplot('pclass', hue = 'survived', data = titanic)
plt.title('Pclass vs Survived')
plt.show()
sns.countplot('pclass', hue = 'survived', data = titanic)
plt.title('Pclass vs Survived')
plt.show()
SyntaxError: multiple statements found while compiling a single statement
sns.countplot('pclass', hue = 'survived', data = titanic)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    sns.countplot('pclass', hue = 'survived', data = titanic)
TypeError: countplot() got multiple values for argument 'data'

 
plt.title('Pclass vs Survived')

Warning (from warnings module):
  File "<pyshell#67>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
Text(0.5, 1.0, 'Pclass vs Survived')
plt.show()

import seaborn as sns
import pandas as pd
titanic.survived.value_counts()
0    549
1    342
Name: survived, dtype: int64
import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))

Warning (from warnings module):
  File "<pyshell#74>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
f, ax = plt.subplots(1, 2, figsize = (10, 5))
titanic_corr = titanic.corr(method = 'pearson')

Warning (from warnings module):
  File "<pyshell#76>", line 1
FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
