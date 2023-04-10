import pandas as pd

df = pd.read_excel("AutomationTest.xlsx")

col1 = []
col2 = []

koml = df.columns[14:42]
index = 0

for x in df["SİGORTALI"]:
    col1.append(x)
    col2.append(" ")
    for y in koml:
        col1.append(y)
        col2.append(df.loc[0+index, y])
    index = index + 1
    d = {'SİGORTA ŞİRKETLERİ': col1, 'DÖNÜŞLER': col2}
    df2 = pd.DataFrame(data=d)
    print(df2)
    col1.clear()
    col2.clear()
    df2.to_excel(f"/Users/egebakalim/desktop/excels/{x}.xlsx")