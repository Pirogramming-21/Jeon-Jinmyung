document.addEventListener('DOMContentLoaded', (event) => {
    let targetNumbers = [];
    let attempts = 9;

    function initializeGame() {
        targetNumbers = generateRandomNumbers();
        attempts = 9;
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        document.querySelector('.result-display').innerHTML = '';
        document.getElementById('game-result-img').src = '';
        document.querySelector('.submit-button').disabled = false;
    }

    function generateRandomNumbers() {
        const numbers = [];
        while (numbers.length < 3) {
            const num = Math.floor(Math.random() * 10);
            if (!numbers.includes(num)) {
                numbers.push(num);
            }
        }
        return numbers;
    }

    function check_numbers() {
        const input1 = document.getElementById('number1').value;
        const input2 = document.getElementById('number2').value;
        const input3 = document.getElementById('number3').value;

        if (input1 === '' || input2 === '' || input3 === '') {
            return;
        }

        const inputNumbers = [parseInt(input1), parseInt(input2), parseInt(input3)];

        if (new Set(inputNumbers).size !== inputNumbers.length) {
            alert("중복되지 않는 숫자를 입력하세요.");
            return;
        }

        const result = getResult(inputNumbers);
        displayResult(inputNumbers, result);
        checkGameStatus(result);

        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        attempts--;
    }

    function getResult(inputNumbers) {
        let strikes = 0;
        let balls = 0;

        inputNumbers.forEach((num, index) => {
            if (num === targetNumbers[index]) {
                strikes++;
            } else if (targetNumbers.includes(num)) {
                balls++;
            }
        });

        return { strikes, balls };
    }

    function displayResult(inputNumbers, result) {
        const resultDisplay = document.querySelector('.result-display');
        const checkResult = document.createElement('div');
        checkResult.className = 'check-result';

        const left = document.createElement('div');
        left.className = 'left';
        left.textContent = inputNumbers.join(' ');

        const right = document.createElement('div');
        right.className = 'right';

        if (result.strikes === 0 && result.balls === 0) {
            const out = document.createElement('div');
            out.className = 'out num-result';
            out.textContent = 'O';
            right.appendChild(out);
        } else {
            if (result.strikes > 0) {
                const strike = document.createElement('div');
                strike.className = 'strike num-result';
                strike.textContent = `${result.strikes} S`;
                right.appendChild(strike);
            }
            if (result.balls > 0) {
                const ball = document.createElement('div');
                ball.className = 'ball num-result';
                ball.textContent = `${result.balls} B`;
                right.appendChild(ball);
            }
        }

        checkResult.appendChild(left);
        checkResult.appendChild(document.createTextNode(':'));
        checkResult.appendChild(right);
        resultDisplay.appendChild(checkResult);
    }

    function checkGameStatus(result) {
        if (result.strikes === 3) {
            document.getElementById('game-result-img').src = 'success.png';
            document.querySelector('.submit-button').disabled = true;
        } else if (attempts <= 1) {
            document.getElementById('game-result-img').src = 'fail.png';
            document.querySelector('.submit-button').disabled = true;
        }
    }

    initializeGame();
    window.check_numbers = check_numbers;
});
