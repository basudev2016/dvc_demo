import pandas as pd

df = pd.read_csv('data.csv')
df["eng_feat_1"] = df["feature_0"] + df["feature_1"] + df["feature_2"] + \
df["feature_3"] + df["feature_4"] + df["feature_5"]

df["eng_feat_2"] = df["feature_6"] * df["feature_7"] * df["feature_8"] * \
df["feature_9"] + df["feature_10"] 

eng_df = pd.concat([df["target"], df["eng_feat_1"], df["eng_feat_2"]], axis=1)
print(eng_df)

eng_df.to_csv('data_with_features.csv', index=False)