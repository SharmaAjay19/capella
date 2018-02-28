function hasGetUserMedia() {
  return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia || navigator.msGetUserMedia);
}

function initializeRecorder(strean){
   audio_context = new AudioContext;
   sampleRate = audio_context.sampleRate;
   var audioInput = audio_context.createMediaStreamSource(stream);

   console.log("Created media stream.");

   var bufferSize = 4096;
   // record only 1 channel
   var recorder = audio_context.createScriptProcessor(bufferSize, 1, 1);
   // specify the processing function
   recorder.onaudioprocess = recorderProcess;
   // connect stream to our recorder
   audioInput.connect(recorder);
   // connect our recorder to the previous destination
   recorder.connect(audio_context.destination);
}

function errorCallback() {
   alert("Error!");
}

function startRecord(){
   if (hasGetUserMedia()) {
      navigator.getUserMedia({audio: true}, initializeRecorder, errorCallback);
      var ws = new WebSocket('ws://0.0.0.0:5001/websocket');

      ws.onopen = function(evt) {
         console.log('Connected to websocket.');

         // First message: send the sample rate
         ws.send("sample rate:" + sampleRate);

         navigator.getUserMedia({audio: true, video: false}, initializeRecorder, function(e) {
            console.log('No live audio input: ' + e);
         });
      }
   } else {
      alert('getUserMedia() is not supported in your browser');
   }
}

function recorderProcess(e) {
  if (recording){
    var left = e.inputBuffer.getChannelData(0);
    ws.send(convertFloat32ToInt16(left));
  }
}

function convertFloat32ToInt16(buffer) {
  l = buffer.length;
  buf = new Int16Array(l);
  while (l--) {
    buf[l] = Math.min(1, buffer[l])*0x7FFF;
  }
  return buf.buffer;
}