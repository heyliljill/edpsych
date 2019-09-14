# 4.	(Table 6) Mean number of Overall gists employed in reading, per passage (3 paragraphs) (mrimgist, mriigist... 4 total)
# a.	Full gist (=3), 2-part relation gist (=5), partial gist (=1), 2 parts(=2), half-gist (=4), no gist (=0)
# b.	Break up into interest, difficulty, gender
# c.	By overall, WDI - Reading subsample, LWDI - Reading subsample

f = open('manova-gists','w+')

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
  suffix = "gist"
  
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
/EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(LSD)
/EMMEANS=TABLES(interest*difficulty) 
/EMMEANS=TABLES(sex*interest) 
/EMMEANS=TABLES(sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest) 
/EMMEANS=TABLES("""+domain+"""*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex) 
/EMMEANS=TABLES(sex*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest) 
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty)
/PRINT=DESCRIPTIVE
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.\n
  """

  compute = computeLine(intmast) + computeLine(intinst) + computeLine(boringmast) + computeLine(boringinst)
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  f.write(filteron)
  
  f.write(makeCopy(0))
  f.write(recodebasic("mr",suffix,0))
  #f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(0))
  
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