### Project Title
AI Impact on Jobs 2030

**Author**
Juliet Zheng

#### Executive summary
Analyze the impact of AI on the job market, including data acquisition, cleaning, exploratory data analysis, feature engineering, and the development of a baseline machine learning model, followed by an initial report and insights.

#### Rationale
Why should anyone care about this question?
AI’s impact on jobs by 2030 shapes:
Skills needed for future work
Job design and worker augmentation
Policy and business strategy
Essentially, preparing today ensures societies and workers benefit from AI rather than suffer from disruption.

#### Research Question
What are you trying to answer?
Skills needed for future work
Job design and worker augmentation
Policy and business strategy

#### Data Sources
What data will you use to answer you question?

https://www.kaggle.com/datasets/khushikyad001/ai-impact-on-jobs-2030?resource=download

#### Methodology
What methods are you using to answer the question?
data acquisition, cleaning, exploratory data analysis, feature engineering, and the development of a baseline machine learning model

#### Results
What did your research find?
Data Analysis Key Findings
Data Quality: The dataset was found to be exceptionally clean, with no missing values and no duplicate rows identified.
Data Type Conversion: posting_date and application_deadline columns were successfully converted to datetime objects, enabling time-series calculations.
Outlier Management: 483 outliers were detected in the salary_usd column using the IQR method and were subsequently capped, with the maximum capped salary being $260,751.625.
Salary Distribution: The distribution of salary_usd is right-skewed, indicating a concentration of jobs at lower to mid-range salaries.
Experience Level Distribution: years_experience is heavily skewed towards lower experience levels (0-5 years), suggesting a younger or less experienced workforce in the dataset.
Feature Correlations:
salary_usd shows a strong positive correlation with years_experience (0.69) and a moderate positive correlation with benefits_score (0.41).
remote_ratio and job_description_length have very weak correlations with other numerical features.
Feature Engineering: Two new features were successfully created:
days_to_deadline: The number of days between the job posting and the application deadline.
num_required_skills: The count of skills listed in the job's required_skills field.
Baseline Model Performance: A Linear Regression model, using numerical features and one-hot encoded experience_level, achieved a Mean Absolute Error (MAE) of $26,444.66 and an R-squared (R2) score of 0.64 in predicting salary_usd.

#### Next steps
What suggestions do you have for next steps?
To address the core task of analyzing AI's impact on jobs, further steps should involve extracting AI-related keywords or themes from job descriptions or titles and then analyzing their correlation with salary, experience, or job availability.

#### Outline of project

- https://github.com/JulietZZheng/zzdas_pb/blob/main/Required_Capstone_Assignment_20_1_Initial_Report_and_Exploratory_Data_Analysis_(EDA)/Required_Capstone_Assignment_20_1_Initial_Report_and_Exploratory_Data_Analysis_(EDA).ipynb


##### Contact and Further Information