'''
@project: Cricket Xtreme
@description: player class definitions; will list all player performance variables and functions
@author: Kinshuk Sunil
@license: GNU GPL 3.0. Read /license-source.txt for more details
'''

class Player(object):
    """This lists all player variables and basic functions to manipulate them"""
    FirstName = "First Name"        ' String Resource, Player First Name
    LastName = "Last Name"          ' String Resource, Player Last Name
    Age = 30                        ' Integer Resource, Age in years
    BattingStyle = 0                ' 0 for Neutral, 1 for Defensive, 2 for Aggresive
    BattingSide = 0                 ' 0 for Neutral, 1 for Off Side, 2 for Leg Side
    BowlingPref = 0                 ' 0 for Neutral, 1 for Spin, 2 for Pace
    PlayHand = 0                    ' 0 for Right, 1 for Left
    BowlType = 0                    ' 0 for Neutral, 1 for Half Pitch, 2 for Over Pitch
    isWicket = False                ' Is the player Wicket Keeper?
    isStar = False                  ' Is the player a Star Player?
    Team = 0                        ' Players Team ID
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
        