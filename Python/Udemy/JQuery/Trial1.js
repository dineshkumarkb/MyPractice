var h1Text = $('h1');

function onHover(){

      $(this).text(" Mouse is over now ");

}

function onOut(){
  $(this).text("Selecting with jQuery");
}

h1Text[0].addEventListener("mouseover",onHover);
h1Text[0].addEventListener("mouseout",onOut)
$('input').eq(0).click(function(){
  $(this).attr("placeholder","Updated text")
})


h1Text[0].addEventListener("click",function(){
  $(this).text("Clicked");
})
