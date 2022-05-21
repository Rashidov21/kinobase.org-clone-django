$(".login").click(()=>{
    $("#account_modal").show()
})

function closeMessages() {
    document.querySelector(".message").style.display= 'none'
}



// function siteHost()
// {
//     var proto = window.location.protocol;
//     var host = window.location.hostname;
//     var port = window.location.port;

//     var site = proto +"//"+ host;
//     if(port != 80) {
//         site+=":"+port;
//     }
//     return site;
// }




