# %% import pandas and read the csv file
# modify the path if needed
import pandas as pd 

df = pd.read_csv("DATA475_lab_rectangles_data.csv")
df["areas"] = df["length"] * df["width"]
df

# %% some simple statistics on Col area
summary = [
    ("Total count", df["areas"].shape[0]),
    ("Total Area", df["areas"].sum()),
    ("Max Area", df["areas"].max()),
    ("Min Area", df["areas"].min()),
    ("Max Area", df["areas"].max()),
    ("Avg Area", df["areas"].mean()),
    ]

for key,value in summary:
    print(f"{key} : {value}")

# %%
pd.DataFrame(
    dict(summary),index= ["summary"]
    ).to_csv("summary_Pandas.csv", index=False)

# %%
