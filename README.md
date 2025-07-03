# 🌌 Inner Cosmos

**Inner Cosmos** is an interactive artistic project that simulates the creation of a universe using hand gestures. It merges **technology, science, and art** to allow users to interact with atoms and simulate gravitational fields in real-time using their hands.

This project is designed to run locally on macOS using **OpenCV**, **MediaPipe**, and **Pygame** — providing complete control over the rendering and gesture recognition process.

---

## ✨ Purpose

Inner Cosmos aims to explore the poetic and scientific process of creating matter, stars, and life using:

- **Real atomic data** (from the periodic table)
- **Hand-tracking interaction**
- **Gravitational simulation**
- **Interactive composition**
- **Educational + meditative experience**

It is inspired by the connection between the inner self and the formation of the universe.

---

## ✅ What has been implemented so far

- 🎥 Real-time webcam capture
- ✋ Hand detection using MediaPipe (right hand)
- 🖱️ A virtual mouse controlled by the index finger
- 💠 Custom UI design in Pygame
- 💻 Clean architecture with modular folder structure (`gestures/`, `ui/`, `utils/`)

---

## 🔄 What will be implemented next

- 👆 Pinch detection (gesture to "select" atoms)
- 🌌 Gravity simulation field with moving atoms
- ✨ Atom combination to simulate star creation
- 🪐 Physics engine for interactions (attraction, repulsion, collision)
- 🧠 Dynamic behavior based on atom type
- 🎨 Visual effects and sound feedback
- 🖼️ Snapshot feature to "save your universe"

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Pygame** (visual rendering)
- **OpenCV** (webcam capture)
- **MediaPipe** (gesture detection)
- **Modular architecture**

---

## 🚀 How to Run

```bash
# Create and activate a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
