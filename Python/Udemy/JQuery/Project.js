var p1 = prompt("Player One:Enter your name, you will be Blue");
var p1Color = 'rgb(18, 124, 218)';


var p2 = prompt("Player Two:Enter your name, you will be Red");
var p2Color = 'rgb(232, 40 ,37)';

//console.log("The player one is : " + p1);
//console.log("The player two is : " + p2);

var play1Text = $("h3").text();
var play2Text = "Player Two: it is your turn. Please pick a column to drop your red chip"

var table = $("table tr");

var btns = $('button');

// for(button of btns ){
//   button.addEventListener(click,"testFunction");
// }


function changeColor(rowIndex,colIndex,color){

  table.eq(rowIndex).find("td").eq(colIndex).find('button').css("background-color",color);

}

$('table button').on("click",function(){
  $(this).text("Clicked");
})
