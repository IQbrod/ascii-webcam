from cv2 import cv2
import numpy as np

def main():
  vc = cv2.VideoCapture(0)

  if vc.isOpened():
    rval, frame = vc.read()
  else:
    rval = False

  while rval:
    rval, frame = vc.read()
    print(toASCII(frame))

    key = cv2.waitKey(50) # 50ms pause -> ~20fps
    # Press echap to end
    if key == 27:
      break

def toASCII(frame, cols = 120, rows = 35):
  # Get a GRAY Frame
  grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Get size ratio
  height, width = grayFrame.shape
  cell_width = width / cols
  cell_height = height / rows
  # Reject invalid sizes
  if cols > width or rows > height:
    raise ValueError('Too many cols or rows.')
  # Initialize return values
  asciiText = ""
  colorGrid = []
  # Get gray's average of cells
  for i in range(rows):
    #colorGrid.push([])
    for j in range(cols):
      gray = np.mean(
        grayFrame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
      )
      # Cast it to ascii char
      asciiText += grayToChar(gray)
      # TODO: Inject RGB in colorGrid
      #colorGrid[i].push(RGB)
    asciiText += '\n'
  return asciiText

def grayToChar(gray):
  CHAR_LIST = ' .:-=+*#%@'
  num_chars = len(CHAR_LIST)
  return CHAR_LIST[
    min(
      int(gray * num_chars / 255), # current gray value
      num_chars - 1 # max gray value
    )
  ]
  
if __name__ == '__main__':
    main()
