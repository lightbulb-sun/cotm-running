.gba
.open "hack.gba", 0x08000000

FREE_SPACE        equ 0x08700000
HELD_BUTTONS      equ 0x020232fe
NEW_BUTTONS       equ 0x020232fc
MASK_BUTTON_DOWN  equ 0x0080
MASK_BUTTON_R     equ 0x0100

.thumb

.org 0x0806b130
        ldr     r0, =dash+1
        bx      r0
.pool

.org 0x0806bad8
        ldr     r2, =tackle+1
        bx      r2
.pool

.org FREE_SPACE
dash:
@@check_for_held_r_button_press:
        ldr     r0, =HELD_BUTTONS
        ldr     r0, [r0]
        ldr     r7, =MASK_BUTTON_R
        and     r0, r7
        cmp     r0, #0
        beq     @@do_nothing
@@continue:
        ldr     r0, =0x0806b14e+1
        bx      r0
@@do_nothing:
        ldr     r0, =0x0806b180+1
        bx      r0

tackle:
@@case1:
@@check_for_new_r_button_press:
        ; replace original instructions
        ldrh    r2, [r0]
        ldrh    r0, [r1]
        and     r0, r2
        cmp     r0, #0
        beq     @@case2
@@check_for_held_down_button_press:
        ldr     r0, =HELD_BUTTONS
        ldr     r0, [r0]
        ldr     r2, =MASK_BUTTON_DOWN
        and     r0, r2
        cmp     r0, #0
        bne     @@execute_tackle
@@case2:
@@check_for_new_down_button_press:
        ldr     r0, =NEW_BUTTONS
        ldr     r0, [r0]
        ldr     r2, =MASK_BUTTON_DOWN
        and     r0, r2
        cmp     r0, #0
        beq     @@do_nothing
@@check_for_held_r_button_press:
        ldr     r0, =HELD_BUTTONS
        ldr     r0, [r0]
        ldr     r2, =MASK_BUTTON_R
        and     r0, r2
        cmp     r0, #0
        beq     @@do_nothing
@@execute_tackle:
        ldr     r0, =0x0806bae2+1
        bx      r0
@@do_nothing:
        ldr     r0, =0x0806bb98+1
        bx      r0
.pool

.close
