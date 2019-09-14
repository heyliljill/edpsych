{"filter":false,"title":"PMcorrections.py","tooltip":"/FrequenciesMain/PMcorrections.py","undoManager":{"mark":157,"position":157,"stack":[[{"start":{"row":0,"column":0},"end":{"row":27,"column":43},"action":"insert","lines":["# 5.(Table 7) mean number of corrections, by type, out of 12 problems","# a. another step (pmim1ano), computational (pmim1com), copying (pmim1cop), operation/key (pmim1opk), operations choice (pmim1opc)","# b. Break up into interest, difficulty, gender","","# pmimano = pmim1ano + pmim2ano + pmim3ano ","# pmiiano = pmii1ano + pmii2ano + pmii3ano","# pmbmano = pmbm1ano + pmbm2ano + pmbm3ano","# pmbiano = pmbi1ano + pmbi2ano + pmbi3ano ","","# pmimcom = pmim1com + pmim2com + pmim3com ","# pmiicom = pmii1com + pmii2com + pmii3com","# pmbmcom = pmbm1com + pmbm2com + pmbm3com","# pmbicom = pmbi1com + pmbi2com + pmbi3com ","","# pmimcop = pmim1cop + pmim2cop + pmim3cop ","# pmiicop = pmii1cop + pmii2cop + pmii3cop","# pmbmcop = pmbm1cop + pmbm2cop + pmbm3cop","# pmbicop = pmbi1cop + pmbi2cop + pmbi3cop ","","# pmimopk = pmim1opk + pmim2opk + pmim3opk ","# pmiiopk = pmii1opk + pmii2opk + pmii3opk","# pmbmopk = pmbm1opk + pmbm2opk + pmbm3opk","# pmbiopk = pmbi1opk + pmbi2opk + pmbi3opk ","","# pmimopc = pmim1opc + pmim2opc + pmim3opc ","# pmiiopc = pmii1opc + pmii2opc + pmii3opc","# pmbmopc = pmbm1opc + pmbm2opc + pmbm3opc","# pmbiopc = pmbi1opc + pmbi2opc + pmbi3opc "],"id":1}],[{"start":{"row":27,"column":43},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":30,"column":0},"end":{"row":74,"column":58},"action":"insert","lines":["f = open('PMchecks.txt','w+')","","#This produces code for calculating frequencies for math variables","#COMPUTE pmchk = pmim1chk + pmim2chk + pmim3chk + pmim4chk... ","","","levels = [\"im\",\"ii\",\"bm\",\"bi\"]","prefix = \"pm\"","suffix = \"chk\"","types = [1,2,3,4,5,6]","",""," ","","switchtext = \"DATASET ACTIVATE pro.\\n\"","# repeat for each type","for i in range(len(types)):","    computeline = \"COMPUTE \"+prefix+suffix+\" = \"","    recodeline = \"recode \"","    variablelabels = \"\"\"VARIABLE LABELS  \"\"\"+prefix+suffix+\"\"\" \\'# of check types from all problems\\'.\\nEXECUTE.\\n\"\"\"","","    for lv in levels:","    #gets im, ii, bm, bi","        for k in range(1,4):","            #gets im1, im2, im3..","            variable = prefix + lv + str(k) + suffix","            computeline = computeline + variable + \" + \"","            recodeline = recodeline + variable + \" \"","    computeline = computeline.rstrip('+ ')+ \".\\n\"   ","    ","    recodeline = recodeline + \"(\"+str(types[i])+\"=1) (else = 0).\\n\"","    ","    frequencies = \"FREQUENCIES variables = \"+prefix+suffix+\"\\n/STATISTICS = mean sum\\n/ORDER=ANALYSIS.\\n\"","    ","    f.write(\"DATASET NAME pro.\\n\")","    ","    copytext = \"\"\"DATASET COPY  proCopy\"\"\"+str(types[i])+\"\"\" WINDOW=FRONT.\\nDATASET ACTIVATE proCopy\"\"\"+str(types[i])+\"\"\".\\n\"\"\"","    ","    f.write(copytext)","    f.write(recodeline)","    f.write(computeline)","    f.write(variablelabels)","    f.write(frequencies)","    f.write(switchtext)","    f.write(\"DATASET CLOSE proCopy\"+str(types[i])+\".\\n\\n\")"],"id":5}],[{"start":{"row":38,"column":14},"end":{"row":39,"column":21},"action":"remove","lines":["","types = [1,2,3,4,5,6]"],"id":6}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":38,"column":14},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":8}],[{"start":{"row":46,"column":70},"end":{"row":46,"column":75},"action":"remove","lines":["check"],"id":9},{"start":{"row":46,"column":70},"end":{"row":46,"column":71},"action":"insert","lines":["c"]}],[{"start":{"row":46,"column":71},"end":{"row":46,"column":72},"action":"insert","lines":["o"],"id":10}],[{"start":{"row":46,"column":72},"end":{"row":46,"column":73},"action":"insert","lines":["r"],"id":11}],[{"start":{"row":46,"column":73},"end":{"row":46,"column":74},"action":"insert","lines":["r"],"id":12}],[{"start":{"row":46,"column":74},"end":{"row":46,"column":75},"action":"insert","lines":["e"],"id":13}],[{"start":{"row":46,"column":75},"end":{"row":46,"column":76},"action":"insert","lines":["c"],"id":14}],[{"start":{"row":46,"column":70},"end":{"row":46,"column":76},"action":"remove","lines":["correc"],"id":15},{"start":{"row":46,"column":70},"end":{"row":46,"column":81},"action":"insert","lines":["corrections"]}],[{"start":{"row":46,"column":81},"end":{"row":46,"column":87},"action":"remove","lines":[" types"],"id":16}],[{"start":{"row":57,"column":66},"end":{"row":57,"column":67},"action":"remove","lines":["\""],"id":17}],[{"start":{"row":56,"column":4},"end":{"row":57,"column":66},"action":"remove","lines":["","    recodeline = recodeline + \"(\"+str(types[i])+\"=1) (else = 0).\\n"],"id":18}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["m"],"id":19}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["i"],"id":20}],[{"start":{"row":5,"column":0},"end":{"row":7,"column":43},"action":"remove","lines":["# pmiiano = pmii1ano + pmii2ano + pmii3ano","# pmbmano = pmbm1ano + pmbm2ano + pmbm3ano","# pmbiano = pmbi1ano + pmbi2ano + pmbi3ano "],"id":21}],[{"start":{"row":4,"column":41},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":22}],[{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"remove","lines":[" "],"id":23}],[{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["."],"id":24}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["."],"id":25}],[{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["."],"id":26}],[{"start":{"row":6,"column":43},"end":{"row":9,"column":43},"action":"remove","lines":["","# pmiicom = pmii1com + pmii2com + pmii3com","# pmbmcom = pmbm1com + pmbm2com + pmbm3com","# pmbicom = pmbi1com + pmbi2com + pmbi3com "],"id":27}],[{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":[" "],"id":28}],[{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["."],"id":29}],[{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["."],"id":30}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":["."],"id":31}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["m"],"id":32}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["i"],"id":33}],[{"start":{"row":9,"column":0},"end":{"row":11,"column":43},"action":"remove","lines":["# pmiicop = pmii1cop + pmii2cop + pmii3cop","# pmbmcop = pmbm1cop + pmbm2cop + pmbm3cop","# pmbicop = pmbi1cop + pmbi2cop + pmbi3cop "],"id":34}],[{"start":{"row":8,"column":43},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":35}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["p"],"id":36}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["o"],"id":37}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["c"],"id":38}],[{"start":{"row":11,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["# pmiiopk = pmii1opk + pmii2opk + pmii3opk","# pmbmopk = pmbm1opk + pmbm2opk + pmbm3opk","# pmbiopk = pmbi1opk + pmbi2opk + pmbi3opk ",""],"id":39}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["m"],"id":40}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["i"],"id":41}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["c"],"id":42}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"],"id":43}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["p"],"id":44}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":["m"],"id":45}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["i"],"id":46}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["m"],"id":47}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["i"],"id":48}],[{"start":{"row":12,"column":41},"end":{"row":15,"column":43},"action":"remove","lines":["","# pmiiopc = pmii1opc + pmii2opc + pmii3opc","# pmbmopc = pmbm1opc + pmbm2opc + pmbm3opc","# pmbiopc = pmbi1opc + pmbi2opc + pmbi3opc "],"id":49}],[{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["."],"id":50}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["."],"id":51}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["."],"id":52}],[{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["."],"id":53}],[{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"insert","lines":["."],"id":54}],[{"start":{"row":10,"column":43},"end":{"row":10,"column":44},"action":"insert","lines":["."],"id":55}],[{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":["."],"id":56}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["."],"id":57}],[{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["."],"id":58}],[{"start":{"row":17,"column":66},"end":{"row":18,"column":62},"action":"remove","lines":["","#COMPUTE pmchk = pmim1chk + pmim2chk + pmim3chk + pmim4chk... "],"id":59}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":18},"action":"remove","lines":["PMchecks"],"id":60},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["P"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["M"],"id":61}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["c"],"id":62}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["o"],"id":63}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["r"],"id":64}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["e"],"id":65}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["e"],"id":66}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["c"],"id":67}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["y"],"id":68}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["i"],"id":69}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["o"],"id":70}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["n"],"id":71}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["s"],"id":72}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["y"],"id":73}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["t"],"id":74}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["e"],"id":75}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["r"],"id":76}],[{"start":{"row":48,"column":21},"end":{"row":49,"column":23},"action":"remove","lines":["","    f.write(recodeline)"],"id":77}],[{"start":{"row":22,"column":14},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":78}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":21},"action":"insert","lines":["types = [1,2,3,4,5,6]"],"id":79}],[{"start":{"row":23,"column":10},"end":{"row":23,"column":20},"action":"remove","lines":[",2,3,4,5,6"],"id":80}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":13},"action":"remove","lines":["chk"],"id":81},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["n"],"id":82}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["o"],"id":83}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["\""],"id":84}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":["o"],"id":85}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["n"],"id":86}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"remove","lines":["a"],"id":87}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":["\""],"id":88}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["["],"id":89}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["\""],"id":90}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["a"],"id":91}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["n"],"id":92}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["d"],"id":93}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["d"],"id":94}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["o"],"id":95}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["\""],"id":96}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":[","],"id":97}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["\""],"id":98}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["c"],"id":99}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["o"],"id":100}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["m"],"id":101}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["\""],"id":102}],[{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":[","],"id":103}],[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["\""],"id":104}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["c"],"id":105}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["o"],"id":106}],[{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["p"],"id":107}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":["\""],"id":108}],[{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":[","],"id":109}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["\""],"id":110}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["o"],"id":111}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["p"],"id":112}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["k"],"id":113}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["\""],"id":114}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["m"],"id":115}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":["m"],"id":116}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":[","],"id":117}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["\""],"id":118}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["o"],"id":119}],[{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["p"],"id":120}],[{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["c"],"id":121}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["\""],"id":122}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["]"],"id":123}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":24},"action":"remove","lines":["types"],"id":124},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["u"],"id":125}],[{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["f"],"id":126}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["f"],"id":127}],[{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["i"],"id":128}],[{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["x"],"id":129}],[{"start":{"row":29,"column":42},"end":{"row":29,"column":43},"action":"insert","lines":["["],"id":130}],[{"start":{"row":29,"column":43},"end":{"row":29,"column":44},"action":"insert","lines":["i"],"id":131}],[{"start":{"row":29,"column":44},"end":{"row":29,"column":45},"action":"insert","lines":["]"],"id":132}],[{"start":{"row":31,"column":58},"end":{"row":31,"column":61},"action":"insert","lines":["[i]"],"id":133}],[{"start":{"row":37,"column":52},"end":{"row":37,"column":55},"action":"insert","lines":["[i]"],"id":134}],[{"start":{"row":43,"column":58},"end":{"row":43,"column":61},"action":"insert","lines":["[i]"],"id":135}],[{"start":{"row":47,"column":47},"end":{"row":47,"column":52},"action":"remove","lines":["types"],"id":136},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"insert","lines":["u"],"id":137}],[{"start":{"row":47,"column":49},"end":{"row":47,"column":50},"action":"insert","lines":["f"],"id":138}],[{"start":{"row":47,"column":50},"end":{"row":47,"column":51},"action":"insert","lines":["f"],"id":139}],[{"start":{"row":47,"column":51},"end":{"row":47,"column":52},"action":"insert","lines":["i"],"id":140}],[{"start":{"row":47,"column":52},"end":{"row":47,"column":53},"action":"insert","lines":["x"],"id":141}],[{"start":{"row":47,"column":109},"end":{"row":47,"column":114},"action":"remove","lines":["types"],"id":142},{"start":{"row":47,"column":109},"end":{"row":47,"column":110},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":110},"end":{"row":47,"column":111},"action":"insert","lines":["u"],"id":143}],[{"start":{"row":47,"column":111},"end":{"row":47,"column":112},"action":"insert","lines":["f"],"id":144}],[{"start":{"row":47,"column":112},"end":{"row":47,"column":113},"action":"insert","lines":["f"],"id":145}],[{"start":{"row":47,"column":113},"end":{"row":47,"column":114},"action":"insert","lines":["i"],"id":146}],[{"start":{"row":47,"column":114},"end":{"row":47,"column":115},"action":"insert","lines":["x"],"id":147}],[{"start":{"row":54,"column":40},"end":{"row":54,"column":45},"action":"remove","lines":["types"],"id":148},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":54,"column":41},"end":{"row":54,"column":42},"action":"insert","lines":["u"],"id":149}],[{"start":{"row":54,"column":42},"end":{"row":54,"column":43},"action":"insert","lines":["f"],"id":150}],[{"start":{"row":54,"column":43},"end":{"row":54,"column":44},"action":"insert","lines":["f"],"id":151}],[{"start":{"row":54,"column":44},"end":{"row":54,"column":45},"action":"insert","lines":["i"],"id":152}],[{"start":{"row":54,"column":45},"end":{"row":54,"column":46},"action":"insert","lines":["x"],"id":153}],[{"start":{"row":54,"column":40},"end":{"row":54,"column":46},"action":"remove","lines":["suffix"],"id":154}],[{"start":{"row":54,"column":42},"end":{"row":54,"column":43},"action":"remove","lines":["]"],"id":155}],[{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"remove","lines":["["],"id":156}],[{"start":{"row":47,"column":47},"end":{"row":47,"column":56},"action":"remove","lines":["suffix[i]"],"id":157},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"insert","lines":["i"]}],[{"start":{"row":47,"column":101},"end":{"row":47,"column":110},"action":"remove","lines":["suffix[i]"],"id":158},{"start":{"row":47,"column":101},"end":{"row":47,"column":102},"action":"insert","lines":["i"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":0},"end":{"row":18,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"8bbdcf096768607808ec81f5ebe713aa025b3105","timestamp":1456248778000}