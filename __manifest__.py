{
    "name": "RFC en mayusculas",
    "version": "1.0",
    "description": "Cambia el RFC del contacto a mayuscula.",
    "summary": "Cambia el RFC del contacto a mayuscula.",
    "author": "DGV",
    # 'website': '',
    "license": "LGPL-3",
    "category": "Contacts",
    "depends": ["contacts"],
    "auto_install": False,
    "application": False,
    "post_init_hook": "post_init_upper_vat",
}
