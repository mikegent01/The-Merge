document.addEventListener('DOMContentLoaded', () => {
    // --- Configuration ---
    const debugMode = true; // SET TO true FOR 0-5 second waits, false for 0-300 second waits
    const minWaitSeconds = debugMode ? 0 : 0;
    const maxWaitSeconds = debugMode ? 50 : 300; // 300 seconds = 5 minutes // Adjusted debug max wait

    // --- Get DOM Elements ---
    const audioElement = document.getElementById('radio-audio');
    const beepAudioElement = document.getElementById('beep-audio'); // <<< GET BEEP ELEMENT
    const statusDisplay = document.getElementById('radio-status');
    const channelDisplay = document.getElementById('radio-channel-display');
    const signalLevelDisplay = document.getElementById('signal-level');
    const locationDisplay = document.getElementById('location-context');
    const powerButton = document.getElementById('power-button');
    const powerIndicator = document.getElementById('power-indicator');
    const channelButtons = document.querySelectorAll('.channel-button');

    // --- State Variables ---
    let isOn = false;
    let currentChannel = null;
    let lastLabel = 'Unknown';
    let currentAudioContext = null;
    let playedSpecificAudio = new Set();
    let isWaitingForNextAudio = false;
    let staticTimerId = null;
    let isPermanentStatic = false;
    let isBeeping = false; // <<< Flag to track if beep is playing

    // --- Get lastLabel from URL ---
    function getQueryParam(param) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }
    lastLabel = getQueryParam('lastLabel') || 'Unknown';
    if (locationDisplay) {
       // locationDisplay.textContent = `LOC: ${lastLabel}`; // Keep commented if not needed
    } else {
        console.warn("Element with ID 'location-context' not found.");
    }

    // --- Configuration Maps ---

    // ** Signal Strength Map **
    const signalStrengthMap = {
        'FrontSeat': 'STRONG',
        'bootcampinsideprojectorroomstart': 'STRONG',
        'stairwell': 'MODERATE',
        'outsideprojectorroom': 'STRONG',
        'storageroom': 'WEAK',
        'laboratory': 'NONE',
        'outsideclosetroom': 'STRONG',
        'outsidecaferoom': 'STRONG',
        'bg militaryentrance': 'STRONG',
        'bg maindeskentrance': 'STRONG',
        'apple': 'WEAK',
        'mirrorstorage': 'WEAK',
        'default': 'MODERATE'
    };

    // ** Audio Mapping Structure **
    // Paths are relative to the htmls/ folder (e.g., game/htmls/audio/...)
    // UPDATE THIS WITH YOUR ACTUAL FILES AND STRUCTURE
    const audioMap = {
        '1': { // Channel 1
            'FrontSeat': { // Label
                specific: ['audio/1.wav', 'audio/frontseat_extra1.mp3', 'audio/frontseat_extra2.wav'], // List of specific sounds
                static: 'audio/static_low.wav', // Static sound for this context
                playSpecificFirst: true // Start with a specific sound?
            },
            'bootcampinsideprojectorroomstart': {
                specific: ['audio/a1.wav', 'audio/a2.wav'],
                static: 'audio/2.mp3',
                playSpecificFirst: true
            },
            // Add other labels for channel 1...
            'default': { // Default for channel 1 if label not found
                specific: [], // No specific audio
                static: 'audio/placeholder_static.mp3',
                playSpecificFirst: false // Start with static
            }
        },
        '2': { // Channel 2 - Example starting with static
             'default': {
                specific: ['audio/channel2_message1.wav', 'audio/channel2_anomaly.mp3'],
                static: 'audio/placeholder_static.mp3',
                playSpecificFirst: false // Start with static, then play specific randomly
            }
        },
        '3': { // Channel 3 - Example with only static
             'default': {
                specific: [],
                static: 'audio/placeholder_static.mp3',
                playSpecificFirst: false
            }
        },
        // Add channels 4, 5, 6 with similar structures...
        '4': { 'default': { specific: [], static: 'audio/placeholder_static.mp3', playSpecificFirst: false } },
        '5': { 'default': { specific: [], static: 'audio/placeholder_static.mp3', playSpecificFirst: false } },
        '6': { 'default': { specific: [], static: 'audio/placeholder_static.mp3', playSpecificFirst: false } }
    };

    // --- Helper Functions ---
    function getAudioContext(channel, label) {
        if (audioMap[channel]) {
            return audioMap[channel][label] || audioMap[channel]['default'];
        }
        // Fallback if channel doesn't exist
        console.warn(`Channel ${channel} not found in audioMap. Using default static.`);
        return { specific: [], static: 'audio/placeholder_static.mp3', playSpecificFirst: false };
    }

    function getFullUrl(relativePath) {
        // Ensure relativePath is a string and not empty
        if (typeof relativePath !== 'string' || !relativePath) {
            console.error("Invalid relative path provided to getFullUrl:", relativePath);
            return null; // Or handle error appropriately
        }
        try {
            return new URL(relativePath, window.location.href).href;
        } catch (e) {
            console.error(`Error creating URL from relative path "${relativePath}":`, e);
            return null; // Or handle error appropriately
        }
    }

    function logDebug(message) {
        if (debugMode) {
            console.log(`[DEBUG] ${message}`);
        }
    }

    // --- Core Audio Functions ---

    function updateDisplay() {
        if (isOn) {
            statusDisplay.textContent = 'STATUS: ONLINE';
            if (powerIndicator) powerIndicator.classList.add('on');

            if (currentChannel) {
                channelDisplay.textContent = `CH: ${currentChannel}`;
                const strength = signalStrengthMap[lastLabel] || signalStrengthMap['default'];
                signalLevelDisplay.textContent = strength;
            } else {
                channelDisplay.textContent = 'CH: --';
                signalLevelDisplay.textContent = 'N/A';
            }
        } else {
            statusDisplay.textContent = 'STATUS: OFF';
            channelDisplay.textContent = 'CH: --';
            signalLevelDisplay.textContent = 'N/A';
            if (powerIndicator) powerIndicator.classList.remove('on');
        }
    }

    function playSpecificAudio(audioPath) {
        if (!isOn) return;
        logDebug(`Playing specific audio: ${audioPath}`);
        isWaitingForNextAudio = false;
        isPermanentStatic = false;
        isBeeping = false; // No longer beeping
        clearTimeout(staticTimerId);

        const fullUrl = getFullUrl(audioPath);
        if (!fullUrl) return; // Stop if URL creation failed

        if (audioElement.src !== fullUrl || audioElement.paused) {
            audioElement.src = fullUrl;
            audioElement.load();
            audioElement.loop = false; // Ensure specific audio does not loop
            audioElement.play().then(() => {
                logDebug(`Successfully started: ${audioPath}`);
                playedSpecificAudio.add(audioPath); // Mark as played *after* successfully starting
            }).catch(e => console.warn("Specific audio play failed:", e));
        } else {
             logDebug(`Audio ${audioPath} already playing or set.`);
        }
        updateDisplay();
    }

    function playStaticAudio(loop = true) {
        if (!isOn || !currentAudioContext || !currentAudioContext.static) return;
        logDebug(`Playing static audio: ${currentAudioContext.static} (Loop: ${loop})`);

        const fullUrl = getFullUrl(currentAudioContext.static);
        if (!fullUrl) return; // Stop if URL creation failed

        // Only change source if needed, always set loop and play
        if (audioElement.src !== fullUrl || audioElement.loop !== loop) { // Also check if loop status needs changing
            audioElement.src = fullUrl;
            audioElement.load();
        }
        audioElement.loop = loop; // Control looping based on parameter
        // Play only if paused or source changed
        if (audioElement.paused || audioElement.src !== fullUrl) {
             audioElement.play().catch(e => console.warn("Static audio play failed:", e));
        }
        updateDisplay();
    }

    function playNextSpecificAudio() {
        if (!isOn || !currentAudioContext) return;
        logDebug("Attempting to play next specific audio...");
        isWaitingForNextAudio = false;
        clearTimeout(staticTimerId);

        const availableSpecific = currentAudioContext.specific.filter(
            audioPath => !playedSpecificAudio.has(audioPath)
        );

        if (availableSpecific.length > 0) {
            const randomIndex = Math.floor(Math.random() * availableSpecific.length);
            const nextAudio = availableSpecific[randomIndex];
            logDebug(`Found ${availableSpecific.length} unplayed specific audio. Will beep before: ${nextAudio}`);

            // --- Play Beep First ---
            if (beepAudioElement && beepAudioElement.src && !beepAudioElement.src.endsWith('/')) { // Check if beep element and src exist and is valid
                isBeeping = true; // Set beeping flag

                // Define the handler that will play the specific audio AFTER the beep
                const playSpecificAfterBeep = () => {
                    beepAudioElement.removeEventListener('ended', playSpecificAfterBeep); // Clean up listener immediately
                    isBeeping = false; // Clear beeping flag
                    // Double-check state in case it changed during the beep
                    if (isOn && currentChannel) {
                        playSpecificAudio(nextAudio);
                    } else {
                        logDebug("State changed during beep, cancelling specific audio play.");
                    }
                };

                // Add listener that runs only once
                beepAudioElement.addEventListener('ended', playSpecificAfterBeep, { once: true });

                // Play the beep
                beepAudioElement.currentTime = 0; // Rewind beep
                beepAudioElement.play().catch(e => {
                    console.warn("Beep play failed:", e);
                    beepAudioElement.removeEventListener('ended', playSpecificAfterBeep); // Clean up listener on error
                    isBeeping = false; // Clear beeping flag on error
                    // If beep fails, play specific audio immediately as a fallback.
                    playSpecificAudio(nextAudio); // Fallback
                });
            } else {
                // If beep element doesn't exist or has no source, play specific audio directly
                logDebug("Beep element/src not found or invalid, playing specific audio directly.");
                playSpecificAudio(nextAudio);
            }
            // --- End Beep Logic ---

        } else {
            logDebug("No unplayed specific audio left. Switching to permanent static.");
            isPermanentStatic = true;
            playStaticAudio(true); // Play static indefinitely (loop=true)
        }
    }

    function playStaticAndScheduleNext() {
        if (!isOn || !currentAudioContext) return; // Check if radio is on and context exists

        if (isPermanentStatic) {
            logDebug("In permanent static mode. Ensuring static loop.");
            playStaticAudio(true); // Ensure static is playing and looping
            return;
        };

        logDebug("Playing static and scheduling next specific audio check...");
        playStaticAudio(true); // Play static (looping while waiting)
        isWaitingForNextAudio = true;

        const waitTime = (Math.random() * (maxWaitSeconds - minWaitSeconds) + minWaitSeconds) * 1000; // Time in milliseconds
        logDebug(`Waiting for ${waitTime / 1000} seconds before next specific audio.`);

        clearTimeout(staticTimerId); // Clear previous timer if any
        staticTimerId = setTimeout(() => {
            // Check state again before playing - crucial!
            if (isOn && currentChannel && isWaitingForNextAudio) {
                playNextSpecificAudio();
            } else {
                logDebug("Timer fired, but state changed (off/channel switch/no longer waiting). Aborting scheduled play.");
                isWaitingForNextAudio = false; // Ensure flag is cleared if timer aborted
            }
        }, waitTime);
    }

    function stopAudio() {
        logDebug("Stopping all audio and timers.");
        clearTimeout(staticTimerId);
        staticTimerId = null;
        isWaitingForNextAudio = false;
        isPermanentStatic = false;
        isBeeping = false; // Clear beeping flag

        // Stop main audio
        if (audioElement && !audioElement.paused) {
            audioElement.pause();
            audioElement.currentTime = 0;
        }
        if (audioElement) audioElement.loop = false; // Ensure loop is off

        // Stop beep audio
        if (beepAudioElement && !beepAudioElement.paused) {
            beepAudioElement.pause();
            beepAudioElement.currentTime = 0;
            logDebug("Beep audio stopped.");
            // Note: {once: true} listener should self-remove, but explicit removal is safer if needed.
            // However, managing the exact handler reference adds complexity. Relying on state checks.
        }

        updateDisplay();
    }

    function selectChannel(channel) {
        logDebug(`Selecting channel: ${channel}`);
        if (!isOn) {
            logDebug("Cannot select channel, radio is off.");
            return;
        }

        // Stop current playback and timers before switching
        stopAudio();

        // Update channel state
        currentChannel = channel;
        currentAudioContext = getAudioContext(channel, lastLabel);
        playedSpecificAudio = new Set(); // Reset played list for the new context
        isPermanentStatic = false; // Reset permanent static flag

        // Check if context is valid
        if (!currentAudioContext) {
            console.error(`Failed to get audio context for channel ${channel}, label ${lastLabel}. Cannot proceed.`);
            currentChannel = null; // Reset channel if context failed
            updateDisplay();
            return;
        }

        logDebug(`Audio context set. Specific: ${currentAudioContext.specific?.length || 0}, Static: ${currentAudioContext.static}, Play Specific First: ${currentAudioContext.playSpecificFirst}`);

        // Update button visuals
        channelButtons.forEach(btn => btn.classList.remove('active'));
        const selectedButton = document.querySelector(`.channel-button[data-channel="${channel}"]`);
        if (selectedButton) {
            selectedButton.classList.add('active');
        }

        // Decide initial playback based on context config
        if (currentAudioContext.playSpecificFirst && currentAudioContext.specific?.length > 0) {
            logDebug("Context starts with specific audio.");
            playNextSpecificAudio(); // This will beep then pick the first random specific one
        } else {
            logDebug("Context starts with static or has no specific audio.");
            playStaticAndScheduleNext(); // Start static and schedule the first specific check (if any specific exist)
        }

        updateDisplay(); // Update channel number, signal etc.
    }

    // --- Event Listeners ---
    if (powerButton) {
        powerButton.addEventListener('click', () => {
            isOn = !isOn;
            logDebug(`Power toggled: ${isOn ? 'ON' : 'OFF'}`);
            if (isOn) {
                // If turning on, re-initialize the current channel if one was selected
                if (currentChannel) {
                    // Re-run select logic to start sequence correctly
                    // Need a slight delay sometimes for audio context to be ready after power on? Test.
                    // setTimeout(() => selectChannel(currentChannel), 50); // Optional small delay
                    selectChannel(currentChannel);
                } else {
                    updateDisplay(); // Just update display if no channel selected yet
                }
            } else {
                stopAudio(); // Stop everything
                currentChannel = null; // Reset channel selection visually/logically
                channelButtons.forEach(btn => btn.classList.remove('active'));
                updateDisplay(); // Update display to OFF state
            }
        });
    } else {
        console.error("Power button not found.");
    }

    if (channelButtons.length > 0) {
        channelButtons.forEach(button => {
            button.addEventListener('click', () => {
                const channel = button.getAttribute('data-channel');
                // Only re-select if channel changed OR if it's the same channel but nothing is playing (e.g., after error)
                if (currentChannel !== channel || (currentChannel === channel && audioElement.paused && !isBeeping)) {
                    selectChannel(channel);
                } else {
                    logDebug(`Channel ${channel} already selected and playing/beeping.`);
                }
            });
        });
    } else {
        console.error("No channel buttons found.");
    }

    // --- Audio Element Event Listener (Main Radio Audio) ---
    audioElement.addEventListener('ended', () => {
        logDebug(`Audio ended: ${audioElement.src}`);
        // Get the expected full URL for the current context's static audio
        const staticFullUrl = currentAudioContext ? getFullUrl(currentAudioContext.static) : null;

        // Check if the audio that just ended was NOT the static audio for the current context
        if (staticFullUrl && audioElement.src === staticFullUrl) {
            // --- Static Audio Ended ---
            // The 'loop' attribute should handle restarting. This is a fallback/check.
            if (isPermanentStatic) {
                logDebug("Static ended in permanent mode, loop should restart it.");
                if (audioElement.paused) audioElement.play().catch(e => console.warn("Static loop restart failed:", e));
            } else if (isWaitingForNextAudio) {
                logDebug("Static ended while waiting for timer, loop should restart it.");
                if (audioElement.paused) audioElement.play().catch(e => console.warn("Static loop restart failed:", e));
            } else {
                logDebug("Static ended unexpectedly (not waiting, not permanent). Restarting loop.");
                 if (audioElement.paused) audioElement.play().catch(e => console.warn("Static loop restart failed:", e));
            }
        } else {
            // --- Specific Audio Ended ---
            // Only transition if radio is on, channel selected, and we weren't already waiting for the next timer
            if (isOn && currentChannel && !isWaitingForNextAudio && !isBeeping) {
                 logDebug("Specific audio finished, switching to static and scheduling next.");
                 playStaticAndScheduleNext(); // Play static and set timer for the *next* specific audio
            } else {
                 logDebug("Specific audio ended, but state indicates no action needed (e.g., turned off, channel changed, already waiting/beeping).");
            }
        }
    }); // <-- This closes the 'ended' listener function

    // --- Initial State ---
    updateDisplay(); // Set initial display based on default state (off)

}); // <-- This is the CORRECT closing brace and parenthesis for the main DOMContentLoaded listener
