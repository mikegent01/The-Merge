// Blinking effect for status indicators

// Blinking effect for status indicators
setInterval(blink, 500);

function blink() {
    $('.blink').each(function () {
        var backColor = $(this).css('background-color');
        var textColor = $(this).css('color');

        $(this).css('background', textColor);
        $(this).css('color', backColor);
    });
}


// Data for the entities
const entityData = {
    'Space Pipes': {
        image: '01.gif',
        audio: '0.wav',
        description: 'Space pipes are anomulous pipes that exist in damp spaces. These pipes emit a unquie hissing sound, the pipes produce dot-like particles that float around the pipe.',
        danger: 'Space pipes are dangerous and you should avoid making contact or breathing in the particles near the affected pipes. Space pipes while not hostile on their own inhibit a dangerous property. When interacted with space pipes will explode and spread there particles onto other pipes creating more space pipes. Breathing in the particles emitted by the pipes is also harmful to human health and can lead to drowsiness and shortness of breath. Falling asleep on uncontrolled pipes can also cause drowsiness and shortness of breath. Falling asleep next to a space pipe can lead to death by suffocation.', 
        solution: 'Space pipes can be stopped by drying out the general area they are located in. Once the space pipie is completedly dry it can be safely removed from the area. If you have come in contact with space pipes it is advisable to go through a full de-contamination process to assure you will not spread any of the particles onto other pipes.' 
    },
    'Entity 2': {
        image: 'house.png',
        audio: '1.wav',
        description: 'Description for Entity 2.',
        danger: 'Danger for Entity 2.',
        solution: 'Solution for Entity 2.'
    },
    'Entity 3': {
        image: 'https://via.placeholder.com/300',
        audio: '2.wav',
        description: 'Description for Entity 3.',
        danger: 'Danger for Entity 3.',
        solution: 'Solution for Entity 3.'
    }
};

// Function to display entity information
function showInfo(entityName) {
    const entity = entityData[entityName];

    // Update Title
    document.getElementById('infoTitle').textContent = entityName;

    // Update Image
    const imgElement = document.getElementById('infoImage');
    imgElement.src = entity.image;
    imgElement.style.display = 'block'; // Show the image

    // Update Audio
    const audioElement = document.getElementById('audioSample');
    const audioSource = document.getElementById('audioSource');
    audioSource.src = entity.audio;
    audioElement.load(); // Reload audio with new source
    document.querySelector('.audio-controls').style.display = 'block'; // Show audio controls

    // Update Description
    document.getElementById('descriptionText').textContent = entity.description;
    document.getElementById('dangerText').textContent = entity.danger;
    document.getElementById('solutionText').textContent = entity.solution;

    // Show the description area
    document.querySelector('.description-area').style.display = 'block';
}
