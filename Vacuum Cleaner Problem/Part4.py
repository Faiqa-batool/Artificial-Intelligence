from abc import abstractmethod

class Room:
    def __init__(self, location, status='dirty', score=0):
        self.location = location
        self.status = status
        self.score = score

class Environment(object):
    @abstractmethod
    def __init__(self, n):
        self.n = n

    def executestep(self, n=1):
        raise NotImplementedError("should be define")

    def executeall(self):
        raise NotImplementedError("should be define")

    def delay(self, n=100):
        self.delay = n

class Agent(object):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def scene(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

class VaccumAgent(Agent):
    def __init__(self):
        self.direction = False

    def scene(self, environment):
        self.environment = environment

    def act(self):
        if(self.environment.currentroom.status == 'dirty'):
            return 'clean'
        if(self.environment.currentroom.location == 'A'):
            self.direction = False
            return 'right'
        elif(self.environment.currentroom.location == 'C'):
            self.direction = True
            return 'left'
        if not self.direction:
            return 'right'
        return 'left'


class ThreeRoom(Environment):
    def __init__(self, agent):
        self.r1 = Room('A', 'dirty', -10)
        self.r2 = Room('B', 'dirty', -10)
        self.r3 = Room('C', 'dirty', -10)
        self.agent = agent
        self.currentroom = self.r1
        self.delay = 1000
        self.action = ""
        self.step = 1

    def executestep(self, n=1):
        for _ in range(0, n):
            self.information()
            self.agent.scene(self)
            result = self.agent.act()
            self.action = result
            if(result == 'clean'):
                self.currentroom.score += 25
                self.currentroom.status = 'cleaned'
            elif(result == 'right'):
                if(self.currentroom == self.r1):
                    self.currentroom = self.r2
                    self.currentroom.score -= 1
                else:
                    self.currentroom = self.r3
                    self.currentroom.score -= 1
            else:
                if(self.currentroom == self.r3):
                    self.currentroom = self.r2
                    self.currentroom.score -= 1
                else:
                    self.currentroom = self.r1
                    self.currentroom.score -= 1
            self.actions()
            self.step += 1

    def executeall(self):
        raise NotImplementedError("should be define")

    def delay(self, n=100):
        self.delay = n

    def information(self):
        print("Percept at this step %d is [%s, %s, %s]" %
              (self.step, self.currentroom.status, self.currentroom.location, self.currentroom.score))

    def actions(self):
        print("Action taken at this step %d is [%s]" % (
            self.step, self.action))
        print("score: ", self.currentroom.score)


if __name__ == '__main__':
    vaccumagent = VaccumAgent()
    environments = ThreeRoom(vaccumagent)
    environments.executestep(10)
