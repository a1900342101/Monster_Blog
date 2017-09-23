/*
KindEditor.ready(function(K) {
    window.editor = K.create('#id_content',{
        width:'600px',
        height:'200px',
    });
});
*/
var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = "";
var KK;
KindEditor.ready(function(K){
     KK = K;
});
function searchtoken() {
    if (csrfitems.length > 0) {
        csrftoken = csrfitems[0].value;
        clearInterval(_interval);
        console.log("csrftoken:" + csrftoken);
        window.editor = KK.create('#id_content',{
            uploadJson: '/admin/upload/img',
            extraFileUploadParams: {
                    csrfmiddlewaretoken:csrftoken
                },

            width:'800px',
            height:'400px',
        });
    }
}
_interval = setInterval(searchtoken, 500);
