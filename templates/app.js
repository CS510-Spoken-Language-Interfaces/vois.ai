var record = document.querySelector('.btn');

 var mediaRecorder = new MediaRecorder(stream);

record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      btn.style.background = "red";

         }
