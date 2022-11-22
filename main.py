# Rainer Herold
# 24.08.2021

# Bibliotheken_Impementierung
import atexit, cv2, pyautogui, time
import numpy as np

# Variablen_Bereich
Programm_Beenden = 0
SCREEN_SIZE = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", codec, 25.0, (SCREEN_SIZE))

# Funktionen_Bereich
def Close():
    time.sleep(3)
    cv2.destroyAllWindows()
    out.release()

while (Programm_Beenden != 1):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)

    if cv2.waitKey(1) == ord("q"):
        Close()
        Programm_Beenden = 1
        
atexit.register(Close)
