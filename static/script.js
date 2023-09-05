const dropContainer = document.getElementById("dropcontainer")
const fileInput = document.getElementById("img")
const overflow = document.getElementById("overflow")
const preview = document.getElementById("preview")

dropContainer.addEventListener("dragover", (e) => {
// prevent default to allow drop
e.preventDefault()
}, false)

dropContainer.addEventListener("dragenter", () => {
dropContainer.classList.add("drag-active")
})

dropContainer.addEventListener("dragleave", () => {
dropContainer.classList.remove("drag-active")
})

dropContainer.addEventListener("drop", (e) => {
e.preventDefault()
dropContainer.classList.remove("drag-active")
fileInput.files = e.dataTransfer.files
})

function show_overflow() {
    overflow.style.display = 'block';
}

document.getElementById("image").onchange = function() {
    if(this.value) {
        const [file] = image.files
        if (file) {
            preview.style.display = "block";
            preview.src = URL.createObjectURL(file)
        }
        document.getElementById("run").disabled = false; 
    }
    else{
        document.getElementById("run").disabled = true;
    }
}

// $(document).ready(function() {
//     $('form').on('submit', function(event) {
//         event.preventDefault();
//         var form_data = new FormData(document.getElementById('image'));
//         $.getJSON({
//             type : 'POST',
//             url : '/classification',
//             data : form_data,
//             contentType: false,
//             processData: false,
//             // success: (function(result){
//             //     console.log(result)
//             // })
//         })
//         .done(function(result){
//             console.log(result);
//             document.getElementById('response').text() = result;
//         })
//      });     
// });