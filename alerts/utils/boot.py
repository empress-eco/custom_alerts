# Alerts © 2024
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


# [Hooks]
def extend(bootinfo):
    import frappe
    
    user = frappe.session.user
    try:
        from .alert import get_alerts_cache
        
        alerts = get_alerts_cache(user)
        if alerts:
            bootinfo.alerts = alerts
    except Exception:
        from frappe import _
        
        from .common import log_error
        
        log_error(_(
            "An error has occurred while getting "
            + "cached alerts on boot of user \"{0}\"."
        ).format(user))
