// declare variables

const form = document.querySelector("#form");
const submitButton = document.querySelector("#submit-button");

submitButton.addEventListener("click", ()=>{
    // e.preventDefault();
    console.log("Submit button clicked!");
    let details = new FormData(form).entries();

    fetch("http://127.0.0.1:8000/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(Object.fromEntries(details))
    })
    

})
