var buttons = document.querySelectorAll(".savebutton");
if(buttons){
  buttons.forEach(function(button){
    button.addEventListener('click', function(){
      fetch('/prefs?type=addChar&characterKey='+this.value+'&userId='+this.getAttribute('user_id'),{method:"post"});
      console.log(this.getAttribute('user_id'));
    })
  }
  )
}
