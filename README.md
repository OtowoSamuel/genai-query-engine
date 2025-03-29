# GenAI Query Engine

## 🔌 Setup (Local Development)

```bash
# 1. Clone repo
git clone https://github.com/your-username/genai-query-engine.git
cd genai-query-engine

# 2. Install dependencies
python -m venv venv
source venv/bin/activate  # Linux/Mac: venv\Scripts\activate (Windows)
pip install -r requirements.txt

# 3. Run
uvicorn app.main:app --reload
```

### 🐳 Using Docker
You can use the Docker file too:

```bash
# Build the Docker image
docker build -t genai-query-engine .

# Run the container
docker run -p 8000:8000 genai-query-engine
```

## 🌐 Live Deployment
**Base URL:**  
[https://genai-query-engine-production.up.railway.app](https://genai-query-engine-production.up.railway.app)

## 🔑 Authentication
**Get JWT token:**

```bash
curl -X POST "https://genai-query-engine-production.up.railway.app/login?username=demo&password=demo123"
```

**Use token in headers:**

```text
Authorization: Bearer <your_token>
```

## 📡 API Endpoints

### 1. Process Query (`/query`)

**Request:**

```bash
curl -X POST https://genai-query-engine-production.up.railway.app/query \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"sales last week"}'
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "query": "sales last week",
    "pseudo_sql": "SELECT * FROM sales WHERE date BETWEEN '2023-11-20' AND '2023-11-27'",
    "confidence": 0.85
  }
}
```

### 2. Explain Query (`/explain`)

```bash
curl -X POST https://genai-query-engine-production.up.railway.app/explain \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"total by region"}'
```

### 3. Validate Query (`/validate`)

```bash
curl -X POST https://genai-query-engine-production.up.railway.app/validate \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":""}'
```

## 🧪 Testing Samples

| Query Type  | Example Input      | Expected SQL Output                |
|------------|------------------|----------------------------------|
| Time-based | "sales last week" | `SELECT ... WHERE date BETWEEN...` |
| Grouping   | "total by region" | `SELECT region, SUM(amount) FROM... GROUP BY` |
| Default    | "show products"   | `SELECT * FROM sales LIMIT 10` |

## 🚨 Error Handling

| Code | Scenario            | Response Example                     |
|------|--------------------|---------------------------------|
| 400  | Malformed query     | `{"detail": "Query parsing failed"}` |
| 401  | Invalid/missing token | `{"detail": "Could not validate credentials"}` |
| 422  | Validation error     | `{"detail": "Field required"}` |

