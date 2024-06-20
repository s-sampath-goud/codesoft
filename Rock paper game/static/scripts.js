async function play(userChoice) {
    const response = await fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ choice: userChoice }),
    });

    const data = await response.json();
    document.getElementById('user-choice').innerText = `Your choice: ${data.user_choice}`;
    document.getElementById('computer-choice').innerText = `Computer's choice: ${data.computer_choice}`;
    document.getElementById('game-result').innerText = `Result: ${data.round_winner}`;
    document.getElementById('player-score').innerText = data.player_score;
    document.getElementById('computer-score').innerText = data.computer_score;
    document.getElementById('moves-left').innerText = data.moves_left;

    if (data.moves_left === 0) {
        const finalResult = data.player_score > data.computer_score ? 'You win!' : data.player_score < data.computer_score ? 'Computer wins!' : 'It\'s a tie!';
        document.getElementById('game-result').innerText = `Game Over! ${finalResult}`;
    }
}

function resetGame() {
    document.getElementById('user-choice').innerText = 'Your choice: ';
    document.getElementById('computer-choice').innerText = 'Computer\'s choice: ';
    document.getElementById('game-result').innerText = 'Result: ';
    document.getElementById('player-score').innerText = '0';
    document.getElementById('computer-score').innerText = '0';
    document.getElementById('moves-left').innerText = '10';

    fetch('/reset', {
        method: 'POST',
    });
}
