// Decalre variables for DOM elements
const file = document.querySelector("#file-input");
const process = document.querySelector("#process");
const timeValues = document.querySelectorAll(".time-values");
const removeButton = document.querySelector(".remove-time-button");
const addButton = document.querySelector("#add-time-button");

addButton.addEventListener("click", ()=>{
    let newTime = document.createElement("div");
    newTime.classList.add("time-values");
    newTime.innerHTML = `<input type="number" min=0 max=5  name="" id="" placeholder="Hrs"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Mins"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Secs"> <span> - </span>
                    
                    <input type="number" min=0 max=5  name="" id="" placeholder="Hrs"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Mins"> <span>:</span>
                    <input type="number" min=0 max=59 name="" id="" placeholder="Secs">

                    <button class="remove-time-button" type="button" onclick="remove_time_input()">
                        <img src="static/app_editor/remove_icon.svg" alt="Remove Time Range" width="24" height="24">
                    </button>`;

    document.querySelector("#time-ranges").appendChild(newTime);
});

                function remove_time_input(){
                    document.querySelector("#time-ranges").removeChild(newTime);
                }