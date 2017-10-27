REG_URL = 'http://10.100.100.130:6001/v2'
REG_HOST = '10.100.100.130'
KEEP_COPIES = 30
IMG_MAP = {
    'opt/gray/nginx':10,
    'opt/gray/go-pay-service':15
}
SRV_MAP = {
    'env':['gray','test','dev'],
    'service':[
        'go-gateway',
        'go-mch-gateway',
        'go-service-order',
        'go-pay-service',
        'go-service-message',
        'go-service-shop',
        'go-gateway-pos-machine',
        'service-shop',
        'service-base',
        'service-qrcode',
        'service-message',
        'service-third-party',
        'service-third-party-interface',
        'service-merchant',
        'service-product',
        'service-pay',
        'gateway-boss',
        'gateway-app-merchant',
        'gateway-app-salesman',
        'frontend-h5-rest-shop',
        'frontend-pc-merchant',
        'frontend-h5-dinner',
        'frontend-pc-dinner',
        'boss-agent',
        'boss-base',
        'boss-data-center',
        'boss-web-admin'
    ]
}
