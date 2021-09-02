import pandas as pd
df = pd.read_csv("datasets/Airplane_Crashes_and_Fatalities_Since_1908.csv")

cleaned = df.drop(["Flight #","Route","Registration","cn/In","Summary"],axis=1)
cleaned.Date = pd.to_datetime(cleaned.Date,format="%m/%d/%Y")

df_cleaned = cleaned[ cleaned.Location.notnull() & cleaned.Operator.notnull() &
                     cleaned.Type.notnull() & cleaned.Aboard.notnull()  & cleaned.Ground.notnull() ]

# (5268-5181)/5268 #Error 0.016

## total fatalities
df_cleaned["TotFat"] = df_cleaned.Fatalities+df_cleaned.Ground

## TotFat/Aboard
df_cleaned["FatRatio"] = df_cleaned.TotFat/df_cleaned.Aboard

