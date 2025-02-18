#This is the main Python code for my project!

#Installing required packages
#Ensure that the csv files in the folder are uploaded (through the file button on the left side or through mounting Google Drive)
#If run on a non-Colab IDE, delete the '!' in front of the pip install command. Some IDEs require direct installation on the terminal.
pip install pandas numpy scikit-learn tensorflow folium flask
import joblib, pandas as pd, statsmodels.api as sm
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#Loading in dataframes from nasa.gov and the World Census data
df_pop = pd.read_csv("populationDensity.csv", skiprows=1)
df_solar = pd.read_csv("solar_stats.csv")

#Standardizing naming within both datasets
df_pop.rename(columns={"Country Code": "Country Code"}, inplace=True)
df_solar.rename(columns={"ISO_A3": "Country Code"}, inplace=True)

#Merging dataframes to create one easily-accessible dataframe
df_merged = pd.merge(df_pop, df_solar, on="Country Code", how="inner")
df_merged = df_merged.dropna()

y = df_merged["Average practical potential \n(PVOUT Level 1, \nkWh/kWp/day), long-term"]

X = df_merged[["Population Density (people per square km)",
        "Average theoretical potential (GHI, kWh/m2/day), \nlong-term",
        "Average economic potential (LCOE, USD/kWh), 2018",
        "Average PV \nseasonality index, long-term",
        "Access to electricity\n(% of rural population), 2016"
       ]] #Split into multiple lines for readability

#Removes N/A or invalid data
X = X.dropna()
y = y[X.index]

#Creating AI model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Used RandomForestRegressor after trying Linear Regressor, which had an MSE of 0.03726435142780103 (higher than this model)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f'R² Score: {r2_score(y_test, y_pred)}') #Typically the best way of measuring accuracy
print(f'MAE: {mean_absolute_error(y_test, y_pred)}')
print(f'MSE: {mean_squared_error(y_test, y_pred)}') #Typically the best way of measuring error

#Testing User Interface

def get_user_input():
    try:
        # Collecting user inputs for all features
        population_density = float(input("Enter Population Density (people per square km): "))
        ghi = float(input("Enter Average Theoretical Potential (GHI, kWh/m²/day): "))
        lcoe = float(input("Enter Average Economic Potential (LCOE, USD/kWh, 2018): "))
        pv_seasonality_index = float(input("Enter Average PV Seasonality Index: "))
        electricity_access = float(input("Enter Access to Electricity (% of rural population, 2016): "))
        return np.array([[population_density, ghi, lcoe, pv_seasonality_index, electricity_access]])

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None

def main():
    #Main function
    print("Welcome to the AI Energy Equity Recommendation System!")
    user_data = get_user_input()

    if user_data is not None:
        # Make prediction
        predicted_pvout = model.predict(user_data)[0]

        print(f"Predicted Average Practical Potential (PVOUT Level 1): {predicted_pvout:.2f} kWh/kWp/day")

        # Recommendation threshold
        if predicted_pvout >= 4.0:
            print("Recommendation: Your region has high solar potential. Solar power is highly recommended.")
        else:
            print("Recommendation: Your region has low solar potential. Consider other energy options.")
    else:
        print("Failed to collect valid inputs. Please try again.")

if __name__ == "__main__":
    main()
