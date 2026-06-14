import streamlit as st
import os
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

# Configuration de la page
st.set_page_config(page_title="AI Financial Agent", page_icon="💼", layout="centered")

st.title("💼 Assistant Financier IA - Startups Tunisiennes")
st.write("Posez vos questions financières en langage naturel à notre Agent intelligent.")

# Sécurité : On demande la clé Groq à l'utilisateur pour ne pas exposer la tienne
api_key = st.text_input("🔑 Entrez votre clé API Groq (gsk_...) :", type="password")

if api_key:
    os.environ["GROQ_API_KEY"] = api_key
    
    # Chargement des données (on simule le CSV directement dans le code pour éviter les erreurs de fichier manquant)
    data_tunisie = """Date,Categorie,Sous_Categorie,Montant_TND,Description
2026-01-01,Revenus,Abonnements_SaaS,12450.00,Renouvellement abonnements clients tunisiens
2026-01-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-01-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-01-10,Depenses,Marketing,-1500.00,Campagne Facebook Ads & LinkedIn Ads
2026-01-15,Depenses,Technologie,-650.00,Facture AWS Serveurs (via Carte Tech)
2026-01-20,Depenses,Admin_Locaux,-1200.00,Loyer bureau au Coworking Space Lac 2
2026-02-01,Revenus,Abonnements_SaaS,14200.00,Nouveaux clients + abonnements mensuels
2026-02-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-02-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-02-12,Depenses,Marketing,-2100.00,Sponsoring evenement tech à Tunis
2026-02-15,Depenses,Technologie,-710.00,Facture AWS Serveurs et outils Dev
2026-03-01,Revenus,Abonnements_SaaS,11100.00,Chute legere - Churn de deux clients PME
2026-03-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-03-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-03-10,Depenses,Marketing,-1200.00,Growth Hacking et contenu SEO
2026-03-15,Depenses,Technologie,-680.00,Facture AWS Serveurs
2026-03-25,Depenses,Admin_Frais,-450.00,Frais comptable et juridique de la startup
2026-04-01,Revenus,Abonnements_SaaS,18900.00,Forte croissance - Signature grand compte
2026-04-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-04-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-04-05,Depenses,RH_Salaires,-1800.00,Recrutement d un stagiaire de fin d etudes payé + UI Designer
2026-04-10,Depenses,Marketing,-3500.00,Budget Ads augmenté pour cibler le marché MENA
2026-04-15,Depenses,Technologie,-920.00,Facture AWS suite à la hausse de trafic
2026-05-01,Revenus,Abonnements_SaaS,22400.00,Revenus recurrents en croissance
2026-05-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-05-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-05-05,Depenses,RH_Salaires,-1800.00,Salaire UI Designer Freelance
2026-05-15,Depenses,Technologie,-950.00,Facture AWS et abonnements Slack/Notion
2026-05-20,Depenses,Marketing,-1500.00,Campagne Retargeting
2026-06-01,Revenus,Abonnements_SaaS,25100.00,Cloture du semestre en hausse
2026-06-05,Depenses,RH_Salaires,-4500.00,Salaire Developpeur Senior Fullstack
2026-06-05,Depenses,RH_Salaires,-2200.00,Salaire Data Analyst Junior
2026-06-05,Depenses,RH_Salaires,-1800.00,Salaire UI Designer Freelance
2026-06-15,Depenses,Technologie,-990.00,Facture serveurs mensuelle"""
    
    # On recrée temporairement le fichier pour l'agent
    with open("finance.csv", "w") as f:
        f.write(data_tunisie)
        
    df = pd.read_csv("finance.csv")
    
    # Initialisation de l'IA et de l'agent
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True, max_iterations=2)
    
    # Zone d'interrogation
    question = st.text_input("Posez votre question à l'agent (Ex: Quel est le total des dépenses RH ?) :")
    
    if st.button("🤖 Interroger l'agent"):
        if question:
            with st.spinner("L'agent analyse les données financières..."):
                try:
                    # On force une consigne simple en arrière-plan pour éviter les hallucinations textuelles
                    reponse = agent.invoke({"input": question + " Donne uniquement une réponse factuelle basée sur le résultat du code."})
                    st.markdown("### 📊 Résultat de l'analyse :")
                    st.info(reponse['output'])
                except Exception as e:
                    st.error(f"Une erreur est survenue lors de l'analyse : {e}")
else:
    st.warning("⚠️ Veuillez entrer votre clé API Groq pour activer l'assistant financier.")
