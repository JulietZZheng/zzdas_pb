# Quick Start Guide

## Environmental Degradation and Well-being Analysis

This guide will help you get started with the project quickly.

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook
- Git (optional, for version control)

---

## Setup Instructions

### 1. Clone or Download the Project

If using Git:
```bash
git clone [repository-url]
cd capstone_project_environment
```

Or simply navigate to the project directory:
```bash
cd capstone_project_environment
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all necessary Python packages.

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your browser.

---

## Project Workflow

Follow the notebooks in sequence:

### Phase 1: Data Preparation
**Notebook 1: Data Collection and Preparation**
- Download data from sources listed in `DATA_SOURCES.md`
- Place raw data files in `data/raw/`
- Run the notebook to clean and integrate data
- Output: Processed datasets in `data/processed/`

### Phase 2: Exploratory Analysis
**Notebook 2: Exploratory Data Analysis**
- Load processed data
- Generate descriptive statistics
- Create visualizations
- Document initial findings

### Phase 3: Statistical Analysis
**Notebook 3: Correlation Analysis**
- Identify relationships between variables
- Test statistical significance
- Visualize correlations

**Notebook 4: Regression Modeling**
- Build predictive models
- Quantify impacts
- Interpret coefficients
- Save trained models

### Phase 4: Advanced Analysis
**Notebook 5: Time Series Analysis**
- Analyze trends over time
- Forecast future scenarios
- Assess policy interventions

**Notebook 6: Spatial Analysis**
- Geographic pattern analysis
- Create interactive maps
- Identify hotspots

**Notebook 7: Clustering and Segmentation**
- Group similar regions
- Profile clusters
- Generate targeted recommendations

### Phase 5: Synthesis
**Notebook 8: Results and Recommendations**
- Synthesize all findings
- Generate comprehensive recommendations
- Create final report

---

## Data Collection Quick Reference

### Recommended Starting Point: Our World in Data

The easiest way to get started is with Our World in Data:

```python
import pandas as pd

# CO2 and emissions data
url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
df = pd.read_csv(url)

# Save to raw data folder
df.to_csv('data/raw/owid_co2_data.csv', index=False)
```

### World Bank Data

```python
import wbdata
import pandas as pd

# Define indicators
indicators = {
    'EN.ATM.CO2E.PC': 'co2_per_capita',
    'EG.USE.PCAP.KG.OE': 'energy_use_per_capita',
    'EG.FEC.RNEW.ZS': 'renewable_energy_pct'
}

# Fetch data
df = wbdata.get_dataframe(indicators, convert_date=True)

# Save
df.to_csv('data/raw/worldbank_environmental_indicators.csv')
```

---

## Directory Structure

```
capstone_project_environment/
├── README.md                          # Main project documentation
├── QUICK_START.md                     # This file
├── DATA_SOURCES.md                    # Detailed data source information
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── notebooks/                         # Jupyter notebooks (run in order)
│   ├── 1_data_collection_and_preparation.ipynb
│   ├── 2_exploratory_data_analysis.ipynb
│   ├── 3_correlation_analysis.ipynb
│   ├── 4_regression_modeling.ipynb
│   ├── 5_time_series_analysis.ipynb
│   ├── 6_spatial_analysis.ipynb
│   ├── 7_clustering_and_segmentation.ipynb
│   └── 8_results_and_recommendations.ipynb
│
├── data/                              # Data directory
│   ├── raw/                          # Original data files (download here)
│   ├── processed/                    # Cleaned, merged data
│   └── external/                     # External files (shapefiles, etc.)
│
├── models/                            # Saved models
│   └── trained_models/               # Trained ML models
│
├── visualizations/                    # Generated visualizations
│   ├── plots/                        # Static plots
│   ├── maps/                         # Geographic visualizations
│   └── dashboards/                   # Interactive dashboards
│
├── reports/                           # Final reports
├── presentation/                      # Presentation materials
└── images/                            # Project images
```

---

## Typical First Session

1. **Setup Environment** (15 minutes)
   - Create virtual environment
   - Install dependencies
   - Launch Jupyter

2. **Data Collection** (30-60 minutes)
   - Review DATA_SOURCES.md
   - Download initial datasets from Our World in Data
   - Optional: Set up World Bank API access

3. **Start Analysis** (remainder of time)
   - Open Notebook 1
   - Load and explore data
   - Begin data cleaning process

---

## Tips and Best Practices

### Data Management
- Keep raw data unmodified
- Document all data transformations
- Use version control for code
- Save intermediate results

### Analysis
- Run notebooks in sequence
- Don't skip exploratory analysis
- Document assumptions and decisions
- Save key visualizations

### Troubleshooting
- Check Python version compatibility
- Ensure all dependencies installed
- Verify data file paths
- Check for missing data files

---

## Common Issues and Solutions

### Issue: Module not found
**Solution:** Install missing package
```bash
pip install [package-name]
```

### Issue: Data file not found
**Solution:** Check file path and ensure data downloaded to correct location
```python
import os
print(os.getcwd())  # Check current directory
```

### Issue: Memory error with large datasets
**Solution:** Load data in chunks or use sampling
```python
df = pd.read_csv('large_file.csv', chunksize=10000)
# Or
df = pd.read_csv('large_file.csv', nrows=10000)  # Load first 10k rows
```

### Issue: Kernel crashes
**Solution:** Restart kernel and clear outputs
- Jupyter: Kernel -> Restart & Clear Output

---

## Customization

### Adapting to Your Specific Use Case

1. **Different Focus Area:** Modify analysis to emphasize specific environmental indicators
2. **Different Geographic Scope:** Filter data to specific regions/countries
3. **Different Time Period:** Adjust time range in data collection
4. **Additional Variables:** Include other factors relevant to your research question

### Adding New Analysis

Create new notebook:
```bash
# From notebooks directory
jupyter notebook new_analysis.ipynb
```

Follow similar structure to existing notebooks.

---

## Getting Help

### Documentation
- Python: https://docs.python.org/
- Pandas: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/
- Matplotlib: https://matplotlib.org/
- Seaborn: https://seaborn.pydata.org/

### Community
- Stack Overflow: Tag your questions with relevant library names
- GitHub Issues: For package-specific problems
- Data Science Stack Exchange: For methodology questions

### Project-Specific
- Review README.md for detailed project information
- Check DATA_SOURCES.md for data questions
- Consult notebook comments for analysis guidance

---

## Next Steps

After completing the analysis:

1. **Review Results**
   - Examine all generated visualizations
   - Verify findings are consistent
   - Check for any anomalies

2. **Create Reports**
   - Technical report for peers
   - Executive summary for stakeholders
   - Presentation slides

3. **Share and Iterate**
   - Share findings with others
   - Gather feedback
   - Refine analysis based on input

4. **Future Work**
   - Identify areas for deeper analysis
   - Collect additional data sources
   - Apply more advanced methods

---

## Checklist for First-Time Users

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed from requirements.txt
- [ ] Jupyter Notebook launching successfully
- [ ] Data sources reviewed in DATA_SOURCES.md
- [ ] Initial data downloaded to data/raw/
- [ ] Notebook 1 opened and ready to run
- [ ] README.md reviewed for project context

---

**Ready to Begin!**

Open `notebooks/1_data_collection_and_preparation.ipynb` and start your analysis!

For detailed project background and objectives, see the main README.md file.

---

**Last Updated:** January 2026