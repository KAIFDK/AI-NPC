"""
Audio compatibility module for Python 3.14+
Provides mock modules for deprecated audio libraries
"""

import sys
import types

# Create mock modules for deprecated audio libraries
def setup_audio_compat():
    """Setup compatibility modules for Python 3.14+"""
    
    # Mock aifc module
    if 'aifc' not in sys.modules:
        aifc = types.ModuleType('aifc')
        sys.modules['aifc'] = aifc
    
    # Mock audioop module
    if 'audioop' not in sys.modules:
        audioop = types.ModuleType('audioop')
        sys.modules['audioop'] = audioop
    
    # Mock wave module helpers if needed
    if 'sunau' not in sys.modules:
        sunau = types.ModuleType('sunau')
        sys.modules['sunau'] = sunau

setup_audio_compat()
