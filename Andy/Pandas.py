import pandas as pd



Car_Panda = {
    "Car": ['bmw', 'audi', 'ford'],
    "Licence": ['Okhn89','L098hg','KJHg32'], 
    "People": [2, 3, 4],
    "Driver": ['John', 'Doe', 'Smith']}
df = pd.DataFrame(Car_Panda, index = ["Person1", "Person2", "Person3"])

myvar = pd.DataFrame(Car_Panda)

print(myvar.loc[0])