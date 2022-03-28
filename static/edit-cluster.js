
  ////
// code to count number of times the site is loaded

let boolc = 1;


//////////////////

//////////////////// 

// code to hide and show videos' description on click

function hideDesc() {
  let list = document.getElementsByClassName("video_desc");
  for(var i=0; i<list.length; i++){
  if(boolc%2 == 0){
  list[i].style.display = 'block';
  }
  else{
  list[i].style.display = 'none';
  }
  }
  boolc++;
  }

  let sho2 = document.querySelector("#edit-cluster-show-2");
  sho2.addEventListener("click", show2);
  function show2(){
      console.log("show cluster 2");
      let child = document.querySelector(".edit-cluster-child-2");
      child.classList.add("edit-cluster-open-child-2");
      let parent = document.querySelector(".edit-cluster-parent-2");
      parent.classList.add("edit-cluster-open-2");
  
      var elems = document.getElementsByClassName('footer');
      for (var i=0;i<elems.length;i++){
          elems[i].style.display = 'none';
      }
  }
  
  document.querySelector("#hide-editcluster-popup-2").addEventListener("click", hide2);
  function hide2(){
      let child = document.querySelector(".edit-cluster-child-2");
      child.classList.remove("edit-cluster-open-child-2");
      let parent = document.querySelector(".edit-cluster-parent-2");
      parent.classList.remove("edit-cluster-open-2");
  
      var elems = document.getElementsByClassName('footer');
      for (var i=0;i<elems.length;i++){
          elems[i].style.display = 'block';
      }
  }

document.querySelector("#hide-editcluster-popup").addEventListener("click", hide);
let sho = document.querySelector("#edit-cluster-show");
sho.addEventListener("click", show);
function show(){
    console.log("show cluster");
    let child = document.querySelector(".edit-cluster-child");
    child.classList.add("edit-cluster-open-child");
    let parent = document.querySelector(".edit-cluster-parent");
    parent.classList.add("edit-cluster-open");

    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'none';
    }
}

document.querySelector("#hide-editcluster-popup").addEventListener("click", hide);
function hide(){
    let child = document.querySelector(".edit-cluster-child");
    child.classList.remove("edit-cluster-open-child");
    let parent = document.querySelector(".edit-cluster-parent");
    parent.classList.remove("edit-cluster-open");

    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'block';
    }
}

