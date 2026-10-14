A multi-modal biometric identity verification and automated attendance processing system designed for educational environments. It combines high-precision facial recognition with dual-layer voice verification to secure classroom check-ins, manage subjects, and process attendance logs seamlessly.

---

## 🚀 Core Features

- **Dual-Layer Biometric Pipelines:**
  - **Facial Recognition:** Built on `dlib`'s frontal face detector, 68-point shape predictors (`shape_predictor`), and `face_recognition_models` computing 128-dimensional face descriptors, classified via an optimized linear Support Vector Classifier (`sklearn.svm.SVC`).
  - **Voice Verification:** Utilizes `resemblyzer` and `librosa` to extract utterance embeddings, process audio segments, and perform robust cosine-similarity speaker matching.
- **Role-Based Portals:**
  - **Teacher Portal:** Secure authentication (with bcrypt password hashing), subject management modals, automated attendance dashboards, and custom class tracking.
  - **Student Portal:** Instant face-scanning attendance check-ins, automated profile registration with live camera feeds, and optional voice enrollment.
- **Interactive Streamlit UI:** Fully responsive dashboard layouts featuring custom HTML components, dialog workflows, dynamic tabs, and branded headers/footers.
- **Cloud Database Integration:** Powered by Supabase for secure relational data handling of students, teacher credentials, subjects, and attendance logs.

---

## 🛠️ Tech Stack

- **Frontend & UI:** Streamlit, PIL (Pillow), Custom HTML/CSS Components
- **Computer Vision & AI:** `dlib`, `face_recognition_models`, `OpenCV`, `scikit-learn` (SVC)
- **Audio Processing:** `resemblyzer`, `librosa`
- **Backend & Database:** Python, Supabase, `bcrypt`

---
## 🧠 How It Works

### 1. Facial Recognition Pipeline
1. **Detection & Alignment:** Captures live feed via Streamlit, detects face bounding boxes using `dlib`'s frontal detector, and extracts 68 facial landmarks.
2. **Descriptor Generation:** Passes landmarks into `dlib_face_recognition_model_v1` to generate a 128-dimensional vector embedding.
3. **Classification:** Uses a Support Vector Machine (`SVC`) with linear kernel and class weight balancing trained on student database embeddings to match faces with confidence thresholds.

### 2. Dual-Layer Voice Pipeline
1. **Audio Preprocessing:** Accepts recorded WAV audio, loads signals at 16kHz via `librosa`, and splits voice segments using non-silent audio detection (`top_db=30`).
2. **Speaker Verification:** Generates utterance embeddings via `resemblyzer.VoiceEncoder` and performs cosine similarity matching against registered voice signatures.

### 3. Smart Attendance Logging
- Once biometrics pass the similarity threshold ($>0.60$ for face, $>0.65$ for voice), attendance logs and unique session instances are automatically updated in the Supabase database.


## 📁 Project Architecture

```text
├── assets/                  # Logos, icons, and UI visual assets
├── src/
│   ├── components/          # Reusable UI elements (Headers, Footers, Cards, Dialogs)
│   ├── database/            # Database configurations and Supabase queries
│   ├── pipeline/            # Core AI pipelines (Face recognition & Voice embedding)
│   └── ui/                  # Layout styling and theme configurations
└── app.py / entry points    # Main application routers (Home, Student, Teacher screens)
