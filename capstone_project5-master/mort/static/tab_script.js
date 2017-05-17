//Since I do not know JavaScript, all js code was taken from
//https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_tabs
function openForm(evt, searchType) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(searchType).style.display = "block";
  evt.currentTarget.className += " active";
}
