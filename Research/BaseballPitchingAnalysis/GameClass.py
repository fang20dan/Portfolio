class game:
    def __init__(self):
        #pitching sequence for specific game (list)
        self.pitches = []
        #events from each pitch (list) (i.e. strike, ball, hit), specific event for specific pitch have same index in list
        self.events = []
        #if was a hit, then will be the result of hit, if not then a 0 will be set as a place holder
        self.outcomes = []

    def getPitches(self):
        return self.pitches
    
    def getEvents(self):
        return self.events

    def getOutcomes(self):
        return self.outcomes

    def addPitches(self, pitch):
        self.pitches.append(pitch)

    def addEvents(self, event):
        self.events.append(event)

    def addOutcomes(self, out):
        self.outcomes.append(out)