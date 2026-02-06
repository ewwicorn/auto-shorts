def download_video(url, sources_path, proxy=None, cookies=None):
    import yt_dlp
    
    ydl_opts = {
        'external_downloader': 'deno',
            'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Connection': 'keep-alive',
        },
        
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios', 'android_embed'],
                'player_skip': ['dash', 'hls', 'configs'],
            }
        },
        'outtmpl': sources_path,
        'format': '18/22/36/17',
        'quiet': False,
        'no_warnings': False,
    }
    
    if proxy:
        ydl_opts['proxy'] = proxy
        
    if cookies:
        ydl_opts['cookiefile'] = cookies
        

    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Video has been downloaded: {info['title']}")
            print(sources_path)
            return True
    except Exception as e:
        print(f"Downloading error: {e}")
        return False
    