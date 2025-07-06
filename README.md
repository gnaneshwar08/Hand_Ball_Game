````markdown
# 🎮 Hand Ball Game using OpenCV & MediaPipe

A simple, interactive computer vision game where you control a virtual ball using your hand gestures captured via webcam!  
Move your **index finger** to tap the green ball on the screen — see how many taps you can score in **30 seconds**.

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV** — for video capturing and displaying the game
- **MediaPipe** — for real-time hand tracking
- **NumPy** — for numerical operations
- **Math** — for distance calculations
- **Random** — to randomize ball positions

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/hand-ball-game.git
   cd hand-ball-game
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**

   ```bash
   python hand_ball_game.py
   ```

---

## 🎮 How to Play

* A green ball appears randomly on the screen.
* Move your **index finger** in front of the webcam.
* When your fingertip overlaps the ball, your **tap count increases by one**.
* The ball then jumps to a new random position.
* You have **30 seconds** to score as many taps as possible.
* Your score and remaining time are displayed on the screen.

**Controls:**

* Press **`q`** to quit anytime.

---

## 📷 Requirements

* A computer with a webcam
* Python 3.7 or newer
* The following Python libraries:

  * opencv-python
  * mediapipe
  * numpy

---

## 📁 Project Structure

```
hand-ball-game/
│
├── hand_ball_game.py       # Main game script
├── requirements.txt        # List of required packages
└── README.md               # Project documentation
```

---

## 📌 Future Improvements

* Add background music and sound effects.
* Track multiple hands or multiple fingers.
* Create difficulty levels with increasing ball speed or decreasing ball size.
* Save high scores.
* Add a start menu and end game leaderboard.

---


## 🙌 Acknowledgments

* [MediaPipe by Google](https://mediapipe.dev/)
* [OpenCV](https://opencv.org/)
* Inspired by basic hand-gesture-based interaction games.

```
