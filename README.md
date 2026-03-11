# 🎰 Object-Oriented Blackjack Engine

An interactive, command-line implementation of Blackjack built with **Python 3**. This project demonstrates the application of Object-Oriented Programming (OOP) to manage complex game states, user interactions, and automated dealer logic.



## 🚀 Key Features

* **Dynamic Ace Handling:** Implements an algorithm that automatically adjusts Ace values between 11 and 1 to prevent the player from busting.
* **Stateful Betting System:** A persistent `Chips` class that tracks the player’s bankroll across multiple rounds of play.
* **Encapsulated Logic:** Each game component (Card, Deck, Hand, Chips) is a self-contained object, ensuring clean and maintainable code.
* **Automated Dealer AI:** The dealer follows casino rules, automatically hitting until reaching a minimum hand value of 17.

## 🛠️ Technical Skills Demonstrated

### 1. Object-Oriented Programming (OOP)
The project uses four distinct classes to handle the game's components:
* `Card`: Data structure for individual card attributes.
* `Deck`: Handles the generation and randomization (shuffling) of 52 card objects.
* `Hand`: Manages the "running state" of cards and calculates real-time values.
* `Chips`: Manages the financial state and betting logic.

### 2. Input Validation & Resilience
The game is built to be robust against invalid user input. It utilizes `try/except` blocks for monetary inputs and string parsing (`.lower().startswith()`) to handle user decisions smoothly.

### 3. Loop Architecture
The engine uses a structured nested loop system:
1.  **Outer Loop:** Manages the overall game session and replayability.
2.  **Player Loop:** Manages real-time decision-making (Hit/Stand).
3.  **Dealer Loop:** An automated mathematical loop executing house rules.



## 📋 How to Run

1. Ensure you have Python 3.x installed.
2. Clone the repository.
3. Run the script:
   ```bash
   python main.py
