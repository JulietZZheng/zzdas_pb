# Data Sources Guide

## Environmental Degradation and Well-being Analysis

This document provides detailed information about data sources for the capstone project.

---

## Primary Data Sources

### 1. World Bank Open Data
**URL:** https://data.worldbank.org/

**Key Datasets:**
- CO2 emissions (metric tons per capita) - Indicator: EN.ATM.CO2E.PC
- Energy use (kg of oil equivalent per capita) - Indicator: EG.USE.PCAP.KG.OE
- Renewable energy consumption (% of total final energy consumption) - Indicator: EG.FEC.RNEW.ZS
- Forest area (% of land area) - Indicator: AG.LND.FRST.ZS
- GDP per capita - Indicator: NY.GDP.PCAP.CD
- Population density - Indicator: EN.POP.DNST

**Access Method:**
- Direct download from website
- API access: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation
- Python package: `wbdata` or `pandas_datareader`

**Data Format:** CSV, XML, JSON
**Coverage:** 1960-present, 200+ countries
**Update Frequency:** Annual

---

### 2. Environmental Protection Agency (EPA)
**URL:** https://www.epa.gov/

**Key Datasets:**
- Air Quality System (AQS) Data
- Greenhouse Gas Reporting Program (GHGRP)
- Toxic Release Inventory (TRI)
- National Emissions Inventory (NEI)

**Access Method:**
- Data.gov portal
- Direct downloads from EPA website
- API access for some datasets

**Coverage:** United States, varies by dataset
**Update Frequency:** Varies (annual to real-time)

---

### 3. European Environment Agency (EEA)
**URL:** https://www.eea.europa.eu/

**Key Datasets:**
- European air quality data
- Greenhouse gas emissions
- Energy consumption statistics
- Waste management data

**Access Method:**
- Download from EEA Data Viewer
- API available for some datasets

**Coverage:** European countries
**Update Frequency:** Annual/Quarterly

---

### 4. United Nations Environment Programme (UNEP)
**URL:** https://www.unep.org/

**Key Resources:**
- UNEP Environmental Data Explorer
- Global Environment Outlook (GEO) data portal
- Climate change indicators

**Coverage:** Global
**Update Frequency:** Varies

---

### 5. International Energy Agency (IEA)
**URL:** https://www.iea.org/

**Key Datasets:**
- World Energy Statistics
- Energy Balances
- CO2 Emissions from Fuel Combustion
- Renewable Energy Statistics

**Note:** Some data requires subscription

**Coverage:** Global, detailed country-level
**Update Frequency:** Annual

---

### 6. Our World in Data
**URL:** https://ourworldindata.org/

**Key Topics:**
- CO2 and Greenhouse Gas Emissions
- Energy
- Air Pollution
- Environmental Impacts of Food Production

**Access Method:**
- Direct download (CSV, XLSX)
- GitHub repository: https://github.com/owid/

**Advantages:**
- Cleaned and standardized data
- Well-documented
- Open source
- Combines multiple sources

**Coverage:** Global, historical data
**Update Frequency:** Regular updates

---

## Secondary Data Sources

### 7. Food and Agriculture Organization (FAO)
**URL:** http://www.fao.org/faostat/

**Key Datasets:**
- Agricultural emissions
- Land use
- Food production statistics
- Forestry data

---

### 8. Global Footprint Network
**URL:** https://www.footprintnetwork.org/

**Key Data:**
- Ecological Footprint by country
- Biocapacity
- Earth Overshoot Day calculations

**Note:** Some data requires registration

---

### 9. Climate Watch (World Resources Institute)
**URL:** https://www.climatewatchdata.org/

**Key Datasets:**
- Historical emissions
- NDC (Nationally Determined Contributions) targets
- Climate finance

**Access Method:**
- Download from website
- API available

---

### 10. Kaggle Environmental Datasets
**URL:** https://www.kaggle.com/datasets

**Search Terms:**
- "climate change"
- "CO2 emissions"
- "air quality"
- "environmental data"
- "sustainability"

**Popular Datasets:**
- Climate Change: Earth Surface Temperature Data
- Global Air Pollution Dataset
- World Happiness Report (includes environmental factors)

---

## Data Collection Strategy

### Phase 1: Core Environmental Indicators
1. CO2 emissions (World Bank, Our World in Data)
2. Energy consumption by source (IEA, World Bank)
3. Renewable energy adoption (IEA, World Bank)
4. Air quality indices (EPA, EEA, WHO)

### Phase 2: Human Activity Indicators
1. Transportation statistics (national statistical agencies)
2. Industrial production (World Bank, national sources)
3. Agricultural data (FAO)
4. Population and demographic data (World Bank, UN)

### Phase 3: Geographic and Contextual Data
1. Geographic boundaries (Natural Earth, GADM)
2. Economic indicators (World Bank, IMF)
3. Policy implementation dates (research literature, news sources)

---

## Data Integration Considerations

### Temporal Alignment
- Most sources provide annual data
- Align all datasets to common years (e.g., 2000-2020)
- Handle missing years through interpolation or exclusion

### Geographic Standardization
- Use ISO 3166 country codes for consistency
- Account for country name changes and splits
- Use World Bank or UN country classifications

### Unit Standardization
- Per capita metrics for comparability
- Convert all emissions to CO2 equivalents
- Standardize energy units (e.g., to joules or oil equivalents)

---

## Python Code Examples

### Example 1: Loading World Bank Data
```python
import pandas as pd
import wbdata

# Get CO2 emissions data
indicators = {'EN.ATM.CO2E.PC': 'co2_per_capita'}
df = wbdata.get_dataframe(indicators, convert_date=True)
```

### Example 2: Using Our World in Data
```python
import pandas as pd

# Load from Our World in Data GitHub
url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
df = pd.read_csv(url)
```

### Example 3: EPA Air Quality Data
```python
import pandas as pd

# Example for loading EPA AQS data
# Download file from https://aqs.epa.gov/aqsweb/airdata/download_files.html
df = pd.read_csv('annual_aqi_by_county_2020.csv')
```

---

## Data Quality Checklist

Before using any dataset, verify:
- [ ] Source credibility and authority
- [ ] Methodology documentation available
- [ ] Known limitations documented
- [ ] Update frequency understood
- [ ] Coverage (geographic and temporal) adequate
- [ ] Data format suitable for analysis
- [ ] License permits intended use
- [ ] Missing data patterns understood

---

## API Access Information

### World Bank API
- Base URL: http://api.worldbank.org/v2/
- Documentation: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- No authentication required
- Rate limits apply

### Climate Watch API
- Base URL: https://www.climatewatchdata.org/api/v1/
- Documentation: https://www.climatewatchdata.org/api-documentation
- No authentication required

---

## Data Storage Recommendations

### Directory Structure
```
data/
├── raw/                    # Original, unmodified data
│   ├── worldbank/
│   ├── epa/
│   ├── iea/
│   └── ...
├── interim/                # Intermediate processing steps
├── processed/              # Cleaned, merged, ready for analysis
└── external/               # External references, shapefiles, etc.
```

### File Naming Convention
`[source]_[description]_[year/daterange].[ext]`

Examples:
- `worldbank_co2_emissions_2000-2020.csv`
- `epa_airquality_2019.csv`
- `owid_energy_data_full.csv`

---

## Additional Resources

### Books and Papers
- IPCC Reports: https://www.ipcc.ch/
- Scientific literature via Google Scholar

### Tools
- Google Dataset Search: https://datasetsearch.research.google.com/
- Data.gov: https://www.data.gov/
- EU Open Data Portal: https://data.europa.eu/

---

## Contact and Support

For questions about specific data sources:
- World Bank: data@worldbank.org
- Our World in Data: https://ourworldindata.org/about#contact
- Check individual source websites for support contacts

---

**Last Updated:** January 2026