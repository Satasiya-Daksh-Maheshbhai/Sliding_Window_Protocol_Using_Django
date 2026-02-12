# 📡 Sliding Window Protocol

This repository contains the implementation and simulation of Sliding Window Protocols used in Computer Networks for reliable data transmission.

The project includes:

### Stop & Wait ARQ

### Go-Back-N ARQ

### Selective Repeat ARQ

# 📖 Introduction

Sliding Window Protocol is a technique used for flow control and error control in data communication.

It allows multiple frames to be sent before receiving acknowledgments, which improves transmission efficiency.

This project demonstrates how different ARQ (Automatic Repeat reQuest) protocols work and how they handle frame loss and retransmission.

# 🚀 Protocols Implemented
## 1️⃣ Stop & Wait ARQ

Sender sends one frame at a time.

Waits for acknowledgment (ACK).

If ACK is not received within time, the frame is retransmitted.

Simple but less efficient.

## 2️⃣ Go-Back-N ARQ

Sender can send multiple frames within a given window size.

Uses cumulative acknowledgment.

If one frame is lost, all frames after that frame are retransmitted.

More efficient than Stop & Wait.

## 3️⃣ Selective Repeat ARQ

Sender sends multiple frames within window size.

Receiver stores out-of-order frames.

Only the lost frame is retransmitted.

Most efficient among the three protocols.

# 🎯 Objectives

Understand the working of Sliding Window Protocol.

Compare Stop & Wait, Go-Back-N, and Selective Repeat.

Study frame transmission and retransmission process.

Analyze efficiency differences between protocols.

# 📊 Comparison Table
Protocol	Window Size	Retransmission Method	Efficiency	Complexity
Stop & Wait	1	One frame at a time	Low	Simple
Go-Back-N	N	Retransmit from lost frame onward	Medium	Moderate
Selective Repeat	N	Retransmit only lost frame	High	Complex

# 🛠️ Applications

Reliable data transmission in networks

Basis of TCP communication

Error control mechanisms

Academic and practical networking projects

# 💻 How to Run
## Step 1: Clone the Repository
git clone https://github.com/your-username/sliding-window-protocol.git

## Step 2: Navigate to the Project Folder
cd minictp

## Step 3: Run the Program
python manage.py runserver

# 📚 Concepts Covered

ARQ (Automatic Repeat reQuest)

Flow Control

Error Control

Acknowledgment Handling

Frame Loss Detection

Sliding Window Mechanism

# 🏁 Conclusion

This project helps in understanding how Sliding Window Protocols ensure reliable data transmission. It clearly shows the working, retransmission strategy, and efficiency differences between Stop & Wait, Go-Back-N, and Selective Repeat protocols.
