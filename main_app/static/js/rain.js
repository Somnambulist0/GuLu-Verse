const numberOfDrops = 100;

function createRain() {
    const rain = document.querySelector('.rain');

    for (let i = 0; i < numberOfDrops; i++) {
        const drop = document.createElement('div');
        drop.className = 'drop';
        drop.style.left = `${Math.random() * 100}vw`;
        drop.style.animationDuration = `${Math.random() * 3 + 0.5}s`;
        drop.style.animationDelay = `${Math.random() * 2}s`;
        rain.appendChild(drop);
    }
}

createRain();