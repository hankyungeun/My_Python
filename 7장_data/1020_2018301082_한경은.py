Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
red_df = pd.read_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/winequality-red.csv', sep = ';', header = 0, engine = 'python')
white_df = pd.read_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/winequality-white.csv', sep = ';', header = 0, engine= 'python')
red_df.to_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/winequality-red2.csv', index = False)
white_df.to_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/winequality-white2.csv', index = False)
red_df.head()
   fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
0            7.4              0.70         0.00  ...       0.56      9.4        5
1            7.8              0.88         0.00  ...       0.68      9.8        5
2            7.8              0.76         0.04  ...       0.65      9.8        5
3           11.2              0.28         0.56  ...       0.58      9.8        6
4            7.4              0.70         0.00  ...       0.56      9.4        5

[5 rows x 12 columns]
red_df.insert(0, column = 'type', value = 'red')
red_df.head()
  type  fixed acidity  volatile acidity  ...  sulphates  alcohol  quality
0  red            7.4              0.70  ...       0.56      9.4        5
1  red            7.8              0.88  ...       0.68      9.8        5
2  red            7.8              0.76  ...       0.65      9.8        5
3  red           11.2              0.28  ...       0.58      9.8        6
4  red            7.4              0.70  ...       0.56      9.4        5

[5 rows x 13 columns]
red_df.shape
(1599, 13)
white_df.head()
   fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
0            7.0              0.27         0.36  ...       0.45      8.8        6
1            6.3              0.30         0.34  ...       0.49      9.5        6
2            8.1              0.28         0.40  ...       0.44     10.1        6
3            7.2              0.23         0.32  ...       0.40      9.9        6
4            7.2              0.23         0.32  ...       0.40      9.9        6

[5 rows x 12 columns]
white_df.insert(0, column = 'type', value = 'white')
white_df.head()
    type  fixed acidity  volatile acidity  ...  sulphates  alcohol  quality
0  white            7.0              0.27  ...       0.45      8.8        6
1  white            6.3              0.30  ...       0.49      9.5        6
2  white            8.1              0.28  ...       0.44     10.1        6
3  white            7.2              0.23  ...       0.40      9.9        6
4  white            7.2              0.23  ...       0.40      9.9        6

[5 rows x 13 columns]
white_df.shape
(4898, 13)
wine = pd.concat([red_df, white_df])
wine.shape
(6497, 13)
wine.to_csv('/Users/hangyeong-eun/Documents/My_Python/7장_data/wine.csv', index = False)
print(wine.info())
<class 'pandas.core.frame.DataFrame'>
Int64Index: 6497 entries, 0 to 4897
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   type                  6497 non-null   object 
 1   fixed acidity         6497 non-null   float64
 2   volatile acidity      6497 non-null   float64
 3   citric acid           6497 non-null   float64
 4   residual sugar        6497 non-null   float64
 5   chlorides             6497 non-null   float64
 6   free sulfur dioxide   6497 non-null   float64
 7   total sulfur dioxide  6497 non-null   float64
 8   density               6497 non-null   float64
 9   pH                    6497 non-null   float64
 10  sulphates             6497 non-null   float64
 11  alcohol               6497 non-null   float64
 12  quality               6497 non-null   int64  
dtypes: float64(11), int64(1), object(1)
memory usage: 710.6+ KB
None
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()
  type  fixed_acidity  volatile_acidity  ...  sulphates  alcohol  quality
0  red            7.4              0.70  ...       0.56      9.4        5
1  red            7.8              0.88  ...       0.68      9.8        5
2  red            7.8              0.76  ...       0.65      9.8        5
3  red           11.2              0.28  ...       0.58      9.8        6
4  red            7.4              0.70  ...       0.56      9.4        5

[5 rows x 13 columns]
wine.describe()
       fixed_acidity  volatile_acidity  ...      alcohol      quality
count    6497.000000       6497.000000  ...  6497.000000  6497.000000
mean        7.215307          0.339666  ...    10.491801     5.818378
std         1.296434          0.164636  ...     1.192712     0.873255
min         3.800000          0.080000  ...     8.000000     3.000000
25%         6.400000          0.230000  ...     9.500000     5.000000
50%         7.000000          0.290000  ...    10.300000     6.000000
75%         7.700000          0.400000  ...    11.300000     6.000000
max        15.900000          1.580000  ...    14.900000     9.000000

[8 rows x 12 columns]
sorted(wine.quality.unique())
[3, 4, 5, 6, 7, 8, 9]
wine.quality.value_counts()
6    2836
5    2138
7    1079
4     216
8     193
3      30
9       5
Name: quality, dtype: int64
wine.groupby('type')['quality'].describe()
        count      mean       std  min  25%  50%  75%  max
type                                                      
red    1599.0  5.636023  0.807569  3.0  5.0  6.0  6.0  8.0
white  4898.0  5.877909  0.885639  3.0  5.0  6.0  6.0  9.0
wine.groupby('type')['quality'].mean()
type
red      5.636023
white    5.877909
Name: quality, dtype: float64
wine.groupby('type')['quality'].std()
type
red      0.807569
white    0.885639
Name: quality, dtype: float64
wine.groupby('type')['quality'].agg(['mean', 'std'])
           mean       std
type                     
red    5.636023  0.807569
white  5.877909  0.885639
from scipy import stats
from statsmodels.formula.api import ols, glm
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']

stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
Ttest_indResult(statistic=-10.149363059143164, pvalue=8.168348870049682e-24)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + \ residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + \ density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data = wine).fit()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    regression_result = ols(Rformula, data = wine).fit()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/statsmodels/base/model.py", line 200, in from_formula
    tmp = handle_formula_data(data, None, formula, depth=eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/statsmodels/formula/formulatools.py", line 63, in handle_formula_data
    result = dmatrices(formula, Y, depth, return_type='dataframe',
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 309, in dmatrices
    (lhs, rhs) = _do_highlevel_design(formula_like, data, eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 164, in _do_highlevel_design
    design_infos = _try_incr_builders(formula_like, data_iter_maker, eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 62, in _try_incr_builders
    formula_like = ModelDesc.from_formula(formula_like)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/desc.py", line 164, in from_formula
    tree = parse_formula(tree_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/parse_formula.py", line 146, in parse_formula
    tree = infix_parse(_tokenize_formula(code, operator_strings),
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/infix_parser.py", line 210, in infix_parse
    for token in token_source:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/parse_formula.py", line 89, in _tokenize_formula
    for pytype, token_string, origin in it:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/util.py", line 349, in next
    return six.advance_iterator(self._it)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/tokens.py", line 40, in python_tokenize
    raise PatsyError("error tokenizing input "
patsy.PatsyError: error tokenizing input (maybe an unclosed string?)
    quality ~ fixed_acidity + volatile_acidity + citric_acid + \ residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + \ density + pH + sulphates + alcohol
                                                              ^
regression_result.summary()
                     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    regression_result.summary()
NameError: name 'regression_result' is not defined
regression_result = ols(Rformula, data = wine).fit()
                     
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    regression_result = ols(Rformula, data = wine).fit()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/statsmodels/base/model.py", line 200, in from_formula
    tmp = handle_formula_data(data, None, formula, depth=eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/statsmodels/formula/formulatools.py", line 63, in handle_formula_data
    result = dmatrices(formula, Y, depth, return_type='dataframe',
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 309, in dmatrices
    (lhs, rhs) = _do_highlevel_design(formula_like, data, eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 164, in _do_highlevel_design
    design_infos = _try_incr_builders(formula_like, data_iter_maker, eval_env,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/highlevel.py", line 62, in _try_incr_builders
    formula_like = ModelDesc.from_formula(formula_like)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/desc.py", line 164, in from_formula
    tree = parse_formula(tree_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/parse_formula.py", line 146, in parse_formula
    tree = infix_parse(_tokenize_formula(code, operator_strings),
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/infix_parser.py", line 210, in infix_parse
    for token in token_source:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/parse_formula.py", line 89, in _tokenize_formula
    for pytype, token_string, origin in it:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/util.py", line 349, in next
    return six.advance_iterator(self._it)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/patsy/tokens.py", line 40, in python_tokenize
    raise PatsyError("error tokenizing input "
patsy.PatsyError: error tokenizing input (maybe an unclosed string?)
    quality ~ fixed_acidity + volatile_acidity + citric_acid + \ residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + \ density + pH + sulphates + alcohol
                                                              ^
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
                     
regression_result = ols(Rformula, data = wine).fit()

regression_result.summary()
                     
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.292
Model:                            OLS   Adj. R-squared:                  0.291
Method:                 Least Squares   F-statistic:                     243.3
Date:                Thu, 20 Oct 2022   Prob (F-statistic):               0.00
Time:                        12:22:21   Log-Likelihood:                -7215.5
No. Observations:                6497   AIC:                         1.445e+04
Df Residuals:                    6485   BIC:                         1.454e+04
Df Model:                          11                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept               55.7627     11.894      4.688      0.000      32.447      79.079
fixed_acidity            0.0677      0.016      4.346      0.000       0.037       0.098
volatile_acidity        -1.3279      0.077    -17.162      0.000      -1.480      -1.176
citric_acid             -0.1097      0.080     -1.377      0.168      -0.266       0.046
residual_sugar           0.0436      0.005      8.449      0.000       0.033       0.054
chlorides               -0.4837      0.333     -1.454      0.146      -1.136       0.168
free_sulfur_dioxide      0.0060      0.001      7.948      0.000       0.004       0.007
total_sulfur_dioxide    -0.0025      0.000     -8.969      0.000      -0.003      -0.002
density                -54.9669     12.137     -4.529      0.000     -78.760     -31.173
pH                       0.4393      0.090      4.861      0.000       0.262       0.616
sulphates                0.7683      0.076     10.092      0.000       0.619       0.917
alcohol                  0.2670      0.017     15.963      0.000       0.234       0.300
==============================================================================
Omnibus:                      144.075   Durbin-Watson:                   1.646
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              324.712
Skew:                          -0.006   Prob(JB):                     3.09e-71
Kurtosis:                       4.095   Cond. No.                     2.49e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.49e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
sample1 = wine[wine.columns.difference(['quality', 'type'])]
                     
sample1 = sample1[0:5][:]
                     
sample1_predict = regression_result.predict(sample1)
                     
sample1_predict
                     
0    4.997607
1    4.924993
2    5.034663
3    5.680333
4    4.997607
dtype: float64
wine[0:5]['quality’]
          
SyntaxError: unterminated string literal (detected at line 1)
wine[0:5]['quality']
          
0    5
1    5
2    5
3    6
4    5
Name: quality, dtype: int64
data = {"fixed_acidity" : [8.5, 8.1], "volatile_acidity":[0.8, 0.5], "citric_acid":[0.3, 0.4], "residual_sugar":[6.1, 5.8], "chlorides":[0.055, 0.04], "free_sulfur_dioxide":[30.0, 31.0], "total_sulfur_dioxide":[98.0, 99], "density":[0.996, 0.91], "pH":[3.25, 3.01], "sulphates":[0.4, 0.35], "alcohol":[9.0, 0.88]}
          
sample2 = pd.DataFrame(data, columns= sample1.columns)
          
sample2
          
   alcohol  chlorides  ...  total_sulfur_dioxide  volatile_acidity
0     9.00      0.055  ...                  98.0               0.8
1     0.88      0.040  ...                  99.0               0.5

[2 rows x 11 columns]
sample2_predict = regression_result.predict(sample2)
          
sample2_predict
          
0    4.809094
1    7.582129
dtype: float64
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')

Warning (from warnings module):
  File "<pyshell#52>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(white_wine_quality, kde = True, label = 'white wine')

Warning (from warnings module):
  File "<pyshell#53>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')


Warning (from warnings module):
  File "<pyshell#54>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')

Warning (from warnings module):
  File "<pyshell#55>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')


Warning (from warnings module):
  File "<pyshell#56>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')
          

Warning (from warnings module):
  File "<pyshell#57>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')

Warning (from warnings module):
  File "<pyshell#61>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')


Warning (from warnings module):
  File "<pyshell#62>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')

Warning (from warnings module):
  File "<pyshell#63>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<AxesSubplot: xlabel='quality', ylabel='Density'>
plt.title("Quality of Wine Type")
Text(0.5, 1.0, 'Quality of Wine Type')
plt.legend()
<matplotlib.legend.Legend object at 0x168f12200>
plt.show()
import statsmodels.api as sm
others = list(set(wine.columns).difference(set(["quality", "fixed_acidity"])))
>>> p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data = wine, ret_coords = True)
eval_env: 1
>>> plt.show()
>>> fig = plt.figure(figsize = (8, 13))

Warning (from warnings module):
  File "<pyshell#71>", line 1
MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
>>> sm.graphics.plot_partregress_grid(regression_result, fig = fig)
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
eval_env: 1
<Figure size 1600x2600 with 12 Axes>
>>> plt.show()
>>> plt.show()
>>> 
================================ RESTART: Shell ================================
>>> plt.show()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    plt.show()
NameError: name 'plt' is not defined
>>> fig = plt.figure(figsize = (8, 13))
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fig = plt.figure(figsize = (8, 13))
NameError: name 'plt' is not defined
