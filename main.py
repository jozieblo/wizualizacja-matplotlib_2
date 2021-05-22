import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# x1 = np.arange(0.0,2.0,0.02)
# x2 = np.arange(0.0,2.0,0.02)
# s1 = np.sin(2*np.pi* x1)
# s2 = np.cos(2*np.pi* x2)
#
# plt.subplot(3,2,1)
# plt.plot(x1,s1,'-')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Dwa podwykresy')
# plt.subplot(2,1,2)
# plt.plot(x2, s2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()

# print("zad1")
# def f(x):
#     return 1/x
# x=np.linspace(20,40)
# y=f(x)
# plt.plot(x, y,'g-', label="y=1/x")
# plt.xlabel('x')
# plt.ylabel('1/x')
# plt.title("Wykres funkcji f(x)=1/x")
# plt.legend()
# plt.show()

# print("zad2")
# def f(x):
#     return 1/x
# x=np.linspace(20,40)
# y=f(x)
# plt.plot(x, y,'bo--', label="y=1/x")
# plt.xlabel('x')
# plt.ylabel('1/x')
# plt.title("Wykres funkcji f(x)=1/x")
# plt.legend()
# plt.show()

# print("zad3")
# x1=np.arange(0,45,0.1)
# x2=np.arange(0,45,0.1)
#
# y1=np.sin(2* np.pi*x1)
# y2=np.cos(2* np.pi*x2)
#
# plt.plot(x2,y2,'-', label="sin(x)")
# plt.plot(x1,y1,'-', label="cos(x)")
# plt.title("Wykres sin(x) i cos(x)")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# print("zad4")
# x1=np.arange(0,45,0.1)
# x2=np.arange(0,45,0.1)
#
# y1=np.sin(2* np.pi*x1)
# y2=np.cos(2* np.pi*x2)
#
# plt.plot(x2,y2,'-', label="sin(x)")
# plt.plot(x1,y1,'-', label="cos(x)")
# plt.title("Wykres sin(x) i cos(x)")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis([0,5,-1,5])
# plt.legend()
# plt.show()

# print("zad5")


# print("zad6")
# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# df2 = df[(df.Plec == 'M')]['Liczba'].sum()
# df3 = df[(df.Plec == 'K')]['Liczba'].sum()
# et=["Kobiety","Mezczyzni"]
# wrt=[df2,df3]
# plt.bar(et, wrt,  color='purple')
# plt.ylabel('Ilosc narodzin w mln')
# plt.title("Zbiór wszystkich urodzonych")
# plt.show()

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# df2 = df[(df.Plec == 'M')]['Liczba'].sum()
# df3 = df[(df.Plec == 'K')]['Liczba'].sum()
# x=np.linspace(0,2,2)
# plt.plot('Kobiety', df3, color='purple')
# plt.plot('Mezczyzni', df2, color='purple')
# plt.ylabel('Ilosc narodzin w mln')
# plt.xlabel('Płec')
# plt.title("Zbiór wszystkich urodzonych")
# plt.show()

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# df1 = df.groupby(['Rok'])['Liczba'].sum()
# plt.bar('Rok',df1, color='purple')
# plt.ylabel('Ilosc narodzin w mln')
# plt.title("Zbiór  urodzonych dla każdego roku")
# plt.show()
