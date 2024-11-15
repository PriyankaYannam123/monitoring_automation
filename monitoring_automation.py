import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='monitoring.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_service_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f"Service is UP: {url}")
        else:
            logging.warning(f"Service DOWN with status {response.status_code}: {url}")
    except Exception as e:
        logging.error(f"Error connecting to {url}: {e}")

def log_metrics(metric_name, value):
    logging.info(f"{metric_name}: {value}")

if __name__ == "__main__":
    # Example URL to monitor
    service_url = 'https://example.com/health-check'
    check_service_status(service_url)

    # Example metrics
    cpu_usage = 75  # Example value
    log_metrics("CPU Usage", f"{cpu_usage}%")
