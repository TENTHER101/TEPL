
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightPOWERleftLPARENRPARENAND DATATYPE DIVIDE EQ EXPECTING FROM GE GT IDENTIFIER IF INPUT LE LPAREN LT MINUS NE NO NUMBER OUTPUT PLUS POWER RANDOM RPAREN SET TEXT THEN TIMES TO YES\n    statement : OUTPUT expression\n              | OUTPUT ask\n    \n    ask : TEXT EXPECTING INPUT AND DATATYPE\n    \n    random_statement : RANDOM DATATYPE FROM expression TO expression\n    \n    var_assignment : SET IDENTIFIER\n    \n    statement : var_assignment TO expression\n              | var_assignment \n              | var_assignment TO ask\n    \n    statement : IF comp_expr THEN statement\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression POWER expression\n    expression : LPAREN expression RPAREN\n    expression : YES\n               | NO\n    \n    comp_expr  : expression EQ expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression NE expression\n    \n    expression : comp_expr\n    expression : NUMBERexpression : IDENTIFIERexpression : random_statementexpression : TEXTexpression : INPUT'
    
_lr_action_items = {'OUTPUT':([0,39,],[2,2,]),'IF':([0,39,],[4,4,]),'SET':([0,39,],[5,5,]),'$end':([1,3,6,7,9,10,11,12,13,14,15,16,21,22,37,38,40,41,42,43,44,45,46,47,48,49,50,51,54,57,59,],[0,-7,-1,-2,-16,-17,-24,-25,-26,-27,-28,-29,-28,-5,-6,-8,-10,-11,-12,-13,-14,-18,-19,-20,-21,-22,-23,-15,-9,-3,-4,]),'LPAREN':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'YES':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NO':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'NUMBER':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'IDENTIFIER':([2,4,5,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[13,13,22,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'TEXT':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[15,21,21,15,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'INPUT':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,35,53,58,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,52,16,16,]),'RANDOM':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'TO':([3,9,10,11,12,13,14,16,21,22,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[18,-16,-17,-24,-25,-26,-27,-29,-28,-5,-10,-11,-12,-13,-14,-18,-19,-20,-21,-22,-23,-15,58,-4,]),'PLUS':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[23,-16,-17,-24,-25,-26,-27,-28,-29,-24,23,-28,23,23,-10,-11,-12,-13,-14,23,23,23,23,23,23,-15,23,23,]),'MINUS':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[24,-16,-17,-24,-25,-26,-27,-28,-29,-24,24,-28,24,24,-10,-11,-12,-13,-14,24,24,24,24,24,24,-15,24,24,]),'TIMES':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[25,-16,-17,-24,-25,-26,-27,-28,-29,-24,25,-28,25,25,25,25,-12,-13,-14,25,25,25,25,25,25,-15,25,25,]),'DIVIDE':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[26,-16,-17,-24,-25,-26,-27,-28,-29,-24,26,-28,26,26,26,26,-12,-13,-14,26,26,26,26,26,26,-15,26,26,]),'POWER':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[27,-16,-17,-24,-25,-26,-27,-28,-29,-24,27,-28,27,27,27,27,27,27,27,27,27,27,27,27,27,-15,27,27,]),'EQ':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[28,-16,-17,-24,-25,-26,-27,-28,-29,-24,28,-28,28,28,-10,-11,-12,-13,-14,28,28,28,28,28,28,-15,28,28,]),'GT':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[29,-16,-17,-24,-25,-26,-27,-28,-29,-24,29,-28,29,29,-10,-11,-12,-13,-14,29,29,29,29,29,29,-15,29,29,]),'LT':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[30,-16,-17,-24,-25,-26,-27,-28,-29,-24,30,-28,30,30,-10,-11,-12,-13,-14,30,30,30,30,30,30,-15,30,30,]),'GE':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[31,-16,-17,-24,-25,-26,-27,-28,-29,-24,31,-28,31,31,-10,-11,-12,-13,-14,31,31,31,31,31,31,-15,31,31,]),'LE':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[32,-16,-17,-24,-25,-26,-27,-28,-29,-24,32,-28,32,32,-10,-11,-12,-13,-14,32,32,32,32,32,32,-15,32,32,]),'NE':([6,9,10,11,12,13,14,15,16,19,20,21,34,37,40,41,42,43,44,45,46,47,48,49,50,51,56,59,],[33,-16,-17,-24,-25,-26,-27,-28,-29,-24,33,-28,33,33,-10,-11,-12,-13,-14,33,33,33,33,33,33,-15,33,33,]),'RPAREN':([9,10,11,12,13,14,16,21,34,40,41,42,43,44,45,46,47,48,49,50,51,59,],[-16,-17,-24,-25,-26,-27,-29,-28,51,-10,-11,-12,-13,-14,-18,-19,-20,-21,-22,-23,-15,-4,]),'THEN':([9,10,11,12,13,14,16,19,21,40,41,42,43,44,45,46,47,48,49,50,51,59,],[-16,-17,-24,-25,-26,-27,-29,39,-28,-10,-11,-12,-13,-14,-18,-19,-20,-21,-22,-23,-15,-4,]),'EXPECTING':([15,],[35,]),'DATATYPE':([17,55,],[36,57,]),'FROM':([36,],[53,]),'AND':([52,],[55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,39,],[1,54,]),'var_assignment':([0,39,],[3,3,]),'expression':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[6,20,34,37,40,41,42,43,44,45,46,47,48,49,50,56,59,]),'ask':([2,18,],[7,38,]),'comp_expr':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[11,19,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'random_statement':([2,4,8,18,23,24,25,26,27,28,29,30,31,32,33,53,58,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> OUTPUT expression','statement',2,'p_statement_output','parser.py',18),
  ('statement -> OUTPUT ask','statement',2,'p_statement_output','parser.py',19),
  ('ask -> TEXT EXPECTING INPUT AND DATATYPE','ask',5,'p_ask_statement','parser.py',26),
  ('random_statement -> RANDOM DATATYPE FROM expression TO expression','random_statement',6,'p_random_statement','parser.py',33),
  ('var_assignment -> SET IDENTIFIER','var_assignment',2,'p_statement_var_assignment','parser.py',40),
  ('statement -> var_assignment TO expression','statement',3,'p_statement_assignment','parser.py',47),
  ('statement -> var_assignment','statement',1,'p_statement_assignment','parser.py',48),
  ('statement -> var_assignment TO ask','statement',3,'p_statement_assignment','parser.py',49),
  ('statement -> IF comp_expr THEN statement','statement',4,'p_statement_if','parser.py',59),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',66),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',67),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',68),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',69),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','parser.py',70),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',76),
  ('expression -> YES','expression',1,'p_expression_boolean','parser.py',82),
  ('expression -> NO','expression',1,'p_expression_boolean','parser.py',83),
  ('comp_expr -> expression EQ expression','comp_expr',3,'p_comp_expr','parser.py',90),
  ('comp_expr -> expression GT expression','comp_expr',3,'p_comp_expr','parser.py',91),
  ('comp_expr -> expression LT expression','comp_expr',3,'p_comp_expr','parser.py',92),
  ('comp_expr -> expression GE expression','comp_expr',3,'p_comp_expr','parser.py',93),
  ('comp_expr -> expression LE expression','comp_expr',3,'p_comp_expr','parser.py',94),
  ('comp_expr -> expression NE expression','comp_expr',3,'p_comp_expr','parser.py',95),
  ('expression -> comp_expr','expression',1,'p_expression_comp_expr','parser.py',102),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',108),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',113),
  ('expression -> random_statement','expression',1,'p_expression_random','parser.py',118),
  ('expression -> TEXT','expression',1,'p_expression_text','parser.py',123),
  ('expression -> INPUT','expression',1,'p_expression_input','parser.py',128),
]
