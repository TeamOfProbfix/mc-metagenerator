from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Java Mcmeta Generator Pro ⚙️</title>
    <link rel="icon" type="image/png" href="/static/favicon.png">
    <style>
        :root {
            --bg-grad: radial-gradient(circle at top, #1e1b4b, #020617);
            --card-bg: rgba(30, 41, 59, 0.8);
            --text-main: #ffffff;
            --text-sub: #a5b4fc;
            --border: rgba(255,255,255,0.1);
            --input-bg: #020617;
            --p-color: #7c3aed;
            --s-color: #22d3ee;
        }
        body.light-theme { --bg-grad: #f1f5f9; --card-bg: #ffffff; --text-main: #0f172a; --text-sub: #475569; --border: #e2e8f0; --input-bg: #f8fafc; --p-color: #4f46e5; --s-color: #0891b2; }
        body.dark-theme { --bg-grad: #020617; --card-bg: #0f172a; --text-main: #f8fafc; --text-sub: #94a3b8; --border: #1e293b; --input-bg: #000000; }

        body { 
            margin:0; font-family: 'Segoe UI', sans-serif; 
            background: var(--bg-grad); color: var(--text-main); 
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            transition: 0.3s;
        }

        .app { width: 100%; max-width: 480px; padding: 20px; position: relative; }

        .menu-btn { position: fixed; top: 20px; right: 20px; cursor: pointer; z-index: 100; padding: 10px; background: var(--card-bg); border-radius: 10px; border: 1px solid var(--border); }
        .menu-btn div { width: 25px; height: 3px; background: var(--s-color); margin: 5px 0; border-radius: 2px; }
        .sidebar { position: fixed; top: 0; right: -250px; width: 200px; height: 100%; background: var(--card-bg); backdrop-filter: blur(20px); padding: 60px 20px; transition: 0.4s; z-index: 90; border-left: 1px solid var(--border); }
        .sidebar.active { right: 0; }
        .theme-opt { display: block; width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text-main); border-radius: 10px; cursor: pointer; text-align: left; }

        .header { text-align: center; margin-bottom: 20px; }
        .header h2 { margin: 0; font-size: 24px; background: linear-gradient(90deg, #c084fc, var(--s-color)); -webkit-background-clip: text; color: transparent; }
        
        .card { background: var(--card-bg); backdrop-filter: blur(15px); padding: 25px; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 10px 40px rgba(0,0,0,0.4); }

        .input-group { margin-bottom: 15px; }
        label { display: block; font-size: 11px; color: var(--text-sub); margin-bottom: 5px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;}
        input, select { width: 100%; padding: 12px; border-radius: 12px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text-main); font-size: 14px; box-sizing: border-box; }

        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .btn-main { width: 100%; padding: 15px; border: none; border-radius: 15px; background: linear-gradient(135deg, var(--p-color), var(--s-color)); font-weight: bold; color: white; cursor: pointer; font-size: 15px; margin-top: 10px;}
        
        pre { background: #000; padding: 15px; border-radius: 12px; font-size: 12px; color: #38bdf8; overflow: auto; max-height: 150px; border: 1px solid var(--border); margin: 15px 0; }
        
        #icon-preview { width: 80px; height: 80px; border-radius: 12px; border: 2px solid var(--s-color); object-fit: cover; display: none; margin: 10px auto; image-rendering: pixelated; }

        .footer { text-align: center; margin-top: 25px; font-size: 11px; color: var(--text-sub); line-height: 1.8; }
        .footer b { color: var(--s-color); }
        .footer a { color: var(--s-color); font-weight: bold; text-decoration: underline; }
    </style>
</head>
<body class="neon-theme">

<div class="menu-btn" onclick="toggleMenu()"><div></div><div></div><div></div></div>
<div class="sidebar" id="sidebar">
    <h4>Themes</h4>
    <button class="theme-opt" onclick="setTheme('neon')">✨ Neon</button>
    <button class="theme-opt" onclick="setTheme('dark')">🌙 Dark</button>
    <button class="theme-opt" onclick="setTheme('light')">☀️ Light</button>
</div>

<div class="app">
    <div class="header"><h2>Java Mcmeta Generator ⚙️</h2></div>

    <div class="card">
        <div class="input-group">
            <label>Pack Icon (Auto pack.png)</label>
            <input type="file" id="icon-input" accept="image/*" onchange="processIcon()">
            <img id="icon-preview">
        </div>

        <div class="input-group">
            <label>Minecraft Version</label>
            <select id="version-select" onchange="syncFormat()">
                <option value="48" selected>1.26.x (Format 48)</option>
                <option value="46">1.21.4 (Format 46)</option>
                <option value="42">1.21.2 - 1.21.3 (Format 42)</option>
                <option value="34">1.21 - 1.21.1 (Format 34)</option>
                <option value="32">1.20.5 - 1.20.6 (Format 32)</option>
                <option value="22">1.20.3 - 1.20.4 (Format 22)</option>
                <option value="18">1.20.2 (Format 18)</option>
                <option value="15">1.20 - 1.20.1 (Format 15)</option>
                <option value="13">1.19.4 (Format 13)</option>
                <option value="12">1.19.3 (Format 12)</option>
                <option value="9">1.19 - 1.19.2 (Format 9)</option>
                <option value="8">1.18.x (Format 8)</option>
                <option value="7">1.17.x (Format 7)</option>
                <option value="6">1.16.2 - 1.16.5 (Format 6)</option>
                <option value="5">1.15 - 1.16.1 (Format 5)</option>
                <option value="4">1.14.x (Format 4)</option>
            </select>
        </div>

        <div class="grid">
            <div class="input-group">
                <label>Pack Format</label>
                <input type="number" id="format-num" value="48" oninput="liveUpdate()">
            </div>
            <div class="input-group">
                <label>Description</label>
                <input id="desc" value="Probfix Java Pack" oninput="liveUpdate()">
            </div>
        </div>

        <pre id="preview"></pre>

        <button class="btn-main" onclick="handleDownload()">Download pack.mcmeta</button>
    </div>

    <div class="footer">
        <div>Make by <b>Probfix</b> & <b>AI partner⚡</b></div>
        <div>Need a Bedrock Manifest? <a href="https://mc-manifestgenerator.onrender.com" target="_blank">Manifest Generator ⚙️</a></div>
        <div>Need a Skin Pack? <a href="https://skin-pack-generator.onrender.com" target="_blank">Auto Skin Pack Here (For Bedrock)</a></div>
    </div>
</div>

<canvas id="canvas" width="128" height="128" style="display:none;"></canvas>

<script>
let currentJSON = null;
let iconBlob = null;

function toggleMenu() { document.getElementById('sidebar').classList.toggle('active'); }
function setTheme(t) { document.body.className = t + '-theme'; toggleMenu(); }

function syncFormat() {
    document.getElementById('format-num').value = document.getElementById('version-select').value;
    liveUpdate();
}

function processIcon() {
    const file = document.getElementById('icon-input').files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            let size = Math.min(img.width, img.height);
            ctx.clearRect(0,0,128,128);
            // Crop square and resize to 128x128
            ctx.drawImage(img, (img.width-size)/2, (img.height-size)/2, size, size, 0, 0, 128, 128);
            canvas.toBlob(blob => {
                iconBlob = blob;
                document.getElementById('icon-preview').src = URL.createObjectURL(blob);
                document.getElementById('icon-preview').style.display = 'block';
            }, 'image/png');
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function liveUpdate() {
    const format = parseInt(document.getElementById("format-num").value) || 48;
    const desc = document.getElementById("desc").value || "Pack";
    currentJSON = {
        "pack": {
            "description": desc,
            "pack_format": format
        }
    };
    document.getElementById("preview").innerText = JSON.stringify(currentJSON, null, 4);
}

async function handleDownload() {
    const res = await fetch("/download", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(currentJSON)
    });
    const blob = await res.blob();
    saveAs(blob, "pack.mcmeta");
    
    if(iconBlob) {
        setTimeout(() => saveAs(iconBlob, "pack.png"), 500);
    }
}

function saveAs(blob, name) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    a.click();
}

liveUpdate();
</script>
</body>
</html>
'''

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(force=True)
    with open("pack.mcmeta", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return send_file("pack.mcmeta", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
