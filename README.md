# Solar Horizons
#### Thanks for taking a look at my project for the 2024-25 Girls Who Code Challenge! This project leverages AI to identify energy-poor regions and recommend possibly solar energy solutions. It predicts solar energy potential (PVOUT Level 1) using factors of population density, solar irradiance, economic potential (LCOE), PV seasonality, and electricity access. The tool promotes sustainable energy solutions for underserved regions.


## Steps to run
1. Ensure you have Python installed on your system.

2. Install Dependencies:
Run the following command to install the necessary libraries:
`pip install flask pandas numpy scikit-learn joblib`

4. Run the Code:
Run the following command to start the program:
`python gwc_sustainability_2425.py`

5. User Interaction:
You will be prompted to enter values for:
Population Density (people per square km)
Average Theoretical Potential (GHI, kWh/m²/day)
Average Economic Potential (LCOE, USD/kWh)
PV Seasonality Index
Access to Electricity (% of rural population)

6. Output:
The tool will display the predicted solar energy potential (PVOUT Level 1) and provide a recommendation based on the prediction.


## Dataset Sources

The data used in this project is sourced from:

[World Bank](https://data.worldbank.org/indicator/EN.POP.DNST)

[Nasa Power](https://power.larc.nasa.gov/data-access-viewer/)
