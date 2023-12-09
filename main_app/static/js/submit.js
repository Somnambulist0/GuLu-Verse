document.getElementById('joinForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);

    fetch('/submit-form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: json
    })
    .then(response => response.json())
    .then(data => {
        alert('Thank you for your submission!');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});