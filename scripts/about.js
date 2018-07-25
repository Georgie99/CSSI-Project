const area = document.querySelector('.demo-card-image.mdl-card');
function name(n) {
  area.style.background = url
}

function gifs(name) {
  let n=Math.floor(Math.random() * 3) + 1
  return "../images/"+name+"/"+n+".gif"
}
function complete(z) {
  gifs(name(z))
}

area.addEventListener('onmouseover', complete({{character.name | safe}}))
