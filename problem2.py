def animate(speed, init):
    solution = []                                       # populate with positions of particles at each time step
    left = stringToBinary(init, 'L')                    # binary representation of left moving particles
    right = stringToBinary(init, 'R')                   # binary representation of right moving particles
    all = left | right                                  # binary representation of all particles

    while all > 0:                                      # check if particles still in frame
        solution.append(binaryToString(all, len(init)))
        left = left << speed
        right = right >> speed
        all = (left | right) & (pow(2, len(init)) - 1)  # masking is required to keep frame aligned

    solution.append(binaryToString(all, len(init)))     # need to append the empty frame to solution
    return solution


# takes the init string and converts it into a binary representation for the specified direction
def stringToBinary(init, direction):
    binary = 0                                          # store the binary representation of init here
    for index, x in enumerate(init):
        if x == direction:
            binary += pow(2, len(init) - 1 - index)     # add to binary value based on position of particle
    return binary

# takes a binary representation of particles and converts it to a string the size of the frame
def binaryToString(binary, size):
    string = ''                                         # store the string representation of positions here

    while binary > 0:
        if binary % 2 == 1:
            string += 'X'
        else:
            string += '.'
        binary //= 2                                    # note the use of floor division (cannot use floats)

    while len(string) < size:                           # populate remaining empty positions
        string += '.'

    return string[::-1]                                 # string needs to be reversed

print(animate(2, "..R...."))
print(animate(3, "RR..LRL"))
print(animate(2, "LRLR.LRLR"))
print(animate(10, "RLRLRLRLRL"))
print(animate(1, "..."))
print(animate(1, "LRRL.LR.LRR.R.LRRL."))