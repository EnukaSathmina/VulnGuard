def analyze_vulnerability(vuln_type: str):

    data = {
        "XSS": {
            "description": "Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by users.",
            "fix": "Sanitize input, escape HTML output, use Content-Security-Policy (CSP).",
            "risk": "HIGH"
        },

        "SQL Injection": {
            "description": "SQL Injection allows attackers to manipulate database queries through user input.",
            "fix": "Use parameterized queries, prepared statements, and ORM frameworks.",
            "risk": "CRITICAL"
        },

        "ERROR": {
            "description": "General error detected in request/response flow.",
            "fix": "Check backend handling and validate inputs properly.",
            "risk": "MEDIUM"
        },

        "INFO": {
            "description": "Informational result, no direct vulnerability confirmed.",
            "fix": "No action required, but monitor behavior.",
            "risk": "LOW"
        }
    }

    return data.get(vuln_type, {
        "description": "Unknown vulnerability type.",
        "fix": "Manual review required.",
        "risk": "UNKNOWN"
    })