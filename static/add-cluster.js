document.querySelector("#hide-addcluster-popup").addEventListener("click", hide);
let sho = document.querySelector("#add-cluster-show");
sho.addEventListener("click", show);
function show(){
    console.log("show cluster");
    let child = document.querySelector(".add-cluster-child");
    child.classList.add("add-cluster-open-child");
    let parent = document.querySelector(".add-cluster-parent");
    parent.classList.add("add-cluster-open");

    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'none';
    }
}

let hid = document.querySelector("#add-cluster-hide");
function hide(){
    let child = document.querySelector(".add-cluster-child");
    child.classList.remove("add-cluster-open-child");
    let parent = document.querySelector(".add-cluster-parent");
    parent.classList.remove("add-cluster-open");

    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'block';
    }
}

///arrange cluster

let btn = document.querySelector("#arrange-cluster-btn");
btn.addEventListener("click", arrangeClusterShow);


function arrangeClusterShow(){
    console.log("amansharma")
    let child2 = document.querySelector("#add-cluster-child2");
    child2.classList.add("add-cluster-open-child2");
    let parent = document.querySelector(".add-cluster-parent");
    parent.classList.add("add-cluster-open");
    
    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'none';
    }
}

function arrangeClusterHide(){
    let child2 = document.querySelector("#add-cluster-child2");
    child2.classList.remove("add-cluster-open-child2");
    let parent = document.querySelector(".add-cluster-parent");
    parent.classList.remove("add-cluster-open");

    var elems = document.getElementsByClassName('footer');
    for (var i=0;i<elems.length;i++){
        elems[i].style.display = 'block';
    }
}

