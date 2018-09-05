import gym
import matplotlib.pyplot as plt

env = gym.make('Blackjack-v0')
env.reset()

rounds = 10
samples = 10

averagepayouts = []

for sample in range(samples):
    round = 1
    totalpayout = 0

    while round <= rounds:
        action = env.action_space.sample()
        obs, payout, done, _ = env.step(action)
        totalpayout += payout
        if done:
            env.reset()
            round += 1
    averagepayouts.append(totalpayout)

print ("Average payout after {} rounds is {}".format(rounds, sum(averagepayouts) / samples))

def normal_strategy(playersum, dealercard):

    actions = [[1] * 10] * 8
    actions.append([1] * 4 + [0] * 2 + [1] * 4)
    actions.append([1] + [0] * 6 + [1] * 3)
    actions.append([0] + [1] * 9)
    actions.append([0] * 2 + [1] * 8)
    actions.append([0] * 1 + [1] * 9)
    actions.append([0] * 2 + [1] * 8)
    actions.append([0] * 5 + [1] * 5)
    actions.append([0] * 4 + [1] * 6)
    actions.extend([[0] * 10] * 4)


    return actions[sum - 2][dealercard - 2]


assert (normal_strategy(15, 2)) == 0
assert (normal_strategy(15, 1)) == 1

rounds = 10
samples = 10
totalpayout = 0

for _ in range(samples):
    round = 1
    while round <= rounds:
        sum, dealercard, done = (env._get_obs())


        action = normal_strategy(sum, dealercard)

        obs, payout, done, _ = env.step(action)
        totalpayout += payout
        if done:
            env.reset()
            round += 1

print ("Average payout after {} rounds is {}".format(rounds, totalpayout / samples))


