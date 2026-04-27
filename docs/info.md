<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works
This project implements a simple 4-bit synchronous up counter using Verilog.
The counter increments on every clock cycle when enabled and resets asynchronously.

⚙️ Features
4-bit counter (counts from 0 to 15)
Asynchronous active-low reset (rst_n)
Enable control using ui_in[0]
Global enable using ena
Compatible with TinyTapeout interface
Verified using cocotb testbench

## How to test

The design is verified using a Python-based cocotb testbench.

Test Steps:
Apply reset
Enable counter
Verify increment for multiple clock cycles
Disable counter and check hold behavior

## External hardware

no external hardware used in your project (e.g. PMOD, LED display, etc), if any
