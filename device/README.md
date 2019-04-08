# xpSimpleBUS Device
Schematics and pcb of the xpSimpleBUS devices hardware.

## Boards
* **simplebus-device-input-port** - 8-bit input port with selectable address (by a 8-jumper row) in a range of 00H-07H.
> ![simplebus-device-input-port.jpg](../.images/simplebus-device-input-port.jpg)

* **simplebus-device-output-port** - 8-bit latched output port with selectable address (by a 8-jumper row) in a range of 00H-07H.
> ![simplebus-device-output-port.jpg](../.images/simplebus-device-output-port.jpg)

* **simplebus-device-sram-128bytes** - 128x8-Bytes Static RAM.
> Ok, *F68x10* is not TTL, but is TTL-levels compatible (from datasheet: Vcc=5.0V, Vih>=2.0), therefore it is incompatible with the HCMOS *74HC* family (from datasheet: Vcc=5V -> Vih>=3.4).
But my 4 pieces (F68A10) have all Voh>=3.15V measured "on board", and seems to work fine with the other HC chips. For now that's enough.
Moreover, interfacing bus to RPi (GPIO are 3.3V) I have powered bus to Vcc=3.3V and... *F68x10* still work well.
Again, for now that's enough.

| levels*| RPi GPIO | HC 3V3 | HC 5V | F68A10 5V | F68A10 3V3 |
|--------|----------|--------|-------|-----------|------------|
| PWR    |   3.3    |   3.3  |   5   |     5     |    3.3     |
| Vih    |          |        |       |           |            |
| Vil    |          |        |       |           |            |
| Voh    |   3.3    |   3.2  |  4.9  |    3.15   |    2.1     |
| Vol    |   0.1    |   0.1  |  0.1  |    0.1    |    0.1     |
(*) measured with tester

> ![simplebus-device-sram-128bytes.jpg](../.images/simplebus-device-sram-128bytes.jpg)
