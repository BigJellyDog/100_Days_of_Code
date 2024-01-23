import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240122.csv")


all_colors = data["Primary Fur Color"]
result = all_colors.value_counts()
new_data = pandas.DataFrame(result)
new_data.to_csv("new_data.csv")
print(result)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240122.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")