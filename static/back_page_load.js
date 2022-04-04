(function () {
    window.onpageshow = function(event) {
        if (event.persisted) {
            window.location.reload();
        }
    };
})();

if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}