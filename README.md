# m3u-checker

**m3u-checker** est un outil Python CLI pour vérifier la validité des flux dans une playlist M3U.

## Fonctionnalités

- Utilise automatiquement `http-user-agent` et `http-referrer` du flux M3U si présent
- Filtre les flux de mauvaise qualité.
- Conçu pour vérifier les liens IPTV à partir du [dépôt IPTV-org](https://github.com/iptv-org/iptv).

## Paramètres pas défaut

- User-Agent par défaut: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36`
- Délai d'attente (secondes avant l'échec de la vérification): `10`
- Résolution minimum requise: `>=480`

## Utilisation
```bash
python main.py /path/to/playlist.m3u
```

## Prérequis

- [**ffmpeg**](https://ffmpeg.org/download.html) 
- **Bibliothèques Python**:
  ```bash
  pip install loguru
  ```

## Des soucis ?

S'il y a des problèmes, vous pouvez les signaler dans l'onglet [Issues](https://github.com/Remchalk/m3u-checker/issues) de ce repo. Cependant, pour être honnête, ce projet a été créé pour un usage unique, et je voulais le publier pour permettre à d'autres de l'utiliser dans un cas très spécifique. Pour plus d'utilisation générale, je recommande l'outil d'[Aleksandr Statciuk's](https://github.com/freearhey), [iptv-checker](https://github.com/freearhey/iptv-checker), qui est beaucoup plus complet et customisable.

Si vous avez des soucis par rapport à la traduction, vous pouvez les signaler dans l'onglet [Issues](https://github.com/TommyLPB39/m3u-checker-fr/issues) de ce fork.
