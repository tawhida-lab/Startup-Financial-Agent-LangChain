# 💼 Assistant Financier Intelligent pour Startup (Agentic AI)

Ce dépôt héberge une application d'**Agentic AI** capable d'analyser et de piloter les données financières d'une startup en langage naturel (Français). Conçu avec une architecture légère, ce projet valide la manipulation de données complexes via des agents autonomes sans infrastructure lourde.

## 🎮 Démo Live
🚀 **[Tester l'application sur Streamlit Cloud](https://share.streamlit.io/)** *(https://startup-financial-agent.streamlit.app/)*

---

## 🗺️ Architecture & Démarche Technique

Pour concevoir cet agent de production robuste et éliminer les instabilités natives des grands modèles de langage (LLM), le projet suit une méthodologie stricte en 5 étapes :

1. **Cadrage Métier :** Simulation d'un jeu de données financières calqué sur l'écosystème des startups (salaires en TND, frais technologiques cloud, revenus récurrents SaaS).
2. **Configuration des Outils (Tools) :** Intégration de l'outil d'exécution de code `python_repl_ast`, permettant à l'IA d'interagir dynamiquement avec les données.
3. **Optimisation du Moteur d'Inférence :** Connexion au modèle **Llama 3.3 (70B)** via l'API **Groq**, configuré avec une température de `0` pour garantir une rigueur mathématique absolue.
4. **Cadrage Système (Prompt Engineering) :** Conception d'instructions systèmes pour interdire à l'IA la génération de données fantômes (hallucinations) et la forcer à exploiter uniquement le DataFrame initial.
5. **Ceinture de Sécurité & Fiabilité :** Implémentation du paramètre `max_iterations=2` pour briser physiquement les boucles infinies de l'agent et isolation des flux de sortie de la console pour extraire des résultats financiers 100% fiables.

---

## 🛠️ Technologies Utilisées
* **Framework :** LangChain & LangChain Experimental
* **Moteur LLM :** Groq API (`llama-3.3-70b-versatile`)
* **Data Processing :** Pandas & Python 3.12
* **Interface Utilisateur :** Streamlit

---

## 🚀 Comment exécuter le projet en local ?

1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/tawhida-lab/Startup-Financial-Agent-LangChain.git](https://github.com/tawhida-lab/Startup-Financial-Agent-LangChain.git)
