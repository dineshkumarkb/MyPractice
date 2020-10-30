// for(var i=0;i < 5;i++){
//   console.log("Hello");
// }
//
// for(var i =0;i <= 25;i++){
//   if(i%2!==0){
//     console.log(i);
//   }
// }

var fname = prompt("Please enter your first name");
var lname = prompt("Please enter your last name");
var age = prompt(" Please enter your age ");
var height = prompt("Enter your height");
var petname = prompt("Enter your petname");



if(fname[0] === lname[0] && (age > 20 && age < 30) && height >= 170 && petname[petname.length-1] === "y"){
  console.log("Welcome spy! You have passed the test");

}
