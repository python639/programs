import csv

#to write into CSV file
fp = open('sample.csv', 'w')
w = csv.writer(fp)
w.writerow(['1','arjun','arjun@gmail.com','9911111111'])

#it will overwrite into CSV file
fp = open('sample.csv', 'w')
w = csv.writer(fp)
w.writerow(['2','rajnish','rajnish@gmail.com','9922222222'])

#to append the values to CSV file
fp = open('sample.csv', 'a')
w = csv.writer(fp)
w.writerow(['3','kiran','kiran@gmail.com','9933333333'])

#to read from CSV file
fp = open('sample.csv', 'r')
r = csv.reader(fp)

for line in r:
    if line!=[]:
        print(line)
