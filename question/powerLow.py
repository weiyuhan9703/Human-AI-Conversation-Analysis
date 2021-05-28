#!/usr/bin/env python
# -*-coding:utf-8 -*-
import pandas as pd
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from scipy.stats import norm



def DataGenerate():
    data = pd.read_excel('C:/Users/Iris/Desktop/system_message_all.xlsx', 'Sheet1')
    X = pd.DataFrame(data, columns=['counts'],dtype=np.float)
    Y = pd.DataFrame(data, columns=['count(subsession_id)'],dtype=np.float)



    # plot raw data
    Y = np.array(Y)
    plt.title("Raw data(user_message)")
    plt.scatter(X, Y, color='black')
    plt.show()

    X = np.log10(X)  # 对X，Y取双对数
    Y = np.log10(Y)
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

def DataFitAndVisualization(X, Y):
    # 模型数据准备
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(X, Y):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    # 模型拟合
    regr = linear_model.LinearRegression()
    regr.fit(X_parameter, Y_parameter)
    # 模型结果与得分
    print('Coefficients: \n', regr.coef_, )
    print("Intercept:\n", regr.intercept_)
    # The mean square error
    print("Residual sum of squares: %.8f"
            % np.mean((regr.predict(X_parameter) - Y_parameter) ** 2))  # 残差平方和

    # 可视化
    plt.title("Log Data(user_message)")
    plt.scatter(X_parameter, Y_parameter, color='black')
    plt.plot(X_parameter, regr.predict(X_parameter), color='blue', linewidth=3)

    # plt.xticks(())
    # plt.yticks(())
    plt.show()

if __name__ == "__main__":
    X, Y = DataGenerate()
    DataFitAndVisualization(X, Y)
