{
    'name': 'Payment Provider: Xendit',
    'version': '0.1',
    'category': 'Accounting/Payment Providers',
    'summary': "A payment provider for Indonesian Localization",
    'depends': ['payment'],
    'data': [
        "data/payment_provider_data.xml",
        "views/payment_provider_views.xml",
    ],
    'installable' : False,
    'application': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            'payment_xendit/static/src/js/payment_form.js',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}


