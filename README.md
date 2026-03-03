# 🐦 Flappy Bird Python Clone

![Flappy Bird Cover](https://raw.githubusercontent.com/thathsara-devindi/Flappy_Bird/main/cover.png) 

A polished 2D side-scroller game built using **Python** and **Pygame**. This project demonstrates core game development principles including physics simulation, collision detection, and real-time event handling.

---

## 🎮 Live Demo
Don't want to download the code? You can play the game directly on your PC here:
👉 **[Play Flappy Bird Clone on Itch.io](https://thathsara-devindi.itch.io/flappy-bird-python-clone)**

---

## 🕹️ How to Play
* **Space Bar:** Press to make the bird jump and stay in the air.
* **Objective:** Navigate the bird through the gaps between the pipes.
* **Score:** Each pipe you pass increases your score by 1.
* **Game Over:** If the bird hits a pipe or boundaries, the game ends.
* **Controls:** Press **'R'** to restart or **'Q'** to quit after a game over.

---

## 🚀 Key Technical Features
- **Physics Simulation:** Implemented constant gravity and upward thrust logic.
- **Dynamic Obstacle Generation:** Randomized pipe heights and gaps for varied difficulty.
- **Collision Detection:** Accurate hit-box handling using `pygame.Rect`.
- **Audio Integration:** Features background music and localized SFX for jumps and crashes.
- **State Management:** Seamless transitions between the main game loop and game-over screens.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** Pygame
* **Deployment:** Itch.io

---

## 📂 Project Structure
```text
Flappy_Bird/
├── main.py              # Main game logic
├── assets/              # Folder for images & sounds
│   ├── bird1.png        
│   ├── background.png   
│   ├── jump.wav         
│   └── bg_music.ogg     
└── README.md            # Documentation
