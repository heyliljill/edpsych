{"filter":false,"title":"MRightWrong.py","tooltip":"/TablesRedo/MRightWrong.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":15,"column":38},"end":{"row":16,"column":53},"action":"remove","lines":["","GLM mmim1rw mmii1rw mmbm1rw mmbi1rw BY readspint sex "],"id":2}],[{"start":{"row":16,"column":0},"end":{"row":27,"column":14},"action":"remove","lines":["  /WSFACTOR=interest 2 Polynomial diff 2 Polynomial ","  /METHOD=SSTYPE(3) ","  /EMMEANS=TABLES(sex) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(interest) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(diff) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(sex*interest) ","  /EMMEANS=TABLES(sex*diff) ","  /EMMEANS=TABLES(interest*diff) ","  /EMMEANS=TABLES(sex*interest*diff) ","  /CRITERIA=ALPHA(.05) ","  /WSDESIGN=interest diff interest*diff ","  /DESIGN=sex."],"id":1},{"start":{"row":16,"column":0},"end":{"row":37,"column":38},"action":"insert","lines":["GLM mmim1rw mmii1rw mmbm1rw mmbi1rw BY readspint sex ","  /WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial ","  /METHOD=SSTYPE(3) ","  /EMMEANS=TABLES(OVERALL) ","  /EMMEANS=TABLES(readspint) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(sex) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(interest) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(readspint*sex) ","  /EMMEANS=TABLES(readspint*interest) ","  /EMMEANS=TABLES(readspint*difficulty) ","  /EMMEANS=TABLES(sex*interest) ","  /EMMEANS=TABLES(sex*difficulty) ","  /EMMEANS=TABLES(interest*difficulty) ","  /EMMEANS=TABLES(readspint*sex*interest) ","  /EMMEANS=TABLES(readspint*sex*difficulty) ","  /EMMEANS=TABLES(readspint*interest*difficulty) ","  /EMMEANS=TABLES(sex*interest*difficulty) ","  /EMMEANS=TABLES(readspint*sex*interest*difficulty) ","  /CRITERIA=ALPHA(.05) ","  /WSDESIGN=interest difficulty interest*difficulty ","  /DESIGN=readspint sex readspint*sex."]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":27,"column":14},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1436497617000,"hash":"49562682e15b35b45d224ba06508e626cd4453d7"}