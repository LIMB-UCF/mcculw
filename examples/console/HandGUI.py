import cv2
import numpy as np

def draw_on_image_and_save(output_filename: str = 'output_image', rescale: float = 1, amplitude: float = 1, trialnum: int = 0):
    # Load the hand model image
    hand_image_path = r"C:\\Users\\VR\\Documents\\mcculwPython\\mcculw\\examples\\console\\HandModel3.0.png"  # Replace with your image path
    hand_image = cv2.imread(hand_image_path)

    # Resize the image to fit within a window (e.g., 600x600)
    windowX = 1000*rescale
    windowY = 849*rescale
    window_size = (int(windowX),int(windowY))
    hand_image = cv2.resize(hand_image, window_size)

    # Create a copy of the image to draw on
    image_copy = hand_image.copy()
    drawing = False  # True if the mouse is pressed

    # Function to draw highlighted circles while dragging
    def draw_circle(event, x, y, flags, param):
        nonlocal drawing

        if event == cv2.EVENT_LBUTTONDOWN:  # When left mouse button is pressed
            drawing = True  # Start drawing
            # Draw a smooth, highlighted circle at the clicked location
            cv2.circle(image_copy, (x, y), 10, (0, 255, 255), -1)  # Yellow filled circle

        elif event == cv2.EVENT_MOUSEMOVE:  # When the mouse is moving
            if drawing:  # Only draw if the mouse is pressed
                cv2.circle(image_copy, (x, y), 10, (0, 255, 255), -1)

        if event == cv2.EVENT_LBUTTONUP:  # When the left mouse button is released
            drawing = False  # Stop drawing

        # TODO Erase
        # if event = cv2.EVENT_FLAG_SHIFTKEY:
        #     cv2.

    # Function to save the image and quit
    def save_and_quit(output_filename):
        output_filename = f"{output_filename}_trial_{trialnum}_amplitude_{amplitude}"
        save_path = f'{output_filename}.png'  # Save with the provided filename
        cv2.imwrite(save_path, image_copy)
        print(f"Image saved at: {save_path}")
        cv2.destroyAllWindows()

    # Set up the OpenCV window and mouse callback function
    cv2.namedWindow("Hand Image")
    cv2.setMouseCallback("Hand Image", draw_circle)

    while True:
        # Display the image
        cv2.imshow("Hand Image", image_copy)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('w'):  # Press 'w' to quit without saving
            cv2.destroyAllWindows()
            break
        elif key == ord('q'):  # Press 'q' to save and quit
            save_and_quit(output_filename)
            break

# Example usage
# draw_on_image_and_save('output_hand_model', 0.75)
