# Snake Game in Streamlit

Welcome to the Snake Game implemented in Streamlit! This is a classic snake game built using Python and Streamlit. Test your reflexes and enjoy the challenge of guiding the snake to collect food while avoiding collisions.

## Features
- Responsive grid-based gameplay.
- Simple controls using buttons in the sidebar.
- Displays real-time score.
- Restart functionality after a game over.

## Demo
![Demo GIF](demo.gif)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snake-game-streamlit.git
   cd snake-game-streamlit
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your web browser (usually at `http://localhost:8501`).

3. Use the controls in the sidebar to play:
   - **⬆️ Up (W)**
   - **⬅️ Left (A)**
   - **⬇️ Down (S)**
   - **➡️ Right (D)**

4. Try to collect as much food as possible without colliding with walls or the snake itself!

## How It Works
- The game is displayed on a grid using HTML and CSS within Streamlit.
- The snake moves continuously in the chosen direction, and the game updates every `0.2` seconds.
- Food is placed randomly on the grid, and the snake grows when it eats food.
- The game ends when the snake collides with itself or the grid boundaries.

## Customization
- **Grid Size**: Adjust the `GRID_SIZE` constant in the code to change the size of the grid.
- **Speed**: Modify the `SPEED` constant to make the game faster or slower.

## Requirements
- Python 3.7+
- Streamlit
- NumPy

## Contributing

Contributions are welcome! If you find a bug or have an idea for a feature, feel free to submit an issue or a pull request.

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Inspired by the classic Snake game.
- Built using [Streamlit](https://streamlit.io/).

---

Happy gaming! 🐍

