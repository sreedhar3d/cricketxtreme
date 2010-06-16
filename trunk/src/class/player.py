'''
@project: Cricket Xtreme
@description: player class definitions; will list all player performance variables and functions
@author: Kinshuk Sunil
@license: GNU GPL 3.0. Read /license-source.txt for more details
'''

class Player(object):
    """This lists all player variables and basic functions to manipulate them"""
    FirstName = "First Name" 				# First Name of Player
    LastName = "Last Name"					# Last Name of Player
    Age = 30								# Age of Player (will be used in later relases for managing retirements)
    BattingStyle = 0						# How does the player bat? -1 = Defensive, 0 = Neutral, 1 = Aggresive
    BattingSide = 0							# What is the preferred side player plays to? -1 = Leg Side, 0 = Neutral, 1 = Off Side
    BowlingPref = 0							# What type of bowls the player is best suited to play? -1 = Spin, 0 = Neutral, 1 = Pace
    PlayHand = 0							# 0 = LHB, 1 = RHB
    BowlType = 0							# What is the type of Bowler?  -1 = Spin, 0 = Neutral, 1 = Pace
    isWicket = False						# Is the player a wicket keeper?
    isStar = False							# Is the player a star player in the team? (will affect commentators and crowd, later)
    
    Aggressiveness = 0
    Agility = 0
    Awareness = 0
    BatSkill = 0
    BowlSkill = 0
    Creativity = 0
    Dodge = 0
    Fitness = 0
    Form = 0
    Handling = 0
    Morale = 0
    Positioning = 0
    Speed = 0
    Stamina = 0
    Strength = 0

    def __init__(selfparams):
        '''
        Constructor
        '''
    
    def CalPerf_bats (self):
        """This function will return a score of the players overall performance as a Batsman"""
        return (self.BatSkill *2)+((self.Agility +self.Aggressiveness)*0.7)+(self.Creativity*0.8)+self.Positioning+((self.Stamina+self.Strength)*1.5)+(self.Speed*0.5) 
    def CalPerf_bowl (self):
        """This function will return a score of the players overall performance as a Bowler"""
        return ((self.Aggressiveness*0.7)+(self.Agility*0.8)+(self.Creativity*0.5)+(self.Dodge*0.75)+(self.Speed*0.75)+(self.Strength*0.7))*1.5+(self.BowlSkill*2)
    def CalPerf_field (self):
        """This function will return a score of the players overall performance as a Fielder"""
        return ((self.Agility*0.85)+self.Dodge+(self.Fitness*0.85)+self.Speed+(self.Stamina*0.85))*2
