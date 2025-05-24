import time
import sys

def zigzag():
    indent = 0
    indent_increasing = True

    try:
        while True:
            print(' ' * indent + '*')
            time.sleep(0.1)

            if indent_increasing:
                indent += 1
                if indent == 20:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        sys.exit("\nZigzag animation stopped.")

zigzag()