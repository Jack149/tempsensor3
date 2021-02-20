def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

temp = 0
radio.set_group(1)
basic.show_icon(IconNames.SQUARE)

def on_forever():
    global temp
    temp = input.temperature()
    radio.send_number(temp)
basic.forever(on_forever)
