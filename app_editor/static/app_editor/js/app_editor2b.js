// Decalre variables for DOM elements
const file = document.querySelector("#file-input");
const process = document.querySelector("#process");
const timeValues = document.querySelectorAll(".time-values");
const removeButton = document.querySelector(".remove-time-button");
const addButton = document.querySelector("#add-time-button");

let varId= 2;
addButton.addEventListener("click", ()=>{
    let newTime = document.createElement("div");
    newTime.classList.add("time-values");
    newTime.innerHTML = `<input type="number" min=0 max=5  name="" id="" placeholder="Hrs"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Mins"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Secs"> <span> - </span>
                    
                    <input type="number" min=0 max=5  name="" id="" placeholder="Hrs"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Mins"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Secs">

                    <button class="remove-time-button" id= ${varId} type="button" onclick="remove_time_input(${varId})">
                        <img src="static/app_editor/remove_icon.svg" alt="Remove Time Range" width="24" height="24">
                    </button>`;
    // newTime.querySelector(".remove-time-button").addEventListener('click', () => {
    //     console.log("Clicked!!!")
    // })

    varId+=1;

    document.querySelector("#time-ranges").appendChild(newTime);
});

                // function remove_time_input(){
                //     document.querySelector("#time-ranges").removeChild(newTime);
                // }

process.addEventListener("click", () => {
    const file_data = file.value;
    const feedback = document.getElementById("feedback");

    time = [...document.querySelectorAll('#time-ranges .time-values')].map(child => {
        const inputs = [...child.querySelectorAll(".time-values input")];

            return {
            start:`${inputs[0].value}:${inputs[1].value}:${inputs[2].value}`,
            end: `${inputs[3].value}:${inputs[4].value}:${inputs[5].value}`
            }
        });

    fetch("/splice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({file: file_data, time: time}),
    }).then(response => response.json())
    .then(text => feedback.innerHTML = `<h4>${text.text}</h4>`)
    .catch(error => feedback.innerHTML = `<h4>${error.message}</h4>`)
})