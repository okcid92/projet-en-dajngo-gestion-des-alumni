document.addEventListener('DOMContentLoaded', function() {
    // Animation des nombres
    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.innerHTML = Math.floor(progress * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // Animer les compteurs en lisant les attributs data-count des cartes
    const statisticCards = document.querySelectorAll('.card[data-count]');

    statisticCards.forEach(card => {
        const countElement = card.querySelector('.display-4');
        const targetValue = parseInt(card.dataset.count);

        if (countElement && !isNaN(targetValue)) {
            animateValue(countElement, 0, targetValue, 1000);
        }
    });
}); 