import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('datasets/DatosProduccion.csv', sep = ';', decimal = ',')
print(df.head(5))
print(df['Horas Trabajadas'].head(10))

x1 = df['Horas Trabajadas'].values.reshape((-1,1)) # Variable independiente
x2 = df['Horas Descanso'].values.reshape((-1,1)) # Variable independiente
y = df['Productos Terminados'].values.reshape((-1,1)) # Variable dependiente

# train and test
model = LinearRegression()

variablex = np.concatenate # auxiliar variable
x_train, x_test, y_train, y_test = train_test_split(x1, y, test_size = 0.2, random_state = 42) # split the train and test datasets
model.fit(x_train, y_train) # train model

y_pred = model.predict(x_test) # predict
print(y_pred[0:10])
mse = mean_squared_error(y_test, y_pred) # mean squared error
print(mse)
print(f'Coeficiente m: {model.coef_[0][0]}')
print(f'Intercepto b: {model.intercept_[0]}')
print(f'ecuacion del plano: y = {model.coef_[0][0]}Horas trabajadas + {model.coef_[0][0]}Horas de descanso + {model.intercept_}')
print(f'Ecuacion del plano: y = {model.coef_[0][0]}x1 + {model.coef_[0][0]}x2 + {model.intercept_}')

fig = plt.figure()
plt.rcParams['figure.figsize'] = (8,8)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x_test[:,0], x_test[:,1], y_test, c = 'b', marker = 'o')
ax.scatter(x_test[:,0], x_test[:,1], y_pred, c = 'r', marker = 'o')

xaux = np.linspace(x_test[:,0].min(), x_test[:,0].max(), num=10)
yaux = np.linspace(x_test[:,1].min(), x_test[:,1].max(), num=10)
xaux, yaux = np.meshgrid(xaux, yaux)

z = model.intercept_ + model.coef_[0][0]*xaux + model.coef_[0][1]*yaux
ax.plot_surface(xaux, yaux, z, alpha = 0.6)
ax.set_xlabel('Horas trabajadas')
ax.set_ylabel('Horas de descanso')
ax.set_zlabel('Productos')
plt.legend(fontsize = 12, loc="upper right")
plt.show()