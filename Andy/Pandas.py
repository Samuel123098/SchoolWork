import pandas as pd



df = pd.read_csv('/Users/san/Documents/GitHub/SchoolWork/Andy/cars.csv', index_col=0)
new_car = input("Enter car brand: ")
new_licence = input("Enter licence plate: ")
new_people = int(input("Enter number of people: "))
new_driver = input("Enter driver's name: ")

new_data = {
    "Car": new_car,
    "Licence": new_licence,
    "People": new_people,
    "Driver": new_driver
}

df.loc[f"Person{len(df) + 1}"] = new_data.values()

df.to_csv('/Users/san/Documents/GitHub/SchoolWork/Andy/cars.csv', index=True)



print(df)
