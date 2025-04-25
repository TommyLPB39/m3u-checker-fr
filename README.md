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

## Requirements

- [**ffmpeg**](https://ffmpeg.org/download.html) 
- **Python libraries**:
  ```bash
  pip install loguru
  ```
