import re

def detect_attempts(log_line):
    pattern = re.compile(r"Authorization: Bearer .*' OR '1'='1", re.IGNORECASE)
    if pattern.search(log_line):
        return True
    return False

if __name__ == "__main__":
    sample_logs = [
        "GET /api/fabric/device/status Authorization: Bearer aaa' OR '1'='1 HTTP/1.1",
        "GET /api/fabric/device/status Authorization: Bearer normaltoken HTTP/1.1",
    ]
    for line in sample_logs:
        if detect_attempts(line):
            print(f"[ALERT] Possible exploit attempt detected: {line}")
        else:
            print(f"[INFO] Clean log: {line}")
