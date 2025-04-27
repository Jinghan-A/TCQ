import zipfile

# 定义HTML内容
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>北玄提词器</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100vh;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        #text-container {
            height: 60vh;
            overflow: auto; /* 添加滚动条 */
            background: #000;
            color: #fff;
            padding: 20px;
            border-radius: 5px;
            width: 100%;
            max-width: 800px;
            font-size: 24px;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .controls {
            display: flex;
            flex-direction: column;
            gap: 10px;
            width: 100%;
            max-width: 800px;
            margin-bottom: 20px;
        }
        .controls > div {
            display: flex;
            justify-content: space-between;
        }
        button {
            padding: 10px 15px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 25%; /* 按钮宽度调整为25% */
            margin: 0 5px; /* 添加按钮之间的间距 */
        }
        button:hover {
            background: #45a049;
        }
        label {
            font-size: 12px; /* 缩小标签文字大小 */
            display: block;
            margin-bottom: 5px;
        }
        input[type="range"] {
            width: 100%;
        }
        .button-row {
            display: flex;
            justify-content: space-around; /* 按钮横向排列 */
            width: 100%;
            max-width: 800px;
        }
    </style>
</head>
<body>
    <h1>北玄提词器</h1>
    
    <div id="text-container" contenteditable="true" placeholder="输入你的文本..."></div>
    
    <div class="controls">
        <div>
            <label for="font-size">字体大小 (10-100):</label>
            <input type="range" id="font-size" min="10" max="100" value="45">
            <span id="font-size-value">45px</span>
        </div>
        <div>
            <label for="speed">滚动速度 (20-90):</label>
            <input type="range" id="speed" min="20" max="90" value="65">
            <span id="speed-value">65</span>
        </div>
    </div>
    
    <div class="button-row">
        <button id="play-btn">播放</button>
        <button id="pause-btn">暂停</button>
        <button id="reset-btn">重置</button>
        <button id="clear-btn">清空</button>
    </div>
    
    <script>
        const textContainer = document.getElementById('text-container');
        const fontSizeSlider = document.getElementById('font-size');
        const fontSizeValue = document.getElementById('font-size-value');
        const speedSlider = document.getElementById('speed');
        const speedValue = document.getElementById('speed-value');
        const playBtn = document.getElementById('play-btn');
        const pauseBtn = document.getElementById('pause-btn');
        const resetBtn = document.getElementById('reset-btn');
        const clearBtn = document.getElementById('clear-btn');
        
        let scrollInterval;
        let isPlaying = false;
        
        // 更新字体大小
        fontSizeSlider.addEventListener('input', function() {
            const size = this.value;
            textContainer.style.fontSize = `${size}px`;
            fontSizeValue.textContent = `${size}px`;
        });
        
        // 更新速度显示
        speedSlider.addEventListener('input', function() {
            speedValue.textContent = this.value;
        });
        
        // 播放功能
        playBtn.addEventListener('click', function() {
            if (!isPlaying) {
                const speed = speedSlider.value;
                scrollInterval = setInterval(() => {
                    textContainer.scrollTop += 1;
                    
                    // 如果滚动到底部，停止滚动
                    if (textContainer.scrollTop >= textContainer.scrollHeight - textContainer.offsetHeight) {
                        pauseScroll();
                    }
                }, 1000 / speed);
                
                isPlaying = true;
            }
        });
        
        // 暂停功能
        pauseBtn.addEventListener('click', pauseScroll);
        
        // 重置功能
        resetBtn.addEventListener('click', function() {
            pauseScroll();
            textContainer.scrollTop = 0;
        });
        
        // 清空功能
        clearBtn.addEventListener('click', function() {
            pauseScroll();
            textContainer.innerHTML = '';
            textContainer.scrollTop = 0;
        });
        
        function pauseScroll() {
            clearInterval(scrollInterval);
            isPlaying = false;
        }
        
        // 初始设置
        textContainer.style.fontSize = `${fontSizeSlider.value}px`;
    </script>
</body>
</html>
"""

# 将HTML内容写入文件
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# 创建一个压缩包，文件名为“提词器.zip”
zip_filename = "提词器.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write("index.html")

print(f"压缩包已生成：{zip_filename}")