# Hand Gesture Recognition using ESP8266 / ESP32 and Python

This project implements a real-time **Hand Gesture Recognition System** using the ESP8266/ESP32 microcontroller and a Python-based machine learning model. Sensor values are collected through the ESP device and transmitted wirelessly to Python, where gestures are classified using ML algorithms.

---

## 🚀 Features
- Real-time gesture recognition  
- Works with ESP8266 and ESP32  
- Wireless communication (WiFi / ESP-NOW)  
- Python-based ML classifier  
- Supports multiple gestures  
- Beginner-friendly and easily extendable  

---

## 🧠 Workflow Overview
1. ESP board collects sensor values  
2. Data sent wirelessly to Python  
3. Python preprocesses the data  
4. ML classifier predicts gesture  
5. Output displayed or used to control devices  

---

## 🛠️ Hardware Requirements
- ESP8266 / ESP32  
- Sensors (Flex sensors / IR / IMU depending on design)  
- Jumper wires  
- Power supply  

---

## 💻 Software Requirements
- Arduino IDE  
- Python 3  
- Libraries: NumPy, Scikit-learn, PySerial, Pandas  

---

## 📡 Data Transmission
The ESP board sends sensor values in JSON or CSV format through serial/WiFi. Python listens to the incoming data and processes it in real-time.

---

## 🧩 ML Model
A lightweight classifier (SVM / RandomForest / kNN) is trained using gesture samples. You can modify the model depending on your dataset.

---

## 🎯 Applications
- Gesture-controlled robotics  
- Smart home automation  
- Human–computer interaction  
- Assistive technology systems  
- Innovative IoT projects  

---

## 📽️ Demonstration
Video tutorial link: *Add your YouTube link here*

---

## 🤝 Contribute
Feel free to improve the ML model, add gestures, or enhance the communication layer.

---

## 📜 License
MIT License  
