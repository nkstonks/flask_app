function GetElementInsideContainer(containerID, childID) {
    var elm = {};
    var elms = document.getElementById(containerID).getElementsByTagName("*");
    for (var i = 0; i < elms.length; i++) {
        if (elms[i].id === childID) {
            elm = elms[i];
            break;
        }
    }
    return elm;
}

function make_active(id) {
    z = GetElementInsideContainer("Topnav", id.toString());
    z = document.getElementById(z.id)
    var z_name = document.getElementById(z.id);
    z_name.className = "active"
}

var pageURL = window.location.href;
var path = pageURL.substr(pageURL.lastIndexOf('/') + 1);
// alert(lastURLSegment);

if (path === "about") {
    make_active(2)
}
else if (path === "links") {
    make_active(3)
}
else if (path === "blog") {
    make_active(4)
}
else if (path === "logout") {
    make_active(7)
}
else if (path === "login") {
    make_active(8)
}
else if (path === "register") {
    make_active(9)
}
else if (!path){
    make_active(1)
}