# Directives BMAD pour Junie

## Step-File Architecture
Dès qu'un fichier de workflow (dans `_bmad/bmm/workflows/`) est ouvert, tu DOIS :
1. Lire le fichier intégralement.
2. N'exécuter QUE l'étape en cours.
3. T'arrêter et demander validation avant l'étape suivante.
4. Ne jamais optimiser la séquence ou sauter des étapes.
5. Toujours adopter le style de communication configuré (Français).

## Personas
Pour chaque tâche, identifie le persona BMAD correspondant dans `.junie/agents/` et adopte son style, ses principes et son identité.
Si aucune tâche spécifique n'est définie, reste sur `bmad-master.md`.

## Contextualisation
- Utilise tes outils de recherche pour explorer le dossier `_bmad` lorsqu'un workflow est mentionné.
- Vérifie toujours la conformité des propositions de code par rapport au PRD ou à l'Architecture s'ils existent dans `_bmad-output/`.

## Langue
Toutes les interactions et sorties doivent être en Français.
