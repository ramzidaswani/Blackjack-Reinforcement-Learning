import gym
from gym import wrappers

env = gym.make('Blackjack-v0')

rounds = 10
samples = 10

num_episodes_values = range(200, 2200, 200)


for num_episodes_value in num_episodes_values:
    totalpayout = 0
    average_payouts = []
    agent = Agent(env=env, epsilon=1.0, alpha=0.8, gamma=0.9, num_episodes_to_train=num_episodes_value)

    observation = env.reset()
    for sample in range(samples):
        round = 1

        while round <= rounds:
            action = agent.choose_action(observation)
            next_observation, payout, done, _ = env.step(action)
            agent.learn(observation, action, payout, next_observation)
            totalpayout += payout
            observation = next_observation
            if done:
                observation = env.reset()
                round += 1
                average_payouts.append(totalpayout / (sample * rounds + round))

    print (
        "Average payout : {} rounds: {} episodes: {}".format(rounds, num_episodes_value, totalpayout / (samples)))

env = gym.make('Blackjack-v0')


total_payout = 0
average_payouts = []
agent = Agent(env=env, epsilon=1.0, alpha=0.8, gamma=0.9, num_episodes_to_train=10)

num_rounds = 10
num_samples = 1


observation = env.reset()
for sample in range(num_samples):
    round = 1
    epsilon_values = []

    while round <= num_rounds:
        epsilon_values.append(agent.epsilon)
        action = agent.choose_action(observation)
        next_observation, payout, is_done, _ = env.step(action)
        agent.learn(observation, action, payout, next_observation)
        total_payout += payout
        observation = next_observation
        if is_done:
            observation = env.reset()
            round += 1
            average_payouts.append(total_payout/(sample*num_rounds + round))
agent = Agent(env=env, epsilon=1.0, alpha=0.5, gamma=0.2, num_episodes_to_train=10)

num_rounds = 10
num_samples = 10

average_payouts = []

observation = env.reset()
for sample in range(num_samples):
    round = 1
    total_payout = 0

    while round <= num_rounds:
        action = agent.choose_action(observation)
        next_observation, payout, is_done, _ = env.step(action)
        agent.learn(observation, action, payout, next_observation)
        total_payout += payout
        observation = next_observation
        if is_done:
            observation = env.reset()
            round += 1
    average_payouts.append(total_payout)

    print ("Average payout after {} rounds is {}".format(num_rounds, sum(average_payouts) / (num_samples)))
