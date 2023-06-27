# Задача 40: Работать с файлом california_housing_train.csv, который 
# находится в папке sample_data. Определить среднюю стоимость дома, где 
# кол-во людей от 0 до 500 (population).

filtered_data = data[data["population"] < 501]
print(data["median_house_value"].mean())

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

min_population = data["population"].min()
min_population_data = data[data["population"] == min_population]
max_households = min_population_data["households"].max()
print(max_households)
