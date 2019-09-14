# 5.	(Table 7) Mean number of paragraphs represented in reading, per passage (3 paragraphs) (mrimpara,mriipara...4 total)
# a.	3 paragraphs (=3), 2 paragraphs (=2), 1 paragraph (=1), topic only (=4), topic related (=5) 
# b.	Break up into interest, difficulty, gender
# c.	By overall, WDI - Reading subsample, LWDI - Reading subsample

f = open('manova-paragraphsB','w+')

def computeLine(variable):
  prefix=variable[0:2]
  level=variable[2:4]
  suffix=variable[4:]
  sum = prefix+level+suffix
  first = prefix+level+'1'+suffix
  second = prefix+level+'2'+suffix
  third = prefix+level+'3'+suffix
  computeLines ="""\nCOMPUTE """+sum+""" = """+first+""" + """+second+""" + """+third+""".
VARIABLE LABELS  """+ sum+""" '# times this type accuracy represented in """+level+""" level reading'. 
EXECUTE.\n
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
  
def recodebasic(prefix,suffix,num):
  levels = ["im","ii","bm","bi"]
  vars = ""
  for level in levels:
    vars = vars+prefix+level+suffix+" "
  recodetext= "recode "+vars+"("+str(num)+"=1) (else = 0).\n"
  return recodetext

  

def main():
  
  prefix = "mr"
  suffix = "para"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  domain = "readspint"
  
  filteron ="""USE ALL. 
COMPUTE filter_$=(group = 1  & pro = 0). 
VARIABLE LABELS filter_$ 'group = 1  & pro = 0 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
"""

  
  GLMtext = """\nGLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
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
/DESIGN="""+domain+""" sex """+domain+"""*sex.\n
  """

  compute = computeLine(intmast) + computeLine(intinst) + computeLine(boringmast) + computeLine(boringinst)
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  f.write(filteron)
  
  f.write(makeCopy(1))
  f.write(recodebasic("mr",suffix,1))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(1))
  
  f.write(makeCopy(2))
  f.write(recodebasic("mr",suffix,2))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(2))
 
  f.write(makeCopy(3))
  f.write(recodebasic("mr",suffix,3))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(3))
 
  f.write(makeCopy(4))
  f.write(recodebasic("mr",suffix,4))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(4))
 
  f.write(makeCopy(5))
  f.write(recodebasic("mr",suffix,5))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(5))
 
main()