## Project 1: Data Analysis on Food Access and Poverty Rate in Georgia Counties
## Overview
This project aims to understand the landscape of food access among different counties within Georgia. The primary focus is on investigating the relationship between poverty rates and access to food. The analysis involves data exploration, cleanup, and visualization using Pandas and Matplotlib in Jupyter notebooks.

## Project Structure
Data Exploration and Cleanup Notebooks: data cleaning and exploration files can be found in each group member's individual branch on this project along with detailed processes of cleaning and formatting the dataset(s).

Data Analysis Notebook: Final_Data.ipynb
Final data analysis, including visualizations.

## Major Findings with Visualizations:
See slide deck: https://docs.google.com/presentation/d/1nV3EgDTbyA7UhJjTXnjQGTgZELnmHuaeg_b_Gea6o5I/edit?usp=sharing

## Main Question: Does Poverty Rate Affect Food Access?
Hypothesis: As the poverty rate increases, access to food decreases.
## Findings: 

## Question 1: How does the poverty rate affect access to food?

**Percent Change in Number of Food Stores in Georgia's Top 5 High-Poverty Counties**
In the first figure, our focus is on the percent change in the number of food stores—convenience stores, SNAP-eligible stores, and supercenters—across the five counties in Georgia with the highest poverty rates. The trends observed reveal a challenging scenario in these economically distressed areas. A prevalent theme is the dominance of negative percent changes, indicating a lack of growth or development in the number of food stores. This suggests considerable obstacles in expanding access to food resources within counties grappling with high poverty rates.

One notable observation is the absence of discernible evidence supporting the growth of supercenters in these high-poverty counties. Despite both supercenters and SNAP stores being recognized as crucial for assisting low-income individuals and families to alleviate food insecurity, the lack of supercenter growth prompts further questions about the accessibility of these resources in areas facing economic hardships. In instances where there is evidence of development in Graph A, it is primarily in the form of an increase in the number of SNAP-eligible stores, underscoring the vital role of SNAP programs in addressing food insecurity in high-poverty areas.

## Question 2: How has this trend changed over time?

**Percent Change in Number of Food Stores in Georgia's Top 5 Low-Poverty Counties**
Shifting our attention to the second graph, which portrays the percent change in the number of food stores in the five counties in Georgia with the lowest poverty rates, a more positive narrative unfolds. Counties with lower poverty rates generally exhibit positive percent changes, indicating development in the number of food stores. This suggests a more favorable environment for expanding access to food resources in economically stable areas.
Of particular note in this graph is the evidence of supercenter growth, a contrast to the findings for the counties with high poverty rates. The presence of supercenters in economically stable areas is a positive indicator, as these establishments offer lower prices and a broader variety of products, potentially contributing to improved access to affordable and diverse food options.

However, the trends for SNAP-eligible and convenience stores in low-poverty rate areas are mixed. While the overall percent change is positive, indicating development, two out of the five counties show evidence of negative percent change in the number of SNAP-eligible stores and convenience stores. It is crucial to acknowledge that negative percent change in these store types may not necessarily imply a lack of access to food, and further investigation is warranted to understand the underlying dynamics.

In conclusion, the comparison between Graphs A and B underscores the disparities in access to food stores based on poverty rates. It emphasizes the need for targeted interventions to address food insecurity in economically distressed areas, where challenges in growth and development of food stores are more pronounced.

## Question 3: Who is affected?
When tackling the question of who is affected, we explored the demographics of the five counties with the highest poverty rate and the lowest poverty rate across Georgia. Based on the data we analyzed, it is clear the counties with the lowest poverty rate are predominantly white. While the counties with the highest poverty rate have significantly more diversity among black and Hispanic demographics.

When considering the above conclusions, it is clear the targeted interventions previously suggested would not only assist the counties with a higher poverty rate but also a significant portion of Georgia’s Black and Hispanic demographics.

## Question 4: How do these variables affect diabetes rates?
When analyzing how poverty rate affects the diabetes rate across Georgia, we determined there to be a r-squared value of .15. Then, when comparing the adult diabetes rate and the median household income, we determined there to be a r-squared value of .2. While these R-values do not indicate significant statistical significance, the slope of the linear regression to be trending in the direction of our hypothesis. While there is not irrefutable evidence to suggest the lack of access to food in counties with higher poverty rates leads to a higher diabetes rate across the population, the linear regression completed shows a positive trend between the two variables.

If food access is not addressed across the counties with a higher poverty rate, the overall health of these counties may see decline. While the analysis shows an increased rate of diabetes, it is not farfetched to assume other health related variables may be experiencing the same trend.

## Conclusion 
Based on the data we recovered, we failed to reject the null hypothesis. It does appear that as poverty rates increase, access to healthy food decreases. Additionally, it appears that as poverty rates increase, diabetes rates also increase.

Clarke County is a potential outlier in our data, because although it has one of the highest poverty rates in Georgia, the population has similar food access to counties with relatively low poverty rates. This makes sense, because it is a college town, with a lot of the economy being supported by students.
Potential limitations in our dataset include a lack of comprehensive poverty rates, limited health information, and no data to represent actual consumer purchasing trends.

## Acknowledgments
This project was completed as part of [Data Analytics and Visualization Bootcamp/Analysis of Food Access and Poverty Rates in GA].
Data source: [Food Environment Atlas ]

...
