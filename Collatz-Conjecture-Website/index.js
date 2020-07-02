function erase() {
  var child = document.getElementById('lever');
  var child2 = document.getElementById('Monserat');

  // var parent = document.getElementById('parent');
  // parent.removeChild(child);
  // parent.removeChild(child2);
  child2.innerHTML = " "
  child.innerHTML = " "
}




function Collatz() {

  var input = document.querySelector('#inputed').value
  console.log(input);
  var tag = document.querySelector('#lever')
  var sag = document.querySelector('#Monserat')

  var num = input
  var iterations = 1;
  var element = document.querySelector("#Monserat")
  var element2 = document.querySelector("#lever")


  element2.innerHTML = 'iteration number   : '+iterations+",  "+num

  while (num !=1) {
    iterations++
    if (num%2 == 0) {
      num = num/2
      var par = document.createElement("div")
      var par2 = document.createElement("br")
      var node = document.createTextNode('iteration number +   : '+iterations+",  "+num)
      par.appendChild(node);
      element.appendChild(node)
      element.appendChild(par2)
    }else if (num %2 !=0) {
      num = (num*3)+1

       var par2 = document.createElement("br")
       var par = document.createElement("div")
       var node = document.createTextNode('iteration number -   : '+iterations+",  "+num)
       par.appendChild(node);
       element.appendChild(node)
       element.appendChild(par2)



    }

  }

}
