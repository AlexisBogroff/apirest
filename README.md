# API REST

Cours d'introduction aux API REST

Effectué dans le cadre d'une mission pour LePont Formations.

1. Découverte des méthodes principales pour la construction et la consommation d'APIs
2. Méthodes complémentaires pour améliorer la sécurité de l'application

## Recommandations

### Pour aller plus loin
- Explorer les différents types de modifications de l'API : changements rompus, non rompus
- Connecter l'API à des bases de données via SQLAlchemy
- Configuration avancée des paramétrages de Flask
- Gérer la pagination pour ne pas renvoyer de trop gros volumes de données
- Tri et autres options de filtre dans le champ de requete ([OC](https://openclassrooms.com/fr/courses/6573181-adoptez-les-api-rest-pour-vos-projets-web/6825136-utilisez-les-fonctionnalites-avancees-des-endpoints))
- Traiter les cookies pour gérer les sessions utilisateurs
- Implémentation de WebSockets pour une communication bidirectionnelle en temps réel.
- Gestion des longs processus avec des requêtes asynchrones et des callbacks.
- Utilisation des GraphQL comme alternative ou complément aux REST APIs.
- Intégration de systèmes de cache distribué (par exemple, Redis) pour améliorer les performances.
- Mise en place de Webhooks pour permettre à l'API d'envoyer des notifications en temps réel.
- Intégration de solutions d'API Gateway pour la gestion des APIs (par exemple, Kong, Tyk).
- Utilisation de Docker et Kubernetes pour le déploiement et la gestion des API.
- Implémentation de HATEOAS (Hypermedia as the Engine of Application State) pour des APIs auto-découvrables.
- Utilisation de WebAssembly pour améliorer les performances côté client.
- Approfondissement sur les standards de sécurité comme OWASP pour les API.
- Mise en œuvre de la sécurisation des APIs avec des techniques avancées telles que les signatures numériques.
- Pratiques de conformité réglementaire (par exemple, GDPR) en ce qui concerne les APIs.
- Audits de sécurité réguliers et tests de pénétration des APIs.
- Gestion des secrets et des clés d'API de manière sécurisée.


### Bonnes Pratiques et Conseils
- Méthodes de dépréciation : planifier et informer les utilisateurs de la dépréciation de certaines fonctionnalités. Fournir également des guides de migrations vers les nouvelles fonctionnalités qui les substituent.
- Versionner lors de refontes majeures de l'API. Plusieurs méthodes : dans l'url, l'en-tête, via les paramètres de la requête.
- Utiliser des logiciels graphiques pour monitorer l'API (Postman) (monitoring, tracing, logging) pour surveiller et diagnostiquer les problèmes des APIs.
- Mettre en place limitation de taux d'utilisation de l'API
- Les participants du groupe de travail **Cigref** préconisent également plusieurs bonnes pratiques dans cette [démarche de servicisation du SI](https://www.cigref.fr/wp/wp-content/uploads/2020/11/Cigref-Rapport-Strategies-servicisation-SI-Transformation-offre-services-Novembre-2020.pdf) : 
    - Favoriser les standards de l’industrie & utiliser un cadre de référence
    - Définir collaborativement l’interface technique avant de l’implémenter
    - Définir des règles de design
    - Soigner la documentation
    - Soutenir et acculturer les équipes
    - Faire preuve de pragmatisme
    - Mettre en place la gouvernance des APIs
    - S’appuyer sur une solution d’API management
- Suivre les guidelines et bonnes pratiques recommandées ici
  - [Microsoft API REST Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md) and [API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
  - [Checklist for designing REST API](https://mathieu.fenniak.net/the-api-checklist/) (recommandations de Microsoft)
- **Ne pas trop découpler trop tôt** : [conf 2023 Julien Topçu](https://www.youtube.com/watch?v=VO6BSb52K5g). Il faut trouver le juste équilibre de manière dynamique. Car au début il n'y a pas assez de contraintes pour connaitre les limites et donc où il faut découpler et où il ne faut pas. Il est aussi problématique d'avoir à gérer un programme complètement couplé qu'un ensemble de micro services complètement découplés.
- Utiliser **OAuth 2.1**
- [Bonnes pratiques concernant la gestion des Tokens d'accès](https://auth0.com/docs/secure/tokens/token-best-practices): définir une date d'expiration
- Gérer les surcharges de l'API (pour ne pas souffrir comme OpenDomesday)
- Utiliser l'asynchrome lorsque nécessaire
- Maintenir une documentation à jour avec Swagger
- Gérer les erreurs
- Séparer l'API en fichiers cohérents (main, fonctions, paramètres, etc.)
- Ecrire un code clair, lisible, facile à comprendre et maintenir à plusieurs
- Maintenir les versions sur un VCS (version control system) comme **Git**
- Créer des tests unitaires, faire de sorte à couvrir l'essentiel des parties sensibles et principales de l'API
- Automatiser le lancement des tests lors de l'intégration de nouvelles features (via Github par exemple)
- Se protéger contre les attaques cyber classiques (DDoS, SQL injection)
- Principes de l'API First Design : commencer par la conception de l'API avant le développement.
- Utilisation de patterns de conception pour les APIs, comme le modèle CQRS (Command Query Responsibility Segregation).
- Mesures de performance et tuning des APIs pour gérer des charges élevées.


### Ressources complémentaires
Ressource collaborative de cours sur HTTP, API REST [MDN](https://github.com/mdn):
- [HTTP cours](https://developer.mozilla.org/fr/docs/Web/HTTP/Overview)
  - [Ressources](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web)
  - [Type MIME](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_Types)
  - [Sécurité](https://developer.mozilla.org/fr/docs/Web/HTTP/CSP)
  - [Authentification](https://developer.mozilla.org/fr/docs/Web/HTTP/Authentication)
  - [Status code](https://developer.mozilla.org/fr/docs/Web/HTTP/Status)
  - [Headers HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers)
  - [HTTP headers](https://github.com/for-GET/know-your-http-well/blob/master/headers.md)
  - [HTTP Requests methods](https://github.com/for-GET/know-your-http-well/blob/master/methods.md)
  - [HTTP Status codes](https://github.com/for-GET/know-your-http-well/blob/master/status-codes.md)
  - [Caching](https://datatracker.ietf.org/doc/html/rfc7234)
  - [Authentification](https://datatracker.ietf.org/doc/html/rfc7235)
- [Gateway pour rate limit](https://konghq.com/products/kong-gateway)
- [Github API](https://docs.github.com/en/rest/repos?apiVersion=2022-11-28#create)
- [Exemple doc stylée - Stripe](https://stripe.com/docs/api)
- [Les API pour les nuls](https://www.ibm.com/cloud-computing/API_pour_les_nuls_WSM14025FRFR_3_of_5.pdf)

- [Standards REST](https://standards.rest/)
- [RFCs IETF](https://webconcepts.info/specs/IETF/RFC/)
- [Checklist for designing REST API](https://mathieu.fenniak.net/the-api-checklist/) (recommandé par Microsoft)
- [Google API Guidelines](https://google.aip.dev/)

- [Git repo list related to flask](https://github.com/mjhea0/awesome-flask)
- [Flask API documentation](https://flask.palletsprojects.com/en/3.0.x/api/)
- Création d'APIs [Flask-restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
- [API REST Flask revenus](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- [API REST Flask simple](https://pythonbasics.org/flask-rest-api/) 
- [Flask login easy](https://pythonbasics.org/flask-login/)
- [Flask complet](https://realpython.com/flask-connexion-rest-api/)