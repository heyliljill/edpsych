{"filter":false,"title":"RParagraphsSPINT.py","tooltip":"/TablesRedo/RParagraphsSPINT.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["S"],"id":2}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["P"],"id":3}],[{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["I"],"id":4}],[{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["N"],"id":5}],[{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["T"],"id":6}],[{"start":{"row":8,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["  ","  mathread = \"r\"","  ","  for i in range(0,2):","    ## SELECT HIGH INTEREST ## ","    filtersign = [\"~=\",\"=\"]","    if mathread == \"m\":","      spint = \"mathspint\"","    elif mathread == \"r\":","      spint = \"readspint\"","    ","    filterText = \"\"\"USE ALL. \\nCOMPUTE filter_$=(\"\"\"+spint+filtersign[i]+ \"2\"+\"\"\"). \\nVARIABLE LABELS filter_$ '\"\"\" + spint+filtersign[i]+ \"2\" +\"\"\"(FILTER)'. \\nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \\nFORMATS filter_$ (f1.0). \\nFILTER BY filter_$. \\nEXECUTE.\\n\\n\"\"\"","  ","    f.write(filterText)"],"id":7}],[{"start":{"row":21,"column":25},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["  "],"id":9},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["  "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["  "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["  "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["  "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["  "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["  "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["  "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["  "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["  "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["  "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["  "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["  "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["  "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["  "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["  "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["  "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["  "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["  "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["  "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["  "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["  "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["  "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["  "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["  "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["  "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["  "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["  "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["  "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["  "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["  "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"insert","lines":["  "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["  "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["  "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["  "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["  "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["  "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["  "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["  "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["  "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["  "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["  "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["  "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["  "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["  "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["  "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["  "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":2},"action":"insert","lines":["  "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["  "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["  "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["  "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["  "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":2},"action":"insert","lines":["  "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["  "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["  "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["  "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["  "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":2},"end":{"row":23,"column":4},"action":"remove","lines":["  "],"id":11}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"remove","lines":["  "],"id":12}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":13}],[{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"remove","lines":[":"],"id":14}],[{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"remove","lines":[" "],"id":15}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":26,"column":21},"end":{"row":26,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1436477441919,"hash":"775061eb980af831a99fa14941a3bb71857499c5"}