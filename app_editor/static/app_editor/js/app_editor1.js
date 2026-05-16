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
    .then(content => times.innerHTML = content)
    .catch(error => times.innerHTML = "<h3>An error occured, contact Site Admin</h3>");
}

fileInput.addEventListener("change", get_duration);