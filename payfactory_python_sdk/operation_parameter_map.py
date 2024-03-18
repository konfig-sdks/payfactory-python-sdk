operation_parameter_map = {
    '/v1/Application/Submit-POST': {
        'parameters': [
            {
                'name': 'isvName'
            },
            {
                'name': 'businessDetails'
            },
            {
                'name': 'customerServiceContact'
            },
            {
                'name': 'riskContact'
            },
            {
                'name': 'businessContact'
            },
            {
                'name': 'processingDetails'
            },
            {
                'name': 'bankDetails'
            },
            {
                'name': 'pricingStructure'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'owners'
            },
        ]
    },
    '/v1/Application/Details/{appId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/Application/Status/{appId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/Application/Delete/{appId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/Application/StartUnderwriting/{appId}-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/ApplicationForm/session-POST': {
        'parameters': [
            {
                'name': 'signer'
            },
            {
                'name': 'companyName'
            },
            {
                'name': 'redirectUrl'
            },
            {
                'name': 'completeUrl'
            },
            {
                'name': 'refreshUrl'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'pricingPlanId'
            },
            {
                'name': 'businessDetails'
            },
        ]
    },
    '/v1/ApplicationForm/session/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/v1/ApplicationForm/session/{sessionId}-PUT': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/v1/Document/Upload/{type}/{appId}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'Document'
            },
        ]
    },
    '/v1/Reporting/AchTransactions/{referenceId}-GET': {
        'parameters': [
            {
                'name': 'referenceId'
            },
        ]
    },
    '/v1/Reporting/Deposits-GET': {
        'parameters': [
        ]
    },
    '/v1/Reporting/Deposits/{numberOfDeposits}-GET': {
        'parameters': [
            {
                'name': 'numberOfDeposits'
            },
        ]
    },
    '/v1/Reporting/Deposits/{referenceId}-GET': {
        'parameters': [
            {
                'name': 'referenceId'
            },
        ]
    },
    '/v1/Transaction/Metadata-POST': {
        'parameters': [
            {
                'name': 'transactionId'
            },
            {
                'name': 'merchantId'
            },
            {
                'name': 'cardHolderName'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'orderId'
            },
            {
                'name': 'partnerFee'
            },
            {
                'name': 'itemCount'
            },
        ]
    },
    '/v1/Transaction/MetadataBulk-POST': {
        'parameters': [
        ]
    },
};