{"filter":false,"title":"RConcurrentVerbSPINT.py","tooltip":"/TablesRedo/RConcurrentVerbSPINT.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["S"],"id":2}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["P"],"id":3}],[{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["I"],"id":4}],[{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["N"],"id":5}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["T"],"id":6}],[{"start":{"row":7,"column":11},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":8,"column":2},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":9,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["  mathread = \"r\"","  ","  for i in range(0,2):","    ## SELECT HIGH INTEREST ## ","    filtersign = [\"~=\",\"=\"]","    if mathread == \"m\":","      spint = \"mathspint\"","    elif mathread == \"r\":","      spint = \"readspint\"","    ","    filterText = \"\"\"USE ALL. \\nCOMPUTE filter_$=(\"\"\"+spint+filtersign[i]+ \"2\"+\"\"\"). \\nVARIABLE LABELS filter_$ '\"\"\" + spint+filtersign[i]+ \"2\" +\"\"\"(FILTER)'. \\nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \\nFORMATS filter_$ (f1.0). \\nFILTER BY filter_$. \\nEXECUTE.\\n\\n\"\"\"","  ","    f.write(filterText)"],"id":9}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["  "],"id":10},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["  "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["  "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["  "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["  "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["  "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["  "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["  "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["  "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["  "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["  "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["  "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["  "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["  "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["  "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["  "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["  "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["  "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["  "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["  "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["  "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["  "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["  "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["  "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["  "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["  "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["  "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["  "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["  "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["  "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["  "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"insert","lines":["  "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["  "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["  "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["  "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["  "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["  "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["  "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["  "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["  "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["  "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["  "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["  "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["  "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["  "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["  "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["  "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":2},"action":"insert","lines":["  "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["  "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["  "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["  "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["  "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":2},"action":"insert","lines":["  "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["  "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["  "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["  "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["  "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["  "]},{"start":{"row":82,"column":0},"end":{"row":82,"column":2},"action":"insert","lines":["  "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":2},"action":"insert","lines":["  "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":2},"action":"insert","lines":["  "]},{"start":{"row":85,"column":0},"end":{"row":85,"column":2},"action":"insert","lines":["  "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":2},"action":"insert","lines":["  "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"insert","lines":["  "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":2},"action":"insert","lines":["  "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["  "]},{"start":{"row":90,"column":0},"end":{"row":90,"column":2},"action":"insert","lines":["  "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["  "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"insert","lines":["  "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"insert","lines":["  "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["  "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":2},"action":"insert","lines":["  "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"insert","lines":["  "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":2},"action":"insert","lines":["  "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["  "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":2},"action":"insert","lines":["  "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["  "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":2},"action":"insert","lines":["  "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["  "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":2},"action":"insert","lines":["  "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["  "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":2},"action":"insert","lines":["  "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["  "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":2},"action":"insert","lines":["  "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["  "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":2},"action":"insert","lines":["  "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":2},"action":"insert","lines":["  "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":2},"action":"insert","lines":["  "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":2},"action":"insert","lines":["  "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":2},"action":"insert","lines":["  "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":2},"action":"insert","lines":["  "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":2},"action":"insert","lines":["  "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":2},"action":"insert","lines":["  "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":2},"action":"insert","lines":["  "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":2},"action":"insert","lines":["  "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":2},"action":"insert","lines":["  "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":2},"action":"insert","lines":["  "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":2},"action":"insert","lines":["  "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":2},"action":"insert","lines":["  "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":2},"action":"insert","lines":["  "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":2},"action":"insert","lines":["  "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["  "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"insert","lines":["  "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["  "]},{"start":{"row":128,"column":0},"end":{"row":128,"column":2},"action":"insert","lines":["  "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":2},"action":"insert","lines":["  "]},{"start":{"row":130,"column":0},"end":{"row":130,"column":2},"action":"insert","lines":["  "]},{"start":{"row":131,"column":0},"end":{"row":131,"column":2},"action":"insert","lines":["  "]},{"start":{"row":132,"column":0},"end":{"row":132,"column":2},"action":"insert","lines":["  "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":2},"action":"insert","lines":["  "]},{"start":{"row":134,"column":0},"end":{"row":134,"column":2},"action":"insert","lines":["  "]},{"start":{"row":135,"column":0},"end":{"row":135,"column":2},"action":"insert","lines":["  "]},{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["  "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["  "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":2},"action":"insert","lines":["  "]},{"start":{"row":139,"column":0},"end":{"row":139,"column":2},"action":"insert","lines":["  "]},{"start":{"row":140,"column":0},"end":{"row":140,"column":2},"action":"insert","lines":["  "]},{"start":{"row":141,"column":0},"end":{"row":141,"column":2},"action":"insert","lines":["  "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":2},"action":"insert","lines":["  "]},{"start":{"row":143,"column":0},"end":{"row":143,"column":2},"action":"insert","lines":["  "]},{"start":{"row":144,"column":0},"end":{"row":144,"column":2},"action":"insert","lines":["  "]},{"start":{"row":145,"column":0},"end":{"row":145,"column":2},"action":"insert","lines":["  "]},{"start":{"row":146,"column":0},"end":{"row":146,"column":2},"action":"insert","lines":["  "]},{"start":{"row":147,"column":0},"end":{"row":147,"column":2},"action":"insert","lines":["  "]},{"start":{"row":148,"column":0},"end":{"row":148,"column":2},"action":"insert","lines":["  "]},{"start":{"row":149,"column":0},"end":{"row":149,"column":2},"action":"insert","lines":["  "]},{"start":{"row":150,"column":0},"end":{"row":150,"column":2},"action":"insert","lines":["  "]},{"start":{"row":151,"column":0},"end":{"row":151,"column":2},"action":"insert","lines":["  "]},{"start":{"row":152,"column":0},"end":{"row":152,"column":2},"action":"insert","lines":["  "]},{"start":{"row":153,"column":0},"end":{"row":153,"column":2},"action":"insert","lines":["  "]},{"start":{"row":154,"column":0},"end":{"row":154,"column":2},"action":"insert","lines":["  "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":2},"action":"insert","lines":["  "]},{"start":{"row":156,"column":0},"end":{"row":156,"column":2},"action":"insert","lines":["  "]},{"start":{"row":157,"column":0},"end":{"row":157,"column":2},"action":"insert","lines":["  "]},{"start":{"row":158,"column":0},"end":{"row":158,"column":2},"action":"insert","lines":["  "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":2},"action":"insert","lines":["  "]},{"start":{"row":160,"column":0},"end":{"row":160,"column":2},"action":"insert","lines":["  "]},{"start":{"row":161,"column":0},"end":{"row":161,"column":2},"action":"insert","lines":["  "]},{"start":{"row":162,"column":0},"end":{"row":162,"column":2},"action":"insert","lines":["  "]},{"start":{"row":163,"column":0},"end":{"row":163,"column":2},"action":"insert","lines":["  "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":2},"action":"insert","lines":["  "]},{"start":{"row":165,"column":0},"end":{"row":165,"column":2},"action":"insert","lines":["  "]},{"start":{"row":166,"column":0},"end":{"row":166,"column":2},"action":"insert","lines":["  "]},{"start":{"row":167,"column":0},"end":{"row":167,"column":2},"action":"insert","lines":["  "]},{"start":{"row":168,"column":0},"end":{"row":168,"column":2},"action":"insert","lines":["  "]},{"start":{"row":169,"column":0},"end":{"row":169,"column":2},"action":"insert","lines":["  "]},{"start":{"row":170,"column":0},"end":{"row":170,"column":2},"action":"insert","lines":["  "]},{"start":{"row":171,"column":0},"end":{"row":171,"column":2},"action":"insert","lines":["  "]},{"start":{"row":172,"column":0},"end":{"row":172,"column":2},"action":"insert","lines":["  "]},{"start":{"row":173,"column":0},"end":{"row":173,"column":2},"action":"insert","lines":["  "]},{"start":{"row":174,"column":0},"end":{"row":174,"column":2},"action":"insert","lines":["  "]},{"start":{"row":175,"column":0},"end":{"row":175,"column":2},"action":"insert","lines":["  "]},{"start":{"row":176,"column":0},"end":{"row":176,"column":2},"action":"insert","lines":["  "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":2},"action":"insert","lines":["  "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":2},"action":"insert","lines":["  "]},{"start":{"row":179,"column":0},"end":{"row":179,"column":2},"action":"insert","lines":["  "]},{"start":{"row":180,"column":0},"end":{"row":180,"column":2},"action":"insert","lines":["  "]},{"start":{"row":181,"column":0},"end":{"row":181,"column":2},"action":"insert","lines":["  "]},{"start":{"row":182,"column":0},"end":{"row":182,"column":2},"action":"insert","lines":["  "]},{"start":{"row":183,"column":0},"end":{"row":183,"column":2},"action":"insert","lines":["  "]},{"start":{"row":184,"column":0},"end":{"row":184,"column":2},"action":"insert","lines":["  "]},{"start":{"row":185,"column":0},"end":{"row":185,"column":2},"action":"insert","lines":["  "]},{"start":{"row":186,"column":0},"end":{"row":186,"column":2},"action":"insert","lines":["  "]},{"start":{"row":187,"column":0},"end":{"row":187,"column":2},"action":"insert","lines":["  "]},{"start":{"row":188,"column":0},"end":{"row":188,"column":2},"action":"insert","lines":["  "]},{"start":{"row":189,"column":0},"end":{"row":189,"column":2},"action":"insert","lines":["  "]},{"start":{"row":190,"column":0},"end":{"row":190,"column":2},"action":"insert","lines":["  "]},{"start":{"row":191,"column":0},"end":{"row":191,"column":2},"action":"insert","lines":["  "]},{"start":{"row":192,"column":0},"end":{"row":192,"column":2},"action":"insert","lines":["  "]},{"start":{"row":193,"column":0},"end":{"row":193,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":2},"action":"remove","lines":["  "],"id":11}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"remove","lines":["  "],"id":12}],[{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"remove","lines":["  "],"id":13}],[{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"remove","lines":["  "],"id":14}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"remove","lines":["  "],"id":15}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"remove","lines":["  "],"id":16}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"remove","lines":["  "],"id":17}],[{"start":{"row":44,"column":2},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":18}],[{"start":{"row":44,"column":2},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"remove","lines":["  "],"id":20}]]},"ace":{"folds":[],"scrolltop":600,"scrollleft":0,"selection":{"start":{"row":47,"column":18},"end":{"row":47,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":36,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1436411204160,"hash":"571bd8d0f3d5cb948f616dcecace79978924dc6f"}