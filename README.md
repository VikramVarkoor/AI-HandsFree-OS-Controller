# AI Hands-Free OS Controller

A Computer Vision-based automation tool that enables hands-free system control using real-time spatial head tracking. Built with OpenCV, this project bridges the gap between digital imaging and OS-level hardware interaction.

## How it Works
The system uses a **Haar Cascade Classifier** to localize the user's face in a 2D coordinate plane. By calculating the offset from the screen's center-point, the script triggers system interrupts:
* **Left Lean:** Decrements System Volume.
* **Right Lean:** Increments System Volume.
* **Deadzone Logic:** Prevents jitter by establishing a central "Neutral Zone."

## Technical Stack
* **Language:** Python 3.13
* **Library:** OpenCV (Computer Vision)
* **OS Bridge:** AppleScript (via `os.system`) for native macOS hardware control.
* **Framework:** Haar Cascade Frontal Face Topology.

---

## Technical Challenge & Solution
**The Challenge:** Standard automation libraries like `PyAutoGUI` often face permission sandboxing in modern macOS environments, preventing keyboard simulation.

**The Solution:** I implemented a native **AppleScript bridge** to talk directly to the macOS core audio framework. This bypassed the accessibility layer and ensured 100% reliability without compromising system security.

---

## Use Cases
1. **Accessibility:** Hands-free control for users with limited mobility.
2. **Productivity:** Controlling media during activities (cooking, exercising) where touching the device is impractical.
3. **HCI Research:** Prototyping non-traditional human-computer interfaces.

---

## Demonstration

![ScreenRecording2025-12-23at3 44 30PM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/ff14d003-0754-4aee-8f9c-0f8e5dc34704)


