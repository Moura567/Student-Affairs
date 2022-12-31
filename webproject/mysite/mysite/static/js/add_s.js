function validate(){
   var sname=document.forms["myform"]["name"].value;
   var sid=document.forms["myform"]["id"].value;
    var slevel=document.forms["myform"]["level"].value;
    var sgpa=document.forms["myform"]["gpa"].value;
    var sdata=document.forms["myform"]["birth"].value;
    var dp = document.getElementById("Departments").value;
   var sphoval=document.forms["myform"]["phonenumber"].value;
   var sgen = document.getElementById("Gender").value;

    var sphone=document.forms["myform"]["Student number"].value;
    if(sname==""){
        alert("enter a name")
        return false;

    }
    
    if(!isNaN(sname)){
        alert("name should be characters only")
        return false;
    }
    if(sid==""){
        alert("enter an ID")
        return false;
    }
    if(sid.length!=8){
        alert("enter a valid ID of 8 numbers")
        return false;
    }
    if(slevel==""){
        alert("enter a level")
        return false;

    }
    if(slevel >4 || slevel <1){
        alert("level should be between 1 and 4 ")
        return false;
    }
    if(sgpa==""){
        alert("enter the GPA")
        return false;

    }
    if(sgpa>4 || sgpa <1){
        alert("GPA should be between 1 and 4 ")
        return false;
    }
    if(sdata==""){
        alert("enter your date")
        return false;
    }
    if(sphone ==""){
        alert("enter a phone a nubmer")
        return false;
    } 
    if(dp=="Select Department"){
        alert(" please select a department")
        return false;
    }
    if(sphoval=="+xxx"){
        alert("choose one for phone number")
        return false;
    }
    if(isNaN(sphone)){
        alert("phone number should be numbers only")
        return false;
    }
    if(sphone.length!=11){
       alert("phone number must be 11 digits")
        return false;
    }
      alert("Student has been added successfully")
      if(sgen=="Select Gender"){
        alert(" please select a Gender")
        return false;
    }
}