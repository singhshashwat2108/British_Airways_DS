import pandas as pd

df=pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1 (1).xlsx")

lookup = pd.DataFrame({
    "HAUL": [
        "SHORT", "SHORT", "SHORT", "SHORT",
        "LONG", "LONG", "LONG", "LONG"
    ],
    "TIME_OF_DAY": [
        "Morning", "Afternoon", "Lunchtime", "Evening",
        "Morning", "Afternoon", "Lunchtime", "Evening"
    ],
    "TIER1_%": [0.03, 0.025, 0.02, 0.015,
                0.12, 0.10, 0.09, 0.08],
    "TIER2_%": [0.15, 0.13, 0.12, 0.10,
                0.35, 0.30, 0.28, 0.25],
    "TIER3_%": [0.50, 0.45, 0.42, 0.40,
                0.75, 0.70, 0.68, 0.65]
})


df = df.merge(
    lookup,
    on=["HAUL", "TIME_OF_DAY"],
    how="left"
)

print(df.head(10))
lookup.to_excel("Lounge_Eligibility_Lookup_Table.xlsx", index=False)




