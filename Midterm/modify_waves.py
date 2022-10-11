import pandas as pd
import numpy as np

df1 = pd.read_csv("wavlength_values.csv")
df2 = pd.read_csv("metadata.csv")

id_vals = df2.ID

new_data_dict = {}
waves = df1["Wavelength"]

for id in id_vals:
    new_data_dict[id] = waves + np.random.normal(loc=0.0,scale=0.005,size =waves.shape)

new_df = pd.DataFrame(new_data_dict)
new_df.to_csv('new_waves.csv', index=False)







