import graph
import gibbs

g = graph.Graph(['s','w','c','r','e','p','sp','co','cl','le','ar','st','m','a'],
[('s', 'e'),('s', 'p'),('w', 'e'),('w', 'p'),('c', 'e'),('c', 'p'),('r', 'e'),
('r', 'p'),('e', 'sp'),('e', 'co'),('e', 'cl'),('e', 'le'),('e', 'ar'),('e', 'st'),
('p', 'sp'),('p', 'co'),('p', 'cl'),('p', 'le'),('p', 'ar'),('p', 'st'),('m', 'sp'),
('m', 'co'),('m', 'cl'),('m', 'le'),('m', 'ar'),('m', 'st'),('a', 'sp'),('a', 'co'),
('a', 'cl'),('a', 'le'),('a', 'ar'),('a', 'st')])

g.add_prob_table('s',[{'field': 's', 'value': True, 'prob':[1]}])
g.add_prob_table('w',[{'field': 'w', 'value': True, 'prob':[1]}])
g.add_prob_table('c',[{'field': 'c', 'value': True, 'prob':[1]}])
g.add_prob_table('r',[{'field': 'r', 'value': True, 'prob':[1]}])
g.add_prob_table('m',[{'field': 'm', 'value': True, 'prob':[1]}])
g.add_prob_table('a',[{'field': 'a', 'value': True, 'prob':[1]}])
g.add_prob_table('e',[{'field': 's', 'value': True, 'prob':
                        [{'field':'w', 'value': True, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'w', 'value': False, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 's', 'value': False, 'prob':
                          [{'field': 'w', 'value': True, 'prob':
                              [{'field': 'c', 'value': True, 'prob':
                                  [{'field': 'r', 'value': True, 'prob': [1]},
                                   {'field': 'r', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'c', 'value': False, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [1]},
                                    {'field': 'r', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'w', 'value': False, 'prob':
                               [{'field': 'c', 'value': True, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [1]},
                                    {'field': 'r', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'c', 'value': False, 'prob':
                                    [{'field': 'r', 'value': True, 'prob': [1]},
                                     {'field': 'r', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('p',[{'field': 's', 'value': True, 'prob':
                        [{'field':'w', 'value': True, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'w', 'value': False, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [1]},
                                {'field':'r', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 's', 'value': False, 'prob':
                          [{'field': 'w', 'value': True, 'prob':
                              [{'field': 'c', 'value': True, 'prob':
                                  [{'field': 'r', 'value': True, 'prob': [1]},
                                   {'field': 'r', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'c', 'value': False, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [1]},
                                    {'field': 'r', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'w', 'value': False, 'prob':
                               [{'field': 'c', 'value': True, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [1]},
                                    {'field': 'r', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'c', 'value': False, 'prob':
                                    [{'field': 'r', 'value': True, 'prob': [1]},
                                     {'field': 'r', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('sp',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('co',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('cl',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('le',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])


g.add_prob_table('ar',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])

g.add_prob_table('st',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [1]},
                                {'field':'p', 'value': False, 'prob': [1]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [1]},
                                   {'field': 'p', 'value': False, 'prob': [1]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [1]},
                                    {'field': 'p', 'value': False, 'prob': [1]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [1]},
                                     {'field': 'p', 'value': False, 'prob': [1]}]
                                 }]
                            }]}])


#g.print_graph()
#g = graph.Graph()

ale_g = gibbs.Gibbs()
print(ale_g.gibbs_ask('a',{'s':True,'w':False},g,2))
