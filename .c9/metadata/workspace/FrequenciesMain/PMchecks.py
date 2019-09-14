{"filter":false,"title":"PMchecks.py","tooltip":"/FrequenciesMain/PMchecks.py","undoManager":{"mark":157,"position":157,"stack":[[{"start":{"row":0,"column":0},"end":{"row":46,"column":59},"action":"insert","lines":["## computational (=4), copying (=5), partial set-up (=2), set-up (=1), unattempted (=6), unfinished (=3)","","f = open('MMmistakes.txt','w+')","","#This produces code for calculating frequencies for math variables","#COMPUTE mmrw = mmim1rw + mmim2rw + mmim3rw + mmii1rw... ","","","levels = [\"im\",\"ii\",\"bm\",\"bi\"]","prefix = \"mm\"","suffix = \"mis\"","types = [1,2,3,4,5,6]","",""," ","","switchtext = \"DATASET ACTIVATE main.\\n\"","# repeat for each type","for i in range(len(types)):","    computeline = \"COMPUTE \"+prefix+suffix+\" = \"","    recodeline = \"recode \"","    variablelabels = \"\"\"VARIABLE LABELS  \"\"\"+prefix+suffix+\"\"\" \\'# of mistake types from all problems\\'.\\nEXECUTE.\\n\"\"\"","","    for lv in levels:","    #gets im, ii, bm, bi","        for k in range(1,4):","            #gets im1, im2, im3..","            variable = prefix + lv + str(k) + suffix","            computeline = computeline + variable + \" + \"","            recodeline = recodeline + variable + \" \"","    computeline = computeline.rstrip('+ ')+ \".\\n\"   ","    ","    recodeline = recodeline + \"(\"+str(types[i])+\"=1) (else = 0).\\n\"","    ","    frequencies = \"FREQUENCIES variables = \"+prefix+suffix+\"\\n/STATISTICS = mean sum\\n/ORDER=ANALYSIS.\\n\"","    ","    f.write(\"DATASET NAME main.\\n\")","    ","    copytext = \"\"\"DATASET COPY  mainCopy\"\"\"+str(types[i])+\"\"\" WINDOW=FRONT.\\nDATASET ACTIVATE mainCopy\"\"\"+str(types[i])+\"\"\".\\n\"\"\"","    ","    f.write(copytext)","    f.write(recodeline)","    f.write(computeline)","    f.write(variablelabels)","    f.write(frequencies)","    f.write(switchtext)","    f.write(\"DATASET CLOSE mainCopy\"+str(types[i])+\".\\n\\n\")"],"id":1}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":20},"action":"remove","lines":["MMmistakes"],"id":2},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["P"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["M"],"id":3}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["c"],"id":4}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["h"],"id":5}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["e"],"id":6}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["c"],"id":7}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["k"],"id":8}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["s"],"id":9}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":16},"action":"remove","lines":["computational"],"id":10},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["o"],"id":11}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["c"],"id":13}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["h"],"id":14}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["e"],"id":15}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["c"],"id":16}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["k"],"id":17}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"remove","lines":["4"],"id":18}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["1"],"id":19}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":25},"action":"remove","lines":["copying"],"id":20},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["a"],"id":21}],[{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["n"],"id":22}],[{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["'"],"id":23}],[{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["t"],"id":24}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":[" "],"id":25}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["t"],"id":26}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["e"],"id":27}],[{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":["l"],"id":28}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["l"],"id":29}],[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["5"],"id":30}],[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["2"],"id":31}],[{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"remove","lines":["2"],"id":32}],[{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"insert","lines":["3"],"id":33}],[{"start":{"row":0,"column":65},"end":{"row":0,"column":66},"action":"remove","lines":["1"],"id":34}],[{"start":{"row":0,"column":65},"end":{"row":0,"column":66},"action":"insert","lines":["4"],"id":35}],[{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"remove","lines":["6"],"id":36}],[{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"insert","lines":["5"],"id":37}],[{"start":{"row":0,"column":100},"end":{"row":0,"column":101},"action":"remove","lines":["3"],"id":38}],[{"start":{"row":0,"column":100},"end":{"row":0,"column":101},"action":"insert","lines":["6"],"id":39}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":49},"action":"remove","lines":["partial set-up"],"id":40},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":["c"]}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["o"],"id":41}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["m"],"id":42}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["p"],"id":43}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["u"],"id":44}],[{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["r"],"id":45}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["a"],"id":46}],[{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["t"],"id":47}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["i"],"id":48}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["o"],"id":49}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":["n"],"id":50}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"remove","lines":["n"],"id":51}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"remove","lines":["o"],"id":52}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"remove","lines":["i"],"id":53}],[{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"remove","lines":["t"],"id":54}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"remove","lines":["a"],"id":55}],[{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"remove","lines":["r"],"id":56}],[{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["t"],"id":57}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["a"],"id":58}],[{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["t"],"id":59}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["i"],"id":60}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["o"],"id":61}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":["n"],"id":62}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":56},"action":"remove","lines":["set"],"id":63}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"remove","lines":["-"],"id":64}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"remove","lines":["u"],"id":65}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"remove","lines":["p"],"id":66}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"insert","lines":["o"],"id":67}],[{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"insert","lines":["p"],"id":68}],[{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"insert","lines":["e"],"id":69}],[{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["r"],"id":70}],[{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"insert","lines":["a"],"id":71}],[{"start":{"row":0,"column":58},"end":{"row":0,"column":59},"action":"insert","lines":["t"],"id":72}],[{"start":{"row":0,"column":59},"end":{"row":0,"column":60},"action":"insert","lines":["i"],"id":73}],[{"start":{"row":0,"column":60},"end":{"row":0,"column":61},"action":"insert","lines":["o"],"id":74}],[{"start":{"row":0,"column":61},"end":{"row":0,"column":62},"action":"insert","lines":["n"],"id":75}],[{"start":{"row":0,"column":69},"end":{"row":0,"column":80},"action":"remove","lines":["unattempted"],"id":76},{"start":{"row":0,"column":69},"end":{"row":0,"column":70},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":70},"end":{"row":0,"column":71},"action":"insert","lines":["e"],"id":77}],[{"start":{"row":0,"column":71},"end":{"row":0,"column":72},"action":"insert","lines":["a"],"id":78}],[{"start":{"row":0,"column":72},"end":{"row":0,"column":73},"action":"insert","lines":["s"],"id":79}],[{"start":{"row":0,"column":73},"end":{"row":0,"column":74},"action":"insert","lines":["o"],"id":80}],[{"start":{"row":0,"column":74},"end":{"row":0,"column":75},"action":"insert","lines":["n"],"id":81}],[{"start":{"row":0,"column":75},"end":{"row":0,"column":76},"action":"insert","lines":["a"],"id":82}],[{"start":{"row":0,"column":76},"end":{"row":0,"column":77},"action":"insert","lines":["b"],"id":83}],[{"start":{"row":0,"column":77},"end":{"row":0,"column":78},"action":"insert","lines":["l"],"id":84}],[{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"insert","lines":["e"],"id":85}],[{"start":{"row":0,"column":79},"end":{"row":0,"column":80},"action":"insert","lines":["n"],"id":86}],[{"start":{"row":0,"column":80},"end":{"row":0,"column":81},"action":"insert","lines":["e"],"id":87}],[{"start":{"row":0,"column":81},"end":{"row":0,"column":82},"action":"insert","lines":["s"],"id":88}],[{"start":{"row":0,"column":82},"end":{"row":0,"column":83},"action":"insert","lines":["s"],"id":89}],[{"start":{"row":0,"column":90},"end":{"row":0,"column":100},"action":"remove","lines":["unfinished"],"id":90},{"start":{"row":0,"column":90},"end":{"row":0,"column":91},"action":"insert","lines":["a"]}],[{"start":{"row":0,"column":91},"end":{"row":0,"column":92},"action":"insert","lines":["l"],"id":91}],[{"start":{"row":0,"column":92},"end":{"row":0,"column":93},"action":"insert","lines":["t"],"id":92}],[{"start":{"row":0,"column":93},"end":{"row":0,"column":94},"action":"insert","lines":["e"],"id":93}],[{"start":{"row":0,"column":94},"end":{"row":0,"column":95},"action":"insert","lines":["r"],"id":94}],[{"start":{"row":0,"column":95},"end":{"row":0,"column":96},"action":"insert","lines":["n"],"id":95}],[{"start":{"row":0,"column":96},"end":{"row":0,"column":97},"action":"insert","lines":["a"],"id":96}],[{"start":{"row":0,"column":97},"end":{"row":0,"column":98},"action":"insert","lines":["t"],"id":97}],[{"start":{"row":0,"column":98},"end":{"row":0,"column":99},"action":"insert","lines":["e"],"id":98}],[{"start":{"row":0,"column":99},"end":{"row":0,"column":100},"action":"insert","lines":[" "],"id":99}],[{"start":{"row":0,"column":100},"end":{"row":0,"column":101},"action":"insert","lines":["s"],"id":100}],[{"start":{"row":0,"column":101},"end":{"row":0,"column":102},"action":"insert","lines":["e"],"id":101}],[{"start":{"row":0,"column":102},"end":{"row":0,"column":103},"action":"insert","lines":["t"],"id":102}],[{"start":{"row":0,"column":103},"end":{"row":0,"column":104},"action":"insert","lines":["-"],"id":103}],[{"start":{"row":0,"column":104},"end":{"row":0,"column":105},"action":"insert","lines":["u"],"id":104}],[{"start":{"row":0,"column":105},"end":{"row":0,"column":106},"action":"insert","lines":["p"],"id":105}],[{"start":{"row":5,"column":57},"end":{"row":5,"column":65},"action":"insert","lines":["pmii3chk"],"id":106}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":13},"action":"remove","lines":["mmrw"],"id":107},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["m"],"id":108}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["c"],"id":109}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["h"],"id":110}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["k"],"id":111}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":24},"action":"remove","lines":["mmim1rw"],"id":112},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["m"],"id":113}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["i"],"id":114}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["m"],"id":115}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["1"],"id":116}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["c"],"id":117}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["h"],"id":118}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["k"],"id":119}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":35},"action":"remove","lines":["mmim2rw"],"id":120},{"start":{"row":5,"column":28},"end":{"row":5,"column":36},"action":"insert","lines":["pmim1chk"]}],[{"start":{"row":5,"column":39},"end":{"row":5,"column":46},"action":"remove","lines":["mmim3rw"],"id":121},{"start":{"row":5,"column":39},"end":{"row":5,"column":47},"action":"insert","lines":["pmim1chk"]}],[{"start":{"row":5,"column":50},"end":{"row":5,"column":57},"action":"remove","lines":["mmii1rw"],"id":122},{"start":{"row":5,"column":50},"end":{"row":5,"column":58},"action":"insert","lines":["pmim1chk"]}],[{"start":{"row":5,"column":62},"end":{"row":5,"column":70},"action":"remove","lines":["pmii3chk"],"id":123}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["1"],"id":124},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["2"]}],[{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"remove","lines":["1"],"id":125},{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"insert","lines":["3"]}],[{"start":{"row":5,"column":54},"end":{"row":5,"column":55},"action":"remove","lines":["1"],"id":126}],[{"start":{"row":5,"column":54},"end":{"row":5,"column":55},"action":"insert","lines":["4"],"id":127}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":12},"action":"remove","lines":["mm"],"id":128},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["p"]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["m"],"id":129}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":13},"action":"remove","lines":["mis"],"id":130},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["c"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["h"],"id":131}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["k"],"id":132}],[{"start":{"row":21,"column":70},"end":{"row":21,"column":77},"action":"remove","lines":["mistake"],"id":133},{"start":{"row":21,"column":70},"end":{"row":21,"column":71},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":71},"end":{"row":21,"column":72},"action":"insert","lines":["h"],"id":134}],[{"start":{"row":21,"column":72},"end":{"row":21,"column":73},"action":"insert","lines":["e"],"id":135}],[{"start":{"row":21,"column":73},"end":{"row":21,"column":74},"action":"insert","lines":["c"],"id":136}],[{"start":{"row":21,"column":74},"end":{"row":21,"column":75},"action":"insert","lines":["k"],"id":137}],[{"start":{"row":16,"column":31},"end":{"row":16,"column":35},"action":"remove","lines":["main"],"id":138},{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"insert","lines":["p"]}],[{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["r"],"id":139}],[{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["o"],"id":140}],[{"start":{"row":36,"column":26},"end":{"row":36,"column":30},"action":"remove","lines":["main"],"id":141},{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"insert","lines":["p"]}],[{"start":{"row":36,"column":27},"end":{"row":36,"column":28},"action":"insert","lines":["r"],"id":142}],[{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":["o"],"id":143}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":40},"action":"remove","lines":["mainCopy"],"id":144},{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"insert","lines":["p"]}],[{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"insert","lines":["r"],"id":145}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["o"],"id":146}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["C"],"id":147}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["o"],"id":148}],[{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["p"],"id":149}],[{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["u"],"id":150}],[{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"remove","lines":["u"],"id":151}],[{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["y"],"id":152}],[{"start":{"row":38,"column":93},"end":{"row":38,"column":97},"action":"remove","lines":["main"],"id":153},{"start":{"row":38,"column":93},"end":{"row":38,"column":94},"action":"insert","lines":["p"]}],[{"start":{"row":38,"column":94},"end":{"row":38,"column":95},"action":"insert","lines":["r"],"id":154}],[{"start":{"row":38,"column":95},"end":{"row":38,"column":96},"action":"insert","lines":["o"],"id":155}],[{"start":{"row":46,"column":27},"end":{"row":46,"column":31},"action":"remove","lines":["main"],"id":156},{"start":{"row":46,"column":27},"end":{"row":46,"column":28},"action":"insert","lines":["p"]}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"insert","lines":["r"],"id":157}],[{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["o"],"id":158}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1456246956000,"hash":"ae488233ded0dbbadda865e74c367acdf2f55801"}