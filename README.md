# SpaceTetrisAI

## Repository contents
This repository consists of three packages:
+ environment  
+ agents  
+ ml  

### Environment
Environment package contains full implementation of Space Tetris. Position represented using a bitboard data structure, 
and the package keeps track of the game's history to allow for backtracking when 
searching the game space. Additionally, the package includes an evaluator script 
that can be used to assess an agent's performance on a given game.

The evaluator.py module includes a score_agent function with a key parameter called deep_score. If deep_score is set to true, the score_agent function will perform a more thorough evaluation of the agent, resulting in a higher performance score. However, this evaluation process takes longer to compute. On the other hand, if deep_score is set to false, a faster but less comprehensive evaluation will be performed, resulting in a much lower score.

During the development phase of an agent, shallow play can be used to quickly assess its potential, while deep play can be used to determine its true ability. Ultimately, the choice between shallow and deep play depends on the specific needs and goals of the evaluation process.

### Agents
Agents package contains implantation for 7 different agents:
+ **Random Agent** score* **897**/**3973**: The Random Agent in the Space Tetris game environment is a baseline or control agent that always chooses a random action. This means that the agent does not take into account the current game position or any long-term strategies, but rather selects a move at random without any specific goal in mind. The purpose of the Random Agent is to provide a baseline for comparison to other agents. By comparing the performance of other agents against the Random Agent, we can determine whether these agents are actually learning and improving over time. The Random Agent also serves as a useful starting point for developing more advanced agents, as it provides a simple and straightforward implementation that can be used as a reference point.
+ **Noise Null Agent** score* **3426**/**22475**: The Noise Null Agent in the Space Tetris game environment is similar to the Null Agent, but with the addition of a layer of random noise. Like the Null Agent, the Noise Null Agent always chooses the play that results in the best immediate outcome if there is an opportunity to clear one or more lines. However, if there is no opportunity to clear any lines, the Noise Null Agent adds a layer of random noise to the score of the potential moves. This means that the agent will occasionally make a random play even if it is not the best immediate choice. The amount of noise added is determined by a configurable parameter, which can be adjusted to control the level of randomness in the agent's decisions.
+ **Null Agent** average score* **4497**/**22671**: The Null Agent in the Space Tetris game environment follows a simple strategy to make its moves. The agent always chooses the play that results in the best immediate outcome. This means that if there is an opportunity to clear one or more lines, the agent will choose that move as it provides the best immediate reward. If there is no opportunity to clear any lines, the Null Agent chooses the first play that it can make. This strategy causes the game board to fill from one side to another over time, which can make the game more challenging as the player has less space to work with.
+ **DNN Agent** score* **7103**/**Na**: The DNN Agent within the Space Tetris game environment makes decisions using a neural network that has been trained using the machine learning (ML) package. The neural network is responsible for determining the best possible moves for the agent to make in order to achieve a high score in the game.
+ **Smart Agent** score* **7496**/**36160**: The Smarter Agent in the Space Tetris game environment aims to minimize the number of exposed block edges. This means that the agent will attempt to minimize the number of blocks on the game board, as the more blocks there are, the more exposed edges there will be. The only way to achieve this is by clearing lines, which removes blocks from the board and reduces the number of exposed edges. Additionally, the Smarter Agent prefers to start at the edge of the game board and play subsequent blocks adjacent to other blocks. This strategy helps to decrease the number of exposed edges, as it maximizes the number of blocks that are touching each other and minimizes the number of blocks that are exposed to the edge of the board.
+ **Smarter Agent** score* **13449**/**56783**: The Smarter Agent in the Space Tetris game environment aims to minimize the difficulty of a given game position. The difficulty of a position is calculated based on how difficult it is to fill individual grid cells. A block of empty cells will have a very low difficulty score, while a single empty cell surrounded by filled cells on all sides will have a very high difficulty score, as there is only one block in the game that can be played to fill that cell. The Smarter Agent uses this difficulty score to determine the best possible move to make, with the goal of minimizing the overall difficulty of the game position. This approach allows the agent to effectively navigate the game board and make strategic moves that set it up for long-term success. For more detailed information on how the Smarter Agent works, please refer to the smarter_agent.py file in the codebase.
+ **Hybrid Agent** score* **14404**/**Na**: The Hybrid Agent in the Space Tetris game environment combines the strengths of both the Smarter Agent and DNN Agent. The Smarter Agent is better at evaluating balanced positions, while the DNN Agent is better at recognizing very good or very bad positions. In this implementation, the Hybrid Agent primarily relies on the Smarter Agent to make decisions. However, the DNN Agent is also utilized to influence the decision-making process in extreme cases where the Smarter Agent may not perform as well.  

*The average score over 1000 for shallow play and 250 for deep play generated using the main.py script is a measure of the performance of the different agents in the Space Tetris game environment. All agents played the exact same 1000/250 games, each with a limit of 500 blocks played per game for shallow play and 1500 for deep play (most agents never reach their block limit).  

![alt text](agent_scores.jpg)

### ML
The ML package contains the network architecture used for the DNN agent, as well as a trainer module that can be used to train the agent, and a train launcher used to start the training process.

While the DNN agent shows promise in its ability to make decisions based on the current game state, it could be greatly improved by further increasing training time. However, training the agent is very slow due to the random nature of the game, which requires a large number of evaluation games per agent to determine its fitness.

It is important to note that training a DNN agent for a game like Space Tetris can be a challenging task, as it requires the agent to learn how to make decisions in a complex and dynamic environment. As such, the training process may need to be tuned carefully to ensure that the agent is able to learn effectively and efficiently.

Overall, while the DNN agent has shown promise in its ability to make decisions in the Space Tetris game environment, further improvements are possible with increased training time and careful tuning of the training process.