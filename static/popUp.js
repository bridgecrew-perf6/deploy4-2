

 const popup2 = document.querySelector('.popup2');
 function showPopup2() {
   popup2.classList.add('open');
   var elems = document.getElementsByClassName('footer');
   for (var i=0;i<elems.length;i+=1){
     elems[i].style.display = 'none';
   }
 }
 function hidePopup2() {
   popup2.classList.remove('open');
   var elems = document.getElementsByClassName('footer');
   for (var i=0;i<elems.length;i++){
     elems[i].style.display = 'block';
   }
 }

 const popup = document.querySelector('.popup');
 function showPopup() {
   popup.classList.add('open');
   var elems = document.getElementsByClassName('footer');
   for (var i=0;i<elems.length;i+=1){
     elems[i].style.display = 'none';
   }
 }
 function hidePopup() {
   popup.classList.remove('open');
   var elems = document.getElementsByClassName('footer');
   for (var i=0;i<elems.length;i++){
     elems[i].style.display = 'block';
   }
 }