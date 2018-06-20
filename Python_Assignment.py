import sys

#Q1. Create the TourPackage class

#class tourpackage
class TourPackage:

    #function __init__ the TourPackage
    def __init__(self, name = "no package name" , destination = "no destination" , duration = "no duration", period = "no travel period", price = 0.00):
        self.name = name
        self.destination = destination
        self.duration = duration
        self.period = period
        self.price = price

    #### start of the get functions for class TourPackage ####
    #function get name - return the name
    def getName(self):
        return self.name
    #function get destination - return the destination
    def getDestination(self):
        return self.destination
    #function get duration  - return the duration
    def getDuration(self):
        return self.duration
    #function get period  - return the period
    def getPeriod(self):
        return self.period
    #function get price  - return the price
    def getPrice(self):
        return self.price
    #function get gst price  - return the gst price
    def getPriceWithGST(self):
        priceWithGst = float(self.price) * 1.07
        return priceWithGst
        #return '%.2f' % priceWithGst
    #### end of the get functions for class TourPackage ####

    #### start of the set functions for class TourPackage ####
    #function set name - sets the name
    def setName(self,name):
        self.name = name
        #return name
    #function set destination - set the destination
    def setDestination(self,destination):
        self.destination = destination
        #return destination
    #function set duration - return the duration
    def setDuration(self,duration):
        self.duration = duration
        #return duration
    #function set period - return the period
    def setPeriod(self,period):
        self.period = period
        #return period
    #function set price - return the price
    def setPrice(self,price):
        self.price = price
        #return price

#End Q1.

#Q2. Create function PrintTourPackageDetails

def PrintTourPackageDetails(TourPackage):

    print ("Package Name:", TourPackage.getName())
    print ("Destination:", TourPackage.getDestination())
    print ("Duration:", TourPackage.getDuration())
    print ("Travel Period:", TourPackage.getPeriod())
    print ("Price:", TourPackage.getPrice())
    #print ("Price:", TourPackage.getPriceWithGST())

### function to print getName ###
def PrintGetName(TourPackage):

    return TourPackage.getName()

### function to print getName ###

#End Q2.


#Q3. Create function SearchBasedOnNameOrDestination

def SearchResult_Function(searchString,listOfTourPackages):
    searchResult = []
    ### use loops to find the array which contain value ###
    for tourPackage in listOfTourPackages:
      if(tourPackage.getName().lower().find(searchString.lower()) > -1 or tourPackage.getDestination().lower().find(searchString.lower()) > -1):
        searchResult.append(tourPackage)

    return searchResult

#End Q3.



#Q4.	Create an empty list listOfTourPackages

listOfTourPackages = []

#End Q4.

#Q5.
#		Open the input.txt file and put it into "file" object
#		Read data into list "rawListOfTourPackages" from the "file" object created in Q4
#		Close the file after data reading is done

### "rawListOfTourPackages" list ###
rawListOfTourPackages = []
### "rawListOfTourPackages" list ###

filePath = "input.txt"

### open the file path ###
file = open(filePath, "r")
data = file.readlines()

for itemsInData in data:
    packages = [itemsInData]
    for itemsInPackages in packages:
        updatedPackages = itemsInPackages.strip('\n').split('|')
    rawListOfTourPackages.append(updatedPackages)

file.close()

#End Q5.


#Q6. Loop through the list "rawListOfTourPackages" and put data into TourPackage object
    #Split data by '|' and put it into list named "attributes"
    #Put the values into a newly created TourPackage object
attributes = []

for tourPackages in rawListOfTourPackages:
  attributes.append(TourPackage(tourPackages[0],tourPackages[1],tourPackages[2],tourPackages[3],tourPackages[4]))

### update/copy the listOfTourPackages database ###
listOfTourPackages = attributes[:]
### update/copy the listOfTourPackages database ###

### length of the tours ###
noOfTourPackages = int(len(listOfTourPackages))
### length of the tours ###

### validate the dataset for the attributes ###
'''
for dataSets in listOfTourPackages:
    PrintTourPackageDetails(dataSets)
'''
#End Q6.

### Start of Additional Functions ###

### start of changes all case string to upper case ###
def upperCaseStringConverter(userInput):
    if not userInput.isdigit():
        userInput = userInput.upper()
        return userInput
    else:
        pass
        return userInput
### end of changes all case string to upper case ###

### start of display tour counter display ###
def tourCounterDisplay(tourPackageCounter,noOfTourPackages):
    if (tourPackageCounter > noOfTourPackages):
        pass
    else:
        print("=================================")
        print("Displaying tour", tourPackageCounter , " of ", noOfTourPackages)
### end of display tour counter display ###

### start of display List Data inside the input.txt ###
def displayListData(input_text):
    counter = 1
    for list_data_1 in input_text:
        print (counter,".", list_data_1)
        counter = counter + 1

### end of display List Data inside the input.txt ###

### End of Additional Functions ###


### start of program ###

############################
#start of storage of strings
############################

#store the program end note
programEnd = "Thank you for using Python Travel Agency"
#store the main menu note
mainmenuOption = "Back to Main Menu"

############################
#end of storage of strings
############################

selections = ["1. Display All Tour Packages",
              "2. Display Names of Tour Packages for Selection",
              "3. Search Tour Packages based on Name Substring",
              "4. Add New Travel Package",
              "5. Remove Existing Travel Package",
              "Q. Press Q to quit"]
userInput = ""

while (userInput != "Q"):
    #print out the selection menu from "selections"
    for options in selections:
      print(options)

    userInput = input("Please input your selection\n")
    userInput = upperCaseStringConverter(userInput)

    #check if user input is "Q", terminate the program
    if (userInput == "Q"):
        sys.exit("### " + "You have selected option " + ">> " + str(userInput) + " << " + " ###" \
        + "\n" + "### " + str(programEnd) + " ###")
    #end if

    # Todo Start: Print out the selected option
    else:
        print("### You have selected option: " + " ###" \
        + "\n" + "### " + str(selections[int(userInput)-1]) + " ###")
    # Todo End: Print out the selected option


    if(userInput == "1"):
        userInput = ""
        tourPackageCounter = 1

        while(userInput != "M"):
        #while(tourPackageCounter >= 1 and tourPackageCounter <= noOfTourPackages and userInput != "M"):
            #Q10. try

            try:

            #Q10 end try

                #Q7. Print out the menu and print the tour package details using the "PrintTourPackageDetails()" function defined in Q2
                ### will not display tour packages if tourpackages is above the current tour package available ###
                tourCounterDisplay(tourPackageCounter,noOfTourPackages)
                ### will not display tour packages if tourpackages is above the current tour package available ###
                print("=================================")
                ### PrintTourPackageDetails() function ###
                PrintTourPackageDetails(listOfTourPackages[tourPackageCounter-1])
                ### PrintTourPackageDetails() function ###
                print("=================================")
                print("Enter N for the next tour package")
                print("Enter P for the previous tour package")
                print("Enter M to return to the main menu")

                #End Q7.

                userInput = input()
                ### initalise to all upper case ###
                userInput = userInput.upper()

                #if user input is N, increase "tourPackageCounter" by 1, else if input is P, decrease "tourPackageCounter" by 1
                if(userInput == "N"):
                    tourPackageCounter += 1
                    ### reset the counter if exceeds the number of tour packages ###
                    '''
                    if(userInput == "N" and tourPackageCounter > noOfTourPackages):
                        tourPackageCounter = 1
                    '''
                    ### reset the counter if exceeds the number of tour packages ###

                #end if
                elif(userInput == "P"):
                    tourPackageCounter -= 1
                    ### reset backwards the counter if exceeds the number of tour packages ###
                    '''
                    if(tourPackageCounter == 0):
                        tourPackageCounter = noOfTourPackages
                        print("Out of range, back to the last item.")
                    '''
                    ### reset backwards the counter if exceeds the number of tour packages ###
                    if(tourPackageCounter == 0):
                        tourPackageCounter = tourPackageCounter + 1
                        print("Out of range, back to the last item.")
                #end elif
            #Q10 except
            except (IndexError) as e:
                print("You have entered a value out of range.")
                print("=================================")
                break
            #Q10 end except
        #end while
    #end if

    elif(userInput == "2"):
        print("=================================")
        print("Displaying name of tour packages for selection")
        tourPackageCounter = 1
        while(userInput != "M"):
            #Q10. try

            try:

            #Q10 end try

                #Q7. Loop through "listOfTourPackages" to display the tour package Destination and Name using the "getDestination()" and "getName()" functions of TourPackage class found in Q1.
                print("=================================")
                for i in range(noOfTourPackages):
                    print (i + 1,".",PrintGetName(listOfTourPackages[i]))
                print("=================================")
                #End Q7.

                ### function for userInput to check if value is a digit ###
                ### convert all lower cases into upper cases ###


                ### function for userInput to check if value is a digit ###


                print("Enter M to return to Main Menu")

                userInput = input("Please enter your selection\n")
                ### changes the value to upper case if the value is a string ###
                userInput = upperCaseStringConverter(userInput)

                if(userInput != "M"):
                    while(userInput != "M"):
                        tourPackageCounter = int(userInput)
                        #Q7. Print out the selected individual tour package in "listOfTourPackages" using the "PrintTourPackageDetails()" function defined in Q2
                        ### will not display tour packages if tourpackages is above the current tour package available ###
                        tourCounterDisplay(tourPackageCounter,noOfTourPackages)
                        ### will not display tour packages if tourpackages is above the current tour package available ###
                        print("=================================")
                        PrintTourPackageDetails(listOfTourPackages[tourPackageCounter-1])

                        #End Q7.
                        print("=================================")
                        print("Select from option", 1, "to", noOfTourPackages)
                        userInput = input("Enter another number to check another package or press M to previous menu")

                        ### changes the value to upper case if the value is a string ###
                        userInput = upperCaseStringConverter(userInput)

                    #end while
                    userInput = ""
                    tourPackageCounter = 1
                #end if
            #Q10 except

            except (IndexError,ValueError) as e:
                print("You have entered an invalid value.")
                print("=================================")
                break

            #Q10 end except
        #end while
    #end elif


    elif(userInput == "3"):
        userInput = ""
        searchString = input("Please enter your search input\n")
        while(userInput != "M"):

            searchResult = []
            #Q8. Based on the "searchString" input, call the SearchBasedOnNameOrDestination function to add the matching destination/name to "searchResult" list to be displayed later on

            ### "searchResult" list ###
            searchResult = SearchResult_Function(searchString,listOfTourPackages)[:]
            ### "searchResult" list ###

            #End Q8.

            #check the number of results
            if(len(searchResult) < 1):
                tourPackageCounter = 0
                print("===== No results found! =====")
            #end if
            else:
                tourPackageCounter = 1
            #end else

            if(tourPackageCounter != 0):
                #Q7. loop and print out all tour packages in "searchResult" using the "PrintTourPackageDetails()" function defined in Q2

                ### to display the counter in print result ###
                tourPackageDisplayCounter = 1
                ### to display the counter in print result ###

                for tourPackage in searchResult:
                    print("=================================")
                    print("Displaying tour", tourPackageDisplayCounter , " of ", len(searchResult))
                    print("=================================")
                    PrintTourPackageDetails(tourPackage)
                    tourPackageDisplayCounter = tourPackageDisplayCounter + 1

		        #End Q7.
            #end if
                userInput = input("1. Search again\nPress any buttons to go back\n")
                ### changes the value to upper case if the value is a string ###
                userInput = upperCaseStringConverter(userInput)
            if(userInput == "1"):
                searchString = input("Please enter your search input\n")
            #end if
            else:
                userInput = "M"
            #end else
        #end while
    #end elif

    if(userInput == "4"):

        while(userInput != "M"):
            ### collect data to put into string ###
            print("=================================")
            print ("Welcome to Tour Package Updater")
            print("=================================")

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
            print("=================================")
            print("Summary of New Package Added:")
            print (newPackage)
            print("=================================")
            ### collect data to put into string ###


            ### append file into input.txt ###
            file = open('input.txt','a')
            ### test dataset ###
            #newData = "more hello world"
            ### test dataset ###
            file.write(newPackage)
            file.close()
            ### append file into input.txt ###

            ### get input from user whether user wants to add any more package ###
            userInput = input("1. Add another package, Press any buttons to exit\n")
            ### changes the value to upper case if the value is a string ###
            userInput = upperCaseStringConverter(userInput)

            if(userInput == "1"):
                pass
            #end if
            else:
                userInput = "M"
            #end else
            ### get input from user whether user wants to add any more package ###

            '''
            ###test data ###
            trumpKimFiesta
            Singapore
            5
            12 June 2018 to 17 June 2018
            2888
            ### test data ###
            '''

        #end while
    #end if

    if(userInput == "5"):

        while(userInput != "M"):
            ### read existing data inside the file ###
            print("=================================")
            print ("Welcome to Tour Package Remover")
            print("=================================")

            input_text = []
            file_read = open('input.txt','r')
            for list_data_1 in file_read.readlines():
                input_text.append(list_data_1.strip('\n'))

            file_read.close()
            displayListData(input_text)
            ### read existing data inside the file ###

            ### make changes to existing data inside the file ###
            print("=================================")
            listRemover = int(input("Select number from list to remove"))
            print("=================================")
            del input_text[listRemover - 1]
            displayListData(input_text)
            ### make changes to existing data inside the file ###

            ### write new data into the file ###
            joinInput_text = '\n'.join(input_text)
            file_write = open('input.txt','w')
            file_write.write(joinInput_text)
            file_write.close()
            ### write new data into the file ###

            print("=================================")
            print ("Package removed Successfully")
            print("=================================")
            ###test dataset ###
            #trumpKimFiesta_1|Singapore|5D4N|12 June 2018 to 17 June 2018|2888
            ###test dataset ###
            ### write new data into the file ###
            ### end of confirm removal ###


            ### get input from user whether user wants to add any more package ###
            print("=================================")
            userInput = input("1. Remove another package \nPress any buttons to exit\n")
            print("=================================")
            ### changes the value to upper case if the value is a string ###
            userInput = upperCaseStringConverter(userInput)

            if(userInput == "1"):
                pass
            #end if
            else:
                userInput = "M"
            #end else
            ### get input from user whether user wants to add any more package ###

        #end while
    #end if

#end while

### end of program ###
