document.addEventListener('DOMContentLoaded', () => {
    // --- Configuration ---
    const TUNING_THRESHOLD = 0.050; // MHz tolerance for tuning
    const MIN_MESSAGE_DELAY = 5000; // 5 seconds (ms)
    const MAX_MESSAGE_DELAY = 15000; // 15 seconds (ms)

    // --- Frequency Ranges ---
    const frequencyRanges = {
        'civil': { min: 26.965, max: 27.405, default: 27.185 },
        'secure': { min: 30.000, max: 88.000, default: 45.500 }
    };

    // --- Target Frequencies (Where static/messages trigger) ---
    const targetFrequencies = {
        'civil': [27.185], // Example CB channel 19
        'secure': [45.500, 75.125] // Example military frequencies
    };

    // --- NEW: Label-Specific Audio Mapping ---
    // Structure: labelAudioMap[labelValue][channel][frequency] = [audioFile1, audioFile2, ...]
    // Note: Frequencies here MUST match targetFrequencies and use .toFixed(3) format.
    const labelAudioMap = {
        'bootcampinsideprojectorroomstart': {
            'secure': {
                '45.500': ['audio/1.wav', 'audio/2.mp3'], // Military-style messages
                '75.125': ['audio/0.wav']                 // Another secure message/sound
            }
            // Add civil messages for this label if needed
            // 'civil': {
            //     '27.185': ['audio/some_other_file.wav']
            // }
        },
        'some_other_label': { // Example for a different scenario
            'civil': {
                '27.185': ['audio/a1.wav', 'audio/a2.wav'] // Civilian-style messages
            }
            // Add secure messages for this label if needed
        },
        // Add more labels and their corresponding audio files here
        'default_label_if_needed': {
             'civil': { '27.185': ['audio/a1.wav'] },
             'secure': { '45.500': ['audio/0.wav'] }
        }
    };

    // --- DOM Elements ---
    const container = document.getElementById('draggable-radio');
    const dragHandle = document.getElementById('drag-handle');
    const statusDisplay = document.getElementById('radio-status');
    const channelDisplay = document.getElementById('radio-channel-display');
    const frequencyDisplay = document.getElementById('frequency-display');
    const powerIndicator = document.getElementById('power-indicator');
    const powerButton = document.getElementById('power-button');
    const channelButtons = document.querySelectorAll('.channel-button');
    const volumeKnob = document.getElementById('volume-knob');
    const volumeIndicator = document.getElementById('volume-indicator');
    const tuningKnob = document.getElementById('tuning-knob');
    const tuningIndicator = document.getElementById('tuning-indicator');

    const staticAudio = document.getElementById('static-audio');
    const messageAudio = document.getElementById('message-audio');

    // --- State Variables ---
    let isOn = false;
    let currentChannel = null;
    let currentFrequency = 0;
    let volumeLevel = 0.5;
    let tuningRotation = 135;
    let isDraggingKnob = false;
    let isDraggingRadio = false;
    let dragOffsetX, dragOffsetY;
    let messageTimeoutId = null;
    let currentLabel = null; // Store the detected valid label
    let hasValidLabel = false; // Flag if *any* known label is detected

    // --- Helper Functions ---
    function getUrlParameter(name) {
        const params = new URLSearchParams(window.location.search);
        return params.get(name);
    }

    function updateDisplay() {
        if (isOn) {
            statusDisplay.textContent = 'STATUS: ONLINE';
            powerIndicator.classList.add('on');
            channelDisplay.textContent = currentChannel ? `CH: ${currentChannel.toUpperCase()}` : 'CH: --';
            frequencyDisplay.textContent = currentChannel ? `${currentFrequency.toFixed(3)} MHz` : '---.--- MHz';
            channelButtons.forEach(btn => {
                btn.classList.toggle('active', btn.dataset.channel === currentChannel);
            });
        } else {
            statusDisplay.textContent = 'STATUS: OFF';
            powerIndicator.classList.remove('on');
            channelDisplay.textContent = 'CH: --';
            frequencyDisplay.textContent = '---.--- MHz';
            channelButtons.forEach(btn => btn.classList.remove('active'));
        }
        volumeIndicator.style.transform = `translateX(-50%) rotate(${volumeLevel * 270}deg)`;
        tuningIndicator.style.transform = `translateX(-50%) rotate(${tuningRotation}deg)`;
    }

    function stopAllAudio() {
        clearTimeout(messageTimeoutId);
        messageTimeoutId = null;
        if (!staticAudio.paused) {
            staticAudio.pause();
            staticAudio.currentTime = 0;
        }
        if (!messageAudio.paused) {
            messageAudio.pause();
            messageAudio.currentTime = 0;
        }
    }

    function playStatic() {
        if (!isOn || !currentChannel) return;
        // Check if already playing to avoid interrupting seeks etc.
        if (staticAudio.paused) {
            console.log("Attempting to play static...");
            staticAudio.volume = volumeLevel * 0.7;
            staticAudio.currentTime = 0; // Reset position
             // Use a promise to handle potential play interruptions
            staticAudio.play().then(() => {
                 console.log("Static playing.");
            }).catch(e => {
                // Ignore errors often caused by rapid start/stop, but log others
                if (e.name !== 'AbortError') {
                    console.error("Error playing static:", e);
                }
            });
        }
    }

    function scheduleRandomMessage(tunedFrequency) {
        // Messages only play if a *valid label* was detected on page load
        if (!hasValidLabel || !isOn || !currentChannel || !currentLabel) {
             console.log("Conditions not met for scheduling message (No valid label, off, no channel).");
             return;
        }

        // --- MODIFIED: Look up messages based on the detected label ---
        const messagesForLabelFreq = labelAudioMap[currentLabel]?.[currentChannel]?.[tunedFrequency.toFixed(3)];
        // --- End Modification ---

        if (!messagesForLabelFreq || messagesForLabelFreq.length === 0) {
            console.log(`No specific messages defined for label '${currentLabel}', channel ${currentChannel}, freq ${tunedFrequency.toFixed(3)} MHz.`);
            // If no messages, just let static play. Don't clear timeout here, static is handled elsewhere.
            return;
        }

        clearTimeout(messageTimeoutId); // Clear previous scheduled message (if any)

        const delay = Math.random() * (MAX_MESSAGE_DELAY - MIN_MESSAGE_DELAY) + MIN_MESSAGE_DELAY;
        console.log(`Scheduling message for label '${currentLabel}' at ${tunedFrequency.toFixed(3)} in ${Math.round(delay / 1000)}s`);

        messageTimeoutId = setTimeout(() => {
            // Re-check conditions *just before* playing
            if (!isOn || currentChannel === null || Math.abs(currentFrequency - tunedFrequency) > TUNING_THRESHOLD || !hasValidLabel) {
                console.log("Conditions changed before message could play. Aborting message.");
                stopAllAudio(); // Make sure static stops if tuned away or turned off
                return;
            }

            const messageIndex = Math.floor(Math.random() * messagesForLabelFreq.length);
            const messageSrc = messagesForLabelFreq[messageIndex];
            console.log(`Playing message: ${messageSrc}`);

            if (!staticAudio.paused) staticAudio.pause(); // Pause static

            messageAudio.src = messageSrc;
            messageAudio.volume = volumeLevel;
            messageAudio.play().then(() => {
                 messageAudio.onended = () => {
                    console.log("Message finished.");
                    messageAudio.onended = null;
                    // Restart static AND schedule next message IF still tuned correctly
                    if (isOn && currentChannel && Math.abs(currentFrequency - tunedFrequency) <= TUNING_THRESHOLD && hasValidLabel) {
                        console.log("Restarting static and scheduling next message.");
                        playStatic();
                        scheduleRandomMessage(tunedFrequency); // Recursive call for next message
                    } else {
                        console.log("Conditions changed after message finished. Not restarting static/scheduling.");
                        stopAllAudio();
                    }
                };
            }).catch(e => {
                console.error("Error playing message:", e);
                 // If message fails, cautiously restart static and reschedule
                 if (isOn && currentChannel && Math.abs(currentFrequency - tunedFrequency) <= TUNING_THRESHOLD && hasValidLabel) {
                    playStatic();
                    scheduleRandomMessage(tunedFrequency);
                }
            });

        }, delay);
    }

     function checkTuning() {
        if (!isOn || !currentChannel) {
            stopAllAudio();
            return;
        }

        let isTuned = false;
        let tunedTargetFreq = null;

        if (targetFrequencies[currentChannel]) {
            for (const targetFreq of targetFrequencies[currentChannel]) {
                if (Math.abs(currentFrequency - targetFreq) <= TUNING_THRESHOLD) {
                    isTuned = true;
                    tunedTargetFreq = targetFreq;
                    break;
                }
            }
        }

        if (isTuned) {
            // Only start static/schedule if static isn't already playing for this frequency
            if (staticAudio.paused) {
                console.log(`Tuned to ${tunedTargetFreq.toFixed(3)} MHz! Starting static.`);
                playStatic();
                // Schedule message *only if* a valid label was detected on load
                if (hasValidLabel) {
                     scheduleRandomMessage(tunedTargetFreq);
                } else {
                    console.log("Tuned, but no valid label detected. Static only.")
                }
            } else {
                 // Already tuned and static is playing, do nothing extra.
                 // The message loop handles rescheduling if applicable.
            }
        } else {
            // Not tuned to any target frequency, stop everything.
            if (!staticAudio.paused || messageTimeoutId !== null) {
                 console.log("Tuned away from target frequency. Stopping audio.");
                 stopAllAudio();
            }
        }
    }

    // --- Knob Drag Logic (Identical to previous version) ---
    function startKnobDrag(e, knobType) {
        e.preventDefault();
        isDraggingKnob = knobType;
        document.addEventListener('mousemove', handleKnobDrag);
        document.addEventListener('touchmove', handleKnobDrag, { passive: false });
        document.addEventListener('mouseup', stopKnobDrag);
        document.addEventListener('touchend', stopKnobDrag);
    }
    function handleKnobDrag(e) {
        if (!isDraggingKnob || !isOn) return;
        e.preventDefault();
        const knobElement = (isDraggingKnob === 'volume') ? volumeKnob : tuningKnob;
        const rect = knobElement.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;
        const angle = Math.atan2(clientY - centerY, clientX - centerX) * (180 / Math.PI) + 90;
        let rotation = angle < 0 ? angle + 360 : angle;
        rotation = Math.max(0, Math.min(270, rotation));

        if (isDraggingKnob === 'volume') {
            volumeLevel = rotation / 270;
            staticAudio.volume = volumeLevel * 0.7;
            if (!messageAudio.paused) messageAudio.volume = volumeLevel;
            volumeIndicator.style.transform = `translateX(-50%) rotate(${rotation}deg)`;
        } else if (isDraggingKnob === 'tuning' && currentChannel) {
            tuningRotation = rotation;
            const range = frequencyRanges[currentChannel];
            const freqSpan = range.max - range.min;
            currentFrequency = range.min + (tuningRotation / 270) * freqSpan;
            frequencyDisplay.textContent = `${currentFrequency.toFixed(3)} MHz`;
            tuningIndicator.style.transform = `translateX(-50%) rotate(${rotation}deg)`;
            checkTuning(); // Check tuning dynamically as knob moves
        }
    }
    function stopKnobDrag() {
        if (!isDraggingKnob) return;
        const wasTuning = (isDraggingKnob === 'tuning');
        isDraggingKnob = false;
        document.removeEventListener('mousemove', handleKnobDrag);
        document.removeEventListener('touchmove', handleKnobDrag);
        document.removeEventListener('mouseup', stopKnobDrag);
        document.removeEventListener('touchend', stopKnobDrag);
        // Final check ONLY if the tuning knob was released
        if (wasTuning && isOn && currentChannel) {
             checkTuning();
        }
    }

    // --- Radio Drag Logic (Identical to previous version) ---
    function startRadioDrag(e) { /* ... same as before ... */ }
    function handleRadioDrag(e) { /* ... same as before ... */ }
    function stopRadioDrag() { /* ... same as before ... */ }
    // --- [Copy the Radio Drag Logic functions from the previous answer here] ---
     function startRadioDrag(e) {
        e.preventDefault();
        isDraggingRadio = true;
        const rect = container.getBoundingClientRect();
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;
        dragOffsetX = clientX - rect.left;
        dragOffsetY = clientY - rect.top;
        container.style.cursor = 'grabbing';
        document.addEventListener('mousemove', handleRadioDrag);
        document.addEventListener('touchmove', handleRadioDrag, { passive: false });
        document.addEventListener('mouseup', stopRadioDrag);
        document.addEventListener('touchend', stopRadioDrag);
    }

    function handleRadioDrag(e) {
        if (!isDraggingRadio) return;
        e.preventDefault();
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;
        let newX = clientX - dragOffsetX;
        let newY = clientY - dragOffsetY;
        const maxX = window.innerWidth - container.offsetWidth;
        const maxY = window.innerHeight - container.offsetHeight;
        newX = Math.max(0, Math.min(maxX, newX));
        newY = Math.max(0, Math.min(maxY, newY));
        container.style.left = `${newX}px`;
        container.style.top = `${newY}px`;
    }

    function stopRadioDrag() {
        isDraggingRadio = false;
        container.style.cursor = 'default';
        dragHandle.style.cursor = 'move';
        document.removeEventListener('mousemove', handleRadioDrag);
        document.removeEventListener('touchmove', handleRadioDrag);
        document.removeEventListener('mouseup', stopRadioDrag);
        document.removeEventListener('touchend', stopRadioDrag);
    }


    // --- Event Listeners ---
    powerButton.addEventListener('click', () => {
        isOn = !isOn;
        console.log(`Power ${isOn ? 'ON' : 'OFF'}`);
        if (!isOn) {
            stopAllAudio();
            currentChannel = null;
        }
        updateDisplay();
         if (isOn && currentChannel) { // Re-check tuning if turning on with a channel selected
            checkTuning();
        }
    });

    channelButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (!isOn) return;
            const selectedChannel = button.dataset.channel;
            if (selectedChannel !== currentChannel) {
                console.log(`Channel selected: ${selectedChannel}`);
                stopAllAudio();
                currentChannel = selectedChannel;
                const range = frequencyRanges[currentChannel];
                currentFrequency = range.default;
                const freqSpan = range.max - range.min;
                tuningRotation = freqSpan > 0 ? ((currentFrequency - range.min) / freqSpan) * 270 : 135;
                tuningRotation = Math.max(0, Math.min(270, tuningRotation));
                updateDisplay();
                checkTuning(); // Check default frequency on channel change
            }
        });
    });

    volumeKnob.addEventListener('mousedown', (e) => startKnobDrag(e, 'volume'));
    volumeKnob.addEventListener('touchstart', (e) => startKnobDrag(e, 'volume'), { passive: false });
    tuningKnob.addEventListener('mousedown', (e) => startKnobDrag(e, 'tuning'));
    tuningKnob.addEventListener('touchstart', (e) => startKnobDrag(e, 'tuning'), { passive: false });

    dragHandle.addEventListener('mousedown', startRadioDrag);
    dragHandle.addEventListener('touchstart', startRadioDrag, { passive: false });

    // --- Initialization ---
    function initializeRadio() {
        // --- MODIFIED: Check URL Parameter against the map ---
        const labelFromUrl = getUrlParameter('lastLabel');
        console.log(`URL Parameter 'lastLabel': ${labelFromUrl}`);
        if (labelFromUrl && labelAudioMap[labelFromUrl]) {
            currentLabel = labelFromUrl; // Store the valid label found
            hasValidLabel = true;
            console.log(`Valid label '${currentLabel}' detected. Messages enabled for this label.`);
        } else {
            currentLabel = null;
            hasValidLabel = false;
            console.warn("No valid/known 'lastLabel' found in URL or map. Message playback disabled. Static will still play on tune.");
        }
        // --- End Modification ---

        const initialX = (window.innerWidth - container.offsetWidth) / 2;
        const initialY = (window.innerHeight - container.offsetHeight) / 2;
        container.style.left = `${initialX}px`;
        container.style.top = `${initialY}px`;
        staticAudio.volume = volumeLevel * 0.7;
        messageAudio.volume = volumeLevel;
        updateDisplay();
    }

    initializeRadio();
});