

https://github.com/user-attachments/assets/23ffbe8f-64e8-414c-8590-a02c0689bf49

![Screenshot 2025-03-13 125619](https://github.com/user-attachments/assets/b817d364-fc82-4133-a018-1474e27da821)
![Screenshot 2025-03-13 125534](https://github.com/user-attachments/assets/6d7236dc-1656-47a3-8270-8bb4bbc9c02c)
![Screenshot 2025-03-13 125505](https://github.com/user-attachments/assets/ddee29e1-bcdb-43c9-b261-93b92c2f238b)
![Screenshot 2025-03-13 125436](https://github.com/user-attachments/assets/1f93d675-32a2-4990-9bb2-a971c37117ee)
# 👤 Face Recognition System

A comprehensive face recognition system built with Python, OpenCV, and Tkinter that allows for face detection, training, and recognition.

## 🌟 Features

- 🔍 Face Detection and Recognition
- 📚 Training Data Management
- 🖥️ User-friendly GUI Interface
- ⚡ Real-time Face Recognition
- 💾 Database Integration (MySQL)
- 👥 Multiple User Support
- 📊 Attendance Tracking
- 🔒 Secure Authentication

## 🛠️ Prerequisites

Before running this project, make sure you have the following installed:

- 🐍 Python 3.x
- 📸 OpenCV (`cv2`)
- 🖼️ PIL (Python Imaging Library)
- 🗄️ MySQL Connector
- 🎯 Tkinter (usually comes with Python)

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/rohitbansal2005/Face-Recognition-Attendance-System-Software
```

2. Install the required packages:
```bash
pip install opencv-python
pip install pillow
pip install mysql-connector-python
pip install numpy
```

3. Set up your MySQL database and update the connection details in the code.

## 📁 Project Structure

```
Face Recognition System/
├── Data/                  # Directory for storing face images
├── college_images/        # Directory for UI images
├── train.py              # Training module
├── face_recognition.py   # Main recognition module
├── face_detector.py      # Face detection module
└── README.md
```

## 🔄 System Flow Diagram

```mermaid
graph TD
    A[Start] --> B[Initialize System]
    B --> C{User Selection}
    C -->|Training| D[Load Training Data]
    C -->|Recognition| E[Start Camera]
    D --> F[Process Images]
    F --> G[Train Classifier]
    G --> H[Save Model]
    E --> I[Face Detection]
    I --> J[Face Recognition]
    J --> K[Database Update]
    K --> L[Display Results]
    H --> M[End]
    L --> M
```
🚀 Usage Guide
Step 1: Start the Application
1.Run the main application:

```bash
python login.py
```
2.The system will open the Login Interface.

Step 2: Register Users
After logging in, navigate to the Registration Interface:
-The registration module allows you to add new users to the system.

Step 3: Capture Photos for Face Recognition
1.Open the Student Management System Interface.
2.Use the Photo Sample option to capture images of the user's face:
-These photos will be stored in the Data directory for training.

Step 4: Train the System
1.Run the training module:

```bash
python train.py
```
2.Click on the "TRAIN DATA" button to process all the captured images and train the classifier.

Step 5: Perform Face Recognition
1.Once training is complete, proceed to the Face Recognition Interface:
-This interface allows real-time face recognition using the trained classifier.

2. Use the interface to:
   - 📸 Capture new face images
   - 🎓 Train the system
   - 🔍 Perform face recognition
   - 📊 View attendance records

## 💾 Database Setup

1. Create a MySQL database
2. Update the database connection details in the code
3. The system will automatically create necessary tables

### Database Schema

```sql
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    department VARCHAR(50),
    face_id INT
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    date DATE,
    time TIME,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);
```

## 🔧 Technical Details

### Face Detection Process
1. Image Capture
2. Grayscale Conversion
3. Face Detection using Haar Cascade
4. Face Region Extraction

### Recognition Algorithm
- LBPH (Local Binary Pattern Histogram) Face Recognition
- Feature Extraction
- Pattern Matching
- Confidence Score Calculation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- OpenCV for face detection and recognition capabilities
- MySQL for database management
- Tkinter for GUI development

## ❓ Support

For support, please open an issue in the repository or contact the maintainers.

## 📞 Contact

- 📧 Email: rohitbansal.dev@gmail.com
  
## 📝 Version History

- v1.0.0 - Initial Release
- v1.1.0 - Added Attendance Tracking
- v1.2.0 - Enhanced UI/UX
- v1.3.0 - Added Real-time Recognition

## 🔒 Security Considerations

- Secure storage of face data
- Encrypted database connections
- Access control implementation
- Regular security updates

## 🌐 System Requirements

- Windows 10/11 or Linux
- 4GB RAM minimum
- 2GB free disk space
- Webcam with 720p resolution minimum
