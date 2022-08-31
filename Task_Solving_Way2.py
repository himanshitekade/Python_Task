# Create a class 'Sports'. Declare the sports details in the class like 
# name of the sport, number of players, rules, country of origin, most played in.
# Create functions inside class to print the details of the sports


class Sports:

	def __init__(self,name_of_sport,number_of_player,rules_of_sports,country_of_the_origin,most_played_in):
		self.name_of_sport    = name_of_sport
		self.number_of_player = number_of_player
		self.rules_of_sports  = rules_of_sports
		self.country_of_the_origin = country_of_the_origin
		self.most_played_in = most_played_in

	def Sports_details(self):
		print("NAME OF SPORTS IS    : ",self.name_of_sport)
		print("NUMBER OF PLAYERS ARE: ",self.number_of_player)
		print("RULES OF SPORTS IS   : ",self.rules_of_sports)
		print("COUNTRY OF ORIGIN IS : ",self.country_of_the_origin)
		print("MOST PLAYED IN       : ", self.most_played_in)	
	
s1 = Sports('CRICKET',11,'PLAYER SHOULD BE 11 FROM BOTH TEAM','ENGLAND','INDIA')
s1.Sports_details()	
	

	

	
