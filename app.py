from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Full English Localization & Enhanced Features
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JAVA Mcmeta Generator Pro</title>
    <style>
        /* Define Theme CSS Variables */
        :root {
            /* Mặc định: Neon Purple/Cyan Vibe */
            --bg-grad: radial-gradient(circle at top, #1e1b4b, #000000); /* Dark purple top */
            --card-bg: rgba(15, 23, 42, 0.9);
            --text-main: #ffffff;
            --text-sub: #a5b4fc; /* Pale purple */
            --border: rgba(34, 211, 238, 0.3); /* Cyan accent */
            --input-bg: #000000;
            --p-color: #7c3aed; /* Purple 600 */
            --s-color: #22d3ee; /* Cyan 400 */
            --neon-glow: 0 0 15px rgba(34, 211, 238, 0.4);
            --special-accent: #22d3ee; /* Cyan for credits */
        }

        /* Light Theme */
        body.light-theme {
            --bg-grad: #f1f5f9;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-sub: #475569;
            --border: #e2e8f0;
            --input-bg: #f8fafc;
            --p-color: #4f46e5; /* Purple 600 */
            --s-color: #0ea5e9; /* Cyan 500 */
            --neon-glow: none;
            --special-accent: #0ea5e9;
        }

        /* Dark Theme (Pure Dark) */
        body.dark-theme {
            --bg-grad: #020617;
            --card-bg: #0f172a;
            --text-main: #f1f5f9;
            --text-sub: #94a3b8;
            --border: #1e293b;
            --input-bg: #000000;
            --neon-glow: none;
            --special-accent: #22d3ee;
        }

        body { 
            margin:0; font-family: 'Segoe UI', Roboto, sans-serif; 
            background: var(--bg-grad); color: var(--text-main); 
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            overflow-x: hidden; transition: background 0.3s, color 0.3s;
        }

        /* Neon Purple Background Glow */
        body::before { 
            content:""; position:fixed; width:500px; height:500px; 
            background: #7c3aed; filter:blur(180px); 
            top:-200px; left:-200px; opacity: 0.15; z-index:-1; 
        }

        .app { width: 100%; max-width: 450px; padding: 20px; z-index: 1; position: relative;}

        /* Theme Switcher Button */
        .menu-btn { position: fixed; top: 20px; right: 20px; cursor: pointer; z-index: 100; padding: 10px; background: var(--card-bg); border-radius: 10px; border: 1px solid var(--border); box-shadow: var(--neon-glow); transition: 0.3s; }
        .menu-btn:hover { border-color: var(--s-color); }
        .menu-btn div { width: 25px; height: 3px; background: var(--s-color); margin: 5px 0; border-radius: 2px;}

        /* Sidebar for Themes */
        .sidebar { position: fixed; top: 0; right: -280px; width: 220px; height: 100%; background: var(--card-bg); backdrop-filter: blur(20px); padding: 70px 20px; transition: 0.4s; z-index: 90; border-left: 1px solid var(--border); box-shadow: -10px 0 30px rgba(0,0,0,0.5); }
        .sidebar.active { right: 0; }
        .sidebar h4 { margin-top: 0; color: var(--s-color); font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; text-align: center;}
        .theme-opt { display: block; width: 100%; padding: 14px; margin-bottom: 12px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text-main); border-radius: 12px; cursor: pointer; text-align: left; font-size: 14px; transition: 0.2s; }
        .theme-opt:hover { border-color: var(--s-color); transform: translateX(-5px); }

        .header { text-align: center; margin-bottom: 25px; }
        .header h2 { 
            margin: 0; font-size: 26px; font-weight: 800;
            background: linear-gradient(90deg, #ffffff, var(--special-accent)); 
            -webkit-background-clip: text; color: transparent;
            text-shadow: var(--neon-glow);
        }
        
        .card { 
            background: var(--card-bg); 
            backdrop-filter: blur(20px); 
            padding: 25px; 
            border-radius: 24px; 
            border: 1px solid var(--border); 
            box-shadow: 0 20px 50px rgba(0,0,0,0.5); 
        }

        .input-group { margin-bottom: 15px; }
        label { display: block; font-size: 11px; color: var(--s-color); margin-bottom: 6px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
        
        input, select { 
            width: 100%; padding: 12px; border-radius: 12px; 
            border: 1px solid var(--border); background: var(--input-bg); 
            color: var(--text-main); font-size: 14px; box-sizing: border-box;
            transition: 0.3s;
        }
        input:focus, select:focus { border-color: var(--s-color); outline: none; box-shadow: 0 0 10px rgba(34, 211, 238, 0.2); }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px; }
        button { 
            padding: 14px; border: none; border-radius: 14px; 
            background: linear-gradient(135deg, var(--p-color), var(--s-color)); 
            font-weight: bold; color: white; cursor: pointer; font-size: 14px;
            transition: 0.2s;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(34, 211, 238, 0.4); }
        button:active { transform: scale(0.95); }

        pre { 
            background: #000; padding: 15px; border-radius: 12px; 
            font-size: 13px; color: #22d3ee; overflow: auto; 
            max-height: 180px; border: 1px solid var(--border); 
            white-space: pre; margin-top: 15px;
        }
        
        #icon-preview { 
            width: 80px; height: 80px; border-radius: 12px; 
            border: 2px solid var(--special-accent); object-fit: cover; 
            display: none; margin: 15px auto; box-shadow: var(--neon-glow);
        }

        .credits-container { text-align: center; margin-top: 30px; font-size: 12px; color: var(--text-sub); line-height: 1.6;}
        .highlight { color: var(--special-accent); font-weight: bold;}
        .bedrock-link { margin-top: 8px; display: block; color: var(--text-sub); text-decoration: none; transition: 0.2s;}
        .bedrock-link a { color: var(--s-color); text-decoration: underline; font-weight: bold;}
        .bedrock-link:hover { color: var(--text-main); }
    </style>
</head>
<body>

<div class="menu-btn" onclick="toggleMenu()">
    <div></div><div></div><div></div>
</div>

<div class="sidebar" id="sidebar">
    <h4>Select Theme</h4>
    <button class="theme-opt" onclick="setTheme('neon')">✨ Neon Vibe</button>
    <button class="theme-opt" onclick="setTheme('dark')">🌙 Pure Dark</button>
    <button class="theme-opt" onclick="setTheme('light')">☀️ Crystal Light</button>
</div>

<div class="app">
    <div class="header">
        <h2>JAVA Mcmeta Generator ⚙️</h2>
    </div>

    <div class="card">
        <div class="input-group">
            <label>Pack Icon (Auto-crop pack.png)</label>
            <input type="file" id="icon-input" accept="image/*" onchange="processIcon()">
            <img id="icon-preview">
        </div>

        <div class="input-group">
            <label>Minecraft Java Version</label>
            <select id="version-select" onchange="syncFormat()">
                <option value="48" selected>1.26.x (Format 48)</option>
                <option value="46">1.21.4 (Format 46)</option>
                <option value="34">1.20.5 - 1.21.1 (Format 34)</option>
                <option value="22">1.20.3 - 1.20.4 (Format 22)</option>
                <option value="18">1.20.2 (Format 18)</option>
                <option value="15">1.20 - 1.20.1 (Format 15)</option>
                <option value="13">1.19.4 (Format 13)</option>
                <option value="12">1.19.3 (Format 12)</option>
                <option value="9">1.18.2 (Format 9)</option>
                <option value="8">1.18 - 1.18.1 (Format 8)</option>
                <option value="7">1.17 (Format 7)</option>
                <option value="6">1.16.2 - 1.16.5 (Format 6)</option>
                <option value="5">1.15 - 1.16.1 (Format 5)</option>
                <option value="4">1.13 - 1.14.4 (Format 4)</option>
            </select>
        </div>

        <div class="input-group">
            <label>Pack Description</label>
            <input id="desc" placeholder="Enter description..." oninput="liveUpdate()" value="My Java Resource Pack">
        </div>

        <div class="input-group">
            <label>Pack Format (Number)</label>
            <input type="number" id="format-num" oninput="liveUpdate()" value="48">
        </div>

        <pre id="preview"></pre>

        <div class="btn-group">
            <button onclick="handleDownload()">Download Pack</button>
            <button onclick="copyCode()">Copy JSON</button>
        </div>
    </div>

    <div class="credits-container">
        <div class="footer-text">
            Make by <span class="highlight">Probfix</span> & <span class="highlight">AI partner⚡</span>
        </div>
        <div class="bedrock-link">
            Need Manifest.json for Minecraft Bedrock? <a href="https://manifest-generator-y00b.onrender.com/" target="_blank">Click here</a>
        </div>
    </div>
</div>

<canvas id="canvas" width="128" height="128" style="display:none;"></canvas>

<script>
let currentJSON = null;
let iconBlob = null;

// Theme Logic
function toggleMenu() { document.getElementById('sidebar').classList.toggle('active'); }
function setTheme(t) { 
    document.body.className = t + '-theme'; 
    localStorage.setItem('mcmeta-theme', t); // Save preference
    toggleMenu(); 
}

// Load saved theme on load
const savedTheme = localStorage.getItem('mcmeta-theme') || 'neon';
document.body.className = savedTheme + '-theme';


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
            
            // Center crop to square
            let size = Math.min(img.width, img.height);
            let x = (img.width - size) / 2;
            let y = (img.height - size) / 2;
            
            ctx.clearRect(0,0,128,128);
            ctx.drawImage(img, x, y, size, size, 0, 0, 128, 128);
            
            canvas.toBlob(blob => {
                iconBlob = blob;
                const preview = document.getElementById('icon-preview');
                preview.src = URL.createObjectURL(blob);
                preview.style.display = 'block';
            }, 'image/png');
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function liveUpdate() {
    const desc = document.getElementById("desc").value || "A Minecraft Pack";
    const format = parseInt(document.getElementById("format-num").value) || 48;

    currentJSON = {
        "pack": {
            "description": desc,
            "pack_format": format
        }
    };
    document.getElementById("preview").innerText = JSON.stringify(currentJSON, null, 4);
}

async function handleDownload() {
    if(!currentJSON) return;

    // 1. Download pack.mcmeta
    const res = await fetch("/download", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(currentJSON)
    });
    const mBlob = await res.blob();
    saveAs(mBlob, "pack.mcmeta");

    // 2. Download pack.png
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

function copyCode() {
    navigator.clipboard.writeText(JSON.stringify(currentJSON, null, 4));
    alert("JSON code copied to clipboard!");
}

// Initial update
liveUpdate();
</script>
</body>
</html>
'''

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(force=True)
    # Ghi tạm vào thư mục làm việc của Render (temporary disk space)
    filename = "pack.mcmeta"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
