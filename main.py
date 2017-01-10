import graph
import gibbs

g = graph.Graph(['s','w','c','r','e','p','sp','co','cl','le','ar','st','m','a'],
[('s', 'e'),('s', 'p'),('w', 'e'),('w', 'p'),('c', 'e'),('c', 'p'),('r', 'e'),
('r', 'p'),('e', 'sp'),('e', 'co'),('e', 'cl'),('e', 'le'),('e', 'ar'),('e', 'st'),
('p', 'sp'),('p', 'co'),('p', 'cl'),('p', 'le'),('p', 'ar'),('p', 'st'),('m', 'sp'),
('m', 'co'),('m', 'cl'),('m', 'le'),('m', 'ar'),('m', 'st'),('a', 'sp'),('a', 'co'),
('a', 'cl'),('a', 'le'),('a', 'ar'),('a', 'st')])

g.add_prob_table('s',[{'field': 's', 'value': True, 'prob':[0.295180723]}])
g.add_prob_table('w',[{'field': 'w', 'value': True, 'prob':[0.081325301]}])
g.add_prob_table('c',[{'field': 'c', 'value': True, 'prob':[0.891566265]}])
g.add_prob_table('r',[{'field': 'r', 'value': True, 'prob':[0.638554217]}])
g.add_prob_table('m',[{'field': 'm', 'value': True, 'prob':[0.571]}])
g.add_prob_table('a',[{'field': 'a', 'value': True, 'prob':[0.519]}])
g.add_prob_table('e',[{'field': 's', 'value': True, 'prob':
                        [{'field':'w', 'value': True, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.007936507937]},
                                {'field':'r', 'value': False, 'prob': [0.0119047619]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.02380952381]},
                                {'field':'r', 'value': False, 'prob': [0.09523809524]}]
                            }]
                         },
                        {'field':'w', 'value': False, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.0119047619]},
                                {'field':'r', 'value': False, 'prob': [0.03571428571]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.05555555556]},
                                {'field':'r', 'value': False, 'prob': [0.1587301587]}]
                            }]
                        }]},
                      {'field': 's', 'value': False, 'prob':
                          [{'field': 'w', 'value': True, 'prob':
                              [{'field': 'c', 'value': True, 'prob':
                                  [{'field': 'r', 'value': True, 'prob': [0.02777777778]},
                                   {'field': 'r', 'value': False, 'prob': [0.02380952381]}]
                                },
                               {'field': 'c', 'value': False, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [0.09920634921]},
                                    {'field': 'r', 'value': False, 'prob': [0.1547619048]}]
                                }]
                            },
                           {'field': 'w', 'value': False, 'prob':
                               [{'field': 'c', 'value': True, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [0.03571428571]},
                                    {'field': 'r', 'value': False, 'prob': [0.01984126984]}]
                                 },
                                {'field': 'c', 'value': False, 'prob':
                                    [{'field': 'r', 'value': True, 'prob': [0.06746031746]},
                                     {'field': 'r', 'value': False, 'prob': [0.1706349206]}]
                                 }]
                            }]}])

g.add_prob_table('p',[{'field': 's', 'value': True, 'prob':
                        [{'field':'w', 'value': True, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.2301587302]},
                                {'field':'r', 'value': False, 'prob': [0.1428571429]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.02777777778]},
                                {'field':'r', 'value': False, 'prob': [0.1865079365]}]
                            }]
                         },
                        {'field':'w', 'value': False, 'prob':
                            [{'field':'c', 'value': True, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.05158730159]},
                                {'field':'r', 'value': False, 'prob': [0.05952380952]}]
                            },
                            {'field':'c', 'value': False, 'prob':
                                [{'field':'r', 'value': True, 'prob': [0.04761904762]},
                                {'field':'r', 'value': False, 'prob': [0.06746031746]}]
                            }]
                        }]},
                      {'field': 's', 'value': False, 'prob':
                          [{'field': 'w', 'value': True, 'prob':
                              [{'field': 'c', 'value': True, 'prob':
                                  [{'field': 'r', 'value': True, 'prob': [0.08333333333]},
                                   {'field': 'r', 'value': False, 'prob': [0.06349206349]}]
                                },
                               {'field': 'c', 'value': False, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [0.003968253968]},
                                    {'field': 'r', 'value': False, 'prob': [0.007936507937]}]
                                }]
                            },
                           {'field': 'w', 'value': False, 'prob':
                               [{'field': 'c', 'value': True, 'prob':
                                   [{'field': 'r', 'value': True, 'prob': [0.007936507937]},
                                    {'field': 'r', 'value': False, 'prob': [0]}]
                                 },
                                {'field': 'c', 'value': False, 'prob':
                                    [{'field': 'r', 'value': True, 'prob': [0]},
                                     {'field': 'r', 'value': False, 'prob': [0.01984126984]}]
                                 }]
                            }]}])

g.add_prob_table('sp',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.1443661972]},
                                {'field':'p', 'value': False, 'prob': [0.07394366197]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.04929577465]},
                                {'field':'p', 'value': False, 'prob': [0.04577464789]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.09507042254]},
                                {'field':'p', 'value': False, 'prob': [0.05281690141]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.03169014085]},
                                {'field':'p', 'value': False, 'prob': [0.03873239437]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.1056338028]},
                                   {'field': 'p', 'value': False, 'prob': [0.04225352113]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.0176056338]},
                                    {'field': 'p', 'value': False, 'prob': [0.02464788732]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.1443661972]},
                                    {'field': 'p', 'value': False, 'prob': [0.07394366197]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.02816901408]},
                                     {'field': 'p', 'value': False, 'prob': [0.03169014085]}]
                                 }]
                            }]}])

g.add_prob_table('co',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.1063829787]},
                                {'field':'p', 'value': False, 'prob': [0.01063829787]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.07446808511]},
                                {'field':'p', 'value': False, 'prob': [0.02127659574]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.06382978723]},
                                {'field':'p', 'value': False, 'prob': [0.01063829787]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.08510638298]},
                                {'field':'p', 'value': False, 'prob': [0.01063829787]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.1063829787]},
                                   {'field': 'p', 'value': False, 'prob': [0.04255319149]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.07446808511]},
                                    {'field': 'p', 'value': False, 'prob': [0.01063829787]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.2021276596]},
                                    {'field': 'p', 'value': False, 'prob': [0.02127659574]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.1276595745]},
                                     {'field': 'p', 'value': False, 'prob': [0.03191489362]}]
                                 }]
                            }]}])

g.add_prob_table('cl',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.1214953271]},
                                {'field':'p', 'value': False, 'prob': [0.03738317757]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.03738317757]},
                                {'field':'p', 'value': False, 'prob': [0.03738317757]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.07476635514]},
                                {'field':'p', 'value': False, 'prob': [0.01869158879]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.03738317757]},
                                {'field':'p', 'value': False, 'prob': [0.01869158879]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.1121495327]},
                                   {'field': 'p', 'value': False, 'prob': [0.05607476636]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.04672897196]},
                                    {'field': 'p', 'value': False, 'prob': [0.01869158879]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.214953271]},
                                    {'field': 'p', 'value': False, 'prob': [0.04672897196]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.08411214953]},
                                     {'field': 'p', 'value': False, 'prob': [0.03738317757]}]
                                 }]
                            }]}])

g.add_prob_table('le',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.09243697479]},
                                {'field':'p', 'value': False, 'prob': [0.03361344538]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.1176470588]},
                                {'field':'p', 'value': False, 'prob': [0.02941176471]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.05042016807]},
                                {'field':'p', 'value': False, 'prob': [0.02941176471]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.1008403361]},
                                {'field':'p', 'value': False, 'prob': [0.01680672269]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.07983193277]},
                                   {'field': 'p', 'value': False, 'prob': [0.03781512605]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.1638655462]},
                                    {'field': 'p', 'value': False, 'prob': [0.01260504202]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.04201680672]},
                                    {'field': 'p', 'value': False, 'prob': [0.02941176471]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.1554621849]},
                                     {'field': 'p', 'value': False, 'prob': [0.008403361345]}]
                                 }]
                            }]}])


g.add_prob_table('ar',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.06074766355]},
                                {'field':'p', 'value': False, 'prob': [0.04906542056]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.08177570093]},
                                {'field':'p', 'value': False, 'prob': [0.03504672897]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.06074766355]},
                                {'field':'p', 'value': False, 'prob': [0.03504672897]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.06074766355]},
                                {'field':'p', 'value': False, 'prob': [0.03037383178]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.1051401869]},
                                   {'field': 'p', 'value': False, 'prob': [0.04205607477]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.09579439252]},
                                    {'field': 'p', 'value': False, 'prob': [0.04906542056]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.08411214953]},
                                    {'field': 'p', 'value': False, 'prob': [0.04906542056]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.09112149533]},
                                     {'field': 'p', 'value': False, 'prob': [0.07009345794]}]
                                 }]
                            }]}])

g.add_prob_table('st',[{'field': 'm', 'value': True, 'prob':
                        [{'field':'a', 'value': True, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.03339191564]},
                                {'field':'p', 'value': False, 'prob': [0.05799648506]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.05799648506]},
                                {'field':'p', 'value': False, 'prob': [0.07732864675]}]
                            }]
                         },
                        {'field':'a', 'value': False, 'prob':
                            [{'field':'e', 'value': True, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.02460456942]},
                                {'field':'p', 'value': False, 'prob': [0.06678383128]}]
                            },
                            {'field':'e', 'value': False, 'prob':
                                [{'field':'p', 'value': True, 'prob': [0.04920913884]},
                                {'field':'p', 'value': False, 'prob': [0.06854130053]}]
                            }]
                        }]},
                      {'field': 'm', 'value': False, 'prob':
                          [{'field': 'a', 'value': True, 'prob':
                              [{'field': 'e', 'value': True, 'prob':
                                  [{'field': 'p', 'value': True, 'prob': [0.0158172232]},
                                   {'field': 'p', 'value': False, 'prob': [0.08787346221]}]
                                },
                               {'field': 'e', 'value': False, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.07029876977]},
                                    {'field': 'p', 'value': False, 'prob': [0.1054481547]}]
                                }]
                            },
                           {'field': 'a', 'value': False, 'prob':
                               [{'field': 'e', 'value': True, 'prob':
                                   [{'field': 'p', 'value': True, 'prob': [0.02811950791]},
                                    {'field': 'p', 'value': False, 'prob': [0.0913884007]}]
                                 },
                                {'field': 'e', 'value': False, 'prob':
                                    [{'field': 'p', 'value': True, 'prob': [0.06502636204]},
                                     {'field': 'p', 'value': False, 'prob': [0.1001757469]}]
                                 }]
                            }]}])


#g.print_graph()
#g = graph.Graph()

ale_g = gibbs.Gibbs()

#print('probability of sunny, given windy = False: ', ale_g.gibbs_ask('s',{'w':False},g,10))
#print('probability of energized, given windy = False: ', ale_g.gibbs_ask('e',{'w':False},g,10))
#print('probability of Sport, given windy = False: ', ale_g.gibbs_ask('sp',{'w':False},g,10))
#print('probability of Arts, given windy = True: ', ale_g.gibbs_ask('ar',{'w':True},g,10))
#print('probability of Cloudy, given windy = False and Energized = True: ', ale_g.gibbs_ask('c',{'w':False,'e':True},g,10))
#print('probability of Energized, given windy = False and sunny = True: ', ale_g.gibbs_ask('e',{'w':False,'s':False},g,10))


print(ale_g.formatted_result('e',{'s':True,'w':True,'c':True,'r':True},g,10))

#print(ale_g.formatted_result('e',{'s':True,'w':True,'c':True,'r':True},g,100))

#print(ale_g.formatted_result('e',{'s':True,'w':True,'c':True,'r':True},g,1000))
#print(ale_g.formatted_result('sp',{'s':True,'w':True,'m':False,'a':True},g,10))
