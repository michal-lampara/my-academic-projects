import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix
import numpy as np
import mlxtend
from mlxtend.plotting import heatmap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import scipy as sp
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("housing.csv")
df.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

df.head()
cols = ["LSTAT", "INDUS", "NOX", "RM", "MEDV"]

print(df)
print(cols)

scatterplotmatrix(df[cols].values, figsize=(10,8), names=cols, alpha=0.5)
plt.tight_layout()
plt.show()

# LSTAT to MEDV
def lin_regplot(X, y, model):
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="black", lw=2)
    return

X = df[["LSTAT"]].values
y = df["MEDV"].values
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel("% lower status of the population [LSTAT]")
plt.ylabel("Price in $1000s [MEDV]")
plt.show()

# MEDV to CRIM
def lin_regplot(X, y, model):
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="black", lw=2)
    return

X = df[["MEDV"]].values
y = df["CRIM"].values
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel("Price in $1000s [MEDV]")
plt.ylabel("Per capita crime rate by town [CRIM]")
plt.show()


# B to CRIM
def lin_regplot(X, y, model):
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="black", lw=2)
    return

X = df[["B"]].values
y = df["CRIM"].values
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel("Proportion of Blacks in town [B]")
plt.ylabel("Per capita crime rate by town [CRIM]")
plt.show()

#----------------------------------------------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

X = np.array([258.0, 270.0, 294.0,
              320.0, 342.0, 368.0,
              396.0, 446.0, 480.0, 
              586.0])[:, np.newaxis]
y = np.array([236.4, 234.4, 252.8,
              298.6, 314.2, 342.2,
              360.8, 368.0, 391.2,
              390.8])

lr = LinearRegression()
pr = LinearRegression()
quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X)

lr.fit(X, y)
X_fit = np.arange(250,600,10)[:, np.newaxis]
y_lin_fit = lr.predict(X_fit)

pr.fit(X_quad, y)
y_quad_fit = pr.predict(quadratic.fit_transform(X_fit))

plt.scatter(X, y, label="Training points")
plt.plot(X_fit, y_lin_fit, label="Linear fit", linestyle="--")
plt.plot(X_fit, y_quad_fit, label="Quadratic fit")
plt.xlabel("Explanatory variable")
plt.ylabel("Predicted or known target values")
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()

y_lin_pred = lr.predict(X)
y_quad_pred = pr.predict(X_quad)

print("Training MSE linear: %.3f, quadratic: %.3f" % (mean_squared_error(y, y_lin_pred),mean_squared_error(y, y_quad_pred)))
print("Training R^2 linear: %.3f, quadratic: %.3f" % (r2_score(y, y_lin_pred),r2_score(y, y_quad_pred)))

#---------------------------------------------------------------------------------------------------------------------------
X = df[["LSTAT"]].values
y = df["MEDV"].values

regr = LinearRegression()

quadratic = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
X_quad = quadratic.fit_transform(X)
X_cubic = cubic.fit_transform(X)

X_fit = np.arange(X.min(), X.max(), 1)[:, np.newaxis]

regr = regr.fit(X,y)
y_lin_fit = regr.predict(X_fit)
linear_r2 = r2_score(y, regr.predict(X))

regr = regr.fit(X_quad,y)
y_quad_fit = regr.predict(quadratic.fit_transform(X_fit))
quadratic_r2 = r2_score(y, regr.predict(X_quad))

regr = regr.fit(X_cubic,y)
y_cubic_fit = regr.predict(cubic.fit_transform(X_fit))
cubic_r2 = r2_score(y, regr.predict(X_cubic))

plt.scatter(X, y, label="Training points", color="lightgrey")

plt.plot(X_fit, y_lin_fit, label="Linear (d=1), $R^2=%.2f$" %linear_r2, color="blue", lw=2, linestyle=":")
plt.plot(X_fit, y_quad_fit, label="Quadratic (d=2), $R^2=%.2f$" %quadratic_r2, color="red", lw=2, linestyle="-")
plt.plot(X_fit, y_cubic_fit, label="Cubic (d=3), $R^2=%.2f$" %cubic_r2, color="green", lw=2, linestyle="--")

plt.xlabel("% lower status of population [LSTAT]")
plt.ylabel("Price in $1000s [MEDV]")
plt.legend(loc="upper right")

plt.show()

#---------------------------------------------------------------------------------------------------------------------------
