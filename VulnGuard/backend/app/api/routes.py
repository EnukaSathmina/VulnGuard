from fastapi import APIRouter
from app.services.crawler import crawl_website
from app.services.scanner import scan_url
from app.services.history import save_scan, get_stats, get_history, reset_stats

router = APIRouter()


@router.get("/")
def root():
    return {"message": "AI Vulnerability Scanner Running 🚀"}


@router.get("/crawl")
def crawl(url: str):
    return crawl_website(url)


@router.get("/scan")
def scan(url: str):

    crawl_data = crawl_website(url)

    results = []
    seen_global = set()  # 🔥 GLOBAL DEDUP

    if "links" in crawl_data:

        for link in crawl_data["links"]:

            scan_result = scan_url(link)

            for r in scan_result:

                key = f"{r['type']}-{r['url']}"

                if key not in seen_global:
                    seen_global.add(key)
                    results.append(r)

    # 🔥 THIS WAS MISSING (CRITICAL)
    save_scan(url, results)

    return {
        "target": url,
        "issues_found": len(results),
        "details": results
    }


@router.get("/stats")
def stats():
    return get_stats()


@router.get("/history")
def history():
    return get_history()


@router.get("/reset")
def reset():
    reset_stats()
    return {"message": "stats reset"}