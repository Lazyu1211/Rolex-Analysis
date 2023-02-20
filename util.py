import pandas as pd

PATH = "/Users/junyuwu/Rolex(Second project)/component/rolex_scaper_clean.csv"
df = pd.read_csv(PATH)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

def get_data():
    return df

def get_model_count():
    model_count = df["model"].value_counts().nlargest(8).to_frame()
    model_count.reset_index(inplace=True)
    #print(model_count)
    return model_count

def get_model_byprice():
    model_byprice = df.groupby("model")["price"].sum().nlargest(10).to_frame()
    model_byprice.reset_index(inplace=True)
    #print(model_byprice)
    return model_byprice

def get_bymovement():
    bymovement = df.groupby("movement")["price"].mean().to_frame()
    bymovement.reset_index(inplace=True)
    return bymovement

def get_bymatrial():
    by_material = df.groupby("case material")["price"].mean().to_frame()
    by_material.reset_index(inplace=True)
    return by_material

def get_bydiameter():
    by_diameter = df.groupby("case diameter")["price"].mean().nlargest(10).to_frame()
    by_diameter.reset_index(inplace=True)
    return by_diameter

def get_bycondition():
    bycondition = df.groupby("condition")["price"].mean().to_frame()
    bycondition.reset_index(inplace=True)
    return bycondition

def get_countries():
    df["exploded_location"] = df["location"].str.split(",")
    df["country"] = [i[0] for i in df["exploded_location"]]
    country_sale_df = df["country"].value_counts()[:10].to_frame()
    total_sale_df = df.groupby("country")["price"].sum().sort_values(ascending=False)[:10].to_frame()
    df_concat = pd.concat([country_sale_df, total_sale_df], axis=1)
    df_concat = df_concat.rename(columns={'country': 'Stores Amount', 'price': 'Total Price'})
    df_concat.reset_index(inplace=True)
    df_concat = df_concat.rename(columns = {'index':'Country'})
    return df_concat

def get_countries_name():
    df["exploded_location"] = df["location"].str.split(",")
    df["country"] = [i[0] for i in df["exploded_location"]]
    country_sale_df = df["country"].value_counts()[:10].to_frame()
    total_sale_df = df.groupby("country")["price"].sum().sort_values(ascending=False)[:10].to_frame()
    df_concat = pd.concat([country_sale_df, total_sale_df], axis=1)
    df_concat = df_concat.rename(columns={'country': 'Stores Amount', 'price': 'Total Price'})
    df_concat.reset_index(inplace=True)
    df_concat = df_concat.rename(columns = {'index':'Country'})
    countries= list(set(df_concat["Country"].tolist()))
    return countries