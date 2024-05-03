enc = []

while True:
    print("pig pen cipher encryption")
    inp = input('enter message for encryption:')
    enc.append(inp)

# ⅃ ⊔ ⌞ ⊐ □ ⊏ ꓶ ⊓ ｢ ⟓ ⊍ ⦝ ⟄ ⊡ ⟃ ⸅ ⍝ ⟔ v > < ⋀ ⟇ ⋗ ⋖ ⟑




    if inp == "": # if user input is empty, break while loop and end
        enc.pop(-1) #pops end of string so the empty char is not shown
        break

print("bye bye :)")

print(enc)
