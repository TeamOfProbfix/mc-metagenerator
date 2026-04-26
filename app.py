from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JAVA Mcmeta Generator Pro</title>
    <style>
        :root {
            --bg-grad: radial-gradient(circle at top, #020617, #000000);
            --card-bg: rgba(15, 23, 42, 0.9);
            --text-main: #ffffff;
            --text-sub: #94a3b8;
            --border: rgba(34, 211, 238, 0.2);
            --input-bg: #000000;
            --p-color: #06b6d4; /* Cyan 500 */
            --s-color: #22d3ee; /* Cyan 400 */
            --neon-glow: 0 0 15px rgba(34, 211, 238, 0.4);
        }

        body { 
            margin:0; font-family: 'Segoe UI', Roboto, sans-serif; 
            background: var(--bg-grad); color: var(--text-main); 
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            overflow-x: hidden;
        }

        /* Hiệu ứng ánh sáng Neon nền */
        body::before { 
            content:""; position:fixed; width:400px; height:400px; 
            background: var(--p-color); filter:blur(150px); 
            top:-150px; left:-150px; opacity: 0.15; z-index:-1; 
        }

        .app { width: 100%; max-width: 450px; padding: 20px; z-index: 1; }

        .header { text-align: center; margin-bottom: 25px; }
        .header h2 { 
            margin: 0; font-size: 26px; font-weight: 800;
            background: linear-gradient(90deg, #ffffff, var(--s-color)); 
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
        label { display: block; font-size: 12px; color: var(--s-color); margin-bottom: 6px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        
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
            background: linear-gradient(135deg, #0891b2, #22d3ee); 
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
            border: 2px solid var(--s-color); object-fit: cover; 
            display: none; margin: 15px auto; box-shadow: var(--neon-glow);
        }

        .footer { text-align: center; margin-top: 25px; font-size: 12px; color: var(--text-sub); opacity: 0.7; }
    </style>
</head>
<body>

<div class="app">
    <div class="header">
        <h2>JAVA Mcmeta Generator ⚙️</h2>
    </div>

    <div class="card">
        <div class="input-group">
            <label>Pack Icon (pack.png)</label>
            <input type="file" id="icon-input" accept="image/*" onchange="processIcon()">
            <img id="icon-preview">
        </div>

        <div class="input-group">
            <label>Phiên bản Minecraft Java</label>
            <select id="version-select" onchange="syncFormat()">
                <option value="46">1.21.4 (Format 46)</option>
                <option value="34">1.20.5 - 1.21.1 (Format 34)</option>
                <option value="22">1.20.3 - 1.20.4 (Format 22)</option>
                <option value="18">1.20.2 (Format 18)</option>
                <option value="15" selected>1.20 - 1.20.1 (Format 15)</option>
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
            <label>Mô tả (Description)</label>
            <input id="desc" placeholder="Nhập mô tả cho pack..." oninput="liveUpdate()" value="My Java Resource Pack">
        </div>

        <div class="input-group">
            <label>Pack Format (Số)</label>
            <input type="number" id="format-num" oninput="liveUpdate()" value="15">
        </div>

        <pre id="preview"></pre>

        <div class="btn-group">
            <button onclick="handleDownload()">Download Pack</button>
            <button onclick="copyCode()">Copy JSON</button>
        </div>
    </div>

    <div class="footer">Coded with ⚡ for Minecraft Java Edition</div>
</div>

<canvas id="canvas" width="128" height="128" style="display:none;"></canvas>

<script>
let currentJSON = null;
let iconBlob = null;

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
            
            // Cắt ảnh vuông trung tâm
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
    const format = parseInt(document.getElementById("format-num").value) || 15;

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
    alert("Đã sao chép mã JSON!");
}

// Khởi tạo ban đầu
liveUpdate();
</script>
</body>
</html>
'''

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(force=True)
    # Lưu tạm file trên server (Render hỗ trợ ghi tạm vào disk)
    with open("pack.mcmeta", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return send_file("pack.mcmeta", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
