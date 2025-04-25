import subprocess
import os
import sys
import re
from loguru import logger

def get_user_agent():
    ua = input("User-Agent? (Press Enter to use the default one): ")
    return ua or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

def extract_error(stderr):
    for line in stderr.splitlines():
        if "error" in line.lower():
            return line.strip()
    return "Unknown error"

def check_stream(url, channel_name, extinf, default_ua, timeout=10):
    ua = re.search(r'http-user-agent="([^"]+)"', extinf)
    ref = re.search(r'http-referrer="([^"]+)"', extinf)

    user_agent = ua.group(1) if ua else default_ua
    if ua: logger.warning(f"http-user-agent override: {user_agent}")
    if ref: logger.warning(f"http-referrer added: {ref.group(1)}")

    logger.info(f"Checking: {channel_name} ({url})")

    cmd = [
        'ffmpeg',
        '-user_agent', user_agent,
        '-i', url,
        '-t', str(timeout),
        '-f', 'null', '-'
    ]
    if ref:
        cmd.extend(['-headers', f'Referer: {ref.group(1)}'])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if result.returncode != 0:
            logger.error(f"Invalid: {extract_error(result.stderr)}")
            return False

        output = result.stderr.lower()
        if 'video:' in output:
            res = re.search(r'(\d{3,4})x(\d{3,4})', output)
            if res:
                height = int(res.group(2))
                if height >= 480:
                    return True
                logger.error("Invalid: Resolution too low")
            else:
                logger.error("Invalid: No resolution found")
        else:
            logger.error("Invalid: No video stream")
    except subprocess.TimeoutExpired:
        logger.error("Invalid: Timed out")
    except Exception as e:
        logger.error(f"Error checking stream: {e}")
    return False

def parse_m3u(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='iso-8859-1') as f:
            lines = f.readlines()

    channels = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('#EXTINF:'):
            extinf = line
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('#EXTVLCOPT'):
                j += 1
            if j < len(lines):
                url = lines[j].strip()
                name = re.search(r',\s*(.*)$', extinf)
                channels.append((extinf, url, name.group(1) if name else "Unknown"))
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    return channels

def rw_playlist(input_file, output_file, user_agent):
    channels = parse_m3u(input_file)

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("#EXTM3U\n")
        try:
            for extinf, url, name in channels:
                if check_stream(url, name, extinf, user_agent):
                    logger.success("Valid: Writing to playlist")
                    out.write(f"{extinf}\n{url}\n")
                    out.flush()
        except KeyboardInterrupt:
            logger.warning("Process interrupted by user.")
            out.flush()

    logger.success(f"Done: Valid streams written to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py /path/to/playlist.m3u")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        logger.error(f"File not found: {input_path}")
        sys.exit(1)

    ua = get_user_agent()
    output_path = os.path.splitext(input_path)[0] + "_checked.m3u"
    rw_playlist(input_path, output_path, ua)
