from typing import Dict, Any

def process_query(natural_query: str) -> Dict[str, Any]:
    query = natural_query.lower()
    
    # Basic keyword matching
    if "sales" in query and "last week" in query:
        pseudo_sql = "SELECT * FROM sales WHERE date BETWEEN '2023-11-20' AND '2023-11-27'"
    elif "total sales by region" in query:
        pseudo_sql = "SELECT region, SUM(amount) FROM sales GROUP BY region"
    else:
        pseudo_sql = "SELECT * FROM sales LIMIT 10"  # Default
    
    return {
        "query": natural_query,
        "pseudo_sql": pseudo_sql,
        "confidence": 0.85,  # Mock confidence score
    }