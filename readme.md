# 🎣 OPENSCRAPER

## 📋 SOMMAIRE
- [INTRODUCTION](#-introduction)
- [TECHNO](#-techno)
- [REQUIREMENTS](#-requirements)
- [ARCHITECTURE](#-architecture)
- [GETTING STARTED](#-getting-started)
- [DATA DOWNLOADED](#-data-downloaded)
- [TO DO](#-to-do)

## 👋 INTRODUCTION
OpenScraper est un outil pratique et flexible conçu pour automatiser la récupération de données provenant d’API ouvertes. Que vous souhaitiez collecter des informations sous forme de fichiers CSV ou JSON, OpenScraper simplifie le processus en offrant une solution polyvalente et accessible, quelle que soit la complexité ou le format de l’API.  
Dans un monde où les données sont essentielles, les API ouvertes permettent d’accéder à une richesse d’informations en temps réel.  

Cependant, la gestion de ces API peut parfois devenir fastidieuse, notamment lorsque :  
- Les formats de réponse varient (JSON, XML ...)
- Les authentifications ou clés API sont nécessaires
- Une grande quantité de données doit être récupérée et exportée
- Plusieurs pages de résultats doivent être parcourues pour obtenir toutes les informations  

Avec OpenScraper, l’accès aux données ouvertes devient simple, rapide et entièrement automatisé. Que vous soyez développeur ou analyste de données, cet outil vous permettra d’exploiter le plein potentiel des API ouvertes sans effort supplémentaire.

## 💻 TECHNO
- **Langage**: Python 3.13.1

[Guide d'installation Python](https://github.com/EmmanuelLefevre/Documentations/blob/master/Tutorials/python_install.md)  

## 📚 REQUIREMENTS
- Colorama
- Requests
- Pandas

## 🏗 ARCHITECTURE
Ce projet respecte les principes de la Clean Architecture en garantissant une séparation claire des responsabilités entre les différentes couches, assurant ainsi une organisation modulaire et maintenable du code.  
```bash
├── src/
│   ├── presentation/
│   │   ├── app_controller.py
│   ├── application/
│   │   ├── dtos/
│   │   │   ├── api_response_dto.py
│   │   ├── exceptions/
│   │   │   ├── user_exit_exception.py
│   │   ├── services/
│   │   │   ├── message_printer.py
│   │   │   ├── user_input_handler.py
│   │   ├── uses_cases/
│   │   │   ├── ask_file_path.py
│   │   │   ├── ask_url.py
│   │   │   ├── display_message.py
│   │   │   ├── fetch_data.py
│   ├── domain/
│   │   ├── models/
│   │   ├── services/
│   │   │   ├── data_extractor.py
│   │   │   ├── data_formatter.py
│   │   │   ├── fetch_more_data.py.py
│   ├── infrastructure/
│   │   ├─── external_services/
│   │   │    ├── api_client.py
│   │   ├─── storage/
│   │   │    ├── data_frame/
│   │   │    │   ├── example_data_frame.json
│   │   │    │   ├── example_data_frame.csv
│   │   │    ├── save_file.py
├── app.py
├── requirements.txt
├── readme.md
├── .gitignore
```

## 🚀 GETTING STARTED
**1. Installer les librairies (en local dans python)**
```bash
pip install -r requirements.txt
```
**2. Vérifier l'installation des librairies**
```bash
pip list
```
**3. Lancer l'application**
- Normalement:
```bash
python -m app
```
- Sans fichiers de compilation:
```bash
python -B -m app
```
- Avec suppression des fichiers de compilation à la fin de l'éxécution du programme
```bash
python -m app; Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```
**4. Effacer les fichiers de compilation**
```bash
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

## 🛒 DATA DOWNLOADED
Les données JSON ou CSV sont stockées dans le dossier suivant de l'application =>
```bash
cd src\infrastructure\storage\data_frame
```

## 📝 TO DO
- A faire...

***

⭐⭐⭐ I hope you enjoy it, if so don't hesitate to leave a like on this repository and on the [Dotfiles](https://github.com/EmmanuelLefevre/Dotfiles) one (click on the "Star" button at the top right of the repository page). Thanks 🤗
