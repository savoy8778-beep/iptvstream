# 📺 Installation facile de Kodi

## Étape 1 — Télécharger Kodi

- **Windows / Mac / Linux** : https://kodi.tv/download
- **Fire TV Stick** : installez l'application "Downloader" depuis l'Amazon Appstore, tapez `kodi.tv/download` dedans, puis installez le fichier APK Android

## Étape 2 — Ouvrir Kodi et ajouter vos videos

1. Lancer Kodi
2. Aller dans **Vidéos → Ajouter un dossier…**
3. Parcourir et choisir votre dossier **Films**
4. Cliquez **OK** puis sur **Ce dossier contient** :
   - Films → **The Movie Database**
   - Séries → **The Movie Database** (séries)
5. Choisir la langue **Français**, puis OK
6. Kodi va interroger la base de données et afficher jaquettes, résumés et notes. Patientez quelques minutes si vous avez beaucoup de fichiers
7. Recommencer pour le dossier **Séries** ou **Anime**

> Si Kodi ne reconnaît pas certains titres, lancez d'abord le script `organiser_videos.py` fourni dans ce kit : des noms au format propre (`Film (2019)`, `Série S01E02`) sont reconnus à presque 100 %.

## Étape 3 — Copier les playlists

Copier les 3 fichiers de `playlists/` vers :

- **Windows** : `C:\Users\VOTRE_NOM\AppData\Roaming\Kodi\userdata\playlists\`
- **Linux** : `~/.kodi/userdata/playlists/`
- **Mac** : `~/Library/Application Support/Kodi/userdata/playlists/`

Redémarrer Kodi : les listes apparaissent dans **Vidéos → Listes de lecture**.

## Étape 4 — Télécommande facile

- **Smartphone** : activez dans Kodi `Paramètres → Services → Contrôle → Autoriser le contrôle à distance`, puis installez Kore (Android) ou Official Kodi Remote (iPhone) sur le même réseau Wi-Fi
- **Clavier** : la touche `S` ouvre le menu d'arrêt, `Échap` revient en arrière

## Sur Fire TV Stick

Kodi est aussi disponible directement sur Fire Stick :
1. Installer **Downloader** depuis l'Amazon Appstore
2. Autoriser l'installation d'applications inconnues (`Paramètres → Appareil → Options développeur`)
3. Dans Downloader, taper `kodi.tv/download` et installer

## Problèmes fréquents

| Problème | Solution |
|---|---|
| films dupliqués dans la bibliothèque | le script de rangement a laissé de vieux noms en double, relancez-le avec `--dry-run` |
| jaquettes incorrectes | clic droit sur le film → « Informations » → « Choisir une image » ou « Re-scanner » |
| Kodi rame sur vieux PC | dans `Paramètres → Lecteur → Vidéos`, passer l'accélération sur « DXVA2 » (Windows) |
