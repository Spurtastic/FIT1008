        .data
x:      .word 0
y:      .word 2
z:      .word 4

        .text
        lw $t0, y
        lw $t1, z
        mult $t0 , $t1
        mflo $t0		# corrected
        sw $t0, x

        lw $t0, x
        div $t0, 4
        mfhi $t0                #corrected
        sw $t0, x

        lw $a0, x	  	# corrected
        addi $v0, $t0, 1	# corrected
        syscall