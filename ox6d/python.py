function updateCountdown(time) {
        const days = Math.floor(time / (3600 * 24));
        const hours = Math.floor((time % (3600 * 24)) / 3600);
        const minutes = Math.floor((time % 3600) / 60);
        const seconds = time % 60;

        const countdownElement = document.getElementById('countdown');
        if (time > 0) {
            countdownElement.innerHTML = `
                
            <center><img src=centerm.png alt = « image illustration » width="480px" height="270px" /></center>
                 <p> ⏳  ${days}d ${hours}h ${minutes}m ${seconds}s ⏳ </p>
            `;
        } else {
            countdownElement.innerHTML = ''; // Masquer le contenu
        }
    }

    function startCountdown(durationInSeconds) {
        let countdown = durationInSeconds;
        const countdownInterval = setInterval(function () {
            updateCountdown(countdown);

            if (--countdown < 0) {
                clearInterval(countdownInterval);
                document.getElementById('redirect-link').style.display = 'block';
            }
        }, 1000);
    }
// Date et heure cible
    const targetDate = new Date('2024-03-29T19:00:00'); // Remplacez par votre date et heure cible
// Calcul du temps restant jusqu'à la date cible
    const now = new Date();
    const timeUntilTarget = Math.floor((targetDate - now) / 1000); // Conversion en secondes
    startCountdown(timeUntilTarget);
    
   
