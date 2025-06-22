# from: https://tio.run/##dVLLTsNADLzvV1hBSFkobSIKB6QegIoTSBW9ctkmLl012Y0cF1F@PjhpsuWZk9ePmfE41Z433l02jS0rTwyl4Y1SOWbbpf1AmIF1HFtX7TiO5pKFPh1prUC@E5gm8pyTWfMIrtt4ycblhvIRpEn7vvdlKRmkDvZRwlqyLdF4XXhPcWA7g2Q8PeKeQtE1WwcG2ibwEr0hmVdUzrsBKsxfQGBQK@9rRurlpldSTHvkFHauKszerAqETJQOzfUCaSEFpEFghraIA9UEvqDqMPVAJmMr2mZAfufy@L8JcUQrfGcyd/3oN56wx0SWH2x4MlsUCxjQ1FaEsYeM0DCKJ6UnWcC72gqY4257pSpqb1bz0VgN5xC9uEj3tegZMzkKylFy6KXAbSna@QYiaW6Hf3nSoUD8sz5s35UPPYeGb4vqP7kPJgkDtP/WkTucUeummSaf

import math

deckSize = int(input("Deck Size = "))
    # 40 = Draft, 60 = Standard, 100 = Commander
deckLands = math.floor(deckSize * 0.4)
    # 40% lands in a deck on average
nonLands = deckSize - deckLands
boosterSize = 15 - 1
    # 1 unplayable card
boostersPerPlayer = math.ceil(nonLands / boosterSize)
boostersFraction = round((nonLands / boosterSize), 1)
extraBoosters = math.ceil(deckSize / 40)
    # Makes it easier to create a more consistent deck

print(str(deckSize) + "\n")
print("Recommended Booster Amount: " + str(boostersPerPlayer) + " (" + str(boostersFraction) + ") + " + str(extraBoosters))
print("Recommended Lands Per Deck: " + str(deckLands))
