PREF_FOOD = 5
PREF_ENERGY = 5
FOODI_LOT_SIZE = 100
ENERGYI_LOT_SIZE = 100
FIPUF = 1 // food infra required to produce unit food
CIPUF = 1 // common infra required to produce unit food
EPUF = 1 // energy required to produce unit food
EIPUE = 1 // energy infra required to produce unit energy
CIPUE = 1 // common infra required to produce unit energy
MPUE = 1 // money required to produce unit energy
CIPUFI = 1 // common infra required to produce food infra
MPUFI = 1 // money required to produce food infra
CIPUEI = 1 // common infra required to produce energy infra
MPUEI = 2 // money required to produce energy infra
MPUCI = 1 // money required to produce common infra
COMMON_INFRA_VALUE = MPUCI
ENERGY_INFRA_VALUE = COMMON_INFRA_VALUE*CIPUEI + MPUEI
FOOD_INFRA_VALUE = COMMON_INFRA_VALUE*CIPUFI + MPUFI
ENERGY_VALUE = ENERGY_INFRA_VALUE*EIPUE \
             + COMMON_INFRA_VALUE*CIPUE \
             + MPUE
FOOD_VALUE = FOOD_INFRA_VALUE*FIPUF \
           + COMMON_INFRA_VALUE*CIPUF \
           + ENERGY_VALUE*EPUF
