// declare variables
let fileInput = document.getElementById("file-input");
let receivedDuration = document.getElementById("received-duration");
let times = document.getElementById("times");
let workingFile = document.getElementById("working-file");
const hidSubmitButton = document.querySelector("#submit-button");

hidSubmitButton.style.display = "none";

let get_duration = () => {

  // set the working file text content to the value of the file input
  workingFile.value = fileInput.value;

  fetch("http://127.0.0.1:8000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      // payload here
      "file": fileInput.value
    })
  })
  .then(response => response.text())
  .then(content => times.innerHTML = content)
  .catch(error => times.innerHTML = "<h3><i>An error occured, contact Site Admin...</i></h3>");

  hidSubmitButton.style.display = "block";
}

fileInput.addEventListener("change", get_duration);