## Getting Started

### 1. Prerequisites
- Python 3.14 or higher
- Elasticsearch 9.x running separately (default: http://localhost:9200)

### 2. Clone the repository
```
git clone <repository-url>
cd lucerna
```

### 3. Create and activate a virtual environment
```
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Windows (cmd)
venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Verify Elasticsearch is running
```
curl.exe -k http://localhost:9200
```
You should get back a JSON response with cluster info.

### 6. Run the server
```
uvicorn app.main:app --reload
```

### 7. Verify the API
- Health check: http://localhost:8000
- Swagger docs: http://localhost:8000/docs
- Example: create a collection
```
curl -X POST http://localhost:8000/collections -H "Content-Type: application/json" -d "{\"group_id\": \"acme\", \"collection_id\": \"shopping\", \"fields\": {\"name\": \"text\", \"price\": \"float\"}}"
```