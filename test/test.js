function selco(element)
{ 
    c = element.innerHTML
    let d = document.getElementById('cart')
    ch = document.createElement('div')
    ch.innerHTML = '<div id ="m4" ><h2 class="names">'+c+'</h2><input type="number" id="nu" value="1" min="1" class="chim"><button id="de" onclick="delo(this)">Remove</button></div>'
    d.appendChild(ch)
         }
function delo(delement)
{
    alert(delement.innerHTML)
    delement.parentElement.remove()
}



    function check(){
     var pro = document.getElementsByClassName("names")
     var prot = document.getElementsByClassName("chim")
     var prod = []
     var quan = []
      for ( var i=0 ; i<pro.length; i++)
                  {
                    prod.push(pro[i].textContent)
                    quan.push(prot[i].value)
                  }
                console.log(prod)
                console.log(quan)
                let p = prod.toString()
                let q = quan.toString()
                jQuery.ajax({
                    url:'see/',
                    type: 'POST',
                    data: {'p': p, 'q':q},
                    dataType: 'json',
                    success: function(){
                          alert('done');
                    },
            
                });
                
            }
            function jq(){
                jQuery.ajax({
                    url:'see/',
                    type: 'POST',
                    data: prod,
                    success: function(){
                          alert('done');
                    },
            
                });
            }
            