
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

survey_raw_df = pd.read_csv('.\Data_set\survey_results_public.csv')
#print(survey_df.info())

# schema_df = pd.read_csv('.\Data_set\survey_results_schema.csv')
# print(schema_df.info())
# print(schema_df)

selected_columns = [
            'ResponseId',
            #specialization
            'MainBranch',
            'Employment',
            'RemoteWork',
            'CodingActivities',
            'LanguageHaveWorkedWith',
            'LanguageWantToWorkWith',
            #learning method
            'EdLevel',
            'LearnCode',
            'LearnCodeOnline',
            'LearnCodeCoursesCert',
            #dev experience
            'YearsCode',
            'YearsCodePro',
            'DevType',
            'Country',
            'ProfessionalTech']

# print(len(selected_columns))
survey_df = survey_raw_df[selected_columns].copy()

survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')

# print(survey_df['YearsCode'].head(10))

# print(survey_df.describe())

#------------------------------

# print(survey_df.Employment.nunique())
top_emp_type = survey_df.Employment.value_counts().head(10)
# print(top_emp_type))
# print(len(top_emp_type))


def auto_pie(df):
    plt.figure(figsize=(12,6))
    plt.pie(df, labels=df.index, autopct='%1.1f%%')
    plt.show()
    plt.savefig(f'{df}.png')
    plt.close()


def countplot_for_ed_level():
    plt.figure(figsize=(12,6))
    sns.countplot(y=survey_df.EdLevel)
    plt.xticks(rotation=75);
    plt.title('EdLevel')
    plt.ylabel(None);
    plt.show()
    plt.savefig('ed_levels.png')
    plt.close()





# types_of_developers = survey_df.DevType.value_counts()
# print(types_of_developers)


#didn't manage to fix problem with ,drop() here
# types_of_developers["other"] = types_of_developers[types_of_developers < 10].sum()
# types_of_developers.drop(types_of_developers[types_of_developers < 10], axis=0)
# print(types_of_developers)

def split_multicolumn(col_series):
    result_df = col_series.to_frame()
    options = []
    # Iterate over the column
    for idx, value  in col_series[col_series.notnull()].items():
        # Break each value into list of options
        for option in value.split(';'):
            # Add the option as a column to result
            if not option in result_df.columns:
                options.append(option)
                result_df[option] = False
            # Mark the value in the option column as True
            result_df.at[idx, option] = True
    return result_df[options]


#print(survey_df.LanguageHaveWorkedWith)

languages_worked_df = split_multicolumn(survey_df.LanguageHaveWorkedWith)
# print(languages_worked_df)

languages_want_to_work_df = split_multicolumn(survey_df.LanguageWantToWorkWith)
# print(languages_worked_df)

def language_persenteges():


    language_percenteges = languages_worked_df.mean().sort_values() * 100
    # auto_pie(language_percenteges.head(20))



    language_percenteges2 = languages_want_to_work_df.mean().sort_values() * 100
    # auto_pie(language_percenteges2.head(20))

    plt.figure(figsize=(12, 12))
    sns.barplot(x=language_percenteges, y=language_percenteges2.index)
    plt.title("Languages used in the past year")
    plt.xlabel('count')
    plt.show()
    plt.savefig('language_percenteges.png')
    plt.close()

# language_persenteges()

def loved_languages():
    languages_loved_df = languages_worked_df & languages_want_to_work_df

    languages_loved_percentages = (languages_loved_df.sum() * 100/ languages_worked_df.sum()).sort_values()

    plt.figure(figsize=(12, 12))
    sns.barplot(x=languages_loved_percentages, y=languages_loved_percentages.index)
    plt.title("Most loved languages")
    plt.xlabel('count')
    plt.show()
    plt.savefig('loved_languages.png')
    plt.close()


#-----------------------


countplot_for_ed_level()
language_persenteges()
loved_languages()
survey_df.to_csv('results.csv')












