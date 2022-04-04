from pygame import K_w, K_a, K_s, K_d

snake_move = {
    "right": [0, 10],
    "left": [0, -10],
    "up": [1, -10],
    "down": [1, 10]
}

key_direction = {
    K_w: "up",
    K_a: "left",
    K_d: "right",
    K_s: "down"
}

opposite_moves = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}
