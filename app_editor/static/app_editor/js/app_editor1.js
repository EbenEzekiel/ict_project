let fileInput = document.getElementById("file-input");
let receivedDuration = document.getElementById("received-duration");
let times = document.getElementById("times");

let get_duration = () => {

    fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        // your payload here
        "file": fileInput.value
      })
    })
    .then(response => response.text())
    .then(content => document.getElementById("body").innerHTML = content)


    // .then(response => response.json())
    // .then(duration => duration["duration"])
    // .then(data => {
    //     if (data < 60){
    //         times.innerHTML = `<div>
    //                               <input type="text" id="title1" name="title1" required />
    //                           </div>
    //                           <div>
    //                             <label>From: &nbsp; </label>
    //                             <input type="number" min="0" max = "59" />
    //                             <label> &nbsp; To: &nbsp; </label>
    //                             <input type="number" min="0" max = "59"/>
    //                           </div>`;
    //     }
    //     else if(data < 3600){
    //         times.innerHTML = `<div>
    //                             <input type="text" id="title1" name="title2" required />
    //                           </div>
    //                           <div>
    //                             <label>From: &nbsp; </label>
    //                             <input type="number" min="0" max = "59"/> 
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "59"/>

    //                             <label> &nbsp; To: &nbsp; </label>
    //                             <input type="number" min="0" max = "59"/> 
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "59"/>
    //                           </div>`;
    //     }
    //     else{
    //         times.innerHTML = `<div>
    //                             <input type="text" id="title1" name="title1" required />
    //                           </div>
    //                           <div>
    //                             <label>From: &nbsp; </label>
    //                             <input type="number" min="0" max = "59"/> 
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "59"/>
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "59"/>

    //                             <label> &nbsp; To: &nbsp; </label>
    //                             <input type="number" min="0" max = "59"/> 
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "59"/>
    //                             <span> : </span> 
    //                             <input type="number" min="0" max = "2"/>
    //                           </div>`;
    //     }
    // })
    //   .catch(error => {
    //     receivedDuration.value = "error detected";
    //   });
}

    
fileInput.addEventListener("change", get_duration);