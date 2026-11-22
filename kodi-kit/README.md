# 🎬 Kit de démarrage Kodi

Tout ce qu'il faut pour transformer un ordinateur branché à la TV en_media center, comme un Fire Stick.

## Contenu du kit

| Fichier | À quoi ça sert |
|---|---|
| `INSTALLATION-FACILE.md` | Guide d'installation de Kodi pas à pas (Windows, Mac, Linux, Fire Stick) |
| `organiser_videos.py` | Script qui range vos films et séries dans des dossiers propres, pour que Kodi reconnaisse tout et affiche jaquettes + résumés |
| `playlists/` | 3 playlists intelligentes prêtes à l'emploi (à copier dans le dossier Kodi) |

## Démarrage rapide

1. Installer Kodi : voir `INSTALLATION-FACILE.md`
2. Lancer le script de rangement :
   ```
   python organiser_videos.py /chemin/vers/mes/videos
   ```
   Le script s'exécute d'abord en mode simulation : il montre ce qu'il va faire avec l'option `--dry-run` et ne déplace rien sans confirmation.
3. Ouvrir Kodi → Vidéos → Ajouter un dossier… → choisir le dossier Films ou Séries → sélectionner le scrapeur "The Movie Database" → OK
4. Copier les playlists : voir la section en bas de ce fichier

## Playlists intelligentes

Les fichiers `.xsp` créent dans Kodi des listes qui se mettent à jour toutes seules :

- **Films récents** : les 25 derniers films ajoutés
- **Films non vus** : films jamais regardés
- **Séries en cours** : épisodes non vus des séries en cours

### Où les copier ?

- **Windows** : `C:\Users\VOTRE_NOM\AppData\Roaming\Kodi\userdata\playlists\`
- **Linux** : `~/.kodi/userdata/playlists/`
- **Mac** : `~/Library/Application Support/Kodi/userdata/playlists/`

## Avertissement légal

Ce kit ne fournit aucun contenu vidéo ni aucun accès à des services non autorisés. Il sert uniquement à organiser et regarder les médias que vous possédez légalement.
