print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord, Sequence
combos = Combos()
from kmk.modules.modtap import ModTap
modtap = ModTap()
# optional: set a custom tap timeout in ms
# modtap.tap_time = 300
from kmk.modules.oneshot import OneShot
oneshot = OneShot()
# optional: set a custom tap timeout in ms (default: 1000ms)
# oneshot.tap_time = 1500
from kmk.extensions.media_keys import MediaKeys



keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

keyboard.modules.append(Layers())
keyboard.modules.append(combos)
keyboard.modules.append(modtap)
keyboard.modules.append(oneshot)
keyboard.extensions.append(MediaKeys())

print(dir(board))
print(dir(keyboard))
print(dir(keyboard.matrix))
keyboard.row_pins = (board.D1,)
keyboard.col_pins = (board.A0, board.A1, board.A2, board.A3, board.D10, board.MOSI, board.MISO, board.CLK)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
#keyboard.diode_orientation = DiodeOrientation.ROW2COL

A_PRN = KC.LT(3, KC.A)
S_NUM = KC.LT(1, KC.S)
#S_NUM = KC.MT(KC.S, KC.MO(1))
E_SYM = KC.LT(2, KC.E)
O_CST = KC.LT(4, KC.O)

DF_NAV  = KC.DF(5)
DF_BASE = KC.DF(0)
#DF_MOU = KC.DF(5)

keyboard.keymap = [
    # 0 - BASE Layer
    [S_NUM, KC.T,  KC.R,  A_PRN,
     O_CST, KC.I,  KC.Y,  E_SYM,],
    #[KC.S, KC.T,  KC.R,  KC.A,
     #KC.O, KC.I,  KC.Y,  KC.E,],

    # 1 - NUM Layer
    [KC.TRNS, KC.N3, KC.N2, KC.N1,
     KC.NO,   KC.N6, KC.N5, KC.N4],

    # 2 - SYMBOL Layer
    [KC.GRV,  KC.SCLN, KC.BSLS, KC.EXLM,
     KC.EQL,  KC.MINS, KC.QUES, KC.TRNS],

    # 3 - PARENS Layer
    [KC.RCBR, KC.LPRN, KC.RPRN, KC.TRNS,
     KC.LCBR, KC.LBRC, KC.RBRC, KC.NO],

    # 4 - CUSTOM Layer
    [KC.NO,   KC.VOLU, KC.INS,  KC.MUTE,
     KC.TRNS, KC.VOLD, KC.PSCR, KC.RSFT],

    # 5 - NAV Layer
    [KC.PGUP, KC.HOME, KC.UP,   KC.END,
     KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT],

    # 6 - MOUSE Layer
    #[KC.SCUP, KC.M2, KC.MUP, KC.M1,
    # KC.SCDN, KC.MLFT, KC.MDWN, KC.MRGT]
]

OS_LSFT = KC.OS(KC.LSFT) #, tap_time=1000)
OS_LCTL = KC.OS(KC.LCTL) #, tap_time=1000)
OS_LALT = KC.OS(KC.LALT) #, tap_time=1000)
OS_LGUI = KC.OS(KC.LGUI) #, tap_time=1000)

combos.combos = [
    #### Alpha Chords ####
                                 #  A
    Chord((O_CST, E_SYM),        KC.B),
    Chord((KC.Y, E_SYM),         KC.C),
    Chord((A_PRN, KC.R, KC.T),   KC.D),
                                 #  E
    Chord((KC.R, A_PRN),         KC.F),
    Chord((KC.T, KC.R),          KC.G),
    Chord((KC.I, E_SYM),         KC.H),
                                 #  I
    Chord((S_NUM, KC.T),         KC.J),
    Chord((O_CST, KC.Y),         KC.K),
    Chord((KC.I, KC.Y, E_SYM),   KC.L),
    Chord((O_CST, KC.I, KC.Y),   KC.M),
    Chord((O_CST, KC.I),         KC.N),
                                 #  O
    Chord((O_CST, KC.I, E_SYM),  KC.P),
    Chord((S_NUM, KC.T, A_PRN),  KC.Q),
                                 #  R
                                 #  S
                                 #  T
    Chord((KC.I, KC.Y),          KC.U),
    Chord((S_NUM, KC.R),         KC.V),
    Chord((S_NUM, A_PRN),        KC.W),
    Chord((S_NUM, KC.T, KC.R),   KC.X),
                                 #  Y
    Chord((S_NUM, KC.T, KC.R, A_PRN), KC.Z),

    #### Symbols ####
    Chord((KC.I, KC.Y, A_PRN),   KC.QUOT),
    Chord((KC.Y, A_PRN),         KC.DOT),
    Chord((KC.I, A_PRN),         KC.COMM),
    Chord((O_CST, A_PRN),        KC.SLSH),
    Chord((KC.I, KC.T),          KC.EXLM),
    
    #### Numeric Chords ####
    Chord((KC.N1, KC.N2), KC.N7),
    Chord((KC.N2, KC.N3), KC.N8),
    Chord((KC.N4, KC.N5), KC.N9),
    Chord((KC.N5, KC.N6), KC.N0),
    Chord((KC.N2, KC.N4), KC.BSPC),

    #### Other Chords ####
    Chord((O_CST, KC.I, KC.Y, E_SYM), KC.SPACE),
    Chord((O_CST, KC.R, A_PRN),       KC.ESC), 
    Chord((A_PRN, E_SYM),             KC.ENT),
    Chord((O_CST, KC.T, KC.R, A_PRN), KC.TAB),
    Chord((E_SYM, KC.R),              KC.BSPC),
    Chord((KC.I, KC.R),               KC.DEL),
    #Chord((O_CST, KC.I, KC.Y, A_PRN), KC.LCAP),
    # Locking Shift???

    #### One-Shot Chords ####
    Chord((E_SYM, KC.R, KC.T, S_NUM), OS_LSFT),
    Chord((S_NUM, E_SYM),             OS_LCTL),
    Chord((S_NUM, KC.I),              OS_LALT),
    Chord((O_CST, KC.Y),              OS_LGUI),

    #### LAYER Trigger Chords ####
    Chord((KC.R, E_SYM, KC.I),        DF_NAV),
    Chord((KC.UP, KC.LEFT, KC.RGHT),  DF_BASE),

    #Chord((A_PRN, KC.T, KC.Y),  DF_MOU)
]

if __name__ == '__main__':
    keyboard.go()

