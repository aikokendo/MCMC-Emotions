import graph

g = graph.Graph(['s','w','c','r','e','p','sp','co','cl','le','ar','st','m','a'],
[('s', 'e'),('s', 'p'),('w', 'e'),('w', 'p'),('c', 'e'),('c', 'p'),('r', 'e'),
('r', 'p'),('e', 'sp'),('e', 'co'),('e', 'cl'),('e', 'le'),('e', 'ar'),('e', 'st'),
('p', 'sp'),('p', 'co'),('p', 'cl'),('p', 'le'),('p', 'ar'),('p', 'st'),('m', 'sp'),
('m', 'co'),('m', 'cl'),('m', 'le'),('m', 'ar'),('m', 'st'),('a', 'sp'),('a', 'co'),
('a', 'cl'),('a', 'le'),('a', 'ar'),('a', 'st')])
g.print_graph()