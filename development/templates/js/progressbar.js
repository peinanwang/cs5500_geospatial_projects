function fileSelected() {
  var file = document.getElementById('file').files[0];
  if (file) {
      var fileSize = 0;
      if (file.size > 1024 * 1024)
          fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
      else
          fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
      document.getElementById('fileName').innerHTML = 'Name: ' + file.name;
      document.getElementById('fileSize').innerHTML = 'Size: ' + fileSize;
      // document.getElementById('fileType').innerHTML = 'Type: ' + file.type;
  }
}

function uploadFile() {
  var fd = new FormData();
  fd.append("file", document.getElementById('file').files[0]);
  var xhr = new XMLHttpRequest();
  xhr.upload.addEventListener("progress", uploadProgress, false);
  xhr.addEventListener("load", uploadComplete, false);
  xhr.addEventListener("error", uploadFailed, false);
  xhr.addEventListener("abort", uploadCanceled, false);
  xhr.open("POST", "${ pageContext.request.contextPath }/upload");  // Change to our interface
  xhr.send(fd);
}

function uploadProgress(evt) {
  if (evt.lengthComputable) {
      var percent = Math.round(evt.loaded * 100 / evt.total);
      document.getElementById('progress').innerHTML = percent.toFixed(2) + '%';
      document.getElementById('progress').style.width = percent.toFixed(2) + '%';
  } else {
      document.getElementById('progress').innerHTML = 'unable to compute';
  }
}

function uploadComplete(evt) {
  // Event triggered when server responses
  document.getElementById('result').innerHTML = evt.target.responseText;
}

function uploadFailed(evt) {
  alert("There was an error attempting to upload the file.");
}

function uploadCanceled(evt) {
  alert("The upload has been canceled by the user or the browser has lost connection.");
}