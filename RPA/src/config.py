# PATH DIRS
# ===================================================================================================
REPORT_FOLDER = './store/reports/'
UPLOAD_FOLDER = './store/uploads/'
MANAGER_FOLDER = './store/manager/'
DATA_ORIGIN_FOLDER = './store/origin/'

# ERRORS_MESSAGEM
# ===================================================================================================
ARGUMENTS_REQUIRED_ERROR_MSG = 'Os argumento [path] e [process] são requiridos!'
EXTENSION_INVALID_ERROR_MSG = 'Seu arquivo deve ser um csv compatíveis!'

# CONSTANTES
# ===================================================================================================
EXTENSION_EXPECTED = '.csv'
ALLOWED_EXTENSIONS = {'.csv'}

# LISTS
# ===================================================================================================
HEADER_COLUMNS = ['create-at', 'description', 'cnpj', 'amount', 'movement-status']
HEADER_TABLE_PENDING = ['create_at', 'name', 'woner', 'active']
HEADER_TABLE_PROCESSED = ['create_at', 'name', 'total_itens', 'size', 'woner', 'report_error', 'report_finish', 'report_sent'] 
