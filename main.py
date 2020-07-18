def on_received_value(name, value):
    global Lounge, Kitchen, Hall_Lower, Hall_Upper
    if name == "l":
        Lounge = value
    if name == "k":
        Kitchen = value
    if name == "hl":
        Hall_Lower = value
    if name == "hu":
        Hall_Upper = value
radio.on_received_value(on_received_value)

Hall_Lower = 0
Kitchen = 0
Lounge = 0
Hall_Upper = 0
radio.set_group(6)
Hall_Upper = input.temperature()
Lounge = 0
Kitchen = 0
Hall_Lower = 0
if Hall_Upper >= 18 and Hall_Upper <= 20:
    basic.show_icon(IconNames.HAPPY)
elif False:
    if Hall_Upper < 18:
        basic.show_string("C")
elif Hall_Upper > 20:
    basic.show_string("H")