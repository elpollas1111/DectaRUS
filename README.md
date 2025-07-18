
## Table of Contents

- [Overview](#overview)
- [Vulnerability Details](#vulnerability-details)
- [Proof of Concept (PoC)](#proof-of-concept-poc)
- [Environment Setup](#environment-setup)
- [Mitigation and Patching](#mitigation-and-patching)
- [Detection and Monitoring](#detection-and-monitoring)
- [References](#references)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)

---

## Overview

CVE-2025-25257 is a **pre-authentication SQL Injection vulnerability** in Fortinet FortiWeb Fabric Connector versions 7.0 through 7.6.x.  
This flaw allows attackers to inject malicious SQL commands into the vulnerable API endpoint, potentially leading to **Remote Code Execution (RCE)**.  

This repository contains an **educational Proof-of-Concept (PoC)** demonstrating the SQL injection vector in a safe and controlled manner.  
No destructive payloads or RCE exploits are included.  

---

## Vulnerability Details

- **Name:** FortiWeb Fabric Connector SQL Injection  
- **CVE:** [CVE-2025-25257](https://nvd.nist.gov/vuln/detail/CVE-2025-25257)  
- **Affected Versions:** FortiWeb Fabric Connector 7.0 through 7.6.x  
- **Severity:** Critical (CVSS Score 9.8)  
- **Impact:** Pre-authentication SQL Injection, leading to Remote Code Execution  
- **Attack Vector:** HTTP API `/api/fabric/device/status`  
- **Exploitation:** Requires malicious `Authorization: Bearer` header with crafted payload  

---

## Proof of Concept (PoC)

The following `curl` command demonstrates the **SQL Injection detection** without executing harmful payloads:

```bash
curl -k -H "Authorization: Bearer aaa' OR '1'='1" \
  https://<fortiweb-ip>/api/fabric/device/status
