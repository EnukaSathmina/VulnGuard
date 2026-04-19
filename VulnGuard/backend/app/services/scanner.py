import requests

XSS_PAYLOAD = "<script>alert(1)</script>"
SQL_PAYLOAD = "' OR '1'='1"


def scan_url(url: str):

    if "?" not in url:
        return []

    results = []
    seen = set()

    try:
        base, query = url.split("?", 1)
        params = query.split("&")
        baseline = requests.get(url, timeout=10).text.lower()
    except:
        return [{
            "type": "ERROR",
            "url": url,
            "status": "Request failed"
        }]

    for p in params:

        if "=" not in p:
            continue

        key = p.split("=")[0]

        # ================= XSS =================
        try:
            test_url = f"{base}?{key}={XSS_PAYLOAD}"
            res = requests.get(test_url, timeout=10).text

            unique_key = f"XSS-{base}-{key}"

            if XSS_PAYLOAD in res:
                if unique_key not in seen:
                    seen.add(unique_key)
                    results.append({
                        "type": "XSS",
                        "url": test_url,
                        "status": "Reflected XSS detected"
                    })
        except:
            pass

        # ================= SQLi =================
        try:
            test_url = f"{base}?{key}={SQL_PAYLOAD}"
            res = requests.get(test_url, timeout=10).text.lower()

            unique_key = f"SQL-{base}-{key}"

            if any(x in res for x in ["sql", "mysql", "error", "syntax"]) or res != baseline:
                if unique_key not in seen:
                    seen.add(unique_key)
                    results.append({
                        "type": "SQL Injection",
                        "url": test_url,
                        "status": "Possible SQL injection"
                    })
        except:
            pass

    return results