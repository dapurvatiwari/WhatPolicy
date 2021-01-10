import random as rnd
from Params import *

class State:
    def __init__(self, fi, ei, ci, m):
        self.id_ = 1
        self.foodInfra = fi
        self.energyInfra = ei
        self.commonInfra = ci
        self.money = m

    def __hash__(self):
        return self.id_

    def __eq__(self, other):
        return self.id_ == other.id_

    def prodFoodInfra(self, units=None):
        if(units is None):
            lots = min((self.commonInfra//CIPUFI)//FOODI_LOT_SIZE,
                   (self.money//MPUFI)//FOODI_LOOT_SZIE)
            units = lots*FOODI_LOT_SIZE
        else:
            lots = units//FOODI_LOT_SIZE
            units = lots*FOODI_LOT_SIZE
        self.foodInfra += units
        self.commonInfra -= units*CIPUFI
        self.money -= units*MPUFI
        return lots
    
    def prodEnergyInfra(self, units=None):
        if(units is None):
            lots = min((self.commonInfra//CIPUEI)//ENERGYI_LOT_SIZE,
                       (self.money//MPUEI)//ENERGYI_LOOT_SZIE)
            units = lots*ENERGYI_LOT_SIZE
        else:
            lots = units//ENERGYI_LOT_SIZE
            units = lots*ENERGYI_LOT_SIZE
        self.energyInfra += units
        self.commonInfra -= units*CIPUEI
        self.money -= units*MPUEI
        return lots

    def prodCommonInfra(self, units=None):
        if(units is None):
            lots = self.money//COMMONI_LOT_SIZE
            units = lots*COMMONI_LOT_SIZE
        else:
            lots = units//COMMONI_LOT_SIZE
            units = lots*COMMONI_LOT_SIZE
        self.commonInfra += units
        self.money -= untis*MPUCI
        return lots
