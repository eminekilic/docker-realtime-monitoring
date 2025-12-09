from prometheus_client import start_http_server, Gauge
import time
import random

# --- 1. DEFINING METRICS ---
TRAFFIC_GAUGE = Gauge('network_traffic_bps', 'Real-time Traffic Speed (bps)')
RISK_GAUGE = Gauge('ai_risk_score', 'AI Risk Score (0-100)')

def main():
    # --- 2. START SERVER ---
    print("📢 Metrics Server is running on port 8000...")
    start_http_server(8000)

    while True:
        # --- 3. SIMULATE DATA ---
        real_bps = random.randint(1000, 5000000) 
        ai_score = random.random() * 100
        
        # --- 4. UPDATE METRICS ---
        TRAFFIC_GAUGE.set(real_bps)
        RISK_GAUGE.set(ai_score)
        
        print(f"Data updated -> Speed: {real_bps} bps, Risk: {ai_score:.2f}%")
        time.sleep(2)

if __name__ == '__main__':
    main()