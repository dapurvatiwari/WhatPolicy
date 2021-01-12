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
        self.role = None
        self.isAlive = True

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
        self.energyInfra += units
        self.commonInfra -= units*CIPUEI
        self.money -= units*MPUEI
        return lots


    # DECISIONS

    def decide:
         """
         Which action to take out of BUY, SELL and PRODUCE
         If requirements == NOT_MET ---> produce/buy suitably
         If requirements == MET ---> then 
                 Cycle-1
                 if basics < PREF --->  if infra is available ---> PRODUCE
                                             if infra not available ---> BUY
                 Cycle-2
                 if money < PREF ---> SELL whatever in most excess (in value terms)
                 Cycle-3
                 if infra < PREF ---> PRODUCE/BUY
                                       if !PRODUCE and !BUY ---> SELL basics
         """
        req_met = (self.food>=2) or (self.energy>=1 and self.food>=1)
        if not req_met:
            if self.food==0:
                amount = self.canProduceFood()
                if amount>=2:
                    self.role=['producer', 'food', amount]
                else:
                    amount = self.canBuyFood()
                    if amount>=2:
                        self.role=['buyer', 'food', amount]
                    else:
                        self.isAlive = False
            if self.food==1: # ==> energy==0; now prefer producing/buying 
                             # atleast 1 energy
                amount = self.canProduceEnergy()
                if amount>=1:
                    self.role=['producer', 'energy', amount]
                else:
                    amount = self.canBuyEnergy()
                    if amount>=1:
                        self.role=['buyer', 'energy', amount]
                    else:
                        self.isAlive=False







                


# def bestBasicsProduce


