📡 Sliding Window Protocol

This repository contains the implementation and simulation of Sliding Window Protocols used in Computer Networks for reliable data transmission.

The project includes:

✅ Stop & Wait ARQ

✅ Go-Back-N ARQ

✅ Selective Repeat ARQ

📖 Introduction

Sliding Window Protocol is a technique used for flow control and error control in data communication.

It allows multiple frames to be sent before receiving acknowledgments, improving efficiency compared to basic transmission methods.

This project demonstrates how different ARQ (Automatic Repeat reQuest) protocols work and how they handle frame loss and retransmission.

🚀 Protocols Implemented
1️⃣ Stop & Wait ARQ

Sender sends one frame at a time.

Waits for acknowledgment (ACK).

If ACK is not received, frame is retransmitted.

Simple but low efficiency.

2️⃣ Go-Back-N ARQ

Sender can send multiple frames within a window size.

If one frame is lost, all frames after it are retransmitted.

Uses cumulative acknowledgment.

More efficient than Stop & Wait.

3️⃣ Selective Repeat ARQ

Sender sends multiple frames.

Only the lost frame is retransmitted.

Receiver stores out-of-order frames.

Highest efficiency among the three.

🎯 Objectives

To understand working of sliding window protocols.

To compare Stop & Wait, Go-Back-N, and Selective Repeat.

To study retransmission mechanisms.

To analyze protocol efficiency.

📊 Comparison Table
Protocol	Window Size	Retransmission	Efficiency	Complexity
Stop & Wait	1	One frame at a time	Low	Simple
Go-Back-N	N	Retransmit from lost frame onward	Medium	Moderate
Selective Repeat	N	Only lost frame	High	Complex
🛠️ Applications

Reliable data transmission

Network communication systems

TCP protocol understanding

Academic and practical learning
