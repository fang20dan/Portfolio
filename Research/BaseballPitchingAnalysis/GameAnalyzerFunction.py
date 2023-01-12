import GameDataSifter
import GameClass
import matplotlib.pyplot as plt

#manually creating, bc data terminology was too specific
hit = {}
ball = {}
foul = {}
strike = {}
out = {}
single = {}
double = {}
triple = {}
home_run = {}

def chooseEvent(name):
    #choosing the event to append to
    if name == "hit_into_play":
        return hit
    elif name == "ball" or name == "blocked_ball":
        return ball
    elif name == "foul" or name == "foul_tip":
        return foul
    elif name == "called_strike" or name == "swinging_strike":
        return strike

def chooseOutcome(name):
    #choosing the outcome to append to
    if name == "field_out" or name == "strikeout":
        return out
    elif name == "single":
        return single
    elif name == "double":
        return double
    elif name == "triple":
        return triple
    elif name == "home_run":
        return home_run

#creating a function to analyze a single game
def analyzeGame(game):
    for i in range(len(game.getPitches())-2, -1,  -1):
        key = game.getPitches()[i+1] + game.getPitches()[i]
        
        #not all events are included in the chooseEvents() checks, so this is just for edge cases
        if chooseEvent(game.getEvents()[i]) != None:
            if key not in chooseEvent(game.getEvents()[i]).keys():
                chooseEvent(game.getEvents()[i])[key] = 1
            else:
                chooseEvent(game.getEvents()[i])[key] += 1
        
        if (chooseEvent(game.getEvents()[i]) == hit or chooseEvent(game.getEvents()[i]) == strike) and chooseOutcome(game.getOutcomes()[i]) != None:
            if key not in chooseOutcome(game.getOutcomes()[i]).keys():
                chooseOutcome(game.getOutcomes()[i])[key] = 1
            else:
                chooseOutcome(game.getOutcomes()[i])[key] += 1

#analyzeGame(GameDataSifter.dataSifter()["game1"])

def totalAnalysis():
    for i in range(1, len(GameDataSifter.dataSifter())+1):
        analyzeGame(GameDataSifter.dataSifter()["game{0}".format(i)])

totalAnalysis()
extraBaseHits = {k: double.get(k,0) + triple.get(k,0) + home_run.get(k,0) for k in set(double) | set(triple) | set(home_run)}

labelsf = list(extraBaseHits.keys())
valsf = list(extraBaseHits.values())
labelsg = list(out.keys())
valsg = list(out.values())

f = plt.figure(1)
plt.bar(range(len(extraBaseHits)), valsf, tick_label = labelsf, align="edge", width = 0.3)
f.show()

g = plt.figure(2)
plt.bar(range(len(out)), valsg, tick_label = labelsg, align="edge", width = 0.3)
g.show()

input()