
from math import *
from itertools import *
from collections import *

data = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,24,1017,1101,0,36,1006,1101,0,30,1011,1101,26,0,1018,1101,32,0,1015,1101,34,0,1004,1101,0,37,1002,1101,25,0,1012,1102,38,1,1010,1101,29,0,1019,1101,308,0,1029,1102,1,696,1027,1102,1,429,1022,1102,1,21,1005,1102,1,33,1013,1101,39,0,1008,1102,20,1,1009,1101,0,652,1025,1102,313,1,1028,1101,0,31,1003,1102,661,1,1024,1101,35,0,1016,1101,0,23,1000,1102,28,1,1014,1102,0,1,1020,1102,27,1,1007,1101,0,1,1021,1102,22,1,1001,1101,703,0,1026,1101,0,422,1023,109,-5,2101,0,9,63,1008,63,31,63,1005,63,205,1001,64,1,64,1105,1,207,4,187,1002,64,2,64,109,6,2102,1,3,63,1008,63,37,63,1005,63,227,1105,1,233,4,213,1001,64,1,64,1002,64,2,64,109,11,21108,40,40,3,1005,1015,255,4,239,1001,64,1,64,1106,0,255,1002,64,2,64,109,-3,21107,41,40,2,1005,1011,275,1001,64,1,64,1105,1,277,4,261,1002,64,2,64,109,4,2107,28,-6,63,1005,63,297,1001,64,1,64,1106,0,299,4,283,1002,64,2,64,109,15,2106,0,0,4,305,1106,0,317,1001,64,1,64,1002,64,2,64,109,-23,2108,22,4,63,1005,63,337,1001,64,1,64,1105,1,339,4,323,1002,64,2,64,109,6,21101,42,0,0,1008,1011,40,63,1005,63,363,1001,64,1,64,1105,1,365,4,345,1002,64,2,64,109,-17,1207,7,21,63,1005,63,381,1105,1,387,4,371,1001,64,1,64,1002,64,2,64,109,14,1201,-1,0,63,1008,63,25,63,1005,63,407,1105,1,413,4,393,1001,64,1,64,1002,64,2,64,109,15,2105,1,0,1001,64,1,64,1105,1,431,4,419,1002,64,2,64,109,-23,2101,0,6,63,1008,63,36,63,1005,63,453,4,437,1106,0,457,1001,64,1,64,1002,64,2,64,109,10,2108,21,-5,63,1005,63,475,4,463,1106,0,479,1001,64,1,64,1002,64,2,64,109,-3,1201,2,0,63,1008,63,20,63,1005,63,505,4,485,1001,64,1,64,1105,1,505,1002,64,2,64,109,4,2107,35,-5,63,1005,63,527,4,511,1001,64,1,64,1105,1,527,1002,64,2,64,109,15,1206,-5,543,1001,64,1,64,1105,1,545,4,533,1002,64,2,64,109,-8,1205,3,563,4,551,1001,64,1,64,1106,0,563,1002,64,2,64,109,-5,1206,7,581,4,569,1001,64,1,64,1105,1,581,1002,64,2,64,109,-8,1207,-3,38,63,1005,63,599,4,587,1105,1,603,1001,64,1,64,1002,64,2,64,109,19,1205,-4,619,1001,64,1,64,1105,1,621,4,609,1002,64,2,64,109,-13,1208,-4,27,63,1005,63,639,4,627,1105,1,643,1001,64,1,64,1002,64,2,64,109,5,2105,1,8,4,649,1001,64,1,64,1106,0,661,1002,64,2,64,109,-16,1202,4,1,63,1008,63,34,63,1005,63,683,4,667,1106,0,687,1001,64,1,64,1002,64,2,64,109,26,2106,0,1,1001,64,1,64,1105,1,705,4,693,1002,64,2,64,109,-9,21102,43,1,-7,1008,1010,46,63,1005,63,725,1105,1,731,4,711,1001,64,1,64,1002,64,2,64,109,-26,1202,9,1,63,1008,63,26,63,1005,63,755,1001,64,1,64,1105,1,757,4,737,1002,64,2,64,109,34,21108,44,43,-8,1005,1017,773,1106,0,779,4,763,1001,64,1,64,1002,64,2,64,109,-15,21102,45,1,1,1008,1011,45,63,1005,63,801,4,785,1106,0,805,1001,64,1,64,1002,64,2,64,109,-14,1208,10,35,63,1005,63,821,1106,0,827,4,811,1001,64,1,64,1002,64,2,64,109,17,2102,1,-4,63,1008,63,20,63,1005,63,853,4,833,1001,64,1,64,1106,0,853,1002,64,2,64,109,6,21107,46,47,-4,1005,1015,871,4,859,1105,1,875,1001,64,1,64,1002,64,2,64,109,-10,21101,47,0,4,1008,1013,47,63,1005,63,901,4,881,1001,64,1,64,1105,1,901,4,64,99,21102,27,1,1,21102,1,915,0,1106,0,922,21201,1,37790,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,1,942,0,1106,0,922,22102,1,1,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1105,1,968,21201,-2,0,-2,109,-3,2105,1,0
]


class DictList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_dict = defaultdict(int)

    def __getitem__(self, item):
        if item < self.__len__():
            return super().__getitem__(item)
        else:
            return self.my_dict[item]

    def __setitem__(self, key, value):
        if key < self.__len__():
            super().__setitem__(key, value)
        else:
            self.my_dict[key] = value


def amp(input_data):
    my_data = DictList(data)
    ptr = 0
    registers = [0]*4
    reg_addrs = [0]*4
    rel_base = 0
    while my_data[ptr] != 99:
        opstr = str(my_data[ptr]).zfill(5)
        op = int(opstr[-2:])
        modes = [
            'padding',
            int(opstr[2]),
            int(opstr[1]),
            int(opstr[0]),
        ]
        for i in range(4):
            try:
                if modes[i] == 0:
                    x_star = my_data[ptr + i]
                    x = my_data[x_star]
                    registers[i] = x
                    reg_addrs[i] = x_star
                elif modes[i] == 1:
                    x = my_data[ptr + i]
                    registers[i] = x
                    reg_addrs[i] = 'fuck'
                elif modes[i] == 2:
                    x_star = my_data[ptr + i] + rel_base
                    x = my_data[x_star]
                    registers[i] = x
                    reg_addrs[i] = x_star
            except IndexError:
                pass
        if op == 1:
            my_data[reg_addrs[3]] = registers[1] + registers[2]
            ptr += 4
        elif op == 2:
            my_data[reg_addrs[3]] = registers[1] * registers[2]
            ptr += 4
        elif op == 3:
            my_data[reg_addrs[1]] = next(input_data)
            ptr += 2
        elif op == 4:
            yield registers[1]
            ptr += 2
        elif op == 5:
            if registers[1]:
                ptr = registers[2]
            else:
                ptr += 3
        elif op == 6:
            if not registers[1]:
                ptr = registers[2]
            else:
                ptr += 3
        elif op == 7:
            my_data[reg_addrs[3]] = int(registers[1] < registers[2])
            ptr += 4
        elif op == 8:
            my_data[reg_addrs[3]] = int(registers[1] == registers[2])
            ptr += 4
        elif op == 9:
            rel_base += registers[1]
            ptr += 2
        else:
            return


input_data = iter([2])

for x in amp(input_data):
    print(x)
