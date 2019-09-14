# 7.	(Table 9) Means for types of distortions in reading, per passage (3 paragraphs)
# a.	Misread (=3), misunderstood (=7), misremembered (=4), miscombined (=2), mislabeled (=6), included extraneous information (=1), added information, elaborated on text (=10), comments on text (=11)

## IDEA: DO mrimsub1 recode them level by level (like 1=1..2=1...) then do same for mrimsub2. for each level, combine them somehow?
## Total will never be more than 1. So take sum of sub1 and sub2. Then do GLM on it.


f = open('manova-distortions','w+')

def computeDistLine(variable):
  prefix=variable[0:2]
  level=variable[2:4]
  suffix=variable[4:7]
  sum = prefix+level+suffix
  first = prefix+level+suffix+"1"
  second = prefix+level+suffix+"2"
  computeLines ="""\nCOMPUTE """+sum+""" = """+first+""" + """+second+""".
VARIABLE LABELS  """+ sum+""" '# times this type distortion represented in """+level+""" level reading'. 
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
  suffix = "sub"
  
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
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """

  compute = computeDistLine(intmast) + computeDistLine(intinst) + computeDistLine(boringmast) + computeDistLine(boringinst)
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  f.write(filteron)
  
  nums = [1,2,3,4,5,6,7,10,11]
  for num in nums:
    f.write(makeCopy(num))
    f.write(recodebasic("mr",suffix+'1',num))
    f.write(recodebasic("mr",suffix+'2',num))
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write(closeCopy(num))
  
  
main()