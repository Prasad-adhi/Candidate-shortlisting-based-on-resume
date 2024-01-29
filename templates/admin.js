function saveFile(event)
    {
        event.preventDefault();
        var form=new FormData()
        form.append("file",document.getElementsByName("file")[0].files[0])
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() 
        {
            if (this.readyState == 4 && this.status == 200) 
            {
                output=JSON.parse(this.responseText);
                string=""
                document.getElementById("message").innerHTML=output["text"]
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/job_upload", true);
        xhttp.send(form);
    }
    function loadDoc()
    {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) 
            {
                output=JSON.parse(this.responseText);
                string=""
                for(var i=0;i<output["Names"].length;i++)
                {
                    string ="Name: "+output['Names'][i]
                    var text=document.createTextNode(string)
                    document.getElementById("output").appendChild(text)
                    document.getElementById("output").appendChild(document.createElement("br"))

                    string ="Contact no: "+output['Contact'][i]
                    var text=document.createTextNode(string)
                    document.getElementById("output").appendChild(text)
                    document.getElementById("output").appendChild(document.createElement("br"))
                    
                    string ="Email id: "+output['Email'][i]
                    var text=document.createTextNode(string)
                    document.getElementById("output").appendChild(text)
                    document.getElementById("output").appendChild(document.createElement("br"))

                    string ="Resume: "
                    var text=document.createTextNode(string)
                    document.getElementById("output").appendChild(text)

                    var link=document.createElement("a")
                    var att = document.createAttribute("href");  
                    att.value = "resumes/"+output['File'][i]
                    link.setAttributeNode(att);
                    var att1 = document.createAttribute("download");  
                    link.setAttributeNode(att1);
                    var filename=document.createTextNode(output['File'][i])
                    link.appendChild(filename)
                    document.getElementById("output").appendChild(link)
                    document.getElementById("output").appendChild(document.createElement("br"))

                    string ="Similarity: "+output['Score'][i]*100
                    var text=document.createTextNode(string)
                    document.getElementById("output").appendChild(text)
                    document.getElementById("output").appendChild(document.createElement("br"))
                    document.getElementById("output").appendChild(document.createElement("br"))
                }
            }
        };
        xhttp.open("GET", "http://127.0.0.1:5000/Result", true);
        xhttp.send();
    }