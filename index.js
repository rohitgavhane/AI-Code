var randomNumber1 = Math.floor(Math.random() *6) +1;

var imgesrc = "dice" + randomNumber1 + ".png";

document.querySelectorAll("img")[0].setAttribute("src", imgesrc);


var randomNumber2 = Math.floor(Math.random() * 6 )+ 1;
var imagesrc2 = "dice" + randomNumber2 + ".png";
document.querySelectorAll("img")[1].setAttribute("src", imagesrc2);

if(randomNumber1 > randomNumber2){
    document.querySelector("h1").innerHTML = "Player One Wins!!😎";
}
else if( randomNumber1 < randomNumber2){
    document.querySelector("h1").innerHTML = "Player two Wins!!😎";
}
else{
    document.querySelector("h1").innerHTML = "Match Drawn 🤪😅"
}