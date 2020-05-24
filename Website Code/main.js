function GetScore() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("score").innerHTML =
                this.responseText;
        }
    };
    xhttp.open("GET", "score.txt", true);
    xhttp.send();
}
function Init() {
    GetScore();
    setInterval(GetScore, 500);
}