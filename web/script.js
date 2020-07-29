function sendData() {
    var rcname = document.getElementById("rcname").value;
    var tm = document.getElementById("tm").value;
    var msg = document.getElementById("msg").value;
    console.log(rcname);
    eel.sendDataToPy(rcname, tm, msg);
}