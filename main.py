import pandas as pd
import matplotlib.pyplot as plt

imposto1 = (0, 2100000, 5)
imposto2 = (2100000, 2400000, 12)
imposto3 = (2400000, 17)


def getImpostoPerc(val):
    if imposto1[0] <= val < imposto1[1]:
        return float(imposto1[2])/100

    elif imposto2[0] <= val < imposto2[1]:
        return float(imposto2[2])/100

    elif val >= imposto3[0]:
        return float(imposto3[1])/100


def q1_q(vendas_df):
    x = vendas_df['Valor unitário']
    y = vendas_df['Qtd']

    total = 0

    merged = zip(list(x), list(y))
    for k in merged:
        total += k[0]*k[1]

    print('%.2f' % (total*getImpostoPerc(total)))


local_file = "C:\\Users\\mathe\\PycharmProjects\\cezar\\q1.xls"
vendas_df = pd.read_excel(local_file)

q1_q(vendas_df)



# plt.figure(figsize=(10,10))
# plt.style.use('seaborn')
# plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
# plt.title("Excel sheet to Scatter Plot")
# plt.show()

