document.getElementById('generateButton').addEventListener('click', function() {
    const length = document.getElementById('length').value;
    const useUppercase = document.getElementById('useUppercase').checked;
    const useLowercase = document.getElementById('useLowercase').checked;
    const useNumbers = document.getElementById('useNumbers').checked;
    const useSymbols = document.getElementById('useSymbols').checked;

    fetch('/generate_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            length: parseInt(length),
            use_uppercase: useUppercase,
            use_lowercase: useLowercase,
            use_numbers: useNumbers,
            use_symbols: useSymbols
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('passwordDisplay').value = data.password;
    })
    .catch(error => console.error('Error:', error));
});
