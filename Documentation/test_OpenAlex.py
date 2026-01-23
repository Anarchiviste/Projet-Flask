from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/reconcile", methods=["GET", "POST"])
def reconcile():
    q = request.args.get("query") or request.json.get("query")
    
    # Appel à OpenAlex
    response = requests.get(
        "https://api.openalex.org/authors",
        params={"search": q, "per-page": 5}
    ).json()
    
    # Transformer la réponse
    results = []
    for author in response.get("results", []):
        results.append({
            "id": author["id"],        # identifiant OpenAlex
            "name": author["display_name"],
            "score": 100,              # tu peux calculer un vrai score
            "match": True
        })
    
    return jsonify({"result": results})

if __name__ == "__main__":
    app.run(port=5000)
