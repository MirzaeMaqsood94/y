import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error


boston = load_boston()
df_x = pd.DataFrame(boston.data)
df_y = pd.DataFrame(boston.target)

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=42)

reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)

print(y_pred)
print(y_test)

print(mean_squared_error(y_test, y_pred))
print(f"{reg.score(x_test, y_test) * 100:.2f}%.")

