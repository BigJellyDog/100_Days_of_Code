# data = []
# for line in open("weather_data.csv", "r"):
#     line = line.strip()
#     data.append(line)


import pandas


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for d in data:
#         if d[1] != 'temp':
#             temperatures.append(int(d[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# average_temp = 0
# for temp in temp_list:
#     average_temp += temp
# average_temp = average_temp // len(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# Get Data in Columns
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# print((monday.temp*(9/5))+32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela", "Chris", "Oscar"],
    "scores": [76, 56, 65, 88, 29]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
