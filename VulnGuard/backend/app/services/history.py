scan_history = []

stats = {
    "total_scans": 0,
    "xss": 0,
    "sqli": 0,
    "info": 0
}


def reset_stats():
    global stats, scan_history
    stats = {"total_scans": 0, "xss": 0, "sqli": 0, "info": 0}
    scan_history = []


def save_scan(url, results):
    global stats

    stats["total_scans"] += 1

    for r in results:

        rtype = r.get("type", "")

        if rtype == "XSS":
            stats["xss"] += 1

        elif rtype == "SQL Injection":
            stats["sqli"] += 1

        else:
            stats["info"] += 1

    scan_history.append({
        "url": url,
        "results": results
    })


def get_history():
    return scan_history


def get_stats():
    return stats