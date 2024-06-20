from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Initialize global variables
player_score = 0
computer_score = 0
moves_left = 10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global player_score, computer_score, moves_left
    user_choice = request.json['choice']
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    
    if result == 'win':
        player_score += 1
        round_winner = 'You win this round!'
    elif result == 'lose':
        computer_score += 1
        round_winner = 'Computer wins this round!'
    else:
        round_winner = "It's a tie!"
    
    moves_left -= 1
    
    if moves_left == 0:
        if player_score > computer_score:
            round_winner = 'Game Over! You win!'
        elif player_score < computer_score:
            round_winner = 'Game Over! Computer wins!'
        else:
            round_winner = 'Game Over! It\'s a tie!'
    
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'player_score': player_score,
        'computer_score': computer_score,
        'moves_left': moves_left,
        'round_winner': round_winner
    })

@app.route('/reset', methods=['POST'])
def reset():
    global player_score, computer_score, moves_left
    player_score = 0
    computer_score = 0
    moves_left = 10
    return '', 204

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

if __name__ == '__main__':
    app.run(debug=True)
