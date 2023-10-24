const buttons = document.querySelectorAll('.ripple');
for (let button of buttons) {
    button.addEventListener('click', function(e) {
        const rect = e.target.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        e.target.style.setProperty('--x', x + 'px');
        e.target.style.setProperty('--y', y + 'px');
    });
}
