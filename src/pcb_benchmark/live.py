"""Live-data helpers: all keyless, with cached fallback for offline reproducibility."""
import json, time, urllib.parse, urllib.request

HEADERS = {"User-Agent": "pcb-benchmark/1.0 (research; contact: research.local)",
           "Accept": "application/json"}

def get_json(url, timeout=20):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "ignore"))

def openalex_count(query, per_page=5):
    q = urllib.parse.quote(query)
    url = f"https://api.openalex.org/works?search={q}&per-page={per_page}&select=id,title,publication_year,cited_by_count,doi"
    try:
        j = get_json(url)
        return {"total": j["meta"]["count"], "sample": [
            {"title": w.get("title"), "year": w.get("publication_year"),
             "cited": w.get("cited_by_count"), "doi": w.get("doi")}
            for w in j["results"]]}
    except Exception as e:
        return {"total": None, "error": str(e)[:200], "sample": []}

def crossref_count(query, rows=5):
    q = urllib.parse.quote(query)
    url = f"https://api.crossref.org/works?query={q}&rows={rows}&select=title,published,DOI,is-referenced-by-count"
    try:
        j = get_json(url)
        items = j["message"]["items"]
        return {"total": j["message"]["total-results"], "sample": [
            {"title": (i.get("title") or [""])[0][:120], "doi": i.get("DOI")}
            for i in items]}
    except Exception as e:
        return {"total": None, "error": str(e)[:200], "sample": []}

def wikipedia_summary(title):
    t = urllib.parse.quote(title)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{t}"
    try:
        return get_json(url)
    except Exception as e:
        return {"error": str(e)[:200]}

def github_repo(owner_repo):
    url = f"https://api.github.com/repos/{owner_repo}"
    try:
        return get_json(url)
    except Exception as e:
        return {"error": str(e)[:200]}

def stackexchange_tagged(tag, pagesize=10):
    q = urllib.parse.quote(tag)
    url = (f"https://api.stackexchange.com/2.3/questions?order=desc&sort=creation"
           f"&tagged={q}&site=stackoverflow&pagesize={pagesize}")
    try:
        return get_json(url)
    except Exception as e:
        return {"error": str(e)[:200], "items": []}

def worldbank_indicator(country="GBR", indicator="SE.TER.ENRR"):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=10"
    try:
        return get_json(url)
    except Exception as e:
        return {"error": str(e)[:200]}
