function namev()
   {
      var name=document.getElementById("name").value
      if(name=="")
      {
         document.getElementById("nerr").innerHTML="Please enter name";
         document.getElementById("name").focus();
      }
      else if(/\d/.test(name))
      {
         document.getElementById("nerr").innerHTML="Name should not contain numbers";
         document.getElementById("name").focus();
      }
      else
      {
         document.getElementById("nerr").innerHTML="";
      }
   }
   function numberv()
   {
      var number=document.getElementById("cno").value
      if(number=="")
      {
         document.getElementById("cnoerr").innerHTML="Please enter your contact number";
         document.getElementById("cno").focus();
      }
      else if(/[a-zA-Z]/g.test(number))
      {
         document.getElementById("cnoerr").innerHTML="Contact number should not have any alphabets";
         document.getElementById("cno").focus();
      }
      else if(number.length!=10)
      {
         document.getElementById("cnoerr").innerHTML="Length of Contact number should be 10";
         document.getElementById("cno").focus();
      }
      else
      {
         document.getElementById("cnoerr").innerHTML="";
      }
   }
   function emailv()
   {
      email=document.getElementById("email").value;
      /*var mailformat = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;*/
      mailformat=/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
      if(email=="")
      {
         document.getElementById("emerr").innerHTML="Please enter your email";
         document.getElementById("email").focus();
      }
      else if(!email.match(mailformat))
      {
         document.getElementById("emerr").innerHTML="Please enter the right email format";
         document.getElementById("email").focus();  
      }
      else
      {
         document.getElementById("emerr").innerHTML="";
      }
   }