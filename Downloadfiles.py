import requests

download_url = 'https://get.videolan.org/vlc/3.0.17.4/win32/vlc-3.0.17.4-win32.exe'

req = requests.get(download_url)
filename = req.url[download_url.rfind("/")+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

def download_file(url, filename = ''):
    try:
        if filename:
            pass
        else:
            filename = req.url[download_url.rfind("/")+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

download_link = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
download_file(download_link)