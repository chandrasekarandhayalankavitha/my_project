import pandas as pd

apps = ["Instagram", "YouTube", "Chrome", "Maps", "WhatsApp"]
bdrain = [18, 25, 10, 30, 7]

bseriesdrain = pd.Series(bdrain, index=apps)
print(bseriesdrain)
print(bseriesdrain["Instagram"])
print(bseriesdrain.values)
print(bseriesdrain.index)

bseriesdrain.index = bseriesdrain.index.str[:3].str.upper()
print(bseriesdrain.index)

print(bseriesdrain.iloc[0])
print(bseriesdrain.iloc[-1])

print(bseriesdrain.loc["YOU"])
print(bseriesdrain.loc["INS" : "CHR"])