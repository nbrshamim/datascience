import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the dataset
    df = pd.read_csv('your_dataset.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100

    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_higher_education = (df[higher_education]['salary'] == '>50K').sum() / len(df[higher_education]) * 100

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_lower_education = (df[lower_education]['salary'] == '>50K').sum() / len(df[lower_education]) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("1. People of each race:")
        print(race_count)
        print("\n2. Average age of men:", round(average_age_men, 1))
        print("\n3. Percentage with Bachelor's degree:", round(percentage_bachelors, 1))
        print("\n4. Percentage with advanced education (>50K):", round(percentage_higher_education, 1))
        print("\n5. Percentage without advanced education (>50K):", round(percentage_lower_education, 1))
        print("\n6. Minimum number of hours a person works per week:", min_work_hours)
        print("\n7. Percentage of minimum hours workers with salary >50K:", round(rich_percentage, 1))
        print("\n8. Country with the highest percentage earning >50K:", highest_earning_country)
        print("   Percentage:", round(highest_earning_country_percentage, 1))
        print("\n9. Most popular occupation for those who earn >50K in India:", top_IN_occupation)

    # Return results as a dictionary
    return {
        "race_count": race_count,
        "average_age_men": round(average_age_men, 1),
        "percentage_bachelors": round(percentage_bachelors, 1),
        "percentage_higher_education": round(percentage_higher_education, 1),
        "percentage_lower_education": round(percentage_lower_education, 1),
        "min_work_hours": min_work_hours,
        "rich_percentage": round(rich_percentage, 1),
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": round(highest_earning_country_percentage, 1),
        "top_IN_occupation": top_IN_occupation
    }