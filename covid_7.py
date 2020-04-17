#!/bin/python3


status = ['code', 'program', 'script', 'accuracy', 'function', 'static', 'concurrency', 'fault tolerance']
match = ['error', 'index', 'method', 'stack', 'chunk', 'function', 'handler', 'bugs']

for coke in status:
  if coke not in match:
    print("List of items not present in match category :-- ",coke)
