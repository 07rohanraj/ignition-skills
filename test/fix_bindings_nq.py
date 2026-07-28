import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path) as f:
    data = json.load(f)

# Named query paths
SAFETY_METRICS_NQ = "Safety/GetSafetyMetrics"
LINE_STATUS_NQ = "Safety/GetLineProductionStatus"

def update_bindings(node, path=''):
    if not isinstance(node, dict):
        return
    name = node.get('meta', {}).get('name', '')
    
    # Update Safety metric tag bindings to named queries
    if name == 'IncidentsValue':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": SAFETY_METRICS_NQ,
                        "mapping": "incidents_today"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {SAFETY_METRICS_NQ}')
    
    elif name == 'DaysValue':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": SAFETY_METRICS_NQ,
                        "mapping": "days_without_incident"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {SAFETY_METRICS_NQ}')
    
    elif name == 'NearMissValue':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": SAFETY_METRICS_NQ,
                        "mapping": "near_miss_count"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {SAFETY_METRICS_NQ}')
    
    # Update Gauge bindings
    elif name == 'Gauge_L1':
        node['propConfig'] = {
            "props.value": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "torque_compliance_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'Gauge_L2':
        node['propConfig'] = {
            "props.value": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "torque_compliance_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'Gauge_L3':
        node['propConfig'] = {
            "props.value": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "torque_compliance_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    # Update FlashRate labels
    elif name == 'FlashRate_L1':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "flashing_failure_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'FlashRate_L2':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "flashing_failure_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'FlashRate_L3':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "flashing_failure_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    # Update PaintRate labels
    elif name == 'PaintRate_L1':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "paint_rejection_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'PaintRate_L2':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "paint_rejection_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'PaintRate_L3':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "paint_rejection_rate"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    # Update LineStatus labels
    elif name == 'L1_FlashCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "units_flashed"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L1_FailCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "flashing_failures"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L1_TorqueInfo':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L1'",
                        "mapping": "torque_checks"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L2_FlashCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "units_flashed"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L2_FailCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "flashing_failures"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L2_TorqueInfo':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L2'",
                        "mapping": "torque_checks"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L3_FlashCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "units_flashed"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L3_FailCount':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "flashing_failures"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    elif name == 'L3_TorqueInfo':
        node['propConfig'] = {
            "props.text": {
                "binding": {
                    "config": {
                        "queryPath": LINE_STATUS_NQ,
                        "whereClause": "line = 'EV-L3'",
                        "mapping": "torque_checks"
                    },
                    "type": "namedQuery"
                }
            }
        }
        print(f'Fixed {name}: -> named query {LINE_STATUS_NQ}')
    
    for i, child in enumerate(node.get('children', [])):
        update_bindings(child, f'{path}/child[{i}]')

update_bindings(data['root'], 'root')

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
print('\nAll bindings updated to named queries.')
