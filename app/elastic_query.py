import requests
from config import ELASTIC_SEARCH_ENDPOINT, TIME_WINDOW_MINUTES, THRESHOLD
from datetime import datetime

def build_query():
    return {
        "size": 0,
        "query": {
            "range": {
                "start_time": {
                    "gte": f"now-{TIME_WINDOW_MINUTES}m",
                    "lte": "now"
                }
            }
        },
        "aggs": {
            "phone_numbers": {
                "terms": {
                    "field": "from.keyword",
                    "size": 100
                },
                "aggs": {
                    "call_count_filter": {
                        "bucket_selector": {
                            "buckets_path": {"callCount": "_count"},
                            "script": f"params.callCount > {THRESHOLD}"
                        }
                    },
                    "top_account": {
                        "top_hits": {
                            "size": 1,
                            "_source": ["account_sid"],
                            "sort": [{"start_time": {"order": "desc"}}]
                        }
                    }
                }
            }
        }
    }

def fetch_breaches():
    response = requests.post(ELASTIC_SEARCH_ENDPOINT, json=build_query())
    if response.status_code != 200:
        raise Exception(f"Elastic error {response.status_code}: {response.text}")

    buckets = response.json().get("aggregations", {}).get("phone_numbers", {}).get("buckets", [])

    return [
        {
            "phone": b.get("key"),
            "calls": b.get("doc_count"),
            "account_sid": (
                b.get("top_account", {})
                 .get("hits", {})
                 .get("hits", [{}])[0]
                 .get("_source", {})
                 .get("account_sid", "Unknown")
            )
        }
        for b in buckets
    ]