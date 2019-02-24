def skyWrite():
    import cv2
    import numpy as np
    from keras.models import load_model

    # mlp_model = load_model('eminst_mlp_model.h5')
    # cnn_model = load_model('emnist_cnn_model.h5')

    camera = cv2.VideoCapture(0)
    ret,frame = camera.read()
    blueLower = np.array([100, 60, 100])
    blueUpper = np.array([140, 255, 255])
    temp_img = np.ones((frame.shape[0],frame.shape[1],3 ), np.uint8)*255
    count =0
    flag = 0
    sometrue = False
    points_main = []
    camera.set(10,200)
    cap_region_x_begin=0.5
    cap_region_y_end=0.5
    kernel = np.ones((5, 5), np.uint8)
    points= []
    while True:
        ret, frame = camera.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blueMask = cv2.inRange(hsv, blueLower, blueUpper)
        blueMask = cv2.erode(blueMask, kernel, iterations=2)
        blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, kernel)
        blueMask = cv2.dilate(blueMask, kernel, iterations=1)
        # cv2.imshow("1",blueMask)
        unmasked = cv2.bitwise_and(frame,frame,mask= blueMask)
        # cv2.imshow("2",unmasked)

        cnts, wtv2 = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(cnts) > 0:
            # Sort the contours and find the largest one -- we
            # will assume this contour correspondes to the area of the bottle cap
            cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
            # Get the radius of the enclosing circle around the found contour
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            # Draw the circle around the contour
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            # Get the moments to calculate the center of the contour (in this case Circle)
            M = cv2.moments(cnt)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
            if sometrue:
                points.append(center)

                if count>0:
                    cv2.line(temp_img,points[count],points[count-1],(0,0,0),20)
                    flag = 1
                count+=1
                

                temp_img_3 = cv2.bitwise_not(temp_img)

                temp_img_2 = cv2.flip(temp_img,1)
                cv2.imshow("3",temp_img_2)
                
                
        else:
            count = 0
            points_main+=points
            points=[]

        if flag == 1:
            frame = cv2.bitwise_or(frame,temp_img_3)
        
        frame = cv2.flip(frame,1)
        
        # cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
        #             (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow("",frame)
        
        k = cv2.waitKey(10)
        if k == 27:  # press ESC to exit
            break
        elif k == ord(' ') and not sometrue:  # press 'b' to capture the background
            sometrue = True
            points_main+=points
            points = []
            count = 0
        elif k == ord(" ") and sometrue:
            points_main+=points
            sometrue = False
        elif k == ord("r"):
            cv2.imwrite("output/temp.png",temp_img_2)
            x_coords=[]
            y_coords=[]
            for point in points_main:
                x_coords.append(point[0])
                y_coords.append(point[1])
            max_x = max(x_coords)
            max_y = max(y_coords)
            min_x =min(x_coords)
            min_y =min(y_coords)
            max_max= max(max_x-min_x,max_y-min_y)
            #cv2.rectangle(temp_img_2,(min_x-5,min_y-5),(min_x+max_max+5,min_y+max_max+5),(0,255,0),2)

            #temp_img_4 = temp_img_2[min_x-5:min_x+max_max+5,min_y-5:min_y+max_max+5]
            
            #cv2.imshow("5",temp_img_2)
            #cv2.waitKey(0)
            # temp_img_2 = temp_img_2[80:560,0:400]

            # print(frame.shape[0],frame.shape[1])
            # temp_img_2 = cv2.cvtColor(temp_img_2,cv2.COLOR_BGR2GRAY)
            # temp_img_2 = cv2.bitwise_not(temp_img_2)
            # newImage = cv2.resize(temp_img_2, (28, 28))

            # cv2.imshow("",newImage)
            # cv2.waitKey(0)
            # newImage = np.array(newImage)
            # newImage = newImage.astype('float32')/255

            # prediction1 = mlp_model.predict(newImage.reshape(1,28,28))[0]
            # prediction1 = np.argmax(prediction1)
            # print(prediction1)
            # prediction2 = cnn_model.predict(newImage.reshape(1,28,28,1))[0]
            # prediction2 = np.argmax(prediction2)        
            # print(prediction2)

    cv2.destroyAllWindows()
    camera.release()


if(__name__=="__main__"):
    skyWrite()
    skyWrite()