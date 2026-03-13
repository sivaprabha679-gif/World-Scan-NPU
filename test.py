import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting dummy test...")
    await Timer(1, units="ns")
    dut._log.info("Test passed!")
