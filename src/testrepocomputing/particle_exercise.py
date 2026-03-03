import math

class Particle:
    ''' Class defining particles'''
    def __init__(self, mass, charge, name, momentum=0.):
        self._mass = mass
        self._charge = charge
        self._name = name
        self.momentum = momentum

    @property
    def mass(self):
        return self._mass    

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, momentum):
        if momentum<0:
            print('cannot set the momentum to a value less than 1')
            print('the momentum will be set to 0')
            self._momentum = 0 
        else:
            self._momentum = momentum               

    @property
    def energy(self):
        return math.sqrt(self.mass**2 + self.momentum**2)


    @energy.setter
    def energy(self, energy):
        if energy < self.mass:
            print("Cannot set the energy to a value lower")    
        else:
            self.momentum = math.sqrt(energy**2 - self.mass**2)

    @property
    def beta(self):
        return self.momentum/self.energy

    @beta.setter
    def beta(self, beta):
        if (beta>1) or (beta<0):
            print('error of beta value')
        elif (beta>=1.) and (self.mass<=0):
            print('Cannot set beta = 1 for a massive particle')   
        else:
            self.momentum = beta * self.energy        

    def print_info(self):
        print(f' Particle {self.name} of mass {self.mass} MeV and charge {self.charge}|e|')
        print(f' the particle has momentum {self.momentum} MeV')          
class Proton(Particle):

    MASS = 938.
    CHARGE = 1.
    NAME = 'Proton'

    def __init__(self, momentum=0.):
        Particle.__init__(self, mass = Proton.MASS, charge= Proton.CHARGE, name= Proton.NAME, momentum=momentum)

if __name__ == '__main__':
    proton = Proton(200.)
    proton.print_info()
    proton.beta = 0.8
    proton.print_info()
