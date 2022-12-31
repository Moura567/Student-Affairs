function validate(){
  var sname=document.forms["myform"]["name"].value;
  var sid=document.forms["myform"]["id"].value;
  var slevel=document.forms["myform"]["level"].value;
  var sgpa=document.forms["myform"]["gpa"].value;
  var dp = document.getElementById("departments").value;

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
if(slevel!=3)
{
  alert("Invalid level!")
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
if(dp=="Select Department"){
  alert(" please select a department")
  return false;
}
alert("Student has been added his department successfully")

}
      
$(document).on('#btn',"#h",function(e){
  e.preventDefault();
  $.ajax({
      type:'POST',
      url:'/department',
      data:{
          name:$('#user').val(),
          id:$('#sid').val(),
          gpa:$('#sgpa').val(),
          level:$('#slevel').val(),
          depart:$('#departments').val(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },

  });
});
