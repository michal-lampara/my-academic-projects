import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix
import numpy as np
import mlxtend
from mlxtend.plotting import heatmap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import scipy as sp
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import LassoCV

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("car_data_beznazw.csv")
df.columns = ["Car_Name","Year","Selling_Price","Present_Price","Driven_kms","Fuel_Type","Selling_type","Transmission","Owner"]

df.head()
cols = ["Year", "Driven_kms", "Owner", "Transmission", "Present_Price"]

print(df)
print(cols)

scatterplotmatrix(df[cols].values, figsize=(16,16), names=cols, alpha=0.5)
plt.tight_layout()
plt.show()

# Year to Present_Price
def lin_regplot(X, y, model):
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="black", lw=2)
    return

X = df[["Year"]].values
y = df["Present_Price"].values
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel("Year")
plt.ylabel("Present Price")
plt.show()

# Selling_Price to Present_Price
def lin_regplot(X, y, model):
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="black", lw=2)
    return

X = df[["Selling_Price"]].values
y = df["Present_Price"].values
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel("Selling Price")
plt.ylabel("Present Price")
plt.show()

#----------------------------------------------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

X = np.array([5.59, 270.0, 294.0,
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
X = df[["Year"]].values
y = df["Selling_Price"].values

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

plt.xlabel("Year")
plt.ylabel("Selling Price")
plt.legend(loc="upper right")

plt.show()

#---------------------------------------------------------------------------------------------------------------------------
