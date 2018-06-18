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

#End Q2.


#Q3. Create function SearchBasedOnNameOrDestination

def SearchResult_Function(searchString,listOfTourPackages):

    searchResult = []
    ### use loops to find the array which contain value ###
    for tourPackage in listOfTourPackages:
      if(tourPackage[1].lower().find(searchString.lower()) > -1 or tourPackage[0].lower().find(searchString.lower()) > -1):
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

#End Q6.
'''

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
              "Q. Press Q to quit"]
userInput = ""

while (userInput != "Q"):
    #print out the selection menu from "selections"
    for options in selections:
      print(options)

    userInput = input("Please input your selection\n")

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

        while(tourPackageCounter >= 1 and tourPackageCounter <= noOfTourPackages and userInput != "M"):
            #Q10. try
#
            #<...insert code here...>

            #Q10 end try

                #Q7. Print out the menu and print the tour package details using the "PrintTourPackageDetails()" function defined in Q2
                print("Displaying tour", tourPackageCounter , " of ", noOfTourPackages)
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
                #end if
                elif(userInput == "P"):
                    tourPackageCounter -= 1
                    if(tourPackageCounter == 0):
                        tourPackageCounter = 1
                        print("Out of range, back to the last item.")
                #end elif
            #Q10 except

            #<...insert code here...>

            #Q10 end except
        #end while
    #end if

    elif(userInput == "2"):
        print("Displaying name of tour packages for selection")
        tourPackageCounter = 1
        while(userInput != "M"):
            #Q10. try

            #<...insert code here...>

            #Q10 end try
                #Q8. Loop through "listOfTourPackages" to display the tour package Destination and Name using the "getDestination()" and "getName()" functions of TourPackage class found in Q1.

                #<...insert code here...>

                #End Q8.

                print("Enter M to return to Main Menu")

                userInput = input("Please enter your selection\n")
                if(userInput != "M"):
                    while(userInput != "M"):
                        tourPackageCounter = int(userInput)
                        #Q7. Print out the selected individual tour package in "listOfTourPackages" using the "PrintTourPackageDetails()" function defined in Q2

                        #<...insert code here...>

                        #End Q7.
                        userInput = input()
                    #end while
                    userInput = ""
                    tourPackageCounter = 1
                #end if
            #Q10 except

            #<...insert code here...>

            #Q10 end except
        #end while
    #end elif

'''
    elif(userInput == "3"):
        userInput = ""
        searchString = input("Please enter your search input\n")
        while(userInput != "M"):

            searchResult = []
            #Q9. Based on the "searchString" input, call the SearchBasedOnNameOrDestination function to add the matching destination/name to "searchResult" list to be displayed later on

            #<...insert code here...>

            #End Q9.

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

                #<...insert code here...>

		        #End Q7.
            #end if
            userInput = input("1. Search again\n2. Return to Main Menu\n")
            if(userInput == "1"):
                searchString = input("Please enter your search input\n")
            #end if
            else:
                userInput = "M"
            #end else
        #end while
    #end elif
#end while

### end of program ###
'''
