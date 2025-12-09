# 🚀 Dockerized Real-Time Telemetry Dashboard

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## 📖 Overview

This project is a Proof of Concept (PoC) for a **real-time monitoring system**. It simulates an IoT/Network telemetry environment where synthetic data is generated, stored in a time-series database, and visualized instantly.

The system is fully containerized using **Docker**, ensuring consistency across different environments. It demonstrates an end-to-end data pipeline from generation to visualization.

### 🎯 Key Features
* **Data Simulation:** Python script generates random telemetry data (e.g., CPU load, Network Traffic, Temperature).
* **Container Orchestration:** All services run on Docker & Docker Compose.
* **Time-Series Storage:** High-performance data storage (**Prometheus**).
* **Visualization:** Custom Grafana dashboards for real-time analytics.

---

## 📸 Dashboard Preview

![Grafana Dashboard](<img width="1466" height="938" alt="Screenshot 2025-12-09 174322" src="https://github.com/user-attachments/assets/d987965a-5511-432c-a3a0-eeced25bb54a" />
)

*Figure 1: Real-time visualization of the generated telemetry data.*

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Data Generator** | Python 3.9 | Simulates sensor/network data. |
| **Database** | Prometheus | Time-series database for storage. |
| **Visualization** | Grafana | Dashboard for monitoring metrics. |
| **Containerization** | Docker | Container platform. |
| **Orchestration** | Docker Compose | Multi-container management. |

---

## 📂 Project Structure

```text
realtime-monitoring/
├── app/
│   ├── main.py            # Python data generator script
│   └── requirements.txt   # Python dependencies
├── docker-compose.yml     # Service definitions
├── README.md              # Project documentation
└── .gitignore             # Ignored files
```

## 🚀 How to Run

### Prerequisites
* **Docker Desktop** installed on your machine.
* **Git**.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/eminekilic/docker-realtime-monitoring.git](https://github.com/eminekilic/docker-realtime-monitoring.git)
    cd repo-ismi
    ```

2.  **Start the services:**
    Run the following command to build and start the containers in detached mode:
    ```bash
    docker-compose up -d --build
    ```

3.  **Access the Dashboard:**
    * Open your browser and go to: `http://localhost:3000`
    * **Username:** `admin`
    * **Password:** `admin` (or as defined in your compose file)

4.  **Verify Data Flow:**
    The Python script will automatically start exposing metrics to Prometheus. You should see the graphs moving in real-time on Grafana.

---

## 🔮 Future Improvements
- [ ] Add alerting rules (e.g., Slack notification when CPU > 90%).
- [ ] Implement secure communication (HTTPS/SSL).
- [ ] Add more complex data patterns (Sine waves, spikes).
