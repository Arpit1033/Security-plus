import os
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from flask import Flask, render_template, Response
from torchvision import transforms

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model definition
class CrimeModel3D(nn.Module):
    def __init__(self):
        super(CrimeModel3D, self).__init__()
        self.conv1 = nn.Conv3d(3, 64, kernel_size=(3, 3, 3), padding=1)
        self.pool = nn.MaxPool3d(2, 2)
        self.conv2 = nn.Conv3d(64, 128, kernel_size=(3, 3, 3), padding=1)
        self.conv3 = nn.Conv3d(128, 256, kernel_size=(3, 3, 3), padding=1)
        self._to_linear = None
        self.convs(torch.zeros(1, 3, 30, 64, 64))
        self.fc1 = nn.Linear(self._to_linear, 512)
        self.fc2 = nn.Linear(512, 3)

    def convs(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        if self._to_linear is None:
            self._to_linear = x.numel()
        return x

    def forward(self, x):
        x = self.convs(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load Model
def load_model():
    global model
    model = CrimeModel3D().to(device)
    model.load_state_dict(torch.load('crime_model_epoch_10.pth', map_location=device))
    model.eval()

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((64, 64))
])

cap = cv2.VideoCapture(1)  # Capture from webcam

def generate_frames():
    frames = []
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_tensor = transform(frame_rgb).numpy()
            frames.append(frame_tensor)

            if len(frames) > 30:
                frames.pop(0)

            if len(frames) == 30:
                frames_np = np.array(frames) 
                input_tensor = torch.from_numpy(frames_np).permute(1, 0, 2, 3).unsqueeze(0).to(device)
                with torch.no_grad():
                    outputs = model(input_tensor)
                    probs = F.softmax(outputs, dim=1)
                    pred_class = torch.argmax(probs, dim=1).item()
                    confidence = probs[0][pred_class].item() * 100
                    if confidence < 60 :
                        pred_class = 2
                
                classes = ["Abuse", "Fighting", "Normal"]
                # classes = ["Abuse", "Normal", "Fighting"]
                label = f"{classes[pred_class]}: {confidence:.2f}%"
                cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

from flask import Flask, Response, render_template
import json
import time
frames = []
@app.route('/predict')
def predict():
    def event_stream():
        while True:
            if len(frames) == 30:
                frames_np = np.array(frames)
                input_tensor = torch.from_numpy(frames_np).permute(1, 0, 2, 3).unsqueeze(0).to(device)
                with torch.no_grad():
                    outputs = model(input_tensor)
                    probs = F.softmax(outputs, dim=1)
                    pred_class = torch.argmax(probs, dim=1).item()
                    confidence = probs[0][pred_class].item() * 100

                classes = ["Abuse", "Fighting", "Normal"]
                label = f"{classes[pred_class]}: {confidence:.2f}%"

                yield f"data: {json.dumps(label)}\n\n"
            time.sleep(1)

    return Response(event_stream(), mimetype="text/event-stream")





if __name__ == '__main__':
    load_model()
    app.run(debug=True)
