# Motion Command V1

## Overview

**MotionCommand v1** is a touchless computer interaction system that recognizes hand movements in real-time for controlling desktop operations. By combining **MediaPipe** hand detection technology with **PyAutoGUI** automation capabilities, it enables users to operate their computer through natural hand gestures instead of traditional peripherals. The application includes three operational modes, providing solutions for accessible computing, hygienic interaction, and creative expression.

## Core Capabilities

- **Live Hand Recognition:** Employs MediaPipe technology for detecting hand positions and movements.
- **Three-Mode System:** Multiple interaction modes accessible through specific hand configurations.
- **Gesture-Based Cursor:** Control mouse pointer movement through fingertip tracking.
- **Touch-Free Clicking:** Execute various mouse operations using finger positioning.
- **Window Management:** Navigate between active programs using hand signals.
- **Creative Drawing Space:** Built-in art application with color and tool selection.
- **Seamless Mode Transitions:** Switch between different control modes using hand shapes.

## Control Gestures

### **Cursor Command Mode**

- **Full Hand Open/Open Palm:** Navigate the cursor.
- **Thumb-Index Pinch:** Left-click.
- **Thumb-Middle Pinch:** Right-click.
- **Thumb-Ring Pinch:** Double-click.
- **Pinky Finger Up with Thumb/Hang Loose:** Screenshot.
- **Two Fingers Up/Peace Sign (Index + Middle):** Switch Tab.
- **L-Formation:** Enter Web browser Navigation Control Mode.

### **Web browser Navigation Control Mode**

- **All Fingers Extended (Open Palm):** Create new browser tab.
- **Side Thumb Fist:** Close current browser tab.
- **Two Fingers Up/Peace Sign (Index + Middle):** Refresh current page.
- **Index Finger Pointing Left:** Navigate to previous browser tab.
- **Index Finger Pointing Right:** Navigate to next browser tab.
- **Three Fingers Up (Index + Middle + Ring):** Scroll page up.
- **Pinky Finger Up with Thumb/Hang Loose:** Scroll page down.
- **Rock Sign (Index + Pinky):** Toggle play/pause for media content.
- **Finger Pinch:** Activate Creative Canvas Mode.

### **Creative Canvas Mode**

- **FDrawing Motion:** Create artwork using index finger movements.
- **FPalette Selection:** Pick colors from available options including primary colors and eraser.
- **FTool Sizing: Modify** brush dimensions through interface controls.
- **Workspace Management:** Reset canvas and toggle display options.
- **Full Hand Open/Open Palm:** Return to Cursor Command Mode.

## Technologies Used

- **Python Language**
- **MediaPipe Library** (hand detection and tracking)
- **OpenCV Framework** (image processing and user interface)
- **PyAutoGUI Tool** (system automation and input simulation)
- **NumPy Library** (numerical computations)
- **Pynput Package** (enhanced input control)

## Quick Setup

1. Download the project files:
   ```bash
   git clone https://github.com/yourusername/MotionCommand-v1.git
   cd MotionCommand-v1
   ```
2. Set up required libraries:
   ```bash
   pip install mediapipe opencv-python pyautogui numpy pynput
   ```
3. Run the script:
   ```bash
   jupyter notebook main.ipynb
   ```

## Platform Compatibility Notes

### Windows

- Screenshot → replace `Shift+Cmd+3` with `Win+Shift+S` or Print Screen
- App Switching → use `Alt+Tab`
- Browser → `Ctrl+T`, `Ctrl+W`, `Ctrl+F5`
- Permissions → usually not required

### macOS

- Screenshot → works with `Shift+Cmd+3`
- App Switching → `Cmd+Tab` (already set)
- Browser → `Cmd+T`, `Cmd+W`, `Cmd+R`
- Permissions → enable in _System Preferences > Security & Privacy > Privacy > Accessibility_

### Linux

- Screenshot → use Print Screen or `scrot`
- App Switching → `Alt+Tab`
- Browser → `Ctrl+T`, `Ctrl+W`, `Ctrl+F5`
- Dependencies → may need `python3-tk` and `scrot`

## Application Areas

- **Assistive Computing:** Input alternative for users with physical limitations.
- **Sterile Environments:** Computer operation without physical contact in clean spaces.
- **Creative Applications:** Digital drawing and artistic work without hardware tools.
- **Public Demonstrations:** Touchless control during presentations and talks.
- **Interactive Installations:** Engaging user experiences in public spaces and exhibits.

## Future Development

- Better gesture detection through machine learning improvements.
- User-configurable gesture assignments and shortcuts.
- Support for multiple hands and complex gesture combinations.
- Enhanced compatibility across different operating systems.
- Speed improvements and reduced response times.

## Contribution

Contributions are welcome! Feel free to fork this repo, open issues for bugs, or suggest new features.

## Legal Information

This project is released under the MIT License.
Modifications © 2025 Inayatu Izzati Imawan

---

### Author: Inayatu Izzati Imawan
