# *128x8-Bytes Static RAM* Board
128x8-Bytes Static RAM.
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

![board-built](simplebus-bridge-admux_built.jpg)


## Schematic
![board-schematic](simplebus-bridge-admux_sch.jpg)


## PCB Layout
![board-pcb](simplebus-bridge-admux_pcb.jpg)


## Bill of Materials
- [x] paperboard 5x7cm
- [x] 1 x bulk capacitors (tantalum) 1uF 16V
- [x] power activity led green 3mm
- [x] led current limiter resistor 1Kohm
- [x] SimpleBUS DIL 24-pin right-angle header

- [x] RAM-IC F6810
- [x] IC-logic 74HC00