var votebuttons = document.querySelectorAll(".votebutton");
if(votebuttons){
  votebuttons.forEach(function(votebutton){
    votebutton.addEventListener('click', function(){
      fetch('/abt?characterKey='+this.value ,{method:"post"});
      console.log('i posted');
    })
  })
}
