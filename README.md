# Hand Ball Game 🎮

An interactive hand gesture-controlled ball tapping game built with Python, OpenCV, and MediaPipe. Test your reflexes by tapping virtual balls using just your index finger!

## 🎯 Game Overview

Hand Ball Game is a fun and engaging computer vision game where players use hand gestures to tap randomly positioned balls on screen. The objective is to tap as many balls as possible within a 30-second time limit using your index finger detected through your webcam.

## ✨ Features

- **Hand Gesture Control**: Uses MediaPipe for accurate hand tracking
- **Real-time Interaction**: Responsive finger tip detection for ball tapping
- **Timed Gameplay**: 30-second rounds with automatic reset
- **Score Tracking**: Counts successful taps during gameplay
- **Visual Feedback**: Live hand landmarks and finger position display
- **Auto-restart**: Game automatically restarts after time expires

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV (cv2)**: Computer vision and video processing
- **MediaPipe**: Hand detection and tracking
- **NumPy**: Numerical computations
- **Math**: Distance calculations
- **Random**: Ball position generation

## 📋 Requirements

Install the required dependencies:

```bash
pip install opencv-python
pip install mediapipe
pip install numpy
```

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gnaneshwar08/Hand_Ball_Game.git
   cd Hand_Ball_Game
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Create a requirements.txt file with the dependencies listed above*

3. **Run the game**:
   ```bash
   python GestureBallGame.py
   ```

4. **Make sure your webcam is connected and working**

## 🎮 How to Play

1. **Position yourself**: Sit in front of your webcam with good lighting
2. **Raise your hand**: Show your hand to the camera (the game tracks one hand)
3. **Point your index finger**: Use your index finger to "tap" the green balls
4. **Tap the balls**: Move your finger close to the green ball to tap it
5. **Score points**: Each successful tap moves the ball to a new random position
6. **Beat the clock**: Try to tap as many balls as possible in 30 seconds!

## 🎯 Game Controls

- **Index Finger**: Primary control for tapping balls
- **Q Key**: Quit the game at any time
- **Automatic Reset**: Game restarts automatically after 30 seconds

## 📊 Game Mechanics

- **Ball Size**: 30-pixel radius
- **Detection Zone**: Ball is tapped when finger is within the ball radius
- **Tap Prevention**: Each ball position can only be tapped once
- **Screen Size**: 1000x700 pixels
- **Game Duration**: 30 seconds per round

## 🔧 Configuration

You can modify game settings by editing the configuration variables in `GestureBallGame.py`:

```python
# Game configuration
screen_width = 1000      # Screen width
screen_height = 700      # Screen height
ball_radius = 30         # Ball size
ball_color = (0, 255, 0) # Ball color (BGR format)
game_duration = 30       # Game duration in seconds
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Multiple difficulty levels
- [ ] High score tracking
- [ ] Multiple ball support
- [ ] Sound effects
- [ ] Different ball colors and sizes
- [ ] Power-ups and special balls
- [ ] Multiplayer support

## 🐛 Troubleshooting

**Camera not working?**
- Ensure your webcam is connected and not being used by other applications
- Try changing the camera index in `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if you have multiple cameras

**Hand detection issues?**
- Ensure good lighting conditions
- Keep your hand clearly visible to the camera
- Try adjusting your distance from the camera

**Performance issues?**
- Close other applications that might be using your camera
- Ensure you have sufficient processing power for real-time video processing

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Gnaneshwar** - [@gnaneshwar08](https://github.com/gnaneshwar08)

---

⭐ If you enjoyed this game, please give it a star! ⭐
