## Environmental Degradation and Well-being Analysis: Quantifying Human Impact

**Capstone Data Analysis Project**

### Executive Summary

**Project overview and goals:** This project aims to quantify the impact of various human activities and lifestyle choices on environmental degradation and well-being. The primary goal is to identify the most significant contributing factors to environmental harm and determine which specific activities have the greatest measurable impact on key environmental indicators. Through comprehensive data analysis, we will establish clear, quantifiable relationships between human behaviors (such as energy consumption, transportation methods, dietary habits, and consumption patterns) and environmental outcomes (including carbon emissions, pollution levels, waste generation, and resource depletion). The analysis will also identify positive factors that contribute to environmental well-being, such as renewable energy adoption, sustainable practices, and conservation efforts. By analyzing trends over time and across different regions, this project will provide actionable insights that can inform individual behavior changes, organizational policies, and governmental regulations toward more sustainable practices.

**Expected Findings:** The analysis is expected to reveal:
- A ranked hierarchy of human activities by their environmental impact, with energy consumption and transportation methods likely emerging as top contributors to carbon emissions
- Quantifiable relationships between lifestyle choices and specific environmental indicators (e.g., X% increase in renewable energy adoption correlates with Y% reduction in carbon emissions)
- Geographic and temporal patterns showing how environmental indicators vary across regions and over time
- Identification of "high-leverage" interventions where small behavioral changes can produce significant environmental benefits
- Evidence-based insights into the effectiveness of existing environmental policies and practices

**Results and Conclusion:** Upon completion, this analysis will produce:
- Clear quantification of the environmental impact of major human activities (measured in carbon footprint, resource consumption, waste generation, etc.)
- Data-driven recommendations for the most effective sustainable lifestyle changes
- Visual representations of trends and patterns in environmental indicators
- Identification of success stories and best practices from regions showing improvement
- A framework for ongoing monitoring and assessment of environmental impact

**Future Research and Development:** This project lays the groundwork for several extensions including: predictive modeling of future environmental scenarios based on current trends, cost-benefit analysis of different sustainability interventions, integration of real-time IoT sensor data for more granular analysis, machine learning models to personalize sustainability recommendations, and development of an interactive dashboard for public environmental awareness.

**Next Steps and Recommendations:** Following the analysis, key recommendations will be provided for policymakers, organizations, and individuals on the most impactful areas for intervention. This includes prioritization of renewable energy transition, optimization of transportation systems, promotion of sustainable dietary choices, and implementation of circular economy principles in product consumption.


### Rationale

Environmental degradation is one of the most pressing challenges facing humanity today. Climate change, pollution, resource depletion, and biodiversity loss are accelerating at unprecedented rates. According to the Intergovernmental Panel on Climate Change (IPCC), human activities have caused approximately 1.0°C of global warming above pre-industrial levels, with significant impacts already visible in the form of more frequent extreme weather events, rising sea levels, and ecosystem disruptions.

While the scientific consensus on climate change is clear, there remains a critical need to translate this understanding into actionable insights about individual and collective behavior. Many people are unaware of which of their daily activities have the greatest environmental impact, leading to misdirected efforts in sustainability. For example, some may focus extensively on recycling while overlooking far more impactful changes like reducing energy consumption or modifying transportation habits.

This project addresses this knowledge gap by providing quantitative, data-driven analysis of the relationships between human activities and environmental outcomes. By identifying the most significant contributing factors to environmental degradation, we can:
- Empower individuals with clear information about the environmental consequences of their lifestyle choices
- Help organizations prioritize sustainability initiatives based on potential impact
- Inform policymakers about which regulations and incentives will be most effective
- Track progress toward environmental goals and identify successful interventions
- Combat misinformation and greenwashing with objective, data-backed conclusions

Understanding the quantitative relationship between human choices and environmental outcomes is crucial for creating an effective and coordinated response to environmental challenges. This project provides the analytical foundation for evidence-based decision-making at all levels of society.


### Research Question

**Primary Research Question:**
How do various human activities and lifestyle choices quantitatively impact environmental degradation and well-being, and what are the most significant contributing factors?

**Sub-questions:**
1. Which human activities contribute most significantly to environmental degradation (measured by carbon emissions, pollution, waste generation, and resource depletion)?
2. What is the quantifiable impact of specific lifestyle choices (energy consumption, transportation methods, dietary habits, consumption of goods) on key environmental indicators?
3. Which factors contribute positively to environmental well-being, and how effective are they?
4. What trends and patterns emerge in environmental indicators over time and across different geographic regions?
5. How do specific events (e.g., policy implementations, technological innovations) or regional characteristics correlate with changes in environmental indicators?
6. Which interventions show the highest return on investment in terms of environmental benefit per unit of behavioral change?


### Data Sources

This analysis will draw from multiple authoritative data sources to ensure comprehensive coverage and reliability:

**Government Environmental Agencies:**
- **Environmental Protection Agency (EPA)**: Air quality indices, water quality measurements, pollution levels, waste generation statistics, and resource consumption data for the United States
- **European Environment Agency (EEA)**: Comprehensive environmental data across European nations, including emissions, resource efficiency, and biodiversity indicators
- **National environmental ministries**: Country-specific environmental monitoring data

**International Organizations:**
- **World Bank**: Open Data platform with indicators on CO2 emissions, energy use, renewable energy consumption, forest area, and environmental health metrics across countries and time periods
- **United Nations Environment Programme (UNEP)**: Global environmental monitoring data, including climate change indicators, pollution levels, and biodiversity assessments
- **International Energy Agency (IEA)**: Energy consumption data by source, country, and sector
- **Food and Agriculture Organization (FAO)**: Data on agricultural practices, land use, deforestation, and food production emissions
- **Our World in Data**: Comprehensive, research-backed datasets on environmental metrics with historical trends

**Research Institutions:**
- **Global Footprint Network**: Ecological footprint and biocapacity data by country
- **Carbon Footprint Ltd.**: Life cycle assessment data for various products and activities
- **Academic research databases**: Published studies with datasets on environmental impact of specific industries, behaviors, and interventions

**Publicly Available Datasets:**
- **Kaggle**: Environmental datasets including climate change data, carbon emissions, air quality measurements, and sustainability indicators
- **Data.gov**: U.S. government's open data portal with extensive environmental datasets
- **Google Dataset Search**: Curated environmental datasets from various sources
- **Climate Watch**: Historical emissions data and climate commitments by country

**Data Integration Strategy:**
Multiple datasets will be combined to create a comprehensive view. For example, correlating energy consumption data (IEA) with carbon emissions data (World Bank) and renewable energy adoption rates (UNEP) will allow for multi-dimensional analysis. Geographic data will enable spatial analysis, while temporal data spanning multiple years will reveal trends and the impact of interventions.

**Expected Data Characteristics:**
- **Temporal coverage**: Minimum 10-20 years of historical data to identify meaningful trends
- **Geographic coverage**: Global data with country-level granularity, and regional/city-level data where available
- **Variables**: Carbon emissions, energy consumption by source, transportation statistics, waste generation, water quality, air quality, renewable energy adoption, land use changes, population demographics, economic indicators, and policy implementation dates


### Methodology

This analysis will employ a combination of statistical techniques, machine learning approaches, and data visualization methods to comprehensively examine the relationships between human activities and environmental outcomes.

#### Data Collection and Preparation

1. **Data Acquisition**: Systematically collect datasets from identified sources, ensuring documentation of provenance, collection methods, and any known limitations
2. **Data Cleaning**:
   - Handle missing values using appropriate imputation techniques or exclusion criteria
   - Identify and address outliers through statistical methods (IQR, Z-scores) and domain knowledge
   - Standardize units of measurement across different data sources
   - Resolve inconsistencies in geographic naming conventions and temporal granularity
3. **Data Integration**: Merge datasets using common keys (geographic identifiers, time periods) while preserving data integrity
4. **Feature Engineering**: Create derived variables such as per capita metrics, growth rates, efficiency ratios, and composite indices

#### Exploratory Data Analysis (EDA)

1. **Descriptive Statistics**:
   - Calculate central tendencies (mean, median, mode) and dispersion measures (standard deviation, variance, range) for all key environmental indicators
   - Summarize distributions of human activities and lifestyle metrics
   - Identify data quality issues and inform preprocessing decisions

2. **Data Visualization**:
   - Time series plots to visualize trends in environmental indicators over time
   - Geographic maps (choropleth maps) to show spatial distributions and regional variations
   - Histograms and density plots to understand variable distributions
   - Box plots to compare distributions across different groups or regions
   - Scatter plots to identify potential relationships between variables

#### Correlation Analysis

1. **Pearson Correlation**: Measure linear relationships between continuous variables (e.g., energy consumption and carbon emissions)
2. **Spearman Rank Correlation**: Assess monotonic relationships for non-normally distributed data
3. **Correlation Matrices and Heatmaps**: Visualize relationships among multiple variables simultaneously
4. **Partial Correlation**: Control for confounding variables to isolate direct relationships

**Purpose**: Identify which human activities and lifestyle choices show the strongest associations with environmental outcomes, informing subsequent modeling efforts.

#### Regression Analysis

1. **Multiple Linear Regression**:
   - Model environmental indicators (dependent variables) as functions of human activities (independent variables)
   - Quantify the magnitude of impact: for each unit increase in an activity, how much does the environmental indicator change?
   - Include control variables (e.g., GDP, population density, climate) to isolate causal effects

2. **Polynomial Regression**: Capture non-linear relationships where impact may accelerate or decelerate

3. **Regularized Regression (Ridge, Lasso)**:
   - Handle multicollinearity among predictors
   - Perform feature selection by identifying the most important contributing factors
   - Lasso regression can reduce coefficients of less important variables to zero

4. **Model Evaluation**:
   - R-squared and adjusted R-squared to assess model fit
   - Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) for prediction accuracy
   - Residual analysis to check model assumptions (normality, homoscedasticity, independence)
   - Cross-validation to ensure model generalizability

**Purpose**: Quantify the impact of specific factors on environmental indicators and identify the most significant contributors.

#### Time Series Analysis

1. **Trend Analysis**: Decompose time series into trend, seasonal, and residual components using methods like STL (Seasonal and Trend decomposition using Loess)
2. **Change Point Detection**: Identify specific time points where environmental indicators show significant shifts (potentially corresponding to policy changes or major events)
3. **Autoregressive Integrated Moving Average (ARIMA)**: Model temporal dependencies and forecast future trends
4. **Intervention Analysis**: Assess the impact of specific events (e.g., implementation of carbon tax, renewable energy subsidies) on environmental indicators using interrupted time series analysis

**Purpose**: Understand how environmental indicators have evolved over time, identify the effectiveness of past interventions, and project future scenarios.

#### Spatial Analysis

1. **Geographic Clustering**: Group regions with similar environmental profiles or human activity patterns using K-means or hierarchical clustering
2. **Spatial Autocorrelation**: Test whether nearby regions have similar environmental indicators using Moran's I statistic
3. **Geographically Weighted Regression**: Allow regression coefficients to vary spatially, acknowledging that relationships may differ across regions
4. **Hotspot Analysis**: Identify areas with statistically significant clusters of high or low environmental impact

**Purpose**: Reveal geographic patterns, identify regions of concern or success, and understand how location-specific factors influence environmental outcomes.

#### Clustering and Segmentation

1. **K-Means Clustering**: Group countries, regions, or time periods based on their environmental and activity profiles
2. **Hierarchical Clustering**: Create dendrograms to visualize relationships and similarity structures
3. **Principal Component Analysis (PCA)**: Reduce dimensionality while retaining variance, facilitating visualization and interpretation of high-dimensional data
4. **Cluster Profiling**: Characterize each cluster by its typical activities, environmental indicators, and outcomes

**Purpose**: Identify distinct patterns of behavior and environmental impact, enabling targeted recommendations for different segments.

#### Advanced Modeling (Optional)

1. **Random Forest Regression**:
   - Capture complex non-linear relationships and interactions between variables
   - Assess feature importance to rank contributing factors
   - Robust to outliers and multicollinearity

2. **Gradient Boosting (XGBoost)**: High-performance modeling for prediction and feature importance ranking

3. **Causal Inference Techniques**: Where appropriate, use methods like propensity score matching or instrumental variables to strengthen causal claims

**Purpose**: Enhance prediction accuracy and deepen understanding of complex, non-linear relationships.

#### Data Visualization and Communication

1. **Interactive Dashboards**: Use tools like Plotly, Tableau, or Power BI to create interactive visualizations allowing stakeholders to explore data
2. **Infographics**: Distill key findings into accessible visual summaries for broader audiences
3. **Storyboarding**: Present findings as a narrative that guides stakeholders from data to insights to recommendations

**Purpose**: Ensure findings are accessible, understandable, and actionable for diverse audiences including policymakers, organizations, and the general public.

#### Software and Tools

- **Programming Languages**: Python (primary), R (for specific statistical methods)
- **Libraries**:
  - Data manipulation: pandas, numpy
  - Statistical analysis: scipy, statsmodels
  - Machine learning: scikit-learn, xgboost
  - Time series: statsmodels, prophet
  - Spatial analysis: geopandas, folium, pysal
  - Visualization: matplotlib, seaborn, plotly, folium
- **Environment**: Jupyter Notebooks for reproducible analysis and documentation


### Expected Results

Upon completion of this comprehensive analysis, the following results are anticipated:

#### 1. Identification of Significant Contributing Factors

**Most Impactful Human Activities:**
- **Energy Consumption**: Expected to be the single largest contributor to carbon emissions, with quantified impacts of fossil fuel use versus renewable energy sources
- **Transportation Methods**: Ranking of transportation modes (air travel, personal vehicles, public transit, cycling/walking) by environmental impact per unit distance
- **Dietary Habits**: Quantification of the carbon footprint and resource consumption of different diets (omnivorous, vegetarian, vegan, locally-sourced, etc.)
- **Consumption of Goods**: Impact of consumer behavior including fast fashion, electronics consumption, single-use plastics, and product lifecycle considerations
- **Residential/Commercial Activities**: Heating/cooling, water usage, waste generation patterns

**Feature Importance Rankings**: A data-driven ranking of activities showing which behaviors offer the greatest potential for environmental impact reduction.

#### 2. Quantification of Impacts

**Specific Relationships and Effect Sizes:**
- "A 10% increase in renewable energy adoption is associated with an X% reduction in carbon emissions per capita"
- "Switching from a gasoline vehicle to electric reduces individual carbon footprint by approximately Y kg CO2 per year"
- "A plant-based diet compared to a meat-heavy diet reduces carbon emissions by approximately Z%"
- "Recycling reduces waste-to-landfill by W% but has less overall environmental impact than reducing consumption"

**Regression Model Outputs**: Coefficients indicating the magnitude and direction of impact for each factor, with confidence intervals and statistical significance levels.

#### 3. Identification of Positive Contributing Factors

**Environmental Well-being Enhancers:**
- **Renewable Energy Adoption**: Solar, wind, hydroelectric, and geothermal energy use and their measured benefits
- **Sustainable Practices**: Composting, water conservation, energy-efficient appliances, green building certifications
- **Conservation Efforts**: Protected areas, reforestation programs, wildlife corridors
- **Policy Effectiveness**: Carbon pricing, emission standards, renewable energy subsidies, and their measurable outcomes

**Success Stories**: Identification of regions or countries that have successfully improved environmental indicators, with analysis of the factors driving their success.

#### 4. Trends and Patterns Over Time

**Temporal Trends:**
- Historical trajectories of carbon emissions, pollution levels, renewable energy adoption, and other key indicators
- Identification of acceleration or deceleration points in environmental degradation
- Correlation of trends with major policy implementations or technological breakthroughs

**Forecasting**: Projected future scenarios based on current trends, including best-case, worst-case, and status-quo scenarios.

#### 5. Geographic Patterns and Regional Variations

**Spatial Insights:**
- Identification of regions with highest and lowest environmental impact per capita
- Understanding of how geographic factors (climate, urbanization, economic development) influence environmental indicators
- Hotspot maps showing areas of concern and areas of success

**Cross-Regional Comparisons**: Lessons learned from comparing different regions' approaches and outcomes.

#### 6. Actionable Insights and Recommendations

**Individual Level:**
- Prioritized list of lifestyle changes ranked by environmental impact
- Practical guidance on high-impact, achievable behavioral modifications
- Personalized recommendations based on geographic location and current lifestyle

**Organizational Level:**
- Data-driven strategies for corporate sustainability initiatives
- Benchmarking against industry standards
- ROI estimates for sustainability investments

**Policy Level:**
- Evidence-based recommendations for governmental interventions
- Identification of policy gaps and opportunities
- Frameworks for monitoring and evaluating policy effectiveness

#### 7. Comprehensive Visualizations

**Deliverables:**
- Interactive dashboards showing relationships between activities and environmental outcomes
- Time series visualizations of trends with key events annotated
- Geographic heat maps and choropleth maps
- Correlation matrices and feature importance charts
- Comparative bar charts and scatter plots illustrating key relationships
- Infographics summarizing key findings for public consumption


### Why This Question is Important

Understanding the quantitative relationship between human choices and environmental outcomes is crucial for several fundamental reasons:

#### 1. Informing Individual Action

**Empowerment Through Knowledge**: Many individuals want to live more sustainably but lack clear, quantitative information about which actions matter most. This analysis provides evidence-based guidance, helping people focus their efforts on high-impact changes rather than symbolic gestures.

**Combating Misinformation**: The sustainability space is rife with greenwashing and misleading claims. Data-driven analysis cuts through marketing narratives to reveal what actually makes a difference.

**Behavioral Economics**: Understanding precise impacts allows for better communication strategies that leverage behavioral insights to encourage adoption of sustainable practices.

#### 2. Guiding Organizational Strategy

**Resource Allocation**: Companies and non-profits can prioritize sustainability initiatives based on their potential environmental impact, ensuring efficient use of limited resources.

**Supply Chain Optimization**: Understanding the environmental footprint of different activities helps organizations identify the most impactful points of intervention in their operations and supply chains.

**Competitive Advantage**: As consumers and investors increasingly value sustainability, data-driven environmental strategies become a source of differentiation and reputation management.

#### 3. Informing Policy and Regulation

**Evidence-Based Policymaking**: Governments need quantitative evidence to design effective environmental regulations, incentives, and public campaigns. This analysis identifies where policy interventions will have the greatest impact.

**Measuring Policy Effectiveness**: By establishing baseline relationships and tracking changes over time, we can evaluate whether implemented policies achieve their intended environmental outcomes.

**International Cooperation**: Understanding common patterns and successful approaches across regions facilitates international climate agreements and knowledge sharing.

#### 4. Accelerating Technological Innovation

**Directing Research and Development**: Quantifying the environmental impact of current technologies helps identify the areas where innovation is most urgently needed.

**Market Signals**: Clear data on environmental costs creates market incentives for developing and adopting cleaner technologies and practices.

#### 5. Addressing Environmental Justice

**Equity Considerations**: Analysis at the regional level can reveal disparities in environmental quality and identify communities disproportionately affected by pollution or climate change.

**Fair Distribution of Responsibility**: Understanding per capita impacts across regions informs discussions about equitable distribution of mitigation responsibilities and climate finance.

#### 6. Long-term Sustainability and Survival

**Planetary Boundaries**: Human activities are pushing Earth's systems beyond safe operating boundaries. Quantifying these impacts is essential for understanding how close we are to irreversible tipping points.

**Future Generations**: The decisions we make today will determine the environmental legacy we leave. Data-driven understanding enables more responsible stewardship of the planet.

**Economic Stability**: Environmental degradation poses significant economic risks through natural disasters, resource scarcity, and health impacts. Prevention is far more cost-effective than remediation.

#### 7. Building Public Consensus

**Shared Understanding**: Objective, data-driven analysis helps build consensus across political and ideological divides by focusing on measurable facts rather than opinions.

**Combating Climate Denial**: Rigorous quantitative analysis adds to the overwhelming body of evidence for human-caused environmental change and the need for action.

**Motivation and Urgency**: Clearly communicating the magnitude of impact helps convey the urgency of the environmental crisis while also highlighting opportunities for positive change.

This project provides the analytical foundation needed to transform abstract environmental concerns into concrete, actionable understanding. By quantifying the relationships between human behavior and environmental outcomes, we enable more effective action at all levels of society—from individual lifestyle choices to global policy frameworks.


### Data Preparation and Exploration Plan

**Phase 1: Data Collection**
- Systematically download and catalog datasets from identified sources
- Document data provenance, collection methodologies, and known limitations
- Establish version control for datasets to ensure reproducibility

**Phase 2: Data Cleaning and Integration**
- Handle missing values, outliers, and inconsistencies
- Standardize geographic identifiers and temporal granularity
- Merge datasets from multiple sources into integrated analytical datasets
- Create data dictionary documenting all variables, units, and transformations

**Phase 3: Exploratory Data Analysis**
- Generate descriptive statistics for all key variables
- Create comprehensive visualizations to understand distributions and relationships
- Identify data quality issues requiring additional attention
- Form initial hypotheses about relationships to test in subsequent analysis

**Phase 4: Statistical Modeling**
- Implement correlation analysis to identify relationships
- Build regression models to quantify impacts
- Conduct time series analysis to understand trends
- Perform spatial analysis to reveal geographic patterns
- Apply clustering techniques to identify segments

**Phase 5: Interpretation and Communication**
- Synthesize findings into coherent narratives
- Create visualizations and dashboards for stakeholder communication
- Develop actionable recommendations based on findings
- Document methodology and results for transparency and reproducibility


### Outline of Project

**Directory Structure:**
```
capstone_project_environment/
├── data/
│   ├── raw/                          # Original, unmodified data files
│   ├── processed/                    # Cleaned and processed datasets
│   └── external/                     # External data sources
├── notebooks/
│   ├── 1_data_collection_and_preparation.ipynb
│   ├── 2_exploratory_data_analysis.ipynb
│   ├── 3_correlation_analysis.ipynb
│   ├── 4_regression_modeling.ipynb
│   ├── 5_time_series_analysis.ipynb
│   ├── 6_spatial_analysis.ipynb
│   ├── 7_clustering_and_segmentation.ipynb
│   └── 8_results_and_recommendations.ipynb
├── models/
│   └── trained_models/               # Saved regression and ML models
├── visualizations/
│   ├── plots/                        # Static plots and charts
│   ├── maps/                         # Geographic visualizations
│   └── dashboards/                   # Interactive dashboard files
├── reports/
│   ├── technical_report.pdf          # Detailed technical documentation
│   └── executive_summary.pdf         # High-level findings for stakeholders
├── presentation/
│   └── environmental_impact_analysis.pptx
└── README.md                         # This file
```

**Analysis Notebooks:**
1. **Data Collection and Preparation**: Data acquisition, cleaning, integration, and initial quality assessment
2. **Exploratory Data Analysis**: Descriptive statistics, distributions, and preliminary visualizations
3. **Correlation Analysis**: Identifying relationships between human activities and environmental indicators
4. **Regression Modeling**: Quantifying impacts and building predictive models
5. **Time Series Analysis**: Analyzing trends over time and forecasting future scenarios
6. **Spatial Analysis**: Geographic patterns and regional comparisons
7. **Clustering and Segmentation**: Identifying distinct groups and patterns
8. **Results and Recommendations**: Synthesis of findings and actionable insights


### Timeline and Deliverables

**Key Deliverables:**
1. Cleaned and integrated dataset ready for analysis
2. Comprehensive exploratory data analysis report with visualizations
3. Statistical models quantifying relationships between activities and environmental outcomes
4. Interactive dashboard for exploring data and findings
5. Technical report documenting methodology, findings, and limitations
6. Executive summary with actionable recommendations
7. Presentation for stakeholders
8. Published Jupyter notebooks for reproducibility and transparency


### Ethical Considerations and Limitations

**Data Limitations:**
- Data availability and quality may vary across regions and time periods
- Some environmental impacts (e.g., biodiversity loss, ecosystem degradation) are difficult to quantify comprehensively
- Establishing causality from observational data presents inherent challenges

**Ethical Considerations:**
- Results should not be used to blame specific populations without considering historical context and structural inequities
- Recommendations should be accessible and equitable, avoiding solutions that only privileged populations can adopt
- Environmental impacts of data collection and computation (e.g., energy use for analysis) should be acknowledged

**Transparency:**
- All data sources, methodologies, and assumptions will be clearly documented
- Uncertainty and confidence intervals will be reported alongside point estimates
- Limitations and potential biases will be explicitly acknowledged


### Contact and Further Information

**Project Lead:** Juliet Zheng

**Email:** juliet.zheng06@gmail.com

**GitHub Repository:** [Repository URL]

**Last Updated:** January 2026


---

*This capstone project demonstrates the application of data science techniques to address one of the most critical challenges facing humanity: understanding and mitigating human impact on the environment. Through rigorous quantitative analysis, we aim to transform environmental concerns into actionable insights that can drive meaningful change at individual, organizational, and societal levels.*