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
    <title>JAVA Mcmeta Generator Pro</title>
    <link rel="icon" type="image/png" href="/static/favicon.png">
    <style>
        :root {
            --bg-grad: radial-gradient(circle at top, #1e1b4b, #000000);
            --card-bg: rgba(15, 23, 42, 0.9);
            --text-main: #ffffff;
            --text-sub: #a5b4fc;
            --border: rgba(34, 211, 238, 0.3);
            --input-bg: #000000;
            --p-color: #7c3aed;
            --s-color: #22d3ee;
            --neon-glow: 0 0 15px rgba(34, 211, 238, 0.4);
            --special-accent: #22d3ee;
        }
        body.light-theme {
            --bg-grad: #f1f5f9; --card-bg: #ffffff; --text-main: #0f172a;
            --text-sub: #475569; --border: #e2e8f0; --input-bg: #f8fafc;
            --p-color: #4f46e5; --s-color: #0ea5e9; --neon-glow: none; --special-accent: #0ea5e9;
        }
        body.dark-theme {
            --bg-grad: #020617; --card-bg: #0f172a; --text-main: #f1f5f9;
            --text-sub: #94a3b8; --border: #1e293b; --input-bg: #000000;
            --neon-glow: none; --special-accent: #22d3ee;
        }
        body { 
            margin:0; font-family: 'Segoe UI', sans-serif; 
            background: var(--bg-grad); color: var(--text-main); 
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            transition: 0.3s;
        }
        .app { width: 100%; max-width: 450px; padding: 20px; z-index: 1; position: relative;}
        .menu-btn { position: fixed; top: 20px; right: 20px; cursor: pointer; z-index: 100; padding: 10px; background: var(--card-bg); border-radius: 10px; border: 1px solid var(--border); }
        .menu-btn div { width: 25px; height: 3px; background: var(--s-color); margin: 5px 0; border-radius: 2px;}
        .sidebar { position: fixed; top: 0; right: -280px; width: 220px; height: 100%; background: var(--card-bg); backdrop-filter: blur(20px); padding: 70px 20px; transition: 0.4s; z-index: 90; border-left: 1px solid var(--border); }
        .sidebar.active { right: 0; }
        .theme-opt { display: block; width: 100%; padding: 14px; margin-bottom: 12px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text-main); border-radius: 12px; cursor: pointer; text-align: left; font-size: 14px; }
        .header { text-align: center; margin-bottom: 25px; }
        .header h2 { margin: 0; font-size: 26px; background: linear-gradient(90deg, #ffffff, var(--special-accent)); -webkit-background-clip: text; color: transparent; text-shadow: var(--neon-glow); }
        .card { background: var(--card-bg); backdrop-filter: blur(20px); padding: 25px; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
        .input-group { margin-bottom: 15px; }
        label { display: block; font-size: 11px; color: var(--s-color); margin-bottom: 6px; font-weight: 700; text-transform: uppercase; }
        input, select { width: 100%; padding: 12px; border-radius: 12px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text-main); font-size: 14px; box-sizing: border-box; }
        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px; }
        button { padding: 14px; border: none; border-radius: 14px; background: linear-gradient(135deg, var(--p-color), var(--s-color)); font-weight: bold; color: white; cursor: pointer; font-size: 14px; }
        pre { background: #000; padding: 15px; border-radius: 12px; font-size: 13px; color: #22d3ee; overflow: auto; max-height: 180px; border: 1px solid var(--border); margin-top: 15px; }
        #icon-preview { width: 80px; height: 80px; border-radius: 12px; border: 2px solid var(--special-accent); object-fit: cover; display: none; margin: 15px auto; }
        .footer { text-align: center; margin-top: 30px; font-size: 12px; color: var(--text-sub); line-height: 1.6;}
        .highlight { color: var(--special-accent); font-weight: bold;}
        .link-box a { color: var(--s-color); font-weight: bold; text-decoration: underline;}
    </style>
</head>
<body>
<div class="menu-btn" onclick="toggleMenu()"><div></div><div></div><div></div></div>
<div class="sidebar" id="sidebar">
    <h4>Select Theme</h4>
    <button class="theme-opt" onclick="setTheme('neon')">✨ Neon Vibe</button>
    <button class="theme-opt" onclick="setTheme('dark')">🌙 Pure Dark</button>
    <button class="theme-opt" onclick="setTheme('light')">☀️ Crystal Light</button>
</div>
<div class="app">
    <div class="header"><h2>JAVA Mcmeta Generator ⚙️</h2></div>
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
                <option value="15">1.20.x (Format 15)</option>
            </select>
        </div>
        <div class="input-group">
            <label>Description</label>
            <input id="desc" oninput="liveUpdate()" value="My Java Resource Pack">
        </div>
        <div class="input-group">
            <label>Pack Format</label>
            <input type="number" id="format-num" oninput="liveUpdate()" value="48">
        </div>
        <pre id="preview"></pre>
        <div class="btn-group">
            <button onclick="handleDownload()">Download</button>
            <button onclick="copyCode()">Copy JSON</button>
        </div>
    </div>
    <div class="footer">
        <div>Make by <span class="highlight">Probfix</span> & <span class="highlight">AI partner⚡</span></div>
        <div class="link-box">Need Manifest.json for Bedrock? <a href="https://manifest-generator-y00b.onrender.com/" target="_blank">Click here</a></div>
    </div>
</div>
<canvas id="canvas" width="128" height="128" style="display:none;"></canvas>
<script>
let currentJSON = null; let iconBlob = null;
function toggleMenu() { document.getElementById('sidebar').classList.toggle('active'); }
function setTheme(t) { document.body.className = t + '-theme'; toggleMenu(); }
function syncFormat() { document.getElementById('format-num').value = document.getElementById('version-select').value; liveUpdate(); }
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
            ctx.drawImage(img, (img.width-size)/2, (img.height-size)/2, size, size, 0, 0, 128, 128);
            canvas.toBlob(blob => { iconBlob = blob; document.getElementById('icon-preview').src = URL.createObjectURL(blob); document.getElementById('icon-preview').style.display = 'block'; }, 'image/png');
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}
function liveUpdate() {
    const desc = document.getElementById("desc").value || "Pack";
    const format = parseInt(document.getElementById("format-num").value) || 48;
    currentJSON = { "pack": { "description": desc, "pack_format": format } };
    document.getElementById("preview").innerText = JSON.stringify(currentJSON, null, 4);
}
async function handleDownload() {
    const res = await fetch("/download", { method: "POST", body: JSON.stringify(currentJSON) });
    const b = await res.blob();
    saveAs(b, "pack.mcmeta");
    if(iconBlob) setTimeout(() => saveAs(iconBlob, "pack.png"), 500);
}
function saveAs(blob, name) { const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = name; a.click(); }
function copyCode() { navigator.clipboard.writeText(JSON.stringify(currentJSON, null, 4)); alert("Copied!"); }
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
