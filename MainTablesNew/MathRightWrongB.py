# Math Right Wrong. mean number of correct answers, out of 12 problems (mmim1rw, mmim2rw, mmmim3rw... 12 total)


# mmimrw = mmim1rw + mmim2rw + mmim3rw 
# mmiirw = mmii1rw + mmii2rw + mmii3rw
# mmbmrw = mmbm1rw + mmbm2rw + mmbm3rw
# mmbirw = mmbi1rw + mmbi2rw + mmbi3rw 


f = open('manova-rightwrongB','w+')

def computeLine(variable):
  prefix=variable[0:2]
  level=variable[2:4]
  suffix=variable[4:]
  sum = prefix+level+suffix
  first = prefix+level+'1'+suffix
  second = prefix+level+'2'+suffix
  third = prefix+level+'3'+suffix
  computeLines ="""COMPUTE """+sum+""" = """+first+""" + """+second+""" + """+third+""".
VARIABLE LABELS  """+ sum+""" '# of correct answers from all problems in """+level+""" level math'. 
EXECUTE.
"""
  return computeLines

def makeCopy(int):
  num = str(int)
  text = "DATASET COPY  mainCopy"+num+" WINDOW=FRONT.\nDATASET ACTIVATE mainCopy"+num+".\n"
  return text
  
def closeCopy(int):
  num = str(int)
  text = "DATASET CLOSE mainCopy"+num+".\n"
  return text

def main():
  
  prefix = "mm"
  suffix = "rw"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  domain = "mathspint"
  
  filteron ="""USE ALL. 
COMPUTE filter_$=(group = 1  & pro = 0). 
VARIABLE LABELS filter_$ 'group = 1  & pro = 0 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
"""

  
  GLMtext = """GLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
/WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial 
/METHOD=SSTYPE(3) 
/EMMEANS=TABLES(OVERALL) 
/EMMEANS=TABLES(interest) COMPARE ADJ(BONFERRONI) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(BONFERRONI) 
/EMMEANS=TABLES(sex) COMPARE ADJ(BONFERRONI) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(BONFERRONI)
/EMMEANS=TABLES(interest*difficulty) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES(interest*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*interest) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*interest) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*difficulty) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*interest) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*interest) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*difficulty) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*interest*difficulty) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*interest*difficulty) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES(sex*interest*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) COMPARE("""+domain+""") ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty) COMPARE(interest) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty) COMPARE(difficulty) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty) COMPARE(sex) ADJ(BONFERRONI)
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty) COMPARE("""+domain+""") ADJ(BONFERRONI)
/PRINT=DESCRIPTIVE ETASQ
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """

  compute = computeLine(intmast) + computeLine(intinst) + computeLine(boringmast) + computeLine(boringinst)
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  f.write(filteron)
  f.write(makeCopy(1))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(1))
 
main()