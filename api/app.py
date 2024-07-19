from flask import Flask, request, jsonify
from googlesearch import search

app = Flask(__name__)

@app.route('/api/search', methods=['GET'])
def search_api():
    query = request.args.get('query')
    num_results = int(request.args.get('num_results', 10))  # Default to 10 results
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    results = []
    for result in search(query, num_results=num_results):
        results.append(result)
    
    return jsonify({"query": query, "results": results})

if __name__ == "__main__":
    app.run()
