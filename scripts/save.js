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

var votebuttons = document.querySelectorAll(".votebutton");
if(votebuttons){
  votebuttons.forEach(function(votebutton){
    votebutton.addEventListener('click', function(){
      fetch('/prefs?type=addVote&characterKey='+this.value ,{method:"post"});
      console.log('i posted');
    })
  })
}
