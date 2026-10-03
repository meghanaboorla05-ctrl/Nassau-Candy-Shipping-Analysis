# Nassau Candy Distributor — Shipping and Sales Analysis

## Project Overview
This project analyzes the Nassau Candy Distributor dataset using Python to understand sales performance, gross profit, shipping modes, and geographical distribution. Data analysis and visualizations are used to identify business patterns and summarize findings.

## Objectives
- Analyze sales and gross profit across shipping modes.
- Compare sales performance across regions and states.
- Identify the top 10 cities by sales.
- Analyze sales and gross profit by product division.
- Examine the recorded time difference between order dates and ship dates.
- Present findings using charts and summary tables.

## Technologies Used
- **Python**
- **Pandas** — data loading, cleaning, grouping, and analysis
- **Matplotlib** — data visualization
- **Visual Studio Code** — development environment
- **CSV** — dataset and exported analysis results

## Dataset
The project uses the Nassau Candy Distributor CSV dataset, containing order, customer, geographical, shipping, product, sales, units, and gross profit information.

## Project Workflow
1. Load the dataset using Pandas.
2. Inspect the dataset and prepare date columns.
3. Analyze sales and gross profit by shipping mode.
4. Compare performance across regions and states.
5. Identify the top 10 cities by sales.
6. Analyze product divisions.
7. Visualize results using Matplotlib.
8. Export summary tables to CSV files.
9. Review data-quality limitations.

## Key Findings
- Standard Class has the highest recorded sales among the shipping modes.
- The Pacific region has the highest recorded sales among the four regions.
- California has the highest recorded state-level sales.
- Chocolate is the leading product division by recorded sales.
- The analysis provides comparisons of gross profit by shipping mode and region.

## Project Outputs
The analysis generates charts and summary files, including:
- `state_sales_analysis.csv`
- `region_sales_analysis.csv`
- `shipping_mode_analysis.csv`
- `division_sales_analysis.csv`

## Limitations
The dataset does not include a factory or shipment-origin location. Therefore, actual factory-to-customer routes and route distances cannot be evaluated.

The recorded order dates range from 2024 to 2025, while ship dates range from 2026 to 2030. These dates require validation before calculated differences can be interpreted as actual delivery times.

## Future Improvements
- Validate and correct source dates.
- Include verified factory and warehouse locations.
- Calculate actual delivery times from reliable data.
- Map routes and compare distances.
- Build an interactive dashboard for business analysis.

## Conclusion
This project demonstrates the use of Python for business data analysis and visualization. It summarizes sales and gross profit patterns across shipping modes, regions, states, cities, and product divisions, while documenting data-quality issues that must be resolved before assessing actual route efficiency.

## Author
Meghana Boorla
