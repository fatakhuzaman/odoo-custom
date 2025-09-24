{
    "name": "My Complex Module",
    "version": "17.0.1.0.0",
    "summary": "Belajar custom modul dengan relasi, compute, dan security",
    "author": "Fatakhuzaman",
    "depends": ["base"],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/my_model_complex_view.xml",
        "views/my_submodel_complex_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}