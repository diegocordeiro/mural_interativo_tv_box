(function(){
    var displayTime = 20000; // tempo de exibição de cada slide (10s)
    var pauseTime = 0;   // pausa entre as transições
    var container = document.getElementById('carouselContainer');
    var items = container.getElementsByClassName('carousel-item');
    var index = 0;
    var timer;

    function showSlide(i){
        for (var j = 0; j < items.length; j++) {
            items[j].className = 'carousel-item';
        }
        items[i].className = 'carousel-item active';
    }

    function nextSlide(){
        // primeiro esconde o atual por um tempo (pausa)
        items[index].classList.remove('active');
        setTimeout(function(){
            index = (index + 1) % items.length;
            showSlide(index);

            // se chegou no último slide, recarrega após exibição
            if (index === items.length - 1) {
                setTimeout(function(){ window.location.reload(); }, displayTime);
            }
        }, pauseTime);
    }

    // inicia
    showSlide(index);
    timer = setInterval(nextSlide, displayTime + pauseTime);
})();
