# Flappy Bird Clone 🐦

A simple 2D side-scroller game built using **Python** and **Pygame**. This project was developed as a practice exercise to understand game physics, object-oriented logic, and real-time event handling in Python.

## 🕹️ How to Play
* **Space Bar:** Press to make the bird jump and stay in the air.
* **Objective:** Navigate the bird through the gaps between the green pipes.
* **Score:** Each pipe you pass increases your score by 1.
* **Game Over:** If the bird hits a pipe or the screen boundaries, the game ends.
* **Restart/Quit:** After a Game Over, press **'R'** to restart or **'Q'** to quit.

## 🚀 Key Features
* **Physics Simulation:** Implemented constant gravity and upward thrust (jump strength).
* **Randomized Obstacles:** Pipes are generated with varying heights and gap sizes for dynamic gameplay.
* **Collision Detection:** Accurate pixel-based collision handling using `pygame.Rect`.
* **Audio Integration:** Features background music and localized sound effects for jumps and crashes.
* **Scrolling Background:** Smooth infinite-scrolling background effect.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** Pygame

## 📂 Project Structure
```text
Flappy_Bird/
├── flappy_bird.py       # Main game script
├── bird1.png            # Bird sprite
├── background.png       # Background image (optional)
├── jump.wav             # Jump sound effect
├── game_over.wav        # Crash sound effect
└── README.md            # Documentation
