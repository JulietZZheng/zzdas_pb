# Data Sources Guide

## Environmental Degradation and Well-being Analysis

This document provides detailed information about data sources for the capstone project.

---

**Master Dataset Characteristics:**
- **File**: `data/processed/master_dataset.csv`
- **Records**: 17,290 observations
- **Countries**: 186 countries with complete data (248 total coverage)
- **Time Period**: 1990-2020 (31 years)
- **Indicators**: 20 environmental and socioeconomic variables

### Primary Data Sources Used

The analysis successfully integrated data from these authoritative sources:

1. **World Bank Open Data** (Primary source)
   - PM2.5 air pollution (μg/m³)
   - CO2 emissions (metric tons per capita)
   - Energy use per capita
   - Renewable energy consumption
   - GDP per capita
   - Population metrics
   - Forest area percentage
   - Access to electricity

2. **World Health Organization (WHO)**
   - Life expectancy at birth
   - Health expenditure indicators
   - Air quality guidelines (10 μg/m³ benchmark)

### Data Quality Achieved

**Completeness:**
- 186 countries with complete 31-year time series
- 62 additional countries with partial coverage
- Missing data handling: Countries excluded if >20% missing values

**Validation:**
- Cross-validated with multiple sources
- Statistical outlier detection applied
- Temporal consistency verified
- Geographic standardization (ISO 3166 codes)

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

### 3. Kaggle Environmental Datasets
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
