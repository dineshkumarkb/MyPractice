var resetButton = document.getElementById("reset")

resetButton.addEventListener("click",resetBoard)


var squares = document.querySelectorAll('td')


function resetBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = " ";
  }
}

function setValues(){
  if(this.textContent === " "){
    this.textContent = "X";
  }
  else if(this.textContent === "X"){
    this.textContent = "O";
  }
  else{
    this.textContent = " ";
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click",setValues);
}
