/*
Author: Matteo Romanello
email: matteo.romanello@gmail.com
*/

tree grammar cp_treeparser;

options {
    tokenVocab=cp_parser;
    language = Python;
    ASTLabelType = Tree;
}

@init{
import logging
self.logger = logging.getLogger("Main.cp_treeparser")
self.refs=[]
self.prev_ref={}
self.curr_ref=None
self.count=0
self.levels=[]
}

doc	:	citation+
;

citation
@after{
result = {}
result["refs"]=self.refs
}:
^(CITATION ref ref*)
;

ref	
@init{
if(self.curr_ref is None):
	self.curr_ref = {}
else:
	self.prev_ref=dict(self.curr_ref)
	self.curr_ref={}
}

@after{
if(not self.curr_ref.has_key('work') and self.prev_ref.has_key('work')):
	self.curr_ref["work"]=self.prev_ref["work"]
elif(not self.curr_ref.has_key('work')):
	self.curr_ref["work"]=None
self.refs.append(dict(self.curr_ref))
}
:	
^(REF work* scp editor*)
;

work:
^(WORK x+=LITERAL+)
{
y=[n.toString() for n in $x]
self.curr_ref["work"]=" ".join(y)
}
;

editor:
^(EDITOR LITERAL)
;

level[typ] returns [List levs]
@init{
if(typ=="end"):
	self.levels=[]
}
@after{
if(typ=="single"):
	self.curr_ref["scp"]["start"]=self.levels
else:
	self.curr_ref["scp"][typ]=self.levels
}
:
^(LEVEL lev+=INT) (^(LEVEL lev1+=INT {
self.count+=1
self.levels.append(str(lev1))
}))*
{
if(not typ=="end"):
	self.count+=1
temp=[]
temp = self.levels
self.levels=[]
self.levels.append(str(lev))
self.levels+=temp
}
;

scp
@init{
self.count=0
self.levels=[]
}

: (scp_single|scp_range)
;

scp_single
@init{
self.curr_ref["scp"]={}
}
:
^(SCOPE_S level["single"])
;

scp_range
@init{
self.curr_ref["scp"]={}
self.curr_ref["scp"]["start"]=[]
self.curr_ref["scp"]["end"]=[]
}
@after{
sl=len(self.curr_ref["scp"]["start"])
el=len(self.curr_ref["scp"]["end"])
if(el!=sl):
  count = 0
  self.curr_ref["scp"]["start"].reverse()
  while(len(self.curr_ref["scp"]["start"])>len(self.curr_ref["scp"]["end"])):
    self.curr_ref["scp"]["end"].append(None)
    count+=1
  for n,l in enumerate(self.curr_ref["scp"]["end"]):
    if(l is None):
      self.curr_ref["scp"]["end"][n]=self.curr_ref["scp"]["start"][n]
  self.curr_ref["scp"]["start"].reverse()
  self.curr_ref["scp"]["end"].reverse()
  
}
:
^(SCOPE_R ^(START level["start"]) ^(END level["end"]))
;