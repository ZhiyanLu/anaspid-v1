
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x0b::\xa5\xadp\xdcYSO<\x03\x115O\x83'
    
_lr_action_items = {'LPAR':([30,],[44,]),'CONSTANT':([7,16,17,41,42,43,44,68,69,70,72,73,],[-8,-6,-7,56,-36,-37,60,60,60,60,60,60,]),'SERVICE':([24,25,34,46,50,53,55,],[26,26,26,26,26,26,26,]),'LESS':([60,61,62,78,79,80,81,82,],[-30,-31,69,69,69,69,69,69,]),'RPAR':([60,61,62,78,79,80,81,82,],[-30,-31,71,-34,-32,-29,-35,-33,]),'PREFIX':([0,3,6,7,16,17,],[1,1,-5,-8,-6,-7,]),'SELECT':([0,3,4,5,6,7,9,16,17,],[-4,-4,11,-3,-5,-8,-2,-6,-7,]),'POINT':([7,16,17,28,32,38,56,57,58,59,64,66,71,75,77,],[-8,-6,-7,-23,-27,53,-42,-28,-40,-41,-26,53,-24,-25,-13,]),'DISTINCT':([11,],[14,]),'WHERE':([18,19,20,22,],[21,-15,23,-14,]),'GREATEREQ':([60,61,62,78,79,80,81,82,],[-30,-31,72,72,72,72,72,72,]),'COLON':([8,],[12,]),'$end':([2,10,48,54,],[0,-1,-10,-9,]),'LKEY':([7,16,17,21,23,24,25,34,36,40,46,50,53,55,],[-8,-6,-7,24,25,34,34,34,50,55,34,34,34,34,]),'UNION':([7,16,17,28,31,32,38,51,52,56,57,58,59,63,64,66,71,75,76,77,],[-8,-6,-7,-23,46,-27,-4,-20,-21,-42,-28,-40,-41,46,-26,-4,-24,-25,-22,-13,]),'RKEY':([7,16,17,27,28,31,32,33,38,39,45,47,49,51,52,56,57,58,59,63,64,65,66,67,71,74,75,76,77,],[-8,-6,-7,-16,-23,-4,-27,48,-4,54,-17,-18,64,-20,-21,-42,-28,-40,-41,-4,-26,75,-4,77,-24,-19,-25,-22,-13,]),'URI':([1,7,12,16,17,24,25,26,29,34,35,37,41,42,43,46,50,53,55,],[7,-8,17,-6,-7,7,7,7,7,7,-39,-38,7,-36,-37,7,7,7,7,]),'EQUALS':([60,61,62,78,79,80,81,82,],[-30,-31,70,70,70,70,70,70,]),'VARIABLE':([7,11,13,14,15,16,17,19,20,22,24,25,29,34,35,37,41,42,43,44,46,50,53,55,68,69,70,72,73,],[-8,-4,19,-11,-12,-6,-7,-15,22,-14,35,35,43,35,-39,-38,59,-36,-37,61,35,35,35,35,61,61,61,61,61,]),'OPTIONAL':([24,25,34,46,50,53,55,],[36,36,36,36,36,36,36,]),'ID':([1,7,12,16,17,24,25,26,29,34,35,37,41,42,43,46,50,53,55,],[8,-8,16,-6,-7,8,8,8,8,8,-39,-38,8,-36,-37,8,8,8,8,]),'ALL':([11,13,14,15,],[-4,18,-11,-12,]),'GREATER':([60,61,62,78,79,80,81,82,],[-30,-31,68,68,68,68,68,68,]),'FILTER':([24,25,34,46,50,53,55,],[30,30,30,30,30,30,30,]),'LESSEQ':([60,61,62,78,79,80,81,82,],[-30,-31,73,73,73,73,73,73,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bgp':([24,25,34,46,50,53,55,],[38,38,38,38,38,66,38,]),'predicate':([29,],[41,]),'join_block':([24,25,34,46,50,55,],[31,31,31,63,31,31,]),'service':([24,25,34,46,50,53,55,],[32,32,32,32,32,32,32,]),'distinct':([11,],[13,]),'expression':([44,68,69,70,72,73,],[62,78,79,80,81,82,]),'object':([41,],[57,]),'rest_join_block':([38,66,],[51,76,]),'uri':([1,24,25,26,29,34,41,46,50,53,55,],[6,37,37,40,42,37,58,37,37,37,37,]),'parse_sparql':([0,],[2,]),'group_graph_pattern':([24,25,34,50,55,],[33,39,49,65,67,]),'rest_union_block':([31,63,],[45,74,]),'prefix':([0,3,],[3,3,]),'triple':([24,25,34,46,50,53,55,],[28,28,28,28,28,28,28,]),'union_block':([24,25,34,50,55,],[27,27,27,27,27,]),'query':([4,],[10,]),'var_list':([13,],[20,]),'prefix_list':([0,3,],[4,9,]),'empty':([0,3,11,31,38,63,66,],[5,5,15,47,52,47,52,]),'subject':([24,25,34,46,50,53,55,],[29,29,29,29,29,29,29,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> parse_sparql","S'",1,None,None,None),
  ('parse_sparql -> prefix_list query','parse_sparql',2,'p_parse_sparql','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',75),
  ('prefix_list -> prefix prefix_list','prefix_list',2,'p_prefix_list','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',82),
  ('prefix_list -> empty','prefix_list',1,'p_empty_prefix_list','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',88),
  ('empty -> <empty>','empty',0,'p_empty','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',94),
  ('prefix -> PREFIX uri','prefix',2,'p_prefix','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',100),
  ('uri -> ID COLON ID','uri',3,'p_uri_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',106),
  ('uri -> ID COLON URI','uri',3,'p_uri_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',112),
  ('uri -> URI','uri',1,'p_uri_2','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',118),
  ('query -> SELECT distinct var_list WHERE LKEY group_graph_pattern RKEY','query',7,'p_query_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',124),
  ('query -> SELECT distinct ALL WHERE LKEY group_graph_pattern RKEY','query',7,'p_query_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',130),
  ('distinct -> DISTINCT','distinct',1,'p_distinct_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',136),
  ('distinct -> empty','distinct',1,'p_distinct_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',142),
  ('service -> SERVICE uri LKEY group_graph_pattern RKEY','service',5,'p_service','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',160),
  ('var_list -> var_list VARIABLE','var_list',2,'p_var_list','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',166),
  ('var_list -> VARIABLE','var_list',1,'p_single_var_list','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',172),
  ('group_graph_pattern -> union_block','group_graph_pattern',1,'p_ggp_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',178),
  ('union_block -> join_block rest_union_block','union_block',2,'p_union_block_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',184),
  ('rest_union_block -> empty','rest_union_block',1,'p_rest_union_block_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',190),
  ('rest_union_block -> UNION join_block rest_union_block','rest_union_block',3,'p_rest_union_block_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',196),
  ('join_block -> bgp rest_join_block','join_block',2,'p_join_block','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',202),
  ('rest_join_block -> empty','rest_join_block',1,'p_rest_join_block_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',208),
  ('rest_join_block -> POINT bgp rest_join_block','rest_join_block',3,'p_rest_join_block_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',214),
  ('bgp -> triple','bgp',1,'p_bgp_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',220),
  ('bgp -> FILTER LPAR expression RPAR','bgp',4,'p_bgp_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',226),
  ('bgp -> OPTIONAL LKEY group_graph_pattern RKEY','bgp',4,'p_bgp_2','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',232),
  ('bgp -> LKEY group_graph_pattern RKEY','bgp',3,'p_bgp_3','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',238),
  ('bgp -> service','bgp',1,'p_bgp_4','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',244),
  ('triple -> subject predicate object','triple',3,'p_triple_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',250),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_0','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',256),
  ('expression -> CONSTANT','expression',1,'p_expression_1','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',262),
  ('expression -> VARIABLE','expression',1,'p_expression_2','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',268),
  ('expression -> expression LESS expression','expression',3,'p_expression_3','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',274),
  ('expression -> expression LESSEQ expression','expression',3,'p_expression_4','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',280),
  ('expression -> expression GREATER expression','expression',3,'p_expression_5','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',286),
  ('expression -> expression GREATEREQ expression','expression',3,'p_expression_6','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',292),
  ('predicate -> uri','predicate',1,'p_predicate_uri','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',298),
  ('predicate -> VARIABLE','predicate',1,'p_predicate_var','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',304),
  ('subject -> uri','subject',1,'p_subject_uri','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',310),
  ('subject -> VARIABLE','subject',1,'p_subject_variable','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',316),
  ('object -> uri','object',1,'p_object_uri','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',322),
  ('object -> VARIABLE','object',1,'p_object_variable','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',328),
  ('object -> CONSTANT','object',1,'p_object_constant','/Library/Python/2.7/site-packages/ANAPSID-20130619-py2.7.egg/ANAPSID/Decomposer/parseQuery1_1.py',334),
]
