// function editProfile(){
//     console.log(sess_id)
//     console.log(sess_id)
//     var sess_id = document.getElementById('sess_id').innerHTML;
    
//     console.log(sess_id)
//     console.log(sess_id)
//     if(sess_id){
//     document.getElementById('settings').style.display = "none";
//     document.getElementById('add-profile-form').style.display = "none";
//     document.getElementById('edit-profile-form').style.display = "block";
//     document.getElementById('profile-options').style.display = "none";
//     console.log(sess_id);
//     }
//     else{
//     console.log(sess_id);  
//     document.getElementById('settings').style.display = "none";      
//     document.getElementById('add-profile-form').style.display = "block";
//     document.getElementById('profile-options').style.display = "none";
//     document.getElementById('profile-options').style.display = "none";
    
//     }
    
//     }
    
//     function showSettings(){
    
//     document.getElementById('settings').style.display = "block";
//     document.getElementById('add-profile-form').style.display = "none";
//     document.getElementById('edit-profile-form').style.display = "none";
//     document.getElementById('profile-options').style.display = "none";
    
//     }



    
//     function popupClose(){
//         let d = document.getElementById("deleteVideosPopup");
//         Object.assign(d.style, {
//           display : "none",
//         });
//         document.getElementsByClassName("footer")[0].style.display = "block";
//         document.getElementsByTagName('body')[0].classList.remove('open-body');
//         document.getElementById('main-page').classList.remove('disable-main');
//       }
    
//       function popUpProfile(){
//         let d = document.getElementById("deleteVideosPopup");
//         Object.assign(d.style, {
//           display : "block",
//         });
      
//         document.getElementsByClassName("footer")[0].style.display = "none";
//         document.getElementsByTagName('body')[0].classList.add('open-body');
//         document.getElementById('main-page').classList.add('disable-main');
        
  
        
//         document.getElementById('profile-options').style.display = "block";
  
//         document.getElementById('settings').style.display = "none";
//         document.getElementById('add-profile-form').style.display = "none";
//         document.getElementById('edit-profile-form').style.display = "none";
//       }

// let sh = document.querySelector("#profile-popup-show-child-1");
// sh.addEventListener("click", showProfile);
// function showProfile(){
//     let child2 = document.querySelector(".profile-popup-child2");
//     child2.classList.add("profile-popup-open-child2");
//     let parent = document.querySelector(".profile-popup-parent");
//     parent.classList.add("profile-popup-open");

//     var elems = document.getElementsByClassName('footer');
//     for (var i=0;i<elems.length;i++){
//         elems[i].style.display = 'none';
//     }
//     var sess_id = document.getElementById('sess_id').innerHTML;
    
//     if(sess_id){
//     document.getElementById('settings').style.display = "none";
//     document.getElementById('add-profile-form').style.display = "none";
//     document.getElementById('edit-profile-form').style.display = "block";
//     }
//     else{
//     document.getElementById('settings').style.display = "none";      
//     document.getElementById('add-profile-form').style.display = "block";
//     document.getElementById('edit-profile-form').style.display = "none";
  
//     }
// }

// function hideProfile(){
//     let child2 = document.querySelector(".profile-popup-child2");
//     child2.classList.remove("profile-popup-open-child2");
//     let parent = document.querySelector(".profile-popup-parent");
//     parent.classList.remove("profile-popup-open");

//     var elems = document.getElementsByClassName('footer');
//     for (var i=0;i<elems.length;i++){
//         elems[i].style.display = 'block';
//     }
// }

// ////
// ///  manage profile options
// ////

// let bt = document.querySelector("#profile-popup-show-child-1");
// bt.addEventListener("click", showProfileOptions);


// function showProfileOptions(){
//     console.log("show");
//     let child1 = document.querySelector(".profile-popup-child1");
//     child1.classList.add("profile-popup-open-child1");
//     let parent = document.querySelector(".profile-popup-parent");
//     parent.classList.add("profile-popup-open");
    
//     var elems = document.getElementsByClassName('footer');
//     for (var i=0;i<elems.length;i++){
//         elems[i].style.display = 'none';
//     }
// }

// function hideProfileOptions(){
//   let child1 = document.querySelector(".profile-popup-child1");
//   child1.classList.remove("profile-popup-open-child1");
//     let parent = document.querySelector(".profile-popup-parent");
//     parent.classList.remove("profile-popup-open");

//     var elems = document.getElementsByClassName('footer');
//     for (var i=0;i<elems.length;i++){
//         elems[i].style.display = 'block';
//     }
// }

// console.log("showit");
// let showit = document.querySelector("#showit");
// showit.addEventListener("click", showIt);

// function showIt(){
//     console.log("showit");
// }

