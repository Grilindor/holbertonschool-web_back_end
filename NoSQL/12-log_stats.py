#!/usr/bin/env python3
"""Analyse des logs Nginx stockés dans MongoDB."""

from pymongo import MongoClient

def main():
    """Affiche des statistiques sur les logs Nginx stockés dans MongoDB."""
    # Connexion à MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs  # Base de données "logs"
    collection = db.nginx  # Collection "nginx"

    # Étape 1 : Compter tous les documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Étape 2 : Afficher les statistiques des méthodes HTTP
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Étape 3 : Compter les requêtes GET pour le chemin /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
