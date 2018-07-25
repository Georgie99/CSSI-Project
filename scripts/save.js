var buttons = document.querySelectorAll(".savebutton");
if(buttons){
  buttons.forEach(function(button){
    button.addEventListener('click', function(){
      fetch('/prefs?type=addChar&characterKey='+this.value, {method:"post"})
      console.log('i posted')
    })
  }
  )
}
