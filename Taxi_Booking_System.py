from datetime import date
import pyodbc

# Connecting a Program to Database
try:
    conn_String = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Programing\Python\TaxiBookingSystem.accdb;'
    conn = pyodbc.connect(conn_String)
    print("Connected")

except pyodbc.Error as e:
    print("Error", e)

cursor = conn.cursor()

#---------------------------------------------------------------------------------------------------------------------------------
class Customer:
    # CONSTRUCTOR
    def __init__(self, customerId, title, firstName, lastName, eMail, password, phoneNumber, town, country, address, postCode, paymentMethod):
        self.customerId = customerId
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.eMail = eMail
        self.phoneNumber = phoneNumber
        self.password = password
        self.town = town
        self.country = country
        self.postCode = postCode
        self.paymentMethod = paymentMethod
        self.address = address

#------------------------------------------------------------------------------------------
        # SETTERS
    def setCustomeID(self, customerId):
        self.customerId = customerId

    def settitle(self, title):
        self.title = title

    def setfirstName(self, firstName):
        self.firstName = firstName

    def setlastName(self, lastName):
        self.lastName = lastName

    def seteMail(self, eMail):
        self.eMail = eMail

    def setpassword(self, password):
        self.password = password

    def setphoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setphoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def settown(self, town):
        self.town = town

    def setcountry(self, country):
        self.country = country

    def setaddress(self, address):
        self.address = address

    def setpostCode(self, postCode):
        self.postCode = postCode

    def setpaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
#------------------------------------------------------------------------------------------
        # GETTERS
    def getCustomeID():
        return customerId
    
    def gettitle():
        return title
    
    def getfirstName():
        return firstName
    
    def getlastName():
        return lastName
    
    def geteMail():
        return eMail
    
    def getpassword():
        return password
    
    def getphoneNumber():
        return phoneNumber
    
    def gettown():
        return town
    
    def getcountry():
        return country
    
    def getaddress():
        return address
    
    def getpostCode():
        return postCode
    
    def getpaymentMethod():
        return paymentMethod
#------------------------------------------------------------------------------------------------------------------
class Booking:
    # CONSTRUCTOR
    def __init__(self, bookingId, customerId, driverId, bookingDate, bookingTime, startAddress, destinationAddress):
        self.bookingId = bookingId
        self.customerId = customerId
        self.driverId = driverId
        self.bookingDate = bookingDate
        self.bookingTime = bookingTime
        self.startAddress = startAddress
        self.destinationAddress = destinationAddress
        self.TodayDate = date.today()
        self.status = "Pending"
        self.payment = 'No'

#------------------------------------------------------------------------------------------
        # SETTERS
    def setBookingId(self, bookingId):
        self.bookingId = bookingId

    def setBookingDate(self, bookingDate):
        self.bookingDate = bookingDate

    def setBookingTime(self, bookingTime):
        self.bookingTime = bookingTime

    def setStartAddress(self, startAddress):
        self.startAddress = startAddress

    def setDestinationAddress(self, destinationAddress):
        self.destinationAddress = destinationAddress

    def setTodayDate(self, TodayDate):
        self.TodayDate = TodayDate

    def setStatus(self, status):
        self.status = status

    def setPayment(self, payment):
        self.payment = payment
#------------------------------------------------------------------------------------------
        # GETTERS
    def getBookingId():
        return bookingId
    
    def getBookingDate():
        return bookingDate

    def getBookingTime():
        return bookingTime
    
    def getStartAddress():
        return startAddress
    
    def getDestinationAddress():
        return destinationAddress
    
    def getTodayDate():
        return TodayDate
    
    def getStatus():
        return status
    
    def getPayment():
        return payment
#------------------------------------------------------------------------------------------------------------------
class TaxiDriver:
    # CONSTRUCTOR
    def __init__(self, driverId, title, firstName, lastName, eMail, password, phoneNumber, registrationNumber):
        self.driverId = driverId
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.eMail = eMail
        self.password = password
        self.phoneNumber = phoneNumber
        self.registrationNumber = registrationNumber

#------------------------------------------------------------------------------------------
        # SETTERS
    def setDriverID(self, driverId):
        self.driverId = driverId

    def settitle(self, title):
        self.title = title

    def setfirstName(self, firstName):
        self.firstName = firstName

    def setlastName(self, lastName):
        self.lastName = lastName

    def seteMail(self, eMail):
        self.eMail = eMail

    def setpassword(self, password):
        self.password = password

    def setphoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setRegistrationNumber(self, registrationNumber):
        self.registrationNumber = registrationNumber
#------------------------------------------------------------------------------------------
    # GETTERS
    def getDriverID():
        return driverId
    
    def gettitle():
        return title
    
    def getfirstName():
        return firstName
    
    def getlastName():
        return lastName
    
    def geteMail():
        return eMail
    
    def getpassword():
        return password
    
    def getphoneNumber():
        return phoneNumber
    
    def getRegistrationNumber():
        return registrationNumber
#------------------------------------------------------------------------------------------------------------------
class Administration:
    def __init__(self, adminId, title, firstName, lastName, password):
        self.adminId = adminId
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
#------------------------------------------------------------------------------------------
    # SETTERS
    def setAdminID(self, adminId):
        self.adminId = adminId

    def settitle(self, title):
        self.title = title

    def setfirstName(self, firstName):
        self.firstName = firstName

    def setlastName(self, lastName):
        self.lastName = lastName

    def setpassword(self, password):
        self.password = password
#------------------------------------------------------------------------------------------
    # GETTERS
    def getAdminID():
        return adminId
    
    def gettitle():
        return title
    
    def getfirstName():
        return firstName
    
    def getlastName():
        return lastName
    
    def getpassword():
        return password
#------------------------------------------------------------------------------------------------------------------

# Function to check login credentials
def check_login(email, password):
    # Adjust the query based on your database structure
    query = f"SELECT * FROM Customer WHERE Email = '{email}' AND Password = '{password}'"
    result = cursor.execute(query).fetchone()
    if result:
        id = result.customerId 
        userName = result.firstName+" "+result.lastName
        return True, userName, id
    else:
        return False, None, None

#---------------------------------------------------------------------------------------------------------------------

# Main Interface
a = True
b = True
print('Welcome to Taxi Booking System')
while (a == True):
    choice  = int (input('\n1- Register\n2- Login\n3- Close Program\n'))
    if(choice == 1):
        # Registring a Customer
        id = input("Enter Customer ID (eg: 000C): ")
        title = input("Enter Title: ")
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        eMail = input("Enter Email: ")
        phoneNumber = input("Enter Phone Number: ")
        password = input("Enter Password: ")
        town = input("Enter Town: ")
        country = input("Enter Country: ")
        address = input("Enter Address: ")
        postCode = input("Enter Post Code: ")
        paymentMethod = input("Enter Payment Method: ")
        customer = Customer(id, title, firstName, lastName, eMail, password, phoneNumber, town, country, address, postCode, paymentMethod)
        # Adding a Customer to DataBase
        try:
            cursor.execute("""
                INSERT INTO Customer (customerId, title, firstName, lastName, eMail, password, phoneNumber, town, country, address, postCode, paymentMethod)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                customer.customerId,
                customer.title,
                customer.firstName,
                customer.lastName,
                customer.eMail,
                customer.password,
                customer.phoneNumber,
                customer.town,
                customer.country,
                customer.address,
                customer.postCode,
                customer.paymentMethod
            ))
            conn.commit()
            print("Customer added successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
    # Log In to System 
    elif(choice == 2):
        eMail = input("\nEnter Email: ")
        password = input("Enter Password: ")
        logic_result, userName, ID = check_login(eMail, password)
        if (logic_result):
            print(f'Hello {userName}, You are Logged in......\n\n')
            while(b == True):
                cusChoice = int (input('1- View Booking\n2- Make Booking\n3- Delete Booking\n4- LogOut\n'))
                # View Booking
                if(cusChoice == 1):
                    print('\n')
                    cursor.execute('select * from Booking')
                    for row in cursor.fetchall():
                        if(row.customerId == ID):
                            print (f'{row.bookingId}- {row.startAddress}  to  {row.destinationAddress}')
                # Make Booking    
                elif(cusChoice == 2):
                    print('\n')
                    bookingId = input("Enter Booking Id (eg: 000B): ")
                    customerId = ID
                    cursor.execute('select * from Driver')
                    for row in cursor.fetchall():
                        print (f'{row.driverId}- {row.firstName} {row.lastName}')
                    driverId = input("\nEnter Driver ID: ")
                    bookingDate = input("Enter Booking Date: ")
                    bookingTime = input("Enter Booking Time: ")
                    startAddress = input("Enter Start Address: ")
                    destinationAddress = input("Enter Destination Address: ")
                    booking = Booking(bookingId, customerId, driverId, bookingDate, bookingTime, startAddress,  destinationAddress)
                    # Adding a Booking to DataBase
                    try:
                        cursor.execute("""
                            INSERT INTO Booking (bookingId, customerId, driverId, bookingDate, bookingTime, startAddress, destinationAddress, Todaydate, status, payment)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,(
                        booking.bookingId,
                        booking.customerId,
                        booking.driverId,
                        booking.bookingDate,
                        booking.bookingTime,
                        booking.startAddress,
                        booking.destinationAddress,
                        booking.TodayDate,
                        booking.status,
                        booking.payment,
                        ))
                        conn.commit()
                        print("Booking added successfully.")
                    except pyodbc.Error as e:
                        print("Error:", e)
                # Delete Booking        
                elif(cusChoice == 3):
                    print('\n')
                    cursor.execute('select * from Booking')
                    for row in cursor.fetchall():
                        if(row.customerId == ID):
                            print (f'{row.bookingId}- {row.startAddress}  to  {row.destinationAddress}')
                    booking_id = input('\nEnter the ID of Booking which you want to Delete: ')
                    delete_query = f"DELETE FROM Booking WHERE bookingId = '{booking_id}'"
                    try:
                        cursor.execute(delete_query)
                        conn.commit()
                        print(f"Booking with ID '{booking_id}' deleted successfully.")
                    except Exception as e:
                        conn.rollback()
                        print(f'Error deleting booking: {e}')
                elif(cusChoice == 4):
                    b = False
        else:
            print('Email or Password is Incorrect / Not Exists')    
    elif(choice == 3):
        print("\nProgram Terminating......\n")
        a = False
    else:
        print("Not Valid")
# End Of Program