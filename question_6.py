#Q6. Loop through the list "rawListOfTourPackages" and put data into TourPackage object
    #Split data by '|' and put it into list named "attributes"
    #Put the values into a newly created TourPackage object
attributes = []


for tourPackages in listOfTourPackages:
    attributes.append(TourPackage(tourPackages))
    #attributes.append(TourPackage(tourPackages))
    #attributes.append(TourPackage(tourPackages))



for dataSets in attributes:
    print (PrintTourPackageDetails(dataSets))
    #print (PrintTourPackageDetails(TourPackage(dataSets))
#End Q6.
