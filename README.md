# ⚽ Player Re-Identification from Single Video Feed

This project implements **real-time player tracking and re-identification** using a 15-second soccer video. It ensures that each player maintains a **consistent ID**, even when they leave and re-enter the camera frame. The solution combines a fine-tuned **YOLOv11 object detection model** with the **Deep SORT** tracking algorithm.

---

## 🧠 Problem Statement

> **Objective**: Track and re-identify players in a single video feed such that players who go out of frame and return are consistently assigned the same ID.

---

## 🗂️ Project Structure

```
player_reid_project/
├── main.py                  # Main script to run tracking
├── model/
│   └── yolov11.pt           # Custom YOLOv11 model (downloaded separately)
├── videos/
│   └── 15sec_input_720p.mp4 # Input 15-second soccer video
├── output/
│   └── reid_output.mp4      # Output video with tracking results
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

### ✅ 1. Create Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### ✅ 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
ultralytics==8.0.230
opencv-python
deep_sort_realtime
numpy
matplotlib
seaborn
pandas
```

---

## ▶️ How to Run the Project

### 🔽 1. Download Files

- Download the YOLOv11 model from:  
  👉 [Google Drive Model Link](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)  
  ➤ Save it as: `model/yolov11.pt`

- Place the input video file `15sec_input_720p.mp4` inside the `videos/` folder.

---

### ▶️ 2. Run the Script

```bash
python main.py
```

What it does:
- Loads YOLOv11 and Deep SORT
- Detects and tracks players frame-by-frame
- Maintains consistent IDs for reappearing players
- Saves the output to `output/reid_output.mp4`

> ✅ Press `Q` in the preview window to stop early.

---

## 📊 Output

- 🎥 A video with consistent player IDs throughout  
- ✅ Players who leave and re-enter are re-identified  
- 📂 Output saved as: `output/reid_output.mp4`

---

## 🔍 Detection Model

- **YOLOv11**: A fine-tuned version of Ultralytics YOLO trained to detect players and the ball  
- **Deep SORT**: Tracker using object motion & appearance for re-identification

---

## 🛠️ Troubleshooting

### ❌ Error: `'Detect' object has no attribute 'grid'`

You're likely using `torch.hub.load(...)` from an old version.  
✅ Fix:

```python
from ultralytics import YOLO
model = YOLO('model/yolov11.pt')
```

Also ensure `ultralytics >= 8.0.0`.

---

## 🚀 Future Work

- Add support for **cross-camera re-identification**
- Web-based UI using **Streamlit** or **Flask**
- Export tracking logs (IDs + coordinates)
- Enable **live webcam** input

---

## 👨‍💻 Author

**Vinay Manda**  
🎓 Final Year – CSE (AI & ML)  
🏆 Google Arcade Champion | AWS Cloud Intern | Web & AI Developer  

📧 Email: [vinay456m@gmail.com](mailto:vinay456m@gmail.com)  
🔗 LinkedIn: [Vinay Manda](https://www.linkedin.com/in/vinay-manda-b6811725a/)  
🔗 GitHub: [github.com/Vinay1608m](https://github.com/Vinay1608m)

---

## 📄 License

This project is licensed under the **MIT License**.  
Use it freely with attribution.

---

⭐ If you found this project useful, give it a ⭐ on GitHub!