import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv("adult.data.csv")

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1)

    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round(
        (df[advanced_edu]['salary'] == '>50K').mean() * 100, 1)

    lower_edu_rich = round(
        (df[~advanced_edu]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers_pct = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1)

  
    country_rich_pct = df[df['salary'] == '>50K']['native-country'].value_counts() / \
                       df['native-country'].value_counts() * 100
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)


    top_IN_occupation = df[(df['native-country'] == 'India') &
                           (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_min_workers_pct,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
