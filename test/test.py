import cocotb
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_upcounter(dut):

    # Initialize signals
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    # Clock generator (10ns period)
    async def clock_gen():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    cocotb.start_soon(clock_gen())

    # Apply reset
    await Timer(10, units="ns")
    dut.rst_n.value = 1

    # Enable counter (ui_in[0] = 1)
    dut.ui_in.value = 0b1

    # Check counting
    expected = 0
    for i in range(10):
        await RisingEdge(dut.clk)
        expected = (expected + 1) % 16
        count = dut.uo_out.value.integer & 0xF

        dut._log.info(f"Expected={expected}, Got={count}")
        assert count == expected, "Count mismatch!"

    # Disable counter → should hold value
    dut.ui_in.value = 0b0
    prev = dut.uo_out.value.integer & 0xF

    for _ in range(3):
        await RisingEdge(dut.clk)
        count = dut.uo_out.value.integer & 0xF
        assert count == prev, "Counter changed when disabled!"

    dut._log.info("All tests passed ✅")
