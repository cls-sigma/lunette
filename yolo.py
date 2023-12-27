

import yaml


from ultralytics import YOLO

from pydub import AudioSegment
from pydub.playback import play


def audio(path3):
    play(AudioSegment.from_file(path3))


# Load a model
model = YOLO("yolov8n.pt")  # load an official model


# print(results)
# import the opencv library
def ocr2():
    import cv2
    i = 0
    compt = 0
    # define a video capture object
    names = ''
    # file_name = "../usr/local/lib/python3.8/dist-packages/ultralytics/yolo/data/datasets/coco8.yaml"
    with open("coco.names", "r") as stream:
        names = stream.read().splitlines()
    # print(names)
    vid = cv2.VideoCapture(0)

    import os
    import shutil
    try:
        shutil.rmtree('runs')
        os.mkdir("runs/")
        print("ok")
    except:
        pass
    bre = 0
    while (True):

        ret, frame = vid.read()
        w_, h_, r = frame.shape
        a, b = (int(h_ / 10), 0), (int(9*h_/10), w_)
        print(a, b, w_, h_)
        cv2.rectangle(frame, a, b, (0, 255, 255), 2)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if bre == 1:
            return 0
        model.predict(frame, save_txt=True, )
        ph = "runs/detect/predict/labels/image0.txt"
        if os.path.exists(ph):
            lis = open(ph, "r").readlines()
            if lis:
                print(lis)
                for l in lis:
                    ind = int(l.split()[0])
                    print(ind, names[ind])
                    # if names[ind].lower():
                    li = l.split()
                    xc, yc, nw, nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])
                    h, w = frame.shape[0], frame.shape[1]
                    xc *= w
                    yc *= h
                    nw *= w
                    nh *= h
                    x = int(xc - nw / 2)
                    y = int(yc - nh / 2)
                    h = nh
                    w = nw
                    cv2.rectangle(frame, (x, y), (int(xc + nw / 2), int(yc + nh / 2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'Dis: {round(h*2.4, 2)} cm', (x + 5, y + 13), cv2.FONT_HERSHEY_COMPLEX, 0.48, (255, 255, 0), 2)

                    top_left = (int(xc - nw / 2), int(yc - nh / 2))
                    bottom_right = (int(xc + nw / 2), int(yc + nh / 2))
                    long=b[0]-a[0]
                    if a[0]<x<b[0] or a[0]<x+h<b[0]:
                        cv2.putText(frame, f' {names[ind]}', (x + 5, y + 23), cv2.FONT_HERSHEY_COMPLEX, 0.48, (0, 255, 0), 2)

                        if x-(w_-(x+w))>100:
                            if w>100:# & dist<1000:
                                cv2.putText(frame, 'Gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        elif x-(w_-(x+w))<100:
                            cv2.putText(frame, 'Droite', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        else:
                            cv2.putText(frame, 'Stop', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    elif (w>(b[0]-a[0])):
                        cv2.putText(frame, 'Obstacle imminent, a gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    else:
                        pass

            else:
                pass#cv2.imshow('frame', frame)




            cv2.imshow('frame', frame)
            os.remove(ph)

        """ else:
            print("N'existe pas")
        compt += 1
        if compt == 30:

            talk("temps expiré pour le guide, j'essayerai de vous"
                 " lire votre document mais la précision ne sera peut-etre pas bonne")
            audio("/home/pi/final_glass/cam.wav")
            res = detect_document(content=frame)
            if res:
                talk("Le texte dans votre image est: ")
                talk(correct(res))
                vid.release()
                # Destroy all the windows
                cv2.destroyAllWindows()
                return 0

            else:
                talk("Je n'ai pas pu lire votre document. Désolé")
                return 0
            break"""
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def ocr1():
    import cv2
    i = 0
    compt = 0
    # define a video capture object
    names = ''
    # file_name = "../usr/local/lib/python3.8/dist-packages/ultralytics/yolo/data/datasets/coco8.yaml"
    with open("coco.names", "r") as stream:
        names = stream.read().splitlines()
    # print(names)
    vid = cv2.VideoCapture(0)

    import os
    import shutil
    try:
        shutil.rmtree('runs')
        os.mkdir("runs/")
        print("ok")
    except:
        pass
    bre = 0
    while (True):

        ret, frame = vid.read()
        w_, h_, r = frame.shape
        a, b = (int(h_ / 10), 0), (int(9*h_/10), w_)
        print(a, b, w_, h_)
        cv2.rectangle(frame, a, b, (0, 255, 255), 2)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if bre == 1:
            return 0
        model.predict(frame, save_txt=True, )
        ph = "runs/detect/predict/labels/image0.txt"
        if os.path.exists(ph):
            lis = open(ph, "r").readlines()
            if lis:
                print(lis)
                for l in lis:
                    ind = int(l.split()[0])
                    print(ind, names[ind])
                    # if names[ind].lower():
                    li = l.split()
                    xc, yc, nw, nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])
                    h, w = frame.shape[0], frame.shape[1]
                    xc *= w
                    yc *= h
                    nw *= w
                    nh *= h
                    x = int(xc - nw / 2)
                    y = int(yc - nh / 2)
                    h = nh
                    w = nw
                    cv2.rectangle(frame, (x, y), (int(xc + nw / 2), int(yc + nh / 2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'Dis: {round(h*2.4, 2)} cm', (x + 5, y + 13), cv2.FONT_HERSHEY_COMPLEX, 0.48, (255, 255, 0), 2)

                    top_left = (int(xc - nw / 2), int(yc - nh / 2))
                    bottom_right = (int(xc + nw / 2), int(yc + nh / 2))
                    long=b[0]-a[0]
                    if a[0]<x<b[0] or a[0]<x+h<b[0]:
                        cv2.putText(frame, f' {names[ind]}', (x + 5, y + 23), cv2.FONT_HERSHEY_COMPLEX, 0.48, (0, 255, 0), 2)

                        if x-(w_-(x+w))>100:
                            if w>100:# & dist<1000:
                                cv2.putText(frame, 'Gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        elif x-(w_-(x+w))<100:
                            cv2.putText(frame, 'Droite', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        else:
                            cv2.putText(frame, 'Stop', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    elif (w>(b[0]-a[0])):
                        cv2.putText(frame, 'Obstacle imminent, a gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    else:
                        pass

            else:
                pass#cv2.imshow('frame', frame)




            cv2.imshow('frame', frame)
            os.remove(ph)

        """ else:
            print("N'existe pas")
        compt += 1
        if compt == 30:

            talk("temps expiré pour le guide, j'essayerai de vous"
                 " lire votre document mais la précision ne sera peut-etre pas bonne")
            audio("/home/pi/final_glass/cam.wav")
            res = detect_document(content=frame)
            if res:
                talk("Le texte dans votre image est: ")
                talk(correct(res))
                vid.release()
                # Destroy all the windows
                cv2.destroyAllWindows()
                return 0

            else:
                talk("Je n'ai pas pu lire votre document. Désolé")
                return 0
            break"""
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
#ocr2()
