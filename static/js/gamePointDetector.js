//function to find game score and put it in console
var gameOff = 0;
const className = document.querySelector('.classnamePara').innerHTML;
function sender(score){
    //console.log('njan dhe senduane');
    fetch('/score?class=' + className + '&score=' + score).then(function (response)
    {
        return response.json();
    });
}
function chambikko(){
    gameOff = 0;
    var intervalid = setInterval(checkOpacity, 200);
    function checkOpacity(){
        const gameOver = document.querySelector('.game-over').children[0];
        const gameOverStyles = window.getComputedStyle(gameOver); 
        const gameOverOpacity = gameOverStyles.getPropertyValue('opacity');
        if (gameOverOpacity == "1"){
            //console.log('game score =' + document.querySelector('#score').innerHTML);
            sender(document.querySelector('#score').innerHTML);
            stopIt();
        }
    }
    function stopIt(){
        clearInterval(intervalid);
        gameOff = 1;
        window.addEventListener("keydown",function(e){
            //console.log("spacekey listen cheyth");
            if(e.key === " " && gameOff == 1){
                chambikko();
            }
        });
        window.addEventListener("click",function(e){
            //console.log("click listen cheyth");
            if(gameOff == 1){
                chambikko();
            }
        });
    }
}
chambikko();