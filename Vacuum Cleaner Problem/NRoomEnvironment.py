# n Room Environment where n>=2:
# ______________________________

from abc import abstractmethod
import random

class Environment(object):
    ''' classdocs '''

    @abstractmethod
    def __init__(self, n):
        self.n = n

    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n

class Room:
    def __init__(self, location, status="dirty"):
     
        self.location = location
        self.status = status

class Agent(object):
    ''' classdocs '''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

class VaccumAgent(Agent):
    ''' classdocs '''

    def __init__(self):
        ''' Constructor '''
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        current_room = self.environment.currentRoom
        if current_room.status == 'dirty':
            return 'clean'
        next_room = self.environment.getNextRoom()
        if next_room is not None:
            self.environment.currentRoom = next_room
        return 'move'

class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, n):
        self.rooms = [Room(str(i), 'dirty') for i in range(1, n+1)]
        self.agent = agent
        self.currentRoom = random.choice(self.rooms)
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'move':
                pass  # Do nothing, already moved to next room
            self.displayAction()
	        self.step+=1
def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def getNextRoom(self):
        current_index = int(self.currentRoom.location) - 1
        next_index = (current_index + 1) % len(self.rooms)
        next_room = self.rooms[next_index]
        if next_room.status == 'dirty':
            return next_room
        for room in self.rooms:
            if room.status == 'dirty':
                return room
        return None

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]"
              % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n

if __name__ == '__main__':
    agent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(agent, n=4)
    env.executeStep(50)



