var num = document.querySelector("")

function fibonaci(num) {
  var array = [1,1]
  var x = 0
  var y = 1
  var limit = 2
  var iterations = 2

  var h1a = document.querySelector("#h1-a")
  var h1b = document.querySelector("#h1-b")



  var para2 = document.createElement("p");
  var para3 = document.createElement("p");
  var node1 = document.createTextNode("Iterations: 1 "+"fibonaci: "+1);
  var node2 = document.createTextNode("Iterations: 2 "+"fibonaci: "+1);
  para2.appendChild(node1);
  para3.appendChild(node2);
  var element = document.getElementById("div1");
  element.appendChild(para2);
  element.appendChild(para3)

  while(limit < num) {
   var answer = BigInt(array[x]) + BigInt(array[y])
    array.push(answer)
    x++
    y++
    limit++
    iterations++
    var para = document.createElement("p");

    var node3 = document.createTextNode("iterations: "+iterations+' '+"fibonaci: "+ answer);
    para.appendChild(node3);
    var element = document.getElementById("div1");
    element.appendChild(para);

  }
  h1a.innerHTML = "Total Number of iterations:"+ iterations
  h1b.innerHTML = "Greatest fibonaci number: " +answer

}
var result= fibonaci(10)
