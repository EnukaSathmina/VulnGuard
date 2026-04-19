const API = "http://127.0.0.1:8000";

// =====================
// ⏳ PROGRESS BAR SYSTEM
// =====================
let progressInterval;
let progress = 0;

function startProgressBar() {
    progress = 0;

    const bar = document.getElementById("progressBar");
    if (!bar) {
        console.warn("Progress bar not found");
        return;
    }

    bar.style.width = "0%";

    progressInterval = setInterval(() => {
        if (progress < 90) {
            progress += Math.random() * 8;
            bar.style.width = progress + "%";
        }
    }, 200);

    console.log("[DEBUG] Progress started");
}

function finishProgressBar() {
    const bar = document.getElementById("progressBar");
    if (!bar) return;

    clearInterval(progressInterval);
    progressInterval = null;

    progress = 100;
    bar.style.width = "100%";

    setTimeout(() => {
        bar.style.width = "0%";
        progress = 0;
    }, 600);

    console.log("[DEBUG] Progress finished");
}

// =====================
// 🖥️ TERMINAL
// =====================
function logTerminal(msg) {
    const terminal = document.getElementById("terminal");
    if (!terminal) return;

    const line = document.createElement("div");
    line.textContent = ">> " + msg;

    terminal.appendChild(line);
    terminal.scrollTop = terminal.scrollHeight;

    console.log("[TERMINAL]", msg);
}

// =====================
// 🌐 GRAPH SYSTEM
// =====================
let canvas, ctx;
let nodes = [];

function initGraph() {
    canvas = document.getElementById("netCanvas");

    if (!canvas) {
        console.error("[GRAPH] Canvas not found");
        return;
    }

    ctx = canvas.getContext("2d");

    // FIX: prevent broken sizing
    setTimeout(() => {
        canvas.width = canvas.offsetWidth;
        canvas.height = 300;

        console.log("[GRAPH] Initialized:", canvas.width, canvas.height);
    }, 100);
}

function addNode(label, type) {
    nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        type
    });
}

function drawGraph() {
    if (!ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    nodes.forEach(n => {
        let color = "#22c55e";

        if (n.type === "SQL Injection") color = "red";
        if (n.type === "XSS") color = "orange";

        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(n.x, n.y, 7, 0, Math.PI * 2);
        ctx.fill();
    });
}

// =====================
// 📊 STATS
// =====================
async function loadStats() {
    try {
        const res = await fetch(API + "/stats");
        const data = await res.json();

        document.getElementById("totalScans").innerText = data.total_scans;
        document.getElementById("xssCount").innerText = data.xss;
        document.getElementById("sqliCount").innerText = data.sqli;
        document.getElementById("infoCount").innerText = data.info;

        console.log("[DEBUG] Stats updated", data);

    } catch (err) {
        console.error("[STATS ERROR]", err);
    }
}

// =====================
// 🚀 SCAN ENGINE
// =====================
async function startScan() {

    const url = document.getElementById("urlInput").value;
    const status = document.getElementById("status");
    const results = document.getElementById("results");

    if (!url) {
        alert("Enter a URL first");
        return;
    }

    // FIX: prevent layout stacking issues
    results.innerHTML = "";
    nodes = [];
    drawGraph();

    status.innerText = "Scanning...";

    logTerminal("Initializing scanner...");
    logTerminal("Connecting backend...");
    logTerminal("Starting scan process...");

    startProgressBar();

    try {

        const fullUrl = API + "/scan?url=" + encodeURIComponent(url);

        console.log("[REQUEST]", fullUrl);

        const res = await fetch(fullUrl);
        const data = await res.json();

        console.log("[RESPONSE]", data);

        logTerminal("Scan response received");
        logTerminal("Analyzing results...");

        // =====================
        // RESULTS UI
        // =====================
        if (!data.details || data.details.length === 0) {

            results.innerHTML = `<div style="color:#22c55e;">No vulnerabilities found</div>`;
            logTerminal("No vulnerabilities found");

        } else {

            data.details.forEach(item => {

                let color = "#22c55e";
                if (item.type === "SQL Injection") color = "red";
                if (item.type === "XSS") color = "orange";

                logTerminal(`${item.type} → ${item.url}`);

                results.innerHTML += `
                    <div style="
                        background:#1f2937;
                        padding:10px;
                        margin:10px 0;
                        border-radius:8px;
                        border-left:4px solid ${color};
                    ">
                        <b>${item.type}</b><br>
                        ${item.url}<br>
                        ${item.status}
                    </div>
                `;
            });
        }

        // =====================
        // GRAPH UPDATE
        // =====================
        nodes = [];

        if (data.details?.length > 0) {
            data.details.forEach(item => addNode(item.url, item.type));
        } else {
            addNode("clean", "SAFE");
        }

        drawGraph();

        finishProgressBar();

        status.innerText = "Scan Complete";

        logTerminal("Scan completed successfully ✔");

        loadStats();

    } catch (err) {

        console.error("[ERROR]", err);

        finishProgressBar();

        logTerminal("Backend connection failed ❌");

        status.innerText = "Backend connection failed ❌";
    }
}

// =====================
// 🚀 INIT
// =====================
window.onload = () => {
    initGraph();
    loadStats();

    logTerminal("VulnGuard Scanner ready ⚡");
};