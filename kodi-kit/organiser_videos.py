#!/usr/bin/env python3
"""Range les videos pour que Kodi les reconnaisse automatiquement.

Usage :
    python organiser_videos.py /chemin/vers/mes/videos            # interactif
    python organiser_videos.py /chemin/vers/mes/videos --dry-run  # simule sans rien deplacer
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".m4v", ".wmv", ".flv", ".webm", ".ts", ".mpg"}
TRASH_DIRNAME = "_A_TRIER"
TV_PATTERNS = [
    re.compile(r"(?P<title>.*?)[\s._-]+S(?P<season>\d{1,2})E(?P<ep>\d{1,3})", re.IGNORECASE),
    re.compile(r"(?P<title>.*?)[\s._-]+(?P<season>\d{1,2})x(?P<ep>\d{1,3})", re.IGNORECASE),
]
MOVIE_PATTERN = re.compile(r"(?P<title>.*?)[\s._-]*\(?(?P<year>(19|20)\d{2})\)?")
EPISODE_EXT = re.compile(r"E(\d{1,3})", re.IGNORECASE)
SEASON_EXT = re.compile(r"S(\d{1,2})", re.IGNORECASE)
MULTI = re.compile(r"[^A-Za-z0-9()'-]+")
WORDS = re.compile(r"[._]+")


def clean_title(raw: str) -> str:
    title = WORDS.sub(" ", raw)
    title = MULTI.sub(" ", title).strip(" -_")
    return title.title()


def classify(path: Path):
    for pattern in TV_PATTERNS:
        m = pattern.search(path.name)
        if m:
            title = clean_title(m.group("title"))
            season = int(m.group("season"))
            return "tv", title, season, int(m.group("ep"))
    m = MOVIE_PATTERN.search(path.name)
    if m:
        return "movie", clean_title(m.group("title")), int(m.group("year")), None
    return "unknown", path.stem, None, None


def episode_number(path: Path) -> int | None:
    m = EPISODE_EXT.search(path.name)
    return int(m.group(1)) if m else None


def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    n = 2
    while (dest.with_name(f"{stem} ({n}){suffix}")).exists():
        n += 1
    return dest.with_name(f"{stem} ({n}){suffix}")


def organize(root: Path, dry_run: bool) -> tuple[int, int]:
    moved = skipped = 0
    videos = sorted(p for p in root.rglob("*") if p.suffix.lower() in VIDEO_EXTENSIONS)

    for video in videos:
        if TRASH_DIRNAME in video.parts:
            continue
        kind, title, num, episode = classify(video)
        if kind == "tv":
            dest_dir = root / "Séries" / title / f"Saison {num:02d}"
            dest = dest_dir / f"{title} S{num:02d}E{episode:02d}{video.suffix.lower()}"
        elif kind == "movie":
            dest_dir = root / "Films"
            dest = dest_dir / f"{title} ({num}){video.suffix.lower()}"
        else:
            dest_dir = root / TRASH_DIRNAME
            dest = dest_dir / video.name
            print(f"  ?  {video.name} -> {dest.relative_to(root)} (titre non reconnu, à trier à la main)")
            if video == dest:
                skipped += 1
                continue
            if dest.exists():
                print(f"  !  {dest.name} existe déjà, fichier ignoré")
                skipped += 1
                continue
            if not dry_run:
                dest = unique_destination(dest)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(video), str(dest))
            skipped += 1
            continue

        if video == dest:
            skipped += 1
            continue
        if dest.exists():
            print(f"  !  {dest.name} existe déjà, fichier ignoré : {video.name}")
            skipped += 1
            continue

        dest = unique_destination(dest)
        action = "SIMULÉ" if dry_run else "OK"
        print(f"  {action}  {video.relative_to(root)}  ->  {dest.relative_to(root)}")
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(video), str(dest))
        moved += 1

    return moved, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Range films et séries pour Kodi.")
    parser.add_argument("dossier", type=Path, help="dossier contenant vos videos")
    parser.add_argument("--dry-run", action="store_true", help="simule sans rien déplacer")
    args = parser.parse_args()

    root = args.dossier.resolve()
    if not root.is_dir():
        print(f"Erreur : {root} n'est pas un dossier.")
        return 1

    print(f"\nRangement de : {root}\n")
    moved, skipped = organize(root, args.dry_run)
    mode = " (simulation, rien déplacé)" if args.dry_run else ""
    print(f"\nTerminé{mode} : {moved} fichier(s) à déplacer, {skipped} ignoré(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
