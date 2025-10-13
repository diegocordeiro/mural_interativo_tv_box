 (function(){
    var interval = 5000; // tempo entre slides
    var container = document.getElementById('carouselContainer');
    var items = container.getElementsByClassName('carousel-item');
    var index = 0;

    function showSlide(i){
    for(var j=0;j<items.length;j++){
        items[j].className = 'carousel-item';
    }
    items[i].className = 'carousel-item active';
    }

    function nextSlide(){
    index = (index + 1) % items.length;
    showSlide(index);
    // se chegou no último, recarrega página após intervalo
    if(index === items.length - 1){
        setTimeout(function(){ window.location.reload(); }, interval);
    }
    }

    setInterval(nextSlide, interval);
})();