# Create a class 'Sports'. Declare the sports details in the class like 
# name of the sport, number of players, rules, country of origin, most played in.
# Create functions inside class to print the details of the sports

class Sports:


    def __init__(self):
        self.Name = []
        self.Pnum = {}
        self.Origin = {}
        self.Rules = {}
        self.temp1 = None
        self.temp2 = None
        self.temp3 = None


    def getDetails(self):

        print()
        self.temp1 = input(" ENTER SPORT NAME : ")
        self.Name.append(self.temp1)
        self.temp2 = input(f" ENTER NUMBER OF PLAYERS IN {self.temp1} : ")
        self.Pnum.update({ self.temp1:self.temp2 })
        self.temp3 = input(f" ENTER COUNTRY OF ORIGIN OF {self.temp1} : ")
        self.Origin.update({ self.temp1:self.temp3 })
        self.temp4_list = []
        self.n2 = int(input(f" ENTER NUMBER OF RULES FOR {self.temp1} : "))
        for k in range(self.n2):
            temp4 = input(f" ENTER RULE {k+1} : ")
            self.temp4_list.append(temp4)
        self.Rules.update({ self.temp1:self.temp4_list })
        print('-----------------------------------------------------------')
        self.OPERATIONS()


    def printDetails(self):
    
        print('SPORT NAMES')
        print('-----------------------')
        for i in range(len(self.Name)):
            print(f'{i+1}. {self.Name[i]}')
        print('-----------------------')
        self.temp1 = input( " ENTER SPORT NAME TO PRINT DETAILS : ")
        self.temp2 = self.Pnum[self.temp1]
        self.temp3 = self.Origin[self.temp1]
        self.temp4_list = []
        self.temp4_list = self.Rules[self.temp1]

        print('DETAILS OF THE SPORT    ')
        print('-----------------------------------------------------------------------------------------------------------')
        print(f'NAME OF SPORT : {self.temp1}       NUMBER OF PLAYERS : {self.temp2}       COUNTRY OF ORIGIN : {self.temp3}')
        print('RULES')
        for i in range(len(self.temp4_list)):
            print(f'{i+1}. {self.temp4_list[i]}.')
        print('-----------------------------------------------------------------------------------------------------------')
        
        self.OPERATIONS()


    def OPERATIONS(self):
        print()
        print(" OPERATIONS               ")
        print("--------------------------")
        print(" 1] ENTER SPORT DETAIL   ")
        print(" 2] DISPLAY SPORT DETAILS")
        print(" 3] EXIT                 ")
        print("--------------------------")
        c = input('ENTER YOUR CHOICE : ')
        if c == '1':
            self.getDetails()
        elif c == '2':
            self.printDetails()
        elif c == '3':
            exit()
        else:
            print('Choice Not Found...try again')
            self.OPERATIONS()


S = Sports()
S.OPERATIONS()