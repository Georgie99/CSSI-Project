var buttons = document.querySelectorAll(".savebutton");
// let characterdiv = document.querySelectorAll("#character");
if(buttons){
  buttons.forEach(function(button){
    button.addEventListener('click', function(){
      fetch('/prefs?type=addChar&characterKey='+this.value+'&userId='+this.getAttribute('user_id'),{method:"post"});
      console.log(this.getAttribute('user_id'));
      // characterdiv.classList.toggle("tada fast");
    })
  }
  )
}
