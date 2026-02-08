'''
import myclient as mc
print([x for x in mc.__dict__ if (x[:2] != '__' and x[:5] != 'class')])
'''
import myclient
print([x for x in myclient.__dict__ if (x[:2] != '__' and x[:5] != 'class')])