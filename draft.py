import numpy as np
import pandas as pd

survey_raw_df = pd.read_csv('.\Data_set\survey_results_public.csv')
#print(survey_df.info())

survey_df = survey_raw_df[0:25_000]
print(survey_df.info())

schema_df = pd.read_csv('.\Data_set\survey_results_schema.csv')
# print(schema_df.info())

#looking at the aquired columns
# servey_columns = survey_df.columns
# print(survey_df.columns)
#
# columns = (['ResponseId',
#             'MainBranch',
#             'Employment',
#             'RemoteWork',
#             'CodingActivities', #how the person feels coding
#             'EdLevel',
#             'LearnCode', #the way of learning code
#             'LearnCodeOnline', #sources for learning code
#             'LearnCodeCoursesCert', #coding cources
#             'YearsCode',
#             'YearsCodePro',
#             'DevType', #profession
#             'OrgSize',
#             'PurchaseInfluence',
#             'BuyNewTool',
#             'Country',
#             'Currency',
#             'CompTotal',
#             'CompFreq',
#             'LanguageHaveWorkedWith',
#             'LanguageWantToWorkWith',
#             'DatabaseHaveWorkedWith',
#             'DatabaseWantToWorkWith',
#             'PlatformHaveWorkedWith',
#             'PlatformWantToWorkWith',
#             'WebframeHaveWorkedWith',
#             'WebframeWantToWorkWith',
#             'MiscTechHaveWorkedWith',
#             'MiscTechWantToWorkWith',
#             'ToolsTechHaveWorkedWith',
#             'ToolsTechWantToWorkWith',
#             'NEWCollabToolsHaveWorkedWith',
#             'NEWCollabToolsWantToWorkWith',
#             'OpSysProfessional use',
#             'OpSysPersonal use',
#             'VersionControlSystem',
#             'VCInteraction',
#             'VCHostingPersonal use',
#             'VCHostingProfessional use',
#             'OfficeStackAsyncHaveWorkedWith',
#             'OfficeStackAsyncWantToWorkWith',
#             'OfficeStackSyncHaveWorkedWith',
#             'OfficeStackSyncWantToWorkWith',
#             'Blockchain',
#             'NEWSOSites',
#             'SOVisitFreq',
#             'SOAccount',
#             'SOPartFreq',
#             'SOComm',
#             'Age',
#             'Gender',
#             'Trans',
#             'Sexuality',
#             'Ethnicity',
#             'Accessibility',
#             'MentalHealth',
#             'TBranch',
#             'ICorPM',
#             'WorkExp',
#             'Knowledge_1',
#             'Knowledge_2',
#             'Knowledge_3',
#             'Knowledge_4',
#             'Knowledge_5',
#             'Knowledge_6',
#             'Knowledge_7',
#             'Frequency_1',
#             'Frequency_2',
#             'Frequency_3',
#             'TimeSearching',
#             'TimeAnswering',
#             'Onboarding',
#             'ProfessionalTech',
#             'TrueFalse_1',
#             'TrueFalse_2',
#             'TrueFalse_3',
#             'SurveyLength',
#             'SurveyEase',
#             'ConvertedCompYearly'],
#             dtype='object')
#
# survey_sample = survey_df[0:1000]
# print(survey_sample['DevType'].sample(10).to_csv('.\Data_set\sampling.csv'))

#
# print(survey_df.info())
#
# survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
# survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')
# survey_df['TimeSearching'] = pd.to_numeric(survey_df.TimeSearching, errors='coerce')
# survey_df['TimeAnswering'] = pd.to_numeric(survey_df.TimeAnswering, errors='coerce')
#
# print(survey_df.describe())


#-----------------------

#-----looking at the aquired columns, result is in the draft
# servey_columns = survey_df.columns
# print(survey_df.columns)
# survey_sample = survey_df[0:1000]
# print(survey_sample['DevType'].sample(10).to_csv('.\Data_set\sampling.csv'))

# #-----clearing data
# survey_df = survey_df[['ResponseId',
#             'MainBranch',
#             'Employment',
#             'RemoteWork',
#             'CodingActivities',
#             'LearnCode',
#             'LearnCodeOnline',
#             'LearnCodeCoursesCert',
#             'YearsCode',
#             'YearsCodePro',
#             'DevType',
#             'Country',
#             'Knowledge_1',
#             'Knowledge_2',
#             'Knowledge_3',
#             'TimeSearching',
#             'TimeAnswering',
#             'ProfessionalTech']]
#
# print(survey_df.info())
#
# survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
# survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')
# survey_df['TimeSearching'] = pd.to_numeric(survey_df.TimeSearching, errors='coerce')
# survey_df['TimeAnswering'] = pd.to_numeric(survey_df.TimeAnswering, errors='coerce')
#
# print(survey_df.describe())
# print(survey_df['TimeAnswering'].sum())
# #'TimeAnswering' does not have any data in my set
# survey_df.drop(['TimeSearching', 'TimeAnswering'])
#
# print(survey_df.info(), axis=1)
#-----------------------------------


# print(len(selected_columns))
survey_df = survey_raw_df[selected_columns].copy()

survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')

# print(survey_df['YearsCode'].head(10))

print(survey_df.describe())
# print(survey_df[survey_df.YearsCode > 40].count())

#------------------------------

#------------------------------

# print(survey_df.Employment.nunique())
top_emp_type = survey_df.Employment.value_counts().head(10)
# print(top_emp_type))
# print(len(top_emp_type))

def pie_for_top_emp_type():
    plt.figure(figsize=(12,6))
    plt.pie(top_emp_type, labels=top_emp_type.index, autopct='%1.1f%%')
    plt.show()
    plt.close()

def countplot_for_ed_level():
    plt.figure(figsize=(12,6))
    sns.countplot(y=survey_df.EdLevel)
    plt.xticks(rotation=75);
    plt.title('EdLevel')
    plt.ylabel(None);
    plt.show()

types_of_developers = survey_df.DevType.value_counts()
print(types_of_developers)


#didn't manage to fix problem with ,drop() here
# types_of_developers["other"] = types_of_developers[types_of_developers < 10].sum()
# types_of_developers.drop(types_of_developers[types_of_developers < 10], axis=0)
# print(types_of_developers)







