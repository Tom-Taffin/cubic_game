from game import Game
from DQN import DQNAgent
from assets.levels.dqn_levels.DQNLevel1 import DQNLevel1

LENGTH = 800
WIDTH = 600

# Initialiser l'agent
jeu = Game(DQNLevel1(LENGTH, WIDTH))
jeu.initScreen()
agent = DQNAgent(state_dim=len(jeu.state()), action_dim=5, batch_size=64)

# Nombre d'épisodes d'entraînement
n_episodes = 1000



for episode in range(n_episodes):
    jeu.initGame(DQNLevel1(LENGTH, WIDTH))
    state = jeu.state()  # Récupérer l'état initial
    done = False
    total_reward = 0
    if episode == n_episodes-1:
        f = open("last.txt", "w")

    while not done:
        action = agent.select_action(state)  # Sélectionner une action selon la politique ε-greedy
        reward, done = jeu.step(action, LENGTH, WIDTH)  # Appliquer l'action et obtenir le nouvel état et la récompense
        next_state = jeu.state()

        if episode == n_episodes-1:
            f.write(str(action) + "\n")

        # Ajouter la transition dans le buffer de replay
        agent.store(state, action, reward, next_state, done)
        
        # Apprendre à partir des transitions dans le replay buffer
        agent.learn()

        # Passer à l'état suivant
        state = next_state
        total_reward += reward
    
    if episode == n_episodes-1:
            f.close()

    print(f"Episode {episode + 1}/{n_episodes}, Score: {jeu.score}, Total Reward: {total_reward}")