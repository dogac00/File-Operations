import csv

# example.csv is for example:
# 1/2/2015,5,6,red
# 1/3/2015,5,2,green
# 1/4/2015,9,1,blue

with open(example.csv) as csvfile:
  readCSV = csv.reader(csvfile, delimiter=",")
  
  for row in readCSV:
    print(row)
    
  # output for this is
  # ['1/2/2015','5','6','red']
  # ['1/3/2015','5','2','green']
  # ['1/4/2015','9','1','blue']
  
  # we can separate data
  
  colors = []
  dates = []
  
  for row in readCSV:
    color = row[3]
    date = row[0]
    
    colros.append(color)
    dates.append(date)
    
  whatColor = input("What color do you wish yo know the date of?")
  color_index = colors.index(whatColor)
  
  theDate = dates[color_index]
  
  print("The date of {} is the date".format(whatColor))
