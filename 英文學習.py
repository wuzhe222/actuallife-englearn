<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TOEIC 800 勇者挑戰賽</title>
    <style>
        /* 定義整體頁面樣式 */
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        /* 遊戲主容器 */
        #game-container { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 400px; text-align: center; }
        /* 主題標籤樣式 */
        .theme-tag { background: #e1f5fe; color: #0288d1; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 1rem; display: inline-block; }
        /* 題目文字樣式 */
        #word-display { font-size: 2rem; color: #333; margin: 10px 0; font-weight: bold; }
        /* 選項按鈕樣式 */
        .option-btn { display: block; width: 100%; padding: 12px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px; background: white; cursor: pointer; transition: 0.3s; font-size: 1rem; }
        /* 滑鼠懸停選項的效果 */
        .option-btn:hover { background: #f8f9fa; border-color: #007bff; }
        /* 答對與答錯的顏色 */
        .correct { background: #d4edda !important; border-color: #28a745 !important; }
        .wrong { background: #f8d7da !important; border-color: #dc3545 !important; }
        /* 狀態列 (分數與生命值) */
        #stats { display: flex; justify-content: space-between; margin-bottom: 20px; color: #666; font-weight: bold; }
    </style>
</head>
<body>

<div id="game-container">
    <div id="stats">
        <span>分數: <span id="score">0</span></span>
        <span>生命值: <span id="hp">❤️ ❤️ ❤️</span></span>
    </div>
    
    <div class="theme-tag" id="theme-display">主題：商務會議 (Business Meetings)</div>
    
    <div id="word-display">Loading...</div>
    <div id="pronunciation" style="color: #888; margin-bottom: 15px;"></div>

    <div id="options-container"></div>
</div>

<script>
    // 定義多益 800 分等級的單字庫 (主題式)
    const wordBank = [
        { word: "Collaborate", trans: "合作", theme: "團隊工作", hint: "/kəˈlæb.ə.reɪt/" },
        { word: "Mandatory", trans: "強制性的", theme: "公司政策", hint: "/ˈmæn.də.tɔːr.i/" },
        { word: "Incentive", trans: "獎勵/動機", theme: "員工福利", hint: "/ɪnˈsen.tɪv/" },
        { word: "Feasible", trans: "可行的", theme: "專案執行", hint: "/ˈfiː.zə.bəl/" },
        { word: "Acquisition", trans: "收購/獲得", theme: "企業擴張", hint: "/ˌæk.wɪˈzɪʃ.ən/" }
    ];

    let score = 0; // 初始化分數
    let hp = 3;    // 初始化生命值
    let currentWord = {}; // 當前題目物件

    // 隨機選取題目與產生選項的函式
    function nextQuestion() {
        if (hp <= 0) { // 檢查是否沒血了
            alert("遊戲結束！最終分數: " + score);
            location.reload(); // 重新整理網頁開始新遊戲
            return;
        }

        // 從字庫隨機挑一個字
        currentWord = wordBank[Math.floor(Math.random() * wordBank.length)];
        
        // 更新介面上的文字
        document.getElementById('word-display').innerText = currentWord.word;
        document.getElementById('theme-display').innerText = "主題：" + currentWord.theme;
        document.getElementById('pronunciation').innerText = currentWord.hint;

        // 產生混淆選項 (1個正確 + 2個隨機錯誤)
        const options = [currentWord.trans];
        while(options.length < 3) {
            let randomTrans = wordBank[Math.floor(Math.random() * wordBank.length)].trans;
            if(!options.includes(randomTrans)) options.push(randomTrans);
        }
        
        // 打亂選項順序
        options.sort(() => Math.random() - 0.5);

        // 渲染按鈕到畫面上
        const container = document.getElementById('options-container');
        container.innerHTML = ''; // 清空舊按鈕
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.innerText = opt;
            btn.onclick = () => checkAnswer(opt, btn); // 綁定點擊事件
            container.appendChild(btn);
        });
    }

    // 檢查答案正確性的函式
    function checkAnswer(selected, btn) {
        const allButtons = document.querySelectorAll('.option-btn');
        allButtons.forEach(b => b.disabled = true); // 點擊後禁用所有按鈕，防止重複點擊

        if (selected === currentWord.trans) { // 答對了
            btn.classList.add('correct');
            score += 100;
            document.getElementById('score').innerText = score;
        } else { // 答錯了
            btn.classList.add('wrong');
            hp--;
            document.getElementById('hp').innerText = "❤️ ".repeat(hp) || "💀";
        }

        // 延遲一秒後進入下一題，讓使用者看清楚答案
        setTimeout(nextQuestion, 1000);
    }

    // 初始啟動第一題
    nextQuestion();
</script>

</body>
</html>