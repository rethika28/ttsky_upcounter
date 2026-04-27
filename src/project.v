`default_nettype none

module tt_um_upcounter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire en = ui_in[0];

    reg [3:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 4'b0000;
        else if (ena && en)
            count <= count + 1;
    end

    assign uo_out = {4'b0000, count};

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{uio_in, 1'b0};

endmodule
