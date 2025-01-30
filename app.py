import streamlit as st
import time
import numpy as np
import random

# Initialize the app configuration
st.set_page_config(page_title="Snake Game", layout="centered")

st.title("🐍 Snake Game")

# Game settings
GRID_SIZE = 20
SPEED = 0.2

# Initialize game state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]  # Initial snake position
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.game_over = False

# Helper functions
def place_food():
    """Place food at a random position on the grid."""
    while True:
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if food not in st.session_state.snake:
            return food

def move_snake():
    """Update the snake's position based on the current direction."""
    head_x, head_y = st.session_state.snake[-1]
    if st.session_state.direction == "UP":
        new_head = (head_x - 1, head_y)
    elif st.session_state.direction == "DOWN":
        new_head = (head_x + 1, head_y)
    elif st.session_state.direction == "LEFT":
        new_head = (head_x, head_y - 1)
    elif st.session_state.direction == "RIGHT":
        new_head = (head_x, head_y + 1)

    # Check collisions
    if (
        new_head[0] < 0
        or new_head[0] >= GRID_SIZE
        or new_head[1] < 0
        or new_head[1] >= GRID_SIZE
        or new_head in st.session_state.snake
    ):
        st.session_state.game_over = True
        return

    # Move snake
    st.session_state.snake.append(new_head)

    # Check if food is eaten
    if new_head == st.session_state.food:
        st.session_state.food = place_food()
        st.session_state.score += 1
    else:
        st.session_state.snake.pop(0)  # Remove the tail if no food eaten

def draw_grid():
    """Render the game grid."""
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    for x, y in st.session_state.snake:
        grid[x, y] = 1
    food_x, food_y = st.session_state.food
    grid[food_x, food_y] = 2

    grid_html = "<div style='display: grid; grid-template-columns: repeat({0}, 20px); gap: 1px;'>".format(GRID_SIZE)
    for row in grid:
        for cell in row:
            if cell == 1:
                color = "green"  # Snake body
            elif cell == 2:
                color = "red"  # Food
            else:
                color = "lightgrey"  # Empty cell
            grid_html += f"<div style='width: 20px; height: 20px; background-color: {color};'></div>"
    grid_html += "</div>"
    st.markdown(grid_html, unsafe_allow_html=True)

# Game controls
def handle_input():
    """Handle user input for controlling the snake."""
    for key in ["w", "a", "s", "d"]:
        if st.session_state.get(key):
            if key == "w" and st.session_state.direction != "DOWN":
                st.session_state.direction = "UP"
            elif key == "s" and st.session_state.direction != "UP":
                st.session_state.direction = "DOWN"
            elif key == "a" and st.session_state.direction != "RIGHT":
                st.session_state.direction = "LEFT"
            elif key == "d" and st.session_state.direction != "LEFT":
                st.session_state.direction = "RIGHT"

# Add input buttons
with st.sidebar:
    st.write("### Controls")
    st.session_state["w"] = st.button("⬆️ Up (W)")
    st.session_state["a"] = st.button("⬅️ Left (A)")
    st.session_state["s"] = st.button("⬇️ Down (S)")
    st.session_state["d"] = st.button("➡️ Right (D)")

# Main game loop
if not st.session_state.game_over:
    handle_input()
    move_snake()
    draw_grid()
    st.write(f"### Score: {st.session_state.score}")
    time.sleep(SPEED)
else:
    st.write("## Game Over! 🥲")
    st.write(f"### Final Score: {st.session_state.score}")
    if st.button("Restart"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = place_food()
        st.session_state.direction = "RIGHT"
        st.session_state.score = 0
        st.session_state.game_over = False
