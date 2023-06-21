const gifContainer = document.getElementById('gif-container');
const generateButton = document.getElementById('generate-button');

generateButton.addEventListener('click', () => {
    fetch('/generate_gif', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            parameters: generateRandomParameters()
        })
    })
    .then(response => response.json())
    .then(data => {
        const gifId = data.gif_id;
        fetch(`/get_gif?gif_id=${gifId}`)
        .then(response => response.json())
        .then(data => {
            const gif = data.gif;
            const img = document.createElement('img');
            img.src = `img/${gif}`;
            gifContainer.appendChild(img);
        });
    });
});

function generateRandomParameters() {
    const parameters = [];
    for (let i = 0; i < 100; i++) {
        parameters.push(Math.random() * 2 - 1);
    }
    return parameters;
}
