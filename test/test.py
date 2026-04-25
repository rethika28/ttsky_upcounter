import cocotb
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_upcounter(dut):

    # Init
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    # Clock
    async def clock():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    cocotb.start_soon(clock())

    # Apply reset
    await Timer(10, units="ns")
    dut.rst_n.value = 1

    # Wait 1 clock AFTER reset (IMPORTANT)
    await RisingEdge(dut.clk)

    # Enable counter
    dut.ui_in.value = 1

    expected = 0

    # Start checking AFTER first increment
    for i in range(10):
        await RisingEdge(dut.clk)
        expected = (expected + 1) % 16

        count = dut.uo_out.value.integer & 0xF
        dut._log.info(f"Expected={expected}, Got={count}")

        assert count == expected, f"Mismatch at cycle {i}"

    # Disable counter
    dut.ui_in.value = 0
    prev = dut.uo_out.value.integer & 0xF

    for _ in range(3):
        await RisingEdge(dut.clk)
        count = dut.uo_out.value.integer & 0xF
        assert count == prev, "Counter changed when disabled"

    dut._log.info("All tests passed ✅")
