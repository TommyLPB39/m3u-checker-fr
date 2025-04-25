# m3u-checker

**m3u-checker** is a Python CLI tool to check the validity of streams in an M3U playlist.

## Features

- Automatically uses `http-user-agent` and `http-referrer` from the M3U file if present.
- Filter out low quality streams.
- Designed to check IPTV links from the [IPTV-org repository](https://github.com/iptv-org/iptv).

## Default settings

- Default User-Agent: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36`
- Timeout (seconds before the check fails): `10`
- Minimum required resolution: `>=480`

## Usage
```bash
python main.py /path/to/playlist.m3u
```

## Requirements

- [**ffmpeg**](https://ffmpeg.org/download.html) 
- **Python libraries**:
  ```bash
  pip install loguru
  ```

## Issues?

If there are any issues, you can report them in the [Issues](https://github.com/Remchalk/m3u-checker/issues) tab of this repo. However, to be honest, this project was created for a one-time use, and I wanted to publish it to allow others to use it in this very specific case. For more general use, I recommend [Aleksandr Statciuk's](https://github.com/freearhey) tool, [iptv-checker](https://github.com/freearhey/iptv-checker), which is much more complete and customizable.
