roster = [];

while(true){

  var command = prompt("Please enter your command.Add,remove,display and quit?")

  if(command == "add"){

    var name = prompt("Please enter the student name");
    roster.push(name);

  }

  else if(command == "remove"){
    var name = prompt("Enter the name to be removed");
    var indexx = roster.indexOf(name);
    roster.splice(indexx,1);
    console.log(" The updated roster array is " + roster);
  }

  else if (command == "display") {
    for (elements of roster){
      console.log(elements);
    }

  }

  else if(command == "quit"){
    break;
  }

}
