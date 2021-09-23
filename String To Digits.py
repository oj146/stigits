#!/usr/bin/python3
def parse_int(string):
    units = [1,"one",2,"two",3,"three",4,"four",5,"five",6,"six",7,"seven",8,"eight",9,"nine",10,"ten",11,"eleven",12,"twelve",13,"thirteen",14,"fourteen",15,"fifteen",16,"sixteen",17,"seventeen",18,"eighteen",19,"nineteen"]
    tens = [20,"twenty",30,"thirty",40,"forty",50,"fifty",60,"sixty",70,"seventy",80,"eighty",90,"ninety"]
    scales = [100,"hundred",1000,"thousand",1000000,"million",1000000000,"billion",1000000000000,"trillion"]
    string = string.replace("-"," ").split(" ")
    finalmsg = 0
    fm_framework = []
    for i in string:
        if i in units:
            fm_framework.append(units[units.index(i)-1])
        elif i in tens:
            fm_framework.append(tens[tens.index(i)-1])
        elif i in scales:                    
            finalmsg = 0
            tot = (scales[scales.index(i)-1])*(fm_framework[len(fm_framework)-1])
            finalmsg += tot
            fm_framework.remove(fm_framework[-1])
            fm_framework.append(finalmsg)
            for j in fm_framework:
                tot2 = 0
                if j < finalmsg:
                    tot2 = j * scales[scales.index(i)-1]
                    fm_framework[fm_framework.index(j)] = tot2 
            finalmsg = 0
    return sum(fm_framework)