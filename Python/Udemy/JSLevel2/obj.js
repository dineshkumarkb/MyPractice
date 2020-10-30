var employee = {

  name:"John Smith",
  job:"Programmer",
  age:31

}


function nameLength(){
  console.log(employee['name'].length);
}

function myAlert(){
  for (var i in employee){
    alert(i + " is " + employee[i]);
    console.log(i + " is " + employee[i]);
  }
}

function lastName(){
  var name = employee["name"]
  var lname = name.split(" ")
  console.log(lname[1]);
}
