# maze topology

import sys
sys.path.append('D:\cognate')
import cognate.knowledge2 as cog

k = cog.KnowledgeStack()
k.append( cog.Path('start', 'junction') )
k.append( cog.Path('junction', 'start') )
k.append( cog.Path('junction', 'path_a') )
k.append( cog.Path('path_a', 'junction') )
k.append( cog.Path('junction', 'path_b') )
k.append( cog.Path('path_b', 'junction') )
k.append( cog.Path('junction', 'path_c') )
k.append( cog.Path('path_c', 'junction') )
k.append( cog.Path('trigger_a', 'trigger_b') )
k.append( cog.Path('trigger_b', 'trigger_a') )
k.append( cog.Path('path_a', 'trigger_a') )
k.append( cog.Path('trigger_a', 'path_a') )
k.append( cog.ClosedGate('path_a', 'trigger_a') )
k.append( cog.ClosedGate('trigger_a', 'path_a') )
k.append( cog.Trigger('path_a', 'trigger_a', 'junction') )
k.append( cog.Trigger('trigger_a', 'path_a', 'junction') )
k.append( cog.Path('path_b', 'path_b1') )
k.append( cog.Path('path_b1', 'path_b') )
k.append( cog.Path('path_b1', 'path_b2') )
k.append( cog.Path('path_b2', 'path_b1') )
k.append( cog.ClosedGate('path_b1', 'path_b2') )
k.append( cog.ClosedGate('path_b2', 'path_b1') )
k.append( cog.Trigger('path_b1', 'path_b2', 'trigger_b') )
k.append( cog.Trigger('path_b2', 'path_b1', 'trigger_b') )
k.append( cog.Path('path_b2', 'path_b3') )
k.append( cog.Path('path_b3', 'path_b2') )
k.append( cog.Path('path_b3', 'end') )
k.append( cog.Path('end', 'path_b3') )
k.append( cog.ClosedGate('path_b3', 'end') )
k.append( cog.ClosedGate('end', 'path_b3') )
k.append( cog.Trigger('path_b3', 'end', 'trigger_c') )
k.append( cog.Trigger('end', 'path_b3', 'trigger_c') )
k.append( cog.Path('path_c', 'trigger_c') )
k.append( cog.Path('trigger_c', 'path_c') )
