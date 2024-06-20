let display = document.getElementById('display');

function clearDisplay() {
    display.textContent = '0';
}

function appendDisplay(value) {
    if (display.textContent === '0') {
        display.textContent = value;
    } else {
        display.textContent += value;
    }
}

function deleteLast() {
    display.textContent = display.textContent.slice(0, -1);
    if (display.textContent === '') {
        display.textContent = '0';
    }
}

function calculate() {
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: display.textContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            display.textContent = 'Error';
        } else {
            display.textContent = data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
