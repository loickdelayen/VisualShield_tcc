import cv2
from ultralytics import YOLO

# Carrega os três modelos
model1 = YOLO('C:/Users/switc/OneDrive/Documentos/Vision_Shield/runs/detect/train/weights/best.pt')    # Capacete
model2 = YOLO('C:/Users/switc/OneDrive/Documentos/Vision_Shield/runs/detect/train2/weights/best.pt')   # Luvas
model3 = YOLO('C:/Users/switc/OneDrive/Documentos/Vision_Shield/runs/detect/train3/weights/best.pt')   # Óculos

# Cores em BGR
color1 = (0, 0, 255)   # Vermelho para capacete
color2 = (0, 255, 255) # Amarelo para luvas
color3 = (255, 0, 0)   # Azul para óculos

# Nomes corretos por modelo
name1 = "Luvas"
name2 = "Capacete"
name3 = "Oculos"

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    annotated_frame = frame.copy()

    # Modelo 1: Capacete
    results1 = model1.predict(frame, conf=0.5, verbose=False)
    for box in results1[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = f"{name1} {conf:.2f}"
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color1, 2)
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color1, 2)

    # Modelo 2: Luvas
    results2 = model2.predict(frame, conf=0.3, verbose=False)
    for box in results2[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = f"{name2} {conf:.2f}"
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color2, 2)
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color2, 2)

    # Modelo 3: Óculos
    results3 = model3.predict(frame, conf=0.5, verbose=False)
    for box in results3[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = f"{name3} {conf:.2f}"
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color3, 2)
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color3, 2)

    # Exibe o resultado final
    cv2.imshow("Detecção com cores personalizadas", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
