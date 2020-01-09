import csv

def getCSVData(filename):
  # # create an empty list to store rows
  # rows = []
  # # open the csv file
  # dataFile = open(fileName, 'r')
  # # create a CSV Reader from CSV file
  # reader = csv.reader(dataFile)
  # # skip the headers
  # next(reader)
  # # add rows from reader to list
  # x=0
  # i=1
  # for row in reader:
  #   if(x<30):
  #     rows.append(row)
  #     content = list(row[i] for i in included_cols)
  #     print(content)
  #     x+=1
  # return rows
  with open(filename,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter="\t")
    x=0
    next(csv_reader)
    for lines in csv_reader:
      num = lines[0]
      for n in csv_reader:
        num = n[0]
        # if(n)
      # if(lines==lines[1]):
      #   print(1)
      #   x+=1

