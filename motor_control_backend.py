import pigpio
import time
from flask import Flask

pi = pigpio.pi()

SPEED = 64

IN1 = 5
IN2 = 6
IN3 = 27
IN4 = 22

html = """
<font size="32vw" color="white">
<h1>
<center>
<a href="fast">Fast</a><br>
<a href="forward">Forward</a><br>
<a href="left">Left</a>
<a>_______</a>
<a href="right">Right</a><br>
<a href="back">Back</a><br>
<a href="stop">Stop</a>
</center>
</h1>
</font>
"""

app = Flask(__name__)

@app.route("/")
def hello():
    return html


@app.route("/forward")
def forward():
    pi.set_PWM_dutycycle(IN1, SPEED)
    pi.write(IN2, 0)
    pi.set_PWM_dutycycle(IN3, SPEED)
    pi.write(IN4, 0)
    return html


@app.route("/back")
def back():
    pi.set_PWM_dutycycle(IN2, SPEED)
    pi.write(IN1, 0)
    pi.set_PWM_dutycycle(IN4, SPEED)
    pi.write(IN3, 0)
    return html


@app.route("/fast")
def fast():
    pi.set_PWM_dutycycle(IN1, SPEED * 2)
    pi.write(IN2, 0)
    pi.set_PWM_dutycycle(IN3, SPEED * 2)
    pi.write(IN4, 0)
    return html


@app.route("/test")
def test():
    pi.set_PWM_dutycycle(IN1, SPEED / 2)
    pi.write(IN2, 0)
    pi.set_PWM_dutycycle(IN3, SPEED / 2)
    pi.write(IN4, 0)
    return html


@app.route("/left")
def left():
    pi.set_PWM_dutycycle(IN3, SPEED)
    pi.write(IN2, 0)
    pi.write(IN1, 0)
    pi.write(IN4, 0)
    return html


@app.route("/right")
def right():
    pi.write(IN3, 0)
    pi.write(IN2, 0)
    pi.set_PWM_dutycycle(IN1, SPEED)
    pi.write(IN4, 0)
    return html


@app.route("/stop")
def stop():
    pi.write(IN1, 0)
    pi.write(IN2, 0)
    pi.write(IN3, 0)
    pi.write(IN4, 0)
    return html


if __name__ == "__main__":
    stop()
    app.run(host='0.0.0.0', port=8000)
    # pi.write(IN4, 0)
    # pi.set_PWM_dutycycle(IN1, 32)
