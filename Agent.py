import random

class Agent():
    def __init__(self, env, epsilon=1.0, alpha=0.5, gamma=0.9, num_episodes_to_train=10):
        self.env = env


        self.valid_actions = list(range(self.env.action_space.n))


        self.Q = dict()
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma


        self.num_episodes_to_train = num_episodes_to_train
        self.small_decrement = (0.1 * epsilon) / (0.3 * num_episodes_to_train)
        self.big_decrement = (0.8 * epsilon) / (0.4 * num_episodes_to_train)

        self.num_episodes_to_train_left = num_episodes_to_train

    def update_parameters(self):

        if self.num_episodes_to_train_left > 0.7 * self.num_episodes_to_train:
            self.epsilon -= self.small_decrement
        elif self.num_episodes_to_train_left > 0.3 * self.num_episodes_to_train:
            self.epsilon -= self.big_decrement
        elif self.num_episodes_to_train_left > 0:
            self.epsilon -= self.small_decrement
        else:
            self.epsilon = 0.0
            self.alpha = 0.0

        self.num_episodes_to_train_left -= 1

    def create_Q_if_new_observation(self, observation):

        if observation not in self.Q:
            self.Q[observation] = dict((action, 0.0) for action in self.valid_actions)

    def get_maxQ(self, observation):

        self.create_Q_if_new_observation(observation)
        return max(self.Q[observation].values())

    def choose_action(self, observation):

        self.create_Q_if_new_observation(observation)


        if random.random() > self.epsilon:
            maxQ = self.get_maxQ(observation)


            action = random.choice([k for k in self.Q[observation].keys()
                                    if self.Q[observation][k] == maxQ])
        else:
            action = random.choice(self.valid_actions)

        self.update_parameters()

        return action


    def learn(self, observation, action, reward, next_observation):

        self.Q[observation][action] += self.alpha * (reward + (self.gamma * self.get_maxQ(next_observation))- self.Q[observation][action])