# Author: Ashwin Sarith 

# def my_function(n,m)

function:
    addi $sp, $sp, -8   ## allocation of space
    sw $ra, 4($sp)      ## saving $ra
    sw $fp, 0($sp)      ## saving $fp

    # cpopying $sp to $fp
    addi $fp, $sp, 0 

if: 
    lw $t0, 8($fp)
    bne $t0, $0, else

    # return m
    lw $v0, 12($fp)
    addi $v0, $t0, 0

    # reload $fp and $ra and deallocate memory
    lw   $fp, 0($sp)
    addi $ra, 4($sp)
    addi $sp, $sp, 8 
    jr $ra

else: 
    lw $t1, 12($fp)
    lw $t2, 8($fp)

    div $t1, $t2
    mflo $t0
    addi $v0, $t0, 0 
    lw $v0, -4($fp)
    addi $sp, $sp, 4

    lw $fp, ($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8 
    jr $ra

# if x<=y for when x and y are global vars

lw $t0, x
lw $t1, y 
slt $t2, $t1, $t0
beq $t2, $0, endif


# 2019 s1 MIPS question

# def func(n):

func:
    addi, $sp, $sp, -8 # making space
    sw $ra, 4($sp)    # initing ra
    sw $fp, 0($sp)     # initing fp
    addi $fp, $sp, 0    # adding sp to fp

    addi $sp, $sp, -4 # make space for the local variable


# if n <= 0:
if: 

    lw $t0, 8($fp)     # loading n
    slt $t1, $t0, $0   # if n<0
    bne $t1, 1, else
    
    # result = 0 
    sw $0, result

    j endif


else:
    
    la $t0, result







