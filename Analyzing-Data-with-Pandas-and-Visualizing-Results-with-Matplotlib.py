import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Task 1: Load and Explore the Dataset
print("Task 1: Loading and Exploring the Dataset")
print("-" * 50)

# Kenyan school dataset
np.random.seed(42)  # For reproducible results

first_names = ["Kevin", "Tom", "Brian", "Peter", "Nixon", "John", "Mwangi", 
              "Jane", "Adrian", "Antony", "Janet", "Atieno", "Kimani", "Megan", 
              "David", "Robert", "Stanly", "Truphena", "ALeshan", "Ali"]
last_names = ["Ngugi", "Omondi", "Wekesa", "Kamau", "Korir", "Onyango", "Maina", 
             "Wanjiku", "Kibet", "Mbugua", "Akoth", "Rose", "Mbugua", "Muthoni", 
             "Kiptoo", "Nyong'o", "Githuka", "Awino", "Lemaiyan", "Juma"]

# Create student names
students = []
for _ in range(50):  # 50 students
    first = random.choice(first_names)
    last = random.choice(last_names)
    students.append(f"{first} {last}")

subjects = ["Mathematics", "English", "Kiswahili", "Science", "Social Studies"]

# Generate random scores for each student in each subject
data = []
for student in students:
    student_data = {"Student_Name": student, "Form": random.choice([1, 2, 3, 4])}
    for subject in subjects:
        # Generate scores between 35 and 95
        student_data[subject] = np.random.randint(35, 96)
    
    # Calculate mean score for each student
    student_data["Average_Score"] = np.mean([student_data[subject] for subject in subjects])
    data.append(student_data)

# Create DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())
print()

# Check the structure of the dataset
print("Dataset info:")
print(df.info())
print()

# Check for missing values
print("Missing values:")
print(df.isnull().sum())
print()

# Set 5 random values in Mathematics column to NaN
random_indices = np.random.randint(0, len(df), 5)
df.loc[random_indices, "Mathematics"] = np.nan

print("After introducing missing values:")
print(df.isnull().sum())
print()

# Clean the dataset by filling missing values with the mean
print("Cleaning the dataset...")
df["Mathematics"] = df["Mathematics"].fillna(df["Mathematics"].mean())

print("Checking if missing values are resolved:")
print(df.isnull().sum())
print()

# Task 2: Basic Data Analysis
print("\nTask 2: Basic Data Analysis")
print("-" * 50)

# Compute basic statistics
print("Basic statistics:")
print(df[subjects + ["Average_Score"]].describe())
print()

# Group by Form and compute mean for each column
print("Mean scores by Form:")
form_means = df.groupby("Form")[subjects + ["Average_Score"]].mean()
print(form_means)
print()

print("Interesting findings:")
print("- The highest average scores are in Form", form_means["Average_Score"].idxmax())
print("- The subject with highest overall average is", 
      df[subjects].mean().idxmax(), "with a mean score of", round(df[subjects].mean().max(), 2))
print("- The subject with lowest overall average is", 
      df[subjects].mean().idxmin(), "with a mean score of", round(df[subjects].mean().min(), 2))
print()

# Task 3: Data Visualization
print("\nTask 3: Data Visualization")
print("-" * 50)

# Create a figure with 2x2 subplots for the four charts
plt.figure(figsize=(14, 10))

# 1. Line chart - Average scores for each subject by Form
plt.subplot(2, 2, 1)
form_means[subjects].T.plot(kind='line', marker='o', ax=plt.gca())
plt.title('Average Subject Scores by Form')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.xticks(rotation=15)
plt.grid(True)

# 2. Bar chart - Average scores by Form
plt.subplot(2, 2, 2)
form_means["Average_Score"].plot(kind='bar', color='skyblue')
plt.title('Average Student Score by Form')
plt.xlabel('Form')
plt.ylabel('Average Score')
plt.grid(axis='y')

# 3. Histogram - Distribution of Mathematics scores
plt.subplot(2, 2, 3)
plt.hist(df['Mathematics'], bins=10, color='green', edgecolor='black', alpha=0.7)
plt.title('Distribution of Mathematics Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.grid(axis='y')

# 4. Scatter plot - Mathematics vs English scores
plt.subplot(2, 2, 4)
# Create a scatter plot with different colors for each Form
for form in sorted(df['Form'].unique()):
    subset = df[df['Form'] == form]
    plt.scatter(
        subset['Mathematics'], 
        subset['English'],
        label=f'Form {form}',
        alpha=0.7
    )
plt.title('Mathematics vs English Scores')
plt.xlabel('Mathematics Score')
plt.ylabel('English Score')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('kenyan_school_data_visualization.png')
plt.show()

print("Analysis complete! Visualizations have been displayed and saved.")