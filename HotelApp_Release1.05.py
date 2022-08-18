## CS 4400 - Section A - Group 85


from tkinter import *
import pymysql
import re
import datetime


class FancyHotelApp():
    def __init__(self):
        ## Create the login window on initialize
        self.loginWin = Tk()
        self.loginWin.title("Login")
        ## Create String Variables for the Text Fields
        self.svUsername = StringVar()
        self.svPassword = StringVar()
        ## Add labels and entry fields for username and password
        Label(self.loginWin, text="Username:").grid(row=0, column=0, sticky=E)
        userEntry = Entry(self.loginWin, text=self.svUsername, width=30)
        userEntry.grid(row=0, column=1, columnspan=3)
        Label(self.loginWin, text="Password:").grid(row=1, column=0, sticky=E)
        pwEntry = Entry(self.loginWin, text=self.svPassword, width=30)
        pwEntry.grid(row=1, column=1, columnspan=3)
        ## Add a filler blank label to create more space
        Label(self.loginWin, text=" ").grid(row=2, column=1)
        ## Add button for login
        loginButton = Button(self.loginWin, text="Login", command=self.login)
        loginButton.grid(row=3, column=2)
        ## Add a filler blank label to create more space
        Label(self.loginWin, text=" ").grid(row=4, column=1)
        ## Add label for "new user?" text
        Label(self.loginWin, text="New User? Create an Account Here:").grid(row=5, column=2, sticky=E)
        ## Add button for registration
        registerButton = Button(self.loginWin, text="Register", command=self.toRegisterWin)
        registerButton.grid(row=5, column=3, sticky=W)
        ## Indicator variable of whether user is a customer
        self.isCustomer = 0
        ## Create dictionary to lookup number of days in a given month
        self.monthsDaysDict = {1: 31,2: 28,3: 31,4: 30,5: 31,
                               6: 30, 7: 31,8: 31,9: 30,10: 31,
                               11: 30,12: 31}
        ## Call methods to create the other windows
        self.registerWin()
        self.chooseFuntionWin()
        self.searchRoomsWin()
        self.makeReservationWin()
        self.paymentInformationWin()
        self.confirmationScreenWin()
        self.updateReservationWin()
        self.cancelReservationWin()
        self.viewReviewWin()
        self.provideReviewWin()
        self.reservationReportWin()
        self.popularRoomReportWin()
        self.revenueReportWin()
        ## Withdraw other windows
        self.registrationWin.withdraw()
        self.chooseFunctionalityWin.withdraw()
        self.searchRmWin.withdraw()
        self.makeResWin.withdraw()
        self.paymentInfoWin.withdraw()
        self.confScreenWin.withdraw()
        self.updateResWin.withdraw()
        self.cancelResWin.withdraw()
        self.viewRevWin.withdraw()
        self.giveReviewWin.withdraw()
        self.resReportWin.withdraw()
        self.popRoomReportWin.withdraw()
        self.revReportWin.withdraw()
        ## Call mainloop
        self.loginWin.mainloop()

    def registerWin(self):
        ## Create the registration window
        self.registrationWin = Toplevel(self.loginWin)
        self.registrationWin.title("New User Registration")
        ## Create string variables for the text fields
        self.svUsernameCreate = StringVar()
        self.svPasswordCreate = StringVar()
        self.svConfirmPassword = StringVar()
        self.svEmail = StringVar()
        ## Add labels and entry fields
        Label(self.registrationWin, text="Username:").grid(row=0, column=0, sticky=W)
        Label(self.registrationWin, text="Password:").grid(row=1, column=0, sticky=W)
        Label(self.registrationWin, text="Confirm Password:").grid(row=2, column=0, sticky=W)
        Label(self.registrationWin, text="Email:").grid(row=3, column=0, sticky=W)
        userEntry = Entry(self.registrationWin, text=self.svUsernameCreate, width=30)
        userEntry.grid(row=0, column=1, columnspan=3)
        pwEntry = Entry(self.registrationWin, text=self.svPasswordCreate, width=30)
        pwEntry.grid(row=1, column=1, columnspan=3)
        pwConfEntry = Entry(self.registrationWin, text=self.svConfirmPassword, width=30)
        pwConfEntry.grid(row=2, column=1, columnspan=3)
        emailEntry = Entry(self.registrationWin, text=self.svEmail, width=30)
        emailEntry.grid(row=3, column=1, columnspan=3)
        ## Add a filler blank label to create more space
        Label(self.registrationWin, text=" ").grid(row=4, column=0)
        ## Add submit button
        submitButton = Button(self.registrationWin, text="Submit", command=self.register)
        submitButton.grid(row=5, column=2)
        #add back button
        backButton = Button(self.registrationWin, text="Back",command=self.backToLogin).grid(row=5,column=1)

    def backToLogin(self):
        self.registrationWin.withdraw()
        self.loginWin.deiconify()

    def chooseFuntionWin(self):
        ## Create the "Choose Functionality" window
        self.chooseFunctionalityWin = Toplevel(self.loginWin)
        self.chooseFunctionalityWin.title("Choose functionality")
        ## Add label for "welcome"
        Label(self.chooseFunctionalityWin, text="Welcome").grid(row=0, column=0,sticky=W)
        ## Add filler blank labels to create more space
        Label(self.chooseFunctionalityWin, text=" ").grid(row=1, column=0)
        Label(self.chooseFunctionalityWin, text="                                       ").grid(row=1, column=1)
        ## Add buttons based on whether the user is customer or management
        if self.isCustomer == 1:
            newReservButton = Button(self.chooseFunctionalityWin, text="Make a new reservation", command=self.makeNewReservation)
            newReservButton.grid(row=2, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=3, column=0)
            updateReservButton = Button(self.chooseFunctionalityWin, text="Update a reservation", command=self.updateReservation)
            updateReservButton.grid(row=4, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=5, column=0)
            cancelReservButton = Button(self.chooseFunctionalityWin, text="Cancel a reservation", command=self.cancelReservation)
            cancelReservButton.grid(row=6, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=7, column=0)
            giveFeedbackButton = Button(self.chooseFunctionalityWin, text="Provide feedback", command=self.giveFeedback)
            giveFeedbackButton.grid(row=8, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=9, column=0)
            viewFeedbackButton = Button(self.chooseFunctionalityWin, text="View feedback", command=self.viewFeedback)
            viewFeedbackButton.grid(row=10, column=0, sticky=W)
            logoutButton = Button(self.chooseFunctionalityWin, text="Logout", command=self.logout)
            logoutButton.grid(row=10, column=1, sticky=E)
        else:
            viewReservReportButton = Button(self.chooseFunctionalityWin, text="View reservation report", command=self.viewResReport)
            viewReservReportButton.grid(row=2, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=3, column=0)
            viewPopRoomCatButton = Button(self.chooseFunctionalityWin, text="View popular room category report", command=self.viewPopRoomReport)
            viewPopRoomCatButton.grid(row=4, column=0, sticky=W)
            ## Add a filler blank label to create more space
            Label(self.chooseFunctionalityWin, text=" ").grid(row=5, column=0)
            viewRevenueButton = Button(self.chooseFunctionalityWin, text="View revenue report", command=self.viewRevReport)
            viewRevenueButton.grid(row=6, column=0, sticky=W)
            logoutButton = Button(self.chooseFunctionalityWin, text="Logout", command=self.logout)
            logoutButton.grid(row=6, column=1, sticky=E)

    def logout(self):
        self.chooseFunctionalityWin.withdraw()
        self.loginWin.deiconify()
        
    def searchRoomsWin(self):
        ## Create the "Search Rooms" window
        self.searchRmWin = Toplevel(self.loginWin)
        self.searchRmWin.title("Search Rooms")
        ## Create string variables for the location and dates
        self.svLocation = StringVar()
        self.svStartDate = StringVar()
        self.svEndDate = StringVar()
        ## Add filler blank labels to create more space
        Label(self.searchRmWin, text=" ").grid(row=0, column=0)
        ## Add label and drop down box for location
        Label(self.searchRmWin, text="Location:").grid(row=1, column=0)
        locDrop = OptionMenu(self.searchRmWin, self.svLocation, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        locDrop.grid(row=1, column=1)
        ## Add filler blank labels to create more space
        Label(self.searchRmWin, text=" ").grid(row=2, column=0)
        ## Add labels and entry boxes for dates
        Label(self.searchRmWin, text="Start Date: (MM/DD/YYYY)").grid(row=3, column=0)
        sDateEntry = Entry(self.searchRmWin, text=self.svStartDate, width=15)
        sDateEntry.grid(row=3, column=1)
        Label(self.searchRmWin, text="End Date: (MM/DD/YYYY)").grid(row=3, column=2)
        eDateEntry = Entry(self.searchRmWin, text=self.svEndDate, width=15)
        eDateEntry.grid(row=3, column=3)
        ## Add filler blank labels to create more space
        Label(self.searchRmWin, text=" ").grid(row=4, column=0)
        ## Add search button
        searchButton = Button(self.searchRmWin, text="Search", command=self.searchRooms)
        searchButton.grid(row=5, column=3)
        ## Add a home button
        homeButton = Button(self.searchRmWin, text="Return Home", command=self.searchRoomWinToHome)
        homeButton.grid(row=5, column=0)

    def searchRoomWinToHome(self):
        self.goToHome(self.searchRmWin)

    def makeReservationWin(self):
        ## Create the "Make a Reservation" main window
        self.makeResWin = Toplevel(self.loginWin)
        self.makeResWin.title("Make a Reservation")
        ## Add filler blank labels to create more space
        Label(self.makeResWin, text=" ").grid(row=0, column=0)
        ## Create Labels for Column Headers
        Label(self.makeResWin, text="Room number").grid(row=1, column=0, sticky=W)
        Label(self.makeResWin, text="Room category").grid(row=1, column=1, sticky=W)
        Label(self.makeResWin, text="Number persons allowed").grid(row=1, column=2, sticky=W)
        Label(self.makeResWin, text="Cost per day").grid(row=1, column=3, sticky=W)
        Label(self.makeResWin, text="Cost of extra bed per day").grid(row=1, column=4, sticky=W)
        Label(self.makeResWin, text="Select room").grid(row=1, column=5, sticky=W)
        
    def paymentInformationWin(self):
        ## Create the "Payment Information" window
        self.paymentInfoWin = Toplevel(self.loginWin)
        self.paymentInfoWin.title("Payment Information")
        ## Add a filler blank label to create more space
        Label(self.paymentInfoWin, text=" ").grid(row=0, column=0)
        ## Create string variables for name, card number (add), exp. date, and card number (delete)
        self.svNameonCard = StringVar()
        self.svCardNumAdd = StringVar()
        self.svCardExpDate = StringVar()
        self.svCardCVV = StringVar()
        self.svCardNumDelete = StringVar()
        ## Add label "Add Card"
        Label(self.paymentInfoWin, text="Add Card").grid(row=1, column=0)
        ## Add a filler blank label to create more space
        Label(self.paymentInfoWin, text=" ").grid(row=2, column=0)
        ## Add labels and entry boxes for adding a card
        Label(self.paymentInfoWin, text="Name on card:").grid(row=3, column=0, sticky=W)
        cardNameAddEntry = Entry(self.paymentInfoWin, text=self.svNameonCard, width=30)
        cardNameAddEntry.grid(row=3, column=1, sticky=W)
        Label(self.paymentInfoWin, text="Card number:").grid(row=4, column=0, sticky=W)
        cardNameAddEntry = Entry(self.paymentInfoWin, text=self.svCardNumAdd, width=30)
        cardNameAddEntry.grid(row=4, column=1, sticky=W)
        Label(self.paymentInfoWin, text="Expiration Date (MM/YYYY):").grid(row=5, column=0, sticky=W)
        cardNameAddEntry = Entry(self.paymentInfoWin, text=self.svCardExpDate, width=15)
        cardNameAddEntry.grid(row=5, column=1, sticky=W)
        Label(self.paymentInfoWin, text="CVV:").grid(row=6, column=0, sticky=W)
        cardNameAddEntry = Entry(self.paymentInfoWin, text=self.svCardCVV, width=10)
        cardNameAddEntry.grid(row=6, column=1, sticky=W)
        ## Add a filler blank label to create more space
        Label(self.paymentInfoWin, text=" ").grid(row=7, column=0)
        ## Add save button
        saveButton = Button(self.paymentInfoWin, text="Save", command=self.saveNewCard)
        saveButton.grid(row=8, column=0)
        ## Add a button to return to reservation window
        resReturnButton = Button(self.paymentInfoWin, text="Return to Reservation Window",
                                 command=self.resReturnHome)
        resReturnButton.grid(row=8, column=1)
        ## Add a filler label to give space between add and delete sides of window
        Label(self.paymentInfoWin, text="               ").grid(row=3, column=2)

        ## Add label "Delete Card"
        Label(self.paymentInfoWin, text="Delete Card").grid(row=1, column=3)
        ## Add label and drop down menu for card number
        Label(self.paymentInfoWin, text="Card Number:").grid(row=3, column=3)
        self.cardNumDeleteList = []

    def resReturnHome(self):
        self.paymentInfoWin.withdraw()
        self.makeResWin.deiconify()
        
    def confirmationScreenWin(self):
        ## Create the "Confirmation Screen" window
        self.confScreenWin = Toplevel(self.loginWin)
        self.confScreenWin.title("Confirmation Screen")
        ## Create a string variable for the reservation id
        self.svReservID = StringVar()
        ## Add a filler blank label to create more space
        Label(self.confScreenWin, text=" ").grid(row=0, column=0)
        ## Create the label and entry box for reservation id
        Label(self.confScreenWin, text="Your Reservation ID:").grid(row=1,column=0)
        resIDEntry = Entry(self.confScreenWin, text=self.svReservID, state="readonly")
        resIDEntry.grid(row=1, column=1)

    def updateReservationWin(self):
        ## Create the "Update Reservation" window
        self.updateResWin = Toplevel(self.loginWin)
        self.updateResWin.title("Update Reservation")
        ## Create a string variable for reservation id
        self.svUpdateResID = StringVar()
        ## Add a filler blank label to create more space
        Label(self.updateResWin, text=" ").grid(row=0, column=0)
        ## Create a label and entry box for reservation id
        Label(self.updateResWin, text="Reservation ID").grid(row=1,column=0)
        resIDEntry = Entry(self.updateResWin, text=self.svUpdateResID, width=20)
        resIDEntry.grid(row=1, column=1)
        ## Create search button
        searchButton = Button(self.updateResWin, text="Search", command=self.updateResSearch)
        searchButton.grid(row=1, column=2)
        ## Create home buttton
        homeButton = Button(self.updateResWin, text="Return Home", command=self.updateResSearchToHome)
        homeButton.grid(row=2, column=2)
        ## Remaining items on update screen will be created by the method called by the search button

    def cancelReservationWin(self): 
        ## Create the "Cancel Reservation" window
        self.cancelResWin = Toplevel(self.loginWin)
        self.cancelResWin.title("Cancel Reservation")
        ## Create a string variable for reservation id
        self.svCancelResID = StringVar()
        ## Add a filler blank label to create more space
        Label(self.cancelResWin, text=" ").grid(row=0, column=0)
        ## Create a label and entry box for reservation id
        Label(self.cancelResWin, text="Reservation ID").grid(row=1,column=0)
        resIDEntry = Entry(self.cancelResWin, text=self.svCancelResID, width=20)
        resIDEntry.grid(row=1, column=1)
        ## Create search button
        searchButton = Button(self.cancelResWin, text="Search", command=self.searchReservationIDCancel)
        searchButton.grid(row=1, column=2)
        ## Create home button
        homeButton = Button(self.cancelResWin, text="Return Home", command=self.cancelResSearchToHome)
        homeButton.grid(row=2, column=2)
        ## Remaining items on update screen will be created by the method called by the search button

    def viewReviewWin(self):
        ## Create the "View Review" window
        self.viewRevWin = Toplevel(self.loginWin)
        self.viewRevWin.title("View Review")
        ## Create a string variable for hotel location
        self.svViewHotelLoc = StringVar()
        ## Add a filler blank label to create more space
        Label(self.viewRevWin, text=" ").grid(row=0, column=0)
        ## Create label and drop down menu for hotel location
        Label(self.viewRevWin, text="Hotel Location").grid(row=1, column=0)
        hotelLocDrop = OptionMenu(self.viewRevWin, self.svViewHotelLoc, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami") 
        hotelLocDrop.grid(row=1,column=1)
        checkReviewsButton = Button(self.viewRevWin, text="Check Reviews", command=self.checkReviews)
        checkReviewsButton.grid(row=2,column=2)
        ## Add a filler blank label to create more space
        Label(self.viewRevWin, text=" ").grid(row=3, column=0)
        ## Add a home button
        homeButton = Button(self.viewRevWin, text="Return Home", command=self.viewReviewWinToHome)
        homeButton.grid(row=0, column=2)
        ## method called upon button click will create the labels to display reviews info

    def viewReviewWinToHome(self):
        self.goToHome(self.viewRevWin)

    def provideReviewWin(self):
        ## Create the "Give Review" window
        self.giveReviewWin = Toplevel(self.loginWin)
        self.giveReviewWin.title("Give Review")
        ## Create string variables for location, rating, and comment
        self.svHotelLoc = StringVar()
        self.svRatingGive = StringVar()
        self.svCommentGive = StringVar()
        ## Add a filler blank label to create more space
        Label(self.giveReviewWin, text=" ").grid(row=0, column=0)
        ## Create labels, drop down menus, and entry boxes
        Label(self.giveReviewWin, text="Hotel Location").grid(row=1, column=0, sticky=W)
        hotelLocDrop = OptionMenu(self.giveReviewWin, self.svHotelLoc,"Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        hotelLocDrop.grid(row=1, column=1)
        ## Add a filler blank label to create more space
        Label(self.giveReviewWin, text=" ").grid(row=2, column=0)
        Label(self.giveReviewWin, text="Rating").grid(row=3, column=0, sticky=W)
        ratingDrop = OptionMenu(self.giveReviewWin, self.svRatingGive,"Excellent", "Good", "Bad", "Very Bad", "Neutral")
        ratingDrop.grid(row=3, column=1)
        ## Add a filler blank label to create more space
        Label(self.giveReviewWin, text=" ").grid(row=4, column=0)
        Label(self.giveReviewWin, text="Comment").grid(row=5, column=0, sticky=W)
        commentEntry = Entry(self.giveReviewWin, text=self.svCommentGive, width=30)
        commentEntry.grid(row=5, column=1)
        ## Add a filler blank label to create more space
        Label(self.giveReviewWin, text=" ").grid(row=6, column=0)
        ## Add submit button
        submitButton = Button(self.giveReviewWin, text="Submit", command=self.submitReview)
        submitButton.grid(row=7,column=2)
        ## Add a home button
        homeButton = Button(self.giveReviewWin, text="Return Home", command=self.giveReviewWinToHome)
        homeButton.grid(row=7, column=0)

    def giveReviewWinToHome(self):
        self.goToHome(self.giveReviewWin)

    def reservationReportWin(self):
        ## Create the "Reservation Report" window
        self.resReportWin = Toplevel(self.loginWin)
        self.resReportWin.title("Reservation Report")
        ## Create a string varaible for the month
        self.svResMonth = StringVar()
        ## Add a filler blank label to create more space
        Label(self.resReportWin, text=" ").grid(row=0, column=0)
        ## Create a label and drop down menu to select month
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        Label(self.resReportWin, text="Please select a month:").grid(row=1, column=0)
        monthDrop = OptionMenu(self.resReportWin, self.svResMonth, *monthsList)
        monthDrop.grid(row=1, column=1)
        ## Create a button to update the report
        updateButton = Button(self.resReportWin, text="Compile Report", command=self.createResReport)
        updateButton.grid(row=1, column=2)
        ## Add a filler blank label to create more space
        Label(self.resReportWin, text="       ").grid(row=1, column=3)
        ## Create a button to return to choose functionality window
        homeButton = Button(self.resReportWin, text="Return to Home Screen", command=self.ResReportHome)
        homeButton.grid(row=1, column=4)

    def ResReportHome(self):
        self.goToHome(self.resReportWin)

    def createResReport(self):
        ## check if month is empty
        dataList = [self.svResMonth.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Create a dictionary to lookup month number from month name
        monthsDict = {"January": "01","February": "02","March": "03","April": "04","May": "05","June": "06",
                      "July": "07","August": "08","September": "09","October": "10","November": "11","December": "12"}
        monthNum = monthsDict[self.svResMonth.get()]

        ## Create a dictionary to aid in placing reservation data on the window
        locationRowDict = {"Atlanta": 0,"Charlotte": 1,"Miami": 2,"Orlando": 3,"Savannah": 4}

        ## run query to get data
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Month(Reservation.End_Date) AS Month, Location, COUNT(*) AS Total_Res
            FROM Reservation
            NATURAL JOIN Room_Reservation
            WHERE Is_Cancelled=0 AND Month(Reservation.End_Date)=(%s)
            GROUP BY Month, Location'''
        cursor.execute(sql,int(monthNum))
        self.resultResReport = cursor.fetchall()
        cursor.close()
        db.close()

        ## Create list of locations
        locationsList = ["Atlanta","Charlotte","Miami","Orlando","Savannah"]

        ## determine which locations are not present in the data
        locsPresentList = []
        for each in self.resultResReport:
            locsPresentList.append(each[1])
        locsNotPresentList = list(set(locationsList) - set(locsPresentList))
        
        ## Add a filler blank label to create more space
        Label(self.resReportWin, text=" ").grid(row=2, column=0)
        ## Create Labels for Column Headers
        Label(self.resReportWin, text="Month").grid(row=2, column=0, sticky=W)
        Label(self.resReportWin, text="Location").grid(row=2, column=1, sticky=W)
        Label(self.resReportWin, text="Total number of reservations").grid(row=2, column=2, sticky=W)
        ## Create list of months
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        ## Create labels for the locations
        for i in range(5):
            Label(self.resReportWin, text=locationsList[i]).grid(row=(i + 3),column=1, sticky=W)
        ## Create labels for the number of reservations
        for i in range(len(self.resultResReport)):
            rowNumAdd = locationRowDict[self.resultResReport[i][1]]
            Label(self.resReportWin, text=self.resultResReport[i][2]).grid(row=(3+rowNumAdd),column=2, sticky=W)
        if len(self.resultResReport) < 5:
            for location in locsNotPresentList:
                rowNumAdd = locationRowDict[location]
                Label(self.resReportWin, text='0').grid(row=(3+rowNumAdd),column=2, sticky=W)
        ## Create label for the month
        Label(self.resReportWin, text=self.svResMonth.get()).grid(row=5,column=0, sticky=W)

    def popularRoomReportWin(self):
        ## Create the "Popular Room-Category Report" window
        self.popRoomReportWin = Toplevel(self.loginWin)
        self.popRoomReportWin.title("Popular Room-Category Report")
        ## Create a string varaible for the month
        self.svRoomMonth = StringVar()
        ## Add a filler blank label to create more space
        Label(self.popRoomReportWin, text=" ").grid(row=0, column=0)
        ## Create a label and drop down menu to select month
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        Label(self.popRoomReportWin, text="Please select a month:").grid(row=1, column=0)
        monthDrop = OptionMenu(self.popRoomReportWin, self.svRoomMonth, *monthsList)
        monthDrop.grid(row=1, column=1)
        ## Create a button to update the report
        updateButton = Button(self.popRoomReportWin, text="Compile Report", command=self.createRoomReport)
        updateButton.grid(row=1, column=2)
        ## Add a filler blank label to create more space
        Label(self.popRoomReportWin, text="       ").grid(row=1, column=3)
        ## Create a button to return to choose functionality window
        homeButton = Button(self.popRoomReportWin, text="Return to Home Screen", command=self.RoomReportHome)
        homeButton.grid(row=1, column=4)

    def RoomReportHome(self):
        self.goToHome(self.popRoomReportWin)

    def createRoomReport(self):
        ## check if month is empty
        dataList = [self.svRoomMonth.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Create a dictionary to lookup month number from month name
        monthsDict = {"January": "01","February": "02","March": "03","April": "04","May": "05","June": "06",
                      "July": "07","August": "08","September": "09","October": "10","November": "11","December": "12"}
        monthNum = monthsDict[self.svRoomMonth.get()]

        ## Create a dictionary to aid in placing reservation data on the window
        locationRowDict = {"Atlanta": 0,"Charlotte": 1,"Miami": 2,"Orlando": 3,"Savannah": 4}

        ## run query to get data
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Month,Room_Category,Location,MAX(NumReserved)
            FROM(
            SELECT MONTH(Reservation.End_Date) AS Month,Room_Category,Location,Count(*) AS NumReserved
            FROM Reservation
            NATURAL JOIN Room_Reservation
            NATURAL JOIN Room
            AS joined
            WHERE Is_Cancelled=0 AND Month(Reservation.End_Date)=(%s)
            Group BY Month,Location,Room_Category
            ) joined
            Group BY Month,Location
            '''
        cursor.execute(sql,int(monthNum))
        self.resultPopReport = cursor.fetchall()

        ## Create list of locations
        locationsList = ["Atlanta","Charlotte","Miami","Orlando","Savannah"]

        ## determine which locations are not present in the data
        locsPresentList = []
        for each in self.resultPopReport:
            locsPresentList.append(each[2])
        locsNotPresentList = list(set(locationsList) - set(locsPresentList))
        
        ## Add a filler blank label to create more space
        Label(self.popRoomReportWin, text=" ").grid(row=0, column=0)
        ## Create Labels for Column Headers
        Label(self.popRoomReportWin, text="Month").grid(row=2, column=0, sticky=W)
        Label(self.popRoomReportWin, text="Location").grid(row=2, column=1, sticky=W)
        Label(self.popRoomReportWin, text="Top room-category").grid(row=2, column=2, sticky=W)
        Label(self.popRoomReportWin, text="Total reservations for category").grid(row=2, column=3, sticky=W)
        ## Create list of months
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        ## Create labels for the locations
        for i in range(5):
            Label(self.popRoomReportWin, text=locationsList[i]).grid(row=(i + 3),column=1, sticky=W)
        ## Create labels for the top room-category and total number of reservations for room category
        for i in range(len(self.resultPopReport)):
            rowNumAdd = locationRowDict[self.resultPopReport[i][2]]
            Label(self.popRoomReportWin, text=self.resultPopReport[i][1]).grid(row=(3+rowNumAdd),column=2, sticky=W)
            Label(self.popRoomReportWin, text=self.resultPopReport[i][3]).grid(row=(3+rowNumAdd),column=3, sticky=W)
            if len(self.resultPopReport) < 5:
                for location in locsNotPresentList:
                    rowNumAdd = locationRowDict[location]
                    Label(self.popRoomReportWin, text='').grid(row=(3+rowNumAdd),column=2, sticky=W)
                    Label(self.popRoomReportWin, text='').grid(row=(3+rowNumAdd),column=3, sticky=W)
        ## Create labels for the months
        Label(self.popRoomReportWin, text=self.svRoomMonth.get()).grid(row=5,column=0, sticky=W)
            
    def revenueReportWin(self):
        ## Create the "Revenue Report" window
        self.revReportWin = Toplevel(self.loginWin)
        self.revReportWin.title("Revenue Report")
        ## Create a string varaible for the month
        self.svRevMonth = StringVar()
        ## Add a filler blank label to create more space
        Label(self.revReportWin, text=" ").grid(row=0, column=0)
        ## Create a label and drop down menu to select month
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        Label(self.revReportWin, text="Please select a month:").grid(row=1, column=0)
        monthDrop = OptionMenu(self.revReportWin, self.svRevMonth, *monthsList)
        monthDrop.grid(row=1, column=1)
        ## Create a button to update the report
        updateButton = Button(self.revReportWin, text="Compile Report", command=self.createRevReport)
        updateButton.grid(row=1, column=2)
        ## Add a filler blank label to create more space
        Label(self.revReportWin, text="       ").grid(row=1, column=3)
        ## Create a button to return to choose functionality window
        homeButton = Button(self.revReportWin, text="Return to Home Screen", command=self.RevReportHome)
        homeButton.grid(row=1, column=4)

    def RevReportHome(self):
        self.goToHome(self.revReportWin)

    def createRevReport(self):
        ## check if month is empty
        dataList = [self.svRevMonth.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Create a dictionary to lookup month number from month name
        monthsDict = {"January": "01","February": "02","March": "03","April": "04","May": "05","June": "06",
                      "July": "07","August": "08","September": "09","October": "10","November": "11","December": "12"}
        monthNum = monthsDict[self.svRevMonth.get()]

        ## Create a dictionary to aid in placing reservation data on the window
        locationRowDict = {"Atlanta": 0,"Charlotte": 1,"Miami": 2,"Orlando": 3,"Savannah": 4}

        ## run query to get data
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT MONTH(Reservation.End_Date) AS Month, Location, SUM(Total_Cost) AS Total_Revenue
                FROM Reservation
                NATURAL JOIN Room_Reservation
                WHERE Month(Reservation.End_Date)=(%s)
                GROUP BY Month, Location
            '''
        cursor.execute(sql,int(monthNum))
        self.resultRevReport = cursor.fetchall()

        ## Create list of locations
        locationsList = ["Atlanta","Charlotte","Miami","Orlando","Savannah"]

        ## determine which locations are not present in the data
        locsPresentList = []
        for each in self.resultRevReport:
            locsPresentList.append(each[1])
        locsNotPresentList = list(set(locationsList) - set(locsPresentList))
        
        ## Add a filler blank label to create more space
        Label(self.revReportWin, text=" ").grid(row=0, column=0)
        ## Create Labels for Column Headers
        Label(self.revReportWin, text="Month").grid(row=2, column=0, sticky=W)
        Label(self.revReportWin, text="Location").grid(row=2, column=1, sticky=W)
        Label(self.revReportWin, text="Total revenue").grid(row=2, column=2, sticky=W)
        ## Create list of months
        monthsList = ["January","February","March","April","May","June","July","August",
                      "September","October","November","December"]
        ## Create labels for the locations
        for i in range(5):
                Label(self.revReportWin, text=locationsList[i]).grid(row=(i + 3),column=1, sticky=W)
        ## Create labels for the number of reservations
        for i in range(len(self.resultRevReport)):
            rowNumAdd = locationRowDict[self.resultRevReport[i][1]]
            Label(self.revReportWin, text=self.resultRevReport[i][2]).grid(row=(3+rowNumAdd),column=2, sticky=W)
        if len(self.resultRevReport) < 5:
            for location in locsNotPresentList:
                rowNumAdd = locationRowDict[location]
                Label(self.revReportWin, text='0.00').grid(row=(3+rowNumAdd),column=2, sticky=W)
        ## Create labels for the months
        Label(self.revReportWin, text=self.svRevMonth.get()).grid(row=5,column=0, sticky=W)


    ## Control Flow methods
        
    def toRegisterWin(self):
        self.loginWin.withdraw()
        self.registrationWin.deiconify()

    def login(self):
        ## Check database to see if credentials are valid
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT COUNT(*) FROM Customer WHERE Username = (%s) AND password = (%s)'''
        cursor.execute(sql, (self.svUsername.get(), self.svPassword.get()))
        result = cursor.fetchone()

        ## If result = 1, the username/password combination was found
        if result == (1,):
            ## indicate that user is a customer
            self.isCustomer = 1
            cursor.close()
            db.close()
            messagebox.showinfo('Login Succeeded.', 'Welcome!')
            ## send user to choose funtionality page
            self.loginWin.withdraw()
            self.chooseFuntionWin()
        else:
            ## run query on Manager table
            sql = '''SELECT COUNT(*) FROM Management WHERE Username = (%s) AND password = (%s)'''
            cursor.execute(sql, (self.svUsername.get(), self.svPassword.get()))
            result = cursor.fetchone()
            cursor.close()
            db.close()
            if result == (1,):
                messagebox.showinfo('Login Succeeded.', 'Welcome!')
                ## indicate that user is a manager
                self.isCustomer = 0
                ## send user to choose funtionality page
                self.loginWin.withdraw()
                self.chooseFuntionWin()
            else:
                messagebox.showerror('Login Failed.', 'Check username and password.')
            
        

    def register(self):
        ## check if username, password, or email are empty
        dataList = [self.svUsernameCreate.get(), self.svPasswordCreate.get(), self.svEmail.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## check if confirm password = password
        if self.svPasswordCreate.get() != self.svConfirmPassword.get():
            messagebox.showerror('Registration Failed.', 'What you entered for password and confirm '+
                                 'password do not match.')
            return None

        ## check if email is a valid email address (syntax-wise)
        rgx = r'[^@\s]+@[^@\s]+\.[^@\s]+'
        valid = re.match(rgx, self.svEmail.get())
        if valid == None:
            messagebox.showerror('Registration Failed.', 'Please enter a valid email address.')
            return None
        
        ## checks for validity/availability of credentials
        db = self.connect()
        cursor = db.cursor()

        sql = '''SELECT COUNT(*) FROM Customer WHERE Username = (%s)'''
        cursor.execute(sql, (self.svUsernameCreate.get()))
        result = cursor.fetchone()
        if result != (0,):
            messagebox.showerror('Registration Failed.', 'That username is already taken. '+
                                 'Please choose another username.')
            return None

        ## check availability of email
        sql = '''SELECT COUNT(*) FROM Customer WHERE Email = (%s)'''
        cursor.execute(sql, (self.svEmail.get()))
        result = cursor.fetchone()
        if result != (0,):
            messagebox.showerror('Registration Failed.', 'That email is already taken. '+
                                 'Please choose another email.')
        
        ## If all checks pass, register the user
        sql = '''INSERT INTO Customer VALUES (%s,%s,%s)'''
        cursor.execute(sql, ("C"+self.svUsernameCreate.get(), self.svPasswordCreate.get(), self.svEmail.get()))
        cursor.close()
        db.commit()
        db.close()

        messagebox.showinfo('Registration Succeeded.', 'You will be taken to the login screen '+
                            'where you will be able to login with your new credentials. \n\n Username: C'+self.svUsernameCreate.get()+
                            '\n Password: '+self.svPasswordCreate.get())
        
        ## send customer to login screen
        self.registrationWin.withdraw()
        self.loginWin.deiconify()

    def makeNewReservation(self):
        self.makeResWin.destroy()
        self.makeReservationWin()
        self.makeResWin.withdraw()

        self.searchRmWin.destroy()
        self.searchRoomsWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.searchRmWin.deiconify()

    def updateReservation(self):
        self.updateResWin.destroy()
        self.updateReservationWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.updateResWin.deiconify()
    
    def cancelReservation(self):
        self.cancelResWin.destroy()
        self.cancelReservationWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.cancelResWin.deiconify()
        
    def giveFeedback(self):
        self.giveReviewWin.destroy()
        self.provideReviewWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.giveReviewWin.deiconify()

    def viewFeedback(self):
        self.viewRevWin.destroy()
        self.viewReviewWin()
    
        self.chooseFunctionalityWin.withdraw()
        self.viewRevWin.deiconify()

    def viewResReport(self):
        self.resReportWin.destroy()
        self.reservationReportWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.resReportWin.deiconify()

    def viewPopRoomReport(self):
        self.popRoomReportWin.destroy()
        self.popularRoomReportWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.popRoomReportWin.deiconify()

    def viewRevReport(self):
        self.revReportWin.destroy()
        self.revenueReportWin()
        
        self.chooseFunctionalityWin.withdraw()
        self.revReportWin.deiconify()

    def searchRooms(self):
        ## check if location, start date, or end date are empty
        dataList = [self.svLocation.get(), self.svStartDate.get(), self.svEndDate.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## check if dates are in the proper form MM/DD/YYYY
        rgx = r'[0|1]{1}[\d ^0]{1}/[0-3]{1}[\d ^0]{1}/[\d]{4}\Z'
        for date in [self.svStartDate.get(), self.svEndDate.get()]:
            valid = re.match(rgx, date)
            if valid == None:
                messagebox.showerror('Search Failed.', 'Please enter a valid date MM/DD/YYYY.')
                return None

        ## check if start date before end date
        sDateYear = int(self.svStartDate.get()[6:10])
        sDateMonth = int(self.svStartDate.get()[0:2])
        sDateDay = int(self.svStartDate.get()[3:5])
        sDateList = [sDateYear, sDateMonth, sDateDay]
        eDateYear = int(self.svEndDate.get()[6:10])
        eDateMonth = int(self.svEndDate.get()[0:2])
        eDateDay = int(self.svEndDate.get()[3:5])
        eDateList = [eDateYear, eDateMonth, eDateDay]
        if sDateList >= eDateList:
            messagebox.showerror('Search Failed.', 'Start date cannot be before end date.')
            return None

        self.finalSDate = self.dateFormatting(self.svStartDate.get())
        self.finalEDate = self.dateFormatting(self.svEndDate.get())

        ## check if start date is before the current date
        currentDate = self.getCurrentDate()
        daysBetween = self.resLength(currentDate, self.svStartDate.get()) - 1
        if daysBetween <= 0:
            messagebox.showerror('Search Failed', 'The start date cannot be today or before today.')
            return None

        ## query database for room availability
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Room_Num, Room_Category, Num_People, Cost_Per_Day, Cost_Extra_Bed_Per_Day
                 FROM Room WHERE Location = %s AND NOT EXISTS(SELECT *
                 FROM Room_Reservation NATURAL JOIN Reservation WHERE Room.Room_Num=Room_Num 
                 AND Room.Location=Location AND Start_Date <= %s AND End_Date >= %s
                 AND Is_Cancelled=0)'''
        cursor.execute(sql, (self.svLocation.get(), self.finalEDate, self.finalSDate))

        ## Create list for the data
        ## It is of the form [[RmNum1,RoomCat1,NumPers1,Cost1,CostExtra1],...,[[RmNumN,RoomCatN,NumPersN,CostN,CostExtraN]]
        self.roomsList = cursor.fetchall()

        ## Create a list of string variables to correspond with the yes/no for selection of a room
        self.selectionList = []
        for i in range(len(self.roomsList)):
            self.selectionList.append(StringVar())
            self.selectionList[i].set("No")
        ## Create labels to display the data
        for i in range(len(self.roomsList)):
            for itemNum in range(5):
                Label(self.makeResWin, text=self.roomsList[i][itemNum]).grid(row=2+i, column=itemNum, sticky=W)
        ## Create option menus for selecting rooms
        for i in range(len(self.roomsList)):
            selectOptionMenu = OptionMenu(self.makeResWin, self.selectionList[i], "Yes", "No")
            selectOptionMenu.grid(row=2+i, column=5, sticky=W)
        ## Add filler blank labels to create more space
        Label(self.makeResWin, text=" ").grid(row=len(self.roomsList)+2, column=0)       
        ## Create check details button
        checkDetailsButton = Button(self.makeResWin, text="Check Details", command=self.resCheckDetails)
        checkDetailsButton.grid(row=len(self.roomsList)+3,column=5)
        ## Add filler blank labels to create more space
        Label(self.makeResWin, text=" ").grid(row=len(self.roomsList)+4, column=0)
        ## Check detail items will be created by the method associated with the check details button
            
        self.searchRmWin.withdraw()
        self.makeResWin.deiconify()

    def saveNewCard(self):
        ## check if name, card number, card exp date, or cvv are empty
        dataList = [self.svNameonCard.get(), self.svCardNumAdd.get(), self.svCardExpDate.get(), self.svCardCVV.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## check if name is of a valid form
        rgx = r'[a-zA-Z ]+\Z'
        valid = re.match(rgx, self.svNameonCard.get())
        if valid == None:
            messagebox.showerror('Save Card Failed.', 'Name should include only English letters.')
            return None

        ## check if card number is of a valid form (16 digits)
        rgx = r'[\d]{16}\Z'
        valid = re.match(rgx, self.svCardNumAdd.get())
        if valid == None:
            messagebox.showerror('Save Card Failed.', 'Card number should be 16 digits.')
            return None

        ## check if expiration date is of a valid form (MM/YYYY)
        rgx = r'[0|1]{1}[\d ^0]{1}/[\d]{4}\Z'
        valid = re.match(rgx, self.svCardExpDate.get())
        if valid == None:
            messagebox.showerror('Save Card Failed.', 'Please enter a valid date MM/YYYY.')
            return None

        ## check if expiration date is in the past
        startDate = self.getCurrentDate()
        endDate = self.svCardExpDate.get()
        numYears = int(endDate[3:7]) - int(startDate[6:10]) ## years difference
        sDay = 0 ## day of the year of reservation start
        monthNum = int(startDate[0:2])
        for i in range(1,monthNum): ## add up days from months prior to start month
            sDay = sDay + self.monthsDaysDict[i]

        eDay = 0 ## day of the year of reservation end
        monthNum = int(endDate[0:2])
        for i in range(1,monthNum): ## add up days from months prior to end month
            eDay = eDay + self.monthsDaysDict[i]

        length = eDay - sDay + numYears*365

        if length < 0:
            messagebox.showerror('Save Card Failed', 'The expiration date cannot be before the current month.')
            return None

        ## check if cvv is of a valid form (3 digits)
        rgx = r'[\d]{3}\Z'
        valid = re.match(rgx, self.svCardCVV.get())
        if valid == None:
            messagebox.showerror('Save Card Failed.', 'CVV code should be 3 digits.')
            return None

        ## check if card number is already taken in the database
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT COUNT(*) FROM Payment_Info WHERE Card_Num = %s'''
        cursor.execute(sql, (self.svCardNumAdd.get()))
        result = cursor.fetchone()
        cursor.close()
        db.close()

        if result != (0,):
            messagebox.showerror('Card Not Added', 'That card number is already taken.')
            return None

        ## insert new card info into database
        db = self.connect()
        cursor = db.cursor()
        sql = '''INSERT INTO Payment_Info VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(sql, (self.svCardNumAdd.get(), self.svCardCVV.get(),
                            self.svCardExpDate.get(), self.svNameonCard.get(),
                            self.svUsername.get()))
        cursor.close()
        db.commit()
        db.close()

        ## Update card selection list on make reservation window to include added card
        self.cardNumList.append(self.svCardNumAdd.get())
        self.resCheckDetails()

        messagebox.showinfo('Card Successfully Added', 'You will be taken back to the reservation window')
        
        self.paymentInfoWin.withdraw()
        self.makeResWin.deiconify()

    def deleteCard(self):
        ## check if card number is empty
        dataList = [self.svCardNumDelete.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## check if card is currently being used in a reservation
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT COUNT(*) FROM Reservation WHERE Card_Num = %s'''
        cursor.execute(sql, (self.svCardNumDelete.get()))
        result = cursor.fetchone()
        cursor.close()
        db.close()

        if result != (0,):
            messagebox.showerror('Card Delete Failed', 'That card is currently being used in a reservation')
            return None
        
        ## Delete the selected card
        db = self.connect()
        cursor = db.cursor()
        sql = '''DELETE FROM Payment_Info WHERE Card_Num = %s'''
        cursor.execute(sql, (self.svCardNumDelete.get()))
        cursor.close()
        db.commit()
        db.close()

        ## Remove card from display list on make reservation window
        self.cardNumList.remove(self.svCardNumDelete.get())

        messagebox.showinfo('Card Deletion.', 'Card successfully deleted')

    def submitReview(self):
        ## Check if any fields are empty
        dataList = [self.svCommentGive.get(), self.svRatingGive.get(),
                    self.svHotelLoc.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Insert customer review data into database
        db = self.connect()
        cursor = db.cursor()
        sql = '''INSERT INTO Hotel_Review (Comment, Rating, Location, Username) VALUES (%s,%s,%s,%s)'''
        cursor.execute(sql, (self.svCommentGive.get(), self.svRatingGive.get(),
                             self.svHotelLoc.get(), self.svUsername.get()))
        cursor.close()
        db.commit()
        db.close()

        messagebox.showinfo('Success', 'Review submited successfully. Thank you for your feedback.')
        
        self.goToHome(self.giveReviewWin)

    def checkReviews(self):
        ## Check if location menu is empty
        dataList = [self.svViewHotelLoc.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Create column headers for rating and comment
        Label(self.viewRevWin, text="Rating").grid(row=4, column=0, sticky=W)
        Label(self.viewRevWin, text="Comment").grid(row=4, column=1)
        ## Create list to store reviews info from database
        reviewsList = []

        ## Populate reviews list with data
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Rating,Comment FROM Hotel_Review WHERE Location = %s'''
        cursor.execute(sql, (self.svViewHotelLoc.get()))
        result = cursor.fetchall()
        for review in result:
            reviewsList.append(review)
        
        ## Create labels to display review data
        for row in range(len(reviewsList)):
            gridRow = row + 5
            Label(self.viewRevWin, text=reviewsList[row][0]).grid(row=gridRow,column=0, sticky=W)
            Label(self.viewRevWin, text=reviewsList[row][1]).grid(row=gridRow,column=1, sticky=W)
        ## Create a button to return to choose functionality window
        homeButton = Button(self.viewRevWin, text="Return to Home Screen", command=self.homeFromViewReviews)
        homeButton.grid(row=gridRow+1,column=2)

    def homeFromViewReviews(self):
        self.goToHome(self.viewRevWin)

    def resCheckDetails(self):
        ## Create Labels for Column Headers
        Label(self.makeResWin, text="Room number").grid(row=len(self.roomsList)+5, column=0, sticky=W)
        Label(self.makeResWin, text="Room category").grid(row=len(self.roomsList)+5, column=1, sticky=W)
        Label(self.makeResWin, text="Number persons allowed").grid(row=len(self.roomsList)+5, column=2, sticky=W)
        Label(self.makeResWin, text="Cost per day").grid(row=len(self.roomsList)+5, column=3, sticky=W)
        Label(self.makeResWin, text="Cost of extra bed per day").grid(row=len(self.roomsList)+5, column=4, sticky=W)
        Label(self.makeResWin, text="Extra bed").grid(row=len(self.roomsList)+5, column=5, sticky=W)
        ## Check which rooms were selected by the user and display only those rooms
        ## Also compile cost information from selected rooms
        self.roomsCostList = []  ## of the form [(Rm1CostPerDay,Rm1EBCostPerDay),...]
        self.selectedRoomNumsList = [] ## for use in inserting reservation information into database
        rowCounter = len(self.roomsList)+6
        roomsCounter = 0
        for i in range(len(self.selectionList)):
            if self.selectionList[i].get() == "Yes":
                roomsCounter = roomsCounter + 1
                for itemNum in range(5):
                    Label(self.makeResWin, text=self.roomsList[i][itemNum]).grid(row=rowCounter, column=itemNum, sticky=W)
                rowCounter = rowCounter + 1
                self.roomsCostList.append( (float(self.roomsList[i][3]), float(self.roomsList[i][4])) )
                self.selectedRoomNumsList.append( int(self.roomsList[i][0]) )
        ## Create a list of string variables to correspond with the yes/no for selection of a room
        self.extraBedSelectionList = []
        for i in range(roomsCounter):
            self.extraBedSelectionList.append(StringVar())
            self.extraBedSelectionList[i].set("No")
        ## Create option menus for selecting extra bed
        rowCounter = len(self.roomsList)+6
        for i in range(roomsCounter):
            selectExtraBedOptionMenu = OptionMenu(self.makeResWin, self.extraBedSelectionList[i], "Yes", "No",
                                                  command=self.updateResCost)
            selectExtraBedOptionMenu.grid(row=rowCounter, column=5, sticky=W)
            rowCounter = rowCounter + 1
        ## Add filler blank labels to create more space
        Label(self.makeResWin, text=" ").grid(row=rowCounter+1, column=0)
        ## Create string variables for dates, cost, and card number
        self.svSDate = StringVar()
        self.svEDate = StringVar()
        self.svTotalCost = StringVar()
        self.svCardNum = StringVar()
        ## Set date string variables
        self.svSDate.set( self.svStartDate.get() )
        self.svEDate.set( self.svEndDate.get() )

        ## Calculate length (in days) of the reservation using helper function
        self.numDays = self.resLength( self.svSDate.get(), self.svEDate.get() )

        ## Calculate initial total cost before selecting any extra beds
        self.updateResCost()
        
        ## Set date string variables
        self.svSDate.set(self.svStartDate.get())
        self.svEDate.set(self.svEndDate.get())
        ## Create labels and entry boxes for dates and cost
        Label(self.makeResWin, text="Start Date").grid(row=rowCounter+2, column=0)
        sDateEntry = Entry(self.makeResWin, text=self.svSDate, state="readonly")
        sDateEntry.grid(row=rowCounter+2, column=1)
        Label(self.makeResWin, text="End Date").grid(row=rowCounter+2, column=3)
        eDateEntry = Entry(self.makeResWin, text=self.svEDate, state="readonly")
        eDateEntry.grid(row=rowCounter+2, column=4)
        Label(self.makeResWin, text="Total Cost").grid(row=rowCounter+3, column=0)
        totalCostEntry = Entry(self.makeResWin, text=self.svTotalCost, state="readonly")
        totalCostEntry.grid(row=rowCounter+3, column=1)
        ## Create label and option menu for card number
        Label(self.makeResWin, text="Use Card").grid(row=rowCounter+4, column=1)
        self.cardNumList = [] 

        ## Populate card list with customer's card data
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Card_Num FROM Payment_Info WHERE Username = (%s)'''
        cursor.execute(sql, (self.svUsername.get()))
        result = cursor.fetchall()
        for num in result:
            self.cardNumList.append(str(num[0]))
            
        if len(self.cardNumList) != 0:
            useCardDrop = OptionMenu(self.makeResWin, self.svCardNum, *self.cardNumList)
            useCardDrop.grid(row=rowCounter+4, column=2)
        ## Create add card and submit buttons
        addCardButton = Button(self.makeResWin, text="Add a New Card", command=self.resAddCard)
        addCardButton.grid(row=rowCounter+4, column=3)
        submitButton = Button(self.makeResWin, text="Submit", command=self.submitReservation)
        submitButton.grid(row=rowCounter+5, column=5)

        ## Create home buttton
        homeButton = Button(self.makeResWin, text="Return Home", command=self.checkResDetailsToHome)
        homeButton.grid(row=rowCounter+5, column=0)

    def checkResDetailsToHome(self):
        self.goToHome(self.makeResWin)

    def updateResCost(self, other=None):
        ## Calculate total cost
        totalCost = 0
        for i in range(len(self.roomsCostList)):
            if self.extraBedSelectionList[i].get() == "Yes":
                totalCost = totalCost + (self.roomsCostList[i][0] + self.roomsCostList[i][1])*self.numDays
            else:
                totalCost = totalCost + (self.roomsCostList[i][0])*self.numDays
                
        ## Set cost string variable
        self.svTotalCost.set("$"+str(totalCost))

    def resAddCard(self):
        self.paymentInfoWin.destroy()
        self.paymentInformationWin()
        
        ##Populate card delete list with customers cards
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Card_Num FROM Payment_Info WHERE Username = (%s)'''
        cursor.execute(sql, (self.svUsername.get()))
        result = cursor.fetchall()
        for num in result:
            self.cardNumDeleteList.append(str(num[0]))

        if len(self.cardNumDeleteList) != 0:
            ## Create option menu
            cardNumDrop = OptionMenu(self.paymentInfoWin, self.svCardNumDelete, *self.cardNumDeleteList)
            cardNumDrop.config(width=30)
            cardNumDrop.grid(row=3, column=4)
            ## Add delete button
            deleteButton = Button(self.paymentInfoWin, text="Delete", command=self.deleteCard)
            deleteButton.grid(row=8, column=4, sticky=W)
        
        self.makeResWin.withdraw()
        self.paymentInfoWin.deiconify()
           
    def submitReservation(self):
        ## check if card number is empty
        dataList = [self.svCardNum.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## Check if user did not select any rooms
        if len(self.roomsCostList) == 0:
            messagebox.showerror('Unable To Submit Reservation', 'You must select at least one room in order to register.')
            self.goToHome(self.makeResWin)
            return None

        ## insert the reservation info into the database
        db = self.connect()
        cursor = db.cursor()
        sqlOne = '''INSERT INTO Reservation (Start_Date, End_Date, Total_Cost, Is_Cancelled, Username, Card_Num)
                    VALUES (%s, %s, %s, 0, %s, %s)'''
        sqlTwo = '''SELECT LAST_INSERT_ID()'''
        cursor.execute(sqlOne, (self.finalSDate, self.finalEDate, float(self.svTotalCost.get().replace('$', '')),
                                self.svUsername.get(), self.svCardNum.get()))
        cursor.execute(sqlTwo)
        result = cursor.fetchone()[0]
        db.commit()
        reservationID = str(result)

        sql = '''INSERT INTO Room_Reservation (Reservation_ID, Room_Num, Location, Has_Extra_Bed)
                 VALUES (%s, %s, %s, %s)'''
        for i in range(len(self.selectedRoomNumsList)):
            roomNum = self.selectedRoomNumsList[i]
            extraBed = self.extraBedSelectionList[i].get()
            if extraBed == "Yes":
                extraBedInsert = 1
            else:
                extraBedInsert = 0
            cursor.execute(sql, (reservationID, roomNum, self.svLocation.get(), extraBedInsert))
            db.commit()

        cursor.close()
        db.close()
        self.svReservID.set(str(reservationID))
            
        self.makeResWin.withdraw()
        self.goToHome(self.makeResWin)
        self.confScreenWin.deiconify()

    def updateResSearch(self):
        ## check if reservation id is empty
        dataList = [self.svUpdateResID.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None
        
        ## Create string variables for the dates
        self.svCSDate = StringVar()
        self.svCEDate = StringVar()
        self.svNSDate = StringVar()
        self.svNEDate = StringVar()

        ## Retrieve data from database
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT * FROM Reservation WHERE Reservation_ID = %s
                 AND Username = %s'''
        cursor.execute(sql, (self.svUpdateResID.get(), self.svUsername.get()))
        reservation = cursor.fetchone()
        cursor.close()
        db.close()

        ## If no reservation found for that user under that Res ID, stop execution and inform user
        if reservation == None:
            messagebox.showerror('Reservation Not Found', 'No reservation was found for you with that ID.')
            return None
        
        ## Set current date string variables according to data from database
        formatSDateCurrent = self.dateFormattingReverse(str(reservation[1]))
        formatEDateCurrent = self.dateFormattingReverse(str(reservation[2]))
        self.svCSDate.set(formatSDateCurrent)
        self.svCEDate.set(formatEDateCurrent)
        ## Add a filler blank label to create more space
        Label(self.updateResWin, text=" ").grid(row=2, column=0)
        ## Create labels and entry boxes for the dates
        Label(self.updateResWin, text="Current Start Date").grid(row=3,column=0)
        csDateEntry = Entry(self.updateResWin, text=self.svCSDate, width=20, state="readonly")
        csDateEntry.grid(row=3, column=1)
        Label(self.updateResWin, text="Current End Date").grid(row=3,column=2)
        ceDateEntry = Entry(self.updateResWin, text=self.svCEDate, width=20, state="readonly")
        ceDateEntry.grid(row=3, column=3)
        Label(self.updateResWin, text="New Start Date").grid(row=4,column=0)
        nsDateEntry = Entry(self.updateResWin, text=self.svNSDate, width=20)
        nsDateEntry.grid(row=4, column=1)
        Label(self.updateResWin, text="New End Date").grid(row=4,column=2)
        neDateEntry = Entry(self.updateResWin, text=self.svNEDate, width=20)
        neDateEntry.grid(row=4, column=3)
        ## Add a filler blank label to create more space
        Label(self.updateResWin, text=" ").grid(row=5, column=0)
        ## Create search availability button
        searchAvailButton = Button(self.updateResWin, text="Search Availability", command=self.searchAvailability)
        searchAvailButton.grid(row=6, column=1)
        ## The remaining items on the update screen will be created by the method for the search availability button

    def updateResSearchToHome(self):
        self.goToHome(self.updateResWin)

    def searchAvailability(self):
        ## check if new start date or new end date are empty
        dataList = [self.svNSDate.get(), self.svNEDate.get()]
        emptyCheck = self.checkIfFieldsEmpty(dataList)
        if emptyCheck == None:
            return None

        ## check if dates are in the proper form MM/DD/YYYY
        rgx = r'[0|1]{1}[\d ^0]{1}/[0-3]{1}[\d ^0]{1}/[\d]{4}\Z'
        for date in [self.svNSDate.get(), self.svNEDate.get()]:
            valid = re.match(rgx, date)
            if valid == None:
                messagebox.showerror('Search Failed.', 'Please enter a valid date MM/DD/YYYY.')
                return None

        ## check if start date before end date
        sDateYear = int(self.svNSDate.get()[6:10])
        sDateMonth = int(self.svNSDate.get()[0:2])
        sDateDay = int(self.svNSDate.get()[3:5])
        sDateList = [sDateYear, sDateMonth, sDateDay]
        eDateYear = int(self.svNEDate.get()[6:10])
        eDateMonth = int(self.svNEDate.get()[0:2])
        eDateDay = int(self.svNEDate.get()[3:5])
        eDateList = [eDateYear, eDateMonth, eDateDay]
        if sDateList >= eDateList:
            messagebox.showerror('Search Failed.', 'Start date cannot be before end date.')
            return None

        ## check if new dates are the same as the current dates
        if self.svCSDate.get() == self.svNSDate.get():
            if self.svCEDate.get() == self.svNEDate.get():
                messagebox.showerror('Search Failed.', 'The new start date, new end date, or both must be different than the original dates.')
                return None

        ## check if new start date is before the current date
        currentDate = self.getCurrentDate()
        daysBetween = self.resLength(currentDate, self.svNSDate.get()) - 1
        
        if daysBetween <= 0:
            messagebox.showerror('Search Failed', 'The new start date cannot be today or before today.')
            return None

        ## check if current start date is within three days after today
        daysBetween = self.resLength(currentDate, self.svCSDate.get()) - 1
        if daysBetween <= 3:
            messagebox.showerror('Search Failed', 'Reservations starting within three days of today cannot be updated .')
            return None                         

        ## Add a filler blank label to create more space
        Label(self.updateResWin, text=" ").grid(row=7, column=0)

        ## Convert new dates into SQL format
        self.formatSDate = self.dateFormatting(self.svNSDate.get())
        self.formatEDate = self.dateFormatting(self.svNEDate.get())

        ## Query database to determine if rooms are available for the updated dates
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT CASE WHEN EXISTS (SELECT * FROM (SELECT Room_Num, Location
        FROM Room_Reservation NATURAL JOIN Room WHERE Reservation_ID = %s) s
        JOIN (SELECT Room_Num, Location, Start_Date, End_Date FROM Reservation
        NATURAL JOIN Room_Reservation NATURAL JOIN Room WHERE Is_Cancelled=0 AND Reservation_ID != %s) t
        ON s.Room_Num=t.Room_Num AND s.Location=t.Location
        WHERE Start_Date <= %s AND End_Date >= %s)
        THEN 0 ELSE 1 END'''
        cursor.execute(sql, (self.svUpdateResID.get(), self.svUpdateResID.get(), self.formatEDate, self.formatSDate))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        
        ## Conditional to determine if rooms are available for the updated dates
        if result == (1,):
            ## Create a "rooms are available" label
            Label(self.updateResWin, text="Rooms are available. Please confirm details below before submitting.").grid(row=8, column=0, columnspan=3)
            ## Add a filler blank label to create more space
            Label(self.updateResWin, text=" ").grid(row=9, column=0)
            ## Create Labels for Column Headers
            Label(self.updateResWin, text="Room number").grid(row=10, column=0, sticky=W)
            Label(self.updateResWin, text="Room category").grid(row=10, column=1, sticky=W)
            Label(self.updateResWin, text="Number persons allowed").grid(row=10, column=2, sticky=W)
            Label(self.updateResWin, text="Cost per day").grid(row=10, column=3, sticky=W)
            Label(self.updateResWin, text="Cost of extra bed per day").grid(row=10, column=4, sticky=W)
            Label(self.updateResWin, text="Extra bed").grid(row=10, column=5, sticky=W)

            ## Query database to retrieve data about the rooms used in the reservation
            db = self.connect()
            cursor = db.cursor()
            sql = '''SELECT Room_Num, Room_Category, Num_People, Cost_Per_Day,
                     Cost_Extra_Bed_Per_Day, Has_Extra_Bed FROM Reservation
                     NATURAL JOIN Room_Reservation NATURAL JOIN Room
                     WHERE Reservation_ID = %s'''
            cursor.execute(sql, (self.svUpdateResID.get()))
            
            ## Create list for the data
            ## It is of the form [[RmNum1,RoomCat1,NumPers1,Cost1,CostExtra1,ExtraBed1],...,[[RmNumN,RoomCatN,NumPersN,CostN,CostExtraN,ExtraBedN]]
            self.reservationRoomList = cursor.fetchall()
            cursor.close()
            db.close()

            ## Create a list to store cost data for rooms
            self.roomsCostListUpdate = []
            ## Create labels for reservation data from database
            rowCounter = 11
            for i in range(len(self.reservationRoomList)):
                for itemNum in range(5):
                    Label(self.updateResWin, text=self.reservationRoomList[i][itemNum]).grid(row=rowCounter, column=itemNum, sticky=W)
                if self.reservationRoomList[i][5] == "1":
                    Label(self.updateResWin, text="Yes").grid(row=rowCounter, column=5, sticky=W)
                else:
                    Label(self.updateResWin, text="No").grid(row=rowCounter, column=5, sticky=W)
                self.roomsCostListUpdate.append( (float(self.reservationRoomList[i][3]),
                                                  float(self.reservationRoomList[i][4])) )
                rowCounter = rowCounter + 1  
            ## Add a filler blank label to create more space
            Label(self.updateResWin, text=" ").grid(row=rowCounter+1, column=0)

            ## Determine length of new reservation
            numDays = self.resLength(self.svNSDate.get(), self.svNEDate.get())
            
            ## Create string variable for updated cost
            self.svUpdatedTotalCost = StringVar()
            ## Set string variable to updated total cost of the reservation
            totalCost = 0
            for i in range(len(self.roomsCostListUpdate)):
                if self.reservationRoomList[i][5] == "Yes":
                    totalCost = totalCost + (self.roomsCostListUpdate[i][0] + self.roomsCostListUpdate[i][1])*numDays
                else:
                    totalCost = totalCost + (self.roomsCostListUpdate[i][0])*numDays

            self.svUpdatedTotalCost.set('$'+str(totalCost))

            ## Create label and entry box for updated cost
            Label(self.updateResWin, text="Updated Total Cost").grid(row=rowCounter+2, column=0, sticky=W)
            updatedCostEntry = Entry(self.updateResWin, text=self.svUpdatedTotalCost, width=20, state="readonly")
            updatedCostEntry.grid(row=rowCounter+2, column=1)
            ## Create a submit button
            submitButton = Button(self.updateResWin, text="Submit", command=self.submitUpdatedReservation)
            submitButton.grid(row=rowCounter+3, column=5)

            ## save reservation id into a variable to prevent user changing it and affecting update
            self.resUpdateResID = self.svUpdateResID.get()
        else:
            messagebox.showerror('Room not available for the new dates', 'Please try again with different dates or make a new reservation.')
            self.goToHome(self.updateResWin)
            return None
            

    def submitUpdatedReservation(self):
        ## Update reservation information in the database
        db = self.connect()
        cursor = db.cursor()
        sql = '''UPDATE Reservation SET Start_Date = %s, End_Date = %s, Total_Cost = %s
                 WHERE Reservation_ID = %s AND Username = %s'''
        cursor.execute(sql, (self.formatSDate, self.formatEDate, float((self.svUpdatedTotalCost.get()).replace('$','')),
                             self.resUpdateResID, self.svUsername.get()))
        db.commit()
        cursor.close()
        db.close()

        messagebox.showinfo('Update Reservation Succeeded', 'You will be taken back to the home screen.')
        
        self.goToHome(self.updateResWin)

    def noUpdateAvailability(self):
        self.goToHome(self.updateResWin)

    def goToHome(self, winName):
        winName.withdraw()
        self.chooseFunctionalityWin.deiconify()
        

    def searchReservationIDCancel(self):
        ## Retrieve reservation data from database
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT * FROM Reservation WHERE Reservation_ID = %s
                 AND Username = %s'''
        cursor.execute(sql, (self.svCancelResID.get(), self.svUsername.get()))
        reservation = cursor.fetchone()
        cursor.close()
        db.close()

        ## If no reservation found for that user under that Res ID, stop execution and inform user
        if reservation == None:
            messagebox.showerror('Reservation Not Found', 'No reservation was found for you with that ID.')
            return None

        ## Retrieve information about rooms associated with reservation from database
        db = self.connect()
        cursor = db.cursor()
        sql = '''SELECT Room_Num, Room_Category, Num_People, Cost_Per_Day,
                 Cost_Extra_Bed_Per_Day, Has_Extra_Bed FROM Reservation
                 NATURAL JOIN Room_Reservation NATURAL JOIN Room
                 WHERE Reservation_ID = %s'''
        cursor.execute(sql, (self.svCancelResID.get()))
        ## Create a list for the reservation data
        ## It is of the form [[RmNum1,RoomCat1,NumPers1,Cost1,CostExtra1,ExtraBed1],...,[[RmNumN,RoomCatN,NumPersN,CostN,CostExtraN,ExtraBedN]]
        self.reservationCancelRoomList = cursor.fetchall()
        cursor.close()
        db.close()

        ## Save reservation ID to a variable to prevent user from affecting the cancel query
        self.cancelResID = self.svCancelResID.get()
        
        ## Add a filler blank label to create more space
        Label(self.cancelResWin, text=" ").grid(row=2, column=0)
        ## Create string variables for the dates
        self.svCancelStartDate = StringVar()
        self.svCancelEndDate = StringVar()
        ## Set current date string variables according to data from database
        formatSDate = self.dateFormattingReverse(str(reservation[1]))
        formatEDate = self.dateFormattingReverse(str(reservation[2]))
        self.svCancelStartDate.set(formatSDate)
        self.svCancelEndDate.set(formatEDate)
        ## Create labels for dates
        ## Create labels and entry boxes for the dates
        Label(self.cancelResWin, text="Current Start Date").grid(row=3,column=0)
        sDateEntry = Entry(self.cancelResWin, text=self.svCancelStartDate, width=20, state="readonly")
        sDateEntry.grid(row=3, column=1)
        Label(self.cancelResWin, text="Current End Date").grid(row=3,column=2)
        eDateEntry = Entry(self.cancelResWin, text=self.svCancelEndDate, width=20, state="readonly")
        eDateEntry.grid(row=3, column=3)
        ## Add a filler blank label to create more space
        Label(self.cancelResWin, text=" ").grid(row=4, column=0)
        ## Create Labels for Column Headers
        Label(self.cancelResWin, text="Room number").grid(row=5, column=0, sticky=W)
        Label(self.cancelResWin, text="Room category").grid(row=5, column=1, sticky=W)
        Label(self.cancelResWin, text="Number persons allowed").grid(row=5, column=2, sticky=W)
        Label(self.cancelResWin, text="Cost per day").grid(row=5, column=3, sticky=W)
        Label(self.cancelResWin, text="Cost of extra bed per day").grid(row=5, column=4, sticky=W)
        Label(self.cancelResWin, text="Extra bed").grid(row=5, column=5, sticky=W)
        ## Create labels for the reservation data from database
        rowCounter = 6
        for i in range(len(self.reservationCancelRoomList)):
            for itemNum in range(5):
                Label(self.cancelResWin, text=self.reservationCancelRoomList[i][itemNum]).grid(row=rowCounter, column=itemNum, sticky=W)
            if self.reservationCancelRoomList[i][5] == "1":
                Label(self.cancelResWin, text="Yes").grid(row=rowCounter, column=5, sticky=W)
            else:
                Label(self.cancelResWin, text="No").grid(row=rowCounter, column=5, sticky=W)
            rowCounter = rowCounter + 1
        ## Add a filler blank label to create more space
        Label(self.cancelResWin, text=" ").grid(row=rowCounter+1, column=0)   
        ## Create labels, entry boxes, and string variables for cost, date, and refund
        self.svTotalCostCancel = StringVar()
        self.svDateOfCancel = StringVar()
        self.svRefundAmount = StringVar()
        
        Label(self.cancelResWin, text="Total cost of reservation").grid(row=rowCounter+2, column=0, sticky=W)
        costEntry = Entry(self.cancelResWin, text=self.svTotalCostCancel, width=20, state="readonly")
        costEntry.grid(row=rowCounter+2, column=1)
        Label(self.cancelResWin, text="Date of cancellation").grid(row=rowCounter+3, column=0, sticky=W)
        dateEntry = Entry(self.cancelResWin, text=self.svDateOfCancel, width=20, state="readonly")
        dateEntry.grid(row=rowCounter+3, column=1)
        Label(self.cancelResWin, text="Amount to be refunded").grid(row=rowCounter+4, column=0, sticky=W)
        refundEntry = Entry(self.cancelResWin, text=self.svRefundAmount, width=20, state="readonly")
        refundEntry.grid(row=rowCounter+4, column=1)
        ## Add a filler blank label to create more space
        Label(self.cancelResWin, text=" ").grid(row=rowCounter+5, column=0)
        ## Create cancel button
        cancelButton = Button(self.cancelResWin, text="Cancel Reservation", command=self.cancelReservationSubmit)
        cancelButton.grid(row=rowCounter+6, column=2)

        ## Set cost, date of cancellation, and refund amount string variables to correct amounts
        self.svTotalCostCancel.set(str(reservation[3]))

        currentDate = self.getCurrentDate()
        self.svDateOfCancel.set(currentDate)

        refund = 0
        ## check number of days between current date and start date
        daysBetween = self.resLength(currentDate, self.svCancelStartDate.get()) - 1
        if daysBetween < 0:
            messagebox.showerror('Cancellation Not Permitted', 'You cannot cancel reservations that started before today')
            self.goToHome(self.cancelResWin)
            return None
        elif daysBetween <= 1:
            messagebox.showinfo('No Refund', 'No refund will be provided because the cancellation is too close to the reservation start date.')
        elif daysBetween <= 3:
            refund = (0.8)*(float(self.svTotalCostCancel.get()))
        else:
            refund = float(self.svTotalCostCancel.get())
            
        self.svRefundAmount.set('$'+str(refund))

    def cancelResSearchToHome(self):
        self.goToHome(self.cancelResWin)

    def cancelReservationSubmit(self):
        ## Update reservation status to cancelled
        db = self.connect()
        cursor = db.cursor()
        sql = '''UPDATE Reservation SET Is_Cancelled=1 WHERE Reservation_ID = %s
                 AND Username = %s'''
        sqlTwo = '''UPDATE Reservation SET Total_Cost = Total_Cost - %s
                    WHERE Reservation_ID = %s AND Username = %s'''
        cursor.execute(sql, (self.cancelResID,self.svUsername.get()))
        cursor.execute(sqlTwo, (float((self.svRefundAmount.get()).replace('$', '')),
                       self.cancelResID,self.svUsername.get()))
        db.commit()
        cursor.close()
        db.close()

        messagebox.showinfo('Cancellation Successful', 'This reservation is now cancelled.')
        
        self.goToHome(self.cancelResWin)

    def connect(self):
        db = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',
                             passwd = 'yA9LuhY5', user = 'cs4400_Group_85',
                             db = 'cs4400_Group_85')
        if db == None:
            messagebox.showerror('Login Failed.', 'Unable to connect to the database.')
            return None
        return db

    def checkIfFieldsEmpty(self, fieldsList):
        for data in fieldsList:
            if data == '':
                messagebox.showerror('Registration Failed.', 'Please complete all fields.')
                return None
        return 1

    def resLength(self, startDate, endDate):
        numYears = int(endDate[6:10]) - int(startDate[6:10]) ## years difference
        sDay = 0 ## day of the year of reservation start
        monthNum = int(startDate[0:2])
        for i in range(1,monthNum): ## add up days from months prior to start month
            sDay = sDay + self.monthsDaysDict[i]
        sDay = sDay + int(startDate[3:5]) ## add days from start month

        eDay = 0 ## day of the year of reservation end
        monthNum = int(endDate[0:2])
        for i in range(1,monthNum): ## add up days from months prior to end month
            eDay = eDay + self.monthsDaysDict[i]
        eDay = eDay + int(endDate[3:5]) ## add days from end month

        numDaysOfRes = eDay - sDay + 1 + numYears*365

        return numDaysOfRes

    def dateFormatting(self, date):
        ## Converts a date of the format MM/DD/YYYY to a date of the format YYYY-MM-DD for SQL
        dateMonth = date[0:2]
        dateDay = date[3:5]
        dateYear = date[6:10]
        newDate = dateYear + "-" + dateMonth + "-" + dateDay
        return newDate

    def dateFormattingReverse(self, date):
        ## Converts a date of the format YYYY-MM-DD from SQL to a date of the format MM/DD/YYYY
        dateMonth = date[5:7]
        dateDay = date[8:10]
        dateYear = date[0:4]
        newDate = dateMonth + "/" + dateDay + "/" + dateYear
        return newDate

    def getCurrentDate(self):
        ## Return current date in the format MM/DD/YYYY
        currentDateTime = datetime.datetime.now()
        dateStr = currentDateTime.strftime('%m/%d/%Y')
        return dateStr
        
FancyHotelApp()


