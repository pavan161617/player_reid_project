# ⚽ AI-Powered Player Re-Identification in Sports Video  
> Real-time Multi-Player Tracking & Re-ID from a Single Static Camera Feed

This project enables **real-time player detection, tracking, and re-identification** in a soccer video using a custom-trained **YOLOv11 model** and the **Deep SORT** tracking algorithm. It ensures that players who leave and re-enter the frame are consistently assigned the same ID.

---

## 🚀 Project Overview

- 🎯 **Goal**: Assign consistent player IDs across frames, even after temporary disappearance.  
- 🧠 **Tech Stack**: YOLOv11 (object detection) + Deep SORT (tracking with re-ID).  
- 📦 **Input**: 15-second soccer video.  
- 📽️ **Output**: Processed video with bounding boxes and player IDs.

---

## 🗂️ Project Structure

```
player_reid_project/
├── main.py                  # Main tracking script
├── model/
│   └── yolov11.pt           # YOLOv11 weights (download separately)
├── videos/
│   └── 15sec_input_720p.mp4 # Input soccer video
├── output/
│   └── reid_output.mp4      # Output video with tracking
├── requirements.txt         # Required Python libraries
└── README.md                # Documentation
```

---

## ⚙️ Setup Instructions

### ✅ Step 1: Create & Activate Virtual Environment

```bash
python -m venv venv
# Activate (Windows):
venv\Scripts\activate
# Activate (macOS/Linux):
source venv/bin/activate
```

### ✅ Step 2: Install Dependencies

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

## 📥 Download Required Files

- **YOLOv11 Model Weights**  
  📎 [Download yolov11.pt](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)  
  ➤ Save it as: `model/yolov11.pt`

- **Video File**  
  ➤ Place `15sec_input_720p.mp4` inside the `videos/` folder.

---

## ▶️ Run the Tracker

```bash
python main.py
```

🔍 What happens:
- Loads YOLOv11 and Deep SORT  
- Detects players and assigns consistent IDs  
- Renders bounding boxes + IDs on each frame  
- Outputs the result to `output/reid_output.mp4`  
- Press `Q` to stop early

---

## 📈 Features at a Glance

| Feature              | Description                                                       |
|----------------------|-------------------------------------------------------------------|
| ✅ Re-ID Support      | Players retain the same ID even after exiting and re-entering     |
| ⚡ Real-Time Tracking | YOLOv11 + Deep SORT = Fast and Accurate                           |
| 🧠 Appearance Matching| Tracks players using color/embedding features                     |
| 💡 Simple Interface   | One-command run: `python main.py`                                 |

---

## 🔧 Under the Hood

### 🔸 YOLOv11 Detector
- Fine-tuned for footballer detection  
- High precision, low latency  
- Detects player & ball classes

### 🔹 Deep SORT Tracker
- Combines motion + visual embeddings  
- Re-identifies players using cosine similarity  
- Maintains identity during occlusions

---

## 🎥 Sample Output

- 📂 Output saved as `output/reid_output.mp4`  
- 🎯 Players retain consistent IDs across frames  
- 🔖 Visualized using bounding boxes + ID tags

---

## 🛠️ Troubleshooting

### ❌ `'Detect' object has no attribute 'grid'`

This usually happens when using an outdated method to load the model.

✅ Fix:

```python
from ultralytics import YOLO
model = YOLO('model/yolov11.pt')
```

✔️ Also, ensure you have `ultralytics >= 8.0.0`.

---

## 🚀 Future Enhancements

- 🌐 Add cross-camera re-identification  
- 📊 Export player logs (ID + frame + position)  
- 🖥️ Build a Streamlit/Flask dashboard  
- 📺 Enable webcam/live stream support  
- 🐳 Provide Docker container setup

---

## 👤 Author

**Pavan Kumar**  
🎓 B.Tech CSE (AI), Pragati Engineering College  
🌐 GitHub: [pavan161617](https://github.com/pavan161617)  
🔗 LinkedIn: [pavan-kumar](https://www.linkedin.com/in/pavan-kumar-b7639125a/)  
📧 Email: [pavan90990@gmail.com](mailto:pavan90990@gmail.com)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to fork, contribute, and share with attribution.

---

## ⭐ Like This Project?

If you found this useful:

- ⭐ Star it on GitHub  
- 🔄 Fork it and build on it  
- 💬 Share feedback and open issues

> “AI in sports is not the future — it’s the **present**. Let’s build smarter analytics together.”
