#payloads.py
"""
Payloads Controller
"""

import tms.models as m

def list():
    """
    List payloads
    """
    # some logic for listing based on who is logged in
    # but for now i'll just pull the only broker in the schema
    broker = m.Broker.get_by_id(545)

    payloads = m.Payload.all().filter('broker =', broker).filter('delivered_at =', None)
    return payloads
