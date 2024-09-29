from flask import Flask, jsonify, request
from tiktok_downloader import Tikmate, snaptik, mdown, tikdown, ttdownloader, tikwm, VideoInfo

app = Flask(__name__)

class TikTokDownloader:
    def __init__(self):
        pass

    def get_video_info(self, url):
        num = 0
        results = {}

        # Tikmate
        try:
            d1 = Tikmate(url)
            v = d1[0]
            results[f"{v.type}{num}"] = v.json
            num += 1
        except:
            results[f"video{num}"] = "Video not found"

        # snaptik
        try:
            d2 = snaptik(url)
            v = d2[0]
            results[f"{v.type}{num}"] = v.json
            num += 1
        except:
            results[f"video{num}"] = "Video not found"

        # ttdownloader
        try:
            d3 = ttdownloader(url)
            v = d3[0]
            results[f"{v.type}{num}"] = v.json
            num += 1
        except:
            results[f"video{num}"] = "Video not found"

        # tikwm
        try:
            d4 = tikwm(url)
            v = d4[0]
            results[f"{v.type}{num}"] = v.json
            num += 1
        except:
            results[f"video{num}"] = "Video not found"

        # tikdown
        try:
            d5 = tikdown(url)
            v = d5[0]
            results[f"{v.type}{num}"] = v.json
            num += 1
        except:
            results[f"video{num}"] = "Video not found"

        return results

@app.route('/video', methods=['POST', 'GET'])
def download_video_info():
    if request.method == 'POST':
        url = request.json.get('url')
    elif request.method == 'GET':
        url = request.args.get('url')

    downloader = TikTokDownloader()
    video_info = downloader.get_video_info(url)
    return jsonify(video_info)

if __name__ == '__main__':
    app.run(debug=True)
