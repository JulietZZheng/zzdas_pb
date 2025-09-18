In this application, it explores a dataset contains information on 426K cars to ensure the speed of processing. The goal is to understand what factors make a car more or less expensive. 
As a result of analysis, a clear recommendations is provided to client—a used car dealership—as to what consumers value in a used car.

Standard process in the industry for data projects CRISP-DM is used throughout these practical applications. 

You can see it in the file prompt_II.ipynb, each phase is well addressed, the notebook is runnable, the out put images can see in the images folder, and the finnal deploy report is at the end, which content is also at below

================================================================================
           USED CAR PRICE DRIVERS ANALYSIS
           Executive Report for Dealership Operations
================================================================================

SUMMARY
================

Our data science analysis of 380,000+ used car transactions has identified the key 
factors that drive consumer willingness to pay premium prices for used vehicles. 
This report provides actionable insights to optimize your inventory acquisition, 
pricing strategy, and profit margins.

KEY BUSINESS IMPACT:
• Identified the top price drivers that explain 75%+ of price variation
• Quantified price premiums for conditions
• Developed predictive model with ~85% accuracy for price estimation
• Provided specific inventory recommendations to maximize profitability



==================================================
1. CRITICAL PRICE DRIVERS DISCOVERED
==================================================

MAXIMUM IMPACT FACTORS:
ODOMETER:
  Correlation with price: -0.480
  Price difference (90th vs 10th percentile): $-24,740
  High value (90th percentile): 180000.0
  Low value (10th percentile): 16481.0

AGE:
  Correlation with price: -0.552
  Price difference (90th vs 10th percentile): $-28,605
  High value (90th percentile): 21.0
  Low value (10th percentile): 6.0

