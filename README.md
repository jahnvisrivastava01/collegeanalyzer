# 🎓 College Analyzer System

## 🚀 Overview

A Python-based analytics system designed to evaluate student performance using multiple academic parameters.

This project goes beyond basic marks analysis by incorporating attendance, subject difficulty, consistency, and risk detection to simulate real-world academic analytics systems.

---

##  Features

### 📊 Performance Analysis

* Total and average marks calculation
* Smart topper detection using weighted scoring
* Subject-wise analysis

### ⚠️ Risk Detection

* Identifies:

  * High Risk 
  * Needs Improvement 
  * Safe 
* Based on attendance + performance

### 🧠 Advanced Insights

* Subject difficulty detection
* Consistency analysis using standard deviation
* Performance scoring system

### 📈 Visualization

* Bar chart of student averages
* Pie chart of student status distribution

### 📁 Output

* Saves final analysis to CSV file.

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib

---

## 📂 Dataset Format

```csv
Name,DSA,Cloud Computing,Operating Systems,Dbms,Attendance
Priya,85,78,80,88,88
Sneha,60,65,70,75,75
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy matplotlib
```

2. Run the project:

```bash
python main.py
```

---

## 📊 Sample Insights

* Smart Topper: Sneha
* Hardest Subject: Cloud Computing
* Risk Students Identified

---

## 💡 Future Improvements

* Machine learning-based performance prediction
* Web dashboard (React integration)
* CSV upload support

---

##  Author

Jahnvi Srivastava
