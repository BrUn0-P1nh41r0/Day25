import pandas

#data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(data["temp"].mean())
#print(data["temp"].max())

#print(data["condition"])

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
#Create a dataframe from scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}

#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
