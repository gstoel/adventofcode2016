import numpy as np

pad = np.arange(1, 10 ,1 ).reshape((3,3))

def move(current, moves):
    row, col = np.where(pad==current)[0][0], np.where(pad==current)[1][0]
    for m in moves:
        if m is 'U':
            row = max(row-1, 0)
        if m is 'D':
            row = min(row+1, 2)
        if m is 'L':
            col = max(col-1, 0)
        if m is 'R':
            col = min(col+1, 2)
    return pad[row][col]

note = ['RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDDRUDLRRDDUDUUDULUDRDULRUDRULRDRUDLDDULRRDLDRLUDDLLDRDDDUDDLUDUDULDRLLDRLULRLURDLULRUUUDRULLUUDLRDLDDUDRRRLDLRUUURRLDDRRRURLLULDUULLDRLRDLLDURDLDDULLDDLDLUURRRURLRURLLRRDURLDUDDLULUUULULLLDRRRRRLULRDUDURURLULRURRRLLUURDURULRRUULDRDLULDLLUDLUDRLUDLRRLDLLDLDUDDLULLDRULRLRULDURRDLDLLUDRLLDRRDLDUDUURUURDUUDDDLDLDDRDLUDLDUUUUDLDRLRURDLURURDLLLUURURDRDLUDLLRUDULLLDLULLULLDLDDRDRRRUDDDUDDDDRULLLLRLDDLLRDRLLLRRLDRRUDRUUURLLLRULRRDURDLDRLDDUUDUUURRLRRUDLDLDDRUDLULLUUDUUUDLUDDRUULLLURUDDDDLRUDDLLLRUR',
'LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRLRURLDDDURUDUUURDRLDDLUUUDRUDUDDDLLURLLULRUULLUDRULUDDULDUDUDULLDRUUUULRDUUDLUDURDLLRLLRLUUDUUDRLLLRULUURUDLDRLLDUDLDDRULDULDURRLDDDUDUDDRUDUDRDURLLLLLULDRDDLLUDULLLUDRURLDLDLDULLDDRURRLUDDRLURLULRLDDDUUUURLRDLRURDDURLDLRRLLRLRLUURRLLDDLDRLRDUDDLLDDDURUUDURLRRDUULRRDDRRUULDRLRUDRRLDDRLDRULLDLDURRULDURRRDLRRLRLLLRLDRLLULRRLLLLLDLDDULDLLDLLDUUDDRLURUUUUULRDDLRDLRDRDRDLUDDLDDRULLUDDRLDLLUDRLUURRLUDURURLLRURRURRLRLLRLURURDDDDRRLURDUULLUU',
'LLRRDURRDLDULRDUDLRDRDRURULDURUDRRURDDDRLDLDRDRDRDRULDUURLULDDUURUULUDULLDUDLLLLDLLLDRLUUULLULDDRRUDDULLLULRDRULDDULDUDRDDLUUURULDLLUDUUUUURUDLLDRDULLRULLDURDRLLDLDRDDURUULUDURRRUULLDUUDDURDURLDLRRLLDURDDLRRRUDLRRRDLDRLUDLUDRDRLDDLLLRLLRURDLRDUUUURRLULDDLDLLLUDRDRLRRDURDDLURDLDDDULLLRRLDDDRULDDDLRRDULUUUDRRULDDLLLURDRRLLLUULDRRRUURRDDLULDRLULDDDLDULDRRRULRULLURLURULLLLRUDRRRDRDRDLDULURLRRRRLRUDDRRRUURUURLLRURURUURRURRDLDLLUDRRRDUDDRDURLLRLRRULD',
'DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURLRUUUDLLDUUDDUULDUULLRUDRURLUDRDLRUDDDLULUDLLDRULULLLDRRULDLLUURLRRRLDRDLDRURRRRDLRUUDULLRLLLDLRUDLDUUDRLDLRDRLRDLDDDUDLRUDLDDLLLDRLLRRUUDRDDUUURURRRUUDLRRDDRUDLDDULULDLRRLRDDUDRUURRUULURLURUDRRURRRULDDDDURDLUUULUULULRDLRRRRRURURRLRUULDUUURRDRRDLDUUUULLULLLLUDLUUDUURRDLDLRRRLUUURULDULDLDRLLURDRUULLLLLULLLDRURURRUDRRRRUDUDUDRUDUDRDRULUUDRURDDUUDLDLDUURUDURLRLRRDRDRDLLDUDDULLRDLDDRLLDLRDURDDULLLDLLLULDLUUUDLDRDLURUURDDLRDLLLLLRLURDLLLULLRRLU',
'DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULDRRDRLUULUDDLUURURDLDDDRDRUDURLDDLUDUURULRRUUDRLURRLRLDURRRULRLDDDRUDDDDDUDDULLLRRLLDULDRULUDLRRDLLUDRDLDULRLLLUULLRULRLLLLUDDRRDRLULDLDLURDDRUDDLDLDLDRULDLLDDUUDULUULULLURDURRLLUDRULLRDUDRDRURDRDRDURUUDULDDRURUDLLUUDUUDURDLRDRURUDRUURLUUURLRLUDRUDRUURLLUDRLURDDURRUDRDRLRRLDDDRDDLUUUDDLULDUURUDUDLLDRURDURRDULRLURRDLDDRLUDRLDLRLDDUURRULDDLDUDDLRDULLDDDLDUUUUDLRUDUDLDRDLRDDLDLRLLUDDRRLUDLDUUULLDDRLRRDLRRRRUDDLRLLULRLRDURDUDDRRULLDDLDLRRDLLULDURURDDURLRLULULURRUDUDRDLURULDUDLUULDUUURLLRUDLLRDLRUDRLULDUDRRDUUDUUULUUUDDRUD']

code = [5]
for n in note:
    code.append(move(code[-1], n))

print(code[1:])
