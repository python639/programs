from pyjavaproperties import Properties
file_path=r"C:\Users\HP\PycharmProjects\selenium\config.properties"

prop=Properties()

#to write data into a file
bname=prop.setProperty("browser","Chrome")    #arguments will be key & value
username=prop.setProperty("username","raj")
password=prop.setProperty("password","987456123")

input_stream=open(file_path,mode="w")
prop.store(input_stream)  #method to store values to the file

#read the data from a file
input_stream=open(file_path,mode="r")
prop.load(input_stream)

bname1=prop.getProperty("browser")   #calling keys to get the values
username1=prop.getProperty("username")
password1=prop.getProperty("password")

print(bname1)
print(username1)
print(password1)

input_stream.close()