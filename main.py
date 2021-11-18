from random import randint

VERBOSE = False
#################################################################################
def roll(i_numDice):
  a_Rolls = []
  for i in range(0, i_numDice):
    a_Rolls.append(randint(1, 6))
  return a_Rolls
#################################################################################


#################################################################################
def simulateTurn(i_attackerDice, i_defenderDice):
  # Roll and print player dice
  a_attackerRoll = sorted(roll(i_numDice=i_attackerDice))
  a_defenderRoll = sorted(roll(i_numDice=i_defenderDice))
  if VERBOSE:
    print(a_attackerRoll, a_defenderRoll)

  # Scenario 1: Attacker and defender both roll 1
  if (i_attackerDice == 1 and i_defenderDice == 1):
    # Whoever has the larger dice removes an army
    if a_attackerRoll[0] > a_defenderRoll[0]:
      if VERBOSE:
        print("Attacker removes 1 army")
      return [1, 0]
    else:
      if VERBOSE:
        print("Defender removes 1 army")
      return [0, 1]

  # Scenario 2: Attacker rolls 1 die, defender rolls 2 dice
  if (i_attackerDice == 1 and i_defenderDice == 2):
    # The defenders max is compared to the attackers single roll
    if a_attackerRoll[0] > max(a_defenderRoll):
      if VERBOSE:
        print("Attacker removes 1 army")
      return [1, 0]
    else:
      if VERBOSE:
        print("Defender removes 1 army")
      return [0, 1]

  # Scenario 3: Attacker rolls 2 die, defneder rolls 1
  if (i_attackerDice == 2 and i_defenderDice == 1):
    if max(a_attackerRoll) > a_defenderRoll[0]:
      if VERBOSE:
        print("Attacker removes 1 army")
      return [1, 0]
    else:
      if VERBOSE:
        print("Defender removes 1 army")
      return [0, 1]

  # Scenario 4: Both players roll 2
  if (i_attackerDice == 2 and i_defenderDice == 2):
    i_attackerArmiesLost = 0
    i_defenderArmiesLost = 0
    if a_attackerRoll[0] > a_defenderRoll[0]:
      i_defenderArmiesLost += 1
    else:
      i_attackerArmiesLost += 1

    if a_attackerRoll[1] > a_defenderRoll[1]:
      i_defenderArmiesLost += 1
    else:
      i_attackerArmiesLost += 1

    if VERBOSE:
      print(f"Attacker removed {i_defenderArmiesLost}, defender removed {i_attackerArmiesLost}")
    return [i_defenderArmiesLost, i_attackerArmiesLost]

  if (i_attackerDice == 3 and i_defenderDice == 1):
    if max(a_attackerRoll) > a_defenderRoll[0]:
      if VERBOSE:
        print("Attacker removed 1 army")
      return [1, 0]
    else:
      if VERBOSE:
        print("Defender removed 1 army")
      return [0, 1]

  if (i_attackerDice == 3 and i_defenderDice == 2):
    i_attackerArmiesLost = 0
    i_defenderArmiesLost = 0
    if a_attackerRoll[2] > a_defenderRoll[1]:
      i_defenderArmiesLost += 1
    else:
      i_attackerArmiesLost += 1

    if a_attackerRoll[1] > a_defenderRoll[0]:
      i_defenderArmiesLost += 1
    else:
      i_attackerArmiesLost += 1

    if VERBOSE:
      print(f"Attacker removed {i_defenderArmiesLost}, defender removed {i_attackerArmiesLost}")
    return [i_defenderArmiesLost, i_attackerArmiesLost]


    
def runTrial(i_numTrials, i_attackerDice, i_defenderDice):
  i_attackerWins = 0
  i_defenderWins = 0
  for i in range(0, i_numTrials):
    a_results = simulateTurn(i_attackerDice, i_defenderDice)
    i_attackerWins += a_results[0]
    i_defenderWins += a_results[1]
  print(f"Over {i_numTrials} trials when the attacker rolls {i_attackerDice} and the defender rolls {i_defenderDice}, the attacker defeated {i_attackerWins} of the defenders armies and the defender defeated {i_defenderWins} of the attackers armies")

  f_attackerAverageWins = (i_attackerWins / i_numTrials)*100
  f_defenderAverageWins = (i_defenderWins / i_numTrials)*100

  print(f"Attacker average success: {f_attackerAverageWins}, defender average success: {f_defenderAverageWins}\n")
  return [f_attackerAverageWins, f_defenderAverageWins]

def main():
  i_numTrials = 1000000
  # Simulate 1000 turns of 1:1 dice
  a_res1 = runTrial(i_numTrials, 1, 1)
  # Simulate 1000 turns of 1:2 dice
  a_res2 = runTrial(i_numTrials, 1, 2)
  # Simulate 1000 turns of 2:1 dice
  a_res3 = runTrial(i_numTrials, 2, 1)
  # Simulate 1000 turns of 2:2 dice
  a_res4 = runTrial(i_numTrials, 2, 2)
  # Simulate 1000 turns of 3:1 dice
  a_res5 = runTrial(i_numTrials, 3, 1)
  # Simulate 1000 turns of 3:2 dice
  a_res6 = runTrial(i_numTrials, 3, 2)


  print("\n\n##### Summary #####")
  print(f"For 1:1 dice rolls: Attacker avg: {a_res1[0]}, defender avg: {a_res1[1]}")
  print(f"For 1:2 dice rolls: Attacker avg: {a_res2[0]}, defender avg: {a_res2[1]}")
  print(f"For 2:1 dice rolls: Attacker avg: {a_res3[0]}, defender avg: {a_res3[1]}")
  print(f"For 2:2 dice rolls: Attacker avg: {a_res4[0]}, defender avg: {a_res4[1]}")
  print(f"For 3:1 dice rolls: Attacker avg: {a_res5[0]}, defender avg: {a_res5[1]}")
  print(f"For 3:2 dice rolls: Attacker avg: {a_res6[0]}, defender avg: {a_res6[1]}")


if __name__ == "__main__":
  main()