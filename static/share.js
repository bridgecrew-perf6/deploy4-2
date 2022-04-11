
$('.copy_text').click(function (e) {
    e.preventDefault();
    var copyText = $(this).attr('href');

    document.addEventListener('copy', function(e) {
    e.clipboardData.setData('text/plain', copyText);
    e.preventDefault();
    }, true);

    document.execCommand('copy');  
    console.log('copied text : ', copyText);
    alert('copied text: ' + copyText); 
});
        

function showOptions(){
    document.getElementById("share-option-child").style.display = "block";
    document.getElementById("select-and-save-cluster-child").style.display = "none";
    document.getElementById("share-parent").style.display = "none";
}
function showSave(){
    document.getElementById("share-option-child").style.display = "none";
    document.getElementById("share-parent").style.display = "none";
    document.getElementById("select-and-save-cluster-child").style.display = "block";
}
function showShare(){
    document.getElementById("share-option-child").style.display = "none";
    document.getElementById("select-and-save-cluster-child").style.display = "none";
    document.getElementById("share-parent").style.display = "block";
}