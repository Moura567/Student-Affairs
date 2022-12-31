function validate(){
    alert("info has been save")
}
function change(){
    let text;
    if (confirm("Are you sure you want to CHANGE") == true) {
      text = "You pressed OK";
    } 
    else {
      text = "You canceled";
    }
}