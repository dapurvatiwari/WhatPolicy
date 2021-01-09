import random as rnd
from Params import *

class Agent:
    def __init__(self, id_, f, e, m, fi, ei, ci):
        self.id_ = id_
        self.food = f
        self.energy = e
        self.money = m
        self.foodInfra = fi
        self.energyInfra = ei
        self.commonInfra = ci

    def __hash__(self):
        return self.id_

    def __eq__(self, other):
        return self.id_ == other.id_

    def buyFood(self, demand, agents):
        units = demand
        while units > 0:
            agent = rnd.choice(agents)
            sold = min(units, agent.food - PREF_FOOD)
            agent.food -= sold
            agent.money += FOOD_VALUE*sold
            units -= sold
            self.food += sold
            self.money -= FOOD_VALUE*sold
            agents.remove(agent)
        return demand - units

    def buyEnergy(self, demand, agents):
        units = demand
        while units > 0:
            agent = rnd.choice(agents)
            sold = min(units, agent.energy - PREF_ENERGY)
            agent.energy -= sold
            agent.money += ENERGY_VALUE*sold
            units -= sold
            self.energy += sold
            self.money -= ENERGY_VALUE*sold
            agents.remove(agent)
        return demand - units

    def buyFoodInfra(self, demand, agents):
        units = demand
        assert units >= FOODI_LOT_SIZE
        units = (units//FOODI_LOT_SIZE)*FOODI_LOT_SIZE
        while units > 0:
            agent = rnd.choice(agents)
            sold = min(units, agent.foodInfra)
            agent.foodInfra -= sold
            agent.money += sold*FOOD_INFRA_VALUE
            units -= sold
            self.foodInfra += sold
            self.money -= sold*FOOD_INFRA_VALUE
            agents.remove(agent)
        return demand - units

    def buyEnergyInfra(self, demand, agents):
        units = demand
        assert units >= ENERGYI_LOT_SIZE
        units = (units//ENERGYI_LOT_SIZE)*ENERGYI_LOT_SIZE
        while units > 0:
            agent = rnd.choice(agents)
            sold = min(units, agent.energyInfra)
            agent.energyInfra -= sold
            agent.money += sold*ENERGY_INFRA_VALUE
            units -= sold
            self.energyInfra += sold
            self.money -= sold*ENERGY_INFRA_VALUE
            agents.remove(agent)
        return demand - units

    def buyCommonInfra(self, demand, state):
        units = demand
        sold = min(units, state.commonInfra)
        state.commonInfra -= sold
        state.money += sold*COMMON_INFRA_VALUE
        units -= sold
        self.commonInfra += sold
        self.money -= sold*COMMON_INFRA_VALUE
        return demand - units

    def prodFood(self):
        units = min(self.foodInfra//FIPUF, self.commonInfra//CIPUF,
                    self.energy//EPUF)
        self.food += units
        self.foodInfra -= units*FIPUF
        self.commonInfra -= units*CIPUF
        self.energy -= units*EPUF
        return units

    def prodEnergy(self):
        units = min(self.energyInfra//EIPUE, self.commonInfra//CIPUE,
                    self.money//MPUE)
        self.energy += units
        self.energyInfra -= units*EIPUE
        self.commonInfra -= units*CIPUE
        self.money -= units*MPUE
        return units

    def prodFoodInfra(self):
        lots = min((self.commonInfra//CIPUFI)//FOODI_LOT_SIZE,
                   (self.money//MPUFI)//FOODI_LOOT_SZIE)
        units = lots*FOODI_LOT_SIZE
        self.foodInfra += units
        self.commonInfra -= units*CIPUFI
        self.money -= units*MPUFI
        return lots

    def prodEnergyInfra(self):
        lots = min((self.commonInfra//CIPUEI)//ENERGYI_LOT_SIZE,
                   (self.money//MPUEI)//ENERGYI_LOOT_SZIE)
        units = lots*ENERGYI_LOT_SIZE
        self.foodInfra += units
        self.commonInfra -= units*CIPUEI
        self.money -= units*MPUEI
        return lots
