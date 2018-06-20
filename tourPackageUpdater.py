'''
### collect data to put into string ###
print ("Welcome to Tour Package Updater")

input_package = input("Enter the name of package : ")
input_destination = input("Enter the destination : ")
input_event_duration_day = int(input("enter the duration of event : "))
input_event_date = str(input("enter the duration period of event : "))
input_price = str(input("Enter the price of the package : "))

input_event_duration_night = 0
if input_event_duration_day > 0:
    input_event_duration_night = input_event_duration_day - 1

def printEventDuration(input_event_duration_day,input_event_duration_night):
    return (str(input_event_duration_day)+"D"+str(input_event_duration_night)+"N")



newPackage = (input_package + "|" + input_destination + "|" + \
              printEventDuration(input_event_duration_day,input_event_duration_night) + "|" +\
              input_event_date + "|" + input_price
              )
#+ input_event_date + str(input_price))

print (newPackage)
### collect data to put into string ###


### append file into input.txt ###
file = open('helloworld.txt','a')
### test dataset ###
#newData = "more hello world"
### test dataset ###
file.write(newPackage + '\n')
file.close()
### append file into input.txt ###

#test dataSets
'''

def displayListData(input_text):
    counter = 1
    for list_data_1 in input_text:
        print (counter, list_data_1)
        counter = counter + 1

### read existing data inside the file ###
input_text = []
file_read = open('helloworld.txt','r')
for list_data_1 in file_read.readlines():
    input_text.append(list_data_1.strip('\n'))

file_read.close()
displayListData(input_text)
### read existing data inside the file ###

### make changes to existing data inside the file ###
listRemover = int(input("Select number from list to remove"))
del input_text[listRemover - 1]
displayListData(input_text)
### make changes to existing data inside the file ###

option = int(input("enter your option"))

if (option == 1):
    ### write new data into the file ###
    joinInput_text = ','.join(input_text)
    new_TextData = joinInput_text.replace(',','\n')
    file_write = open('helloworld.txt','w')
    file_write.write(new_TextData)
    file_write.close()
    ### write new data into the file ###


'''
trumpKimFiesta
Singapore
5
12 June 2018 to 17 June 2018
2888
'''
#trumpKimFiesta_1|Singapore|5D4N|12 June 2018 to 17 June 2018|2888
