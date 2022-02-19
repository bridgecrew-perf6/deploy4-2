 
////
// code to count number of times the site is loaded

let bool = 1;

        var n = localStorage.getItem('on_load_counter');
        
        if (n === null) {
            n = 0;
        }
        
        n++;
        
        localStorage.setItem("on_load_counter", n);

 //////////////////

//////////////////// 

// code to hide and show videos' description on click

function hide() {
var list = document.getElementsByClassName("video_description");
for(var i=0; i<list.length; i++){
    if(bool%2 == 0){
    list[i].style.display = 'block';
    }
    else{
    list[i].style.display = 'none';
    }
}
bool++;
}
//////////////////////


//////////////////////
//code to identify which description about site need to be shown

function myFunction() {
    //localStorage.setItem(localStorage.getItem("count"), localStorage.getItem("count")+1)
    localStorage.setItem("count",localStorage.getItem("count")+1);
    
    if(n%3 == 0){
      document.getElementById("desc").innerHTML = "Your search engine for visually appealing videos ";
    }
    if(n%3 == 1){
      document.getElementById("desc").innerHTML = "Collect videos from all across & store at one place ";
    }
    if(n%3 == 2){
      document.getElementById("desc").innerHTML = "Find video inspirations quick & easy ";
    }
  }
////////////////////  