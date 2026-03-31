import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("college_data.csv")

print("college data")
print(df)

subjects=["Dsa","Cloud Computing" , "Operating Systems" , "Dbms" , "Attendance"]
df["Total"]=df[subjects].sum(axis=1)

df["Average"]=df[subjects].mean(axis=1)
print("updated data")
print(df)

df["Performance Score"] = df["Average"]*0.7+df["Attendance"]*0.3

Topper = df.loc[df["Performance Score"].idxmax()]
print(" Topper:")
print(Topper["Name"])

subject_avg=df[subjects].mean()
hardest_subject=subject_avg.idxmin()

print("Hardest Subject:",hardest_subject)

def get_status(row):
    if row["Attendance"] < 70 and row["Average"] < 60:
        return "High Risk"
    elif row["Average"] < 60:
        return "Needs Improvement"
    else:
        return "Safe"
df["Status"] = df.apply(get_status,axis=1)

print("Student Data")
print(df[["Name","Status"]])


df["Consistency"]=df[subjects].std(axis=1)
print("Consistency")
print(df[["Name","Consistency"]])

plt.figure()
plt.bar(df["Name"],df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()

status_counts = df["Status"].value_counts()

plt.figure()
plt.pie(status_counts,labels=status_counts.index,autopct=("%1.1f%%"))
plt.title("Student Status Dashboard")
plt.show()


df.to_csv("analysis_outputs.csv",index=False)