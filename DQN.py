import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random
import numpy as np
from collections import deque

# Le modèle de réseau de neurones (MLP)
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim=128):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.out = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.out(x)

# Le Replay Buffer
class ReplayBuffer:
    def __init__(self, max_size=10000):
        self.buffer = deque(maxlen=max_size)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)

# L'agent DQN
class DQNAgent:
    def __init__(self, state_dim, action_dim, batch_size=64, gamma=0.99, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01, lr=0.001, update_freq=100):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.batch_size = batch_size
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.update_freq = update_freq
        self.step_count = 0
        
        # Réseau policy et target
        self.policy_net = DQN(state_dim, action_dim)
        self.target_net = DQN(state_dim, action_dim)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()
        
        # Optimiseur et fonction de perte
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()
        
        # Replay buffer
        self.replay_buffer = ReplayBuffer()

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(range(self.action_dim))  # Exploration
        else:
            state_tensor = torch.FloatTensor(state).unsqueeze(0)  # ajouter une dimension pour le batch
            q_values = self.policy_net(state_tensor)  # Prédire Q-values
            return torch.argmax(q_values).item()  # Choisir l'action avec la plus haute Q-value

    def learn(self):
        if len(self.replay_buffer) < self.batch_size:
            return

        # Prendre un batch d'échantillons du replay buffer
        states, actions, rewards, next_states, dones = zip(*self.replay_buffer.sample(self.batch_size))
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions).unsqueeze(1)
        rewards = torch.FloatTensor(rewards).unsqueeze(1)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones).unsqueeze(1)

        # Calcul de Q_pred (les Q-values prédites pour les actions faites)
        q_pred = self.policy_net(states).gather(1, actions)

        # Calcul de Q_next (les Q-values maximales des prochains états)
        q_next = self.target_net(next_states).max(1)[0].unsqueeze(1).detach()

        # Calcul de Q_target
        q_target = rewards + self.gamma * q_next * (1 - dones)

        # Calcul de la perte (MSE)
        loss = self.loss_fn(q_pred, q_target)

        # Optimisation
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Mise à jour de l'epsilon pour la politique d'exploration
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        # Mise à jour du réseau target toutes les `update_freq` étapes
        self.step_count += 1
        if self.step_count % self.update_freq == 0:
            self.target_net.load_state_dict(self.policy_net.state_dict())

    def store(self, state, action, reward, next_state, done):
        self.replay_buffer.push(state, action, reward, next_state, done)
