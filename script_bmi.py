import pandas as pd

# Get the data from API
df = pd.read_csv("https://api.vitaldb.net/cases")
# Filter patients that had a Cholecystectomy
study_df = df[df["opname"].str.contains("cholecystectomy", case=False, na=False)].copy()
# Removing Patients with no registered BMI
study_df = study_df.dropna(subset=["bmi"])
# Forming the BMI Logic
study_df["BMI_Status"] = study_df["bmi"].apply(
    lambda bmi: "Obese" if bmi > 30 else "Normal"
)
# Building the Summary Table
table1 = (
    study_df.groupby("BMI_Status")
    .agg(
        Total_Patients=("caseid", "count"),
        Average_Age=("age", "mean"),
        Average_BMI=("bmi", "mean"),
    )
    .round(1)
)
print(table1)
