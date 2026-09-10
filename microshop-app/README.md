# MicroShop — application de démo pour le TP GitLab CI / Kubernetes

Petite API Flask utilisée comme support du TP. Elle expose :

- `GET /` : message de bienvenue + version
- `GET /health` : endpoint de healthcheck (utilisé pour les probes Kubernetes)
- `GET /api/products` : liste de produits factices
- `GET /api/products/<id>` : détail d'un produit

## Lancer en local (sans Docker)

```bash
pip install -r requirements.txt
python app.py
# puis http://localhost:5000
```

## Lancer avec Docker

```bash
docker build -t microshop .
docker run -p 5000:5000 microshop
```

## Contenu du dépôt fourni aux apprenants

- `app.py`, `requirements.txt`, `Dockerfile` : l'application et son packaging
- `.gitlab-ci.yml` : le pipeline de départ (build + déploiement SSH), celui que les
  apprenants connaissent déjà — point de départ du TP
- `k8s/` : squelettes de manifestes Kubernetes incomplets pour la Partie 2 du TP
